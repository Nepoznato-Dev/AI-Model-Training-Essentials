# Changes for V2

## Remaining audit priorities

- CNN/computer-vision: verify train-only normalization, non-random validation/test transforms, class counts, output dimensions, parameter counts, and benchmark claims.
- RAG: add retrieval metrics (Recall@k/MRR where labels exist), grounding checks, malformed/empty/duplicate/oversized-context tests, and separate retrieval quality from answer quality.
- Cloud/deployment: verify provider SDK APIs, versions, authentication, health checks, timeouts, retries, logging, secrets handling, and failure behavior.
- Knowledge base: protect dates, URLs, model names, versions, code blocks, frontmatter, paths, and identifiers from transformation scripts; add source/revision metadata for time-sensitive facts.
- Translation: track the English source revision, stale/current status, missing sections, structural divergence, and protected technical metadata.
- Agent Modes/Skills: formalize YAML metadata with JSON Schema, validate tool/agent references and handoff targets, and separate descriptive instructions from executable permissions.

## V2 validation gates

```text
[ ] Markdown links resolve
[ ] UTF-8 is valid and BOM-free
[ ] Frontmatter validates against schema
[ ] Python examples compile
[ ] Lightweight smoke tests pass
[ ] Runnable examples have documented dependencies
[ ] No deprecated API is used without an explicit warning
[ ] Performance claims include hardware/methodology context
[ ] Time-sensitive claims have a verification date
[ ] Translation maps to the current English source revision
[ ] Protected metadata is unchanged by automation
[ ] Security examples receive separate review
[ ] Test data is never used for hyperparameter/model selection
[ ] Monitoring alerts reference real exported metrics
[ ] RAG retrieval and generation quality are evaluated separately
```

## Knowledge-base date incident

A prior content-processing script accidentally changed dates to 2026 in parts of the knowledge base. Treat this as a data-pipeline bug rather than manually fixing individual files forever.

Protect dates, URLs, model names, version numbers, code blocks, YAML frontmatter, file paths, and identifiers from translation/transformation scripts, and add a regression test comparing protected metadata before and after transformation.

## Philosophy for V2

Do not sacrifice the repository's breadth. The main improvement needed is **verification**, not a reduction in ambition. The existing guides, projects, knowledge, skills, and agent modes are worth keeping; V2 should make them machine-validatable and reproducible.
