# Chapter 1: CNN Fundamentals and Architecture

## 1.1 Introduction to Convolutional Neural Networks

Convolutional Neural Networks (CNNs) are the backbone of modern computer vision. They excel at processing grid-like data such as images by leveraging spatial hierarchies and local connectivity patterns.

### Key Advantages
- **Parameter Sharing**: Same filter applied across entire image
- **Local Connectivity**: Neurons connect only to local regions
- **Translation Invariance**: Detect features regardless of position
- **Hierarchical Features**: Learn from edges to complex objects

## 1.2 Core Operations

### Convolution Operation

```python
import torch
import torch.nn as nn

class Convolution2D(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        # Initialize weights
        self.weight = nn.Parameter(torch.randn(
            out_channels, in_channels, kernel_size, kernel_size
        ))
        self.bias = nn.Parameter(torch.zeros(out_channels))
    
    def forward(self, x):
        # Add padding
        if self.padding > 0:
            x = nn.functional.pad(x, (self.padding,) * 4)
        
        # Perform convolution
        output = nn.functional.conv2d(x, self.weight, self.bias, stride=self.stride)
        return output
```

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
