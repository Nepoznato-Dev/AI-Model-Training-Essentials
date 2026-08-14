---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoria informacji
Teoria informacji, założona przez Claude’a Shannona w 1948 roku, kwantyfikuje samą informację. Ile mówi Ci wiadomość? Jak bardzo możesz kompresować dane? Jak szybko możesz komunikować się za pomocą hałaśliwego kanału? Na te pytania znajdują się dokładne, matematyczne odpowiedzi. Poza komunikacją, teoria informacji stała się podstawą uczenia maszynowego — entropia krzyżowa jest domyślną funkcją straty w klasyfikacji, rozbieżność KL mierzy podobieństwo rozkładu, a wzajemne informacje napędzają wybór funkcji.
---

## Entropia
**Entropia** mierzy średnią niepewność lub „niespodziankę” zmiennej losowej.
### Entropia Shannona (dyskretna)
Dla dyskretnej zmiennej losowej X z funkcją masy prawdopodobieństwa p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Jednostki: **bity** (przy użyciu log₂) lub **nats** (przy użyciu ln).
| Dystrybucja | Entropia | Intuicja |
|------------|---------|----------|
| Moneta uczciwa (p = 0,5, 0,5) | 1 bit | Maksymalna niepewność wyniku binarnego |
| Moneta stronnicza (p = 0,9, 0,1) | 0,469 bitów | Mniej zaskakujące — głównie głowy |
| Deterministyczny (p = 1, 0) | 0 bitów | Żadnej niepewności |
| Sprawiedliwa kostka (6 stron) | 2,585 bitów | Więcej wyników = większa niepewność |
| Jednolite dla n wyników | log₂(n) bitów | Maksymalna entropia dla n wyników |
### Właściwości entropii
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Nienegatywność | H(X) ≥ 0 |
| Maksymalnie | H(X) ≤ log₂(\|X\|) z równością dla rozkładu równomiernego |
| Reguła łańcucha | H(X, Y) = H(X) + H(Y \| X) |
| Kondycjonowanie zmniejsza | H(X \| Y) ≤ H(X) |
| Wklęsłość | H jest wklęsłą funkcją rozkładu prawdopodobieństwa |
### Entropia różniczkowa (ciągła)
Dla ciągłej zmiennej losowej X o gęstości p(x):
h(X) = −∫ p(x) log p(x) dx
W przeciwieństwie do entropii dyskretnej, entropia różnicowa może być **ujemna**.
| Dystrybucja | Entropia różniczkowa |
|------------|--------------------------------------|
| Mundur na [a,b] | log(b - a) |
| Normalny N(μ, σ²) | (1/2) log(2πeσ²) |
| Wykładniczy(λ) | 1 − ln(λ) |
---

## Informacje wspólne, warunkowe i wzajemne
### Wspólna entropia
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Mierzy całkowitą niepewność pary (X, Y).
### Entropia warunkowa
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Mierzy pozostałą niepewność dotyczącą Y po obserwacji X.
### Wzajemne informacje
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Mierzy, ile wiedza X mówi ci o Y (i odwrotnie).
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Nienegatywność | I(X; Y) ≥ 0 |
| Symetria | I(X; Y) = I(Y; X) |
| Związek z entropią | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Związek ze stawem | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Niepodległość | I(X; Y) = 0 jeśli X i Y są niezależne |
| Informacje o sobie | I(X; X) = H(X) |
### Wizualizacja: diagram entropii
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## Rozbieżność KL
Dywergencja **Kullbacka-Leiblera (KL)** mierzy, jak bardzo różni się jeden rozkład od drugiego.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Nienegatywność | D_KL(P \|\| Q) ≥ 0 (nierówność Gibbsa) |
| Tożsamość | D_KL(P \|\| Q) = 0 jeśli P = Q |
| Asymetria | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) ogólnie |
| To nie jest metryka | Nie spełnia symetrii i nierówności trójkątów |
**Interpretacja:** D_KL(P || Q) to dodatkowa liczba bitów potrzebna do zakodowania danych z P przy użyciu kodu zoptymalizowanego pod kątem Q.
### Związek z innymi wielkościami
| Związek | Formuła |
|------------|------------|
| Entropia krzyżowa | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Wzajemne informacje | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| Warunkowe KL | D_KL(P(Y\|X) \|\| Q(Y\|X)) średnia dla X |
---

## Entropia krzyżowa
**Entropia krzyżowa** pomiędzy rozkładami P i Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropia krzyżowa jako funkcja straty
W klasyfikacji P jest rozkładem prawdziwym (etykieta zakodowana jednokrotnie), a Q jest rozkładem przewidywanym przez model.
**Binarna entropia krzyżowa (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Kategoryczna entropia krzyżowa:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Scenariusz | y (prawda) | ŷ (przewidywany) | Strata |
|---------|----------|--------------|------|
| Poprawny, pewny siebie | 1 | 0,95 | 0,051 |
| Poprawne, niepewne | 1 | 0,55 | 0,598 |
| Źle, pewnie | 1 | 0,05 | 2,996 |
| Źle, niepewne | 1 | 0,45 | 0,799 |
Minimalizowanie entropii krzyżowej jest równoznaczne z minimalizowaniem rozbieżności KL od prawdziwego rozkładu — dlatego działa tak dobrze jako funkcja straty.
---

## Pojemność kanału
### Model kanału komunikacyjnego
```
X → [Channel] → Y
```

- X: wejściowa zmienna losowa
- Y: wyjściowa zmienna losowa
- Kanał: zdefiniowany przez prawdopodobieństwa warunkowe p(y|x)
### Twierdzenie Shannona o kodowaniu kanałów z szumami
Dla kanału o przepustowości C, jeżeli prędkość transmisji R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, niezawodna komunikacja jest niemożliwa.
**Pojemność kanału:**
C = max_{p(x)} I(X; Y)
### Ważne przykłady kanałów
| Kanał | Opis | Pojemność |
|-------------|------------|---------|
| **Binarny symetryczny (BSC)** | Odwraca każdy bit z prawdopodobieństwem p | 1 − H(p) bity |
| **Usuwanie binarne (BEC)** | Kasuje każdy bit z prawdopodobieństwem ε | 1 − ε bity |
| **Gaussowski (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bity |
| **Bezszumowy plik binarny** | Doskonała transmisja | 1 bit |
---

## Kodowanie źródłowe i kompresja
### Twierdzenie o kodowaniu źródłowym
Średnia liczba bitów potrzebnych do zakodowania źródła jest ograniczona poniżej jego entropią:
L ≥ H(X)
Optymalny kod osiąga L ≈ H(X).
### Kodowanie Huffmana
Kod **bez prefiksu**, który przypisuje krótsze kody do bardziej prawdopodobnych symboli.
| Symbol | Prawdopodobieństwo | Kod Huffmana | Długość |
|------------|------------|------------|-------|
| | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Średnia długość: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bitów/symbol
Entropia: H = 1,75 bitów/symbol (optymalnie w tym przypadku!)
### Kompresja bezstratna vs. stratna
| Wpisz | Zasada | Przykłady | Limit |
|------|-----------|----------|-------|
| **Bezstratny** | Usuń nadmiarowość statystyczną | ZIP, PNG, FLAC | Współczynnik entropii H(X) |
| **Strata** | Usuń informacje nieistotne percepcyjnie | JPEG, MP3, H.264 | Funkcja zniekształcenia szybkości R(D) |
**Teoria zniekształceń szybkości:** W przypadku kompresji stratnej z maksymalnym zniekształceniem D, minimalna szybkość wynosi R(D) = min I(X; X̂) z zastrzeżeniem E[d(X, X̂)] ≤ D.
---

## Połączenia z innymi polami
### Teoria informacji i termodynamika
| Koncepcja | Teoria informacji | Termodynamika |
|--------|--------------------------------|----------------|
| Entropia | Entropia Shannona H(X) | Entropia Boltzmanna S = k_B ln W |
| Maksymalna entropia | Równomierny rozkład | Równowaga termiczna |
| Rozbieżność KL | Różnica w dystrybucji | Różnica energii swobodnej |
| Wzajemne informacje | Udostępnione informacje | Korelacje w układach fizycznych |
Formy matematyczne są identyczne — Shannon celowo zapożyczył termin „entropia” z mechaniki statystycznej.
### Teoria informacji i statystyka
| Koncepcja | Aplikacja |
|--------|------------|
| Maksymalne prawdopodobieństwo | Równoważne minimalizacji rozbieżności KL od rozkładu empirycznego do rozkładu modelowego |
| Informacje Fishera | Krzywizna rozbieżności KL; dolna granica wariancji estymatora (Craméra-Rao) |
| Minimalna długość opisu (MDL) | Wybór modelu poprzez minimalizację całkowitej długości kodowania |
| AIC/BIC | Przybliżone kryteria wyboru modelu oparte na KL |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja IT | Aplikacja ML |
|--------------|----------------|
| Strata między entropią | Domyślna utrata klasyfikacji (binarna i wieloklasowa) |
| Rozbieżność KL | Strata VAE (termin regulujący), dopasowanie dystrybucji, destylacja |
| Wzajemne informacje | Wybór cech (MIFS), uczenie się reprezentacji (InfoMax), rozplątanie |
| Entropia | Kryterium podziału drzewa decyzyjnego (zysk informacji), eksploracja w RL (maksymalna entropia RL) |
| Pojemność kanału | Złożoność komunikacji, zrozumienie granic uogólnień |
| Kodowanie źródłowe | Kompresja danych do przechowywania i transmisji, wydajne kodowanie |
| Maksymalna entropia | Klasyfikatory MaxEnt, selekcja wstępna w wnioskowaniu bayesowskim |
| Zniekształcenie szybkości | Zrozumienie kompromisów w kompresji stratnej, kwantyzacji w sieciach neuronowych |
| Informacje Fishera | Naturalne zejście gradientowe, zrozumienie wrażliwości parametrów |
| MDL / AIC / BIC | Wybór modelu, zapobiegający nadmiernemu dopasowaniu |
---

## Streszczenie
| Ilość | Formuła (dyskretna) | Znaczenie |
|---------|---------|--------|
| Entropia H(X) | −Σ p(x) log p(x) | Średnia niepewność |
| Wspólna entropia H(X,Y) | −Σ p(x,y) log p(x,y) | Całkowita niepewność pary |
| Entropia warunkowa H(Y\|X) | H(X,Y) − H(X) | Pozostała niepewność co do Y, biorąc pod uwagę X |
| Wzajemne informacje I(X;Y) | H(X) − H(X\|Y) | Informacje udostępniane pomiędzy X i Y |
| Rozbieżność KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | „Odległość” między rozkładami |
| Entropia krzyżowa H(P,Q) | −Σ P(x) log Q(x) | Koszt kodowania przy użyciu niewłaściwej dystrybucji |
| Pojemność kanału C | maks. I(X;Y) | Maksymalna niezawodna szybkość komunikacji |
Teoria informacji wyznacza podstawowe ograniczenia tego, czego można się nauczyć, skompresować i przekazać. Dla praktyków uczenia maszynowego wyjaśnia, dlaczego entropia krzyżowa działa jako funkcja straty, jak mierzyć jakość wyuczonych reprezentacji i jak myśleć o kompromisie między złożonością modelu a dopasowaniem danych. Spostrzeżenia Shannona z 1948 r. pozostają tak samo istotne dla współczesnej sztucznej inteligencji, jak i dla telekomunikacji.