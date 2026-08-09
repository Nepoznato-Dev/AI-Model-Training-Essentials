---
# Métadonnées
titre : « Fondamentaux de la vision par ordinateur »
description : "CNN, détection d'objets, segmentation, apprentissage par transfert"
catégorie : "IA et Machine Learning"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances sur l'IA et l'apprentissage automatique"
next_review : "2027-08-05"
#Classement
tags : [ordinateur, vision, IA et apprentissage automatique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "8 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Fondamentaux de la vision par ordinateur
La vision par ordinateur donne aux machines la capacité d’interpréter et de comprendre les informations visuelles du monde : images, vidéos et données 3D. Il gère tout, de la reconnaissance faciale sur votre téléphone aux voitures autonomes, en passant par l'analyse d'images médicales et le contrôle qualité industriel. Ce fichier couvre les concepts, architectures et techniques de base.
---

## Comment les ordinateurs voient les images
### Pixels et canaux
Une image numérique est une grille de pixels. Chaque pixel a des valeurs numériques représentant l'intensité de la couleur.
| Type d'image | Chaînes | Valeurs par pixel | Exemple |
|-----------|----------|-----------------|---------|
| **Niveaux de gris** | 1 | 0 (noir) à 255 (blanc) | Radiographies médicales |
| **RVB** | 3 | Rouge, Vert, Bleu (chacun 0-255) | Photos couleur standards |
| **RGBA** | 4 | RVB + Alpha (transparence) | Images avec fond transparent |
| **HSV** | 3 | Teinte, Saturation, Valeur | Segmentation basée sur la couleur |
Une image RVB 1920 × 1080 est un tenseur de forme`(1080, 1920, 3)`— soit 6,2 millions de pixels, chacun avec 3 valeurs.
### Opérations clés
| Opération | Descriptif |
|---------------|-------------|
| **Redimensionnement** | Mettre l'image à l'échelle aux dimensions cibles (interpolation bilinéaire du plus proche voisin) |
| **Recadrage** | Extraire une région d'intérêt |
| **Normalisation** | Mettez à l'échelle les valeurs des pixels sur [0,1] ou [-1,1] pour les réseaux de neurones |
| **Augmentation** | Étendre artificiellement les données d'entraînement (rotation, retournement, gigue de couleur, recadrage) |
---

## Convolution : l'opération de base
Une convolution fait glisser un petit filtre (noyau) sur l'image, calculant les produits scalaires à chaque position. C'est ainsi que les CNN détectent les bords, les textures et les motifs.
### Paramètres de convolution
| Paramètre | Effet |
|-----------|--------|
| **Taille du noyau** | 3×3, 5×5, 7×7 – des noyaux plus gros capturent des motifs plus grands |
| **Foulée** | Taille du pas ; stride=2 réduit de moitié les dimensions de sortie |
| **Rembourrage** | Ajoutez des zéros autour de la bordure pour préserver les dimensions spatiales |
| **Nombre de filtres** | Chaque filtre apprend une fonctionnalité différente (bord, texture, motif de couleur) |
### Ce que les circonvolutions apprennent
| Profondeur de couche | Fonctionnalités détectées |
|-------------|------------------|
| **Premières couches** | Bords, coins, textures simples |
| **Couches intermédiaires** | Formes, parties d'objets (roues, yeux, feuilles) |
| **Couches profondes** | Concepts de haut niveau (visages, voitures, animaux) |
---

## Architectures CNN
L'évolution des architectures CNN raconte l'histoire des progrès de l'apprentissage profond dans la vision par ordinateur.
| Architecture | Année | Innovation clé |
|-------------|------|--------------------|
| **LeNet-5** | 1998 | Premier CNN pratique ; reconnaissance de chiffres |
| **AlexNet** | 2012 | Deep CNN remporte ImageNet ; ReLU, abandon, formation GPU |
| **VGGNet** | 2014 | Convolutions 3×3 empilées (plus profondes = meilleures) |
| **GoogLeNet (Création)** | 2014 | Modules de création (tailles de filtres parallèles) ; 22 couches |
| **ResNet** | 2015 | Ignorer les connexions (apprentissage résiduel); 152+ couches |
| **EfficientNet** | 2019 | Mise à l'échelle composée (profondeur + largeur + résolution) |
| **ConvNeXt** | 2022 | ResNet modernisé ; compétitif avec les transformateurs |
### Pourquoi ResNet a tout changé
Avant ResNet, la formation de réseaux très profonds était presque impossible en raison du problème de gradient de disparition. ResNet a introduit les **connexions ignorées** (également appelées connexions résiduelles) : l'entrée d'une couche est ajoutée à sa sortie.
```
output = F(x) + x    # Skip connection
```

Cette idée simple a permis de former efficacement des réseaux comportant plus de 152 couches, et elle est désormais standard dans pratiquement toutes les architectures profondes.
---

## Tâches de vision principales
###Classement des images
Attribuez une étiquette à une image entière.
| Modèle | Approche |
|-------|--------------|
| CNN (ResNet, EfficientNet) | Approche traditionnelle ; excellente précision |
| Transformateurs de vision (ViT) | Traitez l'image comme une séquence de correctifs ; Encodeur de transformateur |
| Apprentissage par transfert | Affinez un modèle pré-entraîné sur votre ensemble de données |
### Détection d'objets
Recherchez et classez plusieurs objets dans une image, avec des cadres de délimitation.
| Modèle | Tapez | Vitesse |
|-------|------|-------|
| **R-CNN** | En deux étapes (proposition + classement) | Lent |
| **R-CNN rapide** | Amélioré en deux étapes | Moyen |
| **R-CNN plus rapide** | Réseau de propositions de région + détecteur | Moyen |
| **YOLO** (v1-v10) | En une seule étape ; prédire les boîtes + les classes en un seul passage | Très rapide |
| **DETR** | Basé sur un transformateur ; pas de boîtes d'ancrage | Moyen |
**YOLO** (You Only Look Once) est la référence en matière de détection en temps réel. **Un R-CNN plus rapide** est préférable lorsque la précision compte plus que la vitesse.
### Segmentation d'images
Classez chaque pixel d'une image.
| Tapez | Descriptif | Cas d'utilisation |
|------|-------------|--------------|
| **Segmentation sémantique** | Chaque pixel reçoit une étiquette de classe | Conduite autonome (route, voiture, piéton) |
| **Segmentation des instances** | Chaque pixel + ID d'instance d'objet | Comptage d'objets, imagerie médicale |
| **Segmentation panoptique** | Sémantique + instance combinées | Compréhension complète de la scène |
Modèles clés : U-Net (imagerie médicale), Mask R-CNN (instance), DeepLab (sémantique), Segment Anything Model (SAM — segmentation universelle).
### Génération d'images
| Approche | Descriptif | Exemples |
|--------------|-------------|--------------|
| **GAN** | Formation contradictoire générateur vs discriminateur | StyleGAN, CycleGAN |
| **VAE** | Apprendre la distribution latente ; échantillon à générer | Auto-encodeurs variationnels |
| **Modèles de diffusion** | Débruiter itérativement le bruit aléatoire | Diffusion stable, DALL-E, Midjourney |
Les modèles de diffusion ont largement dépassé les GAN en termes de qualité de génération d'images.
---

## Transférer l'apprentissage pour la vision
Former un CNN à partir de zéro nécessite des données et des calculs massifs. L'apprentissage par transfert vous permet de démarrer avec un modèle déjà formé sur des millions d'images (ImageNet) et de l'affiner pour votre tâche spécifique.
### Étapes
1. **Choisissez un modèle pré-entraîné** (ResNet50, EfficientNet-B0, ViT).
2. **Remplacez la tête de classification** par la vôtre (correspondant à votre nombre de classes).
3. **Geler les premières couches** (elles capturent des fonctionnalités génériques telles que les bords).
4. **Affinez** votre ensemble de données avec un faible taux d'apprentissage.
5. **Dégelez progressivement** si vous avez besoin de plus d'adaptation.
Cette approche permet généralement d’obtenir une grande précision avec seulement 1 000 à 10 000 images étiquetées.
---

## Augmentation des données
L'augmentation élargit artificiellement votre ensemble de données d'entraînement en appliquant des transformations.
| Augmentation | Effet | Quand utiliser |
|-------------|--------|-------------|
| **Récolte aléatoire** | Recadrer dans une région aléatoire | Presque toujours |
| **Retournement horizontal** | Image miroir | Quand l'orientation n'a pas d'importance |
| **Rotation** | Rotation selon un angle aléatoire | Quand les objets apparaissent sous n'importe quel angle |
| **Gigue de couleur** | Ajustez aléatoirement la luminosité, le contraste et la saturation | Quand l'éclairage varie |
| **Effacement aléatoire** | Masquer les régions aléatoires | Améliore la robustesse |
| **Mixup / CutMix** | Mélanger deux images et étiquettes | Régularisation |
Bibliothèques :`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **OpenCV** | Opérations CV classiques (filtrage, détection de contours, transformations géométriques) |
| **vision au flambeau** | Modèles de vision PyTorch, transformations, ensembles de données |
| **tf.keras.applications** | Modèles pré-entraînés dans TensorFlow/Keras |
| **Ultralytique (YOLOv8/v11)** | Détection d'objets, segmentation, classification |
| **Visage câlin (transformateurs)** | Transformateurs de vision, SegFormer, DETR |
| **Segmenter n'importe quoi (SAM)** | Segmentation universelle d'images de Meta |
| **Albumentations** | Bibliothèque d'augmentation d'image rapide et flexible |
---

## Conseils pratiques
- **Commencez par l'apprentissage par transfert.** Dans presque tous les cas, la mise au point d'un modèle pré-entraîné est préférable à une formation à partir de zéro.
- **Normalisez vos entrées.** Faites correspondre la normalisation attendue par le modèle pré-entraîné (généralement ImageNet moyenne/std).
- **Utilisez des métriques appropriées.** Précision pour les ensembles de données équilibrés ; F1, mAP ou IoU pour les tâches de déséquilibre ou de détection.
- **Visualisez vos données.** Regardez des exemples d'images, vérifiez les distributions de classes, inspectez les prédictions du modèle.
- **Augmentez judicieusement.** N'appliquez que les transformations qui ont du sens pour votre domaine (ne retournez pas les images médicales verticalement).
- **Surveillez le surajustement.** Si la précision de l'entraînement est élevée mais que la validation est faible, augmentez l'augmentation ou ajoutez l'abandon.