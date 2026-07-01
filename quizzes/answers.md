# Quiz Answers

## 00 - Vocabulary

1. A modality is a type of data, such as text, image, audio, video, document, or action.
2. An embedding is a vector of numbers representing useful meaning/features.
3. An encoder converts raw input into embeddings or tokens.
4. A VLM focuses on vision + language; an MLLM can include broader modalities such as image, audio, video, documents, and actions.
5. Grounding means tying an answer to evidence in the input.
6. Visual hallucination is claiming visual content not supported by the image/video/document.
7. A connector maps vision/audio features into a form the LLM can consume.
8. OCR is extracting text from images or documents.
9. Zero-shot means doing a task without task-specific training examples.
10. Instruction tuning trains the model to follow user requests.

## 01 - CLIP

CLIP trains image and text encoders with contrastive learning so matching image-text pairs are close in embedding space and mismatched pairs are far apart. It enables zero-shot classification by comparing an image embedding to text-label embeddings. It is useful for retrieval/classification but not enough for detailed chat, OCR, counting, or multi-step reasoning.

## 02 - Architecture

A common VLM uses a vision encoder, connector/projector/Q-Former, and LLM. The vision encoder produces visual features; the connector maps those features to LLM-compatible embeddings. Freezing saves compute and preserves pretrained knowledge. Visual instruction tuning teaches assistant-style behavior over visual inputs.

## 03 - Training

Connector alignment teaches the bridge; captioning teaches description; instruction tuning teaches task-following; OCR data teaches text reading; text-only data helps preserve language ability; preference alignment teaches chosen behavior over rejected behavior conditioned on multimodal input.

## 04 - Evaluation

One benchmark cannot cover all skills. Include perception, OCR, charts, documents, screenshots, video, hallucination, uncertainty, and safety. Product-specific data matters because public benchmarks rarely match your real distribution. A good model admits uncertainty when evidence is unreadable.
