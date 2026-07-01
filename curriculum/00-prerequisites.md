# 00 - Prerequisites

## Goal

Before studying multimodal LLMs, make sure you can explain the components that get reused inside them.

## Must know

### LLM basics

- Tokenization
- Embeddings
- Transformer decoder
- Attention and cross-attention
- Context windows
- Pretraining vs fine-tuning vs post-training
- Causal language modeling loss
- Instruction tuning / SFT
- Preference optimization: RLHF, DPO, GRPO-style RL methods

### Vision basics

- CNN vs Vision Transformer (ViT)
- Image patches
- Image embeddings
- Contrastive learning
- CLIP-style image-text alignment

### Training basics

- Cross-entropy loss
- Contrastive loss
- Frozen vs trainable modules
- LoRA / QLoRA / PEFT
- Batch construction and data mixture weighting
- Evaluation leakage and benchmark contamination

## Output artifact

Write a one-page explanation of this pipeline:

```text
image -> vision encoder -> connector -> LLM -> answer
```

Include what is frozen, what is trained, and why freezing is useful.
