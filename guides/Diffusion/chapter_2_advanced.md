# Chapter 2: Advanced Diffusion Architectures

> **Goal:** Build production-quality diffusion models using U-Net denoisers, classifier-free guidance, latent diffusion, and fine-tuning techniques.

---

## 2.1 From MLP to U-Net: The Right Denoiser

The simple MLP denoiser from Chapter 1 treats each pixel independently. Real images have spatial structure — edges, textures, shapes — that require **convolutional** processing.

The **U-Net** (Ronneberger et al., 2015) is the standard denoiser architecture for diffusion models. It's an encoder-decoder network with skip connections that preserves spatial detail:

```
Input (64x64)
    │
    ▼
  Encoder (downsampling)
    │  64→128→256→512
    │  64→32→16→8
    │
    ▼
  Bottleneck (256 features at 8x8)
    │
    ▼
  Decoder (upsampling)
    │  512→256→128→64
    │  8→16→32→64
    │
    ▼
Output (64x64) — predicted noise
```

### Why U-Net Works Well

1. **Encoder** captures high-level semantic information (what objects are present)
2. **Decoder** reconstructs fine spatial details (where exactly the edges are)
3. **Skip connections** pass spatial information directly from encoder to decoder
4. **Attention layers** (in modern variants) capture long-range dependencies

### U-Net Building Block: Residual + Attention

```python
import torch
import torch.nn as nn
import math

class SinusoidalPositionEmbedding(nn.Module):
    """Encode timestep as sinusoidal features (like Transformer position encoding)."""
    
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
    
    def forward(self, t):
        device = t.device
        half_dim = self.dim // 2
        emb = math.log(10000) / (half_dim - 1)
        emb = torch.exp(torch.arange(half_dim, device=device) * -emb)
        emb = t.float().unsqueeze(1) * emb.unsqueeze(0)
        emb = torch.cat([emb.sin(), emb.cos()], dim=-1)
        return emb


class ResidualBlock(nn.Module):
    """Convolutional residual block with time conditioning."""
    
    def __init__(self, in_channels, out_channels, time_dim):
        super().__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, padding=1),
            nn.GroupNorm(8, out_channels),
            nn.SiLU(),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(out_channels, out_channels, 3, padding=1),
            nn.GroupNorm(8, out_channels),
            nn.SiLU(),
        )
        # Project time embedding to feature dimension
        self.time_mlp = nn.Sequential(
            nn.SiLU(),
            nn.Linear(time_dim, out_channels),
        )
        # Shortcut connection for dimension changes
        self.shortcut = nn.Conv2d(in_channels, out_channels, 1) if in_channels != out_channels else nn.Identity()
    
    def forward(self, x, t_embed):
        h = self.conv1(x)
        # Add time conditioning
        h = h + self.time_mlp(t_embed).unsqueeze(-1).unsqueeze(-1)
        h = self.conv2(h)
        return h + self.shortcut(x)
```

---

## 2.2 Classifier-Free Guidance (CFG)

CFG is the most important trick in modern diffusion models. It lets you control generation with text prompts.

### How CFG Works

During training, we randomly drop the text condition 10-20% of the time. This means the model learns both:
- **Conditional prediction:** \(\epsilon_\theta(x_t, t, c)\) — "denoise given this text prompt"
- **Unconditional prediction:** \(\epsilon_\theta(x_t, t, \emptyset)\) — "denoise without any prompt"

At inference time, we combine them:

\[
\hat{\epsilon} = \epsilon_\theta(x_t, t, \emptyset) + w \cdot (\epsilon_\theta(x_t, t, c) - \epsilon_\theta(x_t, t, \emptyset))
\]

Where \(w\) is the **guidance scale** (typically 5-15):
- \(w = 1\): No guidance (standard conditional generation)
- \(w = 7.5\): Balanced quality and prompt adherence
- \(w = 15\): Strong prompt adherence but lower diversity

```python
@torch.no_grad()
def sample_with_cfg(model, x_T, prompt_embed, uncond_embed, T=1000, guidance_scale=7.5):
    """
    Sample with classifier-free guidance.
    
    Args:
        model: The noise prediction network
        x_T: Starting noise
        prompt_embed: Text embedding for the prompt
        uncond_embed: Text embedding for empty/unconditional
        guidance_scale: How strongly to follow the prompt
    """
    x = x_T
    
    for t in reversed(range(T)):
        # Predict noise with condition
        noise_cond = model(x, t, prompt_embed)
        # Predict noise without condition
        noise_uncond = model(x, t, uncond_embed)
        # Combine with CFG
        noise_pred = noise_uncond + guidance_scale * (noise_cond - noise_uncond)
        # Denoise step (simplified)
        x = denoise_step(x, noise_pred, t)
    
    return x
```

---

## 2.3 Latent Diffusion: Working in Compressed Space

Pixel-space diffusion is impractical for high-resolution images. **Latent Diffusion Models (LDMs)** solve this by:

1. Training a VAE (Variational Autoencoder) to compress images
2. Running the diffusion process in the compressed latent space
3. Decoding the final latent back to pixel space

```
Image (256x256x3) → VAE Encoder → Latent (32x32x4) → Diffusion → Denoised Latent → VAE Decoder → Generated Image
```

### Why This Matters

| Approach | Image Size | Latent Size | Speedup |
|----------|-----------|-------------|---------|
| Pixel-space | 256×256×3 = 196,608 values | — | 1x (baseline) |
| Latent-space | — | 32×32×4 = 4,096 values | ~48x faster |

### Using Stable Diffusion (HuggingFace)

```python
from diffusers import StableDiffusionPipeline
import torch

# Load pre-trained Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    safety_checker=None,
)
pipe = pipe.to("cuda")

# Enable memory optimizations
pipe.enable_attention_slicing()
pipe.enable_vae_slicing()

# Generate an image
image = pipe(
    prompt="a beautiful sunset over mountains, oil painting style",
    negative_prompt="blurry, low quality, distorted",
    num_inference_steps=30,
    guidance_scale=7.5,
    generator=torch.Generator().manual_seed(42),
).images[0]

image.save("sunset.png")
print("Image generated!")
```

---

## 2.4 Text Conditioning: Cross-Attention

How does the model "see" the text prompt? Through **cross-attention** layers in the U-Net:

1. Text is encoded by a text encoder (CLIP) into embeddings
2. At each U-Net block, cross-attention lets image features "look at" text features
3. The model learns which image regions correspond to which words

```python
class CrossAttentionBlock(nn.Module):
    """Cross-attention between image features and text embeddings."""
    
    def __init__(self, image_channels, text_dim, num_heads=8):
        super().__init__()
        self.norm_x = nn.LayerNorm(image_channels)
        self.norm_c = nn.LayerNorm(text_dim)
        self.attn = nn.MultiheadAttention(image_channels, num_heads, batch_first=True)
        self.proj = nn.Linear(image_channels, image_channels)
    
    def forward(self, x, text_embed):
        """
        Args:
            x: Image features, shape (B, C, H, W)
            text_embed: Text embeddings, shape (B, seq_len, text_dim)
        """
        B, C, H, W = x.shape
        
        # Reshape image features: (B, H*W, C)
        x_flat = x.permute(0, 2, 3, 1).reshape(B, H * W, C)
        
        # Normalize
        x_norm = self.norm_x(x_flat)
        c_norm = self.norm_c(text_embed)
        
        # Cross-attention: image features attend to text
        attn_out, _ = self.attn(x_norm, c_norm, c_norm)
        
        # Residual connection + reshape back
        x_out = x_flat + self.proj(attn_out)
        x_out = x_out.reshape(B, H, W, C).permute(0, 3, 1, 2)
        
        return x_out
```

---

## 2.5 Fine-Tuning: DreamBooth and LoRA

Training Stable Diffusion from scratch costs ~$160,000 in GPU time. Fine-tuning techniques make it accessible:

### DreamBooth

Fine-tunes the entire model on 3-5 images of a specific subject:

```python
from diffusers import StableDiffusionPipeline
import torch

# Load base model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)

# After DreamBooth fine-tuning (using the diffusers training script):
# pipe = StableDiffusionPipeline.from_pretrained("path/to/dreambooth-model")

# Generate images of your subject
image = pipe("a photo of sks dog in a basket").images[0]
```

### LoRA (Low-Rank Adaptation)

A more efficient approach — only trains small "adapter" matrices:

| Method | Trainable Parameters | VRAM Needed | Quality |
|--------|---------------------|-------------|---------|
| Full fine-tuning | ~860M | 40GB+ | Best |
| DreamBooth | ~860M | 16GB+ | Great |
| LoRA | ~1-4M | 8GB+ | Very Good |

```python
from diffusers import StableDiffusionPipeline
import torch

# Load base model + LoRA weights
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)
pipe.load_lora_weights("path/to/lora_weights")

# Generate with LoRA-enhanced model
image = pipe("your prompt here").images[0]
```

---

## 2.6 Faster Sampling: DDIM and DPM-Solver

Standard DDPM requires 1000 sampling steps. Faster samplers reduce this dramatically:

| Sampler | Steps | Quality | Speed |
|---------|-------|---------|-------|
| DDPM | 1000 | Baseline | Slow |
| DDIM | 50 | ~Same | 20x faster |
| DPM-Solver++ | 20 | ~Same | 50x faster |
| Euler | 25-30 | Good | 33x faster |

```python
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Only 20 steps needed with DPM-Solver++!
image = pipe("a cat", num_inference_steps=20).images[0]
```

---

## 2.7 Practical Tips for Production

### Memory Optimization

```python
# For GPUs with limited VRAM
pipe.enable_attention_slicing()     # Process attention in chunks
pipe.enable_vae_slicing()           # Process VAE in batches
pipe.enable_model_cpu_offload()     # Move model parts to CPU when not in use
```

### Batch Generation

```python
# Generate multiple images at once
prompts = ["a cat", "a dog", "a bird"]
images = pipe(prompts, num_images_per_prompt=4).images
# Returns 12 images total (3 prompts x 4 variations)
```

### Image-to-Image

```python
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

pipe = StableDiffusionImg2ImgPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Transform an existing image
init_image = Image.open("input.png").resize((512, 512))
result = pipe(
    prompt="oil painting of the same scene",
    image=init_image,
    strength=0.75,  # How much to change (0.0-1.0)
).images[0]
```

---

## 2.8 Diffusion vs GANs: When to Use What

| Criterion | Diffusion Models | GANs |
|-----------|-----------------|------|
| Training stability | Very stable | Unstable (mode collapse) |
| Generation quality | Excellent | Excellent |
| Generation speed | Slow (many steps) | Fast (single forward pass) |
| Diversity | High | Can suffer from mode collapse |
| Controllability | Excellent (CFG) | Moderate |
| Memory usage | High | Moderate |
| Best for | High-quality generation, editing | Real-time generation |

---

## 2.9 Key Takeaways

1. **U-Net** is the standard denoiser — convolutions + skip connections + time conditioning
2. **Classifier-Free Guidance** enables text-controlled generation
3. **Latent Diffusion** (Stable Diffusion) works in compressed space for efficiency
4. **Cross-attention** connects text embeddings to image features
5. **LoRA/DreamBooth** make fine-tuning affordable
6. **DPM-Solver++** reduces sampling from 1000 to 20 steps
7. **Diffusion > GANs** for quality and stability; **GANs > Diffusion** for speed

---

## Exercises

1. **Build a mini U-Net:** Implement a U-Net with 3 encoder levels and train it as a denoiser on CIFAR-10
2. **Implement CFG:** Train with conditional dropout and implement the CFG sampling formula
3. **Use Stable Diffusion:** Generate 10 images with different prompts and CFG scales (1, 5, 10, 15)
4. **Fine-tune with LoRA:** Use 5 images of a specific style/object and fine-tune a LoRA adapter
5. **Compare samplers:** Generate the same image with DDPM (1000 steps), DDIM (50 steps), and DPM-Solver (20 steps)
6. **Image-to-image:** Take a photo and transform it into different artistic styles using img2img with varying strength values

---

*Previous: [Chapter 1 — Foundations of Diffusion Models](chapter_1_foundations.md)*
