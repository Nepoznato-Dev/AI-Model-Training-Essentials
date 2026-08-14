---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Time Series and Forecasting

Time series data is any data collected over time: stock prices, temperature readings, website traffic, sales figures, heart rate monitors, energy consumption. Forecasting means predicting future values based on past patterns. It's one of the most practically valuable applications of data science — and one of the hardest, because the future is genuinely uncertain and real-world time series are full of noise, seasonality, and structural breaks.

---

## Characteristics of Time Series

| Component | Description | Example |
|-----------|-------------|---------|
| **Trend** | Long-term increase or decrease | Global temperatures rising over decades |
| **Seasonality** | Regular, predictable patterns at fixed intervals | Retail sales spike every December |
| **Cyclicity** | Fluctuations at non-fixed intervals (often economic) | Recessions every 5-10 years |
| **Noise (residual)** | Random variation that can't be explained | Daily stock price movements |
| **Autocorrelation** | Current values depend on past values | Today's temperature is similar to yesterday's |

### Stationarity

A time series is **stationary** if its statistical properties (mean, variance) don't change over time. Most forecasting methods assume stationarity.

| Test | Purpose |
|------|---------|
| **Augmented Dickey-Fuller (ADF)** | Tests whether a unit root is present (non-stationary) |
| **KPSS test** | Tests whether the series is trend-stationary |

| Transformation | When to Use |
|---------------|-------------|
| **Differencing** | Remove trend: y'(t) = y(t) - y(t-1) |
| **Log transform** | Stabilise variance (for exponential growth) |
| **Seasonal differencing** | Remove seasonality: y'(t) = y(t) - y(t-s) where s is the season length |

---

## Classical Forecasting Methods

### Moving Averages

| Method | Description | Best For |
|--------|-------------|----------|
| **Simple Moving Average (SMA)** | Average of the last N observations | Smoothing noisy data |
| **Weighted Moving Average** | More recent observations get higher weight | When recent data matters more |
| **Exponential Moving Average (EMA)** | Exponentially decreasing weights | Tracking trends with less lag |

### Exponential Smoothing

| Method | Components | Use Case |
|--------|-----------|----------|
| **Simple (SES)** | Level only | No trend, no seasonality |
| **Holt's (Double)** | Level + trend | Data with trend but no seasonality |
| **Holt-Winters (Triple)** | Level + trend + seasonality | Data with both trend and seasonality |

### ARIMA and Variants

ARIMA (AutoRegressive Integrated Moving Average) is the workhorse of classical time series forecasting.

| Component | Meaning | Parameter |
|-----------|---------|-----------|
| **AR (p)** | Regress on the previous p values | How many past values to use |
| **I (d)** | Number of differencing steps to make stationary | How many times to difference |
| **MA (q)** | Model the error as a combination of past errors | How many past errors to use |

| Variant | Extension | Use Case |
|---------|-----------|----------|
| **SARIMA** | Adds seasonal components (P, D, Q, s) | Data with strong seasonality |
| **ARIMAX** | Adds external variables | When you know about upcoming events |
| **VAR** | Multivariate ARIMA; multiple interdependent series | When variables affect each other |

---

## Modern ML Approaches

### LSTM and RNN-Based Models

| Model | Architecture | Advantage |
|-------|-------------|-----------|
| **LSTM** | Long Short-Term Memory network | Captures long-range temporal dependencies |
| **GRU** | Gated Recurrent Unit (simpler LSTM) | Faster training; similar performance |
| **Seq2Seq** | Encoder-decoder for time series | Flexible input/output lengths |
| **Temporal Convolutional Network (TCN)** | Dilated causal convolutions | Parallel training; long receptive field |

### Prophet (Meta)

A practical forecasting tool designed for business time series.

| Feature | Description |
|---------|-------------|
| **Decomposition** | Trend + seasonality + holidays |
| **Flexible** | Handles missing data, outliers, and structural breaks |
| **Interpretable** | Components are human-readable |
| **Automatic** | Reasonable defaults; minimal tuning required |

| Strength | Limitation |
|----------|------------|
| Great for business metrics (sales, users) | Not ideal for very high-frequency data |
| Handles holidays and special events | Assumes additive or multiplicative seasonality |
| Robust to outliers | Less accurate than deep learning for complex patterns |

### Transformer-Based Models

| Model | Key Feature |
|-------|-------------|
| **Informer** | ProbSparse attention for long sequences |
| **Autoformer** | Auto-correlation mechanism for series decomposition |
| **PatchTST** | Patches the time series; channel-independent |
| **TimesFM** (Google) | Foundation model for time series; pre-trained on diverse data |
| **Chronos** (Amazon) | Tokenises time series; uses LLM-style architecture |

---

## Anomaly Detection in Time Series

Detecting unusual patterns that deviate from expected behaviour.

| Method | Approach | Use Case |
|--------|----------|----------|
| **Statistical** | Z-score, IQR, control charts | Simple, well-understood |
| **Isolation Forest** | Tree-based; isolates anomalies by random partitioning | Multivariate anomaly detection |
| **LOF** (Local Outlier Factor) | Density-based; compares local density to neighbours | When anomalies are in low-density regions |
| **Autoencoders** | Reconstruction error; high error = anomaly | Complex, non-linear patterns |
| **LSTM-based** | Predict next step; large prediction error = anomaly | Sequential anomalies |

### Applications

| Domain | What Anomalies Mean |
|--------|-------------------|
| **Finance** | Fraud, market crashes, flash crashes |
| **Healthcare** | Abnormal heart rate, seizure onset |
| **Manufacturing** | Equipment failure, quality defects |
| **Cybersecurity** | Intrusion attempts, DDoS attacks |
| **Infrastructure** | Server overload, network failures |

---

## Evaluation Metrics

| Metric | Formula (conceptual) | When to Use |
|--------|---------------------|-------------|
| **MAE** (Mean Absolute Error) | Average of absolute errors | Interpretable; same units as data |
| **RMSE** (Root Mean Squared Error) | Square root of average squared errors | Penalises large errors more |
| **MAPE** (Mean Absolute Percentage Error) | Average of absolute percentage errors | When relative error matters |
| **SMAPE** (Symmetric MAPE) | Symmetric version of MAPE | Handles values near zero better |
| **MASE** (Mean Absolute Scaled Error) | MAE relative to a naive forecast | Comparing across different series |

---

## Practical Workflow

| Step | Description |
|------|-------------|
| **1. Explore** | Plot the series; identify trend, seasonality, outliers |
| **2. Decompose** | Separate into trend, seasonal, and residual components |
| **3. Stationarise** | Apply differencing or transforms if needed |
| **4. Split** | Time-based split (never random split for time series) |
| **5. Baseline** | Start with a naive forecast (last value, seasonal naive) |
| **6. Model** | Try classical methods (ARIMA, Prophet), then ML methods |
| **7. Evaluate** | Use appropriate metrics; compare to baseline |
| **8. Iterate** | Add features, try different models, tune hyperparameters |

---

## Tools and Libraries

| Tool | Purpose |
|------|---------|
| **statsmodels** | Classical time series (ARIMA, ETS, decomposition) |
| **Prophet** (Meta) | Business time series forecasting |
| **sktime** | Unified ML interface for time series |
| **Darts** | Comprehensive forecasting library (classical + deep learning) |
| **GluonTS** (Amazon) | Probabilistic time series modelling |
| **NeuralProphet** | Prophet with neural network components |
| **tsfresh** | Automatic time series feature extraction |
| **pandas** | Time series manipulation and resampling |

---

## Summary

Time series forecasting combines classical statistics with modern machine learning. Classical methods (ARIMA, exponential smoothing, Prophet) are interpretable, fast, and often accurate. Deep learning methods (LSTM, Transformers) capture complex patterns but require more data and tuning. The key principles remain the same regardless of method: understand your data's structure (trend, seasonality, noise), compare against a simple baseline, evaluate with appropriate metrics, and account for the fact that the future will not exactly replicate the past.
