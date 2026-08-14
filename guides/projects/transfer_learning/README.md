# Transfer Learning Project

A minimal, beginner-friendly introduction to transfer learning using pre-trained models.

## What This Project Does

This project demonstrates how to:
- Load a pre-trained model (ResNet18 trained on ImageNet)
- Adapt it for a new task (CIFAR-10 image classification)
- Use feature extraction mode (freeze most layers)
- Train only the final classification layer
- Compare transfer learning vs training from scratch

## Concepts Covered

- **Transfer Learning**: Using knowledge from one task for another
- **Pre-trained Models**: Models already trained on large datasets
- **Feature Extraction**: Using pre-trained features without updating them
- **Fine-tuning**: Updating pre-trained weights for your task
- **ImageNet**: The standard dataset for image classification (1.2M images)
- **Model Modification**: Adapting architecture for new number of classes

## Prerequisites

Before running this project, you should be comfortable with:
- Basic Python programming
- Installing Python packages with pip
- Basic neural network concepts (helpful but not required)

If you're new to these concepts, check out:
- [Python Basics](../../User%20Questions/prerequisites/python_basics.md)
- [Neural Network Basics](../neural_network_basics/) (recommended first!)

## Quick Start

### Option 1: Google Colab (Recommended for Beginners)

1. Visit [Google Colab](https://colab.research.google.com)
2. Create a new notebook
3. Copy the code from `main.py` into cells
4. Click **Runtime → Change runtime type** and select **GPU** (highly recommended!)
5. Run each cell sequentially

**Benefits:**
- No setup required
- Free GPU access (essential for transfer learning)
- Pre-installed libraries
- Easy to experiment and modify

### Option 2: Local Installation

```bash
# Navigate to this project directory
cd guides/projects/transfer_learning

# Create a virtual environment (recommended)
python -m venv venv

# Activate the environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the project
python main.py
```

**Note:** Training on CPU will be slow. A GPU is highly recommended!

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Main script with heavily commented code (~200 lines) |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation file |

## Code Walkthrough

### Step 1: Load a Pre-trained Model

```python
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
```

This loads ResNet18 with weights trained on ImageNet:
- 11 million parameters
- Trained on 1.2 million images
- Can classify 1000 different object categories
- Learned powerful visual features

### Step 2: Freeze Layers

```python
for param in model.parameters():
    param.requires_grad = False
```

This freezes all layers - we won't update their weights during training. This is called **feature extraction mode**.

### Step 3: Replace Final Layer

```python
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)
```

We replace the final classification layer:
- Original: 1000 classes (ImageNet)
- New: 10 classes (CIFAR-10)
- Only this layer will be trained

### Step 4: Train Only New Layer

```python
optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=0.001
)
```

The optimizer only updates parameters where `requires_grad=True` (our new final layer).

## Exercises

Try these modifications to deepen your understanding:

### Exercise 1: Fine-tune More Layers
Unfreeze some earlier layers and train them too:

```python
# Unfreeze the last ResNet layer
for param in model.layer4.parameters():
    param.requires_grad = True
```

Does accuracy improve? How does training time change?

### Exercise 2: Try Different Pre-trained Models
Experiment with other architectures:

```python
# ResNet50 (deeper, more accurate)
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

# VGG16 (different architecture)
model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)

# EfficientNet (modern, efficient)
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
```

### Exercise 3: Different Datasets
Try transfer learning on other datasets:
- CIFAR-100 (100 classes)
- Fashion-MNIST (clothing items)
- Your own image dataset

### Exercise 4: Adjust Learning Rate
Try different learning rates for the final layer:

```python
optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=0.0001  # Lower learning rate
)
```

### Exercise 5: Compare Training Times
Time how long transfer learning takes vs training a CNN from scratch (from the CNN Basics project).

## Common Issues & Solutions

### Issue: "CUDA out of memory"

**Solution:**
Reduce batch size:
```python
trainloader = DataLoader(trainset, batch_size=16, shuffle=True)
```

Or use a smaller model:
```python
model = models.resnet18(weights=...)  # Smaller than ResNet50
```

### Issue: Slow training on CPU

**Solution:**
1. Use Google Colab with GPU (highly recommended)
2. Use fewer training samples for experimentation
3. Reduce number of epochs
4. Use a smaller model

### Issue: Low accuracy

**Solution:**
1. Train for more epochs
2. Fine-tune more layers (unfreeze some)
3. Use data augmentation
4. Try a larger pre-trained model
5. Adjust learning rate

### Issue: "RuntimeError: size mismatch"

**Solution:**
Make sure you're replacing the correct layer:
```python
# Check the model architecture
print(model)

# Find the final classification layer
# For ResNet: model.fc
# For VGG: model.classifier[6]
# For EfficientNet: model.classifier[1]
```

## Understanding Transfer Learning

### Why Transfer Learning Works

Pre-trained models have learned:
- **Low-level features**: Edges, textures, colors (general)
- **Mid-level features**: Shapes, patterns (somewhat general)
- **High-level features**: Object parts (task-specific)

For new image tasks:
- Low and mid-level features are reusable
- Only high-level features need retraining
- This is why it's so fast and effective!

### Feature Extraction vs Fine-tuning

**Feature Extraction** (what we did):
- Freeze all pre-trained layers
- Only train the final classification layer
- Fast training (minutes)
- Good for small datasets

**Fine-tuning**:
- Unfreeze some or all layers
- Train with small learning rate
- Slower training (hours)
- Better for large datasets or very different domains

### When to Use Transfer Learning

✅ **Use transfer learning when:**
- You have a small dataset (< 10,000 images)
- Your task is similar to ImageNet (image classification)
- You need fast training
- You have limited compute resources

❌ **Train from scratch when:**
- You have a massive dataset (> 100,000 images)
- Your domain is very different from natural images
- You're doing research on model architectures
- You have abundant compute resources

## Expected Results

With the default configuration:
- **Training Time**: ~2-5 minutes on GPU (Colab)
- **Test Accuracy**: 85-90% on CIFAR-10
- **Epochs**: 5 (few needed with transfer learning)
- **Trainable Parameters**: ~8,000 (only final layer)

**Comparison:**
- Training from scratch: ~60-70% accuracy, 30+ minutes
- Transfer learning: ~85-90% accuracy, 2-5 minutes

## Next Steps

After completing this project:

1. **Read the Guide**: Check out the full [CNNs Guide](../../CNNs/) for deeper theory

2. **Try Fine-tuning**: Unfreeze more layers and train them

3. **Use Your Own Data**:
   - Collect images for your task
   - Create a custom dataset
   - Apply transfer learning

4. **Explore Other Tasks**:
   - Object detection (Faster R-CNN, YOLO)
   - Image segmentation (U-Net, DeepLab)
   - Style transfer

5. **Try Domain-Specific Models**:
   - Medical imaging models
   - Satellite imagery models
   - Face recognition models

## Resources

- [PyTorch Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [PyTorch Model Zoo](https://pytorch.org/vision/stable/models.html)
- [Papers With Code](https://paperswithcode.com/) - State-of-the-art models
- [Timm Library](https://github.com/rwightman/pytorch-image-models) - Hundreds of pre-trained models

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~200 |
| Time to Complete | 15-20 minutes (including training) |
| GPU Required | Highly recommended (CPU works but slow) |
| Difficulty | ⭐⭐☆ Easy |
| Prerequisites | Basic Python, basic ML concepts |

## Contributing

Found an issue? Have a suggestion? Feel free to:
- Open an issue on GitHub
- Submit a pull request with improvements
- Share your extensions in the community

---

**Happy Learning!** 🎉

Remember: Transfer learning is one of the most practical skills in deep learning. Most real-world applications use pre-trained models!
