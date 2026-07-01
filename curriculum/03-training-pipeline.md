# 03 - Multimodal Training Pipeline

## Core question

How are multimodal LLMs trained?

## Stage 0 - Choose or train unimodal backbones

Most practical systems reuse:

- A pretrained LLM.
- A pretrained vision encoder such as CLIP/SigLIP/ViT/EVA-CLIP.
- Optional audio encoder, video encoder, document OCR pipeline, or tokenizer.

Decision: freeze or fine-tune?

- Freeze to reduce compute and preserve capability.
- Fine-tune for better modality-specific performance.
- Use LoRA/QLoRA when full fine-tuning is too expensive.

## Stage 1 - Modality alignment / connector pretraining

Goal: map modality features into the LLM's embedding space.

Common losses/tasks:

- Image captioning loss
- Image-text matching
- Contrastive loss
- Next-token prediction on captions
- Region/grounding objectives

Common trainable components:

- Linear projector / MLP projector
- Q-Former / query transformer
- Perceiver resampler
- Cross-attention adapter

## Stage 2 - Multimodal instruction tuning

Goal: teach the model to answer instructions involving non-text input.

Data examples:

- Image + question -> answer
- Image + instruction -> detailed description
- Chart + question -> numerical answer
- Screenshot + task -> UI instruction
- Document page + question -> grounded answer
- Video clip + question -> temporal answer

Important distinction:

- Captioning teaches “describe this.”
- Instruction tuning teaches “follow this user request using the image.”

## Stage 3 - Multi-task mixture tuning

Real models mix many tasks:

- Captioning
- VQA
- OCR
- Chart QA
- Document QA
- Spatial reasoning
- Grounding / bounding boxes
- Referring expression comprehension
- Safety refusal examples
- Conversation data
- Synthetic teacher-generated data

Key engineering problem: **data mixture balance**.

If OCR data is too small, the model reads text poorly. If caption data dominates, answers become descriptive instead of task-focused. If visual data is weak, the model leans on language priors.

## Stage 4 - Preference alignment

Goal: optimize responses for human preference and reduce harmful behavior.

Methods:

- RLHF with reward model + PPO
- DPO / direct preference optimization
- RLAIF / AI feedback
- Rejection sampling
- GRPO and related group-based RL methods for reasoning models

For VLMs, preference data may include:

- Chosen/rejected answers conditioned on image + prompt
- Hallucination preference pairs
- OCR correctness preferences
- Safe refusal examples
- Multi-image/video reasoning preferences

## Stage 5 - Evaluation-driven iteration

Measure before deployment:

- Does the model actually use the image?
- Can it say “I cannot determine from the image”?
- Does it read small text correctly?
- Does it count objects?
- Does it understand spatial relations?
- Does it handle multi-image comparison?
- Does it remain good at text-only tasks after visual tuning?

## Common training bugs

- Connector learns caption shortcuts but not patch-level grounding.
- Model degrades in text-only instruction following after visual instruction tuning.
- Synthetic data is fluent but visually ungrounded.
- Benchmark scores improve while real screenshots/documents fail.
- Video training samples frames but evaluation expects temporal reasoning.

## Output artifact

Draw your own pipeline diagram and annotate:

- Frozen modules
- Trainable modules
- Losses
- Data sources
- Evaluation points
