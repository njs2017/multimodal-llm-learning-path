# 08 - Projects

## Goal

Move from reading to building.

Choose one beginner, one intermediate, and one advanced project.

## Beginner

### Project 1 - CLIP retrieval demo

Build image-text retrieval with a public CLIP/SigLIP model.

Deliverables:

- Notebook/script
- 20 image/caption examples
- Success/failure analysis

### Project 2 - VLM prompt lab

Compare 3 open/source or API VLMs on the same 30 prompts.

Deliverables:

- Prompt set
- Outputs
- Manual scoring rubric
- Failure taxonomy

## Intermediate

### Project 3 - Mini visual instruction dataset

Create 100 examples across OCR, charts, screenshots, objects, and spatial reasoning.

Deliverables:

- JSONL dataset
- Data card
- Quality checklist

### Project 4 - Fine-tune an open VLM with LoRA

Fine-tune a small VLM on your mini dataset.

Deliverables:

- Training config
- Before/after eval
- Notes on overfitting and language degradation

### Project 5 - Hallucination eval harness

Build a small evaluator that checks whether answers mention objects not present in the image.

Deliverables:

- Dataset
- Model outputs
- Manual labels
- Error report

## Advanced

### Project 6 - Document QA assistant

Build a pipeline for visual document QA.

Components:

- Page rendering
- OCR or VLM page understanding
- Retrieval over pages
- Answer generation with citations
- Eval set

### Project 7 - Multimodal browser/screen agent

Build an agent loop:

```text
screenshot -> VLM -> action -> browser/UI -> new screenshot -> verification
```

Deliverables:

- Task set
- Action schema
- Safety constraints
- Success/failure analysis

### Project 8 - Preference dataset and DPO experiment

Create a small chosen/rejected multimodal dataset and run or simulate DPO-style post-training.

Deliverables:

- Preference data card
- Training notes
- Before/after eval
- Analysis of over-optimization risks
