# 05 - Multimodal Training Without the Math

## The big picture

Training a multimodal LLM usually happens in stages.

You do not need the math first. Understand what each stage is trying to teach.

## Stage 0 - Start with existing models

Most teams do not train everything from zero.

They start with:

- A pretrained LLM
- A pretrained vision encoder
- A new connector between them

Why?

Because LLMs already know language, and vision encoders already know a lot about images.

## Stage 1 - Teach the bridge

Goal:

> Make image features understandable to the LLM.

Data:

- Image-caption pairs
- Simple image descriptions

Training behavior:

- Often freeze the LLM and vision encoder.
- Train only the connector.

Plain English:

> The bridge learns to translate image features into the LLM's internal language.

## Stage 2 - Teach it to follow visual instructions

Goal:

> Make the model useful as an assistant.

Data:

```text
image + user question -> helpful answer
```

Examples:

- “Describe the image.”
- “What is the person holding?”
- “Read the text on the sign.”
- “What does this chart show?”
- “Extract the fields as JSON.”

Plain English:

> The model learns that images are not just for captions; they are evidence for user tasks.

## Stage 3 - Mix many skills

A good model needs many visual skills:

- General object recognition
- OCR
- Charts
- Documents
- Screenshots
- Spatial reasoning
- Multi-image comparison
- Safety/refusal
- Text-only conversation

If the data mixture is poor, the model becomes lopsided.

Example:

- Too much captioning -> verbose descriptions
- Too little OCR -> bad at reading screenshots
- Too little text-only data -> weaker normal chat
- Too much synthetic data -> fluent but ungrounded answers

## Stage 4 - Preference alignment

Goal:

> Prefer better answers over worse answers.

Data format:

```text
image + question + chosen answer + rejected answer
```

Example:

```text
Question: What number is on the sign?
Chosen: The sign appears to say 47.
Rejected: The sign says 42.
```

This is useful because the rejected answer may sound fluent but be visually wrong.

## Stage 5 - Evaluate and fix failures

You test the model on tasks like:

- Does it actually use the image?
- Can it read text?
- Can it count?
- Can it compare images?
- Can it answer charts?
- Can it admit uncertainty?
- Does it hallucinate?

Then you adjust data, training, prompts, or architecture.

## Beginner summary

Training teaches five things:

1. **Represent** images/audio/video.
2. **Connect** those representations to language.
3. **Follow instructions** involving those modalities.
4. **Prefer grounded answers** over plausible hallucinations.
5. **Remain reliable** under evaluation.
