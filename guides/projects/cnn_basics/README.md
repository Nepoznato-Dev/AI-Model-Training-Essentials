# CNN Basics Project

A minimal, beginner-friendly introduction to building Convolutional Neural Networks (CNNs) for image classification.

## What This Project Does

This project demonstrates how to:
- Build a simple CNN from scratch using PyTorch
- Load and preprocess image data
- Train a model on image classification task
- Evaluate model performance
- Make predictions on new images

## Concepts Covered

- **Convolutional Layers**: Feature extraction from images
- **Pooling Operations**: Dimensionality reduction
- **Activation Functions**: Introducing non-linearity (ReLU)
- **Fully Connected Layers**: Classification head
- **Training Loops**: Forward pass, loss calculation, backpropagation
- **Image Preprocessing**: Normalization, resizing, augmentation

## Prerequisites

Before running this project, you should be comfortable with:
- Basic Python programming
- Installing Python packages with pip
- Basic neural network concepts (optional but helpful)

If you're new to these concepts, check out:
- [Python Basics](../User%20Questions/prerequisites/python_basics.md)
- [CNNs Guide](../../CNNs/)

## Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Visit [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy the code from `main.py` into cells
4. Click **Runtime → Change runtime type** and select **GPU**
5. Run each cell sequentially

**Benefits:**
- No setup required
- Free GPU access (essential for CNN training)
- Pre-installed libraries (torch, torchvision)
- Easy to experiment and modify

### Option 2: Local Installation

```bash
# Navigate to this project directory
cd guides/projects/cnn_basics

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

**Note:** Training on CPU will be slow. A GPU is highly recommended!

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Main script with heavily commented code (~250 lines) |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation file |
| `cnn_basics.ipynb` | Jupyter notebook version (optional) |

## Code Walkthrough

### Step 1: Import Required Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
```

We use:
- **PyTorch**: Deep learning framework
- **TorchVision**: Dataset loading and transformations
- **DataLoader**: Efficient batch loading

### Step 2: Define the CNN Architecture

```python
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        # Pooling layer
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully connected layers
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 10)
        
        # Activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # Conv + ReLU + Pool
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        
        # Flatten
        x = x.view(-1, 64 * 8 * 8)
        
        # Fully connected layers
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        
        return x
```

### Step 3: Load and Preprocess Data

```python
# Define transformations
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load CIFAR-10 dataset
trainset = datasets.CIFAR10(root='./data', train=True, 
                            download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
```

### Step 4: Initialize Model, Loss, and Optimizer

```python
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### Step 5: Training Loop

```python
for epoch in range(num_epochs):
    for images, labels in trainloader:
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### Step 6: Evaluation

```python
correct = 0
total = 0

with torch.no_grad():
    for images, labels in testloader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total
print(f'Accuracy: {accuracy:.2f}%')
```

## Exercises

Try these modifications to deepen your understanding:

### Exercise 1: Modify the Architecture
Add more convolutional layers or change the number of filters. How does it affect accuracy?

### Exercise 2: Try Different Optimizers
Replace Adam with SGD or RMSprop. Compare training speed and final accuracy.

### Exercise 3: Add Data Augmentation
Add random flips, rotations, or crops to the transformations. Does it improve generalization?

### Exercise 4: Experiment with Hyperparameters
Change:
- Learning rate
- Batch size
- Number of epochs

Track how each affects training.

### Exercise 5: Visualize Filters
Extract and visualize the learned convolutional filters to understand what features the network detects.

## Common Issues & Solutions

### Issue: CUDA Out of Memory

**Solution:**
Reduce batch size:
```python
trainloader = DataLoader(trainset, batch_size=32, shuffle=True)  # Was 64
```

Or use gradient accumulation for effective larger batches.

### Issue: Slow Training on CPU

**Solution:**
CNNs are computationally intensive. Options:
1. Use Google Colab with GPU enabled (recommended)
2. Reduce image size (e.g., 16x16 instead of 32x32)
3. Use fewer training samples for experimentation
4. Reduce model complexity

### Issue: Low Accuracy

**Solution:**
Try these improvements:
1. Train for more epochs
2. Add more convolutional layers
3. Use data augmentation
4. Adjust learning rate
5. Add batch normalization

### Issue: Overfitting (High train, low test accuracy)

**Solution:**
1. Add dropout layers
2. Use data augmentation
3. Add L2 regularization
4. Reduce model complexity
5. Use early stopping

## Understanding CNN Components

### Convolutional Layer
- Applies filters/kernels to detect features
- Learns edges, textures, patterns hierarchically
- Preserves spatial relationships

### Pooling Layer
- Reduces spatial dimensions
- Provides translation invariance
- Common types: Max pooling, Average pooling

### Activation Function (ReLU)
- Introduces non-linearity
- Allows network to learn complex patterns
- Formula: f(x) = max(0, x)

### Fully Connected Layer
- Combines features for classification
- Outputs class probabilities
- Typically at the end of the network

## Expected Results

With the default configuration:
- **Training Time**: ~5-10 minutes on GPU (Colab)
- **Final Accuracy**: 60-70% on CIFAR-10 test set
- **Epochs**: 10

**Note:** This is a simple educational model. State-of-the-art models achieve 95%+ but are much more complex.

## Next Steps

After completing this project:

1. **Read the Guide**: Check out the full [CNNs Guide](../../CNNs/) for deeper theory

2. **Try Advanced Architectures**:
   - ResNet (skip connections)
   - VGG (deep networks)
   - EfficientNet (compound scaling)

3. **Work on Real Projects**:
   - Custom image classifier
   - Object detection
   - Image segmentation

4. **Learn Transfer Learning**:
   - Use pre-trained models
   - Fine-tune on your dataset
   - Achieve better results with less data

## Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [CS231n: CNNs for Visual Recognition](http://cs231n.stanford.edu/) - Stanford course
- [Papers With Code](https://paperswithcode.com/) - Research papers with implementations
- [Kaggle Courses](https://www.kaggle.com/learn) - Practical deep learning courses

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~250 |
| Time to Complete | 20-30 minutes (including training) |
| GPU Required | Recommended (CPU works but slow) |
| Difficulty | ⭐⭐☆ Easy |
| Prerequisites | Basic Python, basic ML concepts |

## Contributing

Found an issue? Have a suggestion? Feel free to:
- Open an issue on GitHub
- Submit a pull request with improvements
- Share your extensions in the community

---

**Happy Learning!** 🎉

Remember: The best way to learn deep learning is by experimenting. Change things, break them, and learn from it!
