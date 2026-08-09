# Chapter 2: Advanced CNN Architectures

## 2.1 Introduction to Modern CNN Designs

Building upon the fundamentals from Chapter 1, this chapter explores advanced CNN architectures that have pushed the boundaries of computer vision performance. We'll dive deep into ResNet, DenseNet, EfficientNet, and Vision Transformers.

### Evolution of CNN Architectures

| Architecture | Year | Key Innovation | Top-1 Error (ImageNet) |
|-------------|------|----------------|------------------------|
| AlexNet | 2012 | ReLU + Dropout | 37.5% |
| VGG-16 | 2014 | Small 3×3 kernels | 28.5% |
| GoogLeNet | 2014 | Inception modules | 21.2% |
| ResNet-50 | 2015 | Skip connections | 22.9% |
| DenseNet-121 | 2017 | Dense connectivity | 25.0% |
| EfficientNet-B7 | 2019 | Compound scaling | 20.0% |

---

## 2.2 ResNet: Deep Residual Learning

### The Vanishing Gradient Problem

As networks get deeper, gradients become smaller during backpropagation, making training difficult:

```python
# Problem: Very deep networks are hard to train
class VeryDeepNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(*[ConvBlock(64, 64) for _ in range(100)])
    
    def forward(self, x):
        # After 100 layers, gradients may vanish!
        for layer in self.layers:
            x = layer(x)
        return x
```

### Residual Learning Solution

ResNet introduces skip connections that allow gradients to flow directly through the network:

**Key Insight**: Instead of learning H(x), learn F(x) = H(x) - x

```python
import torch
import torch.nn as nn

class BasicBlock(nn.Module):
    """ResNet Basic Block for shallow networks"""
    expansion = 1
    
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, 
                               stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, 
                               padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
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
        
        # Skip connection: add input to output
        out += identity
        out = self.relu(out)
        
        return out


class BottleneckBlock(nn.Module):
    """ResNet Bottleneck Block for deeper networks (ResNet-50+)"""
    expansion = 4
    
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super().__init__()
        # 1x1 convolution: reduce dimensions
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        
        # 3x3 convolution: process
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3,
                               stride=stride, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        # 1x1 convolution: restore dimensions
        self.conv3 = nn.Conv2d(out_channels, out_channels * self.expansion,
                               kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(out_channels * self.expansion)
        
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample
        
    def forward(self, x):
        identity = x
        
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)
        
        out = self.conv3(out)
        out = self.bn3(out)
        
        if self.downsample is not None:
            identity = self.downsample(x)
        
        out += identity
        out = self.relu(out)
        
        return out
```

### Building ResNet-50

```python
class ResNet(nn.Module):
    def __init__(self, block, layers, num_classes=1000):
        super().__init__()
        self.in_channels = 64
        
        # Initial convolution
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        
        # Residual layers
        self.layer1 = self._make_layer(block, 64, layers[0], stride=1)
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        
        # Classifier
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512 * block.expansion, num_classes)
        
        # Initialize weights
        self._initialize_weights()
    
    def _make_layer(self, block, out_channels, blocks, stride):
        downsample = None
        
        if stride != 1 or self.in_channels != out_channels * block.expansion:
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channels, out_channels * block.expansion,
                         kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels * block.expansion)
            )
        
        layers = [block(self.in_channels, out_channels, stride, downsample)]
        self.in_channels = out_channels * block.expansion
        
        for _ in range(1, blocks):
            layers.append(block(self.in_channels, out_channels))
        
        return nn.Sequential(*layers)
    
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        
        return x


def resnet50(num_classes=1000):
    """Construct ResNet-50: [3, 4, 6, 3] bottleneck blocks"""
    return ResNet(BottleneckBlock, [3, 4, 6, 3], num_classes)


def resnet101(num_classes=1000):
    """Construct ResNet-101: [3, 4, 23, 3] bottleneck blocks"""
    return ResNet(BottleneckBlock, [3, 4, 23, 3], num_classes)
```

### Why ResNet Works

1. **Identity Mapping**: Skip connections preserve information flow
2. **Ensemble Effect**: Multiple paths through the network
3. **Gradient Highway**: Direct path for gradient flow
4. **Implicit Deep Supervision**: Each layer receives direct supervision signal

---

## 2.3 DenseNet: Dense Connectivity

### From Skip Connections to Dense Connections

While ResNet adds input to output, DenseNet concatenates all previous feature maps:

```python
class DenseBlock(nn.Module):
    """Dense Block with dense connectivity"""
    
    def __init__(self, num_layers, in_channels, growth_rate):
        super().__init__()
        self.layers = nn.ModuleList()
        
        for i in range(num_layers):
            layer = DenseLayer(
                in_channels + i * growth_rate,
                growth_rate
            )
            self.layers.append(layer)
    
    def forward(self, x):
        features = [x]
        
        for layer in self.layers:
            # Concatenate all previous features
            concatenated = torch.cat(features, dim=1)
            new_feature = layer(concatenated)
            features.append(new_feature)
        
        return torch.cat(features, dim=1)


class DenseLayer(nn.Module):
    """Single dense layer: BN -> ReLU -> Conv1x1 -> BN -> ReLU -> Conv3x3"""
    
    def __init__(self, in_channels, growth_rate):
        super().__init__()
        
        # Bottleneck: 1x1 convolution to reduce channels
        self.bottleneck = nn.Sequential(
            nn.BatchNorm2d(in_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels, 4 * growth_rate, kernel_size=1, bias=False)
        )
        
        # Feature extraction: 3x3 convolution
        self.conv = nn.Sequential(
            nn.BatchNorm2d(4 * growth_rate),
            nn.ReLU(inplace=True),
            nn.Conv2d(4 * growth_rate, growth_rate, kernel_size=3, 
                     padding=1, bias=False)
        )
    
    def forward(self, x):
        x = self.bottleneck(x)
        x = self.conv(x)
        return x
```

### Transition Layers

To control model size, DenseNet uses transition layers between dense blocks:

```python
class TransitionLayer(nn.Module):
    """Transition layer: reduces channels and spatial dimensions"""
    
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)
        self.pool = nn.AvgPool2d(kernel_size=2, stride=2)
        self.bn = nn.BatchNorm2d(out_channels)
    
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.pool(x)
        return x
```

### Building DenseNet-121

```python
class DenseNet(nn.Module):
    def __init__(self, growth_rate=32, block_config=(6, 12, 24, 16),
                 num_classes=1000):
        super().__init__()
        
        # Initial convolution
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        
        num_features = 64
        
        # Dense blocks and transition layers
        for i, num_layers in enumerate(block_config):
            dense_block = DenseBlock(num_layers, num_features, growth_rate)
            self.features.add_module(f'denseblock{i+1}', dense_block)
            
            num_features += num_layers * growth_rate
            
            # Add transition layer (except after last block)
            if i != len(block_config) - 1:
                trans = TransitionLayer(num_features, num_features // 2)
                self.features.add_module(f'transition{i+1}', trans)
                num_features = num_features // 2
        
        # Final batch norm and classifier
        self.features.add_module('norm5', nn.BatchNorm2d(num_features))
        self.classifier = nn.Linear(num_features, num_classes)
    
    def forward(self, x):
        features = self.features(x)
        out = nn.functional.relu(features, inplace=True)
        out = nn.functional.adaptive_avg_pool2d(out, (1, 1))
        out = torch.flatten(out, 1)
        out = self.classifier(out)
        return out


def densenet121(num_classes=1000):
    """DenseNet-121: growth_rate=32, layers=(6, 12, 24, 16)"""
    return DenseNet(growth_rate=32, block_config=(6, 12, 24, 16), num_classes=num_classes)
```

### Benefits of Dense Connectivity

1. **Feature Reuse**: All layers have access to original features
2. **Parameter Efficiency**: Fewer parameters than ResNet
3. **Improved Gradient Flow**: Shorter paths from loss to earlier layers
4. **Regularization Effect**: Implicit ensemble of different depth networks

---

## 2.4 EfficientNet: Compound Scaling

### The Scaling Problem

Traditionally, networks are scaled by increasing:
- **Depth** (more layers)
- **Width** (more channels)
- **Resolution** (larger images)

But how do we balance these dimensions optimally?

### Compound Scaling Method

EfficientNet uses a compound coefficient φ to uniformly scale all dimensions:

```
depth: d = α^φ × d₀
width: w = β^φ × w₀
resolution: r = γ^φ × r₀
```

Where α, β, γ are determined by neural architecture search (NAS).

### MBConv Blocks

EfficientNet uses Mobile Inverted Bottleneck Convolution (MBConv):

```python
class MBConvBlock(nn.Module):
    """Mobile Inverted Bottleneck Convolution with Squeeze-and-Excitation"""
    
    def __init__(self, in_channels, out_channels, expand_ratio, stride, se_ratio=0.25):
        super().__init__()
        self.stride = stride
        self.use_residual = (stride == 1 and in_channels == out_channels)
        
        # Expand: 1x1 convolution
        expanded_channels = in_channels * expand_ratio
        self.expand_conv = nn.Sequential(
            nn.Conv2d(in_channels, expanded_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(expanded_channels),
            nn.SiLU(inplace=True)
        ) if expand_ratio > 1 else nn.Identity()
        
        # Depthwise: 3x3 or 5x5 convolution
        kernel_size = 3 if stride <= 2 else 5
        self.depthwise_conv = nn.Sequential(
            nn.Conv2d(expanded_channels, expanded_channels, kernel_size=kernel_size,
                     stride=stride, padding=kernel_size//2, 
                     groups=expanded_channels, bias=False),
            nn.BatchNorm2d(expanded_channels),
            nn.SiLU(inplace=True)
        )
        
        # Squeeze-and-Excitation
        se_channels = max(1, int(in_channels * se_ratio))
        self.se = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(expanded_channels, se_channels, kernel_size=1),
            nn.SiLU(inplace=True),
            nn.Conv2d(se_channels, expanded_channels, kernel_size=1),
            nn.Sigmoid()
        )
        
        # Project: 1x1 convolution
        self.project_conv = nn.Sequential(
            nn.Conv2d(expanded_channels, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels)
        )
    
    def forward(self, x):
        identity = x
        
        # Expand
        x = self.expand_conv(x)
        
        # Depthwise
        x = self.depthwise_conv(x)
        
        # Squeeze-and-Excitation
        se_weight = self.se(x)
        x = x * se_weight
        
        # Project
        x = self.project_conv(x)
        
        # Residual connection
        if self.use_residual:
            x = x + identity
        
        return x
```

### EfficientNet Architecture

```python
def efficientnet_b0(num_classes=1000):
    """EfficientNet-B0 configuration"""
    config = [
        # (kernel, channels, repeat, stride, expand_ratio)
        (3, 16, 1, 1, 1),
        (3, 24, 2, 2, 6),
        (5, 40, 2, 2, 6),
        (3, 80, 3, 2, 6),
        (5, 112, 3, 1, 6),
        (5, 192, 4, 2, 6),
        (3, 320, 1, 1, 6),
    ]
    return EfficientNet(config, num_classes)


class EfficientNet(nn.Module):
    def __init__(self, config, num_classes=1000):
        super().__init__()
        
        # Stem convolution
        self.stem = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.SiLU(inplace=True)
        )
        
        # MBConv blocks
        layers = []
        in_channels = 32
        
        for kernel, channels, repeat, stride, expand_ratio in config:
            for i in range(repeat):
                s = stride if i == 0 else 1
                layers.append(MBConvBlock(in_channels, channels, expand_ratio, s))
                in_channels = channels
        
        self.blocks = nn.Sequential(*layers)
        
        # Head
        self.head = nn.Sequential(
            nn.Conv2d(in_channels, 1280, kernel_size=1, bias=False),
            nn.BatchNorm2d(1280),
            nn.SiLU(inplace=True),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Dropout(0.2),
            nn.Linear(1280, num_classes)
        )
    
    def forward(self, x):
        x = self.stem(x)
        x = self.blocks(x)
        x = self.head(x)
        return x
```

### EfficientNet Variants

| Model | φ | Resolution | Depth | Width | Params | FLOPs |
|-------|---|------------|-------|-------|--------|-------|
| B0 | 0 | 224 | 1.0 | 1.0 | 5.3M | 0.4B |
| B1 | 0.5 | 240 | 1.2 | 1.1 | 7.8M | 0.7B |
| B2 | 1.0 | 260 | 1.4 | 1.2 | 9.1M | 1.0B |
| B3 | 1.5 | 300 | 1.8 | 1.4 | 12M | 1.8B |
| B4 | 2.0 | 380 | 2.2 | 1.8 | 19M | 4.2B |
| B5 | 2.5 | 456 | 2.7 | 2.2 | 30M | 10B |
| B6 | 3.0 | 528 | 3.3 | 2.6 | 43M | 19B |
| B7 | 3.5 | 600 | 4.0 | 3.1 | 66M | 37B |

---

## 2.5 Vision Transformers (ViT)

### Attention Meets Computer Vision

Vision Transformers apply the transformer architecture (originally for NLP) to images:

```python
import torch
import torch.nn as nn
import math

class PatchEmbedding(nn.Module):
    """Split image into patches and embed"""
    
    def __init__(self, img_size=224, patch_size=16, in_channels=3, embed_dim=768):
        super().__init__()
        assert img_size % patch_size == 0, "Image size must be divisible by patch size"
        
        self.num_patches = (img_size // patch_size) ** 2
        self.patch_size = patch_size
        
        # Linear projection of patches
        self.projection = nn.Conv2d(in_channels, embed_dim, 
                                    kernel_size=patch_size, stride=patch_size)
    
    def forward(self, x):
        # x: (batch, channels, height, width)
        x = self.projection(x)  # (batch, embed_dim, num_patches_h, num_patches_w)
        x = x.flatten(2)  # (batch, embed_dim, num_patches)
        x = x.transpose(1, 2)  # (batch, num_patches, embed_dim)
        return x


class MultiHeadAttention(nn.Module):
    """Multi-head self-attention"""
    
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        assert embed_dim % num_heads == 0
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        self.qkv = nn.Linear(embed_dim, embed_dim * 3)
        self.proj = nn.Linear(embed_dim, embed_dim)
    
    def forward(self, x):
        batch_size, seq_len, embed_dim = x.shape
        
        # Get Q, K, V
        qkv = self.qkv(x)  # (batch, seq_len, 3*embed_dim)
        qkv = qkv.reshape(batch_size, seq_len, 3, self.num_heads, self.head_dim)
        qkv = qkv.permute(2, 0, 3, 1, 4)  # (3, batch, heads, seq_len, head_dim)
        q, k, v = qkv[0], qkv[1], qkv[2]
        
        # Compute attention scores
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        attn = torch.softmax(scores, dim=-1)
        
        # Apply attention to values
        out = torch.matmul(attn, v)  # (batch, heads, seq_len, head_dim)
        out = out.transpose(1, 2)  # (batch, seq_len, heads, head_dim)
        out = out.reshape(batch_size, seq_len, embed_dim)
        
        out = self.proj(out)
        return out


class TransformerBlock(nn.Module):
    """Transformer encoder block"""
    
    def __init__(self, embed_dim, num_heads, mlp_ratio=4.0, dropout=0.1):
        super().__init__()
        
        self.norm1 = nn.LayerNorm(embed_dim)
        self.attention = MultiHeadAttention(embed_dim, num_heads)
        self.dropout1 = nn.Dropout(dropout)
        
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, int(embed_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(embed_dim * mlp_ratio), embed_dim),
            nn.Dropout(dropout)
        )
    
    def forward(self, x):
        # Pre-norm architecture
        x = x + self.dropout1(self.attention(self.norm1(x)))
        x = x + self.mlp(self.norm2(x))
        return x


class VisionTransformer(nn.Module):
    """Vision Transformer for image classification"""
    
    def __init__(self, img_size=224, patch_size=16, in_channels=3, num_classes=1000,
                 embed_dim=768, num_heads=12, num_layers=12, mlp_ratio=4.0, dropout=0.1):
        super().__init__()
        
        self.patch_embed = PatchEmbedding(img_size, patch_size, in_channels, embed_dim)
        num_patches = self.patch_embed.num_patches
        
        # Class token
        self.cls_token = nn.Parameter(torch.randn(1, 1, embed_dim))
        
        # Position embeddings
        self.pos_embed = nn.Parameter(torch.randn(1, num_patches + 1, embed_dim))
        self.pos_dropout = nn.Dropout(dropout)
        
        # Transformer encoder
        self.transformer = nn.Sequential(*[
            TransformerBlock(embed_dim, num_heads, mlp_ratio, dropout)
            for _ in range(num_layers)
        ])
        
        # Classification head
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x):
        batch_size = x.shape[0]
        
        # Embed patches
        x = self.patch_embed(x)  # (batch, num_patches, embed_dim)
        
        # Add class token
        cls_tokens = self.cls_token.expand(batch_size, -1, -1)
        x = torch.cat([cls_tokens, x], dim=1)  # (batch, num_patches+1, embed_dim)
        
        # Add positional embeddings
        x = x + self.pos_embed
        x = self.pos_dropout(x)
        
        # Transformer encoder
        x = self.transformer(x)
        
        # Use class token for classification
        x = self.norm(x[:, 0])  # (batch, embed_dim)
        x = self.head(x)
        
        return x


def vit_base_patch16_224(num_classes=1000):
    """ViT-B/16: Base model with 16x16 patches"""
    return VisionTransformer(
        img_size=224, patch_size=16,
        embed_dim=768, num_heads=12, num_layers=12,
        num_classes=num_classes
    )


def vit_large_patch16_224(num_classes=1000):
    """ViT-L/16: Large model with 16x16 patches"""
    return VisionTransformer(
        img_size=224, patch_size=16,
        embed_dim=1024, num_heads=16, num_layers=24,
        num_classes=num_classes
    )
```

### ViT vs CNN Comparison

| Aspect | CNN | Vision Transformer |
|--------|-----|-------------------|
| Inductive Bias | Strong (locality, translation equivariance) | Weak (learns from data) |
| Data Requirements | Moderate | Large (needs pretraining) |
| Global Context | Limited (grows with depth) | Immediate (self-attention) |
| Computation | O(n) | O(n²) for sequence length n |
| Interpretability | Harder | Attention maps provide insight |

---

## 2.6 Practical Implementation Guide

### Loading Pretrained Models

```python
import torchvision.models as models

# Load pretrained ResNet-50
resnet50 = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# Load pretrained DenseNet-121
densenet121 = models.densenet121(weights=models.DenseNet121_Weights.IMAGENET1K_V1)

# Load pretrained EfficientNet-B0
efficientnet_b0 = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)

# Modify for custom number of classes
num_classes = 10
resnet50.fc = nn.Linear(resnet50.fc.in_features, num_classes)
```

### Feature Extraction

```python
def extract_features(model, image, layer_name):
    """Extract intermediate features from a specific layer"""
    features = {}
    
    def hook(module, input, output):
        features[layer_name] = output.detach()
    
    # Register hook
    layer = dict([*model.named_modules()])[layer_name]
    handle = layer.register_forward_hook(hook)
    
    # Forward pass
    with torch.no_grad():
        model(image)
    
    # Remove hook
    handle.remove()
    
    return features[layer_name]


# Example usage
image = torch.randn(1, 3, 224, 224)
resnet = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
features = extract_features(resnet, image, 'layer3')
print(f"Feature shape: {features.shape}")
```

### Model Comparison Script

```python
def compare_models(models_dict, image_size=224):
    """Compare different models on various metrics"""
    import time
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    image = torch.randn(1, 3, image_size, image_size).to(device)
    
    results = []
    
    for name, model in models_dict.items():
        model = model.to(device)
        model.eval()
        
        # Warmup
        with torch.no_grad():
            model(image)
        
        # Measure inference time
        torch.cuda.synchronize()
        start = time.time()
        iterations = 100
        
        with torch.no_grad():
            for _ in range(iterations):
                model(image)
        
        torch.cuda.synchronize()
        avg_time = (time.time() - start) / iterations
        
        # Count parameters
        params = sum(p.numel() for p in model.parameters()) / 1e6
        
        results.append({
            'name': name,
            'params_millions': params,
            'inference_ms': avg_time * 1000
        })
    
    return results


# Usage
models_to_compare = {
    'ResNet-50': models.resnet50(),
    'DenseNet-121': models.densenet121(),
    'EfficientNet-B0': models.efficientnet_b0()
}

results = compare_models(models_to_compare)
for r in results:
    print(f"{r['name']}: {r['params_millions']:.1f}M params, {r['inference_ms']:.2f}ms")
```

---

## 2.7 Choosing the Right Architecture

### Decision Matrix

| Use Case | Recommended Architecture | Reason |
|----------|-------------------------|--------|
| Mobile/Edge | EfficientNet-B0/B1 | Best accuracy/efficiency tradeoff |
| Medical Imaging | ResNet-50/101 | Proven reliability, good transfer learning |
| Fine-grained Classification | DenseNet-121/169 | Feature reuse helps subtle differences |
| Large-scale Production | EfficientNet-B3/B5 | Scalable, well-supported |
| Research/Experimentation | ViT-B/16 | Flexible, strong with sufficient data |
| Low Latency | MobileNetV3 | Optimized for speed |

### Performance Benchmarks (ImageNet)

| Model | Top-1 Acc | Top-5 Acc | Params | FLOPs | Inference (ms)* |
|-------|-----------|-----------|--------|-------|-----------------|
| ResNet-50 | 80.8% | 95.6% | 25M | 4.1B | 15 |
| ResNet-101 | 81.9% | 96.0% | 44M | 7.8B | 25 |
| DenseNet-121 | 75.0% | 92.3% | 8M | 2.9B | 18 |
| EfficientNet-B0 | 77.3% | 93.5% | 5.3M | 0.4B | 8 |
| EfficientNet-B3 | 81.9% | 96.0% | 12M | 1.8B | 18 |
| ViT-B/16 | 84.6%* | 97.0%* | 86M | 17.6B | 35 |

*With JFT-300M pretraining

---

## Exercises

### Exercise 2.1: Implement ResNet-18
Build a ResNet-18 from scratch using BasicBlocks and train it on CIFAR-10. Compare its performance with a plain 18-layer network without skip connections.

### Exercise 2.2: DenseNet Growth Rate Analysis
Experiment with different growth rates (12, 32, 48) in DenseNet-121. How does the growth rate affect accuracy and memory usage?

### Exercise 2.3: EfficientNet Scaling
Take EfficientNet-B0 and apply compound scaling to create a custom variant. Compare your scaled model with the official EfficientNet-B3.

### Exercise 2.4: ViT Attention Visualization
Load a pretrained ViT and visualize the attention maps for different images. What patterns do you observe?

### Exercise 2.5: Architecture Comparison
Train ResNet-50, DenseNet-121, and EfficientNet-B0 on the same dataset with similar compute budgets. Compare their convergence speed and final accuracy.

---

## Summary

In this chapter, we explored advanced CNN architectures:

1. **ResNet**: Introduced skip connections to enable training of very deep networks
2. **DenseNet**: Extended skip connections to dense connectivity for better feature reuse
3. **EfficientNet**: Used compound scaling for optimal balance of depth, width, and resolution
4. **Vision Transformers**: Applied self-attention mechanisms to image recognition

Each architecture offers unique advantages depending on your use case, data availability, and computational constraints. Understanding these designs will help you choose and adapt the right architecture for your specific computer vision tasks.

---

**Next Chapter**: Chapter 3 will cover training techniques including transfer learning, data augmentation strategies, and regularization methods.
