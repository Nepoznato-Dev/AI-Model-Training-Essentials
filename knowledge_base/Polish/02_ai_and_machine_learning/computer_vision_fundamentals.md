---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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

# Podstawy widzenia komputerowego
Wizja komputerowa daje maszynom możliwość interpretowania i rozumienia informacji wizualnych ze świata — obrazów, wideo i danych 3D. Obsługuje wszystko, od rozpoznawania twarzy w telefonie po samochody autonomiczne, analizę obrazów medycznych i przemysłową kontrolę jakości. W tym pliku omówiono podstawowe koncepcje, architektury i techniki.
---

## Jak komputery widzą obrazy
### Piksele i kanały
Obraz cyfrowy to siatka pikseli. Każdy piksel ma wartości liczbowe reprezentujące intensywność koloru.
| Typ obrazu | Kanały | Wartości na piksel | Przykład |
|----------|------|----------------|---------|
| **Skala szarości** | 1 | 0 (czarny) do 255 (biały) | Medyczne zdjęcia rentgenowskie |
| **RGB** | 3 | Czerwony, Zielony, Niebieski (każde 0–255) | Standardowe zdjęcia kolorowe |
| **RGB** | 4 | RGB + Alpha (przezroczystość) | Obrazy z przezroczystym tłem |
| **HSV** | 3 | Barwa, nasycenie, wartość | Segmentacja oparta na kolorach |
Obraz RGB o rozdzielczości 1920 × 1080 to tensor kształtu`(1080, 1920, 3)`— czyli 6,2 miliona pikseli, każdy z 3 wartościami.
### Kluczowe operacje
| Operacja | Opis |
|---------------|------------|
| **Zmiana rozmiaru** | Skaluj obraz do wymiarów docelowych (interpolacja dwuliniowa, najbliższego sąsiada) |
| **Przycinanie** | Wyodrębnij interesujący Cię region |
| **Normalizacja** | Skaluj wartości pikseli do [0,1] lub [-1,1] dla sieci neuronowych |
| **Wzmocnienie** | Sztucznie rozszerzaj dane szkoleniowe (obrót, odwracanie, drgania kolorów, kadrowanie) |
---

## Splot: podstawowa operacja
Splot przesuwa mały filtr (jądro) po obrazie, obliczając iloczyn skalarny w każdej pozycji. W ten sposób CNN wykrywają krawędzie, tekstury i wzory.
### Parametry splotu
| Parametr | Efekt |
|----------|--------|
| **Rozmiar jądra** | 3×3, 5×5, 7×7 — większe jądra rejestrują większe wzory |
| **Krok** | Rozmiar kroku; krok = 2 zmniejsza o połowę wymiary wyjściowe |
| **Wypełnienie** | Dodaj zera wokół granicy, aby zachować wymiary przestrzenne |
| **Liczba filtrów** | Każdy filtr uczy się innej cechy (krawędź, tekstura, wzór koloru) |
### Czego uczą się zwoje
| Głębokość warstwy | Wykryte funkcje |
|------------|----------------------|
| **Wczesne warstwy** | Krawędzie, narożniki, proste tekstury |
| **Warstwy środkowe** | Kształty, części obiektów (koła, oczy, liście) |
| **Głębokie warstwy** | Koncepcje wysokiego poziomu (twarze, samochody, zwierzęta) |
---

## Architektury CNN
Ewolucja architektur CNN opowiada historię postępu głębokiego uczenia się w dziedzinie wizji komputerowej.
| Architektura | Rok | Kluczowa innowacja |
|------------|------|--------------|
| **LeNet-5** | 1998 | Pierwsza praktyczna CNN; rozpoznawanie cyfr |
| **AlexNet** | 2012 | Deep CNN wygrywa ImageNet; ReLU, porzucenie, szkolenie GPU |
| **VGGNet** | 2014 | Skumulowane zwoje 3×3 (głębiej = lepiej) |
| **GoogLeNet (początek)** | 2014 | Moduły początkowe (równoległe rozmiary filtrów); 22 warstwy |
| **ResNet** | 2015 | Pomiń połączenia (uczenie się resztek); Ponad 152 warstwy |
| **EfficientNet** | 2019 | Skalowanie złożone (głębokość + szerokość + rozdzielczość) |
| **ConvNeXt** | 2022 | Zmodernizowany ResNet; konkurencyjny z Transformersami |
### Dlaczego ResNet wszystko zmienił
Przed ResNet uczenie bardzo głębokich sieci było prawie niemożliwe ze względu na problem zanikającego gradientu. ResNet wprowadził **pomiń połączenia** (zwane także połączeniami resztkowymi): dane wejściowe warstwy są dodawane do jej danych wyjściowych.
```
output = F(x) + x    # Skip connection
```

Ten prosty pomysł umożliwił skuteczne szkolenie sieci składających się z ponad 152 warstw i jest obecnie standardem w praktycznie wszystkich głębokich architekturach.
---

## Podstawowe zadania związane z wizją
### Klasyfikacja obrazów
Przypisz etykietę do całego obrazu.
| Modelka | Podejście |
|-------|--------------|
| CNN (ResNet, EfficientNet) | Tradycyjne podejście; doskonała dokładność |
| Transformatory wizyjne (ViT) | Traktuj obraz jako sekwencję łat; Enkoder transformatorowy |
| Przenieś naukę | Dostosuj wstępnie wytrenowany model w zestawie danych |
### Wykrywanie obiektów
Znajdź i klasyfikuj wiele obiektów na obrazie za pomocą obwiedni.
| Modelka | Wpisz | Prędkość |
|-------|------|-------|
| **R-CNN** | Dwuetapowy (propozycja + klasyfikacja) | Powolny |
| **Szybki R-CNN** | Ulepszony dwustopniowy | Średni |
| **Szybszy R-CNN** | Region Propozycja Sieć + detektor | Średni |
| **YOLO** (v1–v10) | Jednostopniowy; przewidywanie pudełek + klas w jednym przebiegu | Bardzo szybko |
| **DETR** | Oparte na transformatorze; brak skrzynek kotwicznych | Średni |
**YOLO** (You Only Look Once) to metoda wykrywania w czasie rzeczywistym. **Szybszy R-CNN** jest preferowany, gdy dokładność jest ważniejsza niż szybkość.
### Segmentacja obrazu
Klasyfikuj każdy piksel obrazu.
| Wpisz | Opis | Przypadek użycia |
|------|------------|--------------|
| **Segmentacja semantyczna** | Każdy piksel otrzymuje etykietę klasy | Jazda autonomiczna (droga, samochód, pieszy) |
| **Segmentacja instancji** | Każdy piksel + identyfikator instancji obiektu | Liczenie obiektów, obrazowanie medyczne |
| **Segmentacja panoptyczna** | Semantyka + instancja w połączeniu | Kompleksowe zrozumienie sceny |
Kluczowe modele: U-Net (obrazowanie medyczne), Mask R-CNN (instancja), DeepLab (semantyczny), Segment Everything Model (SAM – segmentacja uniwersalna).
### Generowanie obrazu
| Podejście | Opis | Przykłady |
|---------|------------|---------|
| **GAN** | Trening kontradyktoryjny generatora i dyskryminatora | StylGAN, CycleGAN |
| **VAE** | Dowiedz się o ukrytej dystrybucji; próbka do wygenerowania | Autoenkodery wariacyjne |
| **Modele dyfuzji** | Iteracyjnie odszumiaj losowy szum | Stabilna dyfuzja, DALL-E, Midjourney |
Modele dyfuzyjne w dużej mierze przewyższają GAN pod względem jakości generowania obrazu.
---

## Przenieś naukę na rzecz wizji
Szkolenie CNN od podstaw wymaga ogromnych ilości danych i obliczeń. Uczenie się transferu pozwala rozpocząć od modelu już przeszkolonego na milionach obrazów (ImageNet) i dostosować go do konkretnego zadania.
### Kroki
1. **Wybierz wstępnie wytrenowany model** (ResNet50, EfficientNet-B0, ViT).
2. **Wymień głowicę klasyfikacyjną** na własną (odpowiadającą liczbie zajęć).
3. **Zamroź wczesne warstwy** (przechwytują ogólne cechy, takie jak krawędzie).
4. **Dopracuj** swój zbiór danych przy niskim tempie uczenia się.
5. **Odmrażaj stopniowo**, jeśli potrzebujesz większej adaptacji.
Podejście to rutynowo zapewnia wysoką dokładność przy zaledwie 1 000–10 000 oznaczonych obrazów.
---

## Rozszerzanie danych
Augmentacja sztucznie rozszerza zbiór danych szkoleniowych poprzez zastosowanie transformacji.
| Zwiększenie | Efekt | Kiedy stosować |
|------------|------------|------------|
| **Losowe przycięcie** | Przytnij do losowego regionu | Prawie zawsze |
| **Odwrócenie poziome** | Odbicie lustrzane | Kiedy orientacja nie ma znaczenia |
| **Obrót** | Obróć o losowy kąt | Gdy obiekty pojawiają się pod dowolnym kątem |
| **Drganie kolorów** | Losowo dostosuj jasność, kontrast, nasycenie | Kiedy oświetlenie się zmienia |
| **Losowe usuwanie** | Maskuj losowe regiony | Poprawia wytrzymałość |
| **Miksowanie / Miksowanie** | Połącz dwa obrazy i etykiety | Regularyzacja |
Biblioteki:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **OpenCV** | Klasyczne operacje CV (filtrowanie, wykrywanie krawędzi, transformacje geometryczne) |
| **wizja pochodni** | Modele wizyjne PyTorch, transformacje, zbiory danych |
| **tf.keras.aplikacje** | Wstępnie wyszkolone modele w TensorFlow/Keras |
| **Ultralytics (YOLOv8/v11)** | Detekcja obiektów, segmentacja, klasyfikacja |
| **Przytulona twarz (transformatory)** | Transformatory wizyjne, SegFormer, DETR |
| **Segmentuj wszystko (SAM)** | Uniwersalna segmentacja obrazu od Meta |
| **Albumentacje** | Szybka, elastyczna biblioteka powiększania obrazu |
---

## Praktyczne wskazówki
- **Zacznij od nauki transferowej.** Dopracowanie wstępnie wytrenowanego modelu w prawie każdym przypadku przewyższa szkolenie od zera.
- **Normalizuj swoje dane wejściowe.** Dopasuj normalizację, jakiej oczekuje wstępnie wytrenowany model (zwykle średnia/std ImageNet).
- **Użyj odpowiednich wskaźników.** Dokładność dla zrównoważonych zbiorów danych; F1, mAP lub IoU w przypadku zadań niezrównoważonych lub wykrywania.
- **Wizualizacja danych.** Obejrzyj przykładowe obrazy, sprawdź rozkład klas, sprawdź przewidywania modelu.
- **Rozwijaj mądrze.** Stosuj tylko przekształcenia, które mają sens dla Twojej domeny (nie odwracaj obrazów medycznych w pionie).
- **Monitoruj nadmierne dopasowanie.** Jeśli dokładność uczenia jest wysoka, ale walidacja jest niska, zwiększ zwiększanie lub dodaj przerwanie.