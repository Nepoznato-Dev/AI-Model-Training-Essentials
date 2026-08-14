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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Fondamenti di visione artificiale
La visione artificiale offre alle macchine la capacità di interpretare e comprendere le informazioni visive provenienti dal mondo: immagini, video e dati 3D. È alla base di tutto, dal riconoscimento facciale sul telefono alle auto a guida autonoma, all'analisi delle immagini mediche e al controllo di qualità industriale. Questo file copre i concetti principali, le architetture e le tecniche.
---

## Come i computer vedono le immagini
### Pixel e canali
Un'immagine digitale è una griglia di pixel. Ogni pixel ha valori numerici che rappresentano l'intensità del colore.
| Tipo di immagine | Canali | Valori per Pixel | Esempio |
|-----------|----------|-----------|---------|
| **Scala di grigi** | 1| 0 (nero) a 255 (bianco) | Radiografie mediche |
| **RGB** | 3| Rosso, verde, blu (ciascuno 0–255) | Foto a colori standard |
| **RGBA** | 4| RGB + Alfa (trasparenza) | Immagini con sfondi trasparenti |
| **HSV** | 3| Tonalità, Saturazione, Valore | Segmentazione basata sul colore |
Un'immagine RGB 1920×1080 è un tensore di forma `(1080, 1920, 3)`: ovvero 6,2 milioni di pixel, ciascuno con 3 valori.
### Operazioni chiave
| Operazione | Descrizione |
|-----------|-------------|
| **Ridimensionamento** | Ridimensiona l'immagine alle dimensioni target (interpolazione bilineare, del vicino più vicino) |
| **Ritaglio** | Estrai una regione di interesse |
| **Normalizzazione** | Ridimensiona i valori dei pixel su [0,1] o [-1,1] per le reti neurali |
| **Aumento** | Espandi artificialmente i dati di addestramento (rotazione, capovolgimento, jitter colore, ritaglio) |
---

## Convoluzione: l'operazione principale
Una convoluzione fa scorrere un piccolo filtro (nucleo) sull'immagine, calcolando i prodotti scalari in ciascuna posizione. Questo è il modo in cui le CNN rilevano bordi, trame e motivi.
### Parametri di convoluzione
| Parametro | Effetto |
|-----------|--------|
| **Dimensione del kernel** | 3×3, 5×5, 7×7: i chicchi più grandi catturano modelli più grandi |
| **Passo** | Dimensione del passo; stride=2 dimezza le dimensioni dell'output |
| **Imbottitura** | Aggiungi zeri attorno al bordo per preservare le dimensioni spaziali |
| **Numero di filtri** | Ogni filtro apprende una caratteristica diversa (bordo, trama, modello di colore) |
### Cosa imparare dalle convoluzioni
| Profondità dello strato | Funzionalità rilevate |
|-------------|------------|
| **Primi strati** | Bordi, angoli, texture semplici |
| **Strati intermedi** | Forme, parti di oggetti (ruote, occhi, foglie) |
| **Strati profondi** | Concetti di alto livello (volti, automobili, animali) |
---

## Architetture della CNN
L'evoluzione delle architetture della CNN racconta la storia dei progressi del deep learning nella visione artificiale.
| Architettura | Anno | Innovazione chiave |
|-------------|------|---------------|
| **LeNet-5** | 1998 | Prima CNN pratica; riconoscimento delle cifre |
| **AlexNet** | 2012| La Deep CNN vince ImageNet; ReLU, abbandono, formazione GPU |
| **VGGNet** | 2014| Convoluzioni 3×3 impilate (più profonda = migliore) |
| **GoogLeNet (inizio)** | 2014| Moduli di inizio (dimensioni dei filtri paralleli); 22 strati |
| **ResNet** | 2015| Salta connessioni (apprendimento residuo); 152+ strati |
| **EfficientNet** | 2019 | Ridimensionamento composto (profondità + larghezza + risoluzione) |
| **ConvNeXt** | 2022 | ResNet modernizzato; competitivo con Transformers |
### Perché ResNet ha cambiato tutto
Prima di ResNet, l'addestramento di reti molto profonde era quasi impossibile a causa del problema del gradiente evanescente. ResNet ha introdotto le **salta connessioni** (chiamate anche connessioni residue): l'input di un livello viene aggiunto al suo output.
```
output = F(x) + x    # Skip connection
```

Questa semplice idea ha consentito di addestrare in modo efficace reti con oltre 152 livelli ed è ora standard praticamente in tutte le architetture profonde.
---

## Compiti fondamentali della visione
### Classificazione delle immagini
Assegna un'etichetta a un'intera immagine.
| Modello | Avvicinamento |
|-------|----------|
| CNN (ResNet, EfficientNet) | Approccio tradizionale; precisione eccellente |
| Trasformatori di visione (ViT) | Tratta l'immagine come una sequenza di patch; Encoder trasformatore |
| Trasferimento dell'apprendimento | Perfeziona un modello pre-addestrato sul tuo set di dati |
### Rilevamento oggetti
Trova e classifica più oggetti all'interno di un'immagine, con riquadri di delimitazione.
| Modello | Digitare | Velocità |
|-------|------|-------|
| **R-CNN** | Due fasi (proposta + classificazione) | Lento |
| **R-CNN veloce** | Migliorato a due stadi | Medio |
| **R-CNN più veloce** | Proposta Regione Rete + rilevatore | Medio |
| **YOLO** (v1–v10) | Monostadio; prevedere scatole + classi in un unico passaggio | Molto veloce |
| **DETR** | Basato su trasformatore; nessuna scatola di ancoraggio | Medio |
**YOLO** (You Only Look Once) è la soluzione ideale per il rilevamento in tempo reale. **R-CNN più veloce** è preferibile quando la precisione conta più della velocità.
### Segmentazione delle immagini
Classificare ogni pixel in un'immagine.
| Digitare | Descrizione | Caso d'uso |
|------|-------------|----------|
| **Segmentazione semantica** | Ogni pixel riceve un'etichetta di classe | Guida autonoma (stradale, automobilistica, pedonale) |
| **Segmentazione delle istanze** | Ogni pixel + ID istanza oggetto | Conteggio di oggetti, imaging medico |
| **Segmentazione panottica** | Semantica + istanza combinata | Comprensione completa della scena |
Modelli chiave: U-Net (imaging medico), Mask R-CNN (istanza), DeepLab (semantico), Segment Anything Model (SAM — segmentazione universale).
### Generazione di immagini
| Avvicinamento | Descrizione | Esempi |
|----------|-------------|----------|
| **GAN** | Formazione contraddittoria generatore vs discriminatore | StileGAN, CycleGAN |
| **VAE** | Imparare la distribuzione latente; campione da generare | Codificatori automatici variazionali |
| **Modelli di diffusione** | Denomina iterativamente il rumore casuale | Diffusione stabile, DALL-E, Midjourney |
I modelli di diffusione hanno ampiamente superato i GAN per la qualità della generazione delle immagini.
---

## Trasferire l'apprendimento per la visione
Addestrare una CNN da zero richiede enormi quantità di dati e di calcolo. Il trasferimento dell'apprendimento ti consente di iniziare con un modello già addestrato su milioni di immagini (ImageNet) e di perfezionarlo per la tua attività specifica.
### Passaggi
1. **Scegli un modello pre-addestrato** (ResNet50, EfficientNet-B0, ViT).
2. **Sostituisci il capo della classificazione** con il tuo (corrispondente al numero di classi).
3. **Blocca i primi livelli** (catturano caratteristiche generiche come i bordi).
4. **Perfeziona** il tuo set di dati con un basso tasso di apprendimento.
5. **Sblocca gradualmente** se hai bisogno di maggiore adattamento.
Questo approccio raggiunge abitualmente un'elevata precisione con un minimo di 1.000-10.000 immagini etichettate.
---

## Aumento dei dati
L'aumento espande artificialmente il set di dati di addestramento applicando trasformazioni.
| Aumento | Effetto | Quando usarlo |
|-------------|--------|-----|
| **Ritaglio casuale** | Ritaglia in una regione casuale | Quasi sempre |
| **Ribaltamento orizzontale** | Immagine speculare | Quando l'orientamento non conta |
| **Rotazione** | Ruota di un angolo casuale | Quando gli oggetti appaiono da qualsiasi angolazione |
| **Vibrazione del colore** | Regola in modo casuale luminosità, contrasto, saturazione | Quando l'illuminazione varia |
| **Cancellazione casuale** | Maschera regioni casuali | Migliora la robustezza |
| **Mixup/CutMix** | Unisci due immagini ed etichette | Regolarizzazione |
Librerie:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **OpenCV** | Operazioni CV classiche (filtraggio, rilevamento dei bordi, trasformazioni geometriche) |
| **visione della torcia** | Modelli di visione PyTorch, trasformazioni, set di dati |
| **tf.keras.applications** | Modelli pre-addestrati in TensorFlow/Keras |
| **Ultralitici (YOLOv8/v11)** | Rilevamento, segmentazione, classificazione degli oggetti |
| **Faccia che abbraccia (trasformatori)** | Trasformatori di visione, SegFormer, DETR |
| **Segmenta qualsiasi cosa (SAM)** | Segmentazione universale delle immagini da Meta |
| **Albumentazioni** | Libreria di potenziamento delle immagini veloce e flessibile |
---

## Consigli pratici
- **Inizia con l'apprendimento basato sul trasferimento.** La messa a punto di un modello preaddestrato è migliore della formazione da zero in quasi tutti i casi.
- **Normalizza i tuoi input.** Corrisponde alla normalizzazione prevista dal modello pre-addestrato (solitamente media/std ImageNet).
- **Utilizza metriche appropriate.** Precisione per set di dati bilanciati; F1, mAP o IoU per attività sbilanciate o di rilevamento.
- **Visualizza i tuoi dati.** Guarda immagini di esempio, controlla le distribuzioni delle classi, esamina le previsioni dei modelli.
- **Aumenta saggiamente.** Applica solo le trasformazioni che hanno senso per il tuo dominio (non capovolgere verticalmente le immagini mediche).
- **Monitora l'overfitting.** Se la precisione dell'addestramento è elevata ma la convalida è bassa, aumenta l'incremento o aggiungi l'abbandono.