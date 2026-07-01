# 01 - Foundations of Multimodal Learning

## Core question

How do we make representations from different modalities comparable or usable together?

## Concepts

### Modality

A modality is a type of signal: text, image, audio, video, depth, point cloud, UI actions, sensor data, etc.

### Embedding space

Models convert raw signals into vectors. Multimodal learning tries to align vectors from different modalities so that related concepts are close.

### Contrastive alignment

CLIP-style training learns from pairs like `(image, caption)`:

- Pull matching image/text embeddings together.
- Push non-matching pairs apart.

This gives strong zero-shot classification and retrieval, but it does not by itself create a conversational assistant.

### Fusion

Multimodal systems need a way to combine modalities:

- Early fusion: combine low-level tokens early.
- Late fusion: combine high-level embeddings or decisions.
- Cross-attention: text attends to visual features or vice versa.
- Token unification: treat all modalities as token streams.

## Required reading

- CLIP: learning transferable visual models from natural language supervision.
- BLIP / BLIP-2 background.
- LLaVA visual instruction tuning abstract and project page.

## Practical exercise

Use an open CLIP model to embed 10 images and 10 captions. Check retrieval quality. Then document where retrieval differs from true reasoning.

## Output artifact

A short note: **retrieval alignment is not the same as multimodal reasoning**.
