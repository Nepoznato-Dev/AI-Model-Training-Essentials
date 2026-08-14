<!--
---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.1"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [computer, vision, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Computer Vision Fundamentals

Computer vision gives machines the ability to interpret and understand visual information from the world — images, video, and 3D data. It powers everything from face recognition on your phone to self-driving cars, medical image analysis, and industrial quality control. This file covers the core concepts, architectures, and techniques.

---

## How Computers See Images

### Pixels and Channels

A digital image is a grid of pixels. Each pixel has numerical values representing colour intensity.

| Image Type | Channels | Values per Pixel | Example |
|-----------|----------|-----------------|---------|
| **Grayscale** | 1 | 0 (black) to 255 (white) | Medical X-rays |
| **RGB** | 3 | Red, Green, Blue (each 0–255) | Standard colour photos |
| **RGBA** | 4 | RGB + Alpha (transparency) | Images with transparent backgrounds |
| **HSV** | 3 | Hue, Saturation, Value | Colour-based segmentation |

A 1920×1080 RGB image is a tensor of shape `(1080, 1920, 3)` — that's 6.2 million pixels, each with 3 values.

### Key Operations

| Operation | Description |
|-----------|-------------|
| **Resizing** | Scale image to target dimensions (bilinear, nearest-neighbour interpolation) |
| **Cropping** | Extract a region of interest |
| **Normalisation** | Scale pixel values to [0,1] or [-1,1] for neural networks |
| **Augmentation** | Artificially expand training data (rotation, flip, colour jitter, crop) |

---

## Convolution: The Core Operation

A convolution slides a small filter (kernel) across the image, computing dot products at each position. This is how CNNs detect edges, textures, and patterns.

### Convolution Parameters

| Parameter | Effect |
|-----------|--------|
| **Kernel size** | 3×3, 5×5, 7×7 — larger kernels capture bigger patterns |
| **Stride** | Step size; stride=2 halves the output dimensions |
| **Padding** | Add zeros around the border to preserve spatial dimensions |
| **Number of filters** | Each filter learns a different feature (edge, texture, colour pattern) |

### What Convolutions Learn

| Layer Depth | Features Detected |
|-------------|------------------|
| **Early layers** | Edges, corners, simple textures |
| **Middle layers** | Shapes, object parts (wheels, eyes, leaves) |
| **Deep layers** | High-level concepts (faces, cars, animals) |

---

## CNN Architectures

The evolution of CNN architectures tells the story of deep learning's progress in computer vision.

| Architecture | Year | Key Innovation |
|-------------|------|---------------|
| **LeNet-5** | 1998 | First practical CNN; digit recognition |
| **AlexNet** | 2012 | Deep CNN wins ImageNet; ReLU, dropout, GPU training |
| **VGGNet** | 2014 | Stacked 3×3 convolutions (deeper = better) |
| **GoogLeNet (Inception)** | 2014 | Inception modules (parallel filter sizes); 22 layers |
| **ResNet** | 2015 | Skip connections (residual learning); 152+ layers |
| **EfficientNet** | 2019 | Compound scaling (depth + width + resolution) |
| **ConvNeXt** | 2022 | Modernised ResNet; competitive with Transformers |

### Why ResNet Changed Everything

Before ResNet, training very deep networks was nearly impossible due to the vanishing gradient problem. ResNet introduced **skip connections** (also called residual connections): the input to a layer is added to its output.

```
output = F(x) + x    # Skip connection
```

This simple idea allowed networks with 152+ layers to be trained effectively, and it's now standard in virtually all deep architectures.

---

## Core Vision Tasks

### Image Classification

Assign a label to an entire image.

| Model | Approach |
|-------|----------|
| CNNs (ResNet, EfficientNet) | Traditional approach; excellent accuracy |
| Vision Transformers (ViT) | Treat image as sequence of patches; Transformer encoder |
| Transfer Learning | Fine-tune a pre-trained model on your dataset |

### Object Detection

Find and classify multiple objects within an image, with bounding boxes.

| Model | Type | Speed |
|-------|------|-------|
| **R-CNN** | Two-stage (proposal + classification) | Slow |
| **Fast R-CNN** | Improved two-stage | Medium |
| **Faster R-CNN** | Region Proposal Network + detector | Medium |
| **YOLO** (v1–v10) | Single-stage; predict boxes + classes in one pass | Very fast |
| **DETR** | Transformer-based; no anchor boxes | Medium |

**YOLO** (You Only Look Once) is the go-to for real-time detection. **Faster R-CNN** is preferred when accuracy matters more than speed.

### Image Segmentation

Classify every pixel in an image.

| Type | Description | Use Case |
|------|-------------|----------|
| **Semantic Segmentation** | Each pixel gets a class label | Autonomous driving (road, car, pedestrian) |
| **Instance Segmentation** | Each pixel + object instance ID | Counting objects, medical imaging |
| **Panoptic Segmentation** | Semantic + instance combined | Comprehensive scene understanding |

Key models: U-Net (medical imaging), Mask R-CNN (instance), DeepLab (semantic), Segment Anything Model (SAM — universal segmentation).

### Image Generation

| Approach | Description | Examples |
|----------|-------------|----------|
| **GANs** | Generator vs discriminator adversarial training | StyleGAN, CycleGAN |
| **VAEs** | Learn latent distribution; sample to generate | Variational Autoencoders |
| **Diffusion Models** | Iteratively denoise random noise | Stable Diffusion, DALL-E, Midjourney |

Diffusion models have largely surpassed GANs for image generation quality.

---

## Transfer Learning for Vision

Training a CNN from scratch requires massive data and compute. Transfer learning lets you start with a model already trained on millions of images (ImageNet) and fine-tune it for your specific task.

### Steps

1. **Choose a pre-trained model** (ResNet50, EfficientNet-B0, ViT).
2. **Replace the classification head** with your own (matching your number of classes).
3. **Freeze early layers** (they capture generic features like edges).
4. **Fine-tune** on your dataset with a low learning rate.
5. **Unfreeze gradually** if you need more adaptation.

This approach routinely achieves high accuracy with as few as 1,000–10,000 labelled images.

---

## Data Augmentation

Augmentation artificially expands your training dataset by applying transformations.

| Augmentation | Effect | When to Use |
|-------------|--------|-------------|
| **Random crop** | Crop to random region | Almost always |
| **Horizontal flip** | Mirror image | When orientation doesn't matter |
| **Rotation** | Rotate by random angle | When objects appear at any angle |
| **Colour jitter** | Randomly adjust brightness, contrast, saturation | When lighting varies |
| **Random erasing** | Mask random regions | Improves robustness |
| **Mixup / CutMix** | Blend two images and labels | Regularisation |

Libraries: `torchvision.transforms`, `albumentations`, `imgaug`, `tf.keras.preprocessing`.

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **OpenCV** | Classic CV operations (filtering, edge detection, geometric transforms) |
| **torchvision** | PyTorch vision models, transforms, datasets |
| **tf.keras.applications** | Pre-trained models in TensorFlow/Keras |
| **Ultralytics (YOLOv8/v11)** | Object detection, segmentation, classification |
| **Hugging Face (transformers)** | Vision Transformers, SegFormer, DETR |
| **Segment Anything (SAM)** | Universal image segmentation from Meta |
| **Albumentations** | Fast, flexible image augmentation library |

---

## Practical Tips

- **Start with transfer learning.** Fine-tuning a pre-trained model beats training from scratch in almost every case.
- **Normalise your inputs.** Match the normalisation the pre-trained model expects (usually ImageNet mean/std).
- **Use appropriate metrics.** Accuracy for balanced datasets; F1, mAP, or IoU for imbalanced or detection tasks.
- **Visualise your data.** Look at sample images, check class distributions, inspect model predictions.
- **Augment wisely.** Only apply transformations that make sense for your domain (don't flip medical images vertically).
- **Monitor overfitting.** If training accuracy is high but validation is low, increase augmentation or add dropout.
