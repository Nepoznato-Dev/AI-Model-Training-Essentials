---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [feature, engineering, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Feature Engineering

Feature engineering is the process of transforming raw data into representations that make machine learning models more effective. It's often described as the most important step in the ML pipeline — the features you give a model matter more than the algorithm you choose. A simple model with well-crafted features will typically outperform a complex model with raw, unprocessed inputs. The art lies in understanding both the domain and the data well enough to create signals the model can learn from.

---

## Why Feature Engineering Matters

| Factor | Impact |
|--------|--------|
| **Signal quality** | Better features = clearer patterns for the model to learn |
| **Model simplicity** | Good features let simpler models perform well; less need for complex architectures |
| **Training speed** | Relevant, well-scaled features converge faster |
| **Generalisation** | Domain-informed features help models work on unseen data |
| **Interpretability** | Meaningful features are easier to explain to stakeholders |

---

## Types of Feature Transformations

### Numerical Transformations

| Transformation | Formula / Description | When to Use |
|---------------|----------------------|-------------|
| **Log transform** | log(x) or log(x + 1) | Right-skewed distributions; monetary values |
| **Square root** | sqrt(x) | Moderate skew; count data |
| **Box-Cox** | Parametric transform that finds best power transformation | Making data more normally distributed |
| **Yeo-Johnson** | Like Box-Cox but handles negative values | Skewed data with negative values |
| **Standardisation** | (x - mean) / std | Features with different scales; algorithms assuming normality |
| **Min-max scaling** | (x - min) / (max - min) | Bounding features to [0, 1]; image pixel values |
| **Robust scaling** | (x - median) / IQR | Data with outliers |
| **Binning** | Convert continuous to categorical | Non-linear relationships; decision trees |
| **Polynomial features** | x², x³, x₁×x₂ | Capturing non-linear relationships in linear models |

### Categorical Encodings

| Encoding | Description | When to Use |
|----------|-------------|-------------|
| **One-hot encoding** | Create a binary column for each category | Low-cardinality categories; tree-based models handle natively |
| **Label encoding** | Assign integer to each category | Ordinal categories; tree-based models |
| **Target encoding** | Replace category with mean of target variable | High-cardinality categories; avoid overfitting with smoothing |
| **Frequency encoding** | Replace category with its count or frequency | When frequency itself is informative |
| **Binary encoding** | Convert integer-encoded categories to binary digits | High-cardinality; reduces dimensionality vs one-hot |
| **Embedding** | Learn dense vector representation | Very high cardinality; NLP; recommender systems |
| **Hash encoding** | Hash categories to a fixed number of features | Very high cardinality; online learning |

### Date and Time Features

| Feature | Description |
|---------|-------------|
| **Hour of day** | Captures daily patterns (rush hour, night-time) |
| **Day of week** | Weekday vs weekend effects |
| **Month / quarter** | Seasonal patterns |
| **Is weekend** | Binary flag for weekend |
| **Is holiday** | Binary flag for public holidays |
| **Time since event** | Days since last purchase; hours since last login |
| **Cyclical encoding** | sin(2π × hour / 24), cos(2π × hour / 24) — preserves circular nature of time |

---

## Handling Missing Values

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Drop rows** | Remove rows with missing values | Missing data is a small fraction; MCAR (missing completely at random) |
| **Drop columns** | Remove features with too many missing values | Feature is mostly missing; not important |
| **Mean / median imputation** | Fill with the feature's mean or median | Simple; preserves mean but reduces variance |
| **Mode imputation** | Fill categorical with most frequent value | Categorical features |
| **KNN imputation** | Use k-nearest neighbours to estimate missing value | When similar instances help predict the missing value |
| **Model-based imputation** | Train a model to predict missing values | More accurate; computationally expensive |
| **Missing indicator** | Add a binary column flagging missingness | When missingness itself is informative |
| **Interpolation** | Fill with interpolated values (linear, spline) | Time series; ordered data |

---

## Feature Selection

### Filter Methods

| Method | Description |
|--------|-------------|
| **Correlation** | Remove features highly correlated with each other |
| **Variance threshold** | Remove features with near-zero variance |
| **Mutual information** | Measure information each feature provides about the target |
| **Chi-squared** | Test independence between categorical features and target |
| **ANOVA F-test** | Test if numerical feature means differ across target classes |

### Wrapper Methods

| Method | Description |
|--------|-------------|
| **Forward selection** | Start empty; add the best feature one at a time |
| **Backward elimination** | Start with all; remove the worst feature one at a time |
| **Recursive feature elimination (RFE)** | Repeatedly train model; remove least important features |

### Embedded Methods

| Method | Description |
|--------|-------------|
| **L1 regularisation (Lasso)** | Shrinks irrelevant feature weights to zero |
| **Tree-based importance** | Use feature importance from tree models |
| **SHAP values** | Measure each feature's contribution to predictions |

---

## Domain-Specific Feature Engineering

### Text Features

| Feature | Description |
|---------|-------------|
| **TF-IDF** | Term frequency weighted by inverse document frequency |
| **Word embeddings** | Dense vectors capturing semantic meaning (Word2Vec, GloVe) |
| **Character n-grams** | Capture sub-word patterns; useful for typos and morphology |
| **Text statistics** | Length; word count; sentence count; average word length |
| **Readability scores** | Flesch-Kincaid; Gunning fog index |

### Time Series Features

| Feature | Description |
|---------|-------------|
| **Lag features** | Previous values: y(t-1), y(t-7), y(t-30) |
| **Rolling statistics** | Mean, std, min, max over a window |
| **Difference** | y(t) - y(t-1); captures trend |
| **Seasonal difference** | y(t) - y(t-12) for monthly data with yearly seasonality |
| **Fourier terms** | Sine and cosine terms for seasonal patterns |

### Image Features (Pre-Deep Learning)

| Feature | Description |
|---------|-------------|
| **HOG** (Histogram of Oriented Gradients) | Distribution of edge directions |
| **LBP** (Local Binary Patterns) | Texture description |
| **SIFT** (Scale-Invariant Feature Transform) | Keypoint descriptors |
| **Colour histograms** | Distribution of colours in the image |

---

## Feature Engineering Best Practices

| Practice | Description |
|----------|-------------|
| **Avoid data leakage** | Never use information from the future or the test set to create features |
| **Document everything** | Record what transformations were applied and why |
| **Version your features** | Track feature changes alongside model changes |
| **Validate with and without** | Test whether a new feature actually improves model performance |
| **Keep it reproducible** | Feature engineering pipelines should be deterministic and repeatable |
| **Monitor feature drift** | Feature distributions may change over time; monitor and retrain |

---

## Summary

Feature engineering is where domain knowledge meets machine learning. It's the process of transforming raw data — messy, incomplete, high-dimensional — into clean, informative representations that models can learn from. Numerical transformations handle skew and scale. Categorical encodings convert labels into numbers models can use. Date features capture temporal patterns. Missing value strategies handle incomplete data. Feature selection removes noise and redundancy. The best feature engineers think like detectives: they ask what signals should be present in the data, where those signals might be hidden, and how to extract them in a way that's honest (no data leakage), reproducible, and robust to change over time.
