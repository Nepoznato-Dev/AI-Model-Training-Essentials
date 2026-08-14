# DCGAN - Image Generation with Deep Convolutional GAN
# Learn how Generative Adversarial Networks work by building a DCGAN on MNIST
# Lines of code: ~300 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import time
import random
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend (works without display)
import matplotlib.pyplot as plt

print("=" * 70)
print("DCGAN - DEEP CONVOLUTIONAL GENERATIVE ADVERSARIAL NETWORK")
print("=" * 70)
print()

# Set random seeds for reproducibility
manual_seed = 42
random.seed(manual_seed)
torch.manual_seed(manual_seed)

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
if device.type == "cpu":
    print("Warning: GAN training is slow on CPU. Consider using Google Colab!")
print()

# ============================================================================
# STEP 2: UNDERSTAND HOW A GAN WORKS
# ============================================================================
#
# A GAN has TWO networks that compete against each other:
#
#   GENERATOR (G):   Random noise -> Fake image
#   DISCRIMINATOR (D): Real or Fake image -> Real/Fake prediction
#
# Training loop:
#   1. G creates a fake image from random noise
#   2. D tries to tell real images from fake ones
#   3. G tries to fool D into thinking its fakes are real
#   4. D gets better at detecting fakes -> G must get better at creating them
#
# Think of it as a counterfeiter (G) vs a detective (D):
#   - The counterfeiter keeps improving their forgeries
#   - The detective keeps improving their detection
#   - Eventually, the forgeries become indistinguishable from real
#
# DCGAN adds convolutional layers and specific design choices for stability:
#   - No pooling layers (use strided convolutions instead)
#   - Batch normalization in both G and D
#   - ReLU activation in G, LeakyReLU in D
#   - Tanh activation in G's output
#
# ============================================================================

# ============================================================================
# STEP 3: BUILD THE GENERATOR
# ============================================================================
#
# The Generator takes a random noise vector (latent vector z) and transforms
# it into a fake image. It's like an "artistic imagination" network.
#
# Flow: z (100-dim) -> reshape to (128, 1, 1) -> transpose convolutions -> image (1, 28, 28)
# ============================================================================

class Generator(nn.Module):
    """
    DCGAN Generator: transforms random noise into fake images.
    
    Architecture:
        z (100-dim noise) -> reshape -> ConvTranspose2d blocks -> Tanh -> image
    
    Each ConvTranspose2d UPSAMPLES the spatial dimensions (opposite of Conv2d).
    BatchNorm stabilizes training. ReLU adds non-linearity.
    Final Tanh squashes output to [-1, 1] (matching normalized image range).
    """
    
    def __init__(self, latent_dim=100, feature_maps=64, channels=1):
        """
        Args:
            latent_dim: Size of the random noise vector (z)
            feature_maps: Base number of filters (doubled at each layer going backward)
            channels: Number of output image channels (1 for grayscale, 3 for RGB)
        """
        super(Generator, self).__init__()
        
        self.main = nn.Sequential(
            # Input: z (batch, 100, 1, 1) -> upsample to (batch, 512, 4, 4)
            nn.ConvTranspose2d(latent_dim, feature_maps * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(feature_maps * 8),
            nn.ReLU(True),
            
            # (batch, 512, 4, 4) -> upsample to (batch, 256, 8, 8)
            nn.ConvTranspose2d(feature_maps * 8, feature_maps * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 4),
            nn.ReLU(True),
            
            # (batch, 256, 8, 8) -> upsample to (batch, 128, 16, 16)
            nn.ConvTranspose2d(feature_maps * 4, feature_maps * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 2),
            nn.ReLU(True),
            
            # (batch, 128, 16, 16) -> upsample to (batch, 64, 32, 32)
            nn.ConvTranspose2d(feature_maps * 2, feature_maps, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps),
            nn.ReLU(True),
            
            # (batch, 64, 32, 32) -> (batch, channels, 64, 64)
            # Wait — MNIST is 28x28. Let's adjust: we'll use 28x28 output.
            # Actually, let's keep it simple and generate 64x64, then we'll
            # just train on 64x64 resized MNIST images.
            # Output: (batch, 1, 64, 64)
            nn.ConvTranspose2d(feature_maps, channels, 4, 2, 1, bias=False),
            nn.Tanh()  # Output range: [-1, 1]
        )
    
    def forward(self, z):
        """
        Generate a fake image from random noise.
        
        Args:
            z: Random noise vector of shape (batch, latent_dim, 1, 1)
        
        Returns:
            Fake image of shape (batch, channels, 64, 64)
        """
        return self.main(z)

# ============================================================================
# STEP 4: BUILD THE DISCRIMINATOR
# ============================================================================
#
# The Discriminator is a binary classifier: given an image, predict whether
# it's real (from the dataset) or fake (generated by G).
#
# Flow: image (1, 64, 64) -> convolutions -> sigmoid -> real/fake score
# ============================================================================

class Discriminator(nn.Module):
    """
    DCGAN Discriminator: classifies images as real or fake.
    
    Architecture:
        image -> Conv2d blocks -> flatten -> sigmoid -> probability
    
    Uses LeakyReLU (instead of ReLU) to allow small negative gradients,
    which helps prevent the "dying ReLU" problem during adversarial training.
    """
    
    def __init__(self, channels=1, feature_maps=64):
        """
        Args:
            channels: Number of input image channels (1 for grayscale)
            feature_maps: Base number of filters
        """
        super(Discriminator, self).__init__()
        
        self.main = nn.Sequential(
            # Input: (batch, 1, 64, 64) -> (batch, 64, 32, 32)
            nn.Conv2d(channels, feature_maps, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            
            # (batch, 64, 32, 32) -> (batch, 128, 16, 16)
            nn.Conv2d(feature_maps, feature_maps * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            # (batch, 128, 16, 16) -> (batch, 256, 8, 8)
            nn.Conv2d(feature_maps * 2, feature_maps * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 4),
            nn.LeakyReLU(0.2, inplace=True),
            
            # (batch, 256, 8, 8) -> (batch, 512, 4, 4)
            nn.Conv2d(feature_maps * 4, feature_maps * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_maps * 8),
            nn.LeakyReLU(0.2, inplace=True),
            
            # (batch, 512, 4, 4) -> (batch, 1, 1, 1)
            nn.Conv2d(feature_maps * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()  # Output: probability of being real
        )
    
    def forward(self, x):
        """
        Classify an image as real or fake.
        
        Args:
            x: Input image of shape (batch, channels, 64, 64)
        
        Returns:
            Probability of being real, shape (batch, 1, 1, 1)
        """
        return self.main(x)

# ============================================================================
# STEP 5: INITIALIZE MODELS
# ============================================================================

# Hyperparameters
latent_dim = 100      # Size of the noise vector
lr = 0.0002           # Learning rate
beta1 = 0.5           # Adam beta1 (momentum)
batch_size = 128

# Create models
netG = Generator(latent_dim=latent_dim, channels=1).to(device)
netD = Discriminator(channels=1).to(device)

# Custom weight initialization (from the DCGAN paper)
def weights_init(m):
    """Initialize ConvTranspose2d, Conv2d, and BatchNorm weights."""
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        nn.init.constant_(m.bias.data, 0)

netG.apply(weights_init)
netD.apply(weights_init)

print("Models created and initialized!")
print(f"  Generator parameters: {sum(p.numel() for p in netG.parameters()):,}")
print(f"  Discriminator parameters: {sum(p.numel() for p in netD.parameters()):,}")
print()

# ============================================================================
# STEP 6: LOAD MNIST DATASET
# ============================================================================

print("Loading MNIST dataset (resized to 64x64)...")
print("(First run will download the dataset)")
print()

# MNIST images are 28x28 grayscale. We resize to 64x64 to match our GAN.
# Normalize to [-1, 1] to match the Generator's Tanh output range.
transform = transforms.Compose([
    transforms.Resize(64),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Scale from [0,1] to [-1,1]
])

dataset = datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=2)

print(f"Dataset loaded!")
print(f"  Training samples: {len(dataset):,}")
print(f"  Image size: 1 x 64 x 64 (grayscale)")
print(f"  Batch size: {batch_size}")
print()

# ============================================================================
# STEP 7: DEFINE LOSS AND OPTIMIZERS
# ============================================================================

# Binary Cross Entropy Loss for real/fake classification
criterion = nn.BCELoss()

# Separate optimizers for Generator and Discriminator
optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta1, 0.999))
optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta1, 0.999))

# Create fixed noise for visualization (same noise every time -> watch G improve)
fixed_noise = torch.randn(16, latent_dim, 1, 1, device=device)

# Labels for real and fake batches
real_label = 1.0
fake_label = 0.0

print("Training setup complete:")
print(f"  Loss: BCELoss (Binary Cross Entropy)")
print(f"  Optimizer: Adam (lr={lr}, beta1={beta1})")
print(f"  Latent dimension: {latent_dim}")
print()

# ============================================================================
# STEP 8: TRAINING LOOP
# ============================================================================

num_epochs = 5
print(f"Starting GAN training for {num_epochs} epochs...")
print("-" * 70)
print("Legend: D_loss = Discriminator loss, G_loss = Generator loss")
print("-" * 70)

start_time = time.time()

# Lists to track losses for plotting later
G_losses = []
D_losses = []

for epoch in range(num_epochs):
    epoch_start = time.time()
    
    for i, (real_images, _) in enumerate(dataloader):
        
        # ---------------------------------------------------------------
        # TRAIN DISCRIMINATOR: maximize log(D(x)) + log(1 - D(G(z)))
        # ---------------------------------------------------------------
        
        netD.zero_grad()
        
        real_images = real_images.to(device)
        batch_size_current = real_images.size(0)
        
        # Create labels for this batch
        real_labels = torch.full((batch_size_current,), real_label, device=device)
        fake_labels = torch.full((batch_size_current,), fake_label, device=device)
        
        # Forward pass: real images
        output_real = netD(real_images).view(-1)
        loss_D_real = criterion(output_real, real_labels)
        
        # Forward pass: fake images (from Generator)
        noise = torch.randn(batch_size_current, latent_dim, 1, 1, device=device)
        fake_images = netG(noise)
        output_fake = netD(fake_images.detach()).view(-1)  # .detach() — don't update G yet
        loss_D_fake = criterion(output_fake, fake_labels)
        
        # Combined D loss and backward pass
        loss_D = loss_D_real + loss_D_fake
        loss_D.backward()
        optimizerD.step()
        
        # ---------------------------------------------------------------
        # TRAIN GENERATOR: maximize log(D(G(z)))
        # (i.e., make D think G's fakes are real)
        # ---------------------------------------------------------------
        
        netG.zero_grad()
        
        # Generate fake images and pass through D
        output_fake_for_G = netD(fake_images).view(-1)
        loss_G = criterion(output_fake_for_G, real_labels)  # G wants D to output "real"
        
        loss_G.backward()
        optimizerG.step()
        
        # Track losses
        G_losses.append(loss_G.item())
        D_losses.append(loss_D.item())
    
    epoch_time = time.time() - epoch_start
    avg_D = sum(D_losses[-len(dataloader):]) / len(dataloader)
    avg_G = sum(G_losses[-len(dataloader):]) / len(dataloader)
    
    print(f"Epoch [{epoch+1}/{num_epochs}] | "
          f"D_loss: {avg_D:.4f} | "
          f"G_loss: {avg_G:.4f} | "
          f"Time: {epoch_time:.1f}s")

total_time = time.time() - start_time
print("-" * 70)
print(f"Training completed in {total_time:.1f}s ({total_time/60:.1f} minutes)")
print()

# ============================================================================
# STEP 9: GENERATE AND SAVE SAMPLE IMAGES
# ============================================================================

print("Generating sample images with the trained Generator...")
print("-" * 70)

netG.eval()
with torch.no_grad():
    fake_samples = netG(fixed_noise).detach().cpu()

# Create a grid of generated images
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
fig.suptitle("Generated MNIST Digits (DCGAN)", fontsize=14)

for i, ax in enumerate(axes.flat):
    # Denormalize: [-1, 1] -> [0, 1]
    img = (fake_samples[i].squeeze() + 1) / 2
    ax.imshow(img, cmap='gray')
    ax.axis('off')

plt.tight_layout()
save_path = "dcgan_generated_digits.png"
plt.savefig(save_path, dpi=150, bbox_inches='tight')
plt.close()

print(f"Generated image grid saved to '{save_path}'")
print()

# ============================================================================
# STEP 10: SAVE MODEL CHECKPOINTS
# ============================================================================

torch.save({
    'generator_state_dict': netG.state_dict(),
    'discriminator_state_dict': netD.state_dict(),
    'g_losses': G_losses,
    'd_losses': D_losses,
}, "dcgan_mnist_checkpoint.pth")
print("Model checkpoint saved to 'dcgan_mnist_checkpoint.pth'")
print()

# To generate new digits later:
# checkpoint = torch.load("dcgan_mnist_checkpoint.pth", weights_only=True)
# netG = Generator(latent_dim=100, channels=1)
# netG.load_state_dict(checkpoint['generator_state_dict'])
# netG.eval()
# noise = torch.randn(1, 100, 1, 1)
# fake_image = netG(noise)

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the DCGAN Image Generation Project!")
print("=" * 70)
print(f"""
What you learned:
- How GANs work (Generator vs Discriminator adversarial training)
- DCGAN architecture and design choices for stable training
- Transposed convolutions (upsampling) in the Generator
- Training a GAN with alternating optimization
- Generating realistic images from random noise

Results Summary:
- Training time: {total_time:.1f}s
- Final D_loss: {D_losses[-1]:.4f}
- Final G_loss: {G_losses[-1]:.4f}
- Generated digits saved: {save_path}

Next steps:
1. Read Chapter 2 of the GANs Guide: Advanced Variants
2. Try training on a color dataset (e.g., CIFAR-10, CelebA)
3. Experiment with conditional GANs (generate specific digits)
4. Try WGAN-GP for more stable training
5. Explore StyleGAN for high-resolution face generation

Resources:
- DCGAN Paper: https://arxiv.org/abs/1511.06434
- GAN Tutorial: https://arxiv.org/abs/1406.2661
""")
print("=" * 70)
