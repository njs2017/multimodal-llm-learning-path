# Papers and Reading List

This is a curated reading order, not a complete bibliography.

## Foundations

### CLIP - Learning Transferable Visual Models From Natural Language Supervision

Why read: establishes contrastive image-text alignment as a scalable foundation.

Key idea: train image and text encoders so matching image-caption pairs are close in embedding space.

### Vision Transformer (ViT)

Why read: many vision encoders in VLMs are ViT-family models.

## Bridge models and early MLLMs

### Flamingo: a Visual Language Model for Few-Shot Learning

Source: <https://arxiv.org/abs/2204.14198>

Why read: important cross-attention architecture for interleaved image/text few-shot learning.

Core idea: connect powerful vision representations to a language model using gated cross-attention/resampling-style components.

### BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

Source: <https://arxiv.org/abs/2301.12597>

Why read: canonical frozen-image-encoder + frozen-LLM bridge recipe.

Core idea: a Q-Former learns to query visual features and feed useful representations to an LLM.

### Visual Instruction Tuning / LLaVA

Source: <https://arxiv.org/abs/2304.08485>

Why read: practical open-source recipe for turning a vision encoder + LLM into a visual assistant.

Core idea: use GPT-4-generated visual instruction data and train a multimodal assistant connecting vision encoder and LLM.

### InstructBLIP

Why read: explores instruction-aware visual feature extraction and broad instruction tuning.

## Modern VLMs / MLLMs to inspect

- Qwen-VL / Qwen2-VL / Qwen2.5-VL
- InternVL
- IDEFICS / IDEFICS2 / IDEFICS3
- LLaMA 3.2 Vision
- Pixtral
- NVLM
- MiniCPM-V / MiniCPM-o
- SmolVLM / SmolVLM2
- Qwen2.5-Omni
- Janus / Janus-Pro

## Surveys

### A Survey of State of the Art Large Vision Language Models: Alignment, Benchmark, Evaluations and Challenges

Source: <https://arxiv.org/html/2501.02189v6>

Why read: broad 2025 overview of architectures, alignment methods, benchmarks, and challenges.

### How to Bridge the Gap between Modalities: Survey on Multimodal Large Language Model

Source: <https://arxiv.org/html/2311.07594v3>

Why read: useful categorization of modality alignment approaches.

### Efficient Multimodal Large Language Models: A Survey

Source: <https://link.springer.com/article/10.1007/s44267-025-00099-6>

Why read: efficiency is central because visual/video tokens are expensive.

## Alignment and post-training

### Aligning Multimodal LLM with Human Preference: A Survey

Source: <https://arxiv.org/html/2503.14504v2>

Why read: covers preference alignment scenarios, datasets, benchmarks, and future directions for MLLMs.

### Multi-modal Preference Alignment Remedies Regression of Visual Instruction Tuning on Language Model

Source: <https://arxiv.org/html/2402.10884v1>

Why read: shows that visual instruction tuning can degrade language abilities and that multimodal preference alignment can help.

### Hugging Face TRL VLM alignment posts/docs

Source: <https://huggingface.co/blog/trl-vlm-alignment>

Why read: practical tooling for VLM SFT, DPO, GRPO/related methods.

## Trend overviews

### Hugging Face - Vision Language Models, Better, Faster, Stronger

Source: <https://huggingface.co/blog/vlms-2025>

Why read: concise 2025 overview of any-to-any models, small VLMs, video language models, multimodal agents, safety, and alignment.


## Video companion

A curated video list is available at [`youtube-videos.md`](youtube-videos.md). Use it to pair lectures and implementation walkthroughs with the paper sequence above.
