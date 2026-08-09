# Neural Network Basics Project

A minimal, beginner-friendly introduction to building neural networks from scratch using PyTorch.

## What This Project Does

This project demonstrates how to:
- Build a simple feedforward neural network (Multi-Layer Perceptron) from scratch
- Create and preprocess a synthetic dataset
- Train a neural network with backpropagation
- Evaluate model performance
- Visualize what the network has learned (decision boundary)
- Make predictions on new data

## Concepts Covered

- **Neurons**: The basic computing unit of a neural network
- **Layers**: Input, hidden, and output layers
- **Activation Functions**: ReLU and why non-linearity matters
- **Forward Pass**: How data flows through the network
- **Loss Function**: Measuring how wrong predictions are
- **Backpropagation**: How the network learns from mistakes
- **Optimizers**: Adam and gradient descent
- **Data Normalization**: Why scaling features is important

## Prerequisites

Before running this project, you should be comfortable with:
- Basic Python programming
- Installing Python packages with pip
- Very basic understanding of what a neural network is (optional but helpful)

If you're new to these concepts, check out:
- [Python Basics](../User%20Questions/prerequisites/python_basics.md)
- [Mathematics for ML](../../prerequisites/mathematics_for_ml.md)

## Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Visit [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy the code from `main.py` into cells
4. Click **Runtime → Change runtime type** and select **GPU** (optional)
5. Run each cell sequentially

**Benefits:**
- No setup required
- Free GPU access
- Pre-installed libraries
- Easy to experiment and modify

### Option 2: Local Installation

```bash
# Navigate to this project directory
cd guides/projects/neural_network_basics

# Create a virtual environment (recommended)
python -m venv venv

# Activate the environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the project
python main.py
```

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Main script with heavily commented code (~200 lines) |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation file |

## Code Walkthrough

### Step 1: Import Required Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
```

We use:
- **PyTorch**: Deep learning framework for building and training the network
- **scikit-learn**: For creating the synthetic dataset and preprocessing
- **matplotlib**: For visualizing results

### Step 2: Create a Simple Dataset

```python
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
```

We use the "two moons" dataset - two interleaving half circles. This is perfect for learning because:
- It's simple to understand
- It's not linearly separable (a straight line can't separate the classes)
- The network must learn a curved decision boundary

### Step 3: Define the Neural Network

```python
class SimpleNeuralNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 16)   # Input: 2 features → 16 neurons
        self.fc2 = nn.Linear(16, 16)  # Hidden: 16 → 16
        self.fc3 = nn.Linear(16, 2)   # Output: 16 → 2 classes
        self.relu = nn.ReLU()
```

This creates a network with:
- 2 input neurons (x, y coordinates)
- Two hidden layers with 16 neurons each
- 2 output neurons (one per class)

### Step 4: Train the Network

```python
for epoch in range(num_epochs):
    outputs = model(X_train)          # Forward pass
    loss = criterion(outputs, y_train) # Calculate loss
    optimizer.zero_grad()              # Clear gradients
    loss.backward()                    # Backpropagation
    optimizer.step()                   # Update weights
```

This is the training loop - the heart of neural network learning.

### Step 5: Visualize Results

The script creates a decision boundary plot showing how the network separates the two classes.

## Exercises

Try these modifications to deepen your understanding:

### Exercise 1: Change the Architecture
Add more hidden layers or change the number of neurons. How does it affect accuracy?

```python
self.fc1 = nn.Linear(2, 32)   # More neurons
self.fc2 = nn.Linear(32, 32)
self.fc3 = nn.Linear(32, 16)  # Extra layer
self.fc4 = nn.Linear(16, 2)
```

### Exercise 2: Try Different Learning Rates
Change the learning rate and observe how training changes:

```python
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Slower
optimizer = optim.Adam(model.parameters(), lr=0.1)    # Faster
```

### Exercise 3: Different Activation Functions
Replace ReLU with other activation functions:

```python
self.sigmoid = nn.Sigmoid()  # Try this instead
self.tanh = nn.Tanh()        # Or this
```

### Exercise 4: More Training Data
Increase the dataset size and see if accuracy improves:

```python
X, y = make_moons(n_samples=5000, noise=0.2, random_state=42)
```

### Exercise 5: Different Datasets
Try other scikit-learn datasets:
- `make_circles()` - Concentric circles
- `make_blobs()` - Clusters of points
- `make_classification()` - More complex patterns

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'torch'"

**Solution:**
```bash
pip install -r requirements.txt
```

Make sure your virtual environment is activated.

### Issue: Low accuracy

**Solution:**
1. Train for more epochs (increase `num_epochs`)
2. Add more neurons or layers
3. Try a different learning rate
4. Check that data is properly normalized

### Issue: Loss not decreasing

**Solution:**
1. Learning rate might be too low - increase it
2. Check that data is normalized
3. Try a different optimizer (SGD, RMSprop)

### Issue: Overfitting (high train accuracy, low test accuracy)

**Solution:**
1. Add dropout layers: `self.dropout = nn.Dropout(0.2)`
2. Get more training data
3. Reduce network complexity
4. Add regularization

## Understanding Neural Network Components

### Neuron
- Takes multiple inputs
- Multiplies each by a weight
- Adds a bias term
- Applies an activation function
- Produces one output

### Layer
- A group of neurons operating on the same input
- Input layer: receives raw data
- Hidden layers: transform data progressively
- Output layer: produces final predictions

### Activation Function (ReLU)
- Formula: f(x) = max(0, x)
- Introduces non-linearity
- Without it, the network could only learn linear patterns
- Allows the network to learn complex, curved boundaries

### Loss Function (CrossEntropyLoss)
- Measures how far predictions are from true labels
- Lower loss = better predictions
- The network tries to minimize this during training

### Optimizer (Adam)
- Updates weights based on gradients
- Adam adapts learning rate per parameter
- More efficient than basic gradient descent

## Expected Results

With the default configuration:
- **Training Time**: ~5-10 seconds on CPU
- **Final Training Accuracy**: 95%+
- **Test Accuracy**: 90%+
- **Epochs**: 100

## Next Steps

After completing this project:

1. **Read the Guide**: Check out the full [Neural Networks Guide](../README.md) for deeper theory

2. **Try the CNN Basics Project**: Learn about convolutional networks for images

3. **Work on Real Datasets**:
   - MNIST (handwritten digits)
   - CIFAR-10 (image classification)
   - Your own data!

4. **Learn Advanced Topics**:
   - Dropout and regularization
   - Batch normalization
   - Learning rate scheduling
   - Different optimizer algorithms

## Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [3Blue1Brown Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk) - Visual explanation
- [Fast.ai Course](https://course.fast.ai/) - Practical deep learning
- [Playground](https://playground.tensorflow.org/) - Interactive neural network visualizer

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~200 |
| Time to Complete | 10-15 minutes |
| GPU Required | No (CPU works fine) |
| Difficulty | ⭐☆☆ Beginner |
| Prerequisites | Basic Python |

## Contributing

Found an issue? Have a suggestion? Feel free to:
- Open an issue on GitHub
- Submit a pull request with improvements
- Share your extensions in the community

---

**Happy Learning!** 🎉

Remember: Every expert started with a simple neural network. Experiment, break things, and learn!
