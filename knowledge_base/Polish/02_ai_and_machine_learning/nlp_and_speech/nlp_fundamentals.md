<!--
---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
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
tags: [nlp, ai-and-machine-learning]
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
# Podstawy NLP
Przetwarzanie języka naturalnego (NLP) to dziedzina uczenia maszyn rozumienia, generowania i pracy z ludzkim językiem. Obsługuje wyszukiwarki, chatboty, systemy tłumaczeniowe, analizę nastrojów i duże modele językowe (LLM), które zmieniły sztuczną inteligencję od 2020 r. Ten plik opisuje ewolucję od technik klasycznych do nowoczesnych architektur opartych na transformatorach.
---

## Wstępne przetwarzanie tekstu
Surowy tekst jest niechlujny. Zanim model będzie mógł z niego skorzystać, należy go oczyścić i uporządkować.
| Krok | Co to robi | Przykład |
|------|------------|--------|
| **Tokenizacja** | Podziel tekst na tokeny (słowa, słowa podrzędne lub znaki) | „Kocham NLP” →`["I", "love", "NLP"]`|
| **Małe litery** | Zamień na małe litery | „Witam” → „Witam” |
| **Zatrzymaj usuwanie słów** | Usuń popularne słowa (the, is, at) | „kot usiadł” → „kot usiadł” |
| **Wyrastanie** | Posiekaj końcówki słów (surowe) | „bieganie” → „bieganie” |
| **Lematyzacja** | Zmniejsz do formy słownikowej (z uwzględnieniem kontekstu) | „lepiej” → „dobrze” |
| **Normalizacja** | Napraw kodowanie, usuń znaki specjalne, rozwiń skurcze | „nie” → „nie” |
Nowoczesne modele Transformerów często pomijają usuwanie słów kończących i rdzeniowanie — uczą się tych wzorców na podstawie danych.
---

## Reprezentacja tekstu
Maszyny potrzebują liczb, a nie słów. Sposób, w jaki reprezentujemy tekst jako wektory, ma fundamentalne znaczenie.
### Podejścia klasyczne
| Metoda | Opis | Ograniczenie |
|------------|------------|---------------|
| **Jedno-gorące kodowanie** | Każde słowo to unikalna pozycja w ogromnym wektorze | Rzadki; brak znaczenia semantycznego |
| **Worek słów (BoW)** | Policz częstotliwości słów; zignorować zamówienie | Całkowicie traci porządek słów |
| **TF-IDF** | Zważ słowa według częstotliwości w dokumencie × rzadkości w całym korpusie | Nadal ignoruje porządek i kontekst |
### Osadzanie słów
Osadzania mapują słowa na gęste wektory, w których podobne słowa znajdują się blisko siebie.
| Modelka | Kluczowa idea |
|-------|--------------|
| **Word2Vec** (2013) | Przewiduj słowo z kontekstu (CBOW) lub kontekst ze słowa (Skip-gram) |
| **Rękawica** (2014) | Globalne statystyki współwystępowania → wektory gęste |
| **FastText** (2016) | Word2Vec + informacja o podsłowie (lepiej radzi sobie z rzadkimi słowami) |
Słynny przykład:`king - man + woman ≈ queen`. Osadzania przechwytują relacje semantyczne.
**Ograniczenia**: klasyczne osadzania przypisują jeden wektor na słowo, więc nie radzą sobie z polisemią (słowa o wielu znaczeniach). „Bank” w „brzegu rzeki” i „koncie bankowym” otrzymuje ten sam wektor.
---

## Modele sekwencji
Przed Transformersami standardowym podejściem w NLP było sekwencyjne przetwarzanie tekstu.
| Architektura | Jak to działa | siła | słabość |
|------------|------------|----------|--------------|
| **NN** | Przetwarzaj żetony pojedynczo; utrzymuj stan ukryty | Obsługuje dane wejściowe o zmiennej długości | Znikające gradienty; nie można przechwycić długich zależności |
| **LSTM** | RNN z bramkami (zapomnij, wejście, wyjście) do kontroli przepływu informacji | Lepiej w zależnościach dalekiego zasięgu | Nadal sekwencyjnie; wolno trenować |
| **GRU** | Uproszczony LSTM (mniej bramek) | Szybszy niż LSTM; podobna wydajność | Te same podstawowe ograniczenia |
Modele te przetwarzają tekst od lewej do prawej, co oznacza, że ​​wolno je trenować (nie można ich wykonywać równolegle) i borykają się z zależnościami dalekiego zasięgu.
---

## Mechanizm uwagi
Uwaga pozwala modelowi spojrzeć jednocześnie na wszystkie pozycje w sekwencji i zdecydować, które z nich są najbardziej istotne dla bieżącej prognozy.
### Kluczowe spostrzeżenia
Zamiast kompresować całe zdanie w jeden ukryty stan (jak robią to RNN), uwaga oblicza sumę ważoną wszystkich ukrytych stanów, w których uczy się wag.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Składnik | Rola |
|----------|------|
| **Zapytanie (Q)** | Czego szukam? |
| **Klawisz (K)** | Co zawieram? |
| **Wartość (V)** | Jakie informacje podaję? |
| **√d_k** | Współczynnik skalowania zapobiegający powstawaniu produktów z dużymi punktami |
---

## Architektura transformatora
Transformer (Vaswani i in., 2017 — „Uwaga to wszystko, czego potrzebujesz”) całkowicie zastąpił nawroty uwagą. Jest to podstawa praktycznie całego współczesnego NLP.
### Architektura
| Składnik | Opis |
|---------------|------------|
| **Koder** | Czyta wprowadzony tekst; tworzy reprezentacje kontekstowe |
| **Dekoder** | Generuje tekst wyjściowy; obsługuje wyjście enkodera |
| **Samouwaga** | Każdy token odpowiada wszystkim innym tokenom w tej samej kolejności |
| **Uwaga wielogłowa** | Uruchom równolegle wiele głów uwagi; uchwycić różne relacje |
| **Kodowanie pozycyjne** | Wstrzyknij informacje o pozycji (ponieważ nie ma nawrotu) |
| **Sieć przekazująca** | Stosowane niezależnie dla każdej pozycji |
| **Normalizacja warstw** | Stabilizacja treningu |
| **Pozostałe połączenia** | Pomiń połączenia dla przepływu gradientowego |
### Tylko koder, tylko dekoder, koder-dekoder
| Wariant | Architektura | Najlepsze dla | Przykłady |
|--------|------------|----------|---------|
| **Tylko koder** | Rozumie tekst | Klasyfikacja, NER, analiza nastrojów | BERT, ROBERTA, DEBERTA |
| **Tylko dekoder** | Generuje tekst | Modele językowe, chatboty, generowanie kodu | GPT-3/4, LLaMA, Claude |
| **Koder-Dekoder** | Przekształca tekst | Tłumaczenie, streszczenie | T5, BART, mBART |
---

## Główne rodziny modelowe
### Rodzina BERT (tylko enkoder)
| Modelka | Kluczowa funkcja |
|-------|------------|
| **BERT** (2018) | Model języka zamaskowanego + przewidywanie następnego zdania |
| **RoBERTA** | Usunięto NSP; trenował dłużej z większą ilością danych |
| **ALBERT** | Udostępnianie parametrów; mniejsza powierzchnia |
| **DeBERTa** | Rozplątana uwaga; ulepszone NLU |
| **DestylBERT** | 40% mniejszy, 60% szybszy, zachowuje 97% wydajności BERT |
### Rodzina GPT (tylko dekoder)
| Modelka | Parametry | Notatki |
|-------|-----------|-------|
| **GPT-2** | 1,5B | Pokazane modele obsługujące tylko dekoder mogą generować spójny tekst |
| **GPT-3** | 175B | Nauka kilku strzałów; monitowany, a nie dostrajany |
| **GPT-3.5 / GPT-4** | Nieujawnione | Dostosowane do instrukcji + RLHF; konwersacyjny |
| **LLaMA** (Meta) | 7B–70B | Otwarta waga; zrodził ekosystem LLM typu open source |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Wydajne modele otwarte o dużej wydajności |
---

## Podstawowe zadania NLP
| Zadanie | Opis | Typowy model |
|------|------------|------------|
| **Klasyfikacja tekstu** | Przypisz etykietę do tekstu (spam/nie spam, pozytywny/negatywny) | BERT, dostrojone klasyfikatory |
| **Rozpoznawanie podmiotów nazwanych (NER)** | Identyfikuj osoby, organizacje, lokalizacje w tekście | BERT + warstwa CRF |
| **Analiza nastrojów** | Określ ton emocjonalny | Dostrojony BERT lub LLM z zerowym strzałem |
| **Tłumaczenie maszynowe** | Tłumacz między językami | T5, mBART, MarianMT |
| **Odpowiedź na pytanie** | Odpowiedz na pytania, biorąc pod uwagę kontekst | BERT (ekstrakcyjny), GPT (generatywny) |
| **Podsumowanie** | Skondensuj długi tekst | T5, BART, GPT |
| **Generowanie tekstu** | Stwórz spójny tekst | GPT-4, LLaMA, Claude |
---

## Dostrajanie a monitowanie
| Podejście | Jak to działa | Kiedy stosować |
|--------------|------------|------------|
| **Dostrajanie** | Zaktualizuj wagi modelu w danych specyficznych dla zadania | Oznaczyłeś dane; potrzebują maksymalnej wydajności |
| **Podpowiadanie** | Podaj instrukcje dotyczące modelu w języku naturalnym | Szybkie prototypowanie; ograniczone dane; korzystanie z LLM |
| **Kilka strzałów** | Dołącz przykłady do zachęty | Kiedy masz kilka przykładów, ale jest ich za mało, aby je dopracować |
| **LoRA / QLoRA** | Efektywne dostrajanie; zaktualizować małe macierze niskiego rzędu | Dostosuj duże modele z ograniczoną pamięcią GPU |
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **Transformatory z przytuloną twarzą** | Wstępnie wytrenowane modele, tokenizery, potoki dostrajania |
| **spaCy** | Potok NLP klasy produkcyjnej (tokenizacja, NER, POS, zależność) |
| **NLTK** | Edukacyjny; klasyczne algorytmy NLP |
| **Gensim** | Modelowanie tematów (LDA), osadzanie słów (Word2Vec, Doc2Vec) |
| **LangChain / Indeks Lamy** | Frameworki do tworzenia aplikacji opartych na LLM |
| **vLLM** | Obsługa LLM o wysokiej przepustowości |
| **Tokenizatory (HF)** | Szybka tokenizacja (BPE, WordPiece, SentencePiece) |
---

## Krajobraz LLM
Współczesny krajobraz NLP jest zdominowany przez modele wielkojęzykowe:
| Kategoria | Przykłady | Notatki |
|---------|---------|-------|
| **Zastrzeżone** | GPT-4, Claude, Bliźnięta | Najlepsza wydajność; Tylko dostęp do API |
| **Masa otwarta** | LLaMA 3, Mistral, Qwen | Dostępne ciężary; uruchamiaj lokalnie |
| **Open-source** | Pytia, OPT | W pełni otwarty (dane, wagi, kod) |
| **Multimodalny** | GPT-4V, Bliźnięta, LLaVA | Tekst procesowy + obrazy |
| **Specjalizacja w kodzie** | CodeLlama, StarCoder, DeepSeek Coder | Przeszkolony w zakresie kodu |
| **Mały / Wydajny** | Phi-3, Gemma, TinyLlama | Wysoka wydajność na małą skalę |
Pole porusza się szybko. To, co jest dziś najnowocześniejsze, może zostać zastąpione za kilka miesięcy. Podstawy – uwaga, tokenizacja, dostrojenie, ocena – pozostają niezmienne.