# Chapter 1: Foundations of Diffusion Models

> **Goal:** Understand the mathematical foundations of diffusion models, implement the forward and reverse processes, and build your first denoising model.

---

## 1.1 The Intuition Behind Diffusion

Diffusion models are inspired by a physical process: heat dissipation. If you place a hot object in a cold room, heat gradually spreads out until everything reaches equilibrium. The reverse — spontaneously concentrating heat — never happens naturally.

Diffusion models exploit this idea:
- **Forward:** Destroy structure by adding noise (like heat spreading)
- **Reverse:** Learn to undo the destruction (like a "reverse physics" simulation)

The key insight from the 2020 DDPM paper (Ho et al.) is that if you add noise slowly enough (in many small steps), a neural network can learn to reverse the process one step at a time.

---

## 1.2 The Forward Process (Adding Noise)

The forward process takes a data point \(x_0\) (e.g., an image) and gradually adds Gaussian noise over \(T\) timesteps:

\[
q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} \, x_{t-1}, \, \beta_t \mathbf{I})
\]

Where:
- \(x_0\) is the original image
- \(x_t\) is the noisy image at timestep \(t\)
- \(\beta_t\) is the noise level at timestep \(t\) (the "noise schedule")
- \(\mathcal{N}\) is a Gaussian (normal) distribution

### Key Property: The Reparameterization Trick

Thanks to properties of Gaussians, we can jump directly to any timestep:

\[
q(x_t | x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} \, x_0, \, (1 - \bar{\alpha}_t) \mathbf{I})
\]

Where:
- \(\alpha_t = 1 - \beta_t\)
- \(\bar{\alpha}_t = \alpha_1 \cdot \alpha_2 \cdot \ldots \cdot \alpha_t\)

This means: \(x_t = \sqrt{\bar{\alpha}_t} \, x_0 + \sqrt{1 - \bar{\alpha}_t} \, \epsilon\), where \(\epsilon \sim \mathcal{N}(0, \mathbf{I})\)

### Implementing the Forward Process

```python
import torch
import numpy as np

def linear_beta_schedule(T=1000, beta_start=1e-4, beta_end=0.02):
    """Create a linear noise schedule."""
    return torch.linspace(beta_start, beta_end, T)

def get_index_from_schedule(alphas_cumprod, t, x_shape):
    """Gather alpha_bar values for the given timesteps."""
    batch_size = t.shape[0]
    sqrt_alpha_bar = alphas_cumprod[t].sqrt()
    sqrt_one_minus_alpha_bar = (1 - alphas_cumprod[t]).sqrt()
    
    # Reshape for broadcasting: (batch, 1, 1, 1)
    sqrt_alpha_bar = sqrt_alpha_bar.reshape(batch_size, 1, 1, 1).expand(x_shape)
    sqrt_one_minus = sqrt_one_minus_alpha_bar.reshape(batch_size, 1, 1, 1).expand(x_shape)
    
    return sqrt_alpha_bar, sqrt_one_minus

def forward_diffusion(x_0, t, alphas_cumprod, noise=None):
    """
    Add noise to an image at timestep t.
    
    Args:
        x_0: Original clean image, shape (batch, C, H, W)
        t: Timestep(s), shape (batch,)
        alphas_cumprod: Precomputed cumulative product of (1 - beta)
        noise: Optional pre-generated noise
    
    Returns:
        x_t: Noisy image at timestep t
        noise: The noise that was added
    """
    if noise is None:
        noise = torch.randn_like(x_0)
    
    sqrt_alpha_bar, sqrt_one_minus = get_index_from_schedule(
        alphas_cumprod, t, x_0.shape
    )
    
    # x_t = sqrt(alpha_bar) * x_0 + sqrt(1 - alpha_bar) * noise
    x_t = sqrt_alpha_bar * x_0 + sqrt_one_minus * noise
    
    return x_t, noise
```

### Visualizing the Forward Process

```python
import matplotlib.pyplot as plt

# Create a sample image (or load one)
x_0 = torch.randn(1, 3, 64, 64)  # Replace with a real image

# Set up the noise schedule
T = 1000
betas = linear_beta_schedule(T)
alphas = 1 - betas
alphas_cumprod = torch.cumprod(alphas, dim=0)

# Visualize at different timesteps
timesteps = [0, 100, 300, 500, 700, 999]
fig, axes = plt.subplots(1, len(timesteps), figsize=(15, 3))

for i, t in enumerate(timesteps):
    x_t, _ = forward_diffusion(x_0, torch.tensor([t]), alphas_cumprod)
    img = x_t[0].permute(1, 2, 0).numpy()
    img = (img - img.min()) / (img.max() - img.min())  # Normalize for display
    axes[i].imshow(img)
    axes[i].set_title(f"t = {t}")
    axes[i].axis('off')

plt.suptitle("Forward Diffusion Process: Image → Noise")
plt.tight_layout()
plt.savefig("forward_process.png", dpi=150)
plt.show()
```

---

## 1.3 The Reverse Process (Removing Noise)

The reverse process is where the magic happens. We train a neural network \(\epsilon_\theta\) to **predict the noise** that was added at each timestep:

\[
\epsilon_\theta(x_t, t) \approx \epsilon
\]

Once the network can predict the noise, we can remove it:

\[
x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right) + \sigma_t z
\]

Where \(z \sim \mathcal{N}(0, \mathbf{I})\) is random noise (for stochasticity) and \(\sigma_t\) controls how much noise to add back.

### The Training Objective

The training loss is simple — just mean squared error between predicted and actual noise:

\[
\mathcal{L} = \mathbb{E}_{t, x_0, \epsilon} \left[ \| \epsilon - \epsilon_\theta(x_t, t) \|^2 \right]
\]

This is elegant: we don't need to know the true reverse distribution. We just train the network to predict noise, and the reverse process emerges naturally.

---

## 1.4 Building a Simple Denoiser

For educational purposes, let's start with a simple MLP (Multi-Layer Perceptron) denoiser. This won't produce great images, but it will help you understand the core mechanics.

```python
import torch
import torch.nn as nn

class SimpleDenoiser(nn.Module):
    """
    A simple MLP-based noise predictor.
    
    Input: Noisy image (flattened) + timestep embedding
    Output: Predicted noise (same shape as input)
    """
    
    def __init__(self, image_size=28*28, hidden_dim=512, time_embed_dim=64):
        super().__init__()
        
        # Time embedding: convert timestep to a learnable representation
        self.time_mlp = nn.Sequential(
            nn.Linear(1, time_embed_dim),
            nn.SiLU(),
            nn.Linear(time_embed_dim, time_embed_dim),
        )
        
        # Main network: takes noisy image + time embedding, predicts noise
        self.network = nn.Sequential(
            nn.Linear(image_size + time_embed_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, image_size),
        )
    
    def forward(self, x_t, t):
        """
        Predict the noise in x_t at timestep t.
        
        Args:
            x_t: Noisy image, shape (batch, image_size)
            t: Timestep, shape (batch, 1)
        
        Returns:
            Predicted noise, shape (batch, image_size)
        """
        # Encode timestep
        t_embed = self.time_mlp(t.float())
        
        # Concatenate image features with time embedding
        x = torch.cat([x_t, t_embed], dim=-1)
        
        # Predict noise
        return self.network(x)
```

---

## 1.5 Training the Model

```python
def train_denoiser(model, dataloader, T=1000, num_epochs=50, lr=1e-3):
    """
    Train the denoiser model.
    
    Training loop:
    1. Sample a random image x_0 from the dataset
    2. Sample a random timestep t
    3. Sample random noise epsilon
    4. Create noisy image x_t using the forward process
    5. Train the model to predict epsilon from (x_t, t)
    """
    betas = linear_beta_schedule(T).to(device)
    alphas = 1 - betas
    alphas_cumprod = torch.cumprod(alphas, dim=0)
    
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    
    for epoch in range(num_epochs):
        total_loss = 0
        
        for batch_idx, (images, _) in enumerate(dataloader):
            images = images.to(device)
            batch_size = images.shape[0]
            
            # Flatten images for MLP
            x_0 = images.view(batch_size, -1)
            
            # Step 1: Sample random timesteps
            t = torch.randint(0, T, (batch_size, 1)).to(device)
            
            # Step 2: Sample random noise
            noise = torch.randn_like(x_0)
            
            # Step 3: Create noisy images
            sqrt_alpha_bar = alphas_cumprod[t].sqrt().to(device)
            sqrt_one_minus = (1 - alphas_cumprod[t]).sqrt().to(device)
            x_t = sqrt_alpha_bar * x_0 + sqrt_one_minus * noise
            
            # Step 4: Predict noise
            predicted_noise = model(x_t, t)
            
            # Step 5: Compute loss and update
            loss = criterion(predicted_noise, noise)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}] Loss: {avg_loss:.6f}")
    
    return model
```

---

## 1.6 Sampling (Generating Images)

Once trained, we generate images by starting from pure noise and iteratively denoising:

```python
@torch.no_grad()
def sample(model, image_size=28*28, T=1000, batch_size=4):
    """
    Generate images by iteratively denoising random noise.
    
    Starting from x_T ~ N(0, I), we go:
    x_T -> x_{T-1} -> ... -> x_1 -> x_0
    """
    betas = linear_beta_schedule(T).to(device)
    alphas = 1 - betas
    alphas_cumprod = torch.cumprod(alphas, dim=0)
    
    model.eval()
    
    # Start from pure noise
    x = torch.randn(batch_size, image_size).to(device)
    
    for t in reversed(range(T)):
        t_batch = torch.full((batch_size, 1), t, device=device)
        
        # Predict noise
        predicted_noise = model(x, t_batch)
        
        # Compute x_{t-1} from x_t
        alpha = alphas[t]
        alpha_bar = alphas_cumprod[t]
        
        # Remove predicted noise
        x = (1 / alpha.sqrt()) * (x - (1 - alpha) / (1 - alpha_bar).sqrt() * predicted_noise)
        
        # Add noise (except at the last step)
        if t > 0:
            noise = torch.randn_like(x)
            sigma = (1 - alpha).sqrt()
            x = x + sigma * noise
    
    # Reshape to image format
    x = x.view(batch_size, 1, 28, 28)
    return x
```

---

## 1.7 Understanding the Noise Schedule

The noise schedule \(\beta_t\) determines how quickly noise is added. Common choices:

| Schedule | Formula | Characteristics |
|----------|---------|----------------|
| **Linear** | \(\beta_t = \beta_{start} + t \cdot (\beta_{end} - \beta_{start}) / T\) | Simple, widely used |
| **Cosine** | Based on cosine function | Better quality, smoother transitions |
| **Sigmoid** | Scaled sigmoid curve | Gradual at start and end |

```python
def cosine_beta_schedule(T=1000, s=0.008):
    """Cosine noise schedule (Nichol & Dhariwal, 2021)."""
    steps = torch.arange(T + 1, dtype=torch.float64)
    alpha_bar = torch.cos(((steps / T) + s) / (1 + s) * torch.pi * 0.5) ** 2
    alpha_bar = alpha_bar / alpha_bar[0]
    betas = 1 - (alpha_bar[1:] / alpha_bar[:-1])
    return torch.clamp(betas, 0, 0.999)
```

---

## 1.8 Key Takeaways

1. **Forward process:** Add Gaussian noise in small steps until data becomes pure noise
2. **Reverse process:** Train a network to predict and remove noise at each step
3. **Training objective:** Simple MSE between predicted and actual noise
4. **Sampling:** Start from noise, iteratively denoise for T steps
5. **Noise schedule matters:** Cosine generally outperforms linear
6. **MLP denoisers work** but produce blurry results — we need convolutions for sharp images

---

## 1.9 Limitations of This Approach

The simple MLP denoiser has problems:
- It treats each pixel independently (no spatial awareness)
- It's very slow (1000 forward passes per image)
- It only works on small, low-resolution images

**Solution:** In Chapter 2, we'll use U-Net (a convolutional architecture) as the denoiser, add classifier-free guidance, and explore latent diffusion for practical image generation.

---

## Exercises

1. **Forward process visualization:** Load a real image and visualize it at timesteps 0, 200, 400, 600, 800, 999
2. **Train the MLP denoiser** on MNIST and generate digits — observe the quality
3. **Compare noise schedules:** Train with linear and cosine schedules, compare FID scores
4. **Implement DDIM sampling:** Reduce the number of sampling steps from 1000 to 50 while maintaining quality
5. **Experiment with hidden dimensions:** How does model size affect generation quality?

---

*Next: [Chapter 2 — Advanced Diffusion Architectures](chapter_2_advanced.md)*
