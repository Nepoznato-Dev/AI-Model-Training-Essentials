# Transfer Learning - Main Script
# A minimal, heavily-commented introduction to using pre-trained models
# Lines of code: ~200 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import time

print("=" * 70)
print("TRANSFER LEARNING PROJECT - Using Pre-trained Models")
print("=" * 70)
print()

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("Note: Training on CPU will be slow. GPU highly recommended!")
print()

# ============================================================================
# STEP 2: LOAD A PRE-TRAINED MODEL
# ============================================================================

# Transfer learning: Use a model that was already trained on a large dataset
# We'll use ResNet18, which was trained on ImageNet (1.2 million images, 1000 classes)
# Instead of training from scratch, we'll adapt it to our task

print("Loading pre-trained ResNet18 model...")
print("(First run will download the model weights)")
print()

# Load pre-trained ResNet18
# weights='DEFAULT' loads the best available weights
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

print("✓ Pre-trained model loaded!")
print(f"  Model: ResNet18")
print(f"  Original parameters: {sum(p.numel() for p in model.parameters()):,}")
print(f"  Trained on: ImageNet (1000 classes)")
print()

# ============================================================================
# STEP 3: MODIFY THE MODEL FOR OUR TASK
# ============================================================================

# ResNet18 was trained to classify 1000 classes
# We want to classify 10 classes (CIFAR-10)
# So we need to replace the final layer

print("Modifying model for CIFAR-10 (10 classes)...")

# Freeze all layers (we won't train them)
# This is called "feature extraction" mode
for param in model.parameters():
    param.requires_grad = False

# IMPORTANT: Also set BatchNorm layers to eval mode so their running
# statistics stay consistent with the frozen weights
for module in model.modules():
    if isinstance(module, nn.BatchNorm2d):
        module.eval()

# Replace the final fully connected layer
# model.fc is the classification head
# Input: 512 features (from ResNet18)
# Output: 10 classes (for CIFAR-10)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)

# Move model to device (GPU/CPU)
model = model.to(device)

print("✓ Model modified!")
print(f"  Trainable parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")
print(f"  Frozen parameters: {sum(p.numel() for p in model.parameters() if not p.requires_grad):,}")
print()

# ============================================================================
# STEP 4: LOAD AND PREPROCESS DATA
# ============================================================================

print("Loading CIFAR-10 dataset...")
print("(First run will download the dataset)")
print()

# Define transformations
# IMPORTANT: Pre-trained models expect specific input formats
# ResNet expects: 224x224 images, normalized with ImageNet mean/std
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to 224x224 (required by ResNet)
    transforms.ToTensor(),          # Convert to tensor and scale to [0, 1]
    # Normalize with ImageNet statistics
    # Mean and std for each channel (RGB)
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# Load training dataset
trainset = datasets.CIFAR10(
    root='./data',
    train=True,
    download=True,
    transform=transform
)
trainloader = DataLoader(trainset, batch_size=32, shuffle=True)

# Load test dataset
testset = datasets.CIFAR10(
    root='./data',
    train=False,
    download=True,
    transform=transform
)
testloader = DataLoader(testset, batch_size=32, shuffle=False)

# CIFAR-10 class names
classes = ('plane', 'car', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck')

print(f"✓ Dataset loaded!")
print(f"  Training samples: {len(trainset):,}")
print(f"  Test samples: {len(testset):,}")
print(f"  Image size: 224x224 (resized from 32x32)")
print(f"  Batch size: 32")
print()

# ============================================================================
# STEP 5: DEFINE LOSS FUNCTION AND OPTIMIZER
# ============================================================================

# Only optimize the parameters we want to train (the final layer)
# We use list comprehension to filter only trainable parameters
optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=0.001
)

# Loss function for multi-class classification
criterion = nn.CrossEntropyLoss()

print("✓ Loss function and optimizer initialized!")
print(f"  Loss: CrossEntropyLoss")
print(f"  Optimizer: Adam (lr=0.001)")
print(f"  Only training the final layer (feature extraction mode)")
print()

# ============================================================================
# STEP 6: TRAINING LOOP
# ============================================================================

num_epochs = 5  # Few epochs needed since we're using pre-trained features
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
        # Move data to device
        images, labels = images.to(device), labels.to(device)
        
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
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
print(f"✓ Training completed in {total_training_time:.1f}s")
print()

# ============================================================================
# STEP 7: EVALUATE ON TEST SET
# ============================================================================

print("Evaluating on test set...")
print("-" * 70)

# Set model to evaluation mode
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
# STEP 8: COMPARE WITH TRAINING FROM SCRATCH
# ============================================================================

print("-" * 70)
print("TRANSFER LEARNING vs TRAINING FROM SCRATCH")
print("-" * 70)

print("""
With Transfer Learning (what we just did):
✓ Training time: typically a few minutes (5 epochs, varies by hardware)
✓ Test accuracy: often reaches ~85-90% on CIFAR-10 (hardware/dataset dependent)
✓ Only trained: Final layer (5,130 parameters)
✓ Used: Pre-trained features from ImageNet

Training from Scratch (for comparison):
✗ Training time: significantly longer (20+ epochs, depends on hardware)
✗ Test accuracy: often lower with limited data (highly variable)
✗ Trained: All parameters (~11 million)
✗ Used: Random initialization

Benefits of Transfer Learning:
1. Faster training (fewer epochs needed)
2. Better accuracy when data is limited (pre-trained features are powerful)
3. Works well with small datasets
4. Less computational resources needed

NOTE: Actual numbers depend on your hardware, PyTorch version, and
random seed. These are typical ranges, not guarantees.
""")

# ============================================================================
# STEP 9: MAKE PREDICTIONS ON SAMPLE IMAGES
# ============================================================================

print("Making predictions on sample test images...")
print("-" * 70)

# Get a batch of test images
images, labels = next(iter(testloader))
images, labels = images.to(device), labels.to(device)

# Make predictions
model.eval()
with torch.no_grad():
    outputs = model(images[:8])
    probabilities = torch.softmax(outputs, dim=1)
    _, predicted = torch.max(outputs, 1)

# Display predictions with confidence
for i in range(8):
    true_label = classes[labels[i]]
    pred_label = classes[predicted[i]]
    confidence = probabilities[i][predicted[i]].item()
    match = "✓" if true_label == pred_label else "✗"
    print(f"{match} Image {i+1}: True={true_label:6}, "
          f"Predicted={pred_label:6} ({confidence:.2%})")

print()

# ============================================================================
# STEP 10: SAVE THE MODEL
# ============================================================================

save_path = "transfer_learning_model.pth"
torch.save(model.state_dict(), save_path)
print(f"✓ Model saved to '{save_path}'")
print()

# To load the model later:
# model = models.resnet18(weights=None)
# model.fc = nn.Linear(512, 10)  # Must match the modified architecture
# model.load_state_dict(torch.load("transfer_learning_model.pth", weights_only=True))
# model.eval()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the Transfer Learning Project!")
print("=" * 70)
print(f"""
What you learned:
✓ How to load a pre-trained model (ResNet18)
✓ How to modify a model for a new task
✓ The difference between feature extraction and fine-tuning
✓ How to freeze layers and train only specific parts
✓ Why transfer learning is faster and more accurate
✓ How to evaluate model performance

Key Concepts:
- Transfer Learning: Using knowledge from one task for another
- Pre-trained Models: Models trained on large datasets (ImageNet)
- Feature Extraction: Using pre-trained features, only training final layer
- Fine-tuning: Updating all or some pre-trained weights
- ImageNet: 1.2M images, 1000 classes (standard benchmark)

Results Summary:
- Training time: {total_training_time:.1f}s
- Test accuracy: {test_accuracy:.2f}%
- Trainable parameters: Only final layer
- Speedup: ~5-10x vs training from scratch

Next steps:
1. Try fine-tuning more layers (unfreeze some layers)
2. Experiment with different pre-trained models (ResNet50, VGG, EfficientNet)
3. Use your own dataset (custom images)
4. Learn about domain-specific pre-trained models
5. Explore other computer vision tasks (object detection, segmentation)

Resources:
- PyTorch Transfer Learning Tutorial: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
- Model Zoo: https://pytorch.org/vision/stable/models.html
- Papers With Code: https://paperswithcode.com/
""")
print("=" * 70)
