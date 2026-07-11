# Contributing

Contributions that make the learning path clearer, more reproducible, or more current are welcome.

## Good contributions

- Fix a broken command or link.
- Add a small Mac/Linux/Windows-tested lab.
- Add a failure case with a reproducible input and expected behavior.
- Clarify a difficult concept without adding unnecessary jargon.
- Update a model or paper entry with a primary-source link and access date.

Please avoid large generated reading lists, benchmark claims without sources, or notebooks that depend on private services without saying so.

## Local quality checks

The core checks do not download a model:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_markdown_links.py
```

For linting:

```bash
python3 -m pip install 'ruff>=0.9,<1'
ruff check scripts tests
```

To run the optional CLIP demo, use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
python3 -m pip install -r requirements.txt
python3 scripts/clip_zero_shot.py --help
```

## Pull requests

Keep each pull request focused. Explain:

1. What a learner could not do or understand before.
2. What changed.
3. Exact commands you ran.
4. Hardware or service requirements.
5. Any limitations that remain.
