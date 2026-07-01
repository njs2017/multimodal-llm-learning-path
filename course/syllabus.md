# Course Syllabus: Multimodal Models for Newcomers

## Course promise

This course takes you from “I know LLMs exist” to “I can explain, evaluate, and prototype simple multimodal systems.”

It intentionally starts with intuition before math and papers.

## Who this is for

- Engineers new to multimodal AI
- Product builders who need to evaluate VLMs
- Researchers entering VLM/MLLM literature
- AI-agent builders who want models that can see screens, documents, and charts

## Prerequisites

Helpful but not required:

- Basic Python
- Basic LLM concepts: prompt, token, embedding
- Basic ML concepts: training, inference, dataset

If you are missing these, still start with `START_HERE.md`.

## Learning outcomes

By the end, you should be able to:

1. Explain what modalities are and why they are hard to combine.
2. Explain CLIP-style contrastive image-text learning.
3. Explain how VLMs connect a vision encoder to an LLM.
4. Distinguish captioning, VQA, OCR, grounding, chart QA, and video understanding.
5. Explain connector alignment, instruction tuning, and preference alignment.
6. Build a small CLIP retrieval or zero-shot classification demo.
7. Build a small VLM evaluation set.
8. Read a VLM paper using an architecture/data/eval checklist.
9. Recognize hallucination and grounding failures.
10. Choose a realistic capstone project.

## Course structure

| Week | Topic | Main artifact |
|---:|---|---|
| 0 | Orientation and vocabulary | Concept map |
| 1 | Modalities, embeddings, and CLIP | CLIP notes + zero-shot demo |
| 2 | From CLIP to VLMs | Architecture diagram |
| 3 | LLaVA, BLIP-2, Flamingo | Model comparison table |
| 4 | Training pipeline | Training-stage diagram |
| 5 | Data and evaluation | Mini benchmark JSONL |
| 6 | Hallucination, grounding, and safety | Failure taxonomy |
| 7 | Audio, video, documents, and agents | System design |
| 8 | Capstone | Final project report |

## Grading yourself

This is a self-study course. Use the checkpoints:

- Can you explain the concept without jargon?
- Can you draw the architecture?
- Can you name what data is needed?
- Can you define a failure mode?
- Can you test it with a small example?

## Recommended order

1. `START_HERE.md`
2. `course/week-00-orientation.md`
3. `course/week-01-clip-and-embeddings.md`
4. `course/week-02-vlm-architecture.md`
5. `course/week-03-model-families.md`
6. `course/week-04-training-pipeline.md`
7. `course/week-05-evaluation.md`
8. `course/week-06-failures-and-safety.md`
9. `course/week-07-beyond-images.md`
10. `course/week-08-capstone.md`
