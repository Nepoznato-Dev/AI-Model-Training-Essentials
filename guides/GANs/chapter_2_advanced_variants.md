# Chapter 2: Advanced GAN Variants

## 2.1 Introduction to GAN Evolution

Since the original GAN paper in 2014, numerous variants have been developed to address training instability, mode collapse, and quality issues. This chapter explores advanced GAN architectures that have pushed the boundaries of generative modeling.

### Evolution Timeline

| Year | Model | Key Contribution |
|------|-------|-----------------|
| 2014 | GAN | Original adversarial framework |
| 2015 | DCGAN | Convolutional architectures |
| 2017 | WGAN | Wasserstein distance for stability |
| 2017 | CycleGAN | Unpaired image-to-image translation |
| 2018 | StyleGAN | Style-based generation control |
| 2019 | BigGAN | Large-scale high-resolution synthesis |
| 2020 | StyleGAN2 | Improved architecture and training |

---

## 2.2 Wasserstein GAN (WGAN)

### The Problem with Traditional GANs

Traditional GANs suffer from:
1. **Training instability**: Minimax game can oscillate
2. **Vanishing gradients**: When discriminator is too good
3. **Mode collapse**: Generator produces limited variety

### Wasserstein Distance Solution

WGAN uses Earth-Mover (Wasserstein-1) distance instead of JS divergence:

```
W(P_r, P_g) = inf_{γ ∈ Π(P_r, P_g)} E_{(x,y)~γ}[||x - y||]
```

Where Π(P_r, P_g) is the set of all joint distributions whose marginals are P_r and P_g.

### WGAN Implementation

```python
import torch
import torch.nn as nn
import torch.optim as optim


class WGAN_Discriminator(nn.Module):
    """WGAN Critic (not classifier - outputs scalar, not probability)"""
    
    def __init__(self, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.network = nn.Sequential(
            # Input: (batch, 3, 64, 64)
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            # (batch, 64, 32, 32)
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # (batch, 128, 16, 16)
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # (batch, 256, 8, 8)
            
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # (batch, 512, 4, 4)
            
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0)
            # Output: (batch, 1, 1, 1) - scalar score
        )
    
    def forward(self, x):
        return self.network(x).view(-1, 1)


class WGAN_Generator(nn.Module):
    """Generator same as DCGAN"""
    
    def __init__(self, latent_dim=100, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.network = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, feature_dim * 8, 4, 1, 0),
            nn.BatchNorm2d(feature_dim * 8),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_dim * 8, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_dim * 4, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_dim * 2, feature_dim, 4, 2, 1),
            nn.BatchNorm2d(feature_dim),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(feature_dim, img_channels, 4, 2, 1),
            nn.Tanh()
        )
    
    def forward(self, z):
        z = z.view(z.size(0), -1, 1, 1)
        return self.network(z)


def train_wgan(generator, discriminator, dataloader, epochs, 
               n_critic=5, clip_value=0.01, lr=0.00005):
    """
    Train WGAN with weight clipping
    
    Args:
        n_critic: Number of critic iterations per generator iteration
        clip_value: Value for weight clipping (enforces Lipschitz constraint)
    """
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    generator = generator.to(device)
    discriminator = discriminator.to(device)
    
    # Optimizers (use RMSProp or Adam with low momentum)
    opt_g = optim.RMSprop(generator.parameters(), lr=lr)
    opt_d = optim.RMSprop(discriminator.parameters(), lr=lr)
    
    fixed_noise = torch.randn(64, 100, 1, 1).to(device)
    
    for epoch in range(epochs):
        for i, (real_images, _) in enumerate(dataloader):
            batch_size = real_images.size(0)
            real_images = real_images.to(device)
            
            # --- Train Critic (Discriminator) multiple times ---
            for _ in range(n_critic):
                opt_d.zero_grad()
                
                # Real images
                d_real = discriminator(real_images)
                
                # Fake images
                noise = torch.randn(batch_size, 100, 1, 1).to(device)
                fake_images = generator(noise)
                d_fake = discriminator(fake_images.detach())
                
                # WGAN loss: maximize D(x) - D(G(z))
                d_loss = -(d_real.mean() - d_fake.mean())
                d_loss.backward()
                opt_d.step()
                
                # Weight clipping (enforce Lipschitz constraint)
                for param in discriminator.parameters():
                    param.data.clamp_(-clip_value, clip_value)
            
            # --- Train Generator ---
            opt_g.zero_grad()
            
            noise = torch.randn(batch_size, 100, 1, 1).to(device)
            fake_images = generator(noise)
            g_loss = -discriminator(fake_images).mean()
            g_loss.backward()
            opt_g.step()
            
            if i % 100 == 0:
                print(f"Epoch [{epoch}/{epochs}] Step [{i}/{len(dataloader)}] "
                      f"D Loss: {d_loss.item():.4f} G Loss: {g_loss.item():.4f}")
        
        # Generate samples
        with torch.no_grad():
            fake = generator(fixed_noise).detach().cpu()
```

### WGAN-GP: Gradient Penalty

Weight clipping can cause optimization problems. WGAN-GP uses gradient penalty instead:

```python
def calculate_gradient_penalty(discriminator, real_data, fake_data, lambda_gp=10):
    """Calculate gradient penalty for WGAN-GP"""
    
    batch_size = real_data.size(0)
    alpha = torch.rand(batch_size, 1, 1, 1).to(real_data.device)
    
    # Interpolate between real and fake
    interpolates = (alpha * real_data + (1 - alpha) * fake_data).requires_grad_(True)
    d_interpolates = discriminator(interpolates)
    
    # Compute gradients
    grad_outputs = torch.ones_like(d_interpolates)
    gradients = torch.autograd.grad(
        outputs=d_interpolates,
        inputs=interpolates,
        grad_outputs=grad_outputs,
        create_graph=True,
        retain_graph=True
    )[0]
    
    # Calculate gradient norm
    gradients = gradients.view(batch_size, -1)
    gradient_norm = gradients.norm(2, dim=1)
    
    # Penalize if gradient norm != 1
    gradient_penalty = ((gradient_norm - 1) ** 2).mean()
    
    return lambda_gp * gradient_penalty


def train_wgan_gp(generator, discriminator, dataloader, epochs, 
                  n_critic=5, lambda_gp=10, lr=0.0001):
    """Train WGAN with Gradient Penalty"""
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    generator = generator.to(device)
    discriminator = discriminator.to(device)
    
    opt_g = optim.Adam(generator.parameters(), lr=lr, betas=(0.5, 0.9))
    opt_d = optim.Adam(discriminator.parameters(), lr=lr, betas=(0.5, 0.9))
    
    for epoch in range(epochs):
        for i, (real_images, _) in enumerate(dataloader):
            batch_size = real_images.size(0)
            real_images = real_images.to(device)
            
            # Train critic
            for _ in range(n_critic):
                opt_d.zero_grad()
                
                # Real
                d_real = discriminator(real_images)
                
                # Fake
                noise = torch.randn(batch_size, 100, 1, 1).to(device)
                fake_images = generator(noise)
                d_fake = discriminator(fake_images.detach())
                
                # Gradient penalty
                gp = calculate_gradient_penalty(discriminator, real_images, fake_images.detach())
                
                # WGAN-GP loss
                d_loss = -(d_real.mean() - d_fake.mean()) + gp
                d_loss.backward()
                opt_d.step()
            
            # Train generator
            opt_g.zero_grad()
            noise = torch.randn(batch_size, 100, 1, 1).to(device)
            fake_images = generator(noise)
            g_loss = -discriminator(fake_images).mean()
            g_loss.backward()
            opt_g.step()
```

---

## 2.3 CycleGAN: Unpaired Image Translation

CycleGAN enables image-to-image translation without paired training data using cycle consistency loss.

### Architecture

```python
class ResidualBlock(nn.Module):
    """Residual block for CycleGAN generators"""
    
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(channels, channels, 3, 1, 1),
            nn.InstanceNorm2d(channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(channels, channels, 3, 1, 1),
            nn.InstanceNorm2d(channels)
        )
    
    def forward(self, x):
        return x + self.conv(x)


class CycleGANGenerator(nn.Module):
    """CycleGAN Generator with residual blocks"""
    
    def __init__(self, img_channels=3, feature_dim=64, n_res_blocks=9):
        super().__init__()
        
        # Initial convolution
        model = [
            nn.Conv2d(img_channels, feature_dim, 7, 1, 3),
            nn.InstanceNorm2d(feature_dim),
            nn.ReLU(inplace=True)
        ]
        
        # Downsampling
        model += [
            nn.Conv2d(feature_dim, feature_dim * 2, 3, 2, 1),
            nn.InstanceNorm2d(feature_dim * 2),
            nn.ReLU(inplace=True),
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 3, 2, 1),
            nn.InstanceNorm2d(feature_dim * 4),
            nn.ReLU(inplace=True)
        ]
        
        # Residual blocks
        for _ in range(n_res_blocks):
            model += [ResidualBlock(feature_dim * 4)]
        
        # Upsampling
        model += [
            nn.ConvTranspose2d(feature_dim * 4, feature_dim * 2, 3, 2, 1, output_padding=1),
            nn.InstanceNorm2d(feature_dim * 2),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(feature_dim * 2, feature_dim, 3, 2, 1, output_padding=1),
            nn.InstanceNorm2d(feature_dim),
            nn.ReLU(inplace=True),
            nn.Conv2d(feature_dim, img_channels, 7, 1, 3),
            nn.Tanh()
        ]
        
        self.model = nn.Sequential(*model)
    
    def forward(self, x):
        return self.model(x)


class PatchDiscriminator(nn.Module):
    """PatchGAN discriminator - classifies patches instead of whole image"""
    
    def __init__(self, img_channels=3, feature_dim=64, n_layers=3):
        super().__init__()
        
        layers = [
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True)
        ]
        
        nf = feature_dim
        for n in range(1, n_layers):
            nf_prev = nf
            nf = min(nf * 2, 512)
            layers += [
                nn.Conv2d(nf_prev, nf, 4, 2, 1),
                nn.InstanceNorm2d(nf),
                nn.LeakyReLU(0.2, inplace=True)
            ]
        
        nf_prev = nf
        nf = min(nf * 2, 512)
        layers += [
            nn.Conv2d(nf_prev, nf, 4, 1, 1),
            nn.InstanceNorm2d(nf),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(nf, 1, 4, 1, 1)
        ]
        
        self.model = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.model(x)
```

### Cycle Consistency Loss

```python
class CycleGANNetwork(nn.Module):
    """Complete CycleGAN with two generators and discriminators"""
    
    def __init__(self):
        super().__init__()
        
        # Generators: A->B and B->A
        self.G_AB = CycleGANGenerator()  # Horse to Zebra
        self.G_BA = CycleGANGenerator()  # Zebra to Horse
        
        # Discriminators
        self.D_A = PatchDiscriminator()
        self.D_B = PatchDiscriminator()
    
    def forward(self, real_A, real_B):
        """
        Forward pass with cycle consistency
        
        Returns:
            Generated images and reconstructed images for loss calculation
        """
        # Forward translation
        fake_B = self.G_AB(real_A)  # A -> B
        fake_A = self.G_BA(real_B)  # B -> A
        
        # Cycle reconstruction
        rec_A = self.G_BA(fake_B)   # A -> B -> A
        rec_B = self.G_AB(fake_A)   # B -> A -> B
        
        # Identity mapping (optional, helps preserve color)
        id_A = self.G_BA(real_A)
        id_B = self.G_AB(real_B)
        
        return {
            'fake_A': fake_A, 'fake_B': fake_B,
            'rec_A': rec_A, 'rec_B': rec_B,
            'id_A': id_A, 'id_B': id_B
        }


class CycleGANLoss(nn.Module):
    """Combined loss for CycleGAN"""
    
    def __init__(self, lambda_cycle=10.0, lambda_identity=0.5):
        super().__init__()
        self.lambda_cycle = lambda_cycle
        self.lambda_identity = lambda_identity
        self.mse_loss = nn.MSELoss()
        self.l1_loss = nn.L1Loss()
    
    def forward(self, network_output, real_A, real_B, 
                disc_A_real, disc_A_fake, disc_B_real, disc_B_fake):
        
        fake_A = network_output['fake_A']
        fake_B = network_output['fake_B']
        rec_A = network_output['rec_A']
        rec_B = network_output['rec_B']
        id_A = network_output['id_A']
        id_B = network_output['id_B']
        
        # Adversarial losses
        adv_A = self.mse_loss(disc_A_fake, torch.ones_like(disc_A_fake))
        adv_B = self.mse_loss(disc_B_fake, torch.ones_like(disc_B_fake))
        
        # Cycle consistency losses
        cycle_A = self.l1_loss(rec_A, real_A)
        cycle_B = self.l1_loss(rec_B, real_B)
        cycle_loss = self.lambda_cycle * (cycle_A + cycle_B)
        
        # Identity losses
        id_A_loss = self.l1_loss(id_A, real_A)
        id_B_loss = self.l1_loss(id_B, real_B)
        id_loss = self.lambda_identity * (id_A_loss + id_B_loss)
        
        # Total generator loss
        gen_loss = adv_A + adv_B + cycle_loss + id_loss
        
        # Discriminator losses
        real_label = torch.ones_like(disc_A_real)
        fake_label = torch.zeros_like(disc_A_fake)
        
        disc_A_loss = self.mse_loss(disc_A_real, real_label) + \
                      self.mse_loss(disc_A_fake.detach(), fake_label)
        disc_B_loss = self.mse_loss(disc_B_real, real_label) + \
                      self.mse_loss(disc_B_fake.detach(), fake_label)
        
        return gen_loss, disc_A_loss, disc_B_loss
```

---

## 2.4 StyleGAN: Style-Based Generation

StyleGAN introduces style-based generator architecture with explicit control over generated image characteristics.

### Mapping Network and Style Injection

```python
class StyleGANMappingNetwork(nn.Module):
    """Maps latent code z to intermediate latent space w"""
    
    def __init__(self, latent_dim=512, num_layers=8):
        super().__init__()
        
        layers = []
        for i in range(num_layers):
            layers.extend([
                nn.Linear(latent_dim, latent_dim),
                nn.LeakyReLU(0.2, inplace=True)
            ])
        
        self.mapping = nn.Sequential(*layers)
    
    def forward(self, z):
        return self.mapping(z)


class StyleModulation(nn.Module):
    """Applies style to feature maps via adaptive instance normalization"""
    
    def __init__(self, feature_dim, style_dim=512):
        super().__init__()
        
        self.style_scale = nn.Linear(style_dim, feature_dim)
        self.style_bias = nn.Linear(style_dim, feature_dim)
        
        # Initialize scale to zeros (identity transform initially)
        nn.init.zeros_(self.style_scale.weight)
        nn.init.ones_(self.style_scale.bias)
        nn.init.zeros_(self.style_bias.weight)
        nn.init.zeros_(self.style_bias.bias)
    
    def forward(self, x, style):
        # x: (batch, feature_dim, H, W)
        # style: (batch, style_dim)
        
        scale = self.style_scale(style).view(-1, x.size(1), 1, 1)
        bias = self.style_bias(style).view(-1, x.size(1), 1, 1)
        
        # Normalize
        x_mean = x.mean(dim=[2, 3], keepdim=True)
        x_std = x.std(dim=[2, 3], keepdim=True)
        x_normalized = (x - x_mean) / (x_std + 1e-8)
        
        # Apply style
        return x_normalized * (scale + 1) + bias


class StyleGANBlock(nn.Module):
    """StyleGAN generator block"""
    
    def __init__(self, in_channels, out_channels, style_dim=512, upsample=True):
        super().__init__()
        
        self.upsample = upsample
        
        # First convolution with style
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, 1, 1)
        self.style1 = StyleModulation(out_channels, style_dim)
        self.noise1 = nn.Parameter(torch.randn(1, 1, 1, 1))
        
        # Second convolution with style
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, 1, 1)
        self.style2 = StyleModulation(out_channels, style_dim)
        self.noise2 = nn.Parameter(torch.randn(1, 1, 1, 1))
        
        self.activate = nn.LeakyReLU(0.2, inplace=True)
    
    def forward(self, x, style):
        if self.upsample:
            x = nn.functional.interpolate(x, scale_factor=2, mode='bilinear', align_corners=False)
        
        # Add noise
        noise1 = self.noise1 * torch.randn(1, 1, x.size(2), x.size(3)).to(x.device)
        x = x + noise1
        
        x = self.conv1(x)
        x = self.style1(x, style)
        x = self.activate(x)
        
        # Add noise again
        noise2 = self.noise2 * torch.randn(1, 1, x.size(2), x.size(3)).to(x.device)
        x = x + noise2
        
        x = self.conv2(x)
        x = self.style2(x, style)
        x = self.activate(x)
        
        return x


class StyleGANGenerator(nn.Module):
    """StyleGAN generator"""
    
    def __init__(self, latent_dim=512, img_channels=3, feature_dim=512):
        super().__init__()
        
        # Mapping network
        self.mapping = StyleGANMappingNetwork(latent_dim)
        
        # Initial 4x4 block
        self.initial = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, feature_dim, 4, 1, 0),
            nn.LeakyReLU(0.2, inplace=True)
        )
        
        # Progressive blocks
        self.blocks = nn.ModuleList([
            StyleGANBlock(feature_dim, feature_dim, latent_dim, upsample=True),
            StyleGANBlock(feature_dim, feature_dim // 2, latent_dim, upsample=True),
            StyleGANBlock(feature_dim // 2, feature_dim // 4, latent_dim, upsample=True),
            StyleGANBlock(feature_dim // 4, feature_dim // 8, latent_dim, upsample=True),
        ])
        
        # To RGB
        self.to_rgb = nn.Conv2d(feature_dim // 8, img_channels, 1)
    
    def forward(self, z):
        # Map to style space
        w = self.mapping(z)
        
        # Initial block
        x = self.initial(z.unsqueeze(2).unsqueeze(3))
        
        # Progressive generation
        for block in self.blocks:
            x = block(x, w)
        
        # Output
        return torch.tanh(self.to_rgb(x))
```

---

## 2.5 Conditional GANs

Conditional GANs enable controlled generation by conditioning on additional information.

### cGAN Architecture

```python
class ConditionalDCGAN_Generator(nn.Module):
    """Conditional DCGAN Generator"""
    
    def __init__(self, latent_dim=100, num_classes=10, img_channels=3, embed_dim=100):
        super().__init__()
        
        # Class embedding
        self.label_embedding = nn.Embedding(num_classes, embed_dim)
        
        # Combined input dimension
        combined_dim = latent_dim + embed_dim
        
        self.network = nn.Sequential(
            nn.ConvTranspose2d(combined_dim, 512, 4, 1, 0),
            nn.BatchNorm2d(512),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(512, 256, 4, 2, 1),
            nn.BatchNorm2d(256),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(256, 128, 4, 2, 1),
            nn.BatchNorm2d(128),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(128, 64, 4, 2, 1),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            
            nn.ConvTranspose2d(64, img_channels, 4, 2, 1),
            nn.Tanh()
        )
    
    def forward(self, z, labels):
        # Embed labels
        label_embed = self.label_embedding(labels).unsqueeze(2).unsqueeze(3)
        
        # Concatenate noise and embedding
        z = torch.cat([z, label_embed], dim=1)
        
        return self.network(z)


class ConditionalDCGAN_Discriminator(nn.Module):
    """Conditional DCGAN Discriminator"""
    
    def __init__(self, img_channels=3, num_classes=10, feature_dim=64, embed_dim=100):
        super().__init__()
        
        # Class embedding
        self.label_embedding = nn.Embedding(num_classes, embed_dim)
        
        # Combined input dimension
        combined_dim = img_channels + embed_dim
        
        self.network = nn.Sequential(
            nn.Conv2d(combined_dim, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 8),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0),
            nn.Sigmoid()
        )
    
    def forward(self, x, labels):
        # Embed and expand labels
        label_embed = self.label_embedding(labels).unsqueeze(2).unsqueeze(3)
        label_embed = label_embed.expand(-1, -1, x.size(2), x.size(3))
        
        # Concatenate image and label embedding
        x = torch.cat([x, label_embed], dim=1)
        
        return self.network(x).view(-1, 1)
```

### Auxiliary Classifier GAN (AC-GAN)

```python
class ACGAN_Discriminator(nn.Module):
    """AC-GAN: Discriminator also predicts class"""
    
    def __init__(self, img_channels=3, num_classes=10, feature_dim=64):
        super().__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1),
            nn.BatchNorm2d(feature_dim * 8),
            nn.LeakyReLU(0.2, inplace=True),
        )
        
        # Real/fake prediction
        self.real_fake = nn.Sequential(
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0),
            nn.Sigmoid()
        )
        
        # Class prediction
        self.classifier = nn.Sequential(
            nn.Conv2d(feature_dim * 8, num_classes, 4, 1, 0)
        )
    
    def forward(self, x):
        features = self.features(x)
        
        real_fake = self.real_fake(features).view(-1, 1)
        class_pred = self.classifier(features).view(-1, 10)
        
        return real_fake, class_pred
```

---

## 2.6 Training Tips and Best Practices

### Common Issues and Solutions

| Issue | Symptoms | Solutions |
|-------|----------|-----------|
| Mode Collapse | Limited diversity | Mini-batch discrimination, unrolled GAN, WGAN |
| Training Instability | Oscillating losses | WGAN-GP, spectral normalization, learning rate tuning |
| Vanishing Gradients | Generator stops learning | Use WGAN, add noise to discriminator inputs |
| Poor Quality | Blurry/generated artifacts | Increase model capacity, use progressive growing |

### Spectral Normalization

```python
def apply_spectral_norm(module):
    """Apply spectral normalization to a module"""
    for name, child in module.named_children():
        apply_spectral_norm(child)
        if isinstance(child, nn.Conv2d) or isinstance(child, nn.Linear):
            nn.utils.spectral_norm(child)


# Usage
discriminator = Discriminator()
apply_spectral_norm(discriminator)
```

### Two-Time-Scale Update Rule (TTUR)

```python
# Different learning rates for G and D
opt_g = optim.Adam(generator.parameters(), lr=0.0001, betas=(0.0, 0.9))
opt_d = optim.Adam(discriminator.parameters(), lr=0.0004, betas=(0.0, 0.9))
```

---

## Exercises

### Exercise 2.1: Implement WGAN-GP
Implement WGAN with gradient penalty and compare training stability with original GAN.

### Exercise 2.2: Build CycleGAN
Create a CycleGAN for horse↔zebra or summer↔winter translation. Visualize the cycle consistency.

### Exercise 2.3: Style Manipulation
Use StyleGAN to generate images and manipulate the style vector to change specific attributes (age, gender, expression).

### Exercise 2.4: Conditional Generation
Build a conditional GAN for MNIST that generates specific digits on demand. Measure the accuracy of conditional generation.

### Exercise 2.5: Compare GAN Variants
Train DCGAN, WGAN, and WGAN-GP on the same dataset. Compare convergence speed, sample quality, and training stability.

---

## Summary

This chapter covered advanced GAN architectures:

1. **WGAN/WGAN-GP**: Improved training stability using Wasserstein distance
2. **CycleGAN**: Unpaired image-to-image translation with cycle consistency
3. **StyleGAN**: Style-based generation with explicit control
4. **Conditional GANs**: Controlled generation based on conditions
5. **Best Practices**: Spectral normalization, TTUR, and troubleshooting tips

These advanced techniques enable more stable training and higher-quality generation. Master them to build state-of-the-art generative models for various applications.

---

**Next**: Chapter 3 will cover stabilization techniques including gradient penalty analysis, spectral normalization, and architectural improvements.
