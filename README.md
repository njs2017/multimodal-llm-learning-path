# Multimodal LLM Learning Path

**New to multimodal models? Start with [`START_HERE.md`](START_HERE.md).**

A beginner-friendly, research-backed, hands-on learning path for understanding **multimodal large language models (MLLMs)** and **multimodal training**: vision-language models, audio/video extensions, alignment, datasets, evaluation, and practical projects.

This repository is meant for newcomers, engineers, and researchers who want to understand how models like LLaVA, BLIP-2, Flamingo, Qwen-VL/Omni, GPT-4V/4o-style systems, Gemini-style systems, and modern VLM agents are built and trained.

## What you will learn

By the end, you should be able to explain and prototype:

- How text-only LLMs are extended to images, audio, video, documents, screens, and actions.
- Core VLM/MLLM architectures: dual encoders, encoder-decoder fusion, frozen-encoder + LLM bridge, cross-attention, query transformers, unified tokenizers, any-to-any systems.
- Training stages: pretraining, connector alignment, multimodal instruction tuning, preference alignment, RL/DPO/GRPO-style post-training, and evaluation.
- Data construction: image-text pairs, captioning, VQA, OCR/doc data, synthetic instruction data, preference data, safety data, video/audio data.
- Evaluation: VQA, OCR, chart/document reasoning, MMMU-style multimodal reasoning, hallucination checks, agent/browser tasks, and human preference evals.
- Practical fine-tuning paths with open-source VLMs.

## Suggested path

| Week | Focus | Output |
|---:|---|---|
| 0 | Prerequisites: Transformers, CLIP, ViT, LLM training | Concept map |
| 1 | Foundations of multimodal learning | Explain CLIP/contrastive alignment |
| 2 | Vision-language model architectures | Compare Flamingo, BLIP-2, LLaVA |
| 3 | Multimodal training pipeline | Draw and explain each training stage |
| 4 | Datasets and data mixtures | Build a dataset catalog and risk checklist |
| 5 | Instruction tuning and alignment | Fine-tune or simulate a visual instruction dataset |
| 6 | Evaluation and hallucination | Build a small evaluation suite |
| 7 | Audio, video, documents, and any-to-any models | Extend the mental model beyond images |
| 8 | Multimodal agents and final project | Build a screen/document/vision assistant prototype |

## Repository structure

```text
.
├── README.md
├── START_HERE.md
├── beginner/
│   ├── 01-what-is-multimodal-ai.md
│   ├── 02-core-mental-model.md
│   ├── 03-clip-before-llava.md
│   ├── 04-from-clip-to-vlm.md
│   ├── 05-training-without-the-math.md
│   ├── 06-how-to-read-vlm-papers.md
│   ├── 07-common-misconceptions.md
│   └── 08-first-projects.md
├── curriculum/
│   ├── 00-prerequisites.md
│   ├── 01-foundations.md
│   ├── 02-architectures.md
│   ├── 03-training-pipeline.md
│   ├── 04-datasets.md
│   ├── 05-alignment.md
│   ├── 06-evaluation.md
│   ├── 07-audio-video-any-to-any.md
│   └── 08-projects.md
├── notes/
│   ├── architecture-taxonomy.md
│   ├── multimodal-training.md
│   └── open-research-questions.md
├── projects/
│   └── project-ideas.md
├── learning-tracks.md
├── labs/
│   ├── 01-clip-retrieval.md
│   ├── 02-build-a-tiny-vlm.md
│   ├── 03-finetune-small-vlm.md
│   └── 04-vlm-evaluation-harness.md
├── resources/
│   ├── beginner-reading.md
│   ├── papers.md
│   ├── youtube-videos.md
│   ├── model-zoo.md
│   ├── datasets-benchmarks.md
│   └── glossary.md
└── diagrams/
    └── training-pipeline.mmd
```

## Fast mental model

Most practical multimodal LLMs are built by combining three things:

```text
Modality encoder -> adapter/projector/resampler -> LLM backbone -> multimodal response
```

Example for image-text chat:

```text
Image -> Vision Transformer / CLIP / SigLIP -> projected visual tokens -> LLM -> answer
Text  -> tokenizer -> text tokens ------------------------------------^
```

Then they are trained in stages:

1. **Pretrain or reuse unimodal backbones**: LLM, vision encoder, audio encoder, etc.
2. **Modality alignment**: teach visual/audio embeddings to be consumable by the LLM.
3. **Multimodal instruction tuning**: teach the model to follow user requests involving images/docs/video/audio.
4. **Preference/safety alignment**: optimize helpfulness, truthfulness, refusal behavior, and reduced hallucination.
5. **Evaluation and deployment tuning**: measure OCR, reasoning, grounding, latency, context cost, and failure modes.

## How to use this repo

### If you are new to multimodal models

1. Start with [`START_HERE.md`](START_HERE.md).
2. Read the `beginner/` folder in order.
3. Use [`resources/beginner-reading.md`](resources/beginner-reading.md) before survey papers.
4. Watch the beginner videos in [`resources/youtube-videos.md`](resources/youtube-videos.md).
5. Do `labs/01-clip-retrieval.md` before trying to fine-tune anything.

### If you already know the basics

1. Choose a route in [`learning-tracks.md`](learning-tracks.md): conceptual researcher, builder, agent-focused, or training/alignment specialist.
2. Read the curriculum in order or follow your selected track.
3. Pair each module with videos from [`resources/youtube-videos.md`](resources/youtube-videos.md).
4. For each module, produce the weekly output artifact.
5. Implement at least two projects from [`projects/project-ideas.md`](projects/project-ideas.md).
6. Work through the hands-on labs in [`labs/`](labs/).
7. Maintain your own error log: where did the model hallucinate, fail OCR, miss spatial relations, or ignore the visual input?

## New hands-on labs

- [`labs/01-clip-retrieval.md`](labs/01-clip-retrieval.md) - CLIP retrieval and failure analysis.
- [`labs/02-build-a-tiny-vlm.md`](labs/02-build-a-tiny-vlm.md) - trace the tensor flow of image -> projector -> LLM.
- [`labs/03-finetune-small-vlm.md`](labs/03-finetune-small-vlm.md) - fine-tune or evaluate a small VLM.
- [`labs/04-vlm-evaluation-harness.md`](labs/04-vlm-evaluation-harness.md) - build a practical multimodal eval set.

## Primary sources used

See `resources/beginner-reading.md`, `resources/papers.md`, `resources/youtube-videos.md`, `resources/model-zoo.md`, and `resources/datasets-benchmarks.md` for the full source list.

Key anchors:

- CLIP, Flamingo, BLIP-2, LLaVA, InstructBLIP, PaLM-E, Qwen-VL/Qwen2.5-VL/Qwen2.5-Omni, GPT-4V/GPT-4o-style systems, Gemini-style systems.
- 2025 VLM surveys and Hugging Face VLM trend summaries.
- Alignment work for VLMs including multimodal preference alignment and TRL support for VLM SFT/DPO/GRPO-style methods.

## License

MIT for the repository structure and original notes. Paper summaries link to their original sources and licenses.
