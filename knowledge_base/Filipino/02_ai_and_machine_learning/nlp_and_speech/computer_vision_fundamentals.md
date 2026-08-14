---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
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
# Computer Vision Fundamentals
Binibigyan ng computer vision ang mga makina ng kakayahang magbigay-kahulugan at maunawaan ang visual na impormasyon mula sa mundo — mga larawan, video, at 3D na data. Pinapatakbo nito ang lahat mula sa pagkilala sa mukha sa iyong telepono hanggang sa mga self-driving na kotse, pagsusuri ng medikal na larawan, at pang-industriyang kontrol sa kalidad. Sinasaklaw ng file na ito ang mga pangunahing konsepto, arkitektura, at diskarte.
---

## Paano Nakikita ng Mga Computer ang Mga Larawan
### Mga Pixel at Channel
Ang isang digital na imahe ay isang grid ng mga pixel. Ang bawat pixel ay may mga numerical na halaga na kumakatawan sa intensity ng kulay.
| Uri ng Larawan | Mga Channel | Mga halaga sa bawat Pixel | Halimbawa |
|-----------|----------|----------------|---------|
| **Grayscale** | 1 | 0 (itim) hanggang 255 (puti) | Medikal na X-ray |
| **RGB** | 3 | Pula, Berde, Asul (bawat 0–255) | Mga karaniwang kulay na larawan |
| ** RGBA** | 4 | RGB + Alpha (transparency) | Mga larawang may transparent na background |
| **HSV** | 3 | Hue, Saturation, Value | Nakabatay sa kulay na segmentation |
Ang 1920×1080 RGB na imahe ay isang tensor ng hugis`(1080, 1920, 3)`— iyon ay 6.2 milyong pixel, bawat isa ay may 3 value.
### Mga Pangunahing Operasyon
| Operasyon | Paglalarawan |
|-----------|-------------|
| **Pagbabago ng laki** | I-scale ang larawan sa mga target na dimensyon (bilinear, pinakamalapit-kapitbahay interpolation) |
| **Pag-crop** | I-extract ang isang rehiyon ng interes |
| **Normalization** | I-scale ang mga halaga ng pixel sa [0,1] o [-1,1] para sa mga neural network |
| **Pagpapalaki** | Artipisyal na palawakin ang data ng pagsasanay (pag-ikot, flip, color jitter, crop) |
---

## Convolution: Ang Pangunahing Operasyon
Ang isang convolution ay nag-slide ng isang maliit na filter (kernel) sa buong imahe, na nagko-compute ng mga produkto ng tuldok sa bawat posisyon. Ito ay kung paano natukoy ng mga CNN ang mga gilid, texture, at pattern.
### Mga Parameter ng Convolution
| Parameter | Epekto |
|-----------|--------|
| **Laki ng kernel** | 3×3, 5×5, 7×7 — mas malalaking kernel ang kumukuha ng mas malalaking pattern |
| **Hakbang** | Laki ng hakbang; stride=2 hinahati ang mga sukat ng output |
| **Padding** | Magdagdag ng mga zero sa paligid ng hangganan upang mapanatili ang mga spatial na dimensyon |
| **Bilang ng mga filter** | Natututo ang bawat filter ng ibang feature (gilid, texture, pattern ng kulay) |
### Ano ang Natutuhan ng Mga Convolution
| Lalim ng Layer | Natukoy ang Mga Tampok |
|-------------|------------------|
| **Maagang mga layer** | Mga gilid, sulok, simpleng texture |
| **Mga gitnang layer** | Mga hugis, bahagi ng bagay (gulong, mata, dahon) |
| **Malalim na layer** | Mga konseptong may mataas na antas (mukha, kotse, hayop) |
---

## Mga Arkitektura ng CNN
Ang ebolusyon ng mga arkitektura ng CNN ay nagsasabi sa kuwento ng malalim na pag-unlad ng pag-aaral sa computer vision.
| Arkitektura | Taon | Pangunahing Pagbabago |
|-------------|------|----------------|
| **LeNet-5** | 1998 | Unang praktikal na CNN; pagkilala sa digit |
| **AlexNet** | 2012 | Nanalo ang Deep CNN sa ImageNet; ReLU, dropout, GPU training |
| **VGGNet** | 2014 | Naka-stack na 3×3 convolutions (mas malalim = mas maganda) |
| **GoogLeNet (Inception)** | 2014 | Mga module ng pagsisimula (parallel na laki ng filter); 22 layer |
| **ResNet** | 2015 | Laktawan ang mga koneksyon (tirang pag-aaral); 152+ na layer |
| **EfficientNet** | 2019 | Compound scaling (depth + width + resolution) |
| **ConvNeXt** | 2022 | Modernized ResNet; mapagkumpitensya sa Transformers |
### Bakit Binago ng ResNet ang Lahat
Bago ang ResNet, halos imposible ang pagsasanay sa mga napakalalim na network dahil sa nawawalang problema sa gradient. Ipinakilala ng ResNet ang **laktawan ang mga koneksyon** (tinatawag ding mga natitirang koneksyon): ang input sa isang layer ay idinaragdag sa output nito.
```
output = F(x) + x    # Skip connection
```

Ang simpleng ideyang ito ay nagbigay-daan sa mga network na may 152+ na layer na mabisang sanayin, at ito ay pamantayan na ngayon sa halos lahat ng malalalim na arkitektura.
---

## Mga Pangunahing Gawain sa Pananaw
### Pag-uuri ng Larawan
Magtalaga ng label sa isang buong larawan.
| Modelo | Diskarte |
|-------|----------|
| Mga CNN (ResNet, EfficientNet) | Tradisyunal na diskarte; mahusay na katumpakan |
| Vision Transformers (ViT) | Tratuhin ang imahe bilang pagkakasunud-sunod ng mga patch; Transformer encoder |
| Transfer Learning | I-fine-tune ang isang pre-trained na modelo sa iyong dataset |
### Object Detection
Maghanap at pag-uri-uriin ang maramihang mga bagay sa loob ng isang imahe, na may mga nakatali na kahon.
| Modelo | Uri | Bilis |
|-------|------|-------|
| **R-CNN** | Dalawang yugto (panukala + pag-uuri) | Mabagal |
| **Mabilis na R-CNN** | Pinahusay na dalawang yugto | Katamtaman |
| **Mas mabilis na R-CNN** | Rehiyon Proposal Network + detector | Katamtaman |
| **YOLO** (v1–v10) | Isang yugto; hulaan ang mga kahon + mga klase sa isang pass | Napakabilis |
| **DETR** | Nakabatay sa transpormer; walang mga anchor box | Katamtaman |
**YOLO** (Minsan Ka Lang Tumingin) ay ang go-to para sa real-time na pag-detect. Mas pinipili ang **Mas mabilis na R-CNN** kapag mas mahalaga ang katumpakan kaysa bilis.
### Segmentation ng Larawan
Uriin ang bawat pixel sa isang larawan.
| Uri | Paglalarawan | Use Case |
|------|-------------|----------|
| **Semantic Segmentation** | Ang bawat pixel ay nakakakuha ng label ng klase | Autonomous na pagmamaneho (kalsada, kotse, pedestrian) |
| **Instance Segmentation** | Ang bawat pixel + object instance ID | Nagbibilang ng mga bagay, medikal na imaging |
| **Panoptic Segmentation** | Pinagsamang semantic + instance | Komprehensibong pag-unawa sa eksena |
Mga pangunahing modelo: U-Net (medical imaging), Mask R-CNN (halimbawa), DeepLab (semantic), Segment Anything Model (SAM — universal segmentation).
### Pagbuo ng Larawan
| Diskarte | Paglalarawan | Mga halimbawa |
|----------|-------------|----------|
| **GANs** | Generator vs discriminator adversarial training | StyleGAN, CycleGAN |
| **VAEs** | Alamin ang nakatagong pamamahagi; sample upang makabuo ng | Variational Autoencoders |
| **Mga Modelo ng Pagsasabog** | Paulit-ulit na i-denoise ang random na ingay | Stable Diffusion, DALL-E, Midjourney |
Ang mga modelo ng pagsasabog ay higit na nalampasan ang mga GAN para sa kalidad ng pagbuo ng imahe.
---

## Ilipat ang Pag-aaral para sa Paningin
Ang pagsasanay sa isang CNN mula sa simula ay nangangailangan ng napakalaking data at pagkalkula. Nagbibigay-daan sa iyo ang paglipat ng pag-aaral na magsimula sa isang modelong sinanay na sa milyun-milyong larawan (ImageNet) at i-fine-tune ito para sa iyong partikular na gawain.
### Mga hakbang
1. **Pumili ng isang pre-trained na modelo** (ResNet50, EfficientNet-B0, ViT).
2. **Palitan ang ulo ng pag-uuri** ng sarili mong (tutugma sa iyong bilang ng mga klase).
3. **I-freeze ang mga maagang layer** (nakakakuha sila ng mga generic na feature tulad ng mga gilid).
4. **Fine-tune** sa iyong dataset na may mababang rate ng pagkatuto.
5. **Unfreeze nang paunti-unti** kung kailangan mo ng higit pang adaptation.
Ang diskarteng ito ay regular na nakakamit ng mataas na katumpakan na may kasing kaunti sa 1,000–10,000 na may label na mga larawan.
---

## Pagpapalaki ng Data
Artipisyal na pinapalawak ng pagpapalaki ang iyong dataset ng pagsasanay sa pamamagitan ng paglalapat ng mga pagbabago.
| Pagpapalaki | Epekto | Kailan Gagamitin |
|-------------|--------|-------------|
| **Random na pag-crop** | I-crop sa random na rehiyon | Halos palaging |
| **Pahalang na flip** | Larawan ng salamin | Kapag hindi mahalaga ang oryentasyon |
| **Pag-ikot** | I-rotate ayon sa random na anggulo | Kapag lumitaw ang mga bagay sa anumang anggulo |
| **Colour jitter** | Random na isaayos ang liwanag, kaibahan, saturation | Kapag nag-iiba ang liwanag |
| **Random na binubura** | I-mask ang mga random na rehiyon | Nagpapabuti ng katatagan |
| **Mixup / CutMix** | Paghaluin ang dalawang larawan at label | Regularisasyon |
Mga Aklatan:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **OpenCV** | Mga klasikong pagpapatakbo ng CV (pag-filter, pagtuklas ng gilid, mga geometric na pagbabago) |
| **torchvision** | PyTorch vision models, transforms, datasets |
| **tf.keras.applications** | Mga pre-trained na modelo sa TensorFlow/Keras |
| **Ultralytics (YOLOv8/v11)** | Pagtuklas ng bagay, pagse-segment, pag-uuri |
| **Hugging Face (transformers)** | Mga Transformer ng Vision, SegFormer, DETR |
| **Segment Anything (SAM)** | Pangkalahatang segmentasyon ng imahe mula sa Meta |
| **Albumentations** | Mabilis, nababaluktot na library ng augmentation ng imahe |
---

## Mga Praktikal na Tip
- **Magsimula sa paglipat ng pag-aaral.** Ang pag-fine-tune ng isang pre-trained na modelo ay higit pa sa pagsasanay mula sa simula sa halos lahat ng kaso.
- **I-normalize ang iyong mga input.** Itugma ang normalisasyon na inaasahan ng pre-trained na modelo (karaniwan ay ImageNet mean/std).
- **Gumamit ng mga naaangkop na sukatan.** Katumpakan para sa mga balanseng dataset; F1, mAP, o IoU para sa mga gawaing hindi balanse o pagtuklas.
- **I-visualize ang iyong data.** Tumingin sa mga sample na larawan, suriin ang mga pamamahagi ng klase, suriin ang mga hula ng modelo.
- **Palakihin nang matalino.** Ilapat lamang ang mga pagbabagong may katuturan para sa iyong domain (huwag i-flip ang mga medikal na larawan nang patayo).
- **Subaybayan ang overfitting.** Kung mataas ang katumpakan ng pagsasanay ngunit mababa ang validation, dagdagan ang augmentation o magdagdag ng dropout.