# Lab 04 - VLM Evaluation Harness

## Goal

Build a small evaluation harness that catches real multimodal failures.

## Dataset split

Create at least 60 examples:

- 10 object recognition
- 10 counting
- 10 OCR
- 10 charts/tables
- 10 screenshots/UI
- 10 ambiguous/insufficient evidence

## JSONL schema

```jsonl
{
  "id": "ocr_001",
  "image": "images/ocr_001.png",
  "prompt": "What number is shown on the sign?",
  "expected": "47",
  "acceptable": ["47", "It appears to be 47"],
  "must_not_include": ["42", "definitely if image is blurry"],
  "skill": "ocr",
  "rubric": {
    "correct": 1,
    "uncertain_but_honest": 0.5,
    "hallucinated": 0
  }
}
```

## Scoring dimensions

- Answer correctness
- Evidence use
- Calibration/uncertainty
- Hallucination
- Format following
- Safety/refusal behavior when applicable

## Important trick

Include **unanswerable** examples.

A good VLM should sometimes say:

```text
I cannot determine that from the image.
```

If your benchmark only rewards answering, you will train overconfident hallucination.

## Deliverable

Create a report:

```text
Model | Overall | OCR | Counting | Chart | Screenshot | Unanswerable | Hallucination rate
```

Then write the top 10 failure patterns.
