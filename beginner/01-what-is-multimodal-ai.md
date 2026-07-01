# 01 - What Is Multimodal AI?

## Simple definition

**Multimodal AI** means AI that can use multiple kinds of data.

A modality is a kind of information:

- Text
- Image
- Audio
- Video
- Document
- Chart
- Screenshot
- Sensor signal
- Action

A text-only chatbot uses one modality: text.

A multimodal assistant may use several:

```text
image + question -> answer
video + question -> answer
screenshot + goal -> action
PDF + question -> cited answer
```

## Everyday examples

### Image question answering

You upload a photo and ask:

> What is broken in this picture?

The model must identify objects and reason from visual evidence.

### Document understanding

You upload a scanned invoice and ask:

> What is the total amount and invoice date?

The model must read text, understand layout, and avoid inventing values.

### Chart reasoning

You upload a chart and ask:

> Which quarter had the largest drop?

The model must read axes, compare values, and reason numerically.

### Screen agents

You give a screenshot and ask:

> Click the button that exports the report.

The model must understand UI layout and produce an action.

## Input vs output modalities

A model can be multimodal in input, output, or both.

| Type | Example |
|---|---|
| Multiple inputs | text + image -> text |
| Different input/output | text -> image |
| Multiple outputs | text -> speech + captions |
| Any-to-any | text/image/audio/video -> text/image/audio/video |

Most beginner VLMs are:

```text
image + text -> text
```

That is enough to learn the core ideas.

## Why images are different from text

Text is already symbolic. It comes as words or tokens.

Images are raw pixels. A model has to discover:

- Objects
- Colors
- Positions
- Text inside the image
- Layout
- Relationships
- What matters for the question

This is why multimodal models often use a special **encoder** before the LLM.

## Key takeaway

Multimodal AI is not just “LLM plus image upload.” It is a system that converts different data types into representations a model can combine and reason over.
