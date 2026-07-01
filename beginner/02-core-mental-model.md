# 02 - The Core Mental Model

## The simplest VLM picture

Most practical vision-language models can be understood as this pipeline:

```text
image -> vision encoder -> connector -> language model -> answer
```

With text included:

```text
image -> vision encoder -> connector ----\
                                         language model -> answer
question -> tokenizer ------------------/
```

## What each piece does

### Vision encoder

Turns pixels into useful visual features.

Examples:

- CLIP vision encoder
- SigLIP
- Vision Transformer, ViT
- EVA-CLIP

Plain English:

> The vision encoder converts “what is in the image” into vectors.

### Connector

Translates visual vectors into something the language model can use.

Examples:

- Linear projector
- MLP projector
- Q-Former
- Perceiver resampler
- Cross-attention adapter

Plain English:

> The connector is the bridge between seeing and speaking.

### Language model

Generates the answer using text tokens and visual tokens.

Examples:

- Vicuna
- LLaMA
- Qwen
- Gemma
- Mistral

Plain English:

> The LLM does the conversation and reasoning, conditioned on visual information.

## Analogy: translator between senses

Imagine the vision encoder speaks “image language” and the LLM speaks “text-token language.”

The connector is a translator.

If the connector is weak, the LLM may answer from prior knowledge instead of the image.

## Why this design is popular

Training a frontier multimodal model from scratch is expensive.

A practical shortcut:

1. Reuse a strong vision model.
2. Reuse a strong LLM.
3. Train a small bridge between them.
4. Fine-tune on image-question-answer examples.

This is why models like BLIP-2 and LLaVA were so influential.

## What can go wrong

### The model ignores the image

The LLM may answer based on language priors.

Prompt:

> What color is the stop sign?

A weak model might answer “red” even if the image is black-and-white or the sign is not visible.

### The model reads poorly

OCR is hard. Small or blurry text often fails.

### The model counts poorly

Counting objects requires precise visual grounding.

### The model overexplains

If trained on captioning data, it may describe the whole image instead of answering the specific question.

## Key takeaway

For newcomers, remember this:

> A VLM is usually an LLM with a visual front-end and a learned bridge.
