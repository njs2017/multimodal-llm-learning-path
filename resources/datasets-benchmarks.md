# Datasets and Benchmarks

## Pretraining / alignment data

| Category | Examples | Use |
|---|---|---|
| Image-text pairs | COCO Captions, Conceptual Captions, LAION-style corpora, DataComp-style mixtures | Broad visual-language alignment |
| Web-scale captions | Filtered image-text web data | General coverage, but high noise |
| Synthetic captions/instructions | ShareGPT4V-style, LLaVA-style teacher-generated data | Instruction following and dense descriptions |

## VQA and reasoning

| Dataset/benchmark | Focus |
|---|---|
| VQAv2 | General visual question answering |
| GQA | Compositional visual reasoning |
| OK-VQA | External knowledge + image reasoning |
| ScienceQA | Scientific diagrams/questions |
| MMMU | College-level multimodal reasoning |
| MathVista | Mathematical and visual reasoning |
| MM-Vet | Integrated multimodal capabilities |
| MMBench / MMBench variants | Broad VLM evaluation |

## OCR, charts, and documents

| Dataset/benchmark | Focus |
|---|---|
| TextVQA | Reading text in natural images |
| DocVQA | Document question answering |
| ChartQA | Chart understanding and numerical reasoning |
| InfographicVQA | Infographics and layout-heavy visual QA |
| OCR-VQA | OCR-grounded question answering |
| PubTabNet-style data | Tables and structure extraction |

## Grounding and localization

| Dataset/benchmark | Focus |
|---|---|
| RefCOCO / RefCOCO+ / RefCOCOg | Referring expression grounding |
| Visual Genome | Region graphs, objects, attributes, relationships |
| COCO detection/segmentation | Object localization and segmentation |

## Hallucination and robustness

| Benchmark family | Focus |
|---|---|
| POPE-style evaluations | Object hallucination probing |
| VLM hallucination suites | Unsupported visual claims |
| Adversarial OCR/chart sets | Small text, misleading labels, chart traps |
| Ambiguous image sets | Calibrated uncertainty |

## Video/audio

| Category | Focus |
|---|---|
| VideoQA datasets | Temporal visual question answering |
| Activity recognition datasets | Actions/events |
| Audio captioning datasets | Sound event understanding |
| ASR corpora | Speech recognition and speech-language grounding |

## Dataset card template

```md
# Dataset Name

- Source:
- License:
- Modalities:
- Task:
- Size:
- Annotation type:
- Strengths:
- Risks:
- Leakage concerns:
- Recommended use in pipeline:
- Do not use for:
```
