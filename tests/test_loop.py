import copy
import importlib.util
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/image-loop/scripts'))
from controller import decide, repair_prompt
from review import check_file


class LoopTests(unittest.TestCase):
    def setUp(self):
        self.brief = {'intent':'Make the bottle blue.', 'criteria':[
            {'id':'color','target':'bottle','kind':'requested','requirement':'Bottle is blue.'},
            {'id':'text','target':'headline','kind':'protected','requirement':'Keep exact headline.'}],
            'file_checks':{'width':1,'height':1,'format':'PNG','alpha_required':False}}
        self.report = {'criteria':[{'id':i,'status':'pass','evidence':'Visible evidence.','suggested_fix':''}
                                    for i in ['color','text']], 'summary':'Checked.'}
        self.checks = {'passed':True,'failures':[]}

    def test_accept_complete_pass(self):
        self.assertEqual(decide(self.brief,self.report,self.checks)['action'],'accepted_by_checks')

    def test_missing_duplicate_or_extra_ids_cannot_pass(self):
        for ids in [['color'],['color','color'],['color','text','invented']]:
            r=copy.deepcopy(self.report)
            r['criteria']=[dict(r['criteria'][0],id=i) for i in ids]
            self.assertEqual(decide(self.brief,r,self.checks)['action'],'stop_invalid_review')

    def test_uncertainty_escalates(self):
        self.report['criteria'][1]['status']='uncertain'
        self.assertEqual(decide(self.brief,self.report,self.checks)['action'],'escalate')

    def test_protected_failure_requires_repair(self):
        self.report['criteria'][1]['status']='fail'
        d=decide(self.brief,self.report,self.checks)
        self.assertEqual(d['action'],'repair')
        self.assertEqual(d['protected_failed'],['text'])
        self.assertIn('Keep exact headline.',repair_prompt(self.brief,self.report,d))

    def test_budget_stops(self):
        self.report['criteria'][0]['status']='fail'
        self.assertEqual(decide(self.brief,self.report,self.checks,3,3)['action'],'stop_budget')

    def test_repeated_failure_stops(self):
        self.report['criteria'][0]['status']='fail'
        self.assertEqual(decide(self.brief,self.report,self.checks,1,3,self.report)['action'],'escalate')

    def test_improving_failure_set_can_continue(self):
        previous=copy.deepcopy(self.report)
        for c in previous['criteria']:c['status']='fail'
        self.report['criteria'][0]['status']='fail'
        self.assertEqual(decide(self.brief,self.report,self.checks,1,3,previous)['action'],'repair')

    def test_file_failure_blocks_acceptance(self):
        self.assertEqual(decide(self.brief,self.report,{'passed':False,'failures':['wrong size']})['action'],'stop_file_checks')

    def test_file_decode_and_alpha(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'fixture.png'
            Image.new('RGBA',(1,1),(0,0,0,255)).save(p)
            expected=dict(self.brief['file_checks'],alpha_required=True)
            self.assertFalse(check_file(p,expected)['passed'])
            Image.new('RGBA',(1,1),(0,0,0,0)).save(p)
            self.assertTrue(check_file(p,expected)['passed'])
            self.assertFalse(check_file(p,dict(expected,width=2))['passed'])

    def test_installer_refuses_overwrite(self):
        spec=importlib.util.spec_from_file_location('installer',ROOT/'scripts/install.py')
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'skills'
            m.install(ROOT/'skills',dest)
            marker=dest/'image-loop/keep.txt';marker.write_text('user work')
            with self.assertRaises(FileExistsError):m.install(ROOT/'skills',dest)
            self.assertEqual(marker.read_text(),'user work')
            with self.assertRaises(ValueError):m.install(ROOT/'skills',ROOT/'skills',replace=True)

    def test_extraction_dimension_guard(self):
        script=ROOT/'skills/image-edit-map/scripts/validate_spec.py'
        image=ROOT/'examples/product/source.png'
        for filename, expected in [('raw-extraction.json',1),('image-spec.json',0)]:
            result=subprocess.run([sys.executable,str(script),str(ROOT/'examples/reverse-engineer'/filename),
                                   '--image',str(image)],capture_output=True,text=True)
            self.assertEqual(result.returncode,expected,result.stdout+result.stderr)

    def test_protected_review_needs_source_before_model_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'review'
            result=subprocess.run([sys.executable,str(ROOT/'skills/image-loop/scripts/review.py'),
                                   '--brief',str(ROOT/'examples/product/brief.json'),
                                   '--candidate',str(ROOT/'examples/product/source.png'),
                                   '--out',str(out),'--model','not-a-model'],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            self.assertIn('Protected comparison criteria require --source',result.stderr)
            self.assertFalse(out.exists())


if __name__ == '__main__':
    unittest.main()
