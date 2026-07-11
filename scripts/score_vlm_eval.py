#!/usr/bin/env python3
"""Score a small, deterministic VLM evaluation set.

This intentionally uses simple text matching. It is a teaching tool for learning
about evaluation design, not a universal semantic judge.
"""

import argparse
import json
from pathlib import Path
from typing import Any


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Read JSON objects from a JSONL file with useful error messages."""
    rows: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(
        Path(path).read_text(encoding="utf-8").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON on line {line_number} of {path}: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"Line {line_number} of {path} must be a JSON object")
        rows.append(row)
    return rows


def index_unique(rows: list[dict[str, Any]], source: str) -> dict[str, dict[str, Any]]:
    """Index rows by ID and reject absent or duplicate IDs."""
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        row_id = str(row.get("id", "")).strip()
        if not row_id:
            raise ValueError(f"Every row in {source} needs a non-empty 'id'")
        if row_id in indexed:
            raise ValueError(f"Duplicate id '{row_id}' in {source}")
        indexed[row_id] = row
    return indexed


def normalize(value: Any) -> str:
    """Normalize text for this deliberately simple scorer."""
    return " ".join(str(value).casefold().split())


def score(
    eval_rows: list[dict[str, Any]], prediction_rows: list[dict[str, Any]]
) -> dict[str, Any]:
    """Score all expected examples, including unanswered ones in the denominator."""
    expected = index_unique(eval_rows, "evaluation file")
    predictions = index_unique(prediction_rows, "predictions file")

    details: list[dict[str, str]] = []
    correct = blocked = unanswered = 0

    for row_id, example in expected.items():
        prediction = predictions.get(row_id)
        if prediction is None:
            unanswered += 1
            details.append({"id": row_id, "status": "unanswered"})
            continue

        answer = normalize(prediction.get("answer", ""))
        acceptable = [normalize(item) for item in example.get("acceptable", [])]
        forbidden = [normalize(item) for item in example.get("must_not_include", [])]

        has_forbidden = any(item and item in answer for item in forbidden)
        has_acceptable = any(item and item in answer for item in acceptable)
        if has_forbidden:
            blocked += 1
            status = "blocked"
        elif has_acceptable:
            correct += 1
            status = "correct"
        else:
            status = "incorrect"
        details.append({"id": row_id, "status": status})

    unexpected = sorted(set(predictions) - set(expected))
    total = len(expected)
    return {
        "total": total,
        "correct": correct,
        "blocked": blocked,
        "incorrect": total - correct - blocked - unanswered,
        "unanswered": unanswered,
        "unexpected": len(unexpected),
        "unexpected_ids": unexpected,
        "accuracy": correct / total if total else 0.0,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eval", required=True, help="Expected JSONL examples")
    parser.add_argument("--predictions", required=True, help="Model answers as JSONL")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    result = score(read_jsonl(args.eval), read_jsonl(args.predictions))
    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(
        " ".join(
            f"{key}={result[key]}"
            for key in (
                "total",
                "correct",
                "incorrect",
                "blocked",
                "unanswered",
                "unexpected",
            )
        )
        + f" accuracy={result['accuracy']:.3f}"
    )
    for detail in result["details"]:
        print(f"{detail['id']}\t{detail['status']}")


if __name__ == "__main__":
    main()
