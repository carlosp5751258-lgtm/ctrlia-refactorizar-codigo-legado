# Refactor legacy code with Claude Code without breaking anything

[Leer en español](README.md) · The Spanish version lives in the repo root and in [README.md](README.md); the English files are in `en/`.

An example to practice the recipe's 5-step method: explore in plan mode, pin the current behavior with characterization tests, change in small steps with a commit each, and keep a way back with git and `/rewind`. It includes a 2014 billing function with real quirks, sample characterization tests, the prompts for each step and the block for your CLAUDE.md.

- Recipe in English: https://ctrlia.dev/en/recetas/refactorizar-codigo-legado.html
- Receta en español: https://ctrlia.dev/recetas/refactorizar-codigo-legado.html

## What's inside

| Path | What it is |
| --- | --- |
| `en/example/invoices.py` | The legacy code (12 lines, no tests) |
| `en/example/tests/test_invoices.py` | 12 sample characterization tests, written by Ctrl+IA to compare with yours |
| `en/prompts/explore.txt` | Step 1 prompt (in plan mode) |
| `en/prompts/characterization.txt` | Step 2 prompt (with `invoices.py` locked) |
| `en/prompts/refactor-step.txt` | Prompt for each small change |
| `en/claude-md-invoices.md` | The section for the project's CLAUDE.md |

## How to use it

You only need Python 3.

```bash
cd en/example
mv tests/test_invoices.py ../test_invoices.example.py   # so you can write your own with Claude
git init -q && git add -A && git commit -qm "before the refactor"

# Step 1: in plan mode (Shift+Tab), paste ../prompts/explore.txt
# Step 2: characterization tests with the code locked
claude --disallowedTools "Edit(invoices.py)"
# paste ../prompts/characterization.txt

python3 -m unittest discover -s tests -t .
git add tests && git commit -m "test: characterization of invoices.total"
```

Then make each small change with `en/prompts/refactor-step.txt` and one commit per change. If you only want to see the sample tests in action: `cd en/example && python3 -m unittest discover -s tests -t .`

## What was tested

With Python 3.12: the 12 sample tests pass with `invoices.py` as is; they still pass after a change of form (extracting `apply_vip`, renaming variables, `is None`), and fail if the function stops modifying its input list. With Claude Code **2.1.316** and `claude -p --model haiku --disallowedTools "Edit(facturas.py)"` (on the Spanish version), Claude wrote its own 10 characterization tests, which passed, and listed the quirks the recipe describes. `/rewind` was not run (it is interactive).

## License

MIT. See [LICENSE](LICENSE).

---
Part of **[Ctrl+IA](https://ctrlia.dev/en/)**: code with Claude Code like a pro. Made by Carlos P.
