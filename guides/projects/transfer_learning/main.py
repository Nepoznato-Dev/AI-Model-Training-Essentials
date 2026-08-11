"""Transfer learning example: ResNet18 feature extraction on CIFAR-10.

Educational example. This version keeps a held-out validation set, avoids test-set
model selection, reports the actual trainable parameter count, and separates
feature extraction from evaluation mode correctly.
"""

import random
import time

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, models, transforms

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

weights = models.ResNet18_Weights.DEFAULT
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

print("Loading CIFAR-10...")
full_trainset = datasets.CIFAR10("./data", train=True, download=True, transform=transform)
testset = datasets.CIFAR10("./data", train=False, download=True, transform=transform)

# Never tune hyperparameters on the test set. Keep it untouched until final evaluation.
train_size = int(0.9 * len(full_trainset))
val_size = len(full_trainset) - train_size
split_generator = torch.Generator().manual_seed(SEED)
trainset, valset = random_split(full_trainset, [train_size, val_size], generator=split_generator)

trainloader = DataLoader(trainset, batch_size=32, shuffle=True)
valloader = DataLoader(valset, batch_size=32, shuffle=False)
testloader = DataLoader(testset, batch_size=32, shuffle=False)

classes = ("plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")
print(f"Train: {len(trainset):,} | Validation: {len(valset):,} | Test: {len(testset):,}")

print("Loading pretrained ResNet18...")
model = models.resnet18(weights=weights)
for param in model.parameters():
    param.requires_grad = False

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, len(classes))
model = model.to(device)

trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
frozen = sum(p.numel() for p in model.parameters() if not p.requires_grad)
print(f"Trainable parameters: {trainable:,}")
print(f"Frozen parameters: {frozen:,}")
print("Note: the new ResNet18 classification head has 5,130 trainable parameters (512*10 + 10).")

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=1e-3)


def run_epoch(loader, training=False):
    # The backbone is frozen, including BatchNorm running statistics. Only the
    # new classification head should enter training mode in feature-extraction mode.
    model.eval()
    if training:
        model.fc.train()

    total_loss = 0.0
    correct = 0
    total = 0
    context = torch.enable_grad() if training else torch.inference_mode()

    with context:
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            if training:
                optimizer.zero_grad(set_to_none=True)

            outputs = model(images)
            loss = criterion(outputs, labels)

            if training:
                loss.backward()
                optimizer.step()

            total_loss += loss.item() * labels.size(0)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
            total += labels.size(0)

    return total_loss / total, correct / total


num_epochs = 5
best_val_accuracy = -1.0
best_state = None
start = time.perf_counter()

for epoch in range(num_epochs):
    train_loss, train_accuracy = run_epoch(trainloader, training=True)
    val_loss, val_accuracy = run_epoch(valloader, training=False)

    if val_accuracy > best_val_accuracy:
        best_val_accuracy = val_accuracy
        best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}

    print(
        f"Epoch {epoch + 1}/{num_epochs} | "
        f"train loss={train_loss:.4f} acc={train_accuracy:.2%} | "
        f"val loss={val_loss:.4f} acc={val_accuracy:.2%}"
    )

assert best_state is not None
model.load_state_dict(best_state)
model = model.to(device)
test_loss, test_accuracy = run_epoch(testloader, training=False)

print(f"Training time: {time.perf_counter() - start:.1f}s")
print(f"Best validation accuracy: {best_val_accuracy:.2%}")
print(f"Final test accuracy: {test_accuracy:.2%}")

model.eval()
class_correct = [0] * len(classes)
class_total = [0] * len(classes)
with torch.inference_mode():
    for images, labels in testloader:
        outputs = model(images.to(device))
        predicted = outputs.argmax(dim=1).cpu()
        for label, pred in zip(labels, predicted):
            class_total[label.item()] += 1
            class_correct[label.item()] += int(pred.item() == label.item())

for index, class_name in enumerate(classes):
    if class_total[index]:
        print(f"{class_name:>6}: {class_correct[index] / class_total[index]:.2%}")

save_path = "transfer_learning_model.pth"
torch.save(
    {
        "model_state_dict": model.state_dict(),
        "num_classes": len(classes),
        "class_names": classes,
        "architecture": "resnet18",
        "pretrained_weights": "ResNet18_Weights.DEFAULT",
    },
    save_path,
)
print(f"Saved model to {save_path}")

print(
    "\nFeature extraction is only one transfer-learning strategy. "
    "For fine-tuning, unfreeze selected backbone layers, use a smaller learning "
    "rate for pretrained layers, and continue to use validation data for model selection."
)
