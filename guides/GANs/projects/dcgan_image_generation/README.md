# DCGAN — Image Generation with Deep Convolutional GAN

Learn how Generative Adversarial Networks work by building a DCGAN on MNIST.

## What This Project Does

This project demonstrates how to:
- Build a **Generator** that creates images from random noise
- Build a **Discriminator** that distinguishes real images from fake ones
- Train both networks in an adversarial **minimax** loop
- Generate realistic handwritten digit images from the MNIST dataset
- Visualize training progress with sample outputs

## Concepts Covered

- Generative Adversarial Networks (GANs) — generator vs. discriminator
- Deep Convolutional GAN (DCGAN) architecture guidelines
- Transposed convolutions (for upsampling in the generator)
- Adversarial training loop and loss functions
- Batch normalization and LeakyReLU activations
- Training instability and mode collapse

## Prerequisites

- Basic Python and PyTorch knowledge
- Familiarity with CNNs (see the [CNNs Guide](../../../CNNs/) for theory)
- Understanding of GAN fundamentals (see the [GANs Guide](../../))

## Quick Start

```bash
# Navigate to this project directory
cd guides/GANs/projects/dcgan_image_generation

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
```

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Full DCGAN implementation (~300 lines, heavily commented) |
| `requirements.txt` | Python dependencies (torch, torchvision, matplotlib) |
| `README.md` | This documentation file |

## How It Works

### The GAN Framework

A GAN has two networks that compete against each other:

- **Generator (G):** Takes random noise → produces a fake image
- **Discriminator (D):** Takes a real or fake image → predicts "real" or "fake"

Training alternates between:
1. Training D to better distinguish real from fake
2. Training G to better fool D

### DCGAN Architecture

This implementation follows the DCGAN guidelines:
- **Generator:** Random noise → TransposedConv layers → Generated image
- **Discriminator:** Input image → Conv layers with stride → Real/Fake prediction
- Batch normalization throughout (except input/output layers)
- LeakyReLU in discriminator, ReLU in generator, Sigmoid output

### Training

- **Loss:** Binary cross-entropy for both networks
- **Optimizer:** Adam with tuned learning rate and beta1
- **Visualization:** Matplotlib saves sample generated images during training

## Exercises

1. Change the noise vector dimension and observe the effect on output quality
2. Remove batch normalization and compare training stability
3. Try training on Fashion-MNIST instead of MNIST
4. Experiment with different learning rates for G and D

## Common Issues

- **Mode collapse:** Generator produces very similar images — try different random seeds or adjust learning rates
- **Training instability:** GANs are notoriously hard to train — use GPU, tune hyperparameters carefully
- **Slow on CPU:** GAN training is compute-intensive — use Google Colab with GPU

## Next Steps

- Read the full [GANs Guide](../../) for deeper theory on GAN variants
- Explore [GANs Chapter 2: Advanced Variants](../../chapter_2_advanced_variants.md) (StyleGAN, CycleGAN, etc.)
- Check [GANs Chapter 3: Stabilization Techniques](../../chapter_3_stabilization_techniques.md) for training tips
- Check [Common Errors](../../../errors/) if you get stuck

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~300 |
| Time to Complete | 30-45 minutes |
| GPU Required | Recommended (CPU works but slow) |
| Difficulty | ⭐⭐⭐ Intermediate |
| Prerequisites | PyTorch, CNN fundamentals, GAN basics |
