# Refactor legacy code with Claude Code without breaking anything

[Leer en español](README.md)

An example to practice the recipe's 5-step method: explore in plan mode, pin the current behavior with characterization tests, change in small steps with a commit each, and keep a way back with git and `/rewind`. It includes a 2014 billing function with real quirks, sample characterization tests, the prompts for each step and the block for your CLAUDE.md.

- Recipe in English: https://ctrlia.dev/en/recetas/refactorizar-codigo-legado.html
- Receta en español: https://ctrlia.dev/recetas/refactorizar-codigo-legado.html

## What's inside

| Path | What it is |
| --- | --- |
| `ejemplo/facturas.py` | The legacy code (12 lines, no tests) |
| `ejemplo/tests/test_facturas.py` | 12 sample characterization tests, written by Ctrl+IA to compare with yours |
| `prompts/explorar.txt` | Step 1 prompt (in plan mode) |
| `prompts/caracterizacion.txt` | Step 2 prompt (with `facturas.py` locked) |
| `prompts/paso-refactor.txt` | Prompt for each small change |
| `claude-md-facturas.md` | The section for the project's CLAUDE.md |

The prompts, test names and CLAUDE.md block are in Spanish.

## How to use it

You only need Python 3.

```bash
cd ejemplo
mv tests/test_facturas.py ../test_facturas.ejemplo.py   # so you can write your own with Claude
git init -q && git add -A && git commit -qm "antes del refactor"

# Step 1: in plan mode (Shift+Tab), paste prompts/explorar.txt
# Step 2: characterization tests with the code locked
claude --disallowedTools "Edit(facturas.py)"
# paste ../prompts/caracterizacion.txt

python3 -m unittest discover -s tests -t .
git add tests && git commit -m "test: caracterización de facturas.total"
```

Then make each small change with `prompts/paso-refactor.txt` and one commit per change. If you only want to see the sample tests in action: `cd ejemplo && python3 -m unittest discover -s tests -t .`

## What was tested

With Python 3.12: the 12 sample tests pass with `facturas.py` as is; they still pass after a change of form (extracting `aplicar_vip`, renaming variables, `is None`), and fail if the function stops modifying its input list. With Claude Code **2.1.316** and `claude -p --model haiku --disallowedTools "Edit(facturas.py)"`, Claude wrote its own 10 characterization tests, which passed, and listed the quirks the recipe describes. `/rewind` was not run (it is interactive).

## License

MIT. See [LICENSE](LICENSE).

---
Part of **[Ctrl+IA](https://ctrlia.dev/en/)**: code with Claude Code like a pro. Made by Carlos P.
