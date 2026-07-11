# Lab 00 - Your First Multimodal Evaluation

**Time:** 15 minutes  
**Cost:** free  
**Hardware:** any Mac, Linux, or Windows computer  
**Model download:** none

## Why start with evaluation?

You do not need to train a model to begin learning multimodal AI. First, learn to ask a more important question: **how do I know whether a model actually used the image?**

This lab gives you a complete loop:

```text
image + question -> model answer -> expected behavior -> score -> failure analysis
```

The included answers are synthetic, so the first run is deterministic. In the next step, replace them with answers from any vision model you can access.

## 1. Clone and enter the repository

```bash
git clone https://github.com/barvhaim/multimodal-llm-learning-path.git
cd multimodal-llm-learning-path
```

Check that Python 3.10 or newer is available:

```bash
python3 --version
```

## 2. Run the scorer

No packages are required:

```bash
python3 scripts/score_vlm_eval.py \
  --eval evaluation/eval-template.jsonl \
  --predictions evaluation/sample-predictions.jsonl
```

You should see four expected cases. Two pass, one is blocked because it contains a specifically forbidden hallucination, and one is unanswered.

Ask yourself:

- Why should an unanswered example count against accuracy?
- Why does a forbidden answer override a partially correct phrase?
- What can substring matching fail to measure?

## 3. Inspect the evaluation data

Open these two files:

- [`evaluation/eval-template.jsonl`](../evaluation/eval-template.jsonl): prompts, acceptable answers, forbidden claims, and rubrics.
- [`evaluation/sample-predictions.jsonl`](../evaluation/sample-predictions.jsonl): model outputs keyed by example ID.

Each line is one JSON object. This format is called **JSONL**.

## 4. Evaluate a real model

Choose any vision-capable model you can access. You can use a hosted chat product; no API key is necessary.

1. Find or create four images: a readable sign, several repeated objects, a chart, and a deliberately blurry detail.
2. Ask the prompts from the evaluation template.
3. Copy the answers into a new file named `evaluation/my-predictions.jsonl`.
4. Keep each original `id` unchanged.
5. Run:

```bash
python3 scripts/score_vlm_eval.py \
  --eval evaluation/eval-template.jsonl \
  --predictions evaluation/my-predictions.jsonl
```

> The template's image paths are placeholders. Your four images do not need those filenames unless you later automate model inference.

## 5. Write a failure report

Create `experiments/first-eval-report.md`:

```markdown
# First multimodal evaluation

## Model and setup
- Model:
- Date:
- Prompting method:

## Results
- Correct:
- Incorrect:
- Unsupported claims:
- Honest uncertainty:

## Most important failure

## What I would test next
```

Do not report only the accuracy. Describe whether the failure came from OCR, counting, chart reasoning, poor grounding, or failure to admit uncertainty.

## What you learned

After this lab, you should be able to explain:

- Why a benchmark needs explicit expected behavior.
- Why missing predictions belong in the denominator.
- Why deterministic matching is useful but limited.
- Why qualitative failure analysis matters alongside one score.

## Next step

Continue with [`01-clip-retrieval.md`](01-clip-retrieval.md) to learn the difference between image-text matching and reasoning.
