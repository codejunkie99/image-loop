# Control dictionary

Show the compact menu first. Expand only the selected control. Questions below are options, not a form to exhaust.

| Category | Properties to inspect or edit | Useful question |
| --- | --- | --- |
| Text content | Exact transcript, language, capitalization, punctuation, line breaks, alignment with labels | “Keep the words, or replace them?” |
| Typography | Serif/sans/script/monospace, candidate family, weight, size, width, tracking, leading, case, outline, shadow, hierarchy | “Thinner, bolder, more compact, or closer to the reference?” |
| Local color | Fill, stroke, semantic palette role, gradient stops/direction, opacity | “Which element changes color? Do you have a swatch or hex code?” |
| Layers and depth | Front/back order, overlap, containment, occlusion, grouping, shadow relationships, inferred blend mode | “Should it sit in front of or behind the subject?” |
| Color grading | White balance, tint, contrast, black/white points, shadow/midtone/highlight treatment, saturation, vibrance, grain, vignette | “Change the whole picture's mood or only the photo area?” |
| Picture type / medium | Photograph, 2D illustration, vector-style art, 3D render, diagram, chart, screenshot/UI, collage, mixed media | “Keep it photographic, or change the medium?” |
| Composition | Position, scale, visual hierarchy, grid, margins, alignment, whitespace, balance, reading order | “What should people notice first?” |
| Framing / geometry | Crop, aspect ratio, orientation, perspective, lens appearance, full subject visibility, horizon | “Crop, pad, or extend the background to fit?” |
| Lighting | Direction, softness, intensity, key/fill/rim light, cast/contact shadows, catchlights, reflections | “Same lighting, or a different time of day/studio setup?” |
| Material / texture | Paper, glass, metal, plastic, skin, fabric, grain, roughness, gloss, wear | “Which surface should change, and what should it feel like?” |
| Identity / product | Facial features, pose, expression, hands, silhouette, proportions, packaging, label, logo | “Which identifying details must stay?” |
| Diagram / chart semantics | Node counts, labels, connections, arrow direction, feedback loops, grouping, units, values, legend | “Is this a visual restyle or a change to the information?” |
| Output | Exact width/height, format, transparency, file size, intended display size, color profile when relevant | “Where will this be displayed, and at what size?” |

Keep asset purpose separate from medium: an advertisement can be a photograph, a 3D render, or an illustration. Keep visual style separate too: “editorial,” “minimal,” and “cinematic” describe treatments, not file formats or proven production methods.

Typography: exact font names require source files, metadata, or other corroboration. With pixels alone, describe letterforms and give explicitly labeled candidates. Estimate sizes relative to canvas height; do not claim original point sizes from an unknown display scale. Preserve exact line breaks when specified. A font change may alter wrapping; resolve a real conflict between font size and locked text box before changing the layout.

Color: label whether a hex value was sampled from decoded pixels or visually estimated. Samples from compressed/graded images do not establish original brand tokens. Grading describes the overall look; do not claim to recover exact editor sliders, camera settings, or a LUT from the finished image. Keep palette changes separate from global grading, especially when logos, skin, or product colors are locked.

Layer: a flattened image supports an inferred visual stack, not recovery of a PSD, SVG, or original layer names. Visible fragments are not complete hidden assets. Rebuilding editable layers is a separate task. Global changes can affect several layers even if the user named only one element; identify that conflict before proceeding.

Picture type: include a primary medium and regional exceptions, e.g. “photograph with overlaid vector-style text.” Do not claim an image is a real photograph, AI-generated, or authored by a named person based solely on visual style.

Accessibility: numbers and names work without distinguishing badge colors. Provide an accessible text legend. Check small text at intended viewing size, contrast, overcrowded arrows, and whether cropping hides essential content. Do not claim a formal contrast ratio unless measured.

Optional advanced controls: repeatable character/product references; per-property locks; shared style tokens across a batch; safe areas for different crops; localized text expansion; transparent edges; print bleed and color profiles when the job calls for print. Offer these when relevant, not as mandatory onboarding questions.
