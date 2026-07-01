# Lab 01 - CLIP Retrieval

## Goal

Understand the difference between **cross-modal retrieval** and **multimodal reasoning**.

## Build

Create a small script or notebook that:

1. Loads a CLIP/SigLIP model from Hugging Face or OpenCLIP.
2. Collects 20 images.
3. Writes 30 candidate captions.
4. Embeds images and captions.
5. Computes image-to-text and text-to-image retrieval.
6. Prints top-k matches.

## Suggested stack

- `transformers` or `open_clip_torch`
- `torch`
- `PIL`
- `numpy`
- Optional: `faiss-cpu` for retrieval

## Experiments

### Easy positives

Use captions that directly describe the image.

### Hard negatives

Add captions with:

- Same object, different color
- Same scene, different count
- Same action, different actor
- Similar words but wrong visual content

### Ambiguity test

Use captions where the image alone is insufficient.

Example:

```text
Image: a person standing near a car
Caption A: a taxi driver is waiting
Caption B: a person is standing near a car
```

CLIP may prefer plausible but ungrounded captions.

## Questions to answer

- When does CLIP succeed?
- When does it confuse semantics with exact visual detail?
- Can it count?
- Can it read text?
- Can it reason about diagrams?
- Why is CLIP useful but insufficient for chat-style VLMs?

## Deliverable

Create `experiments/clip-retrieval-report.md` with:

- Setup
- Example results
- Failure cases
- Key lesson: retrieval alignment is not full multimodal reasoning
