---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
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
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Przetwarzanie sygnału
Przetwarzanie sygnałów to nauka zajmująca się analizowaniem, modyfikowaniem i syntezą sygnałów — reprezentacji wielkości fizycznych zmieniających się w czasie, przestrzeni lub częstotliwości. Dźwięk, obrazy, wideo, dane z czujników, fale mózgowe, ceny akcji – wszystko to są sygnały. Matematyczne narzędzia przetwarzania sygnałów (transformaty Fouriera, filtry, teoria próbkowania) są podstawą uczenia maszynowego, komunikacji, obrazowania medycznego i praktycznie każdej dziedziny zajmującej się danymi.
---

## Sygnały i systemy
### Klasyfikacja sygnału
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Czas ciągły** | Zdefiniowane dla wszystkich t ∈ ℝ | Napięcie audio, temperatura |
| **Czas dyskretny** | Zdefiniowane przy indeksach całkowitych n | Próbkowany dźwięk, wartości pikseli |
| **Analogowy** | Ciągły w czasie i amplitudzie | Rowek płyty winylowej |
| **Cyfrowy** | Dyskretna w czasie i skwantowana amplituda | Plik MP3, obraz JPEG |
| **Okresowe** | x(t + T) = x(t) dla wszystkich t | Fala sinusoidalna, fala prostokątna |
| **Aperiodyczne** | Brak powtarzającego się wzoru | Mowa, muzyka |
| **Deterministyczny** | Całkowicie przewidywalne | Sinusoida |
| **Stochastyczny** | Zawiera losowość | Hałas, ceny akcji |
### Właściwości systemu
| Nieruchomość | Definicja | Przykład |
|---------|-----------|---------|
| **Liniowy** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Filtr dolnoprzepustowy |
| **Niezmienny w czasie** | Przesunięcie na wejściu → to samo przesunięcie na wyjściu | Dowolny stały filtr |
| **Przyczynowy** | Wynik zależy tylko od obecnych i przeszłych danych wejściowych System czasu rzeczywistego |
| **Stabilny (BIBO)** | Ograniczone wejście → ograniczone wyjście | Dobrze zaprojektowany filtr |
| **Bez pamięci** | Wyjście zależy tylko od prądu wejściowego | Wzmacniacz |
---

## Transformata Fouriera
**Transformata Fouriera** rozkłada sygnał na częstotliwości składowe.
### Ciągła transformata Fouriera
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Odwrotność: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Pary z transformacją Fouriera
| Dziedzina czasu x(t) | Dziedzina częstotliwości X(f) |
|--------------------------------|----------------------|
| Impuls prostokątny | funkcja sinc |
| funkcja sinc | Impuls prostokątny |
| Gaussa e^{−at²} | Gaussa (√(π/a))e^{−π²f²/a} |
| Delta Diraca δ(t) | 1 (wszystkie częstotliwości) |
| Złożone wykładnicze e^{j2πf₀t} | δ(f – f₀) |
| Cosinus cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Właściwości klucza
| Nieruchomość | Domena czasu | Dziedzina częstotliwości |
|---------|------------|--------------------------------|
| Liniowość | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Przesunięcie czasu | x(t - t₀) | X(f)e^{−j2πft₀} |
| Przesunięcie częstotliwości | x(t)e^{j2πf₀t} | X(f - f₀) |
| Splot | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Mnożenie | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Różnicowanie | dx/dt | j2πf X(f) |
| Twierdzenie Parsevala | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Twierdzenie o splocie:** Splot w czasie = mnożenie częstotliwości. To najważniejsza właściwość — zamienia drogie operacje splotu w tanie mnożenia.
### Dyskretna transformata Fouriera (DFT)
Dla ciągu x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Nieruchomość | Wartość |
|---------|-------|
| Wejście | N próbek rzeczywistych lub złożonych |
| Wyjście | N złożone przedziały częstotliwości |
| Rozdzielczość częstotliwości | f_s/N (gdzie f_s to częstotliwość próbkowania) |
| Częstotliwość Nyquista | f_s/2 (maksymalna możliwa do przedstawienia częstotliwość) |
| Złożoność | O(N²) obliczenia bezpośrednie |
### Szybka transformata Fouriera (FFT)
**FFT** oblicza DFT w O(N log N) zamiast O(N²).
| N | Operacje O(N²) | O(N log N) Operacje | Przyspieszenie |
|---|----------------------|----------------------|--------|
| 1024 | 1 048 576 | 10240 | 102× |
| 1 048 576 | 1,1 × 10¹² | 20 971 520 | 52 428× |
FFT jest jednym z najważniejszych algorytmów, jakie kiedykolwiek wynaleziono. Umożliwia przetwarzanie dźwięku w czasie rzeczywistym, kompresję obrazu (JPEG), komunikację bezprzewodową (OFDM) i analizę widmową.
---

## Transformacja Laplace’a
**Transformata Laplace’a** rozszerza transformatę Fouriera w celu obsługi niestabilnych systemów i analizy stanów przejściowych.
F(s) = ∫₀^∞ f(t) e^{−st} dt, gdzie s = σ + jω
### Typowe transformaty Laplace’a
| f(t) | F(y) | Region konwergencji |
|------|------|----------------------|
| δ(t) (impuls) | 1 | Wszystko s |
| u(t) (krok) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(s) > 0 |
| sin(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Połączenie z transformacją Fouriera
Gdy σ = 0 (s = jω), transformata Laplace'a sprowadza się do transformaty Fouriera. Transformata Laplace'a zapewnia pełniejszy obraz, włączając informacje o wzroście/zaniku (σ).
---

## Transformacja Z
**Transformacja Z** jest dyskretnym odpowiednikiem transformaty Laplace’a.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Typowe transformacje Z
| x[n] | X(z) | ROC |
|------|------|---------|
| δ[n] | 1 | Wszystko z |
| u[n] (krok) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z-a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z-a)² | \|z\| > \|a\| |
| grzech(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Związek z innymi transformacjami
| Przekształć | Domena | Zmienna |
|----------|--------|---------|
| Fouriera | Częstotliwość ciągła | f lub ω |
| Laplace | Częstotliwość złożona | s = σ + jω |
| Transformacja Z | Częstotliwość zespolona (dyskretna) | z = e^{sT} |
Okrąg jednostkowy w płaszczyźnie z (|z| = 1) odpowiada transformacie Fouriera.
---

## Filtry
Filtry selektywnie przepuszczają lub blokują określone składowe częstotliwości.
### Typy filtrów
| Wpisz | Przepustki | Bloki | Aplikacja |
|------|------------|--------|------------|
| **Dolnoprzepustowy** | Niskie częstotliwości | Wysokie częstotliwości | Wygładzanie, antyaliasing |
| **Górnoprzepustowy** | Wysokie częstotliwości | Niskie częstotliwości | Wykrywanie krawędzi, usuwanie szumów |
| **Przepustka pasmowa** | Zakres częstotliwości | Poza zakresem | Wybór kanału (radio) |
| **Zatrzymanie taśmy (wycięcie)** | Wszystko oprócz zakresu | Konkretny zakres | Usuwanie przydźwięków linii energetycznej |
### Filtry FIR i IIR
| Nieruchomość | FIR (skończona odpowiedź impulsowa) | IIR (nieskończona odpowiedź impulsowa) |
|---------|------------------------------|--------------------------------|
| Odpowiedź impulsowa | Skończony czas trwania | Nieskończony czas trwania |
| Stabilność | Zawsze stabilny | Może być niestabilny |
| Faza | Może być dokładnie liniowy | Generalnie faza nieliniowa |
| Informacje zwrotne | Nie | Tak |
| Obliczenia | Potrzebnych więcej współczynników | Mniej współczynników dla tego samego roll-offu |
| Projekt | Okna, Parki-McClellan | Butterworth, Czebyszew, eliptyczny |
| Funkcja przenoszenia | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Specyfikacje projektu filtra
| Parametr | Opis |
|---------------|------------|
| **Pasmo przepustowe** | Zakres częstotliwości, który powinien przejść z minimalną stratą |
| **Zapora** | Zakres częstotliwości, który należy tłumić |
| **Częstotliwość odcięcia** | Granica między pasmem przepustowym a pasmem zaporowym |
| **falowanie** | Zmiana wzmocnienia pasma przepustowego (lub pasma zaporowego) |
| **Wycofanie** | Współczynnik tłumienia (dB na oktawę lub dekadę) |
| **Pasmo przejściowe** | Region pomiędzy pasmem przepustowym a pasmem zaporowym |
### Typowe projekty filtrów
| Projekt | Charakterystyka | Przypadek użycia |
|------------|----------------|--------------|
| **Butterworth** | Maksymalnie płaskie pasmo przenoszenia, umiarkowane opadanie | Cel ogólny |
| **Czebyszew Typ I** | Tętnienia w paśmie przepustowym, bardziej strome opadanie | Kiedy liczy się roll-off |
| **Czebyszew Typ II** | Tętnienie w paśmie zaporowym, pasmo płaskie | Kiedy liczy się płaskość pasma przenoszenia |
| **Eliptyczny (Cauer)** | Tętnienie w obu przypadkach, najbardziej strome zejście | Wymagane minimalne zamówienie |
| **Bessela** | Faza liniowa (maksymalnie płaskie opóźnienie grupowe) | Zachowując kształt fali |
---

## Teoria próbkowania
### Twierdzenie Nyquista-Shannona o próbkowaniu
Sygnał ciągły można doskonale odtworzyć z jego próbek, jeśli częstotliwość próbkowania przekracza dwukrotnie częstotliwość maksymalną:
f_s > 2f_max
| Termin | Definicja |
|------|------------|
| **Częstotliwość próbkowania** (f_s) | Liczba próbek na sekundę |
| **Stawka Nyquista** | 2f_max (minimalna częstotliwość próbkowania) |
| **Częstotliwość Nyquista** | f_s/2 (maksymalna możliwa do przedstawienia częstotliwość) |
| **Aliasing** | Wysokie częstotliwości udające niskie częstotliwości, gdy f_s < 2f_max |
### Typowe częstotliwości próbkowania
| Aplikacja | Oceń | Częstotliwość Nyquista |
|------------|------|----------------------|
| Przemówienie telefoniczne | 8 kHz | 4 kHz |
| Płyta audio | 44,1 kHz | 22,05 kHz |
| Profesjonalny dźwięk | 48 kHz | 24 kHz |
| Dźwięk w wysokiej rozdzielczości | 96 kHz | 48 kHz |
| Wideo (30 kl./s) | 30 Hz (chwilowy) | 15 Hz |
### Antyaliasing
Przed próbkowaniem **filtr antyaliasingowy** (dolnoprzepustowy) usuwa częstotliwości powyżej f_s/2, aby zapobiec aliasingowi.
---

## Okno
Analizując skończony segment sygnału, pośrednio mnożymy przez prostokątne okno, powodując wyciek widma. **Funkcje okna** zmniejszają ten wyciek.
### Wspólne okna
| Okno | Szerokość głównego płata | Poziom płata bocznego | Przypadek użycia |
|------------|----------------|-----------------|---------|
| Prostokątny | Najwęższy | −13 dB | Kiedy rozdzielczość ma największe znaczenie |
| Hanna | 2× prostokątny | −31 dB | Cel ogólny |
| Hamminga | 2× prostokątny | −41 dB | Zredukowany najbliższy płatek boczny |
| Blackmana | 3× prostokątny | −58 dB | Wysoki zakres dynamiki |
| Cesarz | Regulowany | Regulowane (przez β) | Kiedy kompromis można dostroić |
### Wyciek widmowy
Mnożenie sygnału przez okno powoduje splatanie jego widma z widmem okna. Szersze listki główne zmniejszają rozdzielczość częstotliwości; dolne listki boczne zmniejszają wycieki.
---

## Falki
**Fale** to małe, zlokalizowane funkcje falowe używane do analizy sygnału w wielu rozdzielczościach.
### Transformacja falkowa
W przeciwieństwie do transformaty Fouriera (która podaje globalną informację o częstotliwości), transformata falkowa zapewnia lokalizację **czas-częstotliwość**.
| Przekształć | Rozdzielczość czasu | Rozdzielczość częstotliwości |
|----------|----------------|---------------------------------|
| Fouriera | Brak (globalny) | Znakomity |
| Krótkoterminowy FT | Naprawiono (rozmiar okna) | Naprawiono |
| Falka | Zmienna (dobra przy wysokich częstotliwościach) | Zmienna (dobra przy niskich częstotliwościach) |
### Wspólne rodziny falek
| Rodzina | Właściwości | Aplikacja |
|--------|-----------|------------|
| **Haar** | Najprostszy, nieciągły | Wykrywanie krawędzi, szybka analiza |
| **Daubechies** (dbN) | Kompaktowe wsparcie, N momentów zanikających | Kompresja, odszumianie |
| **Symlety** | Prawie symetryczny Daubechies | Zmniejszone zniekształcenie fazowe |
| **Kofetki** | Zaprojektowany do warunków chwilowych | Przetwarzanie sygnału |
| **Morlet** | Sinusoida z okienkiem Gaussa | Analiza czasowo-częstotliwościowa |
| **Meksykański kapelusz** | Druga pochodna Gaussa | Wykrywanie funkcji |
### Zastosowania falek
| Aplikacja | Jak Wavelety pomagają |
|------------|----------------------|
| Kompresja obrazu (JPEG 2000) | Reprezentacja w wielu rozdzielczościach, lepsza niż DCT dla krawędzi |
| Odszumianie | Próg małych współczynników falkowych (sygnał ma duże współczynniki) |
| Wykrywanie funkcji | Detekcja krawędzi, detekcja stanów przejściowych w szeregach czasowych |
| Analiza EKG | Wykrywanie zespołów QRS, klasyfikacja arytmii |
| Analiza sejsmiczna | Identyfikacja warstw geologicznych, przetwarzanie sygnału trzęsienia ziemi |
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja przetwarzania sygnału | Aplikacja |
|-------------------------|------------|
| Transformata Fouriera | Cechy widmowe audio ML, analiza w dziedzinie częstotliwości szeregów czasowych |
| FFT | Szybki splot w CNN (splot widmowy), wydajna korelacja |
| Twierdzenie o splocie | Zrozumienie działania CNN (są to wyuczone filtry) |
| Filtry | Przetwarzanie wstępne (wygładzanie, odszumianie), ekstrakcja cech |
| Twierdzenie o próbkowaniu | Zrozumienie dyskretyzacji, wybór szybkości czujnika, unikanie aliasingu |
| Okienkowanie | STFT dla audio ML (spektrogramy), analiza czasowo-częstotliwościowa |
| Falki | Ekstrakcja cech dla szeregów czasowych, kompresja, odszumianie |
| Transformata Laplace'a/Z | Teoria sterowania w robotyce, zrozumienie stabilności systemów |
| Analiza widmowa | Analiza EEG/fMRI, monitorowanie drgań, konserwacja predykcyjna |
| stawka Nyquista | Wybór odpowiednich szybkości gromadzenia danych dla rurociągów ML |
---

## Streszczenie
| Narzędzie | Domena | Kluczowy wgląd |
|------|------------|------------|
| Transformata Fouriera | Czas → Częstotliwość | Sygnały są sumami sinusoid |
| Transformata Laplace'a | Czas → Częstotliwość złożona | Obsługuje stany nieustalone i stabilność |
| Transformacja Z | Czas dyskretny → Złożony | Analiza i projektowanie filtrów cyfrowych |
| FFT | Wydajne obliczenia DFT | O(N log N) zamiast O(N²) |
| Filtry | Wybór częstotliwości | Przekazuj to, czego potrzebujesz, blokuj to, czego nie |
| Twierdzenie o próbkowaniu | Ciągły ↔ dyskretny | Próbuj wystarczająco szybko, nic nie stracisz |
| Okienkowanie | Kompromis czasu i częstotliwości | Rozdzielczość wagi i wyciek |
| Falki | Analiza wielorozdzielcza | Lokalne zarówno pod względem czasu, jak i częstotliwości |
Przetwarzanie sygnałów zapewnia matematyczne podstawy zrozumienia, analizowania i manipulowania danymi. Każdy potok uczenia maszynowego, który współpracuje z szeregami czasowymi, dźwiękiem, obrazami lub danymi z czujników, domyślnie wykorzystuje koncepcje przetwarzania sygnałów. W szczególności transformata Fouriera jest prawdopodobnie najważniejszym narzędziem matematycznym po rachunku różniczkowym dla każdego badacza danych.