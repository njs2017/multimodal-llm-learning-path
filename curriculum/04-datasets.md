# 04 - Datasets and Data Mixtures

## Core question

What data does a multimodal LLM need?

## Dataset categories

### Image-text pretraining

Used to learn broad visual-language correspondence.

Examples:

- Web-scale image-caption pairs
- LAION-style data
- COCO captions
- Conceptual Captions
- DataComp-style curated mixtures

### VQA and reasoning

Question-answer pairs over images.

Examples:

- VQAv2
- GQA
- ScienceQA
- OK-VQA
- VizWiz

### OCR and document understanding

Critical for real workflows.

Examples:

- TextVQA
- DocVQA
- ChartQA
- InfographicVQA
- OCR-VQA
- PubTabNet-style table/document data

### Grounding and localization

For linking language to regions.

Examples:

- RefCOCO/RefCOCO+/RefCOCOg
- Visual Genome
- Region captions
- Object detection/segmentation corpora

### Multimodal instruction tuning

Instruction-response pairs involving images/docs/video/audio.

Examples:

- LLaVA-Instruct style synthetic data
- InstructBLIP mixtures
- ShareGPT4V-style high-quality captions/instructions
- InternVL/Qwen-style public mixtures where available

### Preference and safety data

Chosen/rejected pairs and safety prompts.

Examples:

- VLM response preference datasets
- Hallucination-reduction datasets
- Refusal/safety multimodal datasets
- Human/AI feedback data

### Video and audio

Examples:

- VideoQA datasets
- Activity/action datasets
- Audio captioning and speech datasets
- ASR corpora such as Whisper-style training mixtures where licensed

## Data quality checklist

For every dataset, record:

- License
- Source and collection process
- Modality coverage
- Annotation type
- Whether answers are grounded in the input
- Known biases
- OCR/spatial/temporal difficulty
- Train/eval leakage risk
- Whether synthetic teacher answers were verified

## Output artifact

Create a dataset matrix with columns:

```text
Dataset | Modality | Task | Size | License | Strength | Risk | Use in pipeline
```
