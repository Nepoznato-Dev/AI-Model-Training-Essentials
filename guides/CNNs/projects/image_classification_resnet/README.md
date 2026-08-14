# Image Classification with ResNet

Build a ResNet from scratch and train it on CIFAR-10 for image classification.

## What This Project Does

This project demonstrates how to:
- Implement **residual blocks** with skip connections from scratch
- Build a complete **ResNet** architecture in PyTorch
- Train on the **CIFAR-10** dataset (60,000 32×32 color images, 10 classes)
- Use **data augmentation**, learning rate scheduling, and training loops
- Evaluate accuracy on a held-out test set

## Concepts Covered

- Residual (skip) connections and why they solve the vanishing-gradient problem
- Batch normalization and ReLU activation
- Convolutional layers for feature extraction
- Data augmentation (random crops, horizontal flips)
- Learning rate scheduling (step decay)
- Training, validation, and test evaluation loops

## Prerequisites

- Basic Python and PyTorch knowledge
- Familiarity with CNNs (see the [CNNs Guide](../../) for theory)

## Quick Start

```bash
# Navigate to this project directory
cd guides/CNNs/projects/image_classification_resnet

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
| `main.py` | Full ResNet implementation (~300 lines, heavily commented) |
| `requirements.txt` | Python dependencies (torch, torchvision) |
| `README.md` | This documentation file |

## How It Works

### Residual Block

A standard CNN layer does `x → Conv → BN → ReLU → output`. ResNet adds a **skip connection**:

```
Input (x) ──────────────────────────> (+) → ReLU → Output
   │                                    ↑
   ├──> Conv → BN → ReLU → Conv → BN
```

The skip connection lets gradients flow directly through the network, enabling very deep architectures to train effectively.

### Architecture

The implementation builds a small ResNet variant with:
- Two residual blocks (each with two 3×3 conv layers)
- Skip connections that add the input directly to the block output
- Fully connected classification head (→ 10 CIFAR-10 classes)

### Training

- **Optimizer:** Adam with step-decay learning rate schedule
- **Data augmentation:** Random crops and horizontal flips on training set
- **Loss:** Cross-entropy loss

## Exercises

1. Add a third residual block and measure the accuracy change
2. Replace skip connections with plain convolutions — observe the difference
3. Try CIFAR-100 (100 classes) and compare performance
4. Experiment with different learning rate schedules

## Next Steps

- Read the full [CNNs Guide — Chapter 2: Advanced Architectures](../../chapter_2_advanced_architectures.md)
- Explore the [GANs DCGAN Project](../../../GANs/projects/dcgan_image_generation/) for generative models
- Check [Common Errors](../../../errors/) if you get stuck

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~300 |
| Time to Complete | 20-30 minutes |
| GPU Required | Recommended |
| Difficulty | ⭐⭐☆ Easy |
| Prerequisites | Basic PyTorch, CNN fundamentals |
