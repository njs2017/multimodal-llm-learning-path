# 06 - How to Read VLM Papers as a Newcomer

Most multimodal papers are dense. Use this checklist instead of trying to understand every equation first.

## Step 1 - Identify the task

Ask:

- Is this model for image understanding?
- Document QA?
- Video understanding?
- Audio/speech?
- Image generation?
- Robotics/actions?
- Any-to-any input/output?

Write one sentence:

> This paper is trying to improve ______.

## Step 2 - Identify the modalities

Fill this in:

```text
Inputs: text / image / audio / video / document / screen / sensor
Outputs: text / image / audio / action / bounding box / mask
```

## Step 3 - Draw the architecture

Do not start with equations. Draw boxes.

Look for:

- Vision encoder
- Audio/video encoder
- LLM backbone
- Connector/projector/Q-Former/resampler
- Cross-attention
- Tokenizer
- Output head

## Step 4 - Ask what is frozen

Important question:

```text
Which modules are frozen and which are trained?
```

This tells you cost and design philosophy.

## Step 5 - Identify training stages

Most papers have stages like:

1. Pretraining / feature alignment
2. Instruction tuning
3. Preference alignment
4. Task-specific fine-tuning

Write the data used in each stage.

## Step 6 - Inspect data, not only architecture

For modern VLMs, data often matters as much as architecture.

Ask:

- How many examples?
- Human or synthetic?
- What tasks?
- OCR included?
- Documents included?
- Video included?
- Safety included?
- Any filtering/quality control?

## Step 7 - Understand evaluation

Do not trust one benchmark.

Group benchmarks by capability:

- General VQA
- OCR
- Chart/document reasoning
- Math/science diagrams
- Hallucination
- Video
- Agent/UI
- Safety

## Step 8 - Find the limitations

Good papers usually reveal what still fails.

Common limitations:

- Weak grounding
- Hallucination
- Poor small-text OCR
- Video frame sampling issues
- High compute cost
- Dataset contamination
- Weak real-world UI performance

## One-page paper note template

```md
# Paper title

- URL:
- Problem:
- Modalities:
- Inputs:
- Outputs:
- Architecture in one diagram:
- Backbone models:
- Connector/fusion method:
- Training stages:
- Data used:
- Benchmarks:
- Main result:
- Biggest limitation:
- What I learned:
- What I would test myself:
```
