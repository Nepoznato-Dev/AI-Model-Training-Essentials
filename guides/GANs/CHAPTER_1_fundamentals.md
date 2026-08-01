# Chapter 1: GAN Fundamentals

## 1.1 Introduction to Generative Adversarial Networks

Generative Adversarial Networks (GANs), introduced by Ian Goodfellow in 2014, are a class of machine learning frameworks where two neural networks contest with each other in a zero-sum game.

### The GAN Game

```
Generator (G)                    Discriminator (D)
     |                                  ^
     |  Creates fake samples            |  Distinguishes real vs fake
     v                                  |
Noise → [G] → Fake Images ────────────→ [D] → Real/Fake Prediction
                                           ↑
                                    Real Images
```

### Key Concepts

- **Generator**: Learns to create realistic data from random noise
- **Discriminator**: Learns to distinguish real from generated data
- **Minimax Game**: G tries to fool D, D tries to catch G
- **Nash Equilibrium**: Optimal point where G produces perfect fakes

## 1.2 Mathematical Foundation

### Original GAN Objective

```
min_G max_D V(D, G) = E_{x~p_data(x)}[log D(x)] + E_{z~p_z(z)}[log(1 - D(G(z)))]
```

Where:
- x: Real data samples
- z: Random noise vector
- G(z): Generated samples
- D(x): Probability x is real

### Training Algorithm

```python
import torch
import torch.nn as nn
import torch.optim as optim

class BasicGAN:
    def __init__(self, generator, discriminator, lr=0.0002, beta1=0.5):
        self.G = generator
        self.D = discriminator
        self.criterion = nn.BCELoss()
        
        self.optimizer_G = optim.Adam(G.parameters(), lr=lr, betas=(beta1, 0.999))
        self.optimizer_D = optim.Adam(D.parameters(), lr=lr, betas=(beta1, 0.999))
    
    def train_step(self, real_images, noise):
        batch_size = real_images.size(0)
        device = real_images.device
        
        # Labels for real and fake
        real_labels = torch.ones(batch_size, 1, device=device)
        fake_labels = torch.zeros(batch_size, 1, device=device)
        
        # =====================
        # Train Discriminator
        # =====================
        self.optimizer_D.zero_grad()
        
        # Real images
        D_real = self.D(real_images)
        D_loss_real = self.criterion(D_real, real_labels)
        
        # Fake images
        fake_images = self.G(noise)
        D_fake = self.D(fake_images.detach())
        D_loss_fake = self.criterion(D_fake, fake_labels)
        
        D_loss = (D_loss_real + D_loss_fake) / 2
        D_loss.backward()
        self.optimizer_D.step()
        
        # =================
        # Train Generator
        # =================
        self.optimizer_G.zero_grad()
        
        # Try to fool discriminator
        D_fake = self.D(fake_images)
        G_loss = self.criterion(D_fake, real_labels)  # Want D to think fakes are real
        G_loss.backward()
        self.optimizer_G.step()
        
        return D_loss.item(), G_loss.item()
```

## 1.3 Deep Convolutional GAN (DCGAN)

### Architecture Guidelines

- Replace pooling with strided convolutions
- Use batch normalization
- Remove fully connected layers
- Use ReLU in generator (except output)
- Use LeakyReLU in discriminator

### DCGAN Implementation

```python
class Generator(nn.Module):
    def __init__(self, nz=100, ngf=64, nc=3):
        super().__init__()
        self.main = nn.Sequential(
            # Input: z (nz x 1 x 1)
            nn.ConvTranspose2d(nz, ngf * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),
            # State: (ngf*8) x 4 x 4
            
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            # State: (ngf*4) x 8 x 8
            
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            # State: (ngf*2) x 16 x 16
            
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            # State: (ngf) x 32 x 32
            
            nn.ConvTranspose2d(ngf, nc, 4, 2, 1, bias=False),
            nn.Tanh()
            # Output: (nc) x 64 x 64
        )
    
    def forward(self, input):
        return self.main(input)


class Discriminator(nn.Module):
    def __init__(self, nc=3, ndf=64):
        super().__init__()
        self.main = nn.Sequential(
            # Input: (nc) x 64 x 64
            nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (ndf) x 32 x 32
            
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (ndf*2) x 16 x 16
            
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (ndf*4) x 8 x 8
            
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (ndf*8) x 4 x 4
            
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
            # Output: 1 x 1 x 1 (probability)
        )
    
    def forward(self, input):
        return self.main(input).view(-1, 1)
```

## 1.4 Training Best Practices

### Weight Initialization

```python
def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        nn.init.constant_(m.bias.data, 0)
```

### Label Smoothing

```python
# Instead of hard labels (0 and 1), use smoothed labels
real_labels = torch.ones(batch_size, 1) * 0.9  # Instead of 1.0
fake_labels = torch.zeros(batch_size, 1)       # Keep at 0.0
```

### Learning Rate Scheduling

```python
from torch.optim.lr_scheduler import LambdaLR

def get_lr_lambda(epoch):
    return 1.0 - max(0, epoch - 100) / 100.0  # Linear decay after 100 epochs

scheduler_G = LambdaLR(optimizer_G, lr_lambda=get_lr_lambda)
scheduler_D = LambdaLR(optimizer_D, lr_lambda=get_lr_lambda)
```

## 1.5 Common Problems and Solutions

### Mode Collapse

**Problem**: Generator produces limited variety of samples

**Solutions**:
- Mini-batch discrimination
- Unrolled GANs
- Wasserstein GAN (WGAN)
- Add noise to discriminator inputs

### Vanishing Gradients

**Problem**: Discriminator becomes too good, generator stops learning

**Solutions**:
- Use WGAN with gradient penalty
- Label smoothing
- Adjust training ratio (more G updates per D update)
- Use different learning rates

### Non-Convergence

**Problem**: Model oscillates, never stabilizes

**Solutions**:
- Reduce learning rate
- Use Adam with proper beta1 (0.5 instead of 0.9)
- Add instance noise
- Use spectral normalization

## 1.6 Evaluation Metrics

### Inception Score (IS)

```python
from torchvision.models import inception_v3
import torch.nn.functional as F

def calculate_inception_score(images, splits=10):
    model = inception_v3(pretrained=True, transform_input=False)
    model.eval()
    
    preds = []
    with torch.no_grad():
        for img in images:
            pred = F.softmax(model(img.unsqueeze(0)), dim=1)
            preds.append(pred.cpu().numpy())
    
    preds = np.concatenate(preds, 0)
    scores = []
    
    for i in range(splits):
        part = preds[i * (len(preds) // splits): (i + 1) * (len(preds) // splits)]
        kl = part * (np.log(part) - np.log(np.expand_dims(np.mean(part, 0), 0)))
        kl = np.mean(np.sum(kl, 1))
        scores.append(np.exp(kl))
    
    return np.mean(scores), np.std(scores)
```

### Fréchet Inception Distance (FID)

```python
from scipy.linalg import sqrtm
import numpy as np

def calculate_fid(real_features, fake_features):
    mu1, sigma1 = real_features.mean(axis=0), np.cov(real_features, rowvar=False)
    mu2, sigma2 = fake_features.mean(axis=0), np.cov(fake_features, rowvar=False)
    
    ssdiff = np.sum((mu1 - mu2) ** 2)
    covmean = sqrtm(sigma1.dot(sigma2))
    
    if np.iscomplexobj(covmean):
        covmean = covmean.real
    
    fid = ssdiff + np.trace(sigma1 + sigma2 - 2 * covmean)
    return fid
```

---

**Exercise 1.1**: Implement and train DCGAN on MNIST dataset.

**Exercise 1.2**: Experiment with different architectures and observe mode collapse.

**Exercise 1.3**: Calculate IS and FID for your generated samples.
