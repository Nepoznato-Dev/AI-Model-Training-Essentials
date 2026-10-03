# Machine Learning Fundamentals

Core concepts and principles of machine learning required for deep learning specialization.

## 1. Introduction to Machine Learning

### What is Machine Learning?
- Definition and motivation
- Traditional programming vs. ML
- Types of learning paradigms

### Learning Paradigms
- **Supervised Learning**: Learning from labeled data
- **Unsupervised Learning**: Finding patterns in unlabeled data
- **Reinforcement Learning**: Learning through interaction and rewards
- **Self-Supervised Learning**: Learning from data itself

## 2. Core Concepts

### Features and Labels
- Feature vectors and representation
- Target variables (regression vs. classification)
- Feature engineering basics

### Training and Evaluation
- Training, validation, and test sets
- Cross-validation techniques
- Data leakage and how to avoid it

### Model Performance Metrics
- **Classification**: Accuracy, precision, recall, F1-score, ROC-AUC
- **Regression**: MSE, MAE, R²
- **Ranking**: NDCG, MAP

## 3. Classical ML Algorithms

### Linear Models
- Linear regression
- Logistic regression
- Regularization (L1/Lasso, L2/Ridge, Elastic Net)

### Tree-Based Methods
- Decision trees
- Random forests
- Gradient boosting (XGBoost, LightGBM)

### Support Vector Machines
- Maximum margin classification
- Kernel trick
- SVM for regression

### Clustering Algorithms
- K-means clustering
- Hierarchical clustering
- DBSCAN

### Dimensionality Reduction
- PCA (Principal Component Analysis)
- t-SNE and UMAP for visualization

## 4. Neural Networks Basics

### Perceptron and MLP
- Single perceptron model
- Multi-layer perceptrons (MLP)
- Activation functions (ReLU, sigmoid, tanh, softmax)

### Forward Propagation
- Computing predictions
- Computational graphs

### Backpropagation
- Chain rule application
- Computing gradients
- Weight updates

### Training Neural Networks
- Loss functions
- Optimizers (SGD, Adam, RMSprop)
- Learning rate scheduling
- Batch size considerations

## 5. Regularization Techniques

### Preventing Overfitting
- L1 and L2 regularization
- Dropout
- Early stopping
- Data augmentation

### Normalization
- Batch normalization
- Layer normalization
- Weight normalization

## 6. Practical Considerations

### Data Preprocessing
- Handling missing values
- Feature scaling (standardization, normalization)
- Encoding categorical variables
- Handling imbalanced datasets

### Hyperparameter Tuning
- Grid search
- Random search
- Bayesian optimization
- Automated hyperparameter tuning (AutoML)

### Model Selection
- Bias-variance tradeoff
- Underfitting vs. overfitting
- Model complexity

## 7. Deep Learning Readiness

### When to Use Deep Learning
- Large datasets available
- Complex patterns (images, text, speech)
- End-to-end learning beneficial
- Computational resources available

### When Classical ML Suffices
- Small to medium datasets
- Tabular data
- Interpretability requirements
- Limited computational resources

## 🛠️ Hands-On Practice

### Essential Libraries
```python
# Scikit-learn for classical ML
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# PyTorch for deep learning
import torch
import torch.nn as nn
import torch.optim as optim
```

### Mini Projects to Try
1. **Iris Classification**: Multi-class classification with classical ML
2. **House Price Prediction**: Regression with feature engineering
3. **MNIST Digit Recognition**: Introduction to neural networks
4. **Sentiment Analysis**: Text classification with embeddings

## 📚 Recommended Resources

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "Pattern Recognition and Machine Learning" by Christopher Bishop
- "The Elements of Statistical Learning" by Hastie et al.

### Online Courses
- Andrew Ng's Machine Learning Course (Coursera)
- Fast.ai Practical Deep Learning
- Google's Machine Learning Crash Course

### Practice Platforms
- Kaggle: Competitions and datasets
- UCI Machine Learning Repository
- Hugging Face Datasets

## ✅ Self-Assessment Checklist

You're ready for advanced deep learning when you can:

- [ ] Explain the difference between supervised and unsupervised learning
- [ ] Implement linear regression from scratch
- [ ] Describe how backpropagation works
- [ ] Choose appropriate evaluation metrics for a problem
- [ ] Handle overfitting with regularization techniques
- [ ] Train a simple neural network using PyTorch/TensorFlow
- [ ] Perform basic feature engineering on tabular data

## 💡 Tips for Success

1. **Start simple**: Begin with linear models before deep learning
2. **Understand the why**: Don't just use algorithms, understand how they work
3. **Practice consistently**: Work on small projects regularly
4. **Read code**: Study implementations on GitHub
5. **Join communities**: Kaggle, Reddit r/MachineLearning, Discord servers

---

**Next Steps**: After mastering ML fundamentals, choose your specialization:
- [CNNs](../CNNs/README.md) for computer vision
- [Transformers](../Transformers/README.md) for NLP
- [GANs](../GANs/README.md) for generative models
- [GNNs](../GNNs/README.md) for graph data
- [Agentic Systems](../Agentic_Systems/README.md) for autonomous agents
