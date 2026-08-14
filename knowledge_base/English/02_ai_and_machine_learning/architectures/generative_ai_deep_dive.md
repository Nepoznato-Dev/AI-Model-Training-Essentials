---
# Metadata
title: "Generative AI Deep Dive"
description: "GANs, VAEs, diffusion models, LLMs, generative AI applications"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [generative, ai, deep, dive, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Generative AI Deep Dive

Generative AI refers to models that create new content — images, text, audio, video, code — rather than just classifying or predicting existing data. While large language models get most of the attention, the generative AI landscape is far broader. This file covers the architectures, techniques, and trade-offs behind modern generative systems, from diffusion models to variational autoencoders to flow models.

---

## What Makes a Model "Generative"?

| Type | What It Does | Example |
|------|-------------|---------|
| **Discriminative** | Learn the boundary between classes | "Is this image a cat or a dog?" |
| **Generative** | Learn the distribution of the data itself | "Generate a new image of a cat" |

Generative models capture *how the data is produced*, not just how to categorise it. This makes them fundamentally more powerful — and harder to train.

---

## Major Generative Architectures

### Variational Autoencoders (VAEs)

VAEs learn a compressed, structured representation (latent space) of the data, then generate new samples by sampling from that space.

| Component | Role |
|-----------|------|
| **Encoder** | Maps input data to a distribution in latent space (mean and variance) |
| **Latent space** | A continuous, low-dimensional space where similar data points are close together |
| **Decoder** | Maps points in latent space back to data space |
| **KL divergence** | Regularisation term that keeps the latent distribution close to a standard normal |

**How generation works**: sample a random vector from the latent space → pass it through the decoder → get a new data point.

| Strength | Weakness |
|----------|----------|
| Smooth, continuous latent space | Outputs tend to be blurry |
| Principled mathematical framework | Limited by the architecture's capacity |
| Can interpolate between examples | Less sharp than diffusion or GAN outputs |

VAEs are often used as components in other models (e.g., Stable Diffusion uses a VAE as part of its pipeline).

### Generative Adversarial Networks (GANs)

GANs pit two networks against each other: a **generator** that creates fake data, and a **discriminator** that tries to tell real from fake.

| Component | Goal |
|-----------|------|
| **Generator** | Produce data that fools the discriminator |
| **Discriminator** | Correctly classify real vs generated data |

They train simultaneously, each pushing the other to improve. In theory, the generator eventually produces data indistinguishable from real data.

| GAN Variant | Key Innovation |
|-------------|---------------|
| **DCGAN** | Convolutional architectures; stable training |
| **StyleGAN / StyleGAN2 / StyleGAN3** | Style-based generation; photorealistic faces; controllable attributes |
| **CycleGAN** | Unpaired image-to-image translation (horse → zebra) |
| **Pix2Pix** | Paired image-to-image translation (sketch → photo) |
| **ProGAN** | Progressive growing for high-resolution images |
| **BigGAN** | Class-conditional generation at scale |

**Why GANs have declined**: Training is notoriously unstable (mode collapse, vanishing gradients). Diffusion models now produce better quality for most image generation tasks. GANs are still used for real-time applications (they're fast at inference) and specific tasks like super-resolution.

### Diffusion Models

Diffusion models are the current state of the art for image and video generation. They work by gradually adding noise to data until it's pure random noise, then learning to reverse the process.

| Phase | What Happens |
|-------|-------------|
| **Forward process (training)** | Slowly add Gaussian noise over hundreds/thousands of steps until the data is destroyed |
| **Reverse process (generation)** | Learn to denoise step by step, starting from pure noise, until a clean image emerges |

| Model | Developer | Notable Feature |
|-------|-----------|-----------------|
| **DDPM** (Denoising Diffusion Probabilistic Model) | Ho et al., 2020 | Showed diffusion models can produce high-quality images |
| **Stable Diffusion** | Stability AI | Latent diffusion (runs in compressed space); open-source |
| **DALL-E 3** | OpenAI | Integrated with ChatGPT for text understanding |
| **Midjourney** | Midjourney | Artistic quality; closed-source |
| **Imagen** | Google DeepMind | High-fidelity text-to-image |
| **Sora** | OpenAI | Video generation via diffusion transformers |
| **FLUX** | Black Forest Labs | Open-weight successor to Stable Diffusion |

### Why Diffusion Models Won

| Advantage | Explanation |
|-----------|-------------|
| **Training stability** | Much more stable than GANs; no adversarial training |
| **Output quality** | State-of-the-art image quality and diversity |
| **Controllability** | Can be guided with text (via CLIP), inpainting masks, or other conditions |
| **Diversity** | Less mode collapse than GANs; generates diverse outputs |

| Disadvantage | Explanation |
|-------------|-------------|
| **Slow inference** | Requires many denoising steps (20–50 typical) |
| **Compute-intensive** | Each step is a full forward pass through a large model |

### Latent Diffusion

Running diffusion in pixel space is expensive. **Latent diffusion** (used by Stable Diffusion) runs the diffusion process in a compressed latent space instead.

| Step | What Happens |
|------|-------------|
| 1. Compress | A pre-trained VAE encodes the image into a smaller latent representation |
| 2. Diffuse | The diffusion model adds/removes noise in latent space |
| 3. Decode | The VAE decoder converts the latent back into a full image |

This makes generation dramatically faster and cheaper while preserving quality.

---

## Text-Conditioned Generation

Most modern generative systems are conditioned on text prompts — you describe what you want, and the model generates it.

### CLIP (Contrastive Language-Image Pre-training)

CLIP learns a shared embedding space for text and images. It was trained on billions of image-text pairs from the internet.

| Capability | Description |
|------------|-------------|
| **Zero-shot classification** | Classify images using text descriptions without any training |
| **Image-text retrieval** | Find the most relevant image for a text query |
| **Guiding diffusion** | Steer image generation toward the text prompt |

### Classifier-Free Guidance (CFG)

CFG controls how closely the generated image follows the text prompt.

| CFG Scale | Effect |
|-----------|--------|
| **1.0** | No guidance; diverse but may not match the prompt |
| **5.0–7.5** | Balanced; good quality and prompt adherence |
| **10.0+** | Strong adherence; can produce oversaturated or artefact-heavy images |

---

## Other Generative Approaches

### Normalising Flows

| Feature | Description |
|---------|-------------|
| **How it works** | Learn an invertible mapping between data and a simple distribution |
| **Strength** | Exact likelihood computation; fast sampling |
| **Weakness** | Requires carefully designed architectures; less flexible |
| **Use cases** | Anomaly detection, density estimation |

### Autoregressive Models

| Feature | Description |
|---------|-------------|
| **How it works** | Generate data one element at a time, conditioning on all previous elements |
| **Strength** | Natural for sequential data (text, code, music) |
| **Weakness** | Slow generation (must be sequential); limited by training data distribution |
| **Examples** | GPT (text), WaveNet (audio), ImageGPT (images) |

### Energy-Based Models

| Feature | Description |
|---------|-------------|
| **How it works** | Learn an energy function; low energy = realistic data |
| **Strength** | Flexible; no normalisation required |
| **Weakness** | Training is difficult; sampling requires MCMC |
| **Use cases** | Theoretical research; some robotics applications |

---

## Evaluation Metrics

How do you measure the quality of generated data? It's harder than you might think.

| Metric | For | What It Measures | Limitation |
|--------|-----|-----------------|------------|
| **FID** (Fréchet Inception Distance) | Images | Distance between real and generated image distributions | Lower is better; doesn't capture diversity well |
| **IS** (Inception Score) | Images | Quality and diversity of generated images | Controversial; can be gamed |
| **CLIP Score** | Text-to-image | How well the image matches the text prompt | Depends on CLIP's biases |
| **Perplexity** | Text | How well the model predicts the next token | Lower is better; doesn't measure coherence |
| **BLEU / ROUGE** | Text generation | Overlap with reference text | Poor proxy for human judgment |
| **FAD** (Fréchet Audio Distance) | Audio | Distance between real and generated audio distributions | Analogous to FID for audio |

---

## Controllable Generation

Modern systems let you control what gets generated beyond just text prompts.

| Method | Control Type | Example |
|--------|-------------|---------|
| **Inpainting** | Fill in masked regions | Remove an object from a photo |
| **Outpainting** | Extend beyond image boundaries | Make a landscape wider |
| **ControlNet** | Structural guidance (edges, depth, pose) | Generate an image matching a specific pose |
| **IP-Adapter** | Style or content from a reference image | "Make it look like this painting" |
| **LoRA** | Fine-tuned style or concept | Add a specific character or art style |
| **Img2Img** | Transform an existing image | Turn a sketch into a photorealistic image |

---

## Video Generation

Video generation is the next frontier after images. It adds the dimension of time and motion.

| Model | Approach | Notable Feature |
|-------|----------|-----------------|
| **Sora** (OpenAI) | Diffusion Transformer | Up to 1080p; understands physics reasonably well |
| **Runway Gen-3** | Diffusion-based | Commercial video generation tool |
| **Pika** | Diffusion-based | Short video clips from text |
| **Kling** | Autoregressive + diffusion | Long-form video generation |
| **Veo 2** (Google) | Diffusion Transformer | High-quality, physically consistent video |

### Challenges in Video Generation

| Challenge | Why It's Hard |
|-----------|--------------|
| **Temporal consistency** | Objects should look the same across frames |
| **Physics** | Gravity, collisions, fluid dynamics must be approximately correct |
| **Length** | Generating minutes of coherent video is far harder than a single image |
| **Compute** | Video is essentially many images; costs scale with frame count |
| **Evaluation** | No standard metric captures video quality well |

---

## Audio Generation

| Model | Type | Application |
|-------|------|-------------|
| **WaveNet** (DeepMind) | Autoregressive | High-quality speech synthesis |
| **VALL-E** (Microsoft) | Neural codec | Text-to-speech from a 3-second voice sample |
| **MusicGen** (Meta) | Transformer-based | Text-to-music generation |
| **AudioLDM** | Latent diffusion | Sound effect generation |
| **ElevenLabs** | Commercial | Voice cloning and synthesis |

---

## The Economics of Generation

| Factor | Impact |
|--------|--------|
| **Training cost** | Diffusion models: $100K–$10M+ depending on scale |
| **Inference cost** | Image generation: ~$0.01–0.05 per image at scale |
| **Hardware** | Training: multiple A100/H100 GPUs; Inference: single GPU possible |
| **Open vs closed** | Open models (Stable Diffusion, FLUX) can run locally; closed models (DALL-E, Midjourney) are API-only |

---

## Summary

Generative AI has evolved from GANs through VAEs to diffusion models and beyond. The key insight across all these architectures is the same: learn the distribution of data, then sample from it to create new content. Diffusion models currently dominate image and video generation due to their training stability and output quality. VAEs serve as crucial building blocks. Autoregressive models dominate text and code. The field is moving toward multimodal generation — systems that can produce text, images, audio, and video from any combination of inputs — and toward making generation faster, cheaper, and more controllable.
