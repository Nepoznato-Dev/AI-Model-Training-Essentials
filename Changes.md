# Changes for V2

This file is an integration checklist for the next version of AI-Model-Training-Essentials. It summarizes the reliability work completed on the `agent/reliability-pass-v1` branch and is intentionally written so it can be copied into the V2 VS Code project.

## 1. Repository validation

### Added
- `tools/validate_repo.py`
  - UTF-8 validation
  - UTF-8 BOM detection
  - suspicious mojibake detection
  - YAML frontmatter sanity checks for `skills/` and `agent_modes/`
  - broken relative Markdown-link detection
  - Python syntax compilation checks

### Add to V2
Copy the validator into `tools/` and extend it as the V2 schema develops. The current validator is deliberately lightweight; it should eventually also validate project metadata, translation parity, protected dates, dependency references, and runnable examples.

## 2. Continuous integration

### Added
- `.github/workflows/repository-quality.yml`
- Runs repository validation on pushes to `main` and pull requests.
- Uses Python 3.11.

### V2 recommendation
Expand CI into separate jobs:
1. documentation/metadata validation
2. Python syntax validation
3. runnable-example tests
4. link checking
5. dependency/security scanning
6. translation parity checks

## 3. Dependency cleanup

### Added
- `requirements/base.txt`

### Changed
- Root `requirements.txt` is now explicitly marked as a legacy compatibility file.
- Broad dependencies were given upper bounds to reduce accidental major-version drift.

### V2 recommendation
Prefer a project-level `pyproject.toml`, lockfile, focused optional dependency groups, and per-project environments instead of one giant environment.

Suggested structure:

```text
requirements/
  base.txt
  vision.txt
  transformers.txt
  rag.txt
  agents.txt
  deployment.txt
  dev.txt
```

## 4. Model-development fixes

The first pass fixed scheduler signatures, gradient accumulation, Dropout/BatchNorm examples, a missing `SVC` import, deprecated Optuna calls, dynamic quantization, knowledge-distillation teacher gradients, and overconfident reproducibility wording.

## 5. Security fixes

The first pass modernized FGSM/PGD gradient handling, adversarial training, SlowAPI, Pydantic v2, key handling, model artifact guidance, audit timestamps, and agent-specific security controls.

## 6. Second-pass fixes

### `wiki/deployment.md`
- Fixed the Docker health check by installing `curl` and documented alternatives.
- Replaced the broken/missing `BatchPredictor._try_process_batch` path with an actual timeout flush implementation.
- Added locking and exception propagation to the batching example so callers do not hang when inference fails.
- Replaced process-randomized Python `hash()` cache keys with stable JSON serialization.
- Made Redis cache serialization explicit.
- Updated generic Docker/Compose examples toward Python 3.11 and modern `docker compose` usage.
- Added safer API error handling and timezone-aware timestamps.
- Removed obsolete Azure deployment code from the main example and replaced it with a version-aware warning.
- Updated GitHub Actions examples from checkout/setup-python v3/v4 to v4/v5.
- Added warnings around credentials and provider SDK version drift.

### `guides/projects/rag_simple/main.py`
- Corrected the `all-MiniLM-L6-v2` embedding documentation: the code now reports the actual dimension instead of claiming 768.
- Normalized embeddings before cosine similarity.
- Added empty-dataset and `top_k` validation.
- Made multi-document context handling explicit.
- Added a grounded-answer instruction telling the generator to admit when the context does not contain the answer.
- Removed misleading claims about production readiness/runtime.

## 7. Remaining high-priority audit work

- CNN/ML examples need train/validation/test separation where hyperparameters are tuned.
- Transfer-learning example has an incorrect trainable-parameter count and needs explicit BatchNorm/frozen-backbone behavior.
- Decision-boundary plotting needs consistent scaled/raw coordinate handling.
- Text-generation examples need correct `do_sample`/temperature semantics.
- Remaining cloud examples need version/date verification and current-provider API validation.
- Monitoring examples need real metric instrumentation rather than isolated metric names.
- RAG examples need retrieval/generation evaluation, chunking guidance, and a clear grounded-answer policy.
- Agent-mode frontmatter needs a machine-readable schema and tool registry.
- Translation files need source-revision metadata, review status, and parity checks.
- Knowledge-base date fields need protection from content-processing scripts.
- Add runnable-example CI where examples have deterministic/lightweight test paths.

## 8. Knowledge-base date incident

A prior content-processing script accidentally changed dates to 2026 in parts of the knowledge base. Treat this as a data-pipeline bug rather than manually fixing individual files forever.

### V2 recommendation
Protect these fields from translation/transformation scripts:
- dates
- URLs
- model names
- version numbers
- code blocks
- YAML frontmatter
- file paths
- identifiers

Add a regression test that compares protected metadata before and after transformation.

## 9. Recommended V2 validation gates

Before merging future content:

```text
[ ] Markdown links resolve
[ ] UTF-8 is valid and BOM-free
[ ] Frontmatter validates against schema
[ ] Python examples compile
[ ] Runnable examples have dependencies
[ ] Runnable examples execute in their documented environment
[ ] No deprecated API is used without an explicit warning
[ ] Performance claims have hardware/methodology context
[ ] Time-sensitive claims have a verification date
[ ] Translation maps to the current English source revision
[ ] Protected metadata is unchanged by automation
[ ] Security examples are reviewed separately
```

## 10. Important philosophy for V2

Do not sacrifice the repository's breadth. The main improvement needed is **verification**, not a reduction in ambition.

The existing structure—guides, projects, knowledge, skills, and agent modes—is worth keeping. V2 should make those pieces machine-validatable and reproducible rather than replacing them.
