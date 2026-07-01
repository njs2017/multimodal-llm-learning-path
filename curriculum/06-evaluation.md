# 06 - Evaluation and Failure Modes

## Core question

How do we know whether a multimodal model actually understands the input?

## Evaluation dimensions

### Perception

- Object recognition
- Counting
- Color/attribute recognition
- OCR
- Spatial relations
- Grounding/localization

### Reasoning

- Multi-step VQA
- Science/math diagrams
- Charts and tables
- Multi-image comparison
- Causal/physical reasoning
- Video temporal reasoning

### Instruction following

- Does it answer the actual question?
- Does it ask for clarification when needed?
- Does it refuse unsafe requests?
- Does it preserve text-only abilities?

### Groundedness and hallucination

- Does every claim come from the image/document/video?
- Does it admit uncertainty?
- Does it fabricate invisible details?

### Efficiency

- Visual token count
- Latency
- Memory
- Throughput
- Context length pressure

## Benchmark families

Study benchmark categories rather than chasing one leaderboard:

- VQA: VQAv2, GQA, OK-VQA
- Multimodal reasoning: ScienceQA, MMMU, MathVista, MM-Vet
- OCR/document: TextVQA, DocVQA, ChartQA, InfographicVQA
- Hallucination: POPE-style object hallucination checks and newer VLM hallucination suites
- Video: VideoQA and long-video understanding benchmarks
- Agent/UI: screen/browser/GUI task benchmarks

## Build your own mini eval

Create 30 examples:

- 5 photos with obvious answer
- 5 photos with ambiguous answer
- 5 screenshots
- 5 charts
- 5 document pages
- 5 multi-image comparisons

For each, define:

- Expected answer
- Acceptable uncertainty
- Failure modes
- Scoring rubric

## Output artifact

A small evaluation suite in JSONL format:

```jsonl
{"id":"ocr_001","modality":"image","prompt":"What number is on the sign?","expected":"47","failure_modes":["reads 42","overconfident"]}
```
