# 08 - First Projects for Newcomers

These projects are intentionally small. Do not start by training a large model.

## Project 1 - Try a vision model manually

Use ChatGPT/Gemini/Claude vision or an open VLM demo.

Test 20 prompts:

- 5 normal photos
- 5 screenshots
- 5 charts/documents
- 5 ambiguous or hard images

Record:

- Correct answer
- Wrong answer
- Hallucination
- Uncertainty behavior

Deliverable:

```text
experiments/manual-vlm-test.md
```

## Project 2 - CLIP image search

Use CLIP to search images using text.

Example:

```text
Query: "a dog on grass"
Return: top 5 matching images
```

Goal:

Understand embeddings and retrieval.

Use:

- `labs/01-clip-retrieval.md`

## Project 3 - Build a mini benchmark

Create 30 examples:

- Image path
- Prompt
- Expected answer
- Failure modes

Goal:

Learn evaluation before training.

Use:

- `labs/04-vlm-evaluation-harness.md`

## Project 4 - Compare 3 models

Run the same prompts on:

- One frontier API model
- One open model
- One smaller/local model if available

Compare:

- OCR
- Counting
- Chart reasoning
- Hallucination
- Latency
- Cost

## Project 5 - Tiny visual instruction dataset

Create 50 examples:

```text
image + question -> answer
```

Categories:

- 10 captions
- 10 OCR
- 10 charts
- 10 screenshots
- 10 ambiguous/uncertain

Do not fine-tune yet. First inspect data quality.

## Project 6 - Screenshot assistant prototype

Input:

- Screenshot
- User goal

Output:

- Explanation of what to click
- Confidence
- Safety warning if destructive

Goal:

Understand why multimodal agents need verification.

## Recommended order

1. Manual VLM testing
2. CLIP retrieval
3. Mini benchmark
4. Model comparison
5. Tiny instruction dataset
6. Screenshot assistant
