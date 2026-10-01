# Neural Network Basics - Main Script
# A minimal, heavily-commented introduction to building neural networks from scratch
# Lines of code: ~200 (including comments)

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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
print()

print("Creating synthetic dataset (two moons)...")
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_tensor = torch.FloatTensor(X_train_scaled).to(device)
y_train = torch.LongTensor(y_train).to(device)
X_test_tensor = torch.FloatTensor(X_test_scaled).to(device)
y_test = torch.LongTensor(y_test).to(device)

print("✓ Dataset created!")
print(f"  Training samples: {len(X_train_tensor)}")
print(f"  Test samples: {len(X_test_tensor)}")
print(f"  Features per sample: {X_train_tensor.shape[1]}")
print(f"  Classes: 2 (binary classification)")
print()

class SimpleNeuralNet(nn.Module):
    """A small feedforward neural network for binary classification."""

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        return self.fc3(x)

model = SimpleNeuralNet().to(device)

print("✓ Neural network created!")
print(f"  Architecture: SimpleNeuralNet")
print(f"  Total parameters: {sum(p.numel() for p in model.parameters()):,}")
print()
print("Network architecture:")
print(model)
print()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

print("✓ Loss function and optimizer initialized!")
print(f"  Loss function: CrossEntropyLoss")
print(f"  Optimizer: Adam (learning rate = 0.01)")
print()

num_epochs = 100
print(f"Starting training for {num_epochs} epochs...")
print("-" * 70)

train_losses = []
train_accuracies = []

for epoch in range(num_epochs):
    model.train()
    outputs = model(X_train_tensor)
    loss = criterion(outputs, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    predicted = outputs.argmax(dim=1)
    accuracy = 100 * (predicted == y_train).sum().item() / len(y_train)
    train_losses.append(loss.item())
    train_accuracies.append(accuracy)

    if (epoch + 1) % 20 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}] | Loss: {loss.item():.4f} | Accuracy: {accuracy:.2f}%")

print("-" * 70)
print("✓ Training completed!")
print()

print("Evaluating on test set...")
print("-" * 70)
model.eval()
with torch.no_grad():
    outputs = model(X_test_tensor)
    predicted = outputs.argmax(dim=1)
    test_accuracy = 100 * (predicted == y_test).sum().item() / len(y_test)

print(f"Test Accuracy: {test_accuracy:.2f}%")
print(f"Correct predictions: {(predicted == y_test).sum().item()}/{len(y_test)}")
print("-" * 70)
print()

print("Making predictions on new data points...")
print("-" * 70)

new_points = np.array([
    [0.0, 0.0],
    [1.0, 0.5],
    [-1.0, -0.5],
    [0.5, -1.0],
])
new_points_scaled = scaler.transform(new_points)
new_points_tensor = torch.FloatTensor(new_points_scaled).to(device)

model.eval()
with torch.no_grad():
    outputs = model(new_points_tensor)
    probabilities = torch.softmax(outputs, dim=1)
    predicted = outputs.argmax(dim=1)

for i, point in enumerate(new_points):
    pred_class = predicted[i].item()
    prob = probabilities[i][pred_class].item()
    print(f"Point ({point[0]:.2f}, {point[1]:.2f}) → Class {pred_class} (confidence: {prob:.2%})")

print()
print("Visualizing the decision boundary...")
print("The model was trained on standardized features, so the grid and data points must use the same scaled coordinate system.")
print()

# Work entirely in standardized coordinates for the visualization.
all_scaled = np.vstack([X_train_scaled, X_test_scaled])
x_min, x_max = all_scaled[:, 0].min() - 0.5, all_scaled[:, 0].max() + 0.5
y_min, y_max = all_scaled[:, 1].min() - 0.5, all_scaled[:, 1].max() + 0.5
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 100),
    np.linspace(y_min, y_max, 100)
)

grid_points_scaled = np.c_[xx.ravel(), yy.ravel()]
grid_tensor = torch.FloatTensor(grid_points_scaled).to(device)

model.eval()
with torch.no_grad():
    outputs = model(grid_tensor)
    predictions = outputs.argmax(dim=1).cpu().numpy()

predictions_grid = predictions.reshape(xx.shape)

plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, predictions_grid, alpha=0.3, cmap="coolwarm")
plt.scatter(
    X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train.cpu(),
    cmap="coolwarm", edgecolors="k", s=20, label="Training data"
)
plt.scatter(
    X_test_scaled[:, 0], X_test_scaled[:, 1], c=y_test.cpu(),
    cmap="coolwarm", edgecolors="k", s=40, marker="x", label="Test data"
)
plt.xlabel("Standardized Feature 1")
plt.ylabel("Standardized Feature 2")
plt.title("Neural Network Decision Boundary (Standardized Features)")
plt.legend()
plt.colorbar(label="Predicted Class")
plt.tight_layout()
plt.savefig("neural_network_decision_boundary.png", dpi=100)
print("✓ Decision boundary plot saved as 'neural_network_decision_boundary.png'")
print()

save_path = "neural_network_model.pth"
torch.save(model.state_dict(), save_path)
print(f"✓ Model saved to '{save_path}'")
print()

# To load the model later:
# model = SimpleNeuralNet()
# model.load_state_dict(torch.load("neural_network_model.pth", weights_only=True))
# model.eval()

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
