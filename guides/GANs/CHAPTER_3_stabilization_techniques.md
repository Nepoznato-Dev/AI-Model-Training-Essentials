# Chapter 3: GAN Stabilization Techniques

## 3.1 Introduction to Training Stability

GAN training is notoriously unstable due to the adversarial nature of the generator-discriminator game. This chapter covers advanced techniques for stabilizing GAN training and improving convergence.

### Sources of Instability

1. **Non-convergence**: Oscillating parameters without reaching equilibrium
2. **Mode collapse**: Generator produces limited variety
3. **Vanishing gradients**: Discriminator becomes too accurate
4. **Sensitivity to hyperparameters**: Small changes cause large effects

---

## 3.2 Gradient Penalty Deep Dive

### Why Gradient Penalty Works

Gradient penalty enforces the Lipschitz constraint more smoothly than weight clipping:

```python
import torch
import torch.nn as nn


class ImprovedGradientPenalty(nn.Module):
    """Improved gradient penalty calculation with better numerical stability"""
    
    def __init__(self, lambda_gp=10.0, epsilon=1e-6):
        super().__init__()
        self.lambda_gp = lambda_gp
        self.epsilon = epsilon
    
    def forward(self, discriminator, real_data, fake_data):
        batch_size = real_data.size(0)
        
        # Random interpolation coefficient
        alpha = torch.rand(batch_size, 1, 1, 1, device=real_data.device)
        
        # Interpolate between real and fake
        interpolates = (alpha * real_data + (1 - alpha) * fake_data).requires_grad_(True)
        
        # Get discriminator output
        d_interpolates = discriminator(interpolates)
        
        # Compute gradients with improved numerical stability
        grad_outputs = torch.ones_like(d_interpolates)
        gradients = torch.autograd.grad(
            outputs=d_interpolates,
            inputs=interpolates,
            grad_outputs=grad_outputs,
            create_graph=True,
            retain_graph=True,
            only_inputs=True
        )[0]
        
        # Reshape gradients
        gradients = gradients.view(batch_size, -1)
        
        # Calculate gradient norm with epsilon for stability
        gradient_norm = torch.sqrt(torch.sum(gradients ** 2, dim=1) + self.epsilon)
        
        # Penalty: encourage gradient norm to be close to 1
        gradient_penalty = ((gradient_norm - 1) ** 2).mean()
        
        return self.lambda_gp * gradient_penalty
```

### Alternative: R1 Regularization

R1 regularization penalizes the gradient of the discriminator on real data only:

```python
def r1_regularization(discriminator, real_data, gamma=10.0):
    """
    R1 regularization: penalize ||∇_x D(x)||² on real data
    
    More efficient than full gradient penalty
    """
    real_data.requires_grad_(True)
    
    d_real = discriminator(real_data)
    
    # Compute gradient on real data only
    grad_real = torch.autograd.grad(
        outputs=d_real.sum(),
        inputs=real_data,
        create_graph=True,
        retain_graph=True
    )[0]
    
    # Calculate penalty
    r1_penalty = torch.sum(grad_real ** 2)
    
    return gamma * r1_penalty
```

### Comparison: GP vs R1

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| Weight Clipping | Simple | Can cause optimization issues | Basic WGAN |
| Gradient Penalty | Stable, smooth | Computationally expensive | High-quality generation |
| R1 Regularization | Efficient, stable | Less theoretical guarantee | Large-scale training |

---

## 3.3 Spectral Normalization

### Theory

Spectral normalization constrains the Lipschitz constant by normalizing weight matrices by their spectral norm:

```
W_SN = W / σ(W)
```

Where σ(W) is the largest singular value of W.

### Implementation with Power Iteration

```python
class SpectralNormConv2d(nn.Module):
    """Conv2d layer with spectral normalization"""
    
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        super().__init__()
        
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.u = nn.Parameter(torch.randn(1, out_channels), requires_grad=False)
        self.n_power_iterations = 1
    
    def _power_iteration(self, weight, n_iterations):
        """Estimate largest singular value using power iteration"""
        v = torch.randn(weight.size(1), 1, device=weight.device)
        
        for _ in range(n_iterations):
            # u = Wv / ||Wv||
            u = torch.mv(weight.view(weight.size(0), -1), v)
            u = u / (u.norm() + 1e-8)
            
            # v = W^Tu / ||W^Tu||
            v = torch.mv(weight.view(weight.size(0), -1).t(), u)
            v = v / (v.norm() + 1e-8)
        
        # σ = u^TWv
        sigma = torch.dot(u, torch.mv(weight.view(weight.size(0), -1), v))
        
        return sigma, u, v
    
    def forward(self, x):
        weight = self.conv.weight
        
        if self.training:
            sigma, self.u.data, v = self._power_iteration(
                weight.view(weight.size(0), -1), 
                self.n_power_iterations
            )
        else:
            sigma, _, _ = self._power_iteration(
                weight.view(weight.size(0), -1), 
                self.n_power_iterations
            )
        
        # Normalize weight
        weight_sn = weight / (sigma + 1e-8)
        
        # Perform convolution with normalized weight
        return nn.functional.conv2d(
            x, weight_sn, self.conv.bias,
            self.conv.stride, self.conv.padding
        )


class SpectralNormLinear(nn.Module):
    """Linear layer with spectral normalization"""
    
    def __init__(self, in_features, out_features):
        super().__init__()
        
        self.linear = nn.Linear(in_features, out_features)
        self.u = nn.Parameter(torch.randn(1, out_features), requires_grad=False)
    
    def forward(self, x):
        weight = self.linear.weight
        
        # Power iteration
        v = torch.randn(weight.size(1), 1, device=weight.device)
        for _ in range(1):
            u = torch.mv(weight, v)
            u = u / (u.norm() + 1e-8)
            v = torch.mv(weight.t(), u)
            v = v / (v.norm() + 1e-8)
        
        sigma = torch.dot(u, torch.mv(weight, v))
        
        # Normalize
        weight_sn = weight / (sigma + 1e-8)
        
        return nn.functional.linear(x, weight_sn, self.linear.bias)
```

### Using PyTorch's Built-in Spectral Norm

```python
from torch.nn.utils import spectral_norm

# Apply to any layer
conv = spectral_norm(nn.Conv2d(3, 64, 3))
linear = spectral_norm(nn.Linear(100, 512))

# Or apply to entire network
discriminator = nn.Sequential(
    spectral_norm(nn.Conv2d(3, 64, 4, 2, 1)),
    nn.LeakyReLU(0.2),
    spectral_norm(nn.Conv2d(64, 128, 4, 2, 1)),
    nn.LeakyReLU(0.2),
    # ...
)
```

---

## 3.4 Architecture Improvements

### Self-Attention for GANs

Self-attention helps capture long-range dependencies:

```python
class SelfAttention(nn.Module):
    """Self-attention layer for GANs"""
    
    def __init__(self, in_channels):
        super().__init__()
        
        self.query_conv = nn.Conv2d(in_channels, in_channels // 8, kernel_size=1)
        self.key_conv = nn.Conv2d(in_channels, in_channels // 8, kernel_size=1)
        self.value_conv = nn.Conv2d(in_channels, in_channels, kernel_size=1)
        
        self.gamma = nn.Parameter(torch.zeros(1))  # Learnable scaling
        self.softmax = nn.Softmax(dim=-1)
    
    def forward(self, x):
        batch_size, C, width, height = x.size()
        
        # Compute Q, K, V
        query = self.query_conv(x).view(batch_size, -1, width * height).permute(0, 2, 1)
        key = self.key_conv(x).view(batch_size, -1, width * height)
        value = self.value_conv(x).view(batch_size, -1, width * height)
        
        # Attention map
        attention = torch.bmm(query, key)
        attention = self.softmax(attention)
        
        # Apply attention
        out = torch.bmm(value, attention.permute(0, 2, 1))
        out = out.view(batch_size, C, width, height)
        
        # Residual connection with learnable scaling
        out = self.gamma * out + x
        
        return out


class SAGAN_Discriminator(nn.Module):
    """S3GAN discriminator with self-attention"""
    
    def __init__(self, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.network = nn.Sequential(
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            # Self-attention at intermediate resolution
            SelfAttention(feature_dim * 2),
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 8),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0),
        )
    
    def forward(self, x):
        return self.network(x).view(-1, 1)
```

### Progressive Growing

Progressive growing starts with low resolution and gradually increases:

```python
class ProgressiveGenerator(nn.Module):
    """Progressive growing generator"""
    
    def __init__(self, latent_dim=512, img_channels=3):
        super().__init__()
        
        # Initial 4x4 block
        self.initial = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, 512, 4, 1, 0),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True)
        )
        
        # Progressive blocks
        self.to_rgb = nn.ModuleList([
            nn.Conv2d(512, img_channels, 1),  # 4x4
            nn.Conv2d(512, img_channels, 1),  # 8x8
            nn.Conv2d(512, img_channels, 1),  # 16x16
            nn.Conv2d(512, img_channels, 1),  # 32x32
            nn.Conv2d(512, img_channels, 1),  # 64x64
        ])
        
        self.blocks = nn.ModuleList([
            nn.Sequential(
                nn.ConvTranspose2d(512, 512, 4, 2, 1),
                nn.BatchNorm2d(512),
                nn.ReLU(inplace=True),
            ),
            nn.Sequential(
                nn.ConvTranspose2d(512, 512, 4, 2, 1),
                nn.BatchNorm2d(512),
                nn.ReLU(inplace=True),
            ),
            nn.Sequential(
                nn.ConvTranspose2d(512, 512, 4, 2, 1),
                nn.BatchNorm2d(512),
                nn.ReLU(inplace=True),
            ),
            nn.Sequential(
                nn.ConvTranspose2d(512, 512, 4, 2, 1),
                nn.BatchNorm2d(512),
                nn.ReLU(inplace=True),
            ),
        ])
        
        self.current_resolution = 0  # Start at 4x4
    
    def set_resolution(self, resolution_idx):
        """Set current resolution level"""
        self.current_resolution = resolution_idx
    
    def forward(self, z):
        x = self.initial(z.unsqueeze(2).unsqueeze(3))
        
        # Generate up to current resolution
        for i in range(self.current_resolution):
            x = self.blocks[i](x)
        
        # Output RGB
        rgb = self.to_rgb[self.current_resolution](x)
        
        return torch.tanh(rgb)


class ProgressiveTrainer:
    """Manages progressive growing schedule"""
    
    def __init__(self, generator, total_phases=5, images_per_phase=500000):
        self.generator = generator
        self.total_phases = total_phases
        self.images_per_phase = images_per_phase
        self.current_phase = 0
        self.images_generated = 0
    
    def step(self, batch_size):
        """Update phase based on images generated"""
        self.images_generated += batch_size
        
        if self.images_generated >= self.images_per_phase and \
           self.current_phase < self.total_phases - 1:
            self.current_phase += 1
            self.images_generated = 0
            self.generator.set_resolution(self.current_phase)
            print(f"Progressed to resolution phase {self.current_phase}")
```

---

## 3.5 Mini-Batch Discrimination

Mini-batch discrimination helps prevent mode collapse by allowing the discriminator to see multiple samples:

```python
class MiniBatchDiscrimination(nn.Module):
    """Mini-batch discrimination layer"""
    
    def __init__(self, in_features, out_features=50, kernel_dims=50):
        super().__init__()
        
        self.T = nn.Parameter(torch.randn(in_features, out_features, kernel_dims))
        self.out_features = out_features
    
    def forward(self, x):
        # x: (batch, in_features)
        batch_size = x.size(0)
        
        # Compute activation tensor
        # M_i = sum_j |x_i * T - c_j * T|
        activation = torch.bmm(x.unsqueeze(1), self.T.unsqueeze(0).expand(batch_size, -1, -1, -1))
        activation = activation.squeeze(1)  # (batch, out_features, kernel_dims)
        
        # Compute distances between all pairs
        activation_expanded = activation.unsqueeze(0).expand(batch_size, -1, -1, -1)
        activation_tiled = activation.unsqueeze(1).expand(-1, batch_size, -1, -1)
        
        distances = torch.abs(activation_expanded - activation_tiled)
        distances = distances.sum(3)  # Sum over kernel dimension
        
        # Sum distances to other samples
        minibatch_features = distances.sum(1)  # (batch, out_features)
        
        # Concatenate with original features
        return torch.cat([x, minibatch_features], dim=1)


class DCGAN_with_MBD(nn.Module):
    """DCGAN discriminator with mini-batch discrimination"""
    
    def __init__(self, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
        )
        
        # Flatten and apply MBD
        self.mbd = MiniBatchDiscrimination(feature_dim * 4 * 4 * 4)
        
        self.classifier = nn.Sequential(
            nn.Linear(feature_dim * 4 * 4 * 4 + 50, 1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(1024, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.mbd(x)
        return self.classifier(x).view(-1, 1)
```

---

## 3.6 Learning Rate Scheduling for GANs

### Discriminative Learning Rates

```python
def create_gan_optimizers(generator, discriminator, lr_g=0.0001, lr_d=0.0004):
    """Create optimizers with different learning rates (TTUR)"""
    
    opt_g = torch.optim.Adam(
        generator.parameters(),
        lr=lr_g,
        betas=(0.0, 0.9)  # Lower momentum often works better
    )
    
    opt_d = torch.optim.Adam(
        discriminator.parameters(),
        lr=lr_d,
        betas=(0.0, 0.9)
    )
    
    return opt_g, opt_d
```

### Learning Rate Decay

```python
class LinearLRFade:
    """Linearly fade learning rate to zero"""
    
    def __init__(self, optimizer, start_epoch, end_epoch, initial_lr):
        self.optimizer = optimizer
        self.start_epoch = start_epoch
        self.end_epoch = end_epoch
        self.initial_lr = initial_lr
    
    def step(self, epoch):
        if epoch < self.start_epoch:
            lr = self.initial_lr
        elif epoch > self.end_epoch:
            lr = 0.0
        else:
            progress = (epoch - self.start_epoch) / (self.end_epoch - self.start_epoch)
            lr = self.initial_lr * (1 - progress)
        
        for param_group in self.optimizer.param_groups:
            param_group['lr'] = lr
        
        return lr
```

---

## 3.7 Monitoring and Debugging

### Metrics to Track

```python
class GANMonitor:
    """Monitor GAN training metrics"""
    
    def __init__(self):
        self.metrics = {
            'd_loss': [],
            'g_loss': [],
            'd_real_scores': [],
            'd_fake_scores': [],
            'gradient_norms': []
        }
    
    def update(self, d_loss, g_loss, d_real, d_fake, model):
        self.metrics['d_loss'].append(d_loss)
        self.metrics['g_loss'].append(g_loss)
        self.metrics['d_real_scores'].append(d_real.mean().item())
        self.metrics['d_fake_scores'].append(d_fake.mean().item())
        
        # Calculate gradient norms
        grad_norm = 0
        for param in model.parameters():
            if param.grad is not None:
                grad_norm += param.grad.data.norm(2).item() ** 2
        self.metrics['gradient_norms'].append(grad_norm ** 0.5)
    
    def check_mode_collapse(self, threshold=0.1):
        """Detect potential mode collapse"""
        if len(self.metrics['d_fake_scores']) < 100:
            return False
        
        recent = self.metrics['d_fake_scores'][-100:]
        variance = np.var(recent)
        
        return variance < threshold
    
    def plot_metrics(self):
        """Plot training metrics"""
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Losses
        axes[0, 0].plot(self.metrics['d_loss'], label='D Loss')
        axes[0, 0].plot(self.metrics['g_loss'], label='G Loss')
        axes[0, 0].legend()
        axes[0, 0].set_title('Losses')
        
        # Scores
        axes[0, 1].plot(self.metrics['d_real_scores'], label='Real Scores')
        axes[0, 1].plot(self.metrics['d_fake_scores'], label='Fake Scores')
        axes[0, 1].legend()
        axes[0, 1].set_title('Discriminator Scores')
        
        # Gradient norms
        axes[1, 0].plot(self.metrics['gradient_norms'])
        axes[1, 0].set_title('Gradient Norms')
        
        # Score difference
        diff = [r - f for r, f in zip(self.metrics['d_real_scores'], 
                                       self.metrics['d_fake_scores'])]
        axes[1, 1].plot(diff)
        axes[1, 1].set_title('Real - Fake Score Difference')
        
        plt.tight_layout()
        plt.savefig('gan_training_metrics.png')
```

---

## Exercises

### Exercise 3.1: Compare Stabilization Methods
Train the same GAN architecture with: (1) vanilla, (2) WGAN-GP, (3) spectral normalization, (4) R1 regularization. Compare stability and quality.

### Exercise 3.2: Implement Self-Attention
Add self-attention to a DCGAN discriminator. Does it improve the quality of generated images?

### Exercise 3.3: Progressive Growing
Implement progressive growing for a GAN. Start at 4x4 and progressively grow to 64x64.

### Exercise 3.4: Mode Collapse Detection
Build a metric to detect mode collapse during training. Test it on a GAN that you intentionally make collapse.

### Exercise 3.5: Learning Rate Experiments
Experiment with different learning rate schedules (constant, decay, TTUR). Which works best for your dataset?

---

## Summary

This chapter covered stabilization techniques for GAN training:

1. **Gradient Penalty**: Enforce Lipschitz constraint smoothly
2. **Spectral Normalization**: Constrain weight matrix norms
3. **Architecture Improvements**: Self-attention, progressive growing
4. **Mini-Batch Discrimination**: Prevent mode collapse
5. **Learning Rate Strategies**: TTUR, scheduling, decay
6. **Monitoring**: Track metrics and detect issues early

Mastering these techniques is essential for training high-quality GANs that converge reliably and produce diverse, realistic samples.

---

**Next**: Chapter 4 will explore practical applications including image-to-image translation, super-resolution, and data augmentation.
