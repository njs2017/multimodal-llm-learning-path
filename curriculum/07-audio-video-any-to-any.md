# 07 - Audio, Video, Documents, and Any-to-Any Models

## Core question

What changes when we move beyond single images?

## Documents

Document understanding combines:

- OCR
- Layout understanding
- Tables
- Charts
- Long context
- Retrieval
- Visual reasoning

A model must reason over both text and spatial layout.

## Audio

Audio systems may involve:

- ASR / speech-to-text
- Audio event understanding
- Speaker/tone recognition
- Text-to-speech
- End-to-end speech models

Training can use transcriptions, audio captions, speech instruction data, and preference data over spoken responses.

## Video

Video is hard because it adds time.

Problems:

- Too many frames
- Temporal ordering
- Event boundaries
- Long context
- Audio-video synchronization
- Frame sampling bias

Common approach:

```text
video -> sampled frames / video encoder -> visual tokens -> LLM
```

Better systems add temporal position encodings, video-specific encoders, memory, or retrieval over frames.

## Any-to-any systems

Any-to-any models can map between modalities:

- image -> text
- text -> image
- audio -> text
- text -> speech
- video + audio -> text
- text + image -> speech

Architecture often includes:

- Encoders for each input modality
- Shared representation or token space
- Decoders for each output modality
- Routing or modality-specific heads

## Vision-Language-Action models

For robotics and agents, output may be an action, not just text.

Examples:

```text
camera + instruction -> robot action
screenshot + goal -> click/type action
```

This connects multimodal LLMs to agents.

## Output artifact

Pick one domain: documents, audio, video, GUI agents, or robotics. Write a one-page system design for a prototype.
