# Glossary

**Adapter**: Small trainable module inserted between or inside larger frozen models.

**Alignment**: Making model behavior match intended goals, user preferences, safety requirements, or cross-modal correspondence.

**Any-to-any model**: A model that can accept and generate multiple modalities, such as text, image, audio, video, and speech.

**CLIP**: Contrastive Language-Image Pretraining; aligns image and text encoders using paired image-caption data.

**Connector / projector**: Module that maps vision/audio embeddings into a representation the LLM can consume.

**Cross-attention**: Attention mechanism where one stream, e.g. text tokens, attends to another stream, e.g. visual features.

**DPO**: Direct Preference Optimization; a preference tuning method using chosen/rejected response pairs without training a separate reward model.

**Grounding**: Linking generated text to evidence in the input, such as a region in an image or timestamp in a video.

**Instruction tuning**: Fine-tuning on instruction-response examples so a model follows user requests.

**MLLM**: Multimodal Large Language Model.

**OCR**: Optical Character Recognition; extracting text from images/documents/screenshots.

**Q-Former**: Query Transformer used in BLIP-2 to extract useful visual information for a language model.

**Resampler**: Module that compresses many visual tokens into a smaller set of tokens.

**SFT**: Supervised fine-tuning, usually on instruction-response examples.

**VLM**: Vision-Language Model.

**VLA**: Vision-Language-Action model, often used for robotics or GUI agents.

**Visual hallucination**: Claiming visual content that is not present or not supported by the image/video/document.

**Visual instruction tuning**: Instruction tuning where prompts include visual inputs.
