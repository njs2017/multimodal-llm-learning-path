# Model Zoo to Study

This is not a leaderboard. It is a map of model families worth studying to understand design choices.

## Foundation / representation models

### CLIP

- Type: dual encoder
- Key idea: contrastive image-text alignment
- Useful for: retrieval, zero-shot classification, image encoder backbone
- Limitation: not a chat model, weak for detailed reasoning/OCR/counting

### SigLIP

- Type: contrastive/sigmoid loss image-text model
- Useful for: modern VLM vision encoders
- Why study: appears in several newer VLM stacks

## Bridge / adapter VLMs

### Flamingo

- Type: visual features + language model with cross-attention/resampling
- Key idea: few-shot learning over interleaved image-text sequences
- Why study: historically important architecture for LMMs

### BLIP-2

- Type: frozen vision encoder + frozen LLM + Q-Former
- Key idea: Q-Former bridges visual features into language model space
- Why study: efficient bootstrapping recipe

### LLaVA

- Type: CLIP vision encoder + projector + LLM
- Key idea: visual instruction tuning with synthetic instruction data
- Why study: practical open-source baseline and recipe

### InstructBLIP

- Type: BLIP-2 style with instruction-aware visual feature extraction
- Key idea: instruction-conditioned visual querying

## Modern open VLMs

### Qwen-VL / Qwen2-VL / Qwen2.5-VL

- Strong in OCR, document understanding, grounding, and practical usage.
- Study for modern open VLM capabilities and data mixture design.

### InternVL

- Strong open VLM family with broad benchmark coverage.
- Study for scaling and evaluation patterns.

### IDEFICS / IDEFICS2 / IDEFICS3

- Hugging Face/open multimodal models.
- Study for accessible training and inference tooling.

### LLaMA 3.2 Vision

- LLaMA-family vision model.
- Study for mainstream LLM-to-VLM transition.

### Pixtral

- Mistral-family VLM.
- Study for high-quality open inference and architecture tradeoffs.

### PaliGemma / PaliGemma 2

- Gemma-family VLM.
- Study for implementation clarity and transfer tasks.

### SmolVLM / SmolVLM2

- Small VLM family.
- Study for local/on-device tradeoffs and efficient video-capable models.

## Any-to-any / omni models

### Qwen2.5-Omni

- Inputs/outputs include text, audio, image, video, and speech interaction.
- Study for omni-modal architecture and Thinker/Talker-style separation.

### MiniCPM-o

- Compact omni-capable model family.
- Study for efficient multimodal deployment.

### Janus / Janus-Pro

- Decouples visual encoding for understanding vs generation.
- Study for unified understanding/generation design tradeoffs.

## Vision-language-action / agent models

### PaLM-E

- Embodied multimodal language model.
- Study for robotics and sensor-to-language/action grounding.

### VLA models

- Input: vision + language instruction.
- Output: action.
- Study for robotics and GUI/screen agents.

## How to compare models

For each model, fill:

```md
# Model

- Paper / repo:
- Input modalities:
- Output modalities:
- Vision/audio/video encoder:
- LLM backbone:
- Connector/fusion mechanism:
- Training stages:
- Datasets disclosed:
- Benchmarks:
- Strengths:
- Failure modes:
- What design choice I would copy:
```
