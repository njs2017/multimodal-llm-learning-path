# Leaderboards Are Not Enough

A high VLM benchmark score is useful, but it does not prove the model will work for your use case.

## Why

VLMs are not one-skill systems. A model can be strong at one ability and weak at another.

Examples:

- Good at general VQA but weak at OCR.
- Good at OCR but weak at charts.
- Good at static images but weak at video timing.
- Good at benchmark diagrams but weak on your internal screenshots.
- Good at answering but bad at saying “not enough evidence.”

## Benchmark families measure different things

| Family | What it tests | What it may miss |
|---|---|---|
| VQA | General image questions | OCR, charts, exact grounding |
| OCR/document | Text reading and layout | Commonsense visual reasoning |
| Chart QA | Axes, values, trends | Natural image understanding |
| MMMU/ScienceQA | Academic multimodal reasoning | Product screenshots and noisy user data |
| Hallucination tests | Unsupported visual claims | Task success and helpfulness |
| Video QA | Temporal understanding | Static document and OCR ability |
| Agent/UI tasks | Acting on screens | General world knowledge |

## Failure modes hidden by leaderboards

### Language priors

The model answers from common patterns instead of the image.

Example:

> “What color is the banana?” -> “yellow” even if the image shows a green banana.

### Dataset contamination

The model may have seen similar benchmark examples during training.

### Multiple-choice inflation

Multiple-choice scores can be higher than open-ended production performance.

### Weak uncertainty

Many benchmarks reward answering, not calibrated refusal.

### Prompt sensitivity

Small prompt changes can alter results.

### Latency and cost

A model can be accurate but too slow or expensive.

## Build a product-specific eval

For your use case, create 50-200 examples from real data:

- Normal cases
- Edge cases
- Ambiguous cases
- Unanswerable cases
- Safety-sensitive cases
- Low-quality images

Track:

```text
Accuracy | hallucination rate | uncertainty quality | latency | cost | severity of errors
```

## Rule of thumb

Use public benchmarks to shortlist models. Use your own eval to choose models.
