# Capstone Projects

Choose one capstone depending on your goal.

## Capstone A - Explain VLMs visually

Deliverable: a 10-page illustrated explainer.

Must include:

- CLIP
- Vision encoder -> connector -> LLM
- LLaVA-style training
- Evaluation and hallucination
- One diagram per concept

## Capstone B - CLIP image search app

Deliverable: a small app or notebook.

Must include:

- Image folder
- Text query
- Top-k retrieval
- Failure examples
- Short report explaining why retrieval is not reasoning

## Capstone C - VLM model comparison

Deliverable: model comparison report.

Test 3 models on 50 examples:

- photos
- OCR
- charts
- screenshots
- ambiguous examples

Report:

```text
Model | Accuracy | Hallucination rate | Honest uncertainty | Latency | Notes
```

## Capstone D - Screenshot assistant prototype

Deliverable: a prototype that takes a screenshot + goal and returns:

- UI element to click
- reason
- confidence
- safety warning
- verification step

## Capstone E - Mini visual instruction dataset

Deliverable: 100 examples with data card.

Categories:

- captions
- OCR
- chart QA
- screenshots
- spatial reasoning
- unanswerable examples

## Final report template

```md
# Capstone title

## Problem
## Modalities
## Architecture
## Data
## Evaluation
## Results
## Failure analysis
## Safety/limitations
## What I would improve next
```
