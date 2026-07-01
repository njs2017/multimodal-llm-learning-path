# Start Here: Multimodal Models for Newcomers

If you are new to multimodal models, start here before reading papers.

## The one-sentence idea

A **multimodal model** is an AI model that can work with more than one kind of input or output, such as text, images, audio, video, documents, or actions.

Examples:

- Text + image -> answer a question about the image
- Text -> image
- Audio -> transcript and summary
- Video -> explanation of what happened
- Screenshot + goal -> UI action

## Why multimodal models matter

Most real-world information is not clean text.

People work with:

- Photos
- Screenshots
- PDFs
- Charts
- Diagrams
- Voice notes
- Videos
- Websites
- Apps
- Sensor data

Text-only LLMs are powerful, but they need help to understand the rest of the world. Multimodal models add that missing bridge.

## A simple analogy

Think of a text-only LLM as a very smart person who can only read typed text.

A multimodal LLM is closer to a person who can:

- Read text
- Look at images
- Listen to audio
- Watch video
- Inspect a screen
- Then answer or act

It still does not “see” like a human. Internally, everything becomes numbers called **embeddings** or **tokens**.

## The minimum vocabulary

You only need these ideas at first:

| Term | Plain meaning |
|---|---|
| Modality | A type of data: text, image, audio, video |
| Embedding | A list of numbers representing meaning |
| Encoder | Converts raw input, like an image, into embeddings |
| LLM | A language model that predicts and generates text |
| VLM | Vision-language model: image + text model |
| MLLM | Multimodal large language model |
| Connector | Small bridge between a vision/audio encoder and an LLM |
| Instruction tuning | Training the model to follow user requests |
| Grounding | Making sure answers are based on the actual image/audio/video |
| Hallucination | Saying something unsupported or false |

## The core architecture in plain English

Most beginner-friendly VLMs work like this:

```text
image -> vision model -> connector -> language model -> answer
text  -> tokenizer --------------------^ 
```

Meaning:

1. A vision model looks at the image and turns it into numbers.
2. A connector translates those numbers into a form the LLM can use.
3. The LLM combines the image information with your question.
4. The LLM writes the answer.

## The first thing to understand: matching is not reasoning

A model like CLIP can match images and text very well.

Example:

```text
Image: dog on beach
Text: "a dog running on the beach"
```

CLIP learns that those two belong together.

But matching is not the same as reasoning. It may struggle with:

- Counting exactly
- Reading small text
- Understanding charts
- Multi-step logic
- Ambiguous images
- Causal events in video

Modern multimodal LLMs build on these representation ideas but add language-model reasoning and instruction following.

## Recommended first week

### Day 1: Understand the landscape

Read:

- This file
- `beginner/01-what-is-multimodal-ai.md`
- `beginner/02-core-mental-model.md`

Watch:

- Hugging Face VLM intro: <https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro>
- Martin Is A Dad MLLM intro: <https://www.youtube.com/watch?v=jjdKfk89yAM>

### Day 2: Learn CLIP

Read:

- `beginner/03-clip-before-llava.md`
- `curriculum/01-foundations.md`

Watch:

- Samuel Albanie CLIP lecture: <https://www.youtube.com/watch?v=BcfAkQagEWU>

### Day 3: Learn the bridge architecture

Read:

- `beginner/04-from-clip-to-vlm.md`
- `curriculum/02-architectures.md`

Goal: explain this sentence:

> A VLM often connects a vision encoder to an LLM using a trainable projector or query module.

### Day 4: Learn training stages

Read:

- `beginner/05-training-without-the-math.md`
- `curriculum/03-training-pipeline.md`

Goal: explain pretraining, connector alignment, instruction tuning, and preference alignment.

### Day 5: Try models

Do:

- Use ChatGPT/Gemini/Claude vision or an open VLM.
- Upload 5 images.
- Ask easy and hard questions.
- Record where it succeeds and fails.

### Day 6-7: Build tiny intuition

Do:

- `labs/01-clip-retrieval.md`
- Start `labs/04-vlm-evaluation-harness.md`

## Beginner learning path

Follow this order:

1. `START_HERE.md`
2. `beginner/01-what-is-multimodal-ai.md`
3. `beginner/02-core-mental-model.md`
4. `beginner/03-clip-before-llava.md`
5. `beginner/04-from-clip-to-vlm.md`
6. `beginner/05-training-without-the-math.md`
7. `beginner/06-how-to-read-vlm-papers.md`
8. `beginner/07-common-misconceptions.md`
9. `course/syllabus.md`
10. `resources/youtube-videos.md`
11. `labs/01-clip-retrieval.md`
12. `quizzes/00-vocabulary.md`

## What not to do first

Do not start with:

- Implementing PaliGemma from scratch
- Reading every benchmark paper
- Training a model from scratch
- Jumping into RLHF/DPO math
- Comparing leaderboards without understanding tasks

Start with concepts, examples, and failure cases.

## Your first milestone

You are ready to move beyond newcomer material when you can explain:

1. What a modality is.
2. What CLIP learns.
3. Why CLIP is not enough for chat.
4. How a vision encoder connects to an LLM.
5. What visual instruction tuning does.
6. Why multimodal hallucination is different from text hallucination.
7. Why OCR, counting, charts, and video are hard.
