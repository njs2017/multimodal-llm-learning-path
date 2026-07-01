#!/usr/bin/env python3
"""Tiny exact/substring scorer for beginner VLM eval JSONL files.

It expects a predictions JSONL with:
  {"id": "ocr_001", "answer": "..."}

And an eval JSONL with:
  {"id": "ocr_001", "acceptable": ["47"], "must_not_include": ["42"]}

This is not a universal evaluator. It is a teaching tool for building intuition.
"""
import argparse, json
from pathlib import Path


def read_jsonl(path):
    rows=[]
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--eval", required=True)
    ap.add_argument("--predictions", required=True)
    args=ap.parse_args()
    eval_rows={r["id"]:r for r in read_jsonl(args.eval)}
    pred_rows=read_jsonl(args.predictions)
    total=correct=blocked=missing=0
    for pred in pred_rows:
        total += 1
        ex=eval_rows.get(pred.get("id"))
        if not ex:
            missing += 1
            continue
        ans=str(pred.get("answer","")).lower()
        bad=any(str(x).lower() in ans for x in ex.get("must_not_include",[]))
        ok=any(str(x).lower() in ans for x in ex.get("acceptable",[]))
        if bad:
            blocked += 1
        elif ok:
            correct += 1
    print(f"total={total} correct={correct} blocked={blocked} missing={missing} accuracy={correct/max(total,1):.3f}")


if __name__ == "__main__":
    main()
