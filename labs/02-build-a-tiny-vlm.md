# Lab 02 - Build a Tiny VLM Mental Model

## Goal

Implement or trace the minimal architecture behind many VLMs:

```text
image -> vision encoder -> projector -> LLM -> answer
```

You do not need to train a production model. The point is to understand tensor flow.

## Minimal components

### 1. Vision encoder

Options:

- Use a frozen CLIP/SigLIP/ViT encoder.
- Or implement a tiny patch embedding + transformer for learning only.

### 2. Projector

A simple MLP:

```text
visual_dim -> hidden_dim -> llm_embedding_dim
```

### 3. Text model

Options:

- Use a tiny pretrained causal LM.
- Or trace an existing small VLM.

### 4. Token merge

The projected visual tokens become prefix/context tokens for the LLM.

```text
[visual tokens] + [text tokens] -> LLM -> answer tokens
```

## What to inspect

- Shape of image patches.
- Number of visual tokens.
- Projector input/output dimensions.
- Where visual tokens are inserted.
- Which tokens are masked in the loss.
- How generation uses KV-cache after the image prefix.

## Recommended video

Umar Jamil's PaliGemma implementation video:  
<https://www.youtube.com/watch?v=vAmKB7iPkWw>

Suggested chapters from search metadata:

- Contrastive Learning and CLIP
- SigLIP
- Vision Transformer
- PaliGemma architecture review
- PaliGemma input processor
- Image features projection
- KV-cache
- Inference code

## Deliverable

Create a diagram with tensor shapes, for example:

```text
image: [B, 3, H, W]
patches: [B, N, patch_dim]
vision_hidden: [B, N, vision_dim]
projected: [B, N, llm_dim]
text_embeds: [B, T, llm_dim]
merged: [B, N+T, llm_dim]
logits: [B, N+T, vocab]
```
