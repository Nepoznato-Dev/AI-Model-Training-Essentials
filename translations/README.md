# Translation scaffolding

This directory defines the translation layout for the repository's four
document collections:

- `skills/`
- `wiki/`
- `guides/`
- `agent_modes/`

The canonical language list contains 52 targets in
[`languages.txt`](languages.txt). Translated files should be created under:

```text
translations/<Language>/<collection>/<source-relative-path>.md
```

For example, the future Spanish version of `wiki/getting_started.md` belongs
at `translations/Spanish/wiki/getting_started.md`.

No translations are included by this scaffolding. Run the generator to create
explicit placeholders for every Markdown source document before translation
work begins:

```bash
python scripts/scaffold_translations.py --create
```

The generator never copies source content. It only creates a short,
machine-readable placeholder that identifies the source file and language.
Use `--check` in automation to verify that all expected placeholder or
translated files exist.
