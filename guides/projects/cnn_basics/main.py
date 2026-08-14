# CNN Basics - Main Script
# A minimal, heavily-commented introduction to Convolutional Neural Networks
# Lines of code: ~250 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import time

print("=" * 70)
print("CNN BASICS PROJECT - Image Classification with PyTorch")
print("=" * 70)
print()

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("⚠️  Warning: Training on CPU will be slow. Consider using Google Colab with GPU!")
print()

# ============================================================================
# STEP 2: DEFINE THE CNN ARCHITECTURE
# ============================================================================

class SimpleCNN(nn.Module):
    """
    A simple Convolutional Neural Network for image classification.
    
    Architecture:
    - 2 Convolutional layers with ReLU activation and MaxPooling
    - 2 Fully Connected layers for classification
    
    Input: 3-channel RGB images (32x32)
    Output: 10 class probabilities (for CIFAR-10)
    """
    
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        # First convolutional layer
        # Input: 3 channels (RGB), Output: 32 feature maps
        # Kernel size: 3x3, Padding: 1 (keeps spatial dimensions)
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        
        # Second convolutional layer
        # Input: 32 channels, Output: 64 feature maps
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        
        # Max pooling layer
        # Reduces spatial dimensions by half (2x2 window)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully connected layers
        # After 2 pooling operations: 32x32 -> 16x16 -> 8x8
        # So input to FC layer is: 64 channels * 8 * 8 = 4096
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 10)  # 10 classes for CIFAR-10
        
        # Activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        """
        Forward pass through the network.
        
        Args:
            x: Input tensor of shape (batch_size, 3, 32, 32)
        
        Returns:
            Output logits of shape (batch_size, 10)
        """
        # First conv block: Conv -> ReLU -> Pool
        x = self.conv1(x)      # (batch, 32, 32, 32)
        x = self.relu(x)       # Apply ReLU activation
        x = self.pool(x)       # (batch, 32, 16, 16)
        
        # Second conv block: Conv -> ReLU -> Pool
        x = self.conv2(x)      # (batch, 64, 16, 16)
        x = self.relu(x)
        x = self.pool(x)       # (batch, 64, 8, 8)
        
        # Flatten the tensor for fully connected layers
        x = x.view(-1, 64 * 8 * 8)  # (batch, 4096)
        
        # Fully connected layers
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)  # Output logits (no softmax here, included in loss function)
        
        return x

# Initialize the model
model = SimpleCNN().to(device)
print("✓ CNN Model created successfully!")
print(f"  Model architecture: SimpleCNN")
print(f"  Parameters: {sum(p.numel() for p in model.parameters()):,}")
print()

# ============================================================================
# STEP 3: LOAD AND PREPROCESS DATA
# ============================================================================

print("Loading CIFAR-10 dataset...")
print("(First run will download the dataset, this may take a minute)")
print()

# Define image transformations
# - Resize to 32x32 (CIFAR-10 is already 32x32, but good practice)
# - Convert to tensor (scales pixel values to [0, 1])
# - Normalize to have mean=0, std=1 (helps training)
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Load training dataset
trainset = datasets.CIFAR10(
    root='./data', 
    train=True, 
    download=True, 
    transform=transform
)
trainloader = DataLoader(trainset, batch_size=64, shuffle=True)

# Load test dataset
testset = datasets.CIFAR10(
    root='./data', 
    train=False, 
    download=True, 
    transform=transform
)
testloader = DataLoader(testset, batch_size=64, shuffle=False)

# CIFAR-10 class names
classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

print(f"✓ Dataset loaded successfully!")
print(f"  Training samples: {len(trainset):,}")
print(f"  Test samples: {len(testset):,}")
print(f"  Classes: {classes}")
print(f"  Batch size: 64")
print(f"  Batches per epoch: {len(trainloader)}")
print()

# ============================================================================
# STEP 4: DEFINE LOSS FUNCTION AND OPTIMIZER
# ============================================================================

# Cross-Entropy Loss for multi-class classification
# Combines LogSoftmax and NLLLoss in one
criterion = nn.CrossEntropyLoss()

# Adam optimizer - adaptive learning rate method
# lr=0.001 is a good starting point
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("✓ Loss function and optimizer initialized!")
print(f"  Loss: CrossEntropyLoss")
print(f"  Optimizer: Adam (lr=0.001)")
print()

# ============================================================================
# STEP 5: TRAINING LOOP
# ============================================================================

num_epochs = 10
print(f"Starting training for {num_epochs} epochs...")
print("-" * 70)

start_time = time.time()

for epoch in range(num_epochs):
    epoch_start = time.time()
    
    # Set model to training mode
    model.train()
    
    running_loss = 0.0
    correct = 0
    total = 0
    
    # Iterate over training batches
    for i, (images, labels) in enumerate(trainloader):
        # Move data to device (GPU/CPU)
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        optimizer.zero_grad()  # Clear previous gradients
        loss.backward()        # Compute gradients
        optimizer.step()       # Update weights
        
        # Track statistics
        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    # Calculate epoch statistics
    epoch_loss = running_loss / len(trainloader)
    epoch_acc = 100 * correct / total
    epoch_time = time.time() - epoch_start
    
    print(f"Epoch [{epoch+1}/{num_epochs}] | "
          f"Loss: {epoch_loss:.4f} | "
          f"Accuracy: {epoch_acc:.2f}% | "
          f"Time: {epoch_time:.1f}s")

total_training_time = time.time() - start_time
print("-" * 70)
print(f"✓ Training completed in {total_training_time:.1f}s ({total_training_time/60:.1f} minutes)")
print()

# ============================================================================
# STEP 6: EVALUATE ON TEST SET
# ============================================================================

print("Evaluating on test set...")
print("-" * 70)

# Set model to evaluation mode
model.eval()

correct = 0
total = 0
class_correct = [0] * 10
class_total = [0] * 10

with torch.no_grad():  # No gradient computation needed for evaluation
    for images, labels in testloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
        # Per-class accuracy
        for i in range(labels.size(0)):
            label = labels[i]
            class_correct[label] += (predicted[i] == label).item()
            class_total[label] += 1

# Overall accuracy
test_accuracy = 100 * correct / total
print(f"Overall Test Accuracy: {test_accuracy:.2f}% ({correct}/{total})")
print()

# Per-class accuracy
print("Per-class accuracy:")
for i, class_name in enumerate(classes):
    if class_total[i] > 0:
        acc = 100 * class_correct[i] / class_total[i]
        print(f"  {class_name:10}: {acc:5.2f}%")

print("-" * 70)
print()

# ============================================================================
# STEP 7: MAKE PREDICTIONS ON SAMPLE IMAGES
# ============================================================================

print("Making predictions on sample test images...")
print("-" * 70)

# Get a batch of test images
images, labels = next(iter(testloader))
images, labels = images.to(device), labels.to(device)

# Make predictions
model.eval()
with torch.no_grad():
    outputs = model(images[:8])  # First 8 images
    _, predicted = torch.max(outputs, 1)

# Display predictions
for i in range(8):
    true_label = classes[labels[i]]
    pred_label = classes[predicted[i]]
    match = "✓" if true_label == pred_label else "✗"
    print(f"{match} Image {i+1}: True={true_label:6}, Predicted={pred_label:6}")

print()

# ============================================================================
# STEP 8: SAVE THE MODEL (OPTIONAL)
# ============================================================================

save_path = "cnn_cifar10.pth"
torch.save(model.state_dict(), save_path)
print(f"✓ Model saved to '{save_path}'")
print()

# To load the model later:
# model = SimpleCNN()
# model.load_state_dict(torch.load("cnn_cifar10.pth", weights_only=True))
# model.eval()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the CNN Basics Project!")
print("=" * 70)
print(f"""
What you learned:
✓ How to build a CNN architecture in PyTorch
✓ How convolutional and pooling layers work
✓ How to load and preprocess image data
✓ How to train a neural network with batches
✓ How to evaluate model performance
✓ How to make predictions with trained models

Results Summary:
- Training time: {total_training_time:.1f}s
- Final test accuracy: {test_accuracy:.2f}%
- Model saved: {save_path}

Next steps:
1. Read the full CNNs Guide in /guides/CNNs/
2. Try modifying the architecture (more layers, different filters)
3. Experiment with hyperparameters (learning rate, batch size)
4. Learn about advanced architectures (ResNet, VGG, EfficientNet)
5. Try transfer learning with pre-trained models

Resources:
- PyTorch Documentation: https://pytorch.org/docs/
- CS231n Course: http://cs231n.stanford.edu/
- Papers With Code: https://paperswithcode.com/
""")
print("=" * 70)
