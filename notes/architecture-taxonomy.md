# Architecture Taxonomy

## Timeline-style view

### 1. Contrastive / dual encoder era

Representative idea: CLIP.

- Separate image and text encoders.
- Train on paired image-text data.
- Great for retrieval and zero-shot classification.
- Not naturally conversational.

### 2. Multimodal encoder-decoder era

Representative ideas: BLIP, OFA-like systems, captioning/VQA models.

- Fuse vision and language for generation.
- Good for captioning and VQA.
- Less centered on LLM instruction-following.

### 3. LLM-backed bridge era

Representative ideas: Flamingo, BLIP-2, LLaVA, InstructBLIP.

- Reuse a strong pretrained LLM.
- Add a vision encoder and connector.
- Train connector and/or fine-tune LLM.
- Most accessible open-source recipe.

### 4. Native/unified multimodal era

Representative ideas: Chameleon/Emu3/Janus-style and omni models.

- Images/audio/video/text become tokens or shared representations.
- Can support richer input/output combinations.
- Expensive and still rapidly evolving.

### 5. Multimodal agent era

Representative ideas: GUI agents, browser agents, robotics VLA models.

- Model sees state and emits actions.
- Evaluation becomes task success, not just answer quality.
- Requires grounding, verification, and guardrails.

## Design axes

| Axis | Options |
|---|---|
| Input modalities | text, image, document, video, audio, screen, sensor |
| Output modalities | text, speech, image, action, bounding box, tool call |
| Fusion point | early, mid, late, cross-attention, unified tokens |
| Backbone | LLM-centric, vision-centric, native multimodal |
| Training | from scratch, frozen modules, partial fine-tuning, LoRA |
| Alignment | SFT, DPO, RLHF, RLAIF, rejection sampling, GRPO-style |
| Evaluation | perception, OCR, reasoning, grounding, safety, agents |
