# 02 - Architecture Taxonomy

## Core question

What are the main ways to build a multimodal LLM?

## 1. Dual encoder models

Example: CLIP.

```text
image -> image encoder -> image embedding
text  -> text encoder  -> text embedding
```

Strengths:

- Retrieval
- Zero-shot classification
- Scalable pretraining

Weaknesses:

- Not naturally generative
- Weak for multi-step visual reasoning
- No built-in instruction following

## 2. Encoder-decoder / fusion models

Examples: BLIP, early VQA/captioning systems.

Strengths:

- Captioning and VQA
- Flexible fusion

Weaknesses:

- Often task-specific compared with modern LLM-backed systems

## 3. Frozen vision encoder + frozen/fine-tuned LLM + connector

Examples: BLIP-2, LLaVA-style systems.

```text
image -> frozen vision encoder -> Q-Former/projector/resampler -> LLM
text  -> tokenizer ---------------------------------------------> LLM
```

Strengths:

- Efficient
- Reuses strong pretrained LLMs
- Easy to instruction tune
- Popular open-source recipe

Weaknesses:

- Visual tokens may be weakly grounded
- OCR/spatial reasoning may fail
- The LLM can answer from language priors instead of image evidence

## 4. Cross-attention augmented LLMs

Example: Flamingo-style models.

Visual features are inserted through cross-attention layers while the language model remains central.

Strengths:

- Few-shot multimodal learning
- Handles interleaved image/text sequences

Weaknesses:

- Complex and expensive
- Less accessible for small labs

## 5. Unified token / native multimodal transformers

Emerging direction: represent images/audio/video/text as token streams in one transformer.

Strengths:

- Cleaner any-to-any modeling
- Potentially stronger cross-modal reasoning

Weaknesses:

- Very expensive data and compute
- Tokenization design is hard
- Long video/audio becomes costly

## 6. Any-to-any / omni models

Models that can accept and emit multiple modalities, for example text, image, audio, video, and speech.

Examples and directions include Qwen2.5-Omni-style systems and other omni-modal models.

## Output artifact

Create a comparison table of Flamingo, BLIP-2, LLaVA, Qwen-VL, and an omni model. Include:

- Inputs
- Outputs
- Vision encoder
- LLM backbone
- Connector/fusion mechanism
- Training stages
- Strengths
- Failure modes
