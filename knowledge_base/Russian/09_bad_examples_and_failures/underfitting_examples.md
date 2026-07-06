# Underfitting Examples

## Overview

Underfitting occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance on both training and test sets. The model fails to learn the relationship between inputs and outputs, leading to high bias and systematic errors.

## When to Reference This Document

- Debugging poor model performance
- Selecting appropriate model complexity
- Evaluating feature engineering needs
- Diagnosing high bias problems
- Improving model capacity

## Common Underfitting Scenarios

### Model Too Simple

**Bad Example**:
```python
# Using linear regression for non-linear data
from sklearn.linear_model import LinearRegression

# Data has clear quadratic relationship: y = x^2 + 2x + 1
X = np.random.randn(1000, 1)
y = X[:, 0]**2 + 2*X[:, 0] + 1 + np.random.randn(1000) * 0.1

model = LinearRegression()
model.fit(X, y)

# Train R²: 0.15, Test R²: 0.12
# Model cannot capture curvature
```

**Why It's Bad**:
- Cannot represent non-linear relationships
- High bias, systematic errors
- Poor fit even on training data
- Misses important patterns

**Solution**: Use more expressive model
```python
# Option 1: Polynomial features
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('linear', LinearRegression())
])
pipeline.fit(X, y)
# Train R²: 0.98, Test R²: 0.97

# Option 2: Non-linear model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, max_depth=10)
model.fit(X, y)
# Train R²: 0.99, Test R²: 0.98
```

### Insufficient Training

**Bad Example**:
```python
# Deep learning model stopped too early
model = create_deep_network()

# Training for only 2 epochs
for epoch in range(2):
    train_loss = train_one_epoch(model, train_loader)

# Train accuracy: 45%, Test accuracy: 43%
# Model hasn't had time to learn
```

**Why It's Bad**:
- Weights not properly optimized
- Loss far from minimum
- Model潜力未发挥 (untapped potential)
- Premature conclusion about model capability

**Solution**: Train until convergence with proper monitoring
```python
# Train with convergence monitoring
max_epochs = 100
patience = 10
best_loss = float('inf')
no_improve_count = 0

for epoch in range(max_epochs):
    train_loss = train_one_epoch(model, train_loader)
    val_loss = evaluate(model, val_loader)
    
    if val_loss < best_loss:
        best_loss = val_loss
        no_improve_count = 0
        save_checkpoint(model, epoch)
    else:
        no_improve_count += 1
    
    print(f"Epoch {epoch}: train={train_loss:.4f}, val={val_loss:.4f}")
    
    # Stop if converged
    if no_improve_count >= patience:
        print(f"Converged at epoch {epoch}")
        break

# Typical result: converges at epoch 45
# Train accuracy: 94%, Test accuracy: 92%
```

### Poor Feature Engineering

**Bad Example**:
```python
# Predicting house prices with inadequate features
features = ['house_id']  # Useless feature

# Missing important predictors:
# - square_footage
# - number_of_bedrooms
# - location
# - age_of_house
# - neighborhood_quality

model = LinearRegression()
model.fit(X, y)

# R²: 0.02 (essentially random prediction)
```

**Why It's Bad**:
- Missing predictive information
- Model cannot learn without relevant signals
- Garbage in, garbage out
- Fundamental problem, not model issue

**Solution**: Comprehensive feature engineering
```python
# Create informative features
features = [
    'square_footage',
    'bedrooms',
    'bathrooms',
    'lot_size',
    'year_built',
    'garage_spaces',
    'neighborhood_rating',
    'school_district_score',
    'distance_to_city_center',
    'crime_rate',
    'price_per_sqft_neighborhood',
    'age_of_house',
    'renovated_last_5_years',
]

# Add interaction features
features.append('sqft_per_bedroom')
features.append('price_to_income_ratio')

# Add polynomial features for non-linear relationships
# Add temporal features (season, day_of_week)

model = GradientBoostingRegressor()
model.fit(X[features], y)

# R²: 0.85 with proper features
```

### Excessive Regularization

**Bad Example**:
```python
# Overly aggressive regularization prevents learning
from sklearn.linear_model import Ridge

# Extremely high regularization parameter
model = Ridge(alpha=1000000)  # Almost forces all coefficients to zero
model.fit(X, y)

# All coefficients near zero
# Train accuracy: 30%, Test accuracy: 28%
# Model essentially predicts mean for everything
```

**Why It's Bad**:
- Regularization overwhelms signal
- Model capacity artificially constrained
- Cannot fit even training data well
- Defeats purpose of learning

**Solution**: Tune regularization appropriately
```python
from sklearn.model_selection import GridSearchCV

# Search for optimal regularization strength
param_grid = {
    'alpha': [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
}

grid_search = GridSearchCV(
    Ridge(),
    param_grid,
    cv=5,
    scoring='r2'
)
grid_search.fit(X, y)

# Best alpha: 1.0
# Train R²: 0.88, Test R²: 0.86

# Or use cross-validation to find sweet spot
alphas = np.logspace(-4, 4, 50)
cv_scores = []

for alpha in alphas:
    model = Ridge(alpha=alpha)
    scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    cv_scores.append(scores.mean())

# Plot: low alpha = overfitting, high alpha = underfitting
# Choose alpha at peak of curve
```

### Information Loss in Preprocessing

**Bad Example**:
```python
# Aggregating away important variation
def preprocess_data(df):
    # Binning continuous variables loses information
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 55, 100], 
                             labels=['young', 'adult', 'middle', 'senior'])
    
    # Dropping "outliers" that contain signal
    df = df[df['income'] < 100000]  # Removes high-value customers
    
    # One-hot encoding with rare category collapse
    df['city'] = df['city'].apply(lambda x: x if x in top_5_cities else 'other')
    
    return df

# Model cannot distinguish within groups
# Important patterns lost
```

**Why It's Bad**:
- Discards predictive information
- Reduces model's ability to discriminate
- Creates artificial ceilings on performance
- May introduce bias

**Solution**: Preserve information in preprocessing
```python
def preprocess_data(df):
    # Keep continuous variables continuous
    df['age'] = df['age']  # Let model learn non-linear relationships
    
    # Handle outliers appropriately
    # Use robust scaling instead of dropping
    df['income_log'] = np.log1p(df['income'])  # Compress scale without losing data
    
    # Use target encoding for high-cardinality categoricals
    city_encoding = df.groupby('city')['target'].mean()
    df['city_encoded'] = df['city'].map(city_encoding)
    
    # Add features, don't just transform
    df['age_squared'] = df['age'] ** 2
    df['income_to_age_ratio'] = df['income'] / (df['age'] + 1)
    
    return df
```

## Real-World Scenarios

### Scenario 1: Spam Detection
Simple keyword matching misses sophisticated phishing attempts, allowing 40% of spam through filters.

### Scenario 2: Demand Forecasting
Linear trend model fails to capture seasonality and promotions, resulting in 50% forecast errors.

### Scenario 3: Medical Risk Prediction
Basic logistic regression with few features misses complex interactions, failing to identify high-risk patients.

## Detection Patterns

Watch for these warning signs:
- Low accuracy on both train and test sets
- High bias (systematic errors in same direction)
- Learning curves plateau at poor performance
- Adding more data doesn't help
- Simpler models perform similarly
- Residuals show clear patterns

## Prevention Strategies

1. **Increase Model Capacity**: More parameters, deeper networks
2. **Better Features**: Domain expertise, feature engineering
3. **Reduce Regularization**: Allow model to fit data
4. **Train Longer**: Ensure convergence
5. **Try Non-linear Models**: Capture complex patterns
6. **Ensemble Methods**: Combine multiple weak learners
7. **Feature Interactions**: Explicitly model relationships

## Testing Checklist

- [ ] Is training accuracy above acceptable threshold?
- [ ] Do learning curves show convergence?
- [ ] Are features informative and sufficient?
- [ ] Is regularization appropriately tuned?
- [ ] Has model capacity been increased?
- [ ] Are residuals randomly distributed?
- [ ] Would a more complex model be appropriate?

## Related Documents

- [[overfitting_examples]] - Opposite problem: model too complex
- [[bad_dataset_examples]] - Data issues causing underfitting
- [[benchmark_misuse]] - Proper evaluation of model capacity
- [[code_smells]] - Signs of overly simplistic implementations
