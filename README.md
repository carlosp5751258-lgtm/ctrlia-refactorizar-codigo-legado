# Refactorizar código legado con Claude Code sin romper nada

[Read in English](README.en.md)

Un ejemplo para practicar el método de 5 pasos de la receta: explorar en modo plan, fijar el comportamiento actual con tests de caracterización, cambiar en pasos pequeños con commit y tener un camino de vuelta con git y `/rewind`. Incluye una función de facturación de 2014 con rarezas reales, unos tests de caracterización de ejemplo, los prompts de cada paso y el bloque para tu CLAUDE.md.

- Receta en español: https://ctrlia.dev/recetas/refactorizar-codigo-legado.html
- Recipe in English: https://ctrlia.dev/en/recetas/refactorizar-codigo-legado.html

## Qué incluye

| Ruta | Qué es |
| --- | --- |
| `ejemplo/facturas.py` | El código heredado (12 líneas, sin tests) |
| `ejemplo/tests/test_facturas.py` | 12 tests de caracterización de ejemplo, escritos por Ctrl+IA para comparar con los tuyos |
| `prompts/explorar.txt` | Prompt del paso 1 (en modo plan) |
| `prompts/caracterizacion.txt` | Prompt del paso 2 (con `facturas.py` bloqueado) |
| `prompts/paso-refactor.txt` | Prompt para cada cambio pequeño |
| `claude-md-facturas.md` | La sección para el CLAUDE.md del proyecto |

## Cómo usarlo

Solo necesitas Python 3.

```bash
cd ejemplo
mv tests/test_facturas.py ../test_facturas.ejemplo.py   # para escribir los tuyos con Claude
git init -q && git add -A && git commit -qm "antes del refactor"

# Paso 1: en modo plan (Shift+Tab), pega prompts/explorar.txt
# Paso 2: tests de caracterización con el código bloqueado
claude --disallowedTools "Edit(facturas.py)"
# pega ../prompts/caracterizacion.txt

python3 -m unittest discover -s tests -t .
git add tests && git commit -m "test: caracterización de facturas.total"
```

Después, cada cambio pequeño con `prompts/paso-refactor.txt` y un commit por cambio. Si solo quieres ver los tests de ejemplo en acción: `cd ejemplo && python3 -m unittest discover -s tests -t .`

## Qué se probó

Con Python 3.12: los 12 tests de ejemplo pasan con `facturas.py` tal cual; siguen pasando tras un refactor de forma (extraer `aplicar_vip`, renombrar variables, `is None`), y fallan si la función deja de modificar la lista de entrada. Con Claude Code **2.1.316** y `claude -p --model haiku --disallowedTools "Edit(facturas.py)"`, Claude escribió sus propios 10 tests de caracterización, que pasaron, y listó las rarezas que describe la receta. `/rewind` no se ejecutó (es interactivo).

## Licencia

MIT. Ver [LICENSE](LICENSE).

---
Parte de **[Ctrl+IA](https://ctrlia.dev/)**: programa con Claude Code como un pro, en español. Hecho por Carlos P.
