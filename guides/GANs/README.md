# GAN (Generative Adversarial Network) Training Guide

## Welcome! Want AI to Create Things?

**Imagine two people playing a game:**
- **Person A** (the Generator) is a forger trying to create fake paintings
- **Person B** (the Discriminator) is a detective trying to spot the fakes

At first, Person A's forgeries are terrible — obvious fakes that anyone can spot. But Person B keeps getting better at detecting them, which forces Person A to improve. After thousands of rounds, Person A becomes so skilled that even Person B can't tell the difference.

**That's exactly how GANs work!** Two neural networks compete against each other, and both get dramatically better over time.

### What You'll Learn

By the end of this guide, you will:
- Understand the game theory behind GANs
- Build a GAN from scratch that generates images
- Master advanced variants: DCGAN, WGAN, CycleGAN, StyleGAN
- Know why GANs are hard to train and how to fix it
- Apply GANs to real tasks: image generation, style transfer, super-resolution

---

## Before We Begin: The GAN Revolution

### Why GANs Matter

Before GANs (pre-2014), AI could classify images ("this is a cat") but struggled to **create** them. GANs changed everything by giving AI a way to learn the *distribution* of real data and generate convincing new samples.

**GANs unlocked:**
- 🎨 Creating photorealistic images from scratch
- 🖼️ Translating images between domains (photo → painting)
- 🔍 Enhancing low-resolution images
- 🧬 Generating synthetic medical data for training
- 👤 Creating realistic faces for games and film

### The Math (Made Simple)

Don't panic! The core idea is beautifully simple:

```
Generator's Goal:     Make fake data that looks real
Discriminator's Goal: Tell real data from fake data

They play this game → both get better → amazing results!
```

**The Training Loop:**
```
Step 1: Generator creates fake images from random noise
Step 2: Discriminator sees both real and fake images
Step 3: Discriminator tries to tell them apart
Step 4: Generator learns from its mistakes
Step 5: Repeat thousands of times
```

### Real-World Applications

| Application | What GANs Do | Example |
|-------------|-------------|---------|
| **Image Generation** | Create new images from noise | AI-generated artwork, game textures |
| **Style Transfer** | Transform image style | Photo → Monet painting style |
| **Super-Resolution** | Enhance image quality | Blur photo → sharp HD image |
| **Data Augmentation** | Generate training data | Synthetic medical images |
| **Image Translation** | Convert between domains | Sketch → realistic photo |
| **Face Generation** | Create realistic faces | Characters for games/film |
| **Inpainting** | Fill missing regions | Remove objects, restore photos |

---

## How This Guide is Organized

This guide has **3 comprehensive chapters**, each building on the previous:

### Chapter 1: GAN Fundamentals (Start Here!)
- The game theory behind GANs
- Mathematical foundation (minimax objective)
- Generator and discriminator architectures
- Build a basic GAN from scratch in PyTorch
- Training dynamics and the Nash equilibrium
- Why basic GANs struggle (mode collapse, instability)

### Chapter 2: Advanced GAN Variants
- **DCGAN**: Deep convolutional GANs with stable architecture
- **WGAN**: Wasserstein distance for stable training
- **CycleGAN**: Unpaired image-to-image translation
- **StyleGAN**: Controllable, high-quality image generation
- **Conditional GANs**: Generate specific classes on demand
- **Pix2Pix**: Paired image-to-image translation

### Chapter 3: Stabilization & Production Techniques
- Gradient penalty and spectral normalization
- Progressive growing for high-resolution images
- Training tricks that actually work
- Evaluation metrics (FID, IS)
- Common failure modes and how to fix them
- Deploying GANs in production

---

## Your Learning Journey

Each chapter includes:
- **Concept Explanations**: Simple analogies and visual descriptions
- **Code Examples**: Copy-paste ready Python code with line-by-line explanations
- **Exercises**: Hands-on practice to reinforce learning
- **Troubleshooting**: Common errors and how to fix them
- **Real-World Applications**: See how this is used in industry

### Prerequisites

**Required:**
1. **Python proficiency**: Comfortable with PyTorch basics
2. **Understanding of CNNs**: Convolution, pooling, training loops
3. **No prior generative AI experience needed!**

**Helpful but not required:**
- ⭐ Completed the [CNNs guide](../CNNs/README.md)
- ⭐ Experience training neural networks
- ⭐ Basic understanding of loss functions and optimizers

### Hardware Requirements

| Setup Type | What You Need | Best For |
|------------|--------------|----------|
| **Basic Learning** | 8GB RAM, CPU | Reading, understanding concepts |
| **Minimum GPU** | NVIDIA GPU with 6GB+ VRAM | Training basic GANs |
| **Recommended** | NVIDIA GPU with 12GB+ VRAM | DCGAN, CycleGAN experiments |
| **Cloud (Recommended)** | Google Colab Pro | Everything! Best value |

**Important:** GANs are more GPU-intensive than classifiers. You'll want at least 6GB VRAM for meaningful experiments. Google Colab free tier works for Chapters 1-2 but may struggle with Chapter 3.

---

## Quick Start

```bash
# Install dependencies
pip install torch torchvision torchaudio

# Verify installation
python -c "import torch; print(f'PyTorch {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
```

---

## Quick Glossary (Bookmark This!)

| Term | Simple Definition |
|------|------------------|
| **Generator (G)** | Network that creates fake data from random noise |
| **Discriminator (D)** | Network that tells real from fake data |
| **Latent Vector (z)** | Random noise input to the Generator |
| **Minimax Game** | The competing objective: G tries to fool D, D tries to catch G |
| **Mode Collapse** | When G learns to generate only one type of output |
| **Nash Equilibrium** | The ideal point where G produces perfect fakes |
| **DCGAN** | GAN using convolutional layers for stability |
| **WGAN** | GAN using Wasserstein distance for better training |
| **CycleGAN** | Translates images between domains without paired examples |
| **StyleGAN** | Generates high-quality, controllable images |
| **FID Score** | Metric measuring how realistic generated images are |
| **Gradient Penalty** | Technique to stabilize GAN training |
| **Spectral Normalization** | Constraining weights to prevent training instability |
| **Progressive Growing** | Training at low resolution first, then increasing |

---

## Prerequisites

- Python 3.8+
- PyTorch 2.0+
- GPU with 8GB+ VRAM (recommended)
- Basic understanding of neural networks (see [CNNs Guide](../CNNs/README.md))

## Dataset Recommendations

### For Learning
- **MNIST**: Handwritten digits (easy, fast to train)
- **CIFAR-10**: Small color images (good for DCGAN)
- **CelebA**: Celebrity faces (great for face generation)

### For Real Projects
- **LSUN**: Large-scale scene understanding (bedrooms, churches, etc.)
- **ImageNet**: High-quality diverse images
- **FFHQ**: High-quality face images (for StyleGAN)
- **Custom datasets**: Your own images!

## Best Practices

1. **Start with DCGAN architecture** — It's the most reliable starting point
2. **Use batch normalization in Generator** — But NOT in Discriminator (use layer norm instead)
3. **Use LeakyReLU in Discriminator** — Prevents sparse gradients
4. **Normalize inputs to [-1, 1]** — Use `tanh` activation in Generator's final layer
5. **Start with low resolution** — 32×32 or 64×64 before going higher
6. **Monitor both G and D losses** — If D loss goes to 0, D is too strong
7. **Use gradient penalty** — Essential for stable training

## Common Pitfalls

- ❌ Making the Discriminator too strong (Generator can't learn)
- ❌ Mode collapse: Generator produces only one type of image
- ❌ Not using batch normalization (training becomes unstable)
- ❌ Using ReLU in Generator's output layer (use `tanh` instead)
- ❌ Training at full resolution from the start
- ❌ Ignoring the learning rate balance between G and D
- ❌ Not normalizing images to [-1, 1] range

## Troubleshooting

### Issue: Mode collapse (all generated images look the same)
**Fix:** Try these solutions:
```python
# 1. Add noise to labels (label smoothing)
real_labels = torch.ones(batch_size) * 0.9  # Instead of 1.0
fake_labels = torch.ones(batch_size) * 0.1  # Instead of 0.0

# 2. Use mini-batch discrimination
# 3. Try WGAN-GP loss instead of standard GAN loss
```

### Issue: Discriminator loss goes to 0 immediately
**Fix:** D is too strong — weaken it:
```python
# Reduce D's learning rate
d_optimizer = optim.Adam(D.parameters(), lr=0.0001)  # Lower than G
g_optimizer = optim.Adam(G.parameters(), lr=0.0002)

# Or add gradient penalty
```

### Issue: Training is unstable (loss oscillates wildly)
**Fix:** Add gradient penalty:
```python
def gradient_penalty(D, real, fake, device):
    alpha = torch.rand(real.size(0), 1, 1, 1, device=device)
    interpolated = (alpha * real + (1 - alpha) * fake).requires_grad_(True)
    d_interpolated = D(interpolated)
    gradients = torch.autograd.grad(outputs=d_interpolated, inputs=interpolated,
                                     grad_outputs=torch.ones_like(d_interpolated),
                                     create_graph=True)[0]
    return ((gradients.norm(2, dim=[1,2,3]) - 1) ** 2).mean()
```

---

## Learning Pathway

```
Recommended Path:
CNNs → GANs Ch1 → GANs Ch2 → GANs Ch3 → Specialization

Combined with other guides:
GANs → CNNs (for discriminators and feature extraction)
GANs → Infrastructure Layers (for deploying generation services)
GANs → Diffusion Models (for state-of-the-art generation)
```

---

## After This Guide

You'll be able to:
- ✅ Understand GAN theory and training dynamics
- ✅ Build and train various GAN architectures
- ✅ Diagnose and fix common training issues
- ✅ Choose the right GAN variant for your task
- ✅ Evaluate generated image quality with FID/IS
- ✅ Deploy GANs for real-world applications

---

## Additional Resources

- [Original GAN Paper (Goodfellow et al., 2014)](https://arxiv.org/abs/1406.2661)
- [DCGAN Paper](https://arxiv.org/abs/1511.06434)
- [WGAN-GP Paper](https://arxiv.org/abs/1704.00028)
- [StyleGAN Paper](https://arxiv.org/abs/1812.04948)
- [CycleGAN Paper](https://arxiv.org/abs/1703.10593)
- [GAN Training Tricks (Official PyTorch Tutorial)](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)

## Exercises

Each chapter includes hands-on exercises. Complete them to reinforce your learning:

### Chapter 1 Exercises
- Build a basic GAN that generates MNIST digits
- Experiment with different noise dimensions
- Visualize the training progression over epochs

### Chapter 2 Exercises
- Implement DCGAN for CIFAR-10
- Build a CycleGAN for photo-to-monet translation
- Implement conditional GAN for specific digit generation

### Chapter 3 Exercises
- Add gradient penalty to your DCGAN
- Implement FID score calculation
- Train a GAN at progressively higher resolutions

---

**Note**: GANs build on CNN knowledge. If you haven't worked with CNNs before, we recommend completing the [CNNs guide](../CNNs/README.md) first. If you're completely new to AI, start with the [RAG guide](../RAG/README.md)!
