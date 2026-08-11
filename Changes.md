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
Do not keep one giant environment as the primary installation method. Prefer:
- project-level `pyproject.toml`
- lockfiles (`uv.lock` or equivalent)
- focused optional dependency groups
- per-project environments

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

## 4. `wiki/model_development.md`

### Fixed
- Scheduler examples now use the correct `step()` signature for each scheduler.
- Gradient accumulation now handles a final partial accumulation group.
- Dropout/BatchNorm examples now show actual `forward()` usage.
- Added missing `SVC` import.
- Updated Optuna examples away from deprecated `suggest_loguniform` / `suggest_uniform`.
- Dynamic quantization example no longer incorrectly includes `Conv2d`.
- Knowledge-distillation example explicitly runs the teacher under `no_grad()`.
- Reproducibility wording no longer implies that seeds guarantee complete determinism.

## 5. `wiki/security.md`

### Fixed/modernized
- FGSM and PGD now use `torch.autograd.grad` rather than accumulating model gradients.
- Adversarial training now accepts an optimizer and actually performs `optimizer.step()`.
- Randomized smoothing is explicitly described as noisy prediction averaging rather than a complete certified implementation.
- JPEG defense now imports `torchvision.transforms`.
- Fixed SlowAPI example (`Limiter`, `Request`).
- Updated Pydantic examples to v2 (`field_validator`, `ConfigDict`, `json_schema_extra`, `min_length`/`max_length`).
- Removed the unsafe pattern of silently generating an ephemeral encryption key.
- Warned against arbitrary pickle deserialization for untrusted model artifacts.
- Replaced undefined `get_client_ip()` / `get_user_agent()` calls with explicit function parameters.
- Switched audit timestamps to timezone-aware UTC.
- Added agent-specific security requirements: least privilege, tool allowlists, prompt-injection-aware retrieval, secret isolation, and tool auditing.

## 6. Known issues still requiring V2 work

The following were identified in the audit but are not all fixed by this first reliability branch:

- Deployment Docker health check references `curl` without installing it.
- `BatchPredictor` contains a missing `_try_process_batch` implementation.
- Some deployment examples use obsolete cloud SDKs and need current-provider rewrites.
- Some FastAPI examples use older lifecycle patterns.
- Monitoring examples need real metric instrumentation rather than isolated metric names.
- RAG examples need retrieval/generation evaluation and a clear grounded-answer policy.
- `rag_simple` contains an incorrect comment claiming `all-MiniLM-L6-v2` has 768-dimensional embeddings; it is 384-dimensional.
- CNN/ML examples need train/validation/test separation where hyperparameters are tuned.
- Transfer-learning example has an incorrect trainable-parameter count and needs explicit BatchNorm/frozen-backbone behavior.
- Decision-boundary plotting needs consistent scaled/raw coordinate handling.
- Text-generation examples need correct `do_sample`/temperature semantics.
- Cloud examples need version/date verification.
- Agent-mode frontmatter needs a machine-readable schema and tool registry.
- Translation files need source-revision metadata, review status, and parity checks.
- Knowledge-base date fields need protection from content-processing scripts.

## 7. Knowledge-base date incident

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

## 8. Recommended V2 validation gates

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

## 9. Important philosophy for V2

Do not sacrifice the repository's breadth. The main improvement needed is **verification**, not a reduction in ambition.

The existing structure—guides, projects, knowledge, skills, and agent modes—is worth keeping. V2 should make those pieces machine-validatable and reproducible rather than replacing them.
