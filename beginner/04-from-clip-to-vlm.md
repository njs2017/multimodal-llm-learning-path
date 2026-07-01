# 04 - From CLIP to Vision-Language Models

## The leap

CLIP can match images and text.

A VLM can answer questions about images.

That requires adding an LLM-style generation component.

## CLIP-style retrieval

```text
image -> embedding
text -> embedding
compare embeddings
```

Output is usually a similarity score or ranking.

## VLM-style generation

```text
image + question -> answer
```

Output is generated text.

Example:

```text
User: What is unusual in this image?
Model: The dog appears to be wearing sunglasses while sitting at a dinner table.
```

## The bridge problem

The vision encoder outputs visual features.

The LLM expects token embeddings.

So the model needs a bridge:

```text
visual features -> connector -> LLM-compatible embeddings
```

Different models solve this differently:

| Model | Bridge idea |
|---|---|
| Flamingo | visual resampler + cross-attention |
| BLIP-2 | Q-Former |
| LLaVA | linear/MLP projector |
| Qwen-VL-style models | more advanced visual token handling and training mixtures |

## Why instruction tuning is needed

If you only train on captions, the model learns:

> Describe the image.

But users ask many kinds of questions:

- What changed between these images?
- What should I click?
- What does this chart imply?
- Is there enough evidence to answer?
- Extract the table as JSON.

Instruction tuning teaches the model to follow these requests.

## The common two-stage recipe

A simplified LLaVA-like recipe:

### Stage 1: align the connector

Freeze the vision encoder and LLM.

Train the connector so image features fit the LLM space.

### Stage 2: visual instruction tuning

Train on examples like:

```text
image + instruction -> answer
```

This teaches assistant behavior.

## Key takeaway

CLIP gives useful visual-language representations. VLMs add a bridge into an LLM and train the system to follow multimodal instructions.
