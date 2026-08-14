# Monitoring & Observability

## Overview

Guide to monitoring ML systems in production, detecting issues, and maintaining model performance.

---

## Key Metrics to Track

### System Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Latency (p50)** | Median prediction time | > 100ms |
| **Latency (p95)** | 95th percentile prediction time | > 500ms |
| **Latency (p99)** | 99th percentile prediction time | > 1s |
| **Throughput** | Predictions per second | < expected baseline |
| **Error Rate** | Percentage of failed requests | > 1% |
| **CPU Usage** | CPU utilization | > 80% |
| **Memory Usage** | RAM utilization | > 85% |
| **GPU Usage** | GPU utilization (if applicable) | < 50% or > 95% |

### Model Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Prediction Distribution** | Distribution of output values | Significant shift |
| **Confidence Scores** | Average prediction confidence | < baseline - 10% |
| **Input Distribution** | Feature value distributions | KS-test p < 0.05 |
| **Missing Values** | Rate of missing inputs | > 5% |
| **Out-of-Vocabulary** | Rate of unknown tokens/inputs | > 2% |

### Business Metrics

| Metric | Description |
|--------|-------------|
| **Conversion Rate** | Impact on business outcomes |
| **User Engagement** | Clicks, time spent, etc. |
| **Cost per Prediction** | Infrastructure cost tracking |
| **ROI** | Return on investment |

---

## Logging Implementation

### Structured Logging

```python
import logging
import json
import os
from datetime import datetime

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

# Define MODEL_VERSION from environment (set during deployment)
MODEL_VERSION = os.environ.get("MODEL_VERSION", "unknown")

def log_prediction(request_id, input_data, prediction, latency_ms):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "prediction",
        "request_id": request_id,
        "input_shape": list(input_data.shape),
        "prediction": prediction.tolist() if hasattr(prediction, 'tolist') else prediction,
        "latency_ms": latency_ms,
        "model_version": MODEL_VERSION
    }
    logger.info(json.dumps(log_entry))

def log_error(request_id, error_type, error_message):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "error",
        "request_id": request_id,
        "error_type": error_type,
        "error_message": error_message,
        "model_version": MODEL_VERSION
    }
    logger.error(json.dumps(log_entry))
```

### Request/Response Logging

```python
from fastapi import Request, Response
import time
import uuid

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Log request
    logger.info(json.dumps({
        "event": "request_start",
        "request_id": request_id,
        "method": request.method,
        "path": request.url.path,
        "client_ip": request.client.host
    }))
    
    try:
        response: Response = await call_next(request)
        
        # Log response
        duration = time.time() - start_time
        logger.info(json.dumps({
            "event": "request_end",
            "request_id": request_id,
            "status_code": response.status_code,
            "duration_ms": duration * 1000
        }))
        
        return response
    except Exception as e:
        logger.error(json.dumps({
            "event": "request_error",
            "request_id": request_id,
            "error": str(e)
        }))
        raise
```

---

## Drift Detection

### Data Drift Detection

```python
import numpy as np
from scipy import stats
from sklearn.metrics import pairwise_distances

class DataDriftDetector:
    def __init__(self, reference_data, threshold=0.05):
        self.reference_data = reference_data
        self.threshold = threshold
        
    def detect_ks_test(self, new_data, feature_name):
        """Kolmogorov-Smirnov test for continuous features"""
        statistic, p_value = stats.ks_2samp(
            self.reference_data[feature_name],
            new_data[feature_name]
        )
        return {
            'feature': feature_name,
            'statistic': statistic,
            'p_value': p_value,
            'drift_detected': p_value < self.threshold
        }
    
    def detect_chi_square(self, new_data, feature_name):
        """Chi-square test for categorical features"""
        # Use value_counts instead of bincount — works with any categorical encoding
        ref_counts = self.reference_data[feature_name].value_counts()
        new_counts = new_data[feature_name].value_counts()
        
        # Align categories across reference and new data
        all_categories = sorted(set(ref_counts.index) | set(new_counts.index))
        ref_aligned = np.array([ref_counts.get(c, 0) for c in all_categories])
        new_aligned = np.array([new_counts.get(c, 0) for c in all_categories])
        
        statistic, p_value, _, _ = stats.chi2_contingency([ref_aligned, new_aligned])
        return {
            'feature': feature_name,
            'statistic': statistic,
            'p_value': p_value,
            'drift_detected': p_value < self.threshold
        }
    
    def detect_population_stability_index(self, new_data, feature_name, bins=10):
        """PSI for binned features"""
        ref_data = self.reference_data[feature_name]
        
        # Create bins from reference data
        percentiles = np.linspace(0, 100, bins + 1)
        bin_edges = np.unique(np.percentile(ref_data, percentiles))  # unique to handle duplicates
        
        if len(bin_edges) < 2:
            return {'feature': feature_name, 'psi': 0.0, 'drift_detected': False}
        
        # Calculate proportions
        ref_props = np.histogram(ref_data, bins=bin_edges)[0] / len(ref_data)
        new_props = np.histogram(new_data[feature_name], bins=bin_edges)[0] / len(new_data)
        
        # Add small constant to avoid log(0)
        ref_props = ref_props + 1e-6
        new_props = new_props + 1e-6
        
        psi = np.sum((new_props - ref_props) * np.log(new_props / ref_props))
        
        return {
            'feature': feature_name,
            'psi': psi,
            'drift_detected': psi > 0.25  # Common threshold
        }
```

### Concept Drift Detection

```python
from river import drift

class ConceptDriftMonitor:
    def __init__(self):
        self.adwin = drift.ADWIN()
        self.page_hinkley = drift.PageHinkley()
        
    def update(self, prediction, actual):
        """Update with new prediction and actual value"""
        error = abs(prediction - actual)
        
        # ADWIN detection
        self.adwin.update(error)
        adwin_drift = self.adwin.drift_detected
        
        # Page-Hinkley detection
        self.page_hinkley.update(error)
        ph_drift = self.page_hinkley.drift_detected
        
        return {
            'adwin_drift': adwin_drift,
            'page_hinkley_drift': ph_drift,
            'current_error': error
        }

# Usage
monitor = ConceptDriftMonitor()

for prediction, actual in stream:
    result = monitor.update(prediction, actual)
    if result['adwin_drift'] or result['page_hinkley_drift']:
        alert("Concept drift detected!")
        trigger_retraining()
```

---

## Alerting Setup

### Prometheus + Grafana

**prometheus.yml:**
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'ml-api'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

rule_files:
  - 'alerts.yml'
```

**alerts.yml:**
```yaml
groups:
  - name: ml-alerts
    rules:
      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(prediction_latency_seconds_bucket[5m])) > 0.5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High prediction latency"
          description: "95th percentile latency is above 500ms"
      
      - alert: HighErrorRate
        expr: rate(prediction_errors_total[5m]) / rate(predictions_total[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate"
          description: "Error rate is above 1%"
      
      - alert: ModelDriftDetected
        expr: model_drift_score > 0.25
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Model drift detected"
          description: "PSI score indicates significant drift"
```

### Custom Alerting

```python
import smtplib
from email.mime.text import MIMEText
from typing import List

class AlertManager:
    def __init__(self, smtp_server: str, from_email: str, recipients: List[str]):
        self.smtp_server = smtp_server
        self.from_email = from_email
        self.recipients = recipients
    
    def send_alert(self, alert_name: str, message: str, severity: str = "warning"):
        subject = f"[{severity.upper()}] {alert_name}"
        body = f"""
        Alert: {alert_name}
        Severity: {severity}
        
        {message}
        
        Time: {datetime.utcnow().isoformat()}
        """
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.from_email
        msg['To'] = ', '.join(self.recipients)
        
        with smtplib.SMTP(self.smtp_server) as server:
            server.sendmail(self.from_email, self.recipients, msg.as_string())
    
    def check_and_alert(self, metric_name: str, value: float, threshold: float):
        if value > threshold:
            self.send_alert(
                alert_name=f"{metric_name} exceeded threshold",
                message=f"Current value: {value:.4f}, Threshold: {threshold:.4f}",
                severity="critical" if value > threshold * 1.5 else "warning"
            )
```

---

## Dashboard Creation

### Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "ML Model Monitoring",
    "panels": [
      {
        "title": "Prediction Latency (p95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(prediction_latency_seconds_bucket[5m]))",
            "legendFormat": "p95 latency"
          }
        ],
        "thresholds": [
          {"value": 0.5, "colorMode": "warning"},
          {"value": 1.0, "colorMode": "critical"}
        ]
      },
      {
        "title": "Predictions per Second",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(predictions_total[1m])",
            "legendFormat": "throughput"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(prediction_errors_total[5m]) / rate(predictions_total[5m])",
            "legendFormat": "error rate"
          }
        ],
        "thresholds": [
          {"value": 0.01, "colorMode": "warning"},
          {"value": 0.05, "colorMode": "critical"}
        ]
      },
      {
        "title": "Model Drift Score (PSI)",
        "type": "graph",
        "targets": [
          {
            "expr": "model_psi_score",
            "legendFormat": "PSI"
          }
        ],
        "thresholds": [
          {"value": 0.1, "colorMode": "warning"},
          {"value": 0.25, "colorMode": "critical"}
        ]
      }
    ]
  }
}
```

---

## Incident Response

### Runbook Template

```markdown
# Incident Runbook: Model Performance Degradation

## Symptoms
- Increased prediction latency
- Higher error rates
- Drop in model accuracy

## Immediate Actions

1. **Assess Impact**
   - Check dashboard for scope
   - Identify affected users/endpoints
   - Determine business impact

2. **Triage**
   - Check recent deployments
   - Review error logs
   - Verify infrastructure health

3. **Mitigation**
   - Rollback to previous version if recent deployment
   - Scale up resources if overloaded
   - Enable circuit breaker if cascading failures

4. **Communication**
   - Notify stakeholders
   - Update status page
   - Create incident channel

## Investigation

- [ ] Check data pipeline for issues
- [ ] Verify model input distributions
- [ ] Review drift detection metrics
- [ ] Analyze error patterns

## Resolution

- [ ] Deploy fix or rollback
- [ ] Verify recovery
- [ ] Monitor for recurrence

## Post-Incident

- [ ] Schedule post-mortem
- [ ] Document learnings
- [ ] Update runbook
- [ ] Create action items
```

---

## Related Resources

- [Deployment Guide](deployment.md)
- [Architecture Patterns](architecture_patterns.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Best Practices Checklist](references/checklist.md)

## Tools Reference

- **Logging**: ELK Stack, Splunk, Datadog
- **Metrics**: Prometheus, Grafana, CloudWatch
- **Tracing**: Jaeger, Zipkin, X-Ray
- **Alerting**: PagerDuty, OpsGenie, Alertmanager
- **Drift Detection**: Evidently AI, Arize, WhyLabs
