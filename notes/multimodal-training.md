# Multimodal Training Notes

## High-level formula

A multimodal training example usually contains:

```text
modal inputs + text prompt -> target response/action
```

For image chat:

```text
(image, prompt) -> answer
```

For preference alignment:

```text
(image, prompt, chosen_answer, rejected_answer)
```

For grounding:

```text
(image, referring_expression) -> bounding_box / mask / region description
```

For video:

```text
(video frames + optional audio, prompt) -> temporal answer
```

## Losses

### Contrastive loss

Used for image-text alignment and retrieval.

### Next-token prediction

Used when visual tokens condition an autoregressive LLM response.

### Matching / classification losses

Used in older VLM tasks or auxiliary objectives.

### Box/mask losses

Used when grounding outputs include locations.

### Preference losses

Used in DPO/RLHF-style alignment.

## Freezing strategy

Common practical recipe:

1. Freeze LLM and vision encoder.
2. Train connector on caption-style data.
3. Fine-tune connector + LoRA on LLM with instruction data.
4. Optionally unfreeze selected vision/LLM layers for high-quality runs.
5. Run preference alignment and safety tuning.

## Data mixture strategy

Balance data across capabilities:

- General image understanding
- Fine-grained OCR
- Charts/tables
- Screenshots/UI
- Spatial reasoning
- Multi-image comparison
- Safety/refusal
- Text-only retention

Always include text-only or mixed text data if you care about preserving base LLM ability.

## Practical compute tiers

### Laptop / small GPU

- Use API models or small VLM inference.
- Build evals and datasets.
- Fine-tune tiny models if possible.

### Single strong GPU

- LoRA fine-tune small VLMs.
- Evaluate open VLMs.
- Run document/screenshot prototypes.

### Multi-GPU

- Connector pretraining.
- Larger SFT.
- Preference alignment experiments.

### Large lab

- Pretrain native multimodal backbones.
- Train any-to-any systems.
- Large-scale safety and preference pipelines.
