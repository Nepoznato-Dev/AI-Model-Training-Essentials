<!--
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

-->
# Grundlagen der Computer Vision
Computer Vision gibt Maschinen die Fähigkeit, visuelle Informationen aus der Welt – Bilder, Videos und 3D-Daten – zu interpretieren und zu verstehen. Es ermöglicht alles von der Gesichtserkennung auf Ihrem Telefon bis hin zu selbstfahrenden Autos, medizinischer Bildanalyse und industrieller Qualitätskontrolle. Diese Datei behandelt die Kernkonzepte, Architekturen und Techniken.
---

## Wie Computer Bilder sehen
### Pixel und Kanäle
Ein digitales Bild ist ein Pixelraster. Jedes Pixel verfügt über numerische Werte, die die Farbintensität darstellen.
| Bildtyp | Kanäle | Werte pro Pixel | Beispiel |
|-----------|----------|-----------------|---------|
| **Graustufen** | 1 | 0 (schwarz) bis 255 (weiß) | Medizinische Röntgenaufnahmen |
| **RGB** | 3 | Rot, Grün, Blau (jeweils 0–255) | Standard-Farbfotos |
| **RGBA** | 4 | RGB + Alpha (Transparenz) | Bilder mit transparentem Hintergrund |
| **HSV** | 3 | Farbton, Sättigung, Wert | Farbbasierte Segmentierung |
Ein 1920×1080 RGB-Bild ist ein Tensor der Form`(1080, 1920, 3)`– das sind 6,2 Millionen Pixel mit jeweils 3 Werten.
### Schlüsseloperationen
| Betrieb | Beschreibung |
|-----------|-------------|
| **Größenänderung** | Bild auf Zielabmessungen skalieren (bilinear, Interpolation des nächsten Nachbarn) |
| **Zuschneiden** | Einen interessierenden Bereich extrahieren |
| **Normalisierung** | Pixelwerte für neuronale Netze auf [0,1] oder [-1,1] skalieren |
| **Erweiterung** | Trainingsdaten künstlich erweitern (Rotation, Flip, Farbjitter, Zuschneiden) |
---

## Faltung: Die Kernoperation
Eine Faltung verschiebt einen kleinen Filter (Kernel) über das Bild und berechnet Skalarprodukte an jeder Position. Auf diese Weise erkennen CNNs Kanten, Texturen und Muster.
### Faltungsparameter
| Parameter | Wirkung |
|-----------|--------|
| **Kernelgröße** | 3×3, 5×5, 7×7 – größere Kernel erfassen größere Muster |
| **Schritt** | Schrittgröße; stride=2 halbiert die Ausgabeabmessungen |
| **Polsterung** | Fügen Sie am Rand Nullen hinzu, um die räumlichen Abmessungen beizubehalten |
| **Anzahl der Filter** | Jeder Filter lernt eine andere Funktion (Kante, Textur, Farbmuster) |
### Was Faltungen lernen
| Ebenentiefe | Erkannte Merkmale |
|-------------|------------------|
| **Frühe Schichten** | Kanten, Ecken, einfache Texturen |
| **Mittelschichten** | Formen, Objektteile (Räder, Augen, Blätter) |
| **Tiefe Schichten** | Hochrangige Konzepte (Gesichter, Autos, Tiere) |
---

## CNN-Architekturen
Die Entwicklung der CNN-Architekturen erzählt die Geschichte des Fortschritts von Deep Learning in der Computer Vision.
| Architektur | Jahr | Schlüsselinnovation |
|-------------|------|---------------|
| **LeNet-5** | 1998 | Erstes praktisches CNN; Ziffernerkennung |
| **AlexNet** | 2012 | Deep CNN gewinnt ImageNet; ReLU, Dropout, GPU-Training |
| **VGGNet** | 2014 | Gestapelte 3×3 Windungen (tiefer = besser) |
| **GoogLeNet (Inception)** | 2014 | Inception-Module (parallele Filtergrößen); 22 Schichten |
| **ResNet** | 2015 | Verbindungen überspringen (Restlernen); 152+ Schichten |
| **EfficientNet** | 2019 | Zusammengesetzte Skalierung (Tiefe + Breite + Auflösung) |
| **ConvNeXt** | 2022 | Modernisiertes ResNet; konkurrenzfähig mit Transformers |
### Warum ResNet alles verändert hat
Vor ResNet war das Training sehr tiefer Netzwerke aufgrund des Problems des verschwindenden Gradienten nahezu unmöglich. ResNet hat **Verbindungen überspringen** (auch Restverbindungen genannt) eingeführt: Die Eingabe einer Ebene wird zu ihrer Ausgabe hinzugefügt.
```
output = F(x) + x    # Skip connection
```

Diese einfache Idee ermöglichte ein effektives Training von Netzwerken mit mehr als 152 Schichten und ist mittlerweile in praktisch allen tiefen Architekturen Standard.
---

## Kernaufgaben der Vision
### Bildklassifizierung
Weisen Sie einem gesamten Bild eine Beschriftung zu.
| Modell | Ansatz |
|-------|----------|
| CNNs (ResNet, EfficientNet) | Traditioneller Ansatz; ausgezeichnete Genauigkeit |
| Vision Transformers (ViT) | Behandeln Sie das Bild als Folge von Patches. Transformator-Encoder |
| Transferlernen | Feinabstimmung eines vorab trainierten Modells für Ihren Datensatz |
### Objekterkennung
Finden und klassifizieren Sie mehrere Objekte innerhalb eines Bildes mit Begrenzungsrahmen.
| Modell | Geben Sie | ein Geschwindigkeit |
|-------|------|-------|
| **R-CNN** | Zweistufig (Vorschlag + Klassifizierung) | Langsam |
| **Schnelles R-CNN** | Verbesserte zweistufige | Mittel |
| **Schnelleres R-CNN** | Regionsvorschlag Netzwerk + Detektor | Mittel |
| **YOLO** (v1–v10) | Einstufig; Vorhersageboxen + Klassen in einem Durchgang | Sehr schnell |
| **DETR** | Transformatorbasiert; keine Ankerkästen | Mittel |
**YOLO** (You Only Look Once) ist die erste Wahl für die Echtzeiterkennung. **Schnelleres R-CNN** wird bevorzugt, wenn Genauigkeit wichtiger ist als Geschwindigkeit.
### Bildsegmentierung
Klassifizieren Sie jedes Pixel in einem Bild.
| Geben Sie | ein Beschreibung | Anwendungsfall |
|------|-------------|----------|
| **Semantische Segmentierung** | Jedes Pixel erhält eine Klassenbezeichnung | Autonomes Fahren (Straße, Auto, Fußgänger) |
| **Instanzsegmentierung** | Jedes Pixel + Objektinstanz-ID | Zählen von Objekten, medizinische Bildgebung |
| **Panoptische Segmentierung** | Semantik + Instanz kombiniert | Umfassendes Szenenverständnis |
Schlüsselmodelle: U-Net (medizinische Bildgebung), Mask R-CNN (Instanz), DeepLab (Semantik), Segment Anything Model (SAM – universelle Segmentierung).
### Bildgenerierung
| Ansatz | Beschreibung | Beispiele |
|----------|-------------|----------|
| **GANs** | Konfrontatives Training zwischen Generator und Diskriminator | StyleGAN, CycleGAN |
| **VAEs** | Lernen Sie die latente Verteilung kennen; Beispiel zum Generieren | Variationale Autoencoder |
| **Diffusionsmodelle** | Zufälliges Rauschen iterativ entstören | Stabile Diffusion, DALL-E, Midjourney |
Diffusionsmodelle haben GANs hinsichtlich der Qualität der Bilderzeugung weit übertroffen.
---

## Transferlernen für Vision
Das Training eines CNN von Grund auf erfordert enorme Datenmengen und Rechenleistung. Durch Transferlernen können Sie mit einem Modell beginnen, das bereits auf Millionen von Bildern trainiert wurde (ImageNet), und es für Ihre spezifische Aufgabe optimieren.
### Schritte
1. **Wählen Sie ein vorab trainiertes Modell** (ResNet50, EfficientNet-B0, ViT).
2. **Ersetzen Sie den Klassifizierungskopf** durch Ihren eigenen (entsprechend Ihrer Klassenanzahl).
3. **Frühe Ebenen einfrieren** (sie erfassen allgemeine Merkmale wie Kanten).
4. **Feinabstimmung** Ihres Datensatzes mit einer niedrigen Lernrate.
5. **Nach und nach auftauen**, wenn Sie mehr Anpassung benötigen.
Dieser Ansatz erreicht routinemäßig eine hohe Genauigkeit mit nur 1.000–10.000 beschrifteten Bildern.
---

## Datenerweiterung
Augmentation erweitert Ihren Trainingsdatensatz künstlich durch die Anwendung von Transformationen.
| Erweiterung | Wirkung | Wann zu verwenden |
|-------------|--------|-------------|
| **Zufälliger Zuschnitt** | Auf zufälligen Bereich zuschneiden | Fast immer |
| **Horizontale Drehung** | Spiegelbild | Wenn die Orientierung keine Rolle spielt |
| **Rotation** | Um zufälligen Winkel drehen | Wenn Objekte in einem beliebigen Winkel erscheinen |
| **Farbjitter** | Passen Sie Helligkeit, Kontrast und Sättigung nach dem Zufallsprinzip an | Wenn die Beleuchtung variiert |
| **Zufälliges Löschen** | Zufällige Regionen maskieren | Verbessert die Robustheit |
| **Mixup / CutMix** | Zwei Bilder und Beschriftungen mischen | Regularisierung |
Bibliotheken: `torchvision.transforms`, `albumentations`, `imgaug`, `tf.keras.preprocessing`.
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **OpenCV** | Klassische CV-Operationen (Filterung, Kantenerkennung, geometrische Transformationen) |
| **Fackelvision** | PyTorch Vision-Modelle, Transformationen, Datensätze |
| **tf.keras.applications** | Vorab trainierte Modelle in TensorFlow/Keras |
| **Ultralytics (YOLOv8/v11)** | Objekterkennung, Segmentierung, Klassifizierung |
| **Umarmendes Gesicht (Transformer)** | Vision Transformers, SegFormer, DETR |
| **Alles segmentieren (SAM)** | Universelle Bildsegmentierung von Meta |
| **Albumierungen** | Schnelle, flexible Bilderweiterungsbibliothek |
---

## Praktische Tipps
- **Beginnen Sie mit dem Transferlernen.** Die Feinabstimmung eines vorab trainierten Modells ist in fast allen Fällen besser als ein Training von Grund auf.
- **Normalisieren Sie Ihre Eingaben.** Entsprechen Sie der Normalisierung, die das vorab trainierte Modell erwartet (normalerweise ImageNet-Mittelwert/Standard).
- **Verwenden Sie geeignete Metriken.** Genauigkeit für ausgewogene Datensätze; F1, mAP oder IoU für unausgeglichene oder Erkennungsaufgaben.
- **Visualisieren Sie Ihre Daten.** Sehen Sie sich Beispielbilder an, überprüfen Sie Klassenverteilungen und prüfen Sie Modellvorhersagen.
- **Mit Bedacht erweitern.** Wenden Sie nur Transformationen an, die für Ihre Domain sinnvoll sind (spiegeln Sie medizinische Bilder nicht vertikal).
- **Überanpassung überwachen.** Wenn die Trainingsgenauigkeit hoch, aber die Validierung niedrig ist, erhöhen Sie die Erweiterung oder fügen Sie Dropout hinzu.