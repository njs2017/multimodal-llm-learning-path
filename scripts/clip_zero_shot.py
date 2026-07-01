#!/usr/bin/env python3
"""Beginner CLIP zero-shot image classification demo.

Usage:
  python scripts/clip_zero_shot.py --image path/to/image.jpg --labels "cat,dog,car"

This intentionally uses Hugging Face's zero-shot-image-classification pipeline,
matching the official Transformers task guide.
"""
import argparse
from transformers import pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Local image path or URL")
    parser.add_argument("--labels", required=True, help="Comma-separated candidate labels")
    parser.add_argument("--model", default="openai/clip-vit-base-patch32")
    args = parser.parse_args()

    labels = [x.strip() for x in args.labels.split(",") if x.strip()]
    if not labels:
        raise SystemExit("Provide at least one label")

    clf = pipeline("zero-shot-image-classification", model=args.model)
    results = clf(args.image, candidate_labels=labels)
    for row in results:
        print(f"{row['label']}\t{row['score']:.4f}")


if __name__ == "__main__":
    main()
