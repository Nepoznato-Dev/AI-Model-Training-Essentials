# Monitoring & Observability

## Overview

Production ML monitoring should answer four separate questions:

1. **Is the service healthy?** (availability, latency, resource saturation)
2. **Is the model behaving correctly?** (quality and error metrics)
3. **Has the input population changed?** (data drift)
4. **Has the relationship between inputs and outcomes changed?** (concept/performance drift)

The thresholds below are examples, not universal SLOs. Set them from a measured baseline and a documented service objective.

---

## Metrics to Track

### System metrics

| Metric | Meaning | Example alert |
|---|---|---|
| Latency p50/p95/p99 | Request latency distribution | p95 exceeds your SLO for 5m |
| Throughput | Requests or items processed | Below expected baseline |
| Error rate | Failed requests / total requests | Above service SLO |
| CPU / memory / GPU | Resource saturation | Sustained saturation |
| Queue depth | Work waiting for inference | Growing continuously |

Avoid a universal rule such as "GPU usage below 50% is an alert." Low utilization can be perfectly healthy; high utilization can be healthy if latency and error SLOs are still met.

### Model metrics

Track metrics appropriate to the task:

- Classification: accuracy, precision, recall, F1, calibration, confusion matrix.
- Regression: MAE, RMSE, error quantiles.
- Ranking/recommendation: task-specific ranking metrics and business outcomes.
- Generation/RAG: groundedness, retrieval recall, answer quality, refusal/abstention rate, latency, and cost.

Monitor prediction/input distributions as *signals*, not proof of model failure. A statistically significant drift test can flag a tiny but irrelevant change, especially with large sample sizes.

---

## Structured Logging

Use timezone-aware timestamps and avoid logging raw sensitive inputs or secrets.

```python
import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)
MODEL_VERSION = "unknown"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def log_prediction(request_id, input_shape, prediction, latency_ms):
    logger.info(json.dumps({
        "timestamp": utc_now(),
        "event": "prediction",
        "request_id": request_id,
        "input_shape": list(input_shape),
        "prediction": prediction,
        "latency_ms": latency_ms,
        "model_version": MODEL_VERSION,
    }))
```

Do not automatically log full request bodies. Redact or hash sensitive fields and define a retention policy.

### FastAPI request logging

```python
from fastapi import Request
import time
import uuid

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.perf_counter()
    response = None
    try:
        response = await call_next(request)
        return response
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(json.dumps({
            "timestamp": utc_now(),
            "event": "request",
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code if response else 500,
            "duration_ms": duration_ms,
        }))
```

---

## Data Drift

### Kolmogorov-Smirnov test for continuous features

```python
from scipy import stats


def ks_drift(reference, current, alpha=0.05):
    statistic, p_value = stats.ks_2samp(reference, current)
    return {
        "statistic": float(statistic),
        "p_value": float(p_value),
        "drift_detected": p_value < alpha,
    }
```

Statistical significance is not the same as practical significance. Pair the test with an effect-size threshold and inspect the magnitude of the distribution change.

### Categorical drift

A chi-square test should be run on category counts with the same category universe. For sparse categories, combine rare categories or use an appropriate alternative rather than blindly passing raw integer labels to `np.bincount`.

```python
import numpy as np
from scipy.stats import chi2_contingency


def chi_square_drift(reference_labels, current_labels, alpha=0.05):
    categories = np.unique(np.concatenate([reference_labels, current_labels]))
    ref_counts = np.array([(reference_labels == c).sum() for c in categories])
    cur_counts = np.array([(current_labels == c).sum() for c in categories])
    table = np.vstack([ref_counts, cur_counts])
    statistic, p_value, _, _ = chi2_contingency(table)
    return {"statistic": float(statistic), "p_value": float(p_value), "drift_detected": p_value < alpha}
```

### PSI

Population Stability Index requires stable bins. Quantile bins can contain duplicate edges for low-cardinality or constant features, so production implementations must validate or deduplicate bin edges and handle empty bins.

```python
import numpy as np


def psi(reference, current, bins=10, epsilon=1e-6):
    edges = np.unique(np.quantile(reference, np.linspace(0, 1, bins + 1)))
    if len(edges) < 2:
        return 0.0

    ref_counts, _ = np.histogram(reference, bins=edges)
    cur_counts, _ = np.histogram(current, bins=edges)
    ref_props = ref_counts / max(ref_counts.sum(), 1)
    cur_props = cur_counts / max(cur_counts.sum(), 1)
    ref_props = np.maximum(ref_props, epsilon)
    cur_props = np.maximum(cur_props, epsilon)
    return float(np.sum((cur_props - ref_props) * np.log(cur_props / ref_props)))
```

Treat common PSI thresholds as conventions, not scientific constants. Validate them against your data and business impact.

---

## Concept Drift

Libraries such as River provide streaming detectors, but a drift signal should not automatically trigger retraining without safeguards. Validate the signal, check data quality, compare against a baseline, and use a controlled retraining/deployment pipeline.

```python
from river import drift

class ConceptDriftMonitor:
    def __init__(self):
        self.detector = drift.ADWIN()

    def update(self, prediction_error):
        self.detector.update(float(prediction_error))
        return bool(self.detector.drift_detected)
```

---

## Prometheus Metrics

The alert rules in this guide assume that the application actually exposes the corresponding Prometheus metrics. Names such as `prediction_latency_seconds_bucket` do not appear automatically.

```python
from prometheus_client import Counter, Histogram

PREDICTIONS = Counter("predictions_total", "Prediction requests")
ERRORS = Counter("prediction_errors_total", "Prediction errors")
LATENCY = Histogram("prediction_latency_seconds", "Prediction latency")


def record_prediction(duration_seconds, failed=False):
    PREDICTIONS.inc()
    LATENCY.observe(duration_seconds)
    if failed:
        ERRORS.inc()
```

For latency quantiles in Prometheus, use a Histogram and its `_bucket` series. Choose buckets that match the expected latency range.

### Example alert rules

```yaml
groups:
  - name: ml-alerts
    rules:
      - alert: HighPredictionLatency
        expr: histogram_quantile(0.95, rate(prediction_latency_seconds_bucket[5m])) > 0.5
        for: 5m
        labels:
          severity: warning

      - alert: HighErrorRate
        expr: rate(prediction_errors_total[5m]) / clamp_min(rate(predictions_total[5m]), 0.001) > 0.01
        for: 5m
        labels:
          severity: critical
```

Do not deploy an alert without verifying that its metric exists and that the expression behaves correctly when traffic is near zero.

---

## Alerting

```python
import smtplib
from datetime import datetime, timezone
from email.mime.text import MIMEText

class AlertManager:
    def __init__(self, smtp_server, from_email, recipients):
        self.smtp_server = smtp_server
        self.from_email = from_email
        self.recipients = recipients

    def send_alert(self, alert_name, message, severity="warning"):
        body = (
            f"Alert: {alert_name}\n"
            f"Severity: {severity}\n\n"
            f"{message}\n\n"
            f"Time: {datetime.now(timezone.utc).isoformat()}"
        )
        msg = MIMEText(body)
        msg["Subject"] = f"[{severity.upper()}] {alert_name}"
        msg["From"] = self.from_email
        msg["To"] = ", ".join(self.recipients)
        with smtplib.SMTP(self.smtp_server) as server:
            server.sendmail(self.from_email, self.recipients, msg.as_string())
```

For production, prefer a managed alerting system or authenticated SMTP with TLS and explicit timeout/error handling.

---

## Dashboards

A useful dashboard should show:

- request rate
- error rate
- p50/p95/p99 latency
- resource saturation
- queue depth
- model/version identifiers
- model quality when labels become available
- drift signals with reference windows

The exact Grafana JSON schema is version-dependent. Treat exported dashboard JSON as an artifact produced by the Grafana version you deploy rather than a timeless hand-written example.

---

## Incident Response

### Model performance degradation

1. **Assess impact** — identify affected endpoints, users, and business metrics.
2. **Check recent changes** — deployments, model versions, feature pipelines, and configuration.
3. **Check infrastructure** — latency, errors, CPU/GPU/memory, queue depth.
4. **Check data quality** — missing fields, schema changes, distribution shifts.
5. **Check model quality** — labeled outcomes, calibration, error slices, and drift.
6. **Mitigate** — rollback, disable a feature, route traffic to a known-good model, or scale infrastructure.
7. **Verify recovery** — watch SLOs and model-quality metrics after mitigation.
8. **Postmortem** — record root cause, detection gap, corrective action, and regression test.

Do not automatically retrain solely because a drift detector fired. Retraining is a model change and should pass the same evaluation and deployment gates as any other model update.

---

## Related Resources

- [Deployment Guide](deployment.md)
- [Architecture Patterns](architecture_patterns.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Best Practices Checklist](references/checklist.md)
