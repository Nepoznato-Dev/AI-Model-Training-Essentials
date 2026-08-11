# Changes for V2

This file is the migration checklist for the V2 VS Code rebuild. The reliability branch is intentionally being kept separate from `main` so these changes can be reviewed and selectively ported.

## Completed reliability work

### Repository QA
- Added lightweight repository validation for UTF-8, BOMs, mojibake, YAML frontmatter, agent-mode metadata, agent references, Markdown links, and Python syntax.
- Added CI coverage for repository validation and agent-mode validation.
- Added a multilingual knowledge-base validator to check language/file parity, empty files, and protected four-digit year metadata.
- CI now runs the knowledge-base validator as well.

### Model development
- Fixed scheduler signatures and validation behavior.
- Fixed gradient-accumulation handling for final partial batches.
- Corrected Dropout/BatchNorm examples.
- Fixed missing imports and deprecated Optuna usage.
- Corrected dynamic quantization guidance.
- Prevented teacher-model gradients during knowledge distillation.
- Removed unsupported reproducibility/performance guarantees.
- Added proper validation/test separation in transfer learning.
- Corrected the ResNet18 10-class head parameter count to 5,130.
- Added validation-based checkpoint selection and held-out final testing.

### Neural-network basics
- Added train/validation/test separation.
- Added stratified splitting.
- Kept the scaler fitted only on training data.
- Fixed decision-boundary inference on scaled inputs while retaining interpretable original-coordinate plots.
- Avoided using the test set for model selection.

### Text generation
- Fixed Transformers pipeline device selection.
- Corrected `temperature` and `top_p` sampling semantics.
- Corrected token-vs-word terminology around `max_new_tokens`.
- Fixed tokenization demonstration special-token handling.
- Added validation for generation arguments.
- Removed unsupported universal generation-speed/quality claims.

### Security
- Modernized adversarial-gradient handling and adversarial training.
- Updated SlowAPI/Pydantic examples.
- Improved key handling and model-artifact guidance.
- Improved audit timestamps and logging guidance.
- Added agent-specific security considerations.
- Removed unsafe/inappropriate serialization guidance.

### Deployment
- Fixed Docker health checks.
- Fixed the batch-inference timeout/queue failure path and exception propagation.
- Replaced process-randomized Python `hash()` cache keys with stable serialization.
- Improved Redis serialization guidance.
- Updated Docker/Compose examples.
- Improved FastAPI error handling and timezone-aware timestamps.
- Removed obsolete cloud deployment examples and added version-drift warnings.
- Updated GitHub Actions examples to current major versions used by the repo.

### RAG
- Corrected `all-MiniLM-L6-v2` embedding dimension to 384.
- Added normalized embeddings.
- Added empty knowledge-base and `top_k` validation.
- Improved multi-document context construction.
- Added grounded-answer instructions and clearer failure behavior.
- Removed misleading production-readiness claims.

### Monitoring
- Removed arbitrary universal GPU utilization thresholds.
- Added clearer separation between service health, data drift, model quality, and concept/performance drift.
- Fixed timezone-aware timestamps.
- Added privacy/retention guidance for request logging.
- Corrected categorical drift methodology and robust PSI bin handling.
- Added real Prometheus instrumentation and corrected alert expressions.
- Removed brittle hand-written Grafana JSON.
- Removed automatic retraining as the default response to drift.

## Knowledge-base date incident

A content-processing script accidentally changed dates to 2026 in parts of the knowledge base. Treat this as a **data-pipeline regression**, not a reason to manually fix dates forever.

The new `tools/validate_knowledge_base.py` checks translated files against their English source and flags unexpected four-digit years. This is deliberately conservative: it catches accidental year mutation while allowing locale-specific date formatting.

For V2 transformation/translation tooling, protect:

```text
Dates
URLs
Model names
Version numbers
Code blocks
YAML frontmatter
File paths
Identifiers
```

The best long-term solution is to preserve structured metadata separately from prose and test that protected metadata is unchanged after every transformation.

## Remaining audit priorities

- CNN/computer-vision examples: verify train-only normalization, non-random validation/test transforms, class counts, output dimensions, parameter counts, and benchmark claims.
- RAG: add retrieval metrics such as Recall@k/MRR where labels exist, plus grounding and malformed/empty/duplicate/oversized-context tests.
- Cloud/deployment: verify provider SDK APIs, versions, authentication, health checks, retries, secrets handling, and failure behavior.
- Knowledge base: add source/revision metadata for time-sensitive facts.
- Translation: track the English source revision, stale/current status, missing sections, structural divergence, and protected technical metadata.
- Agent Modes/Skills: formalize YAML metadata with JSON Schema and separate descriptive instructions from executable permissions.
- Add lightweight smoke tests for examples that can run deterministically without large models or external services.
- Audit remaining project scripts for dependency isolation and executable correctness.

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

## Philosophy for V2

Do not sacrifice the repository's breadth. The main improvement needed is **verification**, not a reduction in ambition. The existing guides, projects, knowledge base, skills, and agent modes are worth keeping; V2 should make them machine-validatable and reproducible.
