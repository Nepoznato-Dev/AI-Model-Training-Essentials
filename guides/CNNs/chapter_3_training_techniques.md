# Chapter 3: CNN Training Techniques

## 3.1 Introduction to Advanced Training Methods

Training CNNs effectively requires more than just defining an architecture. This chapter covers essential techniques for achieving state-of-the-art performance: transfer learning, data augmentation, regularization, and optimization strategies.

### Key Training Challenges

| Challenge | Solution | Impact |
|-----------|----------|--------|
| Limited data | Transfer learning, augmentation | Prevents overfitting |
| Overfitting | Regularization, dropout | Improves generalization |
| Slow convergence | Learning rate scheduling | Faster training |
| Poor generalization | Data augmentation | Better test accuracy |
| Vanishing gradients | Batch normalization | Stable training |

---

## 3.2 Transfer Learning

### Why Transfer Learning Works

Deep networks learn hierarchical features:
- **Early layers**: Generic (edges, textures)
- **Middle layers**: Task-specific patterns
- **Late layers**: Highly specific to training task

```python
import torch
import torch.nn as nn
import torchvision.models as models
```

### Feature Extraction Approach

Freeze the pretrained backbone and only train the classifier:

```python
def create_feature_extractor(model_name='resnet50', num_classes=10):
    """Use pretrained network as fixed feature extractor"""
    
    # Load pretrained model
    if model_name == 'resnet50':
        model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
        in_features = model.fc.in_features
        # Remove final classification layer
        model.fc = nn.Identity()
    elif model_name == 'efficientnet_b0':
        model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)
        in_features = model.classifier[1].in_features
        model.classifier = nn.Identity()
    else:
        raise ValueError(f"Unknown model: {model_name}")
    
    # Freeze all parameters
    for param in model.parameters():
        param.requires_grad = False
    
    # Create new classifier
    classifier = nn.Sequential(
        nn.Linear(in_features, 256),
        nn.ReLU(inplace=True),
        nn.Dropout(0.5),
        nn.Linear(256, num_classes)
    )
    
    return model, classifier


# Usage
backbone, classifier = create_feature_extractor('resnet50', num_classes=10)
backbone.eval()  # Keep in eval mode (no batch norm updates)

# Training loop (only classifier gradients computed)
for images, labels in dataloader:
    with torch.no_grad():
        features = backbone(images)  # No gradient computation
    outputs = classifier(features)   # Gradients computed here
    loss = criterion(outputs, labels)
    loss.backward()
```

### Fine-Tuning Approach

Unfreeze some layers and train with a lower learning rate:

```python
def create_finetune_model(model_name='resnet50', num_classes=10, 
                          unfreeze_layers=2):
    """Fine-tune pretrained network with selective unfreezing"""
    
    # Load pretrained model
    model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
    
    # Replace final layer
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    
    # Strategy 1: Unfreeze last N layers
    layers_to_unfreeze = []
    for name, module in model.named_modules():
        if isinstance(module, (nn.Conv2d, nn.BatchNorm2d)):
            layers_to_unfreeze.append(name)
    
    # Keep only the last few layers
    layers_to_unfreeze = layers_to_unfreeze[-unfreeze_layers*4:]  # Approximate
    
    # Freeze all, then unfreeze selected
    for param in model.parameters():
        param.requires_grad = False
    
    for name, module in model.named_modules():
        if name in layers_to_unfreeze:
            for param in module.parameters():
                param.requires_grad = True
    
    # Strategy 2: Differential learning rates
    base_params = []
    head_params = []
    
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        
        if 'fc' in name or 'layer4' in name:
            head_params.append(param)
        else:
            base_params.append(param)
    
    optimizer = torch.optim.SGD([
        {'params': base_params, 'lr': 0.001},
        {'params': head_params, 'lr': 0.01}  # Higher LR for new layers
    ], momentum=0.9, weight_decay=1e-4)
    
    return model, optimizer


# Usage
model, optimizer = create_finetune_model('resnet50', num_classes=10, unfreeze_layers=2)
```

### Layer-wise Learning Rate Decay

Gradually decrease learning rate for earlier layers:

```python
def create_llrd_optimizer(model, base_lr=0.01, lr_decay=0.75):
    """Layer-wise Learning Rate Decay (LLRD)"""
    
    param_groups = []
    
    # Group parameters by layer depth
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        
        # Determine layer depth (higher number = deeper)
        if 'layer4' in name:
            depth = 4
        elif 'layer3' in name:
            depth = 3
        elif 'layer2' in name:
            depth = 2
        elif 'layer1' in name:
            depth = 1
        else:
            depth = 5  # Final classifier
        
        # Calculate learning rate for this layer
        lr = base_lr * (lr_decay ** (5 - depth))
        
        param_groups.append({
            'params': [param],
            'lr': lr,
            'name': name
        })
    
    optimizer = torch.optim.SGD(param_groups, momentum=0.9, weight_decay=1e-4)
    return optimizer


# Usage
optimizer = create_llrd_optimizer(model, base_lr=0.01, lr_decay=0.75)
# layer1: 0.01 * 0.75^4 = 0.0032
# layer4: 0.01 * 0.75^1 = 0.0075
# fc:     0.01 * 0.75^0 = 0.01
```

---

## 3.3 Data Augmentation Strategies

### Basic Augmentations

```python
from torchvision import transforms

def get_basic_transforms(img_size=224, is_training=True):
    """Standard data augmentation pipeline"""
    
    if is_training:
        return transforms.Compose([
            transforms.RandomResizedCrop(img_size, scale=(0.8, 1.0)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomVerticalFlip(p=0.1),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, 
                                 saturation=0.2, hue=0.1),
            transforms.RandomRotation(degrees=15),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                               std=[0.229, 0.224, 0.225]),
            transforms.RandomErasing(p=0.5),
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

### Advanced Augmentation: Mixup

Mixup creates virtual training examples by blending images and labels:

```python
class Mixup:
    """Mixup augmentation: blend two images and their labels"""
    
    def __init__(self, alpha=0.4):
        self.alpha = alpha
    
    def __call__(self, images, targets):
        if self.alpha <= 0:
            return images, targets
        
        # Sample mixing coefficient
        import numpy as np
        lam = np.random.beta(self.alpha, self.alpha)
        
        # Random permutation
        batch_size = images.size(0)
        index = torch.randperm(batch_size).to(images.device)
        
        # Mix images
        mixed_images = lam * images + (1 - lam) * images[index]
        
        # Mix labels (for soft labels)
        if len(targets.shape) == 1:
            # Convert to one-hot for mixing
            num_classes = targets.max().item() + 1
            targets_onehot = nn.functional.one_hot(targets, num_classes).float()
            mixed_targets = lam * targets_onehot + (1 - lam) * targets_onehot[index]
        else:
            # Already soft labels
            mixed_targets = lam * targets + (1 - lam) * targets[index]
        
        return mixed_images, mixed_targets


# Usage in training loop
mixup = Mixup(alpha=0.4)

for images, labels in dataloader:
    images, labels = images.cuda(), labels.cuda()
    images, labels = mixup(images, labels)
    
    outputs = model(images)
    loss = criterion(outputs, labels)  # Use BCELoss for soft labels
    loss.backward()
```

### CutMix Augmentation

CutMix replaces regions of one image with patches from another:

```python
class CutMix:
    """CutMix augmentation: replace region with patch from another image"""
    
    def __init__(self, alpha=1.0):
        self.alpha = alpha
    
    def __call__(self, images, targets):
        if self.alpha <= 0:
            return images, targets
        
        batch_size = images.size(0)
        index = torch.randperm(batch_size).to(images.device)
        
        # Sample cutmix parameters
        lam = np.random.beta(self.alpha, self.alpha)
        
        # Generate random bbox
        W, H = images.shape[2], images.shape[3]
        cut_rat = np.sqrt(1. - lam)
        cut_w = int(W * cut_rat)
        cut_h = int(H * cut_rat)
        
        cx = np.random.randint(W)
        cy = np.random.randint(H)
        
        x1 = np.clip(cx - cut_w // 2, 0, W)
        y1 = np.clip(cy - cut_h // 2, 0, H)
        x2 = np.clip(cx + cut_w // 2, 0, W)
        y2 = np.clip(cy + cut_h // 2, 0, H)
        
        # Apply cutmix
        images_cut = images.clone()
        images_cut[:, :, y1:y2, x1:x2] = images[index, :, y1:y2, x1:x2]
        
        # Adjust lambda to actual area
        lam = 1 - ((x2 - x1) * (y2 - y1) / (W * H))
        
        # Mix labels
        if len(targets.shape) == 1:
            num_classes = targets.max().item() + 1
            targets_onehot = nn.functional.one_hot(targets, num_classes).float()
            mixed_targets = lam * targets_onehot + (1 - lam) * targets_onehot[index]
        else:
            mixed_targets = lam * targets + (1 - lam) * targets[index]
        
        return images_cut, mixed_targets


# Usage
cutmix = CutMix(alpha=1.0)
images, labels = cutmix(images, labels)
```

### AutoAugment and RandAugment

Automated augmentation policy search:

```python
from torchvision.transforms import autoaugment

def get_autoaugment_transforms(img_size=224, is_training=True):
    """AutoAugment: learned augmentation policies"""
    
    if is_training:
        # Option 1: AutoAugment ImageNet policy
        transform = transforms.Compose([
            transforms.RandomResizedCrop(img_size),
            transforms.RandomHorizontalFlip(),
            autoaugment.AutoAugment(policy=autoaugment.AutoAugmentPolicy.IMAGENET),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                               std=[0.229, 0.224, 0.225])
        ])
        
        # Option 2: RandAugment (simpler, no search needed)
        # transform = transforms.Compose([
        #     transforms.RandomResizedCrop(img_size),
        #     transforms.RandomHorizontalFlip(),
        #     autoaugment.RandAugment(num_ops=2, magnitude=9),
        #     transforms.ToTensor(),
        #     transforms.Normalize(mean=[0.485, 0.456, 0.406],
        #                        std=[0.229, 0.224, 0.225])
        # ])
        
        return transform
    else:
        return get_basic_transforms(img_size, is_training=False)
```

---

## 3.4 Regularization Techniques

### Dropout Variants

```python
class DropoutVariants(nn.Module):
    """Different dropout variants for regularization"""
    
    def __init__(self, in_features, num_classes, dropout_rate=0.5):
        super().__init__()
        
        # Standard dropout
        self.standard_dropout = nn.Dropout(dropout_rate)
        
        # Spatial dropout (for convolutional features)
        self.spatial_dropout = nn.Dropout2d(dropout_rate)
        
        # DropBlock (structured dropout for CNNs)
        self.dropblock = DropBlock(drop_rate=dropout_rate, block_size=7)
        
        self.fc = nn.Linear(in_features, num_classes)
    
    def forward(self, x, dropout_type='standard'):
        if dropout_type == 'standard':
            x = self.standard_dropout(x)
        elif dropout_type == 'spatial':
            x = self.spatial_dropout(x.unsqueeze(2)).squeeze(2)
        elif dropout_type == 'dropblock':
            x = self.dropblock(x)
        
        return self.fc(x)


class DropBlock(nn.Module):
    """DropBlock: structured dropout for convolutional layers"""
    
    def __init__(self, drop_rate=0.1, block_size=7):
        super().__init__()
        self.drop_rate = drop_rate
        self.block_size = block_size
    
    def forward(self, x):
        if not self.training or self.drop_rate <= 0:
            return x
        
        # Calculate gamma (adjust drop rate based on block size)
        gamma = self._calculate_gamma(x)
        
        # Generate mask
        mask = torch.bernoulli(torch.full_like(x, fill_value=gamma))
        mask = nn.functional.max_pool2d(
            mask, kernel_size=self.block_size, stride=1,
            padding=self.block_size // 2
        )
        
        # Scale and apply
        mask = 1 - mask
        x = x * mask / (1 - self.drop_rate)
        
        return x
    
    def _calculate_gamma(self, x):
        """Adjust drop rate based on activation size"""
        h, w = x.shape[2], x.shape[3]
        return self.drop_rate * (h * w) / (self.block_size ** 2)
```

### Label Smoothing

Prevents overconfidence by smoothing target labels:

```python
class LabelSmoothingCrossEntropy(nn.Module):
    """Cross-entropy loss with label smoothing"""
    
    def __init__(self, smoothing=0.1):
        super().__init__()
        self.smoothing = smoothing
    
    def forward(self, outputs, targets):
        log_probs = nn.functional.log_softmax(outputs, dim=-1)
        
        if len(targets.shape) == 1:
            # Hard labels -> smooth them
            num_classes = outputs.size(-1)
            nll_loss = -log_probs.gather(dim=-1, index=targets.unsqueeze(1)).squeeze(1)
            smooth_loss = -log_probs.mean(dim=-1)
            loss = (1 - self.smoothing) * nll_loss + self.smoothing * smooth_loss
        else:
            # Already soft labels
            loss = -(targets * log_probs).sum(dim=-1)
        
        return loss.mean()


# Usage
criterion = LabelSmoothingCrossEntropy(smoothing=0.1)
```

### Stochastic Depth

Randomly skip layers during training:

```python
class StochasticDepth(nn.Module):
    """Stochastic Depth: randomly drop layers during training"""
    
    def __init__(self, drop_prob, linear_decay=True):
        super().__init__()
        self.drop_prob = drop_prob
        self.linear_decay = linear_decay
    
    def forward(self, x, layer_id, total_layers):
        if not self.training:
            return x
        
        # Calculate drop probability for this layer
        if self.linear_decay:
            # Later layers have higher drop probability
            drop_prob = self.drop_prob * (layer_id / (total_layers - 1))
        else:
            drop_prob = self.drop_prob
        
        # Sample survival
        keep_prob = 1 - drop_prob
        mask = torch.bernoulli(torch.tensor(keep_prob, device=x.device))
        
        if mask.item() == 0:
            # Skip this layer (identity)
            return x
        else:
            # Scale output
            return x / keep_prob


# Usage in ResNet
class ResNetWithStochasticDepth(nn.Module):
    def __init__(self, stochastic_depth_prob=0.2):
        super().__init__()
        self.stochastic_depth = StochasticDepth(stochastic_depth_prob)
        self.total_layers = 16  # For ResNet-18
        # ... rest of model
    
    def forward(self, x):
        # ... initial layers
        
        for i, layer in enumerate(self.layers):
            x = layer(x)
            x = self.stochastic_depth(x, i, self.total_layers)
        
        return x
```

---

## 3.5 Optimization Strategies

### Learning Rate Scheduling

```python
def get_scheduler(optimizer, scheduler_type='cosine', epochs=100):
    """Various learning rate schedules"""
    
    if scheduler_type == 'step':
        # Step decay: reduce LR by factor every N epochs
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer, step_size=30, gamma=0.1
        )
    
    elif scheduler_type == 'multistep':
        # Multi-step decay at specific epochs
        scheduler = torch.optim.lr_scheduler.MultiStepLR(
            optimizer, milestones=[30, 60, 90], gamma=0.1
        )
    
    elif scheduler_type == 'cosine':
        # Cosine annealing
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=epochs, eta_min=1e-6
        )
    
    elif scheduler_type == 'cosine_warmup':
        # Cosine with warmup
        scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
            optimizer, T_0=10, T_mult=2, eta_min=1e-6
        )
    
    elif scheduler_type == 'onecycle':
        # One Cycle Policy
        scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optimizer, max_lr=0.1, epochs=epochs, steps_per_epoch=len(dataloader)
        )
    
    elif scheduler_type == 'reduce_on_plateau':
        # Reduce when validation loss plateaus
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, mode='min', factor=0.5, patience=5, verbose=True
        )
    
    else:
        raise ValueError(f"Unknown scheduler: {scheduler_type}")
    
    return scheduler
```

### Warmup Strategies

```python
class WarmupScheduler:
    """Learning rate warmup wrapper"""
    
    def __init__(self, optimizer, warmup_epochs, base_scheduler):
        self.optimizer = optimizer
        self.warmup_epochs = warmup_epochs
        self.base_scheduler = base_scheduler
        self.current_epoch = 0
        self.base_lrs = [group['lr'] for group in optimizer.param_groups]
    
    def step(self):
        self.current_epoch += 1
        
        if self.current_epoch <= self.warmup_epochs:
            # Linear warmup
            progress = self.current_epoch / self.warmup_epochs
            for param_group, base_lr in zip(self.optimizer.param_groups, self.base_lrs):
                param_group['lr'] = base_lr * progress
        else:
            # Base scheduler
            self.base_scheduler.step()
    
    def get_lr(self):
        return [group['lr'] for group in self.optimizer.param_groups]


# Usage
base_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)
scheduler = WarmupScheduler(optimizer, warmup_epochs=5, base_scheduler=base_scheduler)

for epoch in range(100):
    train(model, dataloader, optimizer)
    scheduler.step()
```

### AdamW Optimizer

Adam with decoupled weight decay:

```python
def create_optimizer(model, optimizer_type='adamw', lr=0.001, weight_decay=0.05):
    """Create optimizer with appropriate settings"""
    
    # Separate weight decay from bias and normalization layers
    decay_params = []
    no_decay_params = []
    
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        
        if 'bias' in name or 'bn' in name or 'layer_norm' in name:
            no_decay_params.append(param)
        else:
            decay_params.append(param)
    
    param_groups = [
        {'params': decay_params, 'weight_decay': weight_decay},
        {'params': no_decay_params, 'weight_decay': 0.0}
    ]
    
    if optimizer_type == 'adamw':
        optimizer = torch.optim.AdamW(param_groups, lr=lr, betas=(0.9, 0.999))
    elif optimizer_type == 'sgd':
        optimizer = torch.optim.SGD(param_groups, lr=lr, momentum=0.9, 
                                   weight_decay=weight_decay)
    elif optimizer_type == 'rmsprop':
        optimizer = torch.optim.RMSprop(param_groups, lr=lr, 
                                       weight_decay=weight_decay)
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_type}")
    
    return optimizer
```

### Gradient Clipping

Prevent exploding gradients:

```python
def train_with_gradient_clipping(model, dataloader, optimizer, criterion, 
                                  clip_value=1.0):
    """Training with gradient clipping"""
    
    model.train()
    
    for images, targets in dataloader:
        images, targets = images.cuda(), targets.cuda()
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, targets)
        loss.backward()
        
        # Clip gradients
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip_value)
        # Alternative: clip by value
        # torch.nn.utils.clip_grad_value_(model.parameters(), clip_value)
        
        optimizer.step()
    
    return loss.item()
```

---

## 3.6 Training Best Practices

### Complete Training Pipeline

```python
class CNNTrainer:
    """Complete CNN training pipeline with best practices"""
    
    def __init__(self, model, config):
        self.model = model.cuda()
        self.config = config
        
        # Optimizer with weight decay separation
        self.optimizer = create_optimizer(
            model, 
            optimizer_type=config.get('optimizer', 'adamw'),
            lr=config.get('lr', 0.001),
            weight_decay=config.get('weight_decay', 0.05)
        )
        
        # Loss with label smoothing
        self.criterion = LabelSmoothingCrossEntropy(
            smoothing=config.get('label_smoothing', 0.1)
        )
        
        # Learning rate scheduler with warmup
        base_scheduler = get_scheduler(
            self.optimizer, 
            scheduler_type='cosine',
            epochs=config['epochs']
        )
        self.scheduler = WarmupScheduler(
            self.optimizer,
            warmup_epochs=config.get('warmup_epochs', 5),
            base_scheduler=base_scheduler
        )
        
        # Augmentation
        self.mixup = Mixup(alpha=config.get('mixup_alpha', 0.4))
        self.cutmix = CutMix(alpha=config.get('cutmix_alpha', 1.0))
        
        # Tracking
        self.best_accuracy = 0
        self.history = {'train_loss': [], 'val_loss': [], 'val_acc': []}
    
    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for images, targets in dataloader:
            images, targets = images.cuda(), targets.cuda()
            
            # Apply augmentation
            if torch.rand(1) < 0.5:
                images, targets = self.mixup(images, targets)
            else:
                images, targets = self.cutmix(images, targets)
            
            self.optimizer.zero_grad()
            outputs = self.model(images)
            loss = self.criterion(outputs, targets)
            loss.backward()
            
            # Gradient clipping
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            
            self.optimizer.step()
            
            total_loss += loss.item()
            
            # Accuracy (for hard labels)
            if len(targets.shape) == 1:
                _, predicted = outputs.max(1)
                total += targets.size(0)
                correct += predicted.eq(targets).sum().item()
        
        avg_loss = total_loss / len(dataloader)
        accuracy = 100. * correct / total if total > 0 else 0
        
        return avg_loss, accuracy
    
    @torch.no_grad()
    def validate(self, dataloader):
        self.model.eval()
        total_loss = 0
        correct = 0
        total = 0
        
        for images, targets in dataloader:
            images, targets = images.cuda(), targets.cuda()
            outputs = self.model(images)
            loss = self.criterion(outputs, targets)
            
            total_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()
        
        avg_loss = total_loss / len(dataloader)
        accuracy = 100. * correct / total
        
        return avg_loss, accuracy
    
    def train(self, train_loader, val_loader):
        for epoch in range(self.config['epochs']):
            # Train
            train_loss, train_acc = self.train_epoch(train_loader)
            
            # Validate
            val_loss, val_acc = self.validate(val_loader)
            
            # Update scheduler
            self.scheduler.step()
            
            # Log
            self.history['train_loss'].append(train_loss)
            self.history['val_loss'].append(val_loss)
            self.history['val_acc'].append(val_acc)
            
            print(f"Epoch {epoch+1}: "
                  f"Train Loss={train_loss:.4f}, Acc={train_acc:.2f}% | "
                  f"Val Loss={val_loss:.4f}, Acc={val_acc:.2f}%")
            
            # Save best model
            if val_acc > self.best_accuracy:
                self.best_accuracy = val_acc
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': self.model.state_dict(),
                    'optimizer_state_dict': self.optimizer.state_dict(),
                    'accuracy': val_acc,
                }, 'best_model.pth')
        
        return self.best_accuracy
```

### Hyperparameter Recommendations

| Dataset Size | Learning Rate | Weight Decay | Batch Size | Epochs |
|-------------|---------------|--------------|------------|--------|
| Small (<10K) | 0.001 | 0.05 | 32 | 100-200 |
| Medium (10K-100K) | 0.01 | 0.05 | 64 | 50-100 |
| Large (>100K) | 0.1 | 0.05 | 256 | 30-50 |

### Common Pitfalls and Solutions

| Problem | Symptom | Solution |
|---------|---------|----------|
| Overfitting | Train acc >> Val acc | More augmentation, dropout, early stopping |
| Underfitting | Low train acc | Increase model capacity, train longer |
| Unstable training | Loss spikes | Lower LR, gradient clipping, batch norm |
| Slow convergence | Loss decreases slowly | LR warmup, better initialization |
| Poor generalization | High val error | Label smoothing, stronger augmentation |

---

## Exercises

### Exercise 3.1: Transfer Learning Comparison
Compare feature extraction vs fine-tuning on a small dataset (e.g., CIFAR-10 with only 100 samples per class). Which approach works better?

### Exercise 3.2: Augmentation Ablation
Train a model with different augmentation strategies: (1) basic, (2) +Mixup, (3) +CutMix, (4) +AutoAugment. Compare final accuracies.

### Exercise 3.3: Learning Rate Schedules
Experiment with different LR schedules (step, cosine, one-cycle) on the same model. Plot the learning curves and compare convergence.

### Exercise 3.4: Label Smoothing Analysis
Train with label smoothing values of 0.0, 0.1, 0.2, and 0.3. How does smoothing affect model confidence and calibration?

### Exercise 3.5: Build a Complete Pipeline
Implement the full `CNNTrainer` class and train on ImageNet subset. Tune hyperparameters to achieve best validation accuracy.

---

## Summary

This chapter covered essential CNN training techniques:

1. **Transfer Learning**: Leverage pretrained models for better performance with less data
2. **Data Augmentation**: Mixup, CutMix, and AutoAugment for improved generalization
3. **Regularization**: Dropout variants, label smoothing, and stochastic depth
4. **Optimization**: Learning rate scheduling, warmup, AdamW, and gradient clipping
5. **Best Practices**: Complete training pipeline with proven hyperparameters

Mastering these techniques will help you train CNNs that achieve state-of-the-art results on your computer vision tasks.

---

**Next Chapter**: Chapter 4 will explore specialized applications including object detection, semantic segmentation, and image generation.
