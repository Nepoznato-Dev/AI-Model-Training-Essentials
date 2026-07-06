# Bad Dataset Examples

## Overview

Training datasets are the foundation of machine learning models. Bad datasets contain issues like poor quality labels, biased samples, data leakage, inadequate coverage, or privacy violations that lead to unreliable, unfair, or harmful model behavior. Understanding these pitfalls is crucial for building robust ML systems.

## When to Reference This Document

- Collecting training data
- Evaluating dataset quality
- Debugging model performance issues
- Auditing datasets for bias
- Preparing data for production models

## Common Dataset Failures

### Label Noise and Inconsistency

**Bad Example**:
```python
# Sentiment dataset with inconsistent labels
dataset = [
    ("I love this product!", "negative"),  # Wrong label
    ("This is terrible.", "positive"),     # Wrong label
    ("It's okay I guess", "neutral"),
    ("Absolutely amazing!", "neutral"),    # Inconsistent
    ("Worst purchase ever", "positive"),   # Wrong label
]

# 40% error rate in labels
```

**Why It's Bad**:
- Model learns incorrect patterns
- Reduced accuracy on clean test data
- Unpredictable behavior in production
- Wasted training compute

**Solution**: Quality assurance processes
```python
def validate_labels(dataset):
    # Multiple annotators per sample
    annotations = collect_multiple_annotations(dataset)
    
    # Calculate inter-annotator agreement
    kappa = cohens_kappa(annotations)
    
    # Flag low-agreement samples for review
    flagged = [sample for sample in annotations if sample.agreement < 0.7]
    
    # Expert review for disputed samples
    reviewed = expert_review(flagged)
    
    return merge_annotations(reviewed)

# Target: >0.8 inter-annotator agreement
```

### Sampling Bias

**Bad Example**:
```python
# Face recognition dataset
dataset = collect_images_from("social_media_platform")

# Demographics:
# - 80% male, 20% female
# - 90% under 35 years old
# - 70% from North America
# - Mostly well-lit, high-quality photos

# Model fails on: women, older adults, other regions, poor lighting
```

**Why It's Bad**:
- Poor performance on underrepresented groups
- Discriminatory outcomes
- Limited real-world applicability
- Ethical and legal risks

**Solution**: Stratified sampling and augmentation
```python
def create_balanced_dataset():
    # Define target demographics
    quotas = {
        "gender": {"male": 0.5, "female": 0.5},
        "age_group": {"0-18": 0.15, "19-35": 0.25, "36-55": 0.30, "55+": 0.30},
        "region": {"north_america": 0.2, "europe": 0.2, "asia": 0.2, 
                   "africa": 0.15, "south_america": 0.15, "oceania": 0.1}
    }
    
    # Collect data to match quotas
    dataset = stratified_collection(quotas)
    
    # Augment underrepresented groups
    dataset = augment_with_synthetic_data(dataset, target_distribution=quotas)
    
    # Validate distribution
    assert check_distribution(dataset, quotas, tolerance=0.05)
    
    return dataset
```

### Data Leakage

**Bad Example**:
```python
# Predicting customer churn
dataset = load_customer_data()

# Features include:
# - customer_id
# - signup_date
# - monthly_charges
# - total_charges
# - contract_type
# - churned (target)
# - cancellation_date  # LEAKAGE: only known after churn!
# - days_since_last_login  # LEAKAGE: calculated at prediction time

# Model achieves 99% accuracy but fails in production
```

**Why It's Bad**:
- Inflated evaluation metrics
- Model cheats using future information
- Complete failure in production
- Wasted development time

**Solution**: Careful feature audit
```python
def audit_for_leakage(features, target, temporal_point):
    leakage_risks = []
    
    for feature in features:
        # Check if feature is available at prediction time
        if not is_available_at(feature, temporal_point):
            leakage_risks.append({
                "feature": feature,
                "reason": "Future information",
                "severity": "HIGH"
            })
        
        # Check for target leakage
        if correlation(feature, target) > 0.9:
            leakage_risks.append({
                "feature": feature,
                "reason": "Possible target leakage",
                "severity": "MEDIUM"
            })
        
        # Check for ID-like features
        if cardinality(feature) == len(dataset):
            leakage_risks.append({
                "feature": feature,
                "reason": "Unique identifier",
                "severity": "HIGH"
            })
    
    return leakage_risks

# Remove all HIGH severity features before training
```

### Inadequate Coverage

**Bad Example**:
```python
# Autonomous driving dataset
dataset = {
    "weather": ["sunny", "clear"],
    "time_of_day": ["daytime"],
    "location": ["California highways"],
    "traffic": ["light"],
    "road_conditions": ["dry"]
}

# Missing: rain, snow, night, urban areas, heavy traffic, wet roads
# Model fails in any condition not in training data
```

**Why It's Bad**:
- Poor generalization to new scenarios
- Safety risks in edge cases
- Limited deployment options
- False confidence in model capabilities

**Solution**: Comprehensive scenario coverage
```python
def ensure_coverage(scenarios):
    # Define dimensions and required values
    dimensions = {
        "weather": ["sunny", "cloudy", "rainy", "snowy", "foggy"],
        "time": ["dawn", "day", "dusk", "night"],
        "location": ["highway", "urban", "suburban", "rural"],
        "traffic": ["none", "light", "moderate", "heavy"],
        "road": ["dry", "wet", "icy", "snow-covered"]
    }
    
    # Generate combinatorial coverage
    required_scenarios = generate_combinations(dimensions, min_coverage=0.8)
    
    # Map existing data to scenarios
    covered = map_to_scenarios(dataset, dimensions)
    
    # Identify gaps
    gaps = required_scenarios - covered
    
    # Prioritize data collection for gaps
    collection_plan = prioritize_gaps(gaps, risk_assessment)
    
    return collection_plan
```

### Privacy Violations

**Bad Example**:
```python
# Medical records dataset
dataset = load_patient_records()

# Contains:
# - Patient names
# - Social security numbers
# - Exact addresses
# - Full dates of birth
# - Unmasked medical conditions

# Published without anonymization
```

**Why It's Bad**:
- Legal violations (HIPAA, GDPR)
- Privacy harm to individuals
- Reputational damage
- Potential lawsuits and fines

**Solution**: Proper anonymization
```python
def anonymize_medical_data(dataset):
    # Remove direct identifiers
    dataset = remove_fields(dataset, [
        "name", "ssn", "email", "phone", "address"
    ])
    
    # Generalize quasi-identifiers
    dataset["age"] = generalize_age(dataset["dob"], bins=10)
    dataset["location"] = generalize_location(dataset["zip"], level="state")
    dataset["date"] = shift_dates(dataset["dates"], random_offset=True)
    
    # Apply k-anonymity
    dataset = enforce_k_anonymity(dataset, k=5)
    
    # Check l-diversity for sensitive attributes
    assert check_l_diversity(dataset, sensitive_field="condition", l=3)
    
    # Differential privacy for aggregates
    dataset = add_differential_privacy_noise(dataset, epsilon=1.0)
    
    return dataset
```

## Real-World Scenarios

### Scenario 1: Hiring Algorithm
Training data reflects historical hiring biases, causing model to discriminate against certain demographics.

### Scenario 2: Medical Diagnosis
Dataset lacks rare disease examples, causing model to miss critical diagnoses for underrepresented conditions.

### Scenario 3: Voice Assistant
Training data only includes native English speakers, failing to understand accents or non-native speakers.

## Detection Patterns

Watch for these warning signs:
- Large train-test performance gap
- Poor performance on specific subgroups
- Suspiciously high accuracy
- Features with extreme correlation to target
- Missing edge case coverage
- Privacy concerns in raw data

## Prevention Strategies

1. **Multiple Annotators**: Ensure label quality through agreement
2. **Stratified Sampling**: Balance representation across groups
3. **Leakage Audits**: Systematically check for data leakage
4. **Coverage Analysis**: Map and fill scenario gaps
5. **Privacy Review**: Legal and ethical data handling
6. **Documentation**: Datasheets for datasets
7. **Continuous Monitoring**: Track data drift over time

## Testing Checklist

- [ ] Is inter-annotator agreement above 0.8?
- [ ] Does dataset represent target population?
- [ ] Have all features been audited for leakage?
- [ ] Are edge cases adequately covered?
- [ ] Is privacy properly protected?
- [ ] Is there documentation (datasheet)?
- [ ] Is there a plan for monitoring drift?

## Related Documents

- [[overfitting_examples]] - Models memorizing bad datasets
- [[underfitting_examples]] - Models failing to learn from data
- [[benchmark_misuse]] - Evaluating on flawed benchmarks
- [[misinformation_examples]] - False information in training data
