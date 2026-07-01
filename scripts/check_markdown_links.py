#!/usr/bin/env python3
"""Check local Markdown links in this repository."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
missing=[]
for md in ROOT.rglob("*.md"):
    text=md.read_text(encoding="utf-8")
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        link=match.group(1).split("#")[0]
        if not link or link.startswith(("http://","https://","mailto:")):
            continue
        if not (md.parent / link).resolve().exists():
            missing.append((md.relative_to(ROOT), link))
if missing:
    for src, link in missing:
        print(f"MISSING {src}: {link}")
    raise SystemExit(1)
print("All local Markdown links resolved")
