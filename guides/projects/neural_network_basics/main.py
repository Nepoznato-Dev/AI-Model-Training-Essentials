# Neural Network Basics - Main Script
# A minimal, heavily-commented introduction to building neural networks from scratch
# Lines of code: ~200 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

print("=" * 70)
print("NEURAL NETWORK BASICS PROJECT - Building Your First Neural Network")
print("=" * 70)
print()

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
print()

# ============================================================================
# STEP 2: CREATE A SIMPLE DATASET
# ============================================================================

# We'll use a synthetic dataset called "make_moons"
# It creates two interleaving half circles - perfect for learning classification
print("Creating synthetic dataset (two moons)...")

X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)

# Split into training and testing sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalize the data (important for neural networks!)
# This makes all features have mean=0 and std=1
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train = torch.FloatTensor(X_train).to(device)
y_train = torch.LongTensor(y_train).to(device)
X_test = torch.FloatTensor(X_test).to(device)
y_test = torch.LongTensor(y_test).to(device)

print(f"✓ Dataset created!")
print(f"  Training samples: {len(X_train)}")
print(f"  Test samples: {len(X_test)}")
print(f"  Features per sample: {X_train.shape[1]}")
print(f"  Classes: 2 (binary classification)")
print()

# ============================================================================
# STEP 3: DEFINE THE NEURAL NETWORK ARCHITECTURE
# ============================================================================

class SimpleNeuralNet(nn.Module):
    """
    A simple feedforward neural network (also called Multi-Layer Perceptron).
    
    Architecture:
    - Input layer: 2 features (x, y coordinates)
    - Hidden layer 1: 16 neurons with ReLU activation
    - Hidden layer 2: 16 neurons with ReLU activation
    - Output layer: 2 neurons (one for each class)
    
    This is called a "feedforward" network because data flows in one direction:
    Input → Hidden Layers → Output
    """
    
    def __init__(self):
        super(SimpleNeuralNet, self).__init__()
        
        # Define the layers
        # nn.Linear creates a fully connected layer
        # Parameters: (input_size, output_size)
        
        # First hidden layer: 2 inputs → 16 neurons
        self.fc1 = nn.Linear(2, 16)
        
        # Second hidden layer: 16 inputs → 16 neurons
        self.fc2 = nn.Linear(16, 16)
        
        # Output layer: 16 inputs → 2 outputs (one per class)
        self.fc3 = nn.Linear(16, 2)
        
        # Activation function
        # ReLU = Rectified Linear Unit
        # Formula: f(x) = max(0, x)
        # It introduces non-linearity, allowing the network to learn complex patterns
        self.relu = nn.ReLU()
    
    def forward(self, x):
        """
        Forward pass: defines how data flows through the network.
        
        Args:
            x: Input tensor of shape (batch_size, 2)
        
        Returns:
            Output logits of shape (batch_size, 2)
        """
        # Pass data through first hidden layer
        x = self.fc1(x)      # Linear transformation
        x = self.relu(x)     # Apply ReLU activation
        
        # Pass through second hidden layer
        x = self.fc2(x)
        x = self.relu(x)
        
        # Pass through output layer
        # Note: We don't apply softmax here because CrossEntropyLoss includes it
        x = self.fc3(x)
        
        return x

# Initialize the model
model = SimpleNeuralNet().to(device)

print("✓ Neural network created!")
print(f"  Architecture: SimpleNeuralNet")
print(f"  Total parameters: {sum(p.numel() for p in model.parameters()):,}")
print()

# Let's see the architecture
print("Network architecture:")
print(model)
print()

# ============================================================================
# STEP 4: DEFINE LOSS FUNCTION AND OPTIMIZER
# ============================================================================

# Loss function: CrossEntropyLoss
# This is the standard loss for multi-class classification
# It combines LogSoftmax and NLLLoss (Negative Log Likelihood Loss)
# It measures how far our predictions are from the true labels
criterion = nn.CrossEntropyLoss()

# Optimizer: Adam
# Adam is an advanced version of gradient descent
# It adapts the learning rate for each parameter automatically
# lr (learning rate) controls how big the steps are during training
optimizer = optim.Adam(model.parameters(), lr=0.01)

print("✓ Loss function and optimizer initialized!")
print(f"  Loss function: CrossEntropyLoss")
print(f"  Optimizer: Adam (learning rate = 0.01)")
print()

# ============================================================================
# STEP 5: TRAINING LOOP
# ============================================================================

# Number of epochs (how many times to go through the entire dataset)
num_epochs = 100

print(f"Starting training for {num_epochs} epochs...")
print("-" * 70)

# Track training progress
train_losses = []
train_accuracies = []

for epoch in range(num_epochs):
    # Set model to training mode
    model.train()
    
    # Forward pass: make predictions
    outputs = model(X_train)
    
    # Calculate loss (how wrong are we?)
    loss = criterion(outputs, y_train)
    
    # Backward pass and optimization
    optimizer.zero_grad()  # Clear previous gradients (important!)
    loss.backward()        # Compute gradients (backpropagation)
    optimizer.step()       # Update weights
    
    # Calculate accuracy
    _, predicted = torch.max(outputs, 1)
    accuracy = 100 * (predicted == y_train).sum().item() / len(y_train)
    
    # Track progress
    train_losses.append(loss.item())
    train_accuracies.append(accuracy)
    
    # Print progress every 20 epochs
    if (epoch + 1) % 20 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}] | "
              f"Loss: {loss.item():.4f} | "
              f"Accuracy: {accuracy:.2f}%")

print("-" * 70)
print(f"✓ Training completed!")
print()

# ============================================================================
# STEP 6: EVALUATE ON TEST SET
# ============================================================================

print("Evaluating on test set...")
print("-" * 70)

# Set model to evaluation mode
# This disables dropout and batch normalization updates (not used here, but good practice)
model.eval()

# Disable gradient computation for evaluation (saves memory and speeds up)
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
    
    # Calculate test accuracy
    test_accuracy = 100 * (predicted == y_test).sum().item() / len(y_test)
    
    print(f"Test Accuracy: {test_accuracy:.2f}%")
    print(f"Correct predictions: {(predicted == y_test).sum().item()}/{len(y_test)}")

print("-" * 70)
print()

# ============================================================================
# STEP 7: MAKE PREDICTIONS ON NEW DATA
# ============================================================================

print("Making predictions on new data points...")
print("-" * 70)

# Create some new test points
new_points = torch.FloatTensor([
    [0.0, 0.0],    # Center
    [1.0, 0.5],    # Right side
    [-1.0, -0.5],  # Left side
    [0.5, -1.0],   # Bottom
]).to(device)

# Scale them using the same scaler
new_points_scaled = scaler.transform(new_points.cpu().numpy())
new_points_scaled = torch.FloatTensor(new_points_scaled).to(device)

# Make predictions
model.eval()
with torch.no_grad():
    outputs = model(new_points_scaled)
    probabilities = torch.softmax(outputs, dim=1)
    _, predicted = torch.max(outputs, 1)

# Display results
for i, point in enumerate(new_points):
    pred_class = predicted[i].item()
    prob = probabilities[i][pred_class].item()
    print(f"Point ({point[0]:.2f}, {point[1]:.2f}) → "
          f"Class {pred_class} (confidence: {prob:.2%})")

print()

# ============================================================================
# STEP 8: VISUALIZE THE DECISION BOUNDARY
# ============================================================================

print("Visualizing the decision boundary...")
print("(This shows how the network separates the two classes)")
print()

# Create a grid of points
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 100),
    np.linspace(y_min, y_max, 100)
)

# Flatten the grid
grid_points = np.c_[xx.ravel(), yy.ravel()]
grid_points_scaled = scaler.transform(grid_points)
grid_tensor = torch.FloatTensor(grid_points_scaled).to(device)

# Predict class for each point in the grid
model.eval()
with torch.no_grad():
    outputs = model(grid_tensor)
    _, predictions = torch.max(outputs, 1)
    predictions = predictions.cpu().numpy()

# Reshape predictions back to grid
predictions_grid = predictions.reshape(xx.shape)

# Plot
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, predictions_grid, alpha=0.3, cmap='coolwarm')
# Inverse-transform scaled data back to original space for correct plotting
X_train_orig = scaler.inverse_transform(X_train.cpu().numpy())
X_test_orig = scaler.inverse_transform(X_test.cpu().numpy())
plt.scatter(X_train_orig[:, 0], X_train_orig[:, 1], c=y_train.cpu(), 
           cmap='coolwarm', edgecolors='k', s=20, label='Training data')
plt.scatter(X_test_orig[:, 0], X_test_orig[:, 1], c=y_test.cpu(), 
           cmap='coolwarm', edgecolors='k', s=40, marker='x', label='Test data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Neural Network Decision Boundary')
plt.legend()
plt.colorbar(label='Predicted Class')
plt.tight_layout()
plt.savefig('neural_network_decision_boundary.png', dpi=100)
print("✓ Decision boundary plot saved as 'neural_network_decision_boundary.png'")
print()

# ============================================================================
# STEP 9: SAVE THE MODEL (OPTIONAL)
# ============================================================================

save_path = "neural_network_model.pth"
torch.save(model.state_dict(), save_path)
print(f"✓ Model saved to '{save_path}'")
print()

# To load the model later:
# model = SimpleNeuralNet()
# model.load_state_dict(torch.load("neural_network_model.pth", weights_only=True))
# model.eval()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the Neural Network Basics Project!")
print("=" * 70)
print(f"""
What you learned:
✓ How to create a simple feedforward neural network (MLP)
✓ What neurons, layers, and activation functions are
✓ How to prepare and normalize data
✓ How to train a neural network with backpropagation
✓ How to evaluate model performance
✓ How to make predictions with trained models
✓ How to visualize what the network learned

Key Concepts:
- Neurons: Basic computing units that take inputs and produce outputs
- Layers: Groups of neurons that process information
- Activation functions (ReLU): Add non-linearity to learn complex patterns
- Loss function: Measures how wrong the predictions are
- Optimizer (Adam): Updates weights to reduce the loss
- Backpropagation: Algorithm that computes gradients for weight updates

Results Summary:
- Final training accuracy: {train_accuracies[-1]:.2f}%
- Test accuracy: {test_accuracy:.2f}%
- Model saved: {save_path}

Next steps:
1. Try changing the number of neurons or layers
2. Experiment with different learning rates
3. Add more hidden layers (deep neural network)
4. Try different activation functions (Sigmoid, Tanh)
5. Work on a real dataset (MNIST, CIFAR-10)

Resources:
- PyTorch Documentation: https://pytorch.org/docs/
- 3Blue1Brown Neural Networks: https://www.youtube.com/watch?v=aircAruvnKk
- Fast.ai Course: https://course.fast.ai/
""")
print("=" * 70)
