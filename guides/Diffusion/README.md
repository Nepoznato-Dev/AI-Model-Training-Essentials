# Diffusion Models

> **Welcome to the Diffusion Models guide!** Learn how AI generates stunning images by gradually removing noise — like a sculptor revealing a statue from a block of marble.

---

## What Are Diffusion Models?

Imagine you have a blurry, noisy image that looks like TV static. Now imagine an AI that can slowly, step by step, remove that noise until a clear, beautiful image emerges. That's a **diffusion model**.

Diffusion models work in two phases:

1. **Forward process (destroy):** Gradually add random noise to an image until it's pure static
2. **Reverse process (create):** Learn to reverse this process — starting from noise, generate a clean image

This is fundamentally different from GANs (which pit two networks against each other). Diffusion models are more stable to train and produce higher-quality results, which is why they power tools like DALL-E, Stable Diffusion, and Midjourney.

### Analogy

Think of diffusion models like **sculpting with noise**:
- You start with a block of marble (pure noise)
- Each step, you chip away a little noise (the model predicts what to remove)
- After many steps, a clear image emerges (the sculpture is revealed)

---

## Why Are Diffusion Models Important?

| Application | Example |
|-------------|---------|
| Text-to-Image | Generate art from text descriptions (DALL-E, Stable Diffusion) |
| Image Editing | Modify specific parts of images while keeping the rest |
| Video Generation | Create short video clips from text prompts |
| Super-Resolution | Enhance low-resolution images |
| Inpainting | Fill in missing parts of images |
| Drug Discovery | Generate molecular structures with desired properties |

---

## Guide Structure

This guide is organized into **2 chapters**, each building on the previous:

| Chapter | Title | What You'll Learn |
|---------|-------|-------------------|
| 1 | [Foundations of Diffusion Models](chapter_1_foundations.md) | The math behind diffusion, DDPM, forward/reverse process, noise schedules |
| 2 | [Advanced Diffusion Architectures](chapter_2_advanced.md) | U-Net denoisers, classifier-free guidance, latent diffusion, Stable Diffusion |

---

## Prerequisites

Before starting, you should be comfortable with:

| Topic | Recommended Resource |
|-------|---------------------|
| Python & PyTorch | Basic tensor operations, training loops |
| CNNs | Our [CNNs Guide](../CNNs/README.md) — understanding convolutions is essential |
| Probability | Gaussian distributions, sampling |
| GANs (helpful) | Our [GANs Guide](../GANs/README.md) — for comparison with diffusion |

---

## Hardware Requirements

| Setup | Details |
|-------|---------|
| **Minimum** | CPU with 8GB RAM (slow but educational) |
| **Recommended** | GPU with 8GB+ VRAM (NVIDIA RTX 3060 or better) |
| **Ideal** | GPU with 12GB+ VRAM for training, 8GB+ for inference |

> **Note:** You can use pre-trained models for inference on modest hardware. Training from scratch requires significant GPU resources.

---

## Quick Start

```bash
# Install dependencies
pip install torch torchvision diffusers transformers accelerate

# Verify installation
python -c "import diffusers; print(f'Diffusers {diffusers.__version__} ready!')"

# Run a pre-trained model (Stable Diffusion)
python -c "
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5')
image = pipe('a cat sitting on a windowsill').images[0]
image.save('cat.png')
print('Image generated!')
"
```

---

## Key Concepts Glossary

| Term | Definition |
|------|-----------|
| **Forward Process** | Gradually adding Gaussian noise to data over T timesteps |
| **Reverse Process** | Learning to denoise step by step, from noise back to data |
| **Noise Schedule** | How much noise is added at each timestep (linear, cosine, etc.) |
| **DDPM** | Denoising Diffusion Probabilistic Models — the foundational algorithm |
| **U-Net** | Neural network architecture used as the denoiser (encoder-decoder with skip connections) |
| **Classifier-Free Guidance (CFG)** | Technique to control generation quality by conditioning on text prompts |
| **Latent Diffusion** | Running diffusion in a compressed latent space (much faster than pixel space) |
| **Timestep Embedding** | Encoding the current timestep so the model knows how much noise to remove |
| **Sampling** | The process of generating images by iteratively denoising random noise |
| **DDIM** | A faster sampling method that skips timesteps (fewer steps needed) |
| **VAE** | Variational Autoencoder — used in latent diffusion to compress images |
| **Cross-Attention** | Mechanism that connects text embeddings to image features |

---

## Best Practices

1. **Start with pre-trained models** — Don't train from scratch; use HuggingFace diffusers
2. **Use DDIM sampling** — 50 steps instead of 1000 for much faster generation
3. **Tune CFG scale** — Higher values = more prompt adherence but less diversity
4. **Work in latent space** — Latent diffusion is 10-100x faster than pixel-space
5. **Use mixed precision** — `torch.float16` halves memory usage with minimal quality loss
6. **Batch your generations** — Generate multiple images at once for efficiency
7. **Monitor GPU memory** — Use `torch.cuda.empty_cache()` between large generations

---

## Common Pitfalls

1. **Training from scratch** — Requires massive compute; start with fine-tuning instead
2. **Too many timesteps** — 1000 steps is for training; use 20-50 for inference with DDIM
3. **Ignoring the noise schedule** — The choice of schedule (linear vs cosine) greatly affects quality
4. **CFG scale too high** — Produces oversaturated, artifact-heavy images
5. **Not using a VAE** — Pixel-space diffusion is impractical for high-resolution images
6. **Forgetting timestep embeddings** — Without them, the model can't adapt to different noise levels
7. **Memory errors** — Always use `torch.no_grad()` during inference and clear cache between batches

---

## Troubleshooting

### "CUDA out of memory when running Stable Diffusion"

```python
# Solution: Use float16 and enable attention slicing
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    safety_checker=None
)
pipe.enable_attention_slicing()  # Reduces memory usage
pipe = pipe.to("cuda")
```

### "Generated images look noisy or blurry"

```python
# Solution: Adjust num_inference_steps and guidance_scale
image = pipe(
    prompt="your prompt here",
    num_inference_steps=50,     # More steps = cleaner results
    guidance_scale=7.5,         # Higher = more prompt adherence
    generator=torch.Generator().manual_seed(42)  # Reproducible results
).images[0]
```

### "Model produces completely different images each run"

```python
# Solution: Set a fixed seed for reproducibility
generator = torch.Generator(device="cuda").manual_seed(42)
image = pipe("prompt", generator=generator).images[0]
```

---

## Learning Pathway

```
Prerequisites (PyTorch, CNNs)
        │
        ▼
Chapter 1: Foundations
  - Forward/reverse process
  - DDPM algorithm
  - Noise schedules
  - Simple denoiser
        │
        ▼
Chapter 2: Advanced Architectures
  - U-Net denoiser
  - Classifier-free guidance
  - Latent diffusion (Stable Diffusion)
  - Fine-tuning with DreamBooth/LoRA
        │
        ▼
  Build your own diffusion project!
```

---

## What You'll Be Able to Do

After completing this guide:

- Understand the mathematical foundations of diffusion models
- Build and train a simple DDPM from scratch
- Use U-Net architectures as denoisers
- Apply classifier-free guidance for controlled generation
- Use and fine-tune Stable Diffusion with HuggingFace diffusers
- Apply LoRA/DreamBooth for personalized image generation
- Compare diffusion models with GANs and choose the right tool

---

## Additional Resources

- [Denoising Diffusion Probabilistic Models (DDPM) Paper](https://arxiv.org/abs/2006.11239)
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [HuggingFace Diffusers Documentation](https://huggingface.co/docs/diffusers)
- [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/)
- [Score-Based Generative Modeling](https://yang-song.github.io/blog/2021/score/)

---

## Exercises

### Chapter 1 Exercises
1. Implement the forward diffusion process: add noise to an image at different timesteps and visualize
2. Train a simple MLP denoiser on MNIST (pixel by pixel)
3. Experiment with different noise schedules (linear vs cosine) and compare results

### Chapter 2 Exercises
1. Build a U-Net denoiser and train it on CIFAR-10
2. Implement classifier-free guidance and compare generated images with/without it
3. Fine-tune Stable Diffusion with DreamBooth on 5 images of your choice
4. Implement DDIM sampling and compare speed vs quality with DDPM

---

## Related Guides

| Guide | Connection |
|-------|-----------|
| [CNNs](../CNNs/README.md) | U-Net uses convolutions extensively |
| [GANs](../GANs/README.md) | Alternative generative model — compare approaches |
| [Transformers](../Transformers/README.md) | Some diffusion models use transformer backbones |

---

*Ready to start? Head to [Chapter 1: Foundations of Diffusion Models](chapter_1_foundations.md).*
