# Chapter 1: CNN Fundamentals and Architecture

## 🎯 Welcome to Your First CNN!

**Don't worry if you're new to this!** We'll walk through everything step-by-step, starting from the basics. By the end of this chapter, you'll understand how CNNs work and build your first one from scratch.

### What You'll Learn
- What CNNs are and why they're perfect for images
- How convolution operations detect features (with visual examples!)
- Building blocks like pooling and batch normalization
- Your first working CNN implementation in PyTorch
- Common mistakes and how to avoid them

**Time Estimate:** 2-3 hours  
**Prerequisites:** Basic Python knowledge (we'll explain everything else!)

---

## 1.1 What is a CNN? (Simple Explanation)

Imagine you're looking at a photo of a cat. How do you know it's a cat?

You probably don't look at every single pixel individually. Instead, you notice:
1. **Edges** - The outline of ears, whiskers, tail
2. **Shapes** - Round eyes, triangular ears
3. **Patterns** - Fur texture, color combinations
4. **Complete object** - "That's a cat!"

**CNNs work the same way!** They start by detecting simple features (edges), then combine them into complex features (shapes), and finally recognize complete objects.

### Why Not Use Regular Neural Networks?

Great question! Let's compare:

| **Regular Neural Network** | **Convolutional Neural Network (CNN)** |
|---------------------------|----------------------------------------|
| Treats image as flat list of pixels | Understands 2D structure of images |
| Millions of parameters (slow!) | Shares parameters (efficient!) |
| Doesn't care where features are | Detects features anywhere in image |
| Poor at image recognition | Excellent at image recognition |

### Real-World Example

Think about how Instagram automatically tags your friends in photos:
1. CNN detects faces in the image
2. CNN extracts facial features (eyes, nose, mouth positions)
3. CNN compares to known faces
4. CNN suggests: "This is Alice!"

All of this happens because CNNs are specially designed for **grid-like data** (images, videos, even some audio).

---

## 1.2 Core Concepts Explained Simply

### The Convolution Operation (The Magic Behind CNNs)

**What is convolution?** Don't let the fancy name scare you! It's just a way to scan an image with a small "window" to detect features.

#### Visual Analogy: Using a Flashlight in the Dark

Imagine you're in a dark room with a flashlight that only lights up a 3x3 square area. You slowly move the flashlight across the entire room, noting what you see in each spot.

**In CNNs:**
- The **flashlight** = Filter (or kernel)
- The **room** = Input image
- **Moving the flashlight** = Sliding window operation
- **What you note** = Feature detection (edges, textures, etc.)

```python
import torch
import torch.nn as nn

# Now let's implement this step-by-step!

class Convolution2D(nn.Module):
    """
    A simple 2D convolution layer built from scratch.
    
    Don't worry about understanding every line yet - we'll explain each part!
    """
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        # Initialize weights - think of these as the "flashlight pattern"
        # We use random values initially, then learn better patterns during training
        self.weight = nn.Parameter(torch.randn(
            out_channels, in_channels, kernel_size, kernel_size
        ))
        self.bias = nn.Parameter(torch.zeros(out_channels))
        
        # Quick note: 
        # - in_channels: How many "color channels" in the input (e.g., 3 for RGB)
        # - out_channels: How many different features we want to detect
        # - kernel_size: Size of our sliding window (e.g., 3x3)
    
    def forward(self, x):
        """
        This is where the magic happens!
        The convolution operation slides our filter across the image.
        """
        # Add padding if needed (like adding a border around the image)
        if self.padding > 0:
            x = nn.functional.pad(x, (self.padding,) * 4)
        
        # Perform convolution - PyTorch does the heavy lifting here
        output = nn.functional.conv2d(x, self.weight, self.bias, stride=self.stride)
        return output


# 💡 Beginner Tip: Most of the time, you'll use PyTorch's built-in nn.Conv2d
# But understanding what's underneath helps you debug and optimize!
```

#### Understanding the Parameters

Let's break down what each parameter means with a real example:

```python
# Example: You have an RGB image (3 channels) and want to detect 64 different features
conv_layer = Convolution2D(
    in_channels=3,      # RGB image has 3 color channels
    out_channels=64,    # We want to learn 64 different feature detectors
    kernel_size=3,      # Use a 3x3 sliding window
    stride=1,           # Move 1 pixel at a time
    padding=1           # Add 1-pixel border to preserve image size
)

print(f"Number of parameters: {sum(p.numel() for p in conv_layer.parameters())}")
# Output: Number of parameters: 1792
# Compare this to a fully-connected layer which would need MILLIONS!
```

### Pooling Operations (Downsampling)

**What is pooling?** After detecting features, we often want to reduce the image size while keeping the important information. Think of it like creating a thumbnail of a photo - smaller but still recognizable!

#### Visual Analogy: Summarizing a Story

Imagine you read a 10-page story and need to summarize it in 2 pages:
- **Max Pooling**: Keep only the most exciting parts (the "maximum" moments)
- **Average Pooling**: Take the average of each section (general overview)

```python
class Pooling2D(nn.Module):
    """
    Pooling reduces the spatial dimensions while preserving important features.
    
    Why use pooling?
    - Reduces computation (smaller images = faster processing)
    - Provides translation invariance (features detected regardless of exact position)
    - Helps prevent overfitting
    """
    def __init__(self, kernel_size=2, stride=2, pool_type='max'):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.pool_type = pool_type
    
    def forward(self, x):
        if self.pool_type == 'max':
            # Max pooling: take the maximum value in each window
            # Best for preserving sharp features (edges, corners)
            return nn.functional.max_pool2d(x, self.kernel_size, self.stride)
        elif self.pool_type == 'avg':
            # Average pooling: take the average value in each window
            # Smoother, good for general background information
            return nn.functional.avg_pool2d(x, self.kernel_size, self.stride)


# Example usage:
pool_layer = Pooling2D(kernel_size=2, stride=2, pool_type='max')

# Input: [batch_size=1, channels=64, height=28, width=28]
# Output: [batch_size=1, channels=64, height=14, width=14]
# Notice: Spatial dimensions halved, but channels stay the same!
```

#### When to Use Max vs Average Pooling

| **Max Pooling** | **Average Pooling** |
|-----------------|---------------------|
| Preserves sharpest features | Creates smoother representations |
| Better for texture/edge detection | Better for background context |
| Most common choice | Used in specific architectures |
| Example: Detecting cat ears | Example: Overall scene classification |

**Beginner Advice:** Start with max pooling - it works well for most cases!

### Pooling Operations

```python
class Pooling2D(nn.Module):
    def __init__(self, kernel_size=2, stride=2, pool_type='max'):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.pool_type = pool_type
    
    def forward(self, x):
        if self.pool_type == 'max':
            return nn.functional.max_pool2d(x, self.kernel_size, self.stride)
        elif self.pool_type == 'avg':
            return nn.functional.avg_pool2d(x, self.kernel_size, self.stride)
```

## 1.3 Building Blocks

### Convolution Block with BatchNorm and ReLU

```python
class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, 
                 stride=1, padding=1, use_batchnorm=True):
        super().__init__()
        
        layers = [
            nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding),
        ]
        
        if use_batchnorm:
            layers.append(nn.BatchNorm2d(out_channels))
        
        layers.append(nn.ReLU(inplace=True))
        
        self.block = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.block(x)
```

### Residual Block (ResNet)

```python
class ResidualBlock(nn.Module):
    def __init__(self, channels, stride=1, downsample=None):
        super().__init__()
        
        self.conv1 = nn.Conv2d(channels, channels, 3, stride, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(channels, channels, 3, 1, 1, bias=False)
        self.bn2 = nn.BatchNorm2d(channels)
        self.downsample = downsample
    
    def forward(self, x):
        identity = x
        
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        
        if self.downsample is not None:
            identity = self.downsample(x)
        
        out += identity
        out = self.relu(out)
        
        return out
```

## 1.4 Classic Architectures

### LeNet-5 Implementation

```python
class LeNet5(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(1, 6, 5),      # 28x28 -> 24x24
            nn.AvgPool2d(2),         # 24x24 -> 12x12
            nn.Sigmoid(),
            nn.Conv2d(6, 16, 5),     # 12x12 -> 8x8
            nn.AvgPool2d(2),         # 8x8 -> 4x4
            nn.Sigmoid(),
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(16 * 4 * 4, 120),
            nn.Sigmoid(),
            nn.Linear(120, 84),
            nn.Sigmoid(),
            nn.Linear(84, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x
```

### VGG Network

```python
class VGG(nn.Module):
    def __init__(self, cfg, num_classes=1000):
        super().__init__()
        self.features = self.make_layers(cfg)
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes),
        )
    
    def make_layers(self, cfg, batch_norm=True):
        layers = []
        in_channels = 3
        for v in cfg:
            if v == 'M':
                layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
            else:
                conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
                if batch_norm:
                    layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
                else:
                    layers += [conv2d, nn.ReLU(inplace=True)]
                in_channels = v
        return nn.Sequential(*layers)
    
    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

# VGG-16 configuration
vgg16_cfg = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']
```

## 1.5 Training Pipeline

```python
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class CNNTrainer:
    def __init__(self, model, learning_rate=0.001, weight_decay=1e-4):
        self.model = model
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=0.9,
            weight_decay=weight_decay
        )
        self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=30, gamma=0.1)
    
    def train_epoch(self, dataloader, device):
        self.model.train()
        total_loss = 0
        correct = 0
        
        for batch_idx, (data, target) in enumerate(dataloader):
            data, target = data.to(device), target.to(device)
            
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()
        
        accuracy = 100. * correct / len(dataloader.dataset)
        avg_loss = total_loss / len(dataloader)
        
        return avg_loss, accuracy
    
    @torch.no_grad()
    def evaluate(self, dataloader, device):
        self.model.eval()
        total_loss = 0
        correct = 0
        
        for data, target in dataloader:
            data, target = data.to(device), target.to(device)
            output = self.model(data)
            total_loss += self.criterion(output, target).item()
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()
        
        accuracy = 100. * correct / len(dataloader.dataset)
        avg_loss = total_loss / len(dataloader)
        
        return avg_loss, accuracy
    
    def train(self, train_loader, val_loader, epochs=100, device='cuda'):
        best_accuracy = 0
        
        for epoch in range(epochs):
            train_loss, train_acc = self.train_epoch(train_loader, device)
            val_loss, val_acc = self.evaluate(val_loader, device)
            
            print(f'Epoch {epoch+1}: Train Loss={train_loss:.4f}, Acc={train_acc:.2f}% | '
                  f'Val Loss={val_loss:.4f}, Acc={val_acc:.2f}%')
            
            if val_acc > best_accuracy:
                best_accuracy = val_acc
                torch.save(self.model.state_dict(), 'best_model.pth')
            
            self.scheduler.step()
        
        return best_accuracy
```

## 1.6 Data Augmentation

```python
def get_transforms(train=True, img_size=224):
    if train:
        return transforms.Compose([
            transforms.RandomResizedCrop(img_size),
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
    else:
        return transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(img_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
```

---

**Exercise 1.1**: Implement and train LeNet-5 on MNIST dataset.

**Exercise 1.2**: Build VGG-16 from scratch and train on CIFAR-10.

**Exercise 1.3**: Compare different pooling strategies on your validation set.
