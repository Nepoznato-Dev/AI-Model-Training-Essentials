# Image Classification with ResNet
# Build a ResNet from scratch and use it for CIFAR-10 image classification
# Lines of code: ~300 (including comments)

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
print("IMAGE CLASSIFICATION WITH RESNET - PyTorch")
print("=" * 70)
print()

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("Warning: Training on CPU will be slow. Consider using Google Colab with GPU!")
print()

# ============================================================================
# STEP 2: UNDERSTAND THE RESIDUAL BLOCK
# ============================================================================
#
# Standard CNN layers just do:  x -> Conv -> BN -> ReLU -> output
#
# ResNet adds a "skip connection" (shortcut):
#
#   Input (x) ──────────────────────────> (+) -> ReLU -> Output
#      │                                    ↑
#      ├──> Conv -> BN -> ReLU -> Conv -> BN
#
# Why? When layers get deeper, they can struggle to learn identity mappings
# (i.e., "just pass the information through"). The skip connection lets
# gradients flow directly through the network, solving the vanishing
# gradient problem and allowing very deep networks to train effectively.
#
# ============================================================================

class ResidualBlock(nn.Module):
    """
    A single residual block (the building block of ResNet).
    
    Architecture:
        Conv -> BatchNorm -> ReLU -> Conv -> BatchNorm
        + skip connection (identity shortcut)
        -> ReLU activation
    
    If input and output dimensions don't match (e.g., when changing from
    32 to 64 filters), we use a 1x1 convolution to project the input
    to the correct shape.
    """
    
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        
        # First convolutional layer
        self.conv1 = nn.Conv2d(
            in_channels, out_channels, 
            kernel_size=3, stride=stride, padding=1, bias=False
        )
        self.bn1 = nn.BatchNorm2d(out_channels)
        
        # Second convolutional layer
        self.conv2 = nn.Conv2d(
            out_channels, out_channels, 
            kernel_size=3, stride=1, padding=1, bias=False
        )
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        self.relu = nn.ReLU()
        
        # Skip connection (identity shortcut)
        # If dimensions change, we need a projection shortcut
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )
    
    def forward(self, x):
        """
        Forward pass through the residual block.
        
        Args:
            x: Input tensor
        
        Returns:
            Output = ReLU(Conv2(BN2(Conv1(BN1(x)))) + shortcut(x))
        """
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        
        # Add the skip connection
        out = out + self.shortcut(x)
        out = self.relu(out)
        
        return out

# ============================================================================
# STEP 3: BUILD THE FULL RESNET ARCHITECTURE
# ============================================================================
#
# Our mini-ResNet for CIFAR-10:
#   - Initial conv layer (no pooling, since CIFAR-10 images are small 32x32)
#   - 4 groups of residual blocks (6, 6, 6, 6 blocks)
#   - Global average pooling
#   - Fully connected classifier
#
# This gives us a network with ~1.7M parameters — much smaller than the
# original ResNet-50 (25M params), but follows the same architecture.
# ============================================================================

class MiniResNet(nn.Module):
    """
    A compact ResNet for CIFAR-10 classification.
    
    Architecture overview:
        Input (3x32x32)
        -> Conv (3->64) + BN + ReLU
        -> 6 residual blocks (64 filters)
        -> 6 residual blocks (128 filters, stride=2)  [downsample]
        -> 6 residual blocks (256 filters, stride=2)  [downsample]
        -> 6 residual blocks (512 filters, stride=2)  [downsample]
        -> Global Average Pooling
        -> FC (512 -> 10)
    """
    
    def __init__(self):
        super(MiniResNet, self).__init__()
        
        # Initial convolutional layer (no pooling for small images)
        self.initial = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        
        # Group 1: 6 blocks, 64 filters (no downsampling)
        self.group1 = self._make_group(64, 64, num_blocks=6, stride=1)
        
        # Group 2: 6 blocks, 128 filters (downsample 32x32 -> 16x16)
        self.group2 = self._make_group(64, 128, num_blocks=6, stride=2)
        
        # Group 3: 6 blocks, 256 filters (downsample 16x16 -> 8x8)
        self.group3 = self._make_group(128, 256, num_blocks=6, stride=2)
        
        # Group 4: 6 blocks, 512 filters (downsample 8x8 -> 4x4)
        self.group4 = self._make_group(256, 512, num_blocks=6, stride=2)
        
        # Classifier: global average pooling + fully connected layer
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))  # Output: (batch, 512, 1, 1)
        self.fc = nn.Linear(512, 10)  # 10 classes for CIFAR-10
    
    def _make_group(self, in_channels, out_channels, num_blocks, stride):
        """
        Create a group of residual blocks.
        
        The first block may downsample (stride=2), the rest use stride=1.
        """
        layers = []
        
        # First block: may change dimensions
        layers.append(ResidualBlock(in_channels, out_channels, stride))
        
        # Remaining blocks: same dimensions
        for _ in range(1, num_blocks):
            layers.append(ResidualBlock(out_channels, out_channels, stride=1))
        
        return nn.Sequential(*layers)
    
    def forward(self, x):
        """
        Forward pass through the full ResNet.
        
        Args:
            x: Input tensor of shape (batch_size, 3, 32, 32)
        
        Returns:
            Output logits of shape (batch_size, 10)
        """
        out = self.initial(x)       # (batch, 64, 32, 32)
        out = self.group1(out)      # (batch, 64, 32, 32)
        out = self.group2(out)      # (batch, 128, 16, 16)
        out = self.group3(out)      # (batch, 256, 8, 8)
        out = self.group4(out)      # (batch, 512, 4, 4)
        out = self.avg_pool(out)    # (batch, 512, 1, 1)
        out = out.view(out.size(0), -1)  # (batch, 512)
        out = self.fc(out)          # (batch, 10)
        return out

# Initialize the model
model = MiniResNet().to(device)
print("ResNet Model created successfully!")
print(f"  Architecture: MiniResNet (24 residual blocks)")
print(f"  Parameters: {sum(p.numel() for p in model.parameters()):,}")
print()

# ============================================================================
# STEP 4: LOAD AND PREPROCESS DATA
# ============================================================================

print("Loading CIFAR-10 dataset...")
print("(First run will download the dataset, this may take a minute)")
print()

# Data augmentation for training:
# - RandomCrop: randomly crops the image (helps generalization)
# - RandomHorizontalFlip: flips images horizontally with 50% probability
# - Normalize: standardizes pixel values (helps training stability)
#
# For testing, we only normalize (no augmentation — we want consistent evaluation)
train_transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

# Load datasets
trainset = datasets.CIFAR10(
    root='./data', train=True, download=True, transform=train_transform
)
trainloader = DataLoader(trainset, batch_size=128, shuffle=True, num_workers=2)

testset = datasets.CIFAR10(
    root='./data', train=False, download=True, transform=test_transform
)
testloader = DataLoader(testset, batch_size=128, shuffle=False, num_workers=2)

# CIFAR-10 class names
classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

print(f"Dataset loaded successfully!")
print(f"  Training samples: {len(trainset):,}")
print(f"  Test samples: {len(testset):,}")
print(f"  Batch size: 128")
print()

# ============================================================================
# STEP 5: DEFINE LOSS FUNCTION AND OPTIMIZER
# ============================================================================

# Cross-Entropy Loss (combines softmax + negative log likelihood)
criterion = nn.CrossEntropyLoss()

# Adam optimizer with weight decay (L2 regularization)
# Weight decay helps prevent overfitting
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)

# Learning rate scheduler: reduces LR when training plateaus
# This helps the model fine-tune weights in later epochs
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', factor=0.5, patience=3, verbose=True
)

print("Training components initialized:")
print(f"  Loss: CrossEntropyLoss")
print(f"  Optimizer: Adam (lr=0.001, weight_decay=1e-4)")
print(f"  Scheduler: ReduceLROnPlateau (factor=0.5, patience=3)")
print()

# ============================================================================
# STEP 6: TRAINING LOOP
# ============================================================================

num_epochs = 20
best_acc = 0.0
print(f"Starting training for {num_epochs} epochs...")
print("-" * 70)

start_time = time.time()

for epoch in range(num_epochs):
    epoch_start = time.time()
    model.train()
    
    running_loss = 0.0
    correct = 0
    total = 0
    
    for batch_idx, (images, labels) in enumerate(trainloader):
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Track statistics
        running_loss += loss.item()
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    # Epoch statistics
    epoch_loss = running_loss / len(trainloader)
    epoch_acc = 100 * correct / total
    epoch_time = time.time() - epoch_start
    
    # Update learning rate scheduler
    scheduler.step(epoch_loss)
    
    print(f"Epoch [{epoch+1:2d}/{num_epochs}] | "
          f"Loss: {epoch_loss:.4f} | "
          f"Train Acc: {epoch_acc:.2f}% | "
          f"Time: {epoch_time:.1f}s")

total_training_time = time.time() - start_time
print("-" * 70)
print(f"Training completed in {total_training_time:.1f}s ({total_training_time/60:.1f} minutes)")
print()

# ============================================================================
# STEP 7: EVALUATE ON TEST SET
# ============================================================================

print("Evaluating on test set...")
print("-" * 70)

model.eval()
correct = 0
total = 0
class_correct = [0] * 10
class_total = [0] * 10

with torch.no_grad():
    for images, labels in testloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
        for i in range(labels.size(0)):
            label = labels[i]
            class_correct[label] += (predicted[i] == label).item()
            class_total[label] += 1

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
# STEP 8: SAVE THE MODEL
# ============================================================================

save_path = "resnet_cifar10.pth"
torch.save({
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'test_accuracy': test_accuracy,
}, save_path)
print(f"Model checkpoint saved to '{save_path}'")
print()

# To load and use the model later:
# checkpoint = torch.load("resnet_cifar10.pth", weights_only=True)
# model = MiniResNet()
# model.load_state_dict(checkpoint['model_state_dict'])
# model.eval()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the ResNet Image Classification Project!")
print("=" * 70)
print(f"""
What you learned:
- Residual blocks and skip connections (why deeper networks need shortcuts)
- Building a modular ResNet architecture from scratch
- Data augmentation techniques for better generalization
- Learning rate scheduling (ReduceLROnPlateau)
- Training and evaluating a deep residual network

Results Summary:
- Training time: {total_training_time:.1f}s
- Final test accuracy: {test_accuracy:.2f}%
- Model saved: {save_path}

Next steps:
1. Read Chapter 2 of the CNNs Guide: Advanced Architectures
2. Try increasing the number of blocks (deeper network)
3. Experiment with different datasets (e.g., CIFAR-100, STL-10)
4. Compare with torchvision's built-in ResNet18
5. Try transfer learning: fine-tune a pre-trained ResNet on your own images

Resources:
- Original ResNet Paper: https://arxiv.org/abs/1512.03385
- PyTorch Documentation: https://pytorch.org/docs/
""")
print("=" * 70)
