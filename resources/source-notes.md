# Source Notes from Deep Research

This file records source-grounded takeaways used to expand the course.

## Hugging Face VLM intro

Source: <https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro>

Key takeaways:

- Multimodal learning needs both representation and alignment.
- CLIP is a central example of image-text contrastive learning.
- VLM strategies include joint embedding training, image embeddings as prefixes, cross-attention fusion, and no-training combinations.

## Hugging Face zero-shot image classification

Source: <https://huggingface.co/docs/transformers/en/tasks/zero_shot_image_classification>

Key takeaways:

- Zero-shot image classification lets users classify images into labels not seen as task-specific training labels.
- Open-vocabulary image classification uses aligned image/text representations.
- The official `pipeline("zero-shot-image-classification")` is the simplest beginner-friendly demo path.

## Introductory VLM paper

Source: <https://arxiv.org/html/2405.17247v1>

Key takeaways:

- VLMs still struggle with spatial relations, counting, attributes, ordering, prompt adherence, hallucination, bias, and grounding.
- The paper groups VLMs into contrastive, masking-objective, generative, and pretrained-backbone families.
- The repo’s newcomer path emphasizes these failure modes early rather than presenting VLMs as solved.

## VLM evaluation guide

Source: <https://learnopencv.com/vlm-evaluation-metrics>

Key takeaways:

- No single test covers VLM ability.
- Evaluation should be task-specific: VQA, document/chart/OCR, grounding, captioning.
- Language priors can make models answer without visual evidence, which is why balanced/evidence-focused evals matter.

## LLaVA architecture explainer

Source: <https://mbrenndoerfer.com/writing/llava-architecture-visual-instruction-tuning>

Key takeaways:

- LLaVA demonstrates a practical recipe: frozen vision encoder, lightweight projection layer, pretrained LLM, visual instruction tuning.
- The connector maps visual features into the LLM embedding space.
- The repo’s beginner explanation centers on this “seeing -> translating -> speaking” architecture.
