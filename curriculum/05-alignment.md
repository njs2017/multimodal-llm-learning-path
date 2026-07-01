# 05 - Multimodal Instruction Tuning and Alignment

## Core question

How do we make a multimodal model helpful, honest, grounded, and safe?

## Visual instruction tuning

LLaVA popularized a practical recipe:

1. Use a vision encoder.
2. Connect it to an LLM with a projector.
3. Generate or collect image-instruction-answer triples.
4. Fine-tune the model to answer user instructions about images.

This converts “captioning ability” into “assistant behavior.”

## Preference alignment for VLMs

After SFT, models may still:

- Hallucinate visual details.
- Over-answer when evidence is missing.
- Ignore the image and rely on priors.
- Lose some text-only instruction-following quality.
- Fail safety policies on images.

Preference alignment uses chosen/rejected responses to improve behavior.

Methods to study:

- DPO for VLMs
- RLHF for VLMs
- RLAIF for multimodal feedback
- Rejection sampling
- GRPO-style reasoning alignment for VLMs

## What makes VLM alignment different from text alignment?

The preference is conditioned on both prompt and visual/audio input:

```text
preference = f(image, prompt, chosen_response, rejected_response)
```

A rejected answer can be fluent and safe but visually wrong.

Example:

Prompt: “What number is shown on the sign?”

- Chosen: “The sign appears to show 47.”
- Rejected: “The sign shows 42.”

The difference depends on reading the image correctly, not just language quality.

## Hallucination-specific alignment

Useful preference patterns:

- Reward “not visible / cannot determine” when appropriate.
- Penalize invented objects, text, colors, counts, and spatial relations.
- Require evidence-based wording.
- Prefer uncertainty when resolution is low.

## Output artifact

Design 20 multimodal preference examples:

- 5 OCR
- 5 object/spatial
- 5 chart/document
- 5 safety/uncertainty

For each: image description, prompt, chosen answer, rejected answer, why chosen is better.
