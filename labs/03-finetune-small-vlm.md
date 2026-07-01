# Lab 03 - Fine-tune a Small VLM

## Goal

Run a small, controlled fine-tuning experiment so you understand VLM post-training tradeoffs.

## Recommended task

Structured extraction from images.

Examples:

- Food image -> JSON tags
- Receipt image -> JSON fields
- Screenshot -> UI state summary
- Chart -> answer with value and evidence

## Dataset format

Use JSONL:

```jsonl
{"image":"images/001.jpg","messages":[{"role":"user","content":"Extract the visible food items as JSON."},{"role":"assistant","content":"{\"items\":[\"pizza\",\"salad\"]}"}]}
```

## Training options

### Option A - No training, just eval

Use an API or local VLM and evaluate prompts.

### Option B - LoRA / QLoRA

Fine-tune a small open VLM with PEFT.

### Option C - Full fine-tune small model

Only if the model is small enough and you have sufficient GPU memory.

## Track before/after

Use the same eval set before and after training:

- Exact JSON validity
- Field accuracy
- Hallucinated fields
- OCR correctness
- Refusal/uncertainty behavior
- Text-only capability regression

## Common failure modes

- Model overfits output format but ignores image.
- JSON becomes valid but values are hallucinated.
- Fine-tuning improves target task but hurts general VQA.
- Synthetic labels contain errors that become learned behavior.

## Suggested resources

- Hugging Face VLM fine-tuning tutorial:  
  <https://www.learnhuggingface.com/notebooks/hugging_face_vlm_fine_tune_tutorial>
- Hugging Face VLM overview:  
  <https://huggingface.co/blog/vlms>
- TRL VLM alignment:  
  <https://huggingface.co/blog/trl-vlm-alignment>

## Deliverable

Create:

- `experiments/vlm-finetune-config.yaml`
- `experiments/before-after-eval.md`
- `experiments/error-analysis.md`
