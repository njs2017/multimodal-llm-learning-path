# YouTube Videos and Playlists

Curated videos to pair with the curriculum. The goal is not to watch everything, but to use videos when a concept needs a visual walkthrough.

## Recommended order

### 1. Prerequisites

#### Transformer / ViT / CLIP foundations

- **Contrastive Language-Image Pre-training (CLIP)** - Samuel Albanie  
  <https://www.youtube.com/watch?v=BcfAkQagEWU>  
  Best for: understanding why CLIP became the foundation for many VLMs.  
  Covers: image-text contrastive learning, zero-shot transfer, robustness, limitations, data overlap, broader impacts.  
  Watch with: `curriculum/01-foundations.md`.

- **Foundation multimodal vision language models** - playlist  
  <https://www.youtube.com/playlist?list=PLXtAHOcKKDTnlySH3pLA0ZVn74WvlLb47>  
  Best for: a broad lecture-style path through ViT, LLMs, ImageBind, LayoutLMv2, and related multimodal foundations.  
  Watch with: weeks 0-2.

## 2. Multimodal LLM overview

- **Multimodal Large Language Model Intro By Google Engineer | LLaVA | BLIP-2** - Martin Is A Dad  
  <https://www.youtube.com/watch?v=jjdKfk89yAM>  
  Best for: a compact introduction to typical MLLM architecture and training.  
  Chapters from search metadata: intro, MLLM architecture, MLLM training, challenges, LLaVA, BLIP-2, future.  
  Watch with: `curriculum/02-architectures.md` and `curriculum/03-training-pipeline.md`.

- **Lecture 5 - Visual-Language Models Introduction Part-II: FLAMINGO, FLAVA, PAINTER, BLIP-2** - UCF CRCV  
  <https://www.youtube.com/watch?v=jwOxr_sObFo>  
  Best for: academic lecture context around the transition from classic VLMs to larger multimodal systems.  
  Watch with: `notes/architecture-taxonomy.md`.

## 3. BLIP-2 and Q-Former

- **Computer Vision Study Group Session on BLIP-2** - Hugging Face  
  <https://www.youtube.com/watch?v=k0DAtZCCl1w>  
  Best for: a paper-study style explanation of BLIP-2.  
  Focus while watching: why BLIP-2 freezes the vision encoder and LLM, what Q-Former does, and what is actually trained.

- **Chat with your Image! BLIP-2 connects Q-Former w/ Vision-Language models** - Discover AI  
  <https://www.youtube.com/watch?v=QHktvcxsGJ0>  
  Best for: quick conceptual overview of Q-Former and image chat.  
  Watch with: `resources/papers.md` BLIP-2 section.

- **How to get started with BLIP 2 | Vision Language Model Tutorial** - CodeTops  
  <https://www.youtube.com/watch?v=uOwuvC374Co>  
  Best for: practical Hugging Face model loading and image captioning.  
  Use for: first hands-on BLIP-2 inference demo.

## 4. LLaVA and visual instruction tuning

- **How LLaVA works - A Multimodal Open Source LLM for image recognition and chat** - Oxen  
  <https://www.youtube.com/watch?v=bK9ns4DkxQg>  
  Best for: paper discussion and practical intuition around the LLaVA recipe.  
  Focus while watching: projector alignment, synthetic instruction data, and visual instruction tuning.

- **New LLaVA AI explained: GPT-4 VISION's Little Brother** - Discover AI  
  <https://www.youtube.com/watch?v=O5mnYvxdKFI>  
  Best for: LLaVA 1.5 architecture and training overview.  
  Useful details from search metadata: pre-trained vision encoder + pre-trained LLM, projection layer/MLP, GPT-4 generated instruction-following data, two-stage training.

## 5. Coding from scratch / implementation-heavy

- **Coding a Multimodal (Vision) Language Model from scratch in PyTorch with full explanation** - Umar Jamil  
  <https://www.youtube.com/watch?v=vAmKB7iPkWw>  
  Best for: deep implementation.  
  Covers: CLIP/SigLIP, ViT, PaliGemma-style architecture, Gemma decoder, KV-cache, image feature projection, attention masks, GQA, RoPE, inference.  
  Code: <https://github.com/hkproj/pytorch-paligemma>  
  Watch with: `labs/02-build-a-tiny-vlm.md`. Do not start here unless you are comfortable with Transformers.

- **Vision-Language Models Tutorial | Build & Train VLMs From Scratch**  
  <https://www.youtube.com/watch?v=na5MWt07NMk>  
  Best for: implementation-oriented VLM learning.  
  Use as: supplementary build-from-scratch walkthrough.

## 6. Fine-tuning and Hugging Face practical track

- **Fine-tune a Vision Language Model with Hugging Face Tutorial**  
  Article/notebook: <https://www.learnhuggingface.com/notebooks/hugging_face_vlm_fine_tune_tutorial>  
  Best for: practical fine-tuning workflow on a custom structured extraction task.  
  Watch/read with: `labs/03-finetune-small-vlm.md`.

- **Vision Language Models Explained** - Hugging Face blog  
  <https://huggingface.co/blog/vlms>  
  Best for: model selection, inference, and fine-tuning overview.

- **Vision Language Models (Better, faster, stronger)** - Hugging Face blog  
  <https://huggingface.co/blog/vlms-2025>  
  Best for: 2025 trends: any-to-any models, reasoning VLMs, small VLMs, video language models, VLA, safety, and alignment.

## 7. Supplemental reading that pairs well with videos

- **Multimodality and Large Multimodal Models** - Chip Huyen  
  <https://huyenchip.com/2023/10/10/multimodal.html>  
  Best for: conceptual grounding, modality types, CLIP/Flamingo, and broader LMM framing.

- **Design choices for Vision Language Models in 2024** - Hugging Face  
  <https://huggingface.co/blog/gigant/vlm-design>  
  Best for: architectural tradeoffs and visual abstractors/connectors.

- **Introduction to Vision Language Models** - Hugging Face Computer Vision Course  
  <https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro>  
  Best for: beginner-friendly VLM fundamentals.

## How to take notes from videos

For every video, write:

```md
# Video title

- URL:
- Date watched:
- Level: beginner / intermediate / advanced
- Main idea in one sentence:
- Architecture terms introduced:
- Training stages mentioned:
- Datasets/benchmarks mentioned:
- 3 things I understood better:
- 3 questions I still have:
- How this changes my project plan:
```

## Suggested watch schedule

| Week | Watch |
|---:|---|
| 0 | CLIP lecture + HF VLM intro |
| 1 | Martin Is A Dad MLLM intro |
| 2 | UCF VLM lecture + BLIP-2 HF study group |
| 3 | LLaVA Oxen discussion + LLaVA 1.5 explainer |
| 4 | Hugging Face VLM fine-tuning material |
| 5 | TRL/VLM alignment material from `resources/papers.md` |
| 6 | Umar Jamil PaliGemma from-scratch video, selected chapters only |
| 7 | HF 2025 VLM trends + any-to-any/omni sections |
| 8 | Re-watch selected implementation sections while building final project |
