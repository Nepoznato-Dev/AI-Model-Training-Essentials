# Chapter 4: Specialized CNN Applications

## 4.1 Introduction to Advanced Vision Tasks

Beyond image classification, CNNs power a wide range of computer vision applications. This chapter explores object detection, semantic segmentation, instance segmentation, and image generation—tasks that require specialized architectures and training approaches.

### Task Comparison

| Task | Input | Output | Key Challenge |
|------|-------|--------|---------------|
| Classification | Image | Single label | Recognize what's in the image |
| Object Detection | Image | Bounding boxes + labels | Find and classify multiple objects |
| Semantic Segmentation | Image | Pixel-wise labels | Classify every pixel |
| Instance Segmentation | Image | Pixel masks per object | Separate individual object instances |
| Image Generation | Noise/Condition | New image | Generate realistic images |

---

## 4.2 Object Detection

Object detection localizes and classifies multiple objects in an image. Two main paradigms exist: two-stage and one-stage detectors.

### Two-Stage Detectors: Faster R-CNN

Faster R-CNN uses a Region Proposal Network (RPN) followed by a detection head:

```python
import torch
import torch.nn as nn
import torchvision.models as models
from torchvision.ops import RoIPool, MultiScaleRoIAlign


class FasterRCNN(nn.Module):
    """Simplified Faster R-CNN implementation"""
    
    def __init__(self, num_classes, backbone='resnet50'):
        super().__init__()
        
        # Backbone (feature extractor)
        if backbone == 'resnet50':
            weights = models.ResNet50_Weights.IMAGENET1K_V2
            resnet = models.resnet50(weights=weights)
            # Remove final layers
            self.backbone = nn.Sequential(*list(resnet.children())[:-2])
            self.out_channels = 2048
        else:
            raise ValueError(f"Unknown backbone: {backbone}")
        
        # Region Proposal Network (RPN)
        self.rpn_conv = nn.Conv2d(self.out_channels, 512, kernel_size=3, padding=1)
        self.rpn_cls = nn.Conv2d(512, 9 * 2, kernel_size=1)  # 9 anchors, 2 classes (obj/bg)
        self.rpn_reg = nn.Conv2d(512, 9 * 4, kernel_size=1)  # 9 anchors, 4 box coords
        
        # ROI Pooling
        self.roi_pool = RoIPool(output_size=(7, 7), spatial_scale=1/16)
        
        # Detection head
        self.fc6 = nn.Linear(self.out_channels * 7 * 7, 1024)
        self.fc7 = nn.Linear(1024, 1024)
        self.cls_score = nn.Linear(1024, num_classes)
        self.bbox_pred = nn.Linear(1024, num_classes * 4)
        
        # Anchor generation
        self.anchor_scales = [8, 16, 32]
        self.anchor_ratios = [0.5, 1, 2]
    
    def generate_anchors(self, feature_map_size):
        """Generate anchor boxes for each location"""
        H, W = feature_map_size
        anchors = []
        
        for i in range(H):
            for j in range(W):
                cx = (j + 0.5) * 16  # Stride = 16
                cy = (i + 0.5) * 16
                
                for scale in self.anchor_scales:
                    for ratio in self.anchor_ratios:
                        w = scale * (ratio ** 0.5)
                        h = scale / (ratio ** 0.5)
                        
                        anchors.append([
                            cx - w/2, cy - h/2,
                            cx + w/2, cy + h/2
                        ])
        
        return torch.tensor(anchors, dtype=torch.float32)
    
    def forward(self, x, proposals=None):
        # Extract features
        features = self.backbone(x)
        
        # RPN
        rpn_features = torch.relu(self.rpn_conv(features))
        rpn_cls_logits = self.rpn_cls(rpn_features)
        rpn_bbox_deltas = self.rpn_reg(rpn_features)
        
        # Reshape RPN outputs
        N, _, H, W = rpn_cls_logits.shape
        rpn_cls_logits = rpn_cls_logits.permute(0, 2, 3, 1).reshape(N, -1, 2)
        rpn_bbox_deltas = rpn_bbox_deltas.permute(0, 2, 3, 1).reshape(N, -1, 4)
        
        # If proposals provided (training), do second stage
        if proposals is not None:
            # ROI Pooling
            pooled = self.roi_pool(features, proposals)
            pooled = pooled.view(pooled.size(0), -1)
            
            # Detection head
            x = torch.relu(self.fc6(pooled))
            x = torch.relu(self.fc7(x))
            
            cls_scores = self.cls_score(x)
            bbox_preds = self.bbox_pred(x)
            
            return {
                'rpn_cls': rpn_cls_logits,
                'rpn_reg': rpn_bbox_deltas,
                'cls_scores': cls_scores,
                'bbox_preds': bbox_preds,
                'proposals': proposals
            }
        
        return {
            'rpn_cls': rpn_cls_logits,
            'rpn_reg': rpn_bbox_deltas,
            'features': features
        }
```

### One-Stage Detectors: YOLO Architecture

YOLO (You Only Look Once) predicts boxes and classes directly from full images:

```python
class YOLOBlock(nn.Module):
    """YOLO detection block with convolutions"""
    
    def __init__(self, in_channels, out_channels, num_anchors, num_classes):
        super().__init__()
        
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels * 2, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels * 2)
        
        # Final predictions: (x, y, w, h, confidence, class_probs) per anchor
        self.prediction = nn.Conv2d(
            out_channels * 2,
            num_anchors * (5 + num_classes),
            kernel_size=1
        )
        
        self.leaky_relu = nn.LeakyReLU(0.1, inplace=True)
    
    def forward(self, x):
        x = self.leaky_relu(self.bn1(self.conv1(x)))
        x = self.leaky_relu(self.bn2(self.conv2(x)))
        x = self.prediction(x)
        return x


class SimpleYOLO(nn.Module):
    """Simplified YOLO architecture"""
    
    def __init__(self, num_classes=80, num_anchors=3):
        super().__init__()
        
        # Backbone (simplified Darknet-style)
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.LeakyReLU(0.1),
            nn.Conv2d(32, 64, 3, stride=2, padding=1), nn.BatchNorm2d(64), nn.LeakyReLU(0.1),
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.LeakyReLU(0.1),
            nn.Conv2d(128, 256, 3, stride=2, padding=1), nn.BatchNorm2d(256), nn.LeakyReLU(0.1),
            nn.Conv2d(256, 512, 3, padding=1), nn.BatchNorm2d(512), nn.LeakyReLU(0.1),
            nn.Conv2d(512, 1024, 3, padding=1), nn.BatchNorm2d(1024), nn.LeakyReLU(0.1),
        )
        
        # Detection heads at multiple scales
        self.detect_small = YOLOBlock(1024, 512, num_anchors, num_classes)
        self.detect_medium = YOLOBlock(512, 256, num_anchors, num_classes)
        self.detect_large = YOLOBlock(256, 128, num_anchors, num_classes)
    
    def forward(self, x):
        # Extract features at different scales
        features = []
        for i, layer in enumerate(self.backbone):
            x = layer(x)
            if i in [6, 10, 14]:  # Save intermediate features
                features.append(x)
        
        # Detect at multiple scales
        pred_large = self.detect_large(features[2])   # Small objects
        pred_medium = self.detect_medium(features[1]) # Medium objects
        pred_small = self.detect_small(features[0])   # Large objects
        
        return [pred_large, pred_medium, pred_small]
```

### Loss Functions for Detection

```python
class DetectionLoss(nn.Module):
    """Combined loss for object detection"""
    
    def __init__(self, cls_weight=1.0, box_weight=5.0, obj_weight=1.0):
        super().__init__()
        self.cls_weight = cls_weight
        self.box_weight = box_weight
        self.obj_weight = obj_weight
        
        self.bce_loss = nn.BCEWithLogitsLoss(reduction='none')
        self.ce_loss = nn.CrossEntropyLoss()
    
    def forward(self, predictions, targets):
        """
        predictions: dict with 'rpn_cls', 'rpn_reg', 'cls_scores', 'bbox_preds'
        targets: list of dicts with 'boxes' and 'labels'
        """
        total_loss = 0
        
        # RPN Classification Loss (object vs background)
        rpn_cls_loss = self.bce_loss(predictions['rpn_cls'], targets['rpn_labels'])
        total_loss += self.obj_weight * rpn_cls_loss.mean()
        
        # RPN Regression Loss (smooth L1)
        rpn_reg_loss = nn.functional.smooth_l1_loss(
            predictions['rpn_reg'], targets['rpn_boxes'], reduction='mean'
        )
        total_loss += self.box_weight * rpn_reg_loss
        
        # Detection Classification Loss
        cls_loss = self.ce_loss(predictions['cls_scores'], targets['labels'])
        total_loss += self.cls_weight * cls_loss
        
        # Detection Box Regression Loss
        bbox_loss = nn.functional.smooth_l1_loss(
            predictions['bbox_preds'], targets['boxes'], reduction='mean'
        )
        total_loss += self.box_weight * bbox_loss
        
        return total_loss
```

### Intersection over Union (IoU) Variants

```python
def calculate_iou(box1, box2):
    """Calculate IoU between two sets of boxes"""
    # box format: (x1, y1, x2, y2)
    
    # Calculate intersection
    x1 = torch.max(box1[..., 0], box2[..., 0])
    y1 = torch.max(box1[..., 1], box2[..., 1])
    x2 = torch.min(box1[..., 2], box2[..., 2])
    y2 = torch.min(box1[..., 3], box2[..., 3])
    
    intersection = torch.clamp(x2 - x1, min=0) * torch.clamp(y2 - y1, min=0)
    
    # Calculate union
    area1 = (box1[..., 2] - box1[..., 0]) * (box1[..., 3] - box1[..., 1])
    area2 = (box2[..., 2] - box2[..., 0]) * (box2[..., 3] - box2[..., 1])
    union = area1 + area2 - intersection
    
    iou = intersection / (union + 1e-6)
    return iou


def giou_loss(pred_boxes, target_boxes):
    """Generalized IoU Loss"""
    iou = calculate_iou(pred_boxes, target_boxes)
    
    # Smallest enclosing box
    c_x1 = torch.min(pred_boxes[..., 0], target_boxes[..., 0])
    c_y1 = torch.min(pred_boxes[..., 1], target_boxes[..., 1])
    c_x2 = torch.max(pred_boxes[..., 2], target_boxes[..., 2])
    c_y2 = torch.max(pred_boxes[..., 3], target_boxes[..., 3])
    
    c_area = (c_x2 - c_x1) * (c_y2 - c_y1)
    union = (pred_boxes[..., 2] - pred_boxes[..., 0]) * (pred_boxes[..., 3] - pred_boxes[..., 1]) + \
            (target_boxes[..., 2] - target_boxes[..., 0]) * (target_boxes[..., 3] - target_boxes[..., 1]) - \
            iou * ((c_x2 - c_x1) * (c_y2 - c_y1))
    
    giou = iou - (c_area - union) / (c_area + 1e-6)
    return 1 - giou
```

---

## 4.3 Semantic Segmentation

Semantic segmentation assigns a class label to every pixel in an image.

### U-Net Architecture

U-Net uses a symmetric encoder-decoder structure with skip connections:

```python
class UNet(nn.Module):
    """U-Net for semantic segmentation"""
    
    def __init__(self, in_channels=3, num_classes=21):
        super().__init__()
        
        # Encoder (downsampling)
        self.enc1 = self._block(in_channels, 64)
        self.enc2 = self._block(64, 128)
        self.enc3 = self._block(128, 256)
        self.enc4 = self._block(256, 512)
        
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Bottleneck
        self.bottleneck = self._block(512, 1024)
        
        # Decoder (upsampling)
        self.upconv4 = nn.ConvTranspose2d(1024, 512, kernel_size=2, stride=2)
        self.dec4 = self._block(1024, 512)
        
        self.upconv3 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.dec3 = self._block(512, 256)
        
        self.upconv2 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec2 = self._block(256, 128)
        
        self.upconv1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec1 = self._block(128, 64)
        
        # Final convolution
        self.final = nn.Conv2d(64, num_classes, kernel_size=1)
    
    def _block(self, in_channels, out_channels):
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        enc1 = self.enc1(x)
        enc2 = self.enc2(self.pool(enc1))
        enc3 = self.enc3(self.pool(enc2))
        enc4 = self.enc4(self.pool(enc3))
        
        # Bottleneck
        bottleneck = self.bottleneck(self.pool(enc4))
        
        # Decoder with skip connections
        dec4 = self.upconv4(bottleneck)
        dec4 = torch.cat([dec4, enc4], dim=1)
        dec4 = self.dec4(dec4)
        
        dec3 = self.upconv3(dec4)
        dec3 = torch.cat([dec3, enc3], dim=1)
        dec3 = self.dec3(dec3)
        
        dec2 = self.upconv2(dec3)
        dec2 = torch.cat([dec2, enc2], dim=1)
        dec2 = self.dec2(dec2)
        
        dec1 = self.upconv1(dec2)
        dec1 = torch.cat([dec1, enc1], dim=1)
        dec1 = self.dec1(dec1)
        
        return self.final(dec1)
```

### DeepLabV3+ Architecture

DeepLab uses atrous convolutions and spatial pyramid pooling:

```python
class AtrousConvolution(nn.Module):
    """Atrous (dilated) convolution"""
    
    def __init__(self, in_channels, out_channels, rate=1):
        super().__init__()
        self.conv = nn.Conv2d(
            in_channels, out_channels, kernel_size=3,
            padding=rate, dilation=rate, bias=False
        )
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
    
    def forward(self, x):
        return self.relu(self.bn(self.conv(x)))


class ASPP(nn.Module):
    """Atrous Spatial Pyramid Pooling"""
    
    def __init__(self, in_channels, out_channels=256, rates=[6, 12, 18]):
        super().__init__()
        
        # Global average pooling
        self.global_pool = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
        
        # Atrous convolutions at different rates
        self.atrous_convs = nn.ModuleList([
            AtrousConvolution(in_channels, out_channels, rate)
            for rate in rates
        ])
        
        # 1x1 convolution
        self.conv1x1 = AtrousConvolution(in_channels, out_channels, rate=1)
        
        # Final fusion
        self.fusion = nn.Sequential(
            nn.Conv2d(out_channels * 5, out_channels, kernel_size=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5)
        )
    
    def forward(self, x):
        # Global pooling branch
        global_feat = self.global_pool(x)
        global_feat = nn.functional.interpolate(
            global_feat, size=x.shape[2:], mode='bilinear', align_corners=False
        )
        
        # Collect all branches
        features = [self.conv1x1(x)]
        features.extend([conv(x) for conv in self.atrous_convs])
        features.append(global_feat)
        
        # Concatenate and fuse
        x = torch.cat(features, dim=1)
        return self.fusion(x)


class DeepLabV3Plus(nn.Module):
    """DeepLabV3+ architecture"""
    
    def __init__(self, num_classes=21, backbone='resnet50'):
        super().__init__()
        
        # Backbone
        resnet = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
        self.layer0 = nn.Sequential(resnet.conv1, resnet.bn1, resnet.relu, resnet.maxpool)
        self.layer1 = resnet.layer1
        self.layer2 = resnet.layer2
        self.layer3 = resnet.layer3
        self.layer4 = resnet.layer4
        
        # ASPP
        self.aspp = ASPP(2048, 256)
        
        # Low-level features from layer1
        self.low_level_conv = nn.Sequential(
            nn.Conv2d(256, 48, kernel_size=1, bias=False),
            nn.BatchNorm2d(48),
            nn.ReLU(inplace=True)
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Conv2d(256 + 48, 256, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, num_classes, kernel_size=1)
        )
    
    def forward(self, x):
        # Backbone
        x0 = self.layer0(x)
        x1 = self.layer1(x0)      # Low-level features (C1)
        x2 = self.layer2(x1)
        x3 = self.layer3(x2)
        x4 = self.layer4(x3)      # High-level features (C4)
        
        # ASPP on high-level features
        x4 = self.aspp(x4)
        x4 = nn.functional.interpolate(
            x4, size=x1.shape[2:], mode='bilinear', align_corners=False
        )
        
        # Low-level features
        x1 = self.low_level_conv(x1)
        
        # Fuse
        x = torch.cat([x4, x1], dim=1)
        x = self.decoder(x)
        
        # Upsample to input size
        x = nn.functional.interpolate(
            x, size=x.shape[2:] * 4, mode='bilinear', align_corners=False
        )
        
        return x
```

### Segmentation Loss Functions

```python
class DiceLoss(nn.Module):
    """Dice loss for segmentation"""
    
    def __init__(self, smooth=1.0):
        super().__init__()
        self.smooth = smooth
    
    def forward(self, pred, target):
        pred = torch.sigmoid(pred)
        pred = pred.view(-1)
        target = target.view(-1)
        
        intersection = (pred * target).sum()
        dice = (2. * intersection + self.smooth) / (pred.sum() + target.sum() + self.smooth)
        
        return 1 - dice


class FocalLoss(nn.Module):
    """Focal loss for handling class imbalance"""
    
    def __init__(self, alpha=0.25, gamma=2.0):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
    
    def forward(self, pred, target):
        ce_loss = nn.functional.cross_entropy(pred, target, reduction='none')
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha * (1 - pt) ** self.gamma * ce_loss
        return focal_loss.mean()


class CombinedSegmentationLoss(nn.Module):
    """Combine cross-entropy and dice loss"""
    
    def __init__(self, ce_weight=0.5, dice_weight=0.5):
        super().__init__()
        self.ce_weight = ce_weight
        self.dice_weight = dice_weight
        self.ce_loss = nn.CrossEntropyLoss()
        self.dice_loss = DiceLoss()
    
    def forward(self, pred, target):
        ce = self.ce_loss(pred, target)
        dice = self.dice_loss(pred, target)
        return self.ce_weight * ce + self.dice_weight * dice
```

---

## 4.4 Instance Segmentation

Instance segmentation combines object detection and semantic segmentation to identify individual object instances.

### Mask R-CNN Architecture

Mask R-CNN extends Faster R-CNN with a mask prediction branch:

```python
class MaskRCNN(nn.Module):
    """Mask R-CNN for instance segmentation"""
    
    def __init__(self, num_classes, mask_size=14):
        super().__init__()
        
        # Backbone + RPN + ROI Head (same as Faster R-CNN)
        self.backbone = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
        # ... (RPN and ROI components)
        
        # Mask branch
        self.mask_branch = nn.Sequential(
            nn.Conv2d(1024, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(256, 256, kernel_size=2, stride=2),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(256, 256, kernel_size=2, stride=2),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, num_classes, kernel_size=1)
        )
    
    def forward(self, x, proposals=None):
        # Feature extraction
        features = self.backbone(x)
        
        # ... (RPN and ROI processing)
        
        # Mask prediction
        if proposals is not None:
            # ROI Align for masks (better than ROI Pool)
            roi_features = self.roi_align(features, proposals)
            masks = self.mask_branch(roi_features)
            return masks
        
        return features
```

---

## 4.5 Image Generation with CNNs

### Generative Adversarial Networks (GANs)

DCGAN (Deep Convolutional GAN) architecture:

```python
class Generator(nn.Module):
    """DCGAN Generator"""
    
    def __init__(self, latent_dim=100, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.network = nn.Sequential(
            # Input: (batch, latent_dim, 1, 1)
            nn.ConvTranspose2d(latent_dim, feature_dim * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(feature_dim * 8),
            nn.ReLU(True),
            # State: (batch, 512, 4, 4)
            
            nn.ConvTranspose2d(feature_dim * 8, feature_dim * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 4),
            nn.ReLU(True),
            # State: (batch, 256, 8, 8)
            
            nn.ConvTranspose2d(feature_dim * 4, feature_dim * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 2),
            nn.ReLU(True),
            # State: (batch, 128, 16, 16)
            
            nn.ConvTranspose2d(feature_dim * 2, feature_dim, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim),
            nn.ReLU(True),
            # State: (batch, 64, 32, 32)
            
            nn.ConvTranspose2d(feature_dim, img_channels, 4, 2, 1, bias=False),
            nn.Tanh()
            # Output: (batch, 3, 64, 64)
        )
    
    def forward(self, z):
        z = z.view(z.size(0), -1, 1, 1)
        return self.network(z)


class Discriminator(nn.Module):
    """DCGAN Discriminator"""
    
    def __init__(self, img_channels=3, feature_dim=64):
        super().__init__()
        
        self.network = nn.Sequential(
            # Input: (batch, 3, 64, 64)
            nn.Conv2d(img_channels, feature_dim, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (batch, 64, 32, 32)
            
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (batch, 128, 16, 16)
            
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (batch, 256, 8, 8)
            
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # State: (batch, 512, 4, 4)
            
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
            # Output: (batch, 1, 1, 1) probability
        )
    
    def forward(self, x):
        return self.network(x).view(-1, 1)
```

### GAN Training Loop

```python
def train_gan(generator, discriminator, dataloader, epochs, lr=0.0002):
    """Train DCGAN"""
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    generator = generator.to(device)
    discriminator = discriminator.to(device)
    
    # Optimizers
    opt_g = torch.optim.Adam(generator.parameters(), lr=lr, betas=(0.5, 0.999))
    opt_d = torch.optim.Adam(discriminator.parameters(), lr=lr, betas=(0.5, 0.999))
    
    # Loss
    criterion = nn.BCELoss()
    
    fixed_noise = torch.randn(64, 100, 1, 1).to(device)
    
    for epoch in range(epochs):
        for i, (real_images, _) in enumerate(dataloader):
            batch_size = real_images.size(0)
            real_images = real_images.to(device)
            
            # Labels
            real_labels = torch.ones(batch_size, 1).to(device)
            fake_labels = torch.zeros(batch_size, 1).to(device)
            
            # --- Train Discriminator ---
            opt_d.zero_grad()
            
            # Real images
            d_real = discriminator(real_images)
            d_loss_real = criterion(d_real, real_labels)
            
            # Fake images
            noise = torch.randn(batch_size, 100, 1, 1).to(device)
            fake_images = generator(noise)
            d_fake = discriminator(fake_images.detach())
            d_loss_fake = criterion(d_fake, fake_labels)
            
            d_loss = (d_loss_real + d_loss_fake) / 2
            d_loss.backward()
            opt_d.step()
            
            # --- Train Generator ---
            opt_g.zero_grad()
            
            g_fake = discriminator(fake_images)
            g_loss = criterion(g_fake, real_labels)
            g_loss.backward()
            opt_g.step()
            
            if i % 100 == 0:
                print(f"Epoch [{epoch}/{epochs}] Step [{i}/{len(dataloader)}] "
                      f"D Loss: {d_loss.item():.4f} G Loss: {g_loss.item():.4f}")
        
        # Save generated samples
        with torch.no_grad():
            fake = generator(fixed_noise).detach().cpu()
            # Save or visualize fake images
```

---

## 4.6 Practical Implementation Guide

### Using Pretrained Models

```python
import torchvision

# Object Detection
detector = torchvision.models.detection.fasterrcnn_resnet50_fpn(
    weights=torchvision.models.detection.FasterRCNN_ResNet50_FPN_Weights.COCO_V1
)
detector.eval()

# With custom classes
detector_custom = torchvision.models.detection.fasterrcnn_resnet50_fpn(
    pretrained=False,
    num_classes=10  # Your number of classes
)

# Semantic Segmentation
segmenter = torchvision.models.segmentation.deeplabv3_resnet50(
    weights=torchvision.models.segmentation.DeepLabV3_ResNet50_Weights.COCO_WITH_VOC_LABELS_V1
)

# Instance Segmentation
mask_rcnn = torchvision.models.detection.maskrcnn_resnet50_fpn(
    weights=torchvision.models.detection.MaskRCNN_ResNet50_FPN_Weights.COCO_V1
)
```

### Inference Example

```python
@torch.no_grad()
def detect_objects(image, model, threshold=0.5):
    """Run object detection inference"""
    model.eval()
    
    # Prepare image
    if isinstance(image, np.ndarray):
        image = torch.from_numpy(image).permute(2, 0, 1).float() / 255.0
    
    # Run detection
    predictions = model([image])
    
    # Filter by threshold
    boxes = predictions[0]['boxes']
    scores = predictions[0]['scores']
    labels = predictions[0]['labels']
    
    mask = scores > threshold
    filtered_boxes = boxes[mask]
    filtered_scores = scores[mask]
    filtered_labels = labels[mask]
    
    return {
        'boxes': filtered_boxes.cpu().numpy(),
        'scores': filtered_scores.cpu().numpy(),
        'labels': filtered_labels.cpu().numpy()
    }
```

---

## Exercises

### Exercise 4.1: Implement YOLO Loss
Implement the complete YOLO loss function including box regression, objectness, and classification losses. Train on a small dataset like Pascal VOC.

### Exercise 4.2: Build U-Net from Scratch
Implement U-Net and train it on the Oxford-IIIT Pet Dataset for semantic segmentation. Compare performance with and without skip connections.

### Exercise 4.3: Train DCGAN
Train a DCGAN on CIFAR-10 or CelebA dataset. Experiment with different architectures and observe how they affect generated image quality.

### Exercise 4.4: Fine-tune Mask R-CNN
Fine-tune a pretrained Mask R-CNN on a custom dataset for instance segmentation. Create annotations using tools like LabelMe or CVAT.

### Exercise 4.5: Multi-Task Learning
Build a network that performs both object detection and semantic segmentation simultaneously. Share the backbone and have separate heads for each task.

---

## Summary

This chapter explored specialized CNN applications:

1. **Object Detection**: Two-stage (Faster R-CNN) and one-stage (YOLO) detectors
2. **Semantic Segmentation**: U-Net and DeepLab architectures for pixel-wise classification
3. **Instance Segmentation**: Mask R-CNN for identifying individual object instances
4. **Image Generation**: GANs for generating realistic images
5. **Practical Tools**: Using pretrained models and implementing inference pipelines

These advanced techniques enable CNNs to solve complex real-world vision problems beyond simple classification. Master them to build powerful computer vision systems for diverse applications.

---

**Congratulations!** You've completed the CNN Training Guide. You now have comprehensive knowledge of CNN architectures, training techniques, and specialized applications. Continue practicing with real projects to deepen your expertise!
