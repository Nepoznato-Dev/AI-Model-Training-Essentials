# Changes for V2

This file is the integration checklist for the next version of AI-Model-Training-Essentials. It summarizes the reliability work completed on `agent/reliability-pass-v1` and is written so it can be copied into the V2 VS Code project.

## 1. Repository validation

### Added
- `tools/validate_repo.py`
  - UTF-8 validation
  - UTF-8 BOM detection
  - suspicious mojibake detection
  - YAML frontmatter sanity checks for `skills/` and `agent_modes/`
  - full YAML parsing for agent-mode metadata
  - required agent-mode metadata fields and types
  - filename/name consistency checks
  - handoff structure/type checks
  - agent-mode reference checks against files actually present in `agent_modes/`
  - broken relative Markdown-link detection
  - Python syntax compilation checks

### V2 recommendation
Extend the validator with project metadata, translation parity, protected dates, dependency references, runnable examples, and schema validation for other machine-readable content.

## 2. Continuous integration

### Added
- `.github/workflows/repository-quality.yml`
- Runs repository validation on pushes to `main` and pull requests.
- Uses Python 3.11.

### V2 recommendation
Expand CI into separate jobs for documentation/metadata validation, Python syntax, runnable examples, links, dependency/security scanning, and translation parity.

## 3. Dependency cleanup

### Added
- `requirements/base.txt`

### Changed
- Root `requirements.txt` is explicitly marked as a legacy compatibility environment.
- Broad dependencies have upper bounds to reduce accidental major-version drift.

### V2 recommendation
Prefer `pyproject.toml`, a lockfile, focused optional dependency groups, and per-project environments rather than one giant environment.

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

## 6. Deployment/RAG fixes

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
- Corrected the `all-MiniLM-L6-v2` embedding documentation: the model produces 384-dimensional embeddings, not 768.
- Normalized embeddings before cosine similarity.
- Added empty-dataset and `top_k` validation.
- Made multi-document context handling explicit.
- Added a grounded-answer instruction telling the generator to admit when the context does not contain the answer.
- Removed misleading claims about production readiness/runtime.

## 7. Transfer-learning fixes

### `guides/projects/transfer_learning/main.py`
- Added an explicit train/validation/test split.
- Prevented the test set from being used for checkpoint/model selection.
- Corrected the trainable-parameter count for the ResNet18 10-class head: 5,130 parameters.
- Kept the pretrained backbone frozen for the feature-extraction example.
- Added validation-based best-checkpoint selection.
- Evaluated the held-out test set only after model selection.
- Added reproducibility seeds.
- Improved checkpoint metadata so the saved model can be reconstructed correctly.
- Removed unsupported fixed claims such as guaranteed 85–90% accuracy, 5–10x speedup, and exact training times.
- Clarified that fine-tuning requires a separate strategy for selectively unfreezing pretrained layers.

## 8. Monitoring fixes

### `wiki/monitoring.md`
- Replaced universal GPU utilization thresholds with baseline/SLO-based guidance.
- Separated service health, model quality, data drift, and concept/performance drift.
- Replaced naive `datetime.utcnow()` usage with timezone-aware UTC timestamps.
- Removed automatic logging of full request bodies and added privacy/retention guidance.
- Fixed categorical drift guidance so category counts share the same category universe.
- Made PSI robust to duplicate quantile edges and empty/constant features.
- Clarified that statistical significance does not equal practical significance.
- Added actual Prometheus `Counter`/`Histogram` instrumentation instead of referring to metrics that were never defined.
- Added safer low-traffic handling to the error-rate alert expression.
- Fixed the custom alert example's missing datetime import.
- Removed the brittle hand-written Grafana JSON example and replaced it with version-aware guidance.
- Removed automatic retraining as the default response to drift detection.

## 9. Agent-mode validation

### `tools/validate_repo.py`
Agent modes now have an explicit machine-checkable metadata contract:
- `name`
- `description`
- `argument-hint`
- `tools`
- `agents`
- `handoffs`

The validator checks that:
- YAML parses successfully.
- Required fields exist and have the expected basic types.
- Mode filename matches the declared mode name.
- Tool and agent entries are non-empty strings.
- Handoffs have the expected fields and types.
- Referenced agents actually exist as `agent_modes/*.md` files.

This is deliberately a validation layer rather than a runtime agent framework; V2 can later promote the metadata into a formal JSON Schema/tool registry.

## 10. Remaining high-priority audit work

- CNN/ML examples need train/validation/test separation where hyperparameters are tuned.
- Decision-boundary plotting needs consistent scaled/raw coordinate handling.
- Text-generation examples need correct `do_sample`/temperature semantics.
- Remaining cloud examples need version/date verification and current-provider API validation.
- RAG examples need stronger retrieval/generation evaluation, chunking guidance, and benchmarkable groundedness tests.
- Translation files need source-revision metadata, review status, and parity checks.
- Knowledge-base date fields need protection from content-processing scripts.
- Add runnable-example CI where examples have deterministic/lightweight test paths.
- Audit remaining project scripts for dependency isolation and executable correctness.

## 11. Knowledge-base date incident

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

## 12. Recommended V2 validation gates

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
[ ] Test data is never used for hyperparameter/model selection
[ ] Monitoring alerts reference real exported metrics
```

## 13. Important philosophy for V2

Do not sacrifice the repository's breadth. The main improvement needed is **verification**, not a reduction in ambition.

The existing structure—guides, projects, knowledge, skills, and agent modes—is worth keeping. V2 should make those pieces machine-validatable and reproducible rather than replacing them.
