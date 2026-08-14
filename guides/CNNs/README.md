# CNN (Convolutional Neural Network) Training Guide

## Welcome! Never Worked with Images in AI?

**Imagine you're teaching a child to recognize cats.** You don't hand them a spreadsheet of pixel values. You show them pictures! They notice pointy ears, whiskers, fluffy tails — and over time, they can spot any cat.

**Convolutional Neural Networks (CNNs)** do something similar. They're specially designed neural networks that look at images the way you do — by detecting edges, then shapes, then complete objects.

### What You'll Learn

By the end of this guide, you will:
- Understand how CNNs "see" images differently from regular neural networks
- Know what convolution, pooling, and feature maps are
- Build CNN architectures from LeNet to ResNet
- Train your own image classifiers from scratch
- Apply transfer learning to leverage pre-trained models
- Handle real-world tasks: object detection, segmentation, and more

---

## Before We Begin: Why CNNs?

### The Problem with Regular Neural Networks

A regular neural network treats an image as a flat list of pixels. For a 224×224 color image, that's **150,528 input neurons** — each connected to every neuron in the next layer. This is:
- **Too many parameters** (slow and memory-hungry)
- **Ignores spatial structure** (nearby pixels matter!)
- **Can't handle different image sizes**

### The CNN Solution

CNNs solve all these problems with three brilliant ideas:

| Concept | What It Does | Analogy |
|---------|-------------|---------|
| **Convolution** | Slides a small filter across the image detecting features | Like using a magnifying glass to scan a photo |
| **Pooling** | Shrinks the image, keeping only the most important features | Like summarizing a paragraph in one sentence |
| **Hierarchy** | Stacks layers to detect increasingly complex features | Edges → Shapes → Objects → Scenes |

### How CNNs "See"

```
Layer 1: Detects edges and colors
         ┌──────────┐
         │ /  /  /  │  ← Finds lines, borders
         └──────────┘

Layer 2: Combines edges into shapes
         ┌──────────┐
         │ ◯  △  □  │  ← Finds circles, triangles
         └──────────┘

Layer 3: Combines shapes into objects
         ┌──────────┐
         │ 🐱  🚗  │  ← Finds cats, cars
         └──────────┘
```

### Real-World Applications

- **Medical Imaging**: Detecting tumors in X-rays and MRIs
- **Self-Driving Cars**: Recognizing pedestrians, signs, and lanes
- **Face Recognition**: Unlocking your phone with your face
- **Quality Control**: Finding defects in manufactured products
- **Art & Photography**: Style transfer, super-resolution, filters
- **Satellite Imagery**: Land use classification, disaster monitoring

---

## How This Guide is Organized

This guide has **4 comprehensive chapters**, each building on the previous:

### Chapter 1: CNN Fundamentals (Start Here!)
- What are CNNs and why they work for images
- Convolution operations explained with visual examples
- Pooling layers and feature maps
- Batch normalization and dropout
- Build your first CNN from scratch in PyTorch
- Common mistakes beginners make

### Chapter 2: Advanced Architectures
- **LeNet-5**: The original CNN (1998)
- **AlexNet**: The deep learning revolution (2012)
- **VGG**: Going deeper with small filters
- **ResNet**: Skip connections that changed everything
- **DenseNet**: Connecting every layer to every other layer
- **EfficientNet**: Finding the optimal architecture
- **Vision Transformers**: The new challenger

### Chapter 3: Training Techniques
- **Transfer Learning**: Use pre-trained models as your starting point
- **Data Augmentation**: Artificially expand your dataset
- **Regularization**: Prevent overfitting
- **Learning Rate Scheduling**: Train smarter, not harder
- **Mixed Precision Training**: Faster training with less memory
- **Hyperparameter Tuning**: Finding the best settings

### Chapter 4: Specialized Applications
- **Object Detection**: Finding and labeling objects in images (YOLO, SSD)
- **Semantic Segmentation**: Classifying every pixel (U-Net, DeepLab)
- **Image Generation**: Creating new images (GANs, VAEs)
- **Image-to-Image Translation**: Style transfer, super-resolution
- **Video Analysis**: Action recognition and tracking

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
1. **Basic Python**: Variables, loops, functions, classes
2. **High school math**: Basic algebra (we explain the rest)
3. **No prior AI/ML experience needed!**

**Helpful but not required:**
- ⭐ Some NumPy experience
- ⭐ Basic understanding of what neural networks are
- ⭐ Completed the [Prerequisites](../prerequisites/README.md) section

### Hardware Requirements

| Setup Type | What You Need | Best For |
|------------|--------------|----------|
| **Basic Learning** | Any laptop, 8GB RAM, CPU | Reading, small experiments |
| **Recommended** | NVIDIA GPU with 8GB+ VRAM | Training CNNs on real datasets |
| **Cloud (Free!)** | Google Colab | Everything! Free GPU access |

Don't have a GPU? No problem! We'll show you how to use free cloud services like Google Colab.

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
| **Convolution** | Sliding a small filter across an image to detect features |
| **Filter/Kernel** | The small matrix that detects a specific feature (like edges) |
| **Feature Map** | The output of a convolution — shows where a feature was found |
| **Pooling** | Shrinking the image to keep only the most important information |
| **Stride** | How many pixels the filter moves at each step |
| **Padding** | Adding zeros around the image to preserve its size |
| **Batch Normalization** | Normalizing layer inputs for faster, more stable training |
| **Transfer Learning** | Using a pre-trained model as a starting point |
| **Data Augmentation** | Creating new training images by transforming existing ones |
| **ResNet** | Architecture with "skip connections" that enables very deep networks |
| **Backbone** | The main feature-extraction part of a CNN |
| **Fine-Tuning** | Taking a pre-trained model and adapting it to your specific task |

---

## Prerequisites

- Python 3.8+
- PyTorch 2.0+
- GPU with 8GB+ VRAM (recommended but not required)
- Basic Python knowledge (see [Prerequisites](../prerequisites/README.md))

## Dataset Recommendations

### For Learning
- **MNIST**: Handwritten digits (the "hello world" of CNNs)
- **CIFAR-10**: 60,000 tiny images in 10 categories
- **Fashion-MNIST**: Clothing items (drop-in replacement for MNIST)

### For Real Projects
- **ImageNet**: 1.2M images, 1000 categories (the gold standard)
- **COCO**: 330K images with object detection annotations
- **CelebA**: 200K celebrity faces with attributes

## Best Practices

1. **Start with transfer learning** — Don't train from scratch unless you have millions of images
2. **Use data augmentation** — It's free performance improvement
3. **Start with a proven architecture** — ResNet18 or EfficientNet-B0 are great defaults
4. **Normalize your inputs** — Use ImageNet mean/std if using pre-trained models
5. **Monitor both training and validation loss** — Watch for overfitting
6. **Use learning rate scheduling** — Start high, reduce gradually
7. **Save checkpoints** — Don't lose hours of training

## Common Pitfalls

- ❌ Training from scratch with a small dataset
- ❌ Forgetting to normalize input images
- ❌ Using a learning rate that's too high (loss explodes)
- ❌ Not using data augmentation (overfitting quickly)
- ❌ Ignoring class imbalance in your dataset
- ❌ Using images that are too large for your GPU memory
- ❌ Forgetting to set `model.eval()` during inference

## Troubleshooting

### Issue: "CUDA out of memory"
**Fix:** Reduce batch size or image resolution:
```python
batch_size = 8  # Try 4 or 2 if needed
transform = transforms.Resize((128, 128))  # Smaller images
```

### Issue: Model accuracy is stuck
**Fix:** Check your learning rate and data preprocessing:
```python
# Use ImageNet normalization with pre-trained models
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)
```

### Issue: Training is very slow
**Fix:** Enable GPU and use data loading workers:
```python
trainloader = DataLoader(
    trainset, batch_size=32, shuffle=True,
    num_workers=4, pin_memory=True  # Faster GPU transfers
)
```

---

## Learning Pathway

```
Recommended Path:
Prerequisites → CNNs Ch1 → CNNs Ch2 → CNNs Ch3 → CNNs Ch4 → Specialization

Combined with other guides:
CNNs → GANs (for image generation)
CNNs → GNNs (for graph + vision tasks)
CNNs → Infrastructure Layers (for deployment)
```

---

## After This Guide

You'll be able to:
- ✅ Understand how CNNs process images
- ✅ Build and train CNN architectures from scratch
- ✅ Apply transfer learning effectively
- ✅ Choose the right architecture for your problem
- ✅ Handle object detection and segmentation tasks
- ✅ Deploy CNN models for real applications
- ✅ Debug common training issues confidently

---

## Additional Resources

- [CS231n: CNNs for Visual Recognition](http://cs231n.stanford.edu/)
- [PyTorch Vision Documentation](https://pytorch.org/vision/stable/)
- [Papers With Code: Image Classification](https://paperswithcode.com/task/image-classification)
- [The Illustrated CNN (Blog)](https://poloclub.github.io/cnn-explainer/)
- [Fast.ai Practical Deep Learning](https://course.fast.ai/)

## Exercises

Each chapter includes hands-on exercises. Complete them to reinforce your learning:

### Chapter 1 Exercises
- Build a CNN with 3 convolutional layers for CIFAR-10
- Visualize what each filter detects
- Experiment with different kernel sizes (3×3 vs 5×5 vs 7×7)

### Chapter 2 Exercises
- Implement a ResNet block with skip connections
- Compare accuracy of LeNet vs ResNet on the same data
- Build an EfficientNet with compound scaling

### Chapter 3 Exercises
- Fine-tune a pre-trained ResNet on a custom dataset
- Implement 5 different data augmentation techniques
- Compare training with and without mixed precision

### Chapter 4 Exercises
- Build an object detector using YOLO architecture
- Implement semantic segmentation with U-Net
- Create a style transfer system

---

**Note**: If you're completely new to AI, consider starting with the [RAG guide](../RAG/README.md) first to learn fundamental concepts, then come back here for computer vision specialization.
