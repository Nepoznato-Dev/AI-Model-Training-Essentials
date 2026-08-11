# Neural Network Basics - Main Script
# Beginner-friendly MLP classification example using a synthetic two-moons dataset.

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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Keep three distinct splits: training for fitting, validation for model
# selection, and test for the final unbiased evaluation.
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32, device=device)
y_train = torch.tensor(y_train, dtype=torch.long, device=device)
X_val = torch.tensor(X_val, dtype=torch.float32, device=device)
y_val = torch.tensor(y_val, dtype=torch.long, device=device)
X_test = torch.tensor(X_test, dtype=torch.float32, device=device)
y_test = torch.tensor(y_test, dtype=torch.long, device=device)

print(f"Training samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")
print(f"Test samples: {len(X_test)}")


class SimpleNeuralNet(nn.Module):
    """Small feedforward network for two-class classification."""

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 16)
        self.fc2 = nn.Linear(16, 16)
        self.fc3 = nn.Linear(16, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        return self.fc3(x)  # CrossEntropyLoss applies the class normalization.


model = SimpleNeuralNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
num_epochs = 100

train_losses = []
train_accuracies = []
val_losses = []
val_accuracies = []
best_val_loss = float("inf")
best_state = None

for epoch in range(num_epochs):
    model.train()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    with torch.no_grad():
        train_predictions = outputs.argmax(dim=1)
        train_accuracy = (train_predictions == y_train).float().mean().item() * 100

        model.eval()
        val_outputs = model(X_val)
        val_loss = criterion(val_outputs, y_val)
        val_predictions = val_outputs.argmax(dim=1)
        val_accuracy = (val_predictions == y_val).float().mean().item() * 100

    train_losses.append(loss.item())
    train_accuracies.append(train_accuracy)
    val_losses.append(val_loss.item())
    val_accuracies.append(val_accuracy)

    # Select the checkpoint using validation data, never the test set.
    if val_loss.item() < best_val_loss:
        best_val_loss = val_loss.item()
        best_state = {key: value.detach().cpu().clone() for key, value in model.state_dict().items()}

    if (epoch + 1) % 20 == 0:
        print(
            f"Epoch [{epoch + 1}/{num_epochs}] | "
            f"Train loss: {loss.item():.4f} | "
            f"Train acc: {train_accuracy:.2f}% | "
            f"Val loss: {val_loss.item():.4f} | "
            f"Val acc: {val_accuracy:.2f}%"
        )

# Restore the best validation checkpoint before touching the test set.
if best_state is None:
    raise RuntimeError("No validation checkpoint was produced")
model.load_state_dict(best_state)

model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    test_loss = criterion(test_outputs, y_test).item()
    test_predictions = test_outputs.argmax(dim=1)
    test_accuracy = (test_predictions == y_test).float().mean().item() * 100

print(f"\nFinal held-out test loss: {test_loss:.4f}")
print(f"Final held-out test accuracy: {test_accuracy:.2f}%")
print(f"Correct predictions: {(test_predictions == y_test).sum().item()}/{len(y_test)}")

# New points are specified in the original feature space and transformed with
# the scaler fitted on training data only.
new_points = np.array([
    [0.0, 0.0],
    [1.0, 0.5],
    [-1.0, -0.5],
    [0.5, -1.0],
], dtype=np.float32)
new_points_scaled = torch.tensor(scaler.transform(new_points), dtype=torch.float32, device=device)

with torch.no_grad():
    outputs = model(new_points_scaled)
    probabilities = torch.softmax(outputs, dim=1)
    predictions = outputs.argmax(dim=1)

for i, point in enumerate(new_points):
    pred_class = predictions[i].item()
    confidence = probabilities[i, pred_class].item()
    print(f"Point ({point[0]:.2f}, {point[1]:.2f}) → Class {pred_class} ({confidence:.2%})")

# Decision boundary: create the grid in the same original feature space as
# the plotted points, then apply the training-fitted scaler before inference.
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 100),
    np.linspace(y_min, y_max, 100),
)
grid_points = np.c_[xx.ravel(), yy.ravel()]
grid_tensor = torch.tensor(scaler.transform(grid_points), dtype=torch.float32, device=device)

with torch.no_grad():
    grid_predictions = model(grid_tensor).argmax(dim=1).cpu().numpy().reshape(xx.shape)

# Plot original-coordinate data. Keep the raw coordinates separate from the
# standardized tensors used by the network so the axes remain interpretable.
X_train_raw, X_temp_raw, y_train_raw, y_temp_raw = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
X_val_raw, X_test_raw, y_val_raw, y_test_raw = train_test_split(
    X_temp_raw, y_temp_raw, test_size=0.50, random_state=42, stratify=y_temp_raw
)

plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, grid_predictions, alpha=0.3, cmap="coolwarm")
plt.scatter(X_train_raw[:, 0], X_train_raw[:, 1], c=y_train_raw, cmap="coolwarm", edgecolors="k", s=20, label="Training data")
plt.scatter(X_val_raw[:, 0], X_val_raw[:, 1], c=y_val_raw, cmap="coolwarm", edgecolors="k", s=35, marker="^", label="Validation data")
plt.scatter(X_test_raw[:, 0], X_test_raw[:, 1], c=y_test_raw, cmap="coolwarm", edgecolors="k", s=40, marker="x", label="Test data")
plt.xlabel("Feature 1 (original scale)")
plt.ylabel("Feature 2 (original scale)")
plt.title("Neural Network Decision Boundary")
plt.legend()
plt.colorbar(label="Predicted Class")
plt.tight_layout()
plt.savefig("neural_network_decision_boundary.png", dpi=100)
print("Decision boundary plot saved to neural_network_decision_boundary.png")

save_path = "neural_network_model.pth"
torch.save(model.state_dict(), save_path)
print(f"Model saved to {save_path}")

print("=" * 70)
print("PROJECT COMPLETE")
print("=" * 70)
print(f"Best validation loss: {best_val_loss:.4f}")
print(f"Final test accuracy: {test_accuracy:.2f}%")
print("The test set was used only for final evaluation.")
