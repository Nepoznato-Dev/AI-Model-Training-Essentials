---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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

# Optymalizacja i wdrażanie modelu
Trenowanie dużego modelu sztucznej inteligencji robi wrażenie, ale większość prac inżynieryjnych zajmuje się jego efektywnym wdrażaniem. Model, który potrzebuje 10 sekund na reakcję lub wymaga ośmiu procesorów graficznych A100, jest bezużyteczny w większości rzeczywistych zastosowań. Optymalizacja modeli to sztuka i nauka polegająca na tworzeniu mniejszych, szybszych i tańszych modeli — bez poświęcania zbyt dużej jakości. Ten plik obejmuje kwantyzację, przycinanie, destylację i praktyczne narzędzia umożliwiające wprowadzenie modeli do produkcji.
---

## Dlaczego optymalizować?
| Obawa | Wpływ |
|--------|--------|
| **Opóźnienie** | Użytkownicy oczekują odpowiedzi w czasie krótszym niż 1 sekunda; każde dodatkowe 100 ms powoduje utratę zaangażowania |
| **Koszt** | Wnioskowanie z GPU jest kosztowne; model 70B kosztuje ~0,05-0,15 USD za 1 milion tokenów na sprzęcie w chmurze |
| **Pamięć** | Model 7B w FP32 potrzebuje 28 GB pamięci VRAM; większość konsumenckich procesorów graficznych ma 8-24 GB |
| **Energia** | Uruchamianie dużych modeli zużywa znaczną ilość energii elektrycznej; ma znaczenie dla urządzeń mobilnych i brzegowych |
| **Skala** | Obsługa milionów użytkowników wymaga modeli pasujących do dostępnego sprzętu |
---

## Kwantyzacja
Kwantyzacja zmniejsza precyzję wag modelu z 32-bitowego zmiennoprzecinkowego (FP32) do mniejszych formatów, takich jak INT8, INT4 lub nawet niższych.
### Precyzyjne formaty
| Formatuj | Bity na wagę | Pamięć dla modelu 7B | Jakość |
|------------|----------------|--------------------|--------|
| **FP32** | 32 | 28 GB | Linia bazowa (pełna precyzja) |
| **PR16 / BF16** | 16 | 14 GB | Prawie identyczny jak FP32 |
| **INT8** | 8 | 7 GB | Bardzo mała utrata jakości |
| **INT4** | 4 | 3,5 GB | Umiarkowana utrata jakości; nadal użyteczny |
| **INT3 / INT2** | 3-2 | 2,6-1,75 GB | Znacząca utrata jakości; etap badawczy |
### Metody kwantyzacji
| Metoda | Kiedy to się stanie | Jak to działa | Jakość |
|------------|----------------|-------------|--------|
| **Kwantyzacja potreningowa (PTQ)** | Po zakończeniu szkolenia | Skalibruj model na małym zbiorze danych; znajdź optymalne skale | Dobre dla INT8; ulega degradacji przy INT4 |
| **GPTQ** | Po treningu | Przyjazna dla GPU kwantyzacja INT4 z wykorzystaniem przybliżonych informacji drugiego rzędu | Dobra jakość w INT4 |
| **AWQ** (kwantyzacja masy uwzględniająca aktywację) | Po treningu | Chroń najważniejsze wagi w oparciu o wielkości aktywacji | Lepsze niż GPTQ na INT4 |
| **GGUF** (format lama.cpp) | Po treningu | Kwantyzacja przyjazna dla procesora; mieszana precyzja na warstwę | Zoptymalizowany pod kątem wnioskowania o procesorze |
| **Szkolenie w zakresie kwantyzacji (QAT)** | Podczas treningu | Symuluj kwantyzację podczas treningu, aby model nauczył się sobie radzić Najlepsza jakość; wymaga przekwalifikowania |
### Praktyczny wpływ
| Modelka | Rozmiar FP16 | INT4 Rozmiar | Przyspieszenie | Utrata jakości |
|-------|------|-----------|---------|-------------|
| **LLaMA 7B** | 14 GB | 3,5 GB | 2-4x | ~1-2% w benchmarkach |
| **LLaMA 70B** | 140 GB | 35 GB | 2-3x | ~2-3% w benchmarkach |
---

## Przycinanie
Przycinanie usuwa niepotrzebne obciążniki lub neurony z wyuczonego modelu.
| Wpisz | Opis | Zaleta | Wyzwanie |
|------|-------------|-----------|---------------|
| **Nieustrukturyzowany** | Usuń poszczególne wagi (ustaw na zero) | Najwyższe współczynniki kompresji | Wymaga rzadkiego wsparcia sprzętowego |
| **Strukturalne** | Usuń całe neurony, głowy uwagi lub warstwy | Bezpośrednio zmniejsza rozmiar modelu | Może stracić więcej jakości |
| **Na podstawie wielkości** | Usuń wagi z najmniejszymi wartościami bezwzględnymi | Prosty; działa dobrze | Może przegapić ważne małe ciężary |
| **Oparte na znaczeniu** | Usuń wagi na podstawie ich udziału w produkcji | Lepsze zachowanie jakości | Droższe w obliczeniach |
### Przycinanie rurociągu
| Krok | Opis |
|------|------------|
| 1. Pociąg | Normalnie trenuj pełny model |
| 2. Wynik | Oblicz wyniki ważności dla każdej wagi/neuronu |
| 3. Przycinaj | Usuń najmniej ważne elementy |
| 4. Dostosuj | Trenuj ponownie, aby odzyskać utraconą celność |
| 5. Powtórz | Iteracyjne przycinanie i dostrajanie w celu uzyskania wyższej kompresji |
---

## Destylacja wiedzy
Trenowanie małego modelu „ucznia” tak, aby naśladował duży model „nauczyciela”.
| Składnik | Rola |
|----------|------|
| **Nauczyciel** | Duży, wysokiej jakości model |
| **Student** | Mały model, który uczy się od nauczyciela |
| **Strata destylacyjna** | Uczeń próbuje dopasować rozkład wyników nauczyciela (miękkie etykiety) |
### Rodzaje destylacji
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Oparte na Logicie** | Uczeń dopasowuje prawdopodobieństwa wyjściowe nauczyciela | Oryginalna destylacja Hintona |
| **Oparte na funkcjach** | Uczeń dopasowuje pośrednie reprezentacje nauczyciela | FitNety |
| **Oparte na relacjach** | Student dopasowuje zależności pomiędzy próbkami | RKD (destylacja wiedzy relacyjnej) |
| **Bez danych** | Nie są potrzebne żadne oryginalne dane szkoleniowe; skorzystaj z pokolenia nauczycieli | DAFL, głęboka inwersja |
### Godne uwagi przykłady destylacji
| Nauczyciel | Studentka | Wynik |
|--------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (plotki) | Mniejszy model o jakości podobnej do GPT-4 |
| **BERT-duży** | DestylBERT | 40% mniejszy, 60% szybszy, 97% wydajności BERT |
| **LLaMA 70B** | LLaMA 7B (poprzez destylację) | Mały model typu open source zbliża się do jakości dużego modelu |
---

## Optymalizacje specyficzne dla LLM
### Optymalizacja pamięci podręcznej KV
Duże modele językowe buforują pary klucz-wartość z poprzednich tokenów, aby uniknąć ponownego obliczenia.
| Technika | Opis | Wpływ |
|----------|------------|-------|
| **Uwaga na wiele zapytań (MQA)** | Wszystkie głowy uwagi mają wspólną parę KV | Zmniejsza pamięć; niewielka utrata jakości |
| **Uwaga na zapytania grupowe (GQA)** | Grupy głów dzielą pary KV | Równowaga pomiędzy MQA a standardową uwagą |
| **Uwaga na przesuwane okno** | Zajmij się tylko ostatnimi żetonami W | Zmniejsza rozmiar pamięci podręcznej KV dla długich kontekstów |
### Dekodowanie spekulatywne
| Krok | Opis |
|------|------------|
| 1 | Mały model „szkicowy” szybko generuje K tokenów |
| 2 | Duży model weryfikuje wszystkie tokeny K w jednym przejściu do przodu |
| 3 | Zaakceptowane tokeny są zachowywane; odrzucone są regenerowane |
Wynik: 2-3-krotne przyspieszenie generacji bez utraty jakości (duży model zawsze ma ostatnie słowo).
### Błysk Uwaga
| Funkcja | Opis |
|--------|------------|
| **Problem** | Uwaga standardowa wymaga pamięci O(n²) dla macierzy uwagi |
| **Rozwiązanie** | Oblicz uwagę w blokach; nigdy nie materializuj pełnej matrycy w pamięci |
| **Wynik** | 2-4x szybciej; umożliwia znacznie dłuższe okna kontekstowe |
| **Warianty** | Flash Attention 2 (szybciej), FlashDecoding (zoptymalizowany pod kątem wnioskowania) |
---

## Struktury obsługi
| Ramy | Najlepsze dla | Kluczowa funkcja |
|----------|----------|------------|
| **vLLM** | Obsługa LLM | PagedUwaga; ciągłe dozowanie; wysoka przepustowość |
| **TensorRT-LLM** | Wnioskowanie dotyczące procesora graficznego NVIDIA | Maksymalna wydajność na sprzęcie NVIDIA |
| **llama.cpp** | Wnioskowanie o procesorze i konsumenckim GPU | Uruchamia skwantowane modele na laptopach i telefonach |
| **Ollama** | Działa model lokalny | Przyjazne dla użytkownika opakowanie wokół llama.cpp |
| **Serwer wnioskowania Triton** | Obsługa wielu platform | Obsługuje TensorFlow, PyTorch, ONNX, TensorRT |
| **Służenie Pochodni** | Obsługa modelu PyTorch | Natywna integracja z PyTorch |
| **Środowisko wykonawcze ONNX** | Wnioskowanie między platformami | Zoptymalizowane wykonanie na sprzęcie |
| **BentoML** | Wdrożenie produkcyjne | Niezależny od frameworka; zajmuje się pakowaniem i serwowaniem |
---

## Wzorce wdrażania
| Wzór | Opis | Kiedy stosować |
|--------|------------|------------|
| **Wdrożenie brzegowe** | Uruchamiaj modele na telefonach, urządzeniach IoT lub sprzęcie wbudowanym | Niskie opóźnienie; nieaktywny; prywatność |
| **API w chmurze** | Hostuj modele na procesorach graficznych w chmurze; obsługiwać przez API | Maksymalne obliczenia; płacić za użycie |
| **Hybryda** | Mały model na urządzeniu; duży model w chmurze | Najlepsze z obu światów |
| **Bezserwerowy** | Skaluj do zera; płacisz tylko wtedy, gdy jest używany | Sporadyczny ruch; wrażliwe na koszty |
| **Wnioskowanie zbiorcze** | Przetwarzaj dane zbiorczo według harmonogramu | Kiedy czas rzeczywisty nie jest potrzebny |
---

## Testowanie porównawcze
| Metryczne | Co to mierzy |
|------------|--------------------------------|
| **Tokeny na sekundę** | Przepustowość generacji (im wyższa tym lepsza) |
| **Czas do pierwszego tokena (TTFT)** | Opóźnienie przed pojawieniem się pierwszego tokena wyjściowego |
| **Opóźnienie na żądanie** | Całkowity czas od wejścia do całkowitego wyjścia |
| **Wykorzystanie pamięci** | VRAM lub RAM zużyte podczas wnioskowania |
| **Przepustowość** | Żądania obsługiwane na sekundę |
| **Koszt za 1 milion tokenów** | Dolarowy koszt przetworzenia 1 miliona tokenów |
---

## Praktyczne wskazówki
- **Zacznij od kwantyzacji.** Kwantyzacja INT4 (AWQ lub GPTQ) zapewnia najlepszy kompromis między jakością a rozmiarem. Większość modeli 7B działa wygodnie na jednym konsumenckim procesorze graficznym z interwałem INT4.
- **Użyj vLLM do obsługi LLM.** To najszybsza opcja typu open source do wysokoprzepustowego wnioskowania LLM.
- **Profil przed optymalizacją.** Zmierz, gdzie faktycznie spędzasz czas. Często wąskim gardłem jest przepustowość pamięci, a nie moc obliczeniowa.
- **Dopasuj model do zadania.** Model 7B jest odpowiedni do większości zadań. Nie używaj 70B, gdy wystarczy 7B.
- **Rozważ destylację.** Jeśli potrzebujesz małego, szybkiego modelu do produkcji, destyluj z większego modelu, zamiast trenować od zera.
- **Monitoruj w sposób ciągły.** Wydajność modelu może z czasem ulec pogorszeniu w miarę zmiany rozkładu danych. Śledź opóźnienia, przepustowość i wskaźniki jakości.
---

## Streszczenie
Optymalizacja modelu jest pomostem pomiędzy badaniami i produkcją. Kwantyzacja zmniejsza modele 4-8x przy minimalnej utracie jakości. Przycinanie usuwa ciężar własny. Destylacja przenosi wiedzę z dużych do małych modeli. Triki Flash Attention i KV-cache przyspieszają wnioskowanie. Łącznie te techniki zmieniają model wymagający centrum danych w taki, który działa na laptopie lub telefonie. Pole rozwija się szybko — to, co w zeszłym roku wymagało ośmiu procesorów A100, działa obecnie na konsumenckim procesorze graficznym.