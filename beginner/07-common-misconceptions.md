# 07 - Common Misconceptions

## Misconception 1: “The model sees like a human”

It does not.

Images are converted into patches, embeddings, or tokens. The model processes numerical representations.

That can work very well, but it is not the same as human perception.

## Misconception 2: “If it can describe an image, it understands it”

Description is easier than grounded reasoning.

A model may generate a plausible caption while still failing:

- Counting
- Reading text
- Identifying exact positions
- Explaining charts
- Comparing two images
- Knowing when evidence is insufficient

## Misconception 3: “OCR is solved”

OCR is much better than before, but still difficult when text is:

- Small
- Blurry
- Rotated
- Handwritten
- Low contrast
- Embedded in a complex layout
- Mixed with charts or tables

## Misconception 4: “More modalities always means better”

More modalities add complexity.

A weak video model may perform worse than a strong image model plus good frame selection.

A multimodal system is only useful if the model is trained and evaluated for the target task.

## Misconception 5: “A high benchmark score means it will work in my product”

Benchmarks are useful, but real data may differ.

Always test on your own:

- Screenshots
- Documents
- Charts
- User photos
- Failure cases
- Ambiguous examples

## Misconception 6: “The LLM does all the work”

The LLM is important, but the system also depends on:

- Vision encoder quality
- Connector quality
- Visual token budget
- Training data mixture
- OCR/document data
- Evaluation and prompting

## Misconception 7: “Hallucination is only a language problem”

Multimodal hallucination can mean:

- Inventing objects not in the image
- Reading text incorrectly
- Claiming a chart trend that is not present
- Assuming context from prior knowledge
- Describing hidden regions
- Overstating confidence from low-resolution evidence

## Misconception 8: “Video is just many images”

Video adds time.

The model must understand:

- Order
- Motion
- Cause and effect
- Events
- State changes
- Audio-video synchronization

Sampling a few frames may miss the important moment.

## Key takeaway

Treat multimodal models as powerful but imperfect perception-and-language systems. Always test grounding, uncertainty, and task-specific behavior.
