# 03 - Learn CLIP Before LLaVA

## Why CLIP matters

CLIP is one of the most important stepping stones in multimodal AI.

It showed that a model can learn useful visual concepts from natural language supervision instead of fixed human labels.

## The problem before CLIP

Classic image classifiers were trained like this:

```text
image -> label from fixed list
```

Example labels:

- cat
- dog
- car
- airplane

Problem: the model only knows the labels it was trained on.

## CLIP's idea

Train two encoders:

```text
image -> image encoder -> image embedding
text  -> text encoder  -> text embedding
```

Then train them so matching image/text pairs are close together.

Example:

```text
image of a dog on the beach <-> "a dog running on the beach"
```

The model learns a shared embedding space where images and text can be compared.

## Contrastive learning in plain English

In each training batch, CLIP sees many images and many captions.

It learns:

- This image belongs with this caption.
- This image does not belong with those other captions.

So the training game is:

```text
Pull correct pairs together.
Push incorrect pairs apart.
```

## What CLIP can do

- Image search using text
- Text search using images
- Zero-shot classification
- Image clustering
- Image filtering
- Provide vision encoders for later VLMs

## What CLIP cannot do well by itself

CLIP is not a chatbot.

It does not naturally produce detailed answers like:

> The chart shows revenue declining after Q3 because...

It is mainly a representation and retrieval model.

Weaknesses:

- Detailed OCR
- Counting
- Multi-step reasoning
- Explaining diagrams
- Following complex instructions
- Saying “I do not know” reliably

## Why this matters for LLaVA-style models

LLaVA uses a CLIP-like vision encoder and connects it to an LLM.

That gives the system:

- CLIP-style visual representations
- LLM-style conversation and reasoning
- Instruction-following behavior after fine-tuning

## Beginner checkpoint

Before reading LLaVA, make sure you can explain:

1. What two encoders CLIP trains.
2. What “shared embedding space” means.
3. What contrastive learning does.
4. Why CLIP is useful but not enough for image chat.
