---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
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
tags: [speech, audio, processing, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Przetwarzanie mowy i dźwięku
Przetwarzanie mowy i dźwięku obejmuje technologie, które pozwalają maszynom słyszeć, rozumieć, generować i manipulować dźwiękiem. Obejmuje to rozpoznawanie mowy (przekształcanie wypowiadanych słów w tekst), syntezę mowy (przekształcanie tekstu w wypowiadane słowa), identyfikację mówiącego, generowanie muzyki i rozumienie dźwięków otoczenia. Dziedzina ta uległa przemianie dzięki głębokiemu uczeniu się — nowoczesne systemy zbliżają się do dokładności rozpoznawania mowy na poziomie człowieka i wytwarzają niesamowicie naturalne, syntetyczne głosy.
---

## Podstawy dźwięku cyfrowego
Dźwięk to fala ciśnienia. Aby przetworzyć go cyfrowo, próbkujemy falę w regularnych odstępach czasu.
| Koncepcja | Opis | Typowa wartość |
|--------|-------------|-------------|
| **Częstotliwość próbkowania** | Ile razy na sekundę mierzony jest dźwięk | 8 kHz (telefon), 16 kHz (mowa), 44,1 kHz (CD), 48 kHz (profesjonalne) |
| **Głębia bitowa** | Precyzja każdej próbki | 16-bitowy (CD), 24-bitowy (profesjonalny), 32-bitowy float (przetwarzanie) |
| **Kanały** | Mono (1), stereo (2), surround (5.1, 7.1) | Stereo do muzyki; mono dla mowy |
| **Czas trwania** | Długość dźwięku | Różnie |
1-minutowe nagranie monofoniczne przy 16 kHz, 16 bitów = 1,92 MB. 3-minutowy utwór stereo przy 44,1 kHz, 16 bitów = 30,3 MB.
---

## Ekstrakcja funkcji audio
Surowe przebiegi audio są trudne do bezpośredniej pracy z modelami. Wyodrębniamy cechy, które oddają ważne cechy dźwięku.
| Funkcja | Co przechwytuje | Przypadek użycia |
|--------|--------------------------------|---------|
| **Spektrogram Mel** | Zawartość częstotliwości w czasie, odwzorowana na percepcję ludzkiego słuchu | Rozpoznawanie mowy, klasyfikacja muzyki |
| **MFCC** (współczynniki cepstralne częstotliwości Mel) | Kompaktowa reprezentacja obwiedni widmowej | Tradycyjne rozpoznawanie mowy |
| **Chromagram** | Rozkład klas wysokości dźwięków (które nuty są odtwarzane) | Analiza muzyki, wykrywanie akordów |
| **Współczynnik przejścia przez zero** | Jak często sygnał przekracza zero | Wykrywanie dźwięczne i bezdźwięczne |
| **Energia RMS** | Głośność sygnału w czasie | Wykrywanie aktywności głosowej |
| **Skok (F0)** | Częstotliwość podstawowa | Identyfikacja mówcy, transkrypcja muzyki |
### Spektrogram Mela
Najpopularniejsza reprezentacja dźwięku w przypadku głębokiego uczenia się. Konwertuje dźwięk do formatu podobnego do obrazu 2D:
| Oś | Reprezentuje |
|------|-----------|
| **Oś X** | Czas |
| **Oś Y** | Częstotliwość (w skali Mel — w odstępach percepcyjnych) |
| **Kolor/intensywność** | Energia o tej częstotliwości i czasie |
Skala Mel jest zbliżona do ludzkiego słuchu: lepiej rozróżniamy niskie częstotliwości niż wysokie.
---

## Automatyczne rozpoznawanie mowy (ASR)
ASR konwertuje język mówiony na tekst. To jedno z najważniejszych komercyjnie zastosowań audio AI.
### Ewolucja ASR
| epoka | Podejście | Ograniczenie |
|---------|----------|------------|
| **Sprzed 2010 r.** | Ukryte modele Markowa + modele mieszaniny Gaussa | Wymagana rozległa inżynieria ręczna; biedny w hałaśliwych warunkach |
| **2010-2015** | Hybryda DNN-HMM | Sieci neuronowe zastąpiły GMM; znacząca poprawa |
| **2015-2020** | Modele typu end-to-end (Deep Speech, LAS) | Pojedyncza sieć neuronowa od dźwięku do tekstu |
| **2020+** | Transformatorowy (Whisper, Conformer) | Najnowocześniejsza dokładność; wielojęzyczny; solidny |
### Kluczowe modele ASR
| Modelka | Architektura | Dane szkoleniowe | Godna uwagi funkcja |
|-------|------------|--------------|----------------|
| **Szept** (OpenAI) | Enkoder-dekoder Transformator | 680 000 godzin, 99 języków | Wielojęzyczny; odporny na akcenty i hałas; open source |
| **Konformer** | Splot + samouważność | Różne | Łączy funkcje lokalne (konwencja) i globalne (uwaga) |
| **wav2vec 2.0** | Transformator samonadzorowany | Mowa bez etykiety | Uczy się na podstawie surowego dźwięku bez transkrypcji |
| **USM** (Google) | Uniwersalny model mowy | 2 miliony godzin, ponad 300 języków | Większość języków objętych |
| **MMS** (Meta) | Masowo wielojęzyczna mowa | Ponad 1400 języków | Rozszerza zasięg na języki o niskich zasobach |
### Metryki ASR
| Metryczne | Opis |
|------------|------------|
| **WER** (wskaźnik błędów w słowach) | Procent słów przepisanych niepoprawnie. Niżej jest lepiej. Wydajność człowieka w przypadku czystego języka angielskiego wynosi ~4-5%. |
| **CER** (stopień błędu znaku) | To samo co WER, ale na poziomie postaci. Używane w przypadku języków bez granic słów (chiński, japoński). |
### Typowe wyzwania ASR
| Wyzwanie | Opis |
|---------------|------------|
| **Akcenty i dialekty** | Wydajność znacznie spada w przypadku niestandardowych akcentów |
| **Szum w tle** | Muzyka, ruch uliczny i inne głośniki pogarszają dokładność |
| **Przełączanie kodu** | Głośniki przełączają się między językami w połowie zdania |
| **Homofony** | „Tam” vs „ich” vs „oni” — wymaga kontekstu |
| **Interpunkcja i formatowanie** | Dane wyjściowe ASR są zazwyczaj niepunktowane; wymaga przetwarzania |
| **Języki o niskich zasobach** | Większość modeli słabo radzi sobie z językami z niewielką ilością danych szkoleniowych
---

## Zamiana tekstu na mowę (TTS)
TTS konwertuje tekst pisany na dźwięk mówiony. Nowoczesne systemy wytwarzają mowę, która często jest nie do odróżnienia od nagrań ludzkich.
### Ewolucja TTS
| epoka | Podejście | Jakość |
|---------|----------|--------|
| **Sprzed 2010 r.** | Konkatenatywny (łączenie nagranych fragmentów) | Robotyczny; ograniczona ekspresja |
| **2010-2017** | Statystyczne parametryczne (HMM, wczesne neuronowe) | Lepsze, ale nadal rozpoznawalne jako syntetyczne |
| **2017-2020** | Neuronowe (Tacotron, WaveNet) | Jakość niemal ludzka; wyrazisty |
| **2020+** | Kodek neuronowy (VALL-E, Bark) | Klonowanie głosu; kilka strzałów; wysoce naturalny |
### Kluczowe modele TTS
| Modelka | Architektura | Godna uwagi funkcja |
|-------|------------|--------------------------------|
| **WaveNet** (DeepMind) | Autoregresyjny model generatywny | Pierwszy prawdziwie naturalnie brzmiący TTS |
| **Tacotron 2** (Google) | Seq2seq + wokoder | Kompleksowo; wysoka jakość |
| **WITY** | Wnioskowanie wariacyjne + trening kontradyktoryjny | Szybko; dobra jakość; powszechnie stosowane |
| **VALL-E** (Microsoft) | Model języka kodeka neuronowego | Klonowanie głosu z 3-sekundowej próbki |
| **Kora** (Suno) | Oparte na transformatorze | Wielojęzyczny; dźwięki inne niż mowa (śmiech, muzyka) |
| **JedenaścieLab** | Komercyjne | Wiodące w branży klonowanie głosu |
| **CzatTTS** | Otwarte oprogramowanie | Zoptymalizowany pod kątem mowy konwersacyjnej |
| **Mowa Ryby** | Otwarte oprogramowanie | Szybko; wielojęzyczny |
### Klonowanie głosu
Klonowanie głosu tworzy syntetyczny głos, który brzmi jak konkretna osoba na podstawie krótkiej próbki audio.
| Metoda | Potrzebne dane | Jakość |
|------------|------------|--------|
| **Dostrajanie** | 10-60 minut wystąpienia | Wysoka jakość; specyficzne dla głośnika |
| **Kilka strzałów** | 3-30 sekund mowy | Dobra jakość; szybka konfiguracja |
| **Zerowy strzał** | Brak danych głośnika docelowego | Używa dźwięku referencyjnego w czasie wnioskowania |
**Zagadnienia etyczne**: klonowanie głosu może być wykorzystywane do podszywania się pod inne osoby, oszustw i deepfake’ów. Większość dostawców komercyjnych wymaga zgody głosowej.
---

## Rozpoznawanie mówcy
| Zadanie | Opis | Aplikacja |
|------|------------|------------|
| **Weryfikacja prelegenta** | „Czy to osoba, za którą się podaje?” | Bankowość telefoniczna, odblokowanie urządzenia |
| **Identyfikacja mówcy** | "Z kim mam przyjemność?" | Transkrypcja spotkań, kryminalistyka |
| **Daryzacja mówcy** | – Kto kiedy mówił? (w trybie dźwięku wielogłośnikowego) | Podsumowania spotkań, generowanie napisów |
| Modelka | Podejście |
|-------|--------------|
| **ECAPA-TDNN** | Oparte na osadzaniu; najnowocześniejszy do weryfikacji |
| **wektor d** | Proste osadzanie głośników od DNN |
| **wektor x** | Ulepszone osadzanie głośników; powszechnie stosowane |
---

## Wyszukiwanie informacji muzycznych
| Zadanie | Opis | Narzędzia/Modele |
|------|------------|------------|
| **Transkrypcja muzyki** | Konwertuj dźwięk na nuty / MIDI | Spotify Basic Pitch, Spleeter |
| **Separacja źródła** | Izoluj poszczególne instrumenty lub wokale | Demucs, Spleeter, Separacja źródeł muzyki |
| **Klasyfikacja gatunku** | Kategoryzuj muzykę według gatunku | CNN na spektrogramach |
| **Śledzenie rytmu** | Wykryj pozycje tempa i rytmu | Librosa, Madmam |
| **Rozpoznawanie akordów** | Rozpoznaj akordy w muzyce | Modele Chord-CNN, CRF |
| **Pokolenie muzyki** | Twórz nową muzykę | MusicGen, MuseNet, AIVA |
---

## Wykrywanie dźwięku otoczenia
| Zadanie | Opis | Aplikacja |
|------|------------|------------|
| **Wykrywanie zdarzeń dźwiękowych** | Identyfikuj dźwięki w środowisku | Inteligentny dom (tłuczenie szkła, płacz dziecka) |
| **Klasyfikacja scen akustycznych** | Klasyfikuj środowisko (biuro, park, ruch uliczny) | Urządzenia kontekstowe |
| **Wykrywanie anomalii** | Wykryj niezwykłe dźwięki | Monitoring przemysłowy (maszynaæ·…éšœ) |
| Zbiór danych | Brzmi | Rozmiar |
|--------|-------|------|
| **Zestaw audio** | 632 klas dźwiękowych | Ponad 2 miliony klipów na YouTube |
| **ESC-50** | 50 klas ochrony środowiska | 2000 klipów |
| **UrbanSound8K** | Miejskie dźwięki | 8732 klipów |
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **Librosa** | Biblioteka Pythona do analizy dźwięku (funkcje, efekty, wizualizacja) |
| **Pydub** | Prosta manipulacja dźwiękiem (wycinanie, łączenie, eksport) |
| **FFmpeg** | Przetwarzanie audio/wideo z wiersza poleceń (szwajcarski scyzoryk) |
| **Torchaudio** | Przetwarzanie dźwięku PyTorch (transformacje, zbiory danych, modele) |
| **Przytulona twarz (transformatory)** | Wstępnie przeszkolone modele ASR i TTS |
| **Szept (OpenAI)** | Rozpoznawanie mowy (open source) |
| **Coqui TTS** | Zestaw narzędzi TTS typu open source |
| **Demuks** | Separacja źródła muzyki |
| **Mózg Mowy** | Kompleksowy zestaw narzędzi do rozpoznawania mowy (ASR, TTS, rozpoznawanie mówcy) |
---

## Praktyczne wskazówki
- **Zawsze słuchaj swoich danych.** Przed rozpoczęciem treningu posłuchaj przykładowego dźwięku. Zwróć uwagę na częstotliwość próbkowania, poziom szumu i charakterystykę głośnika.
- **Dopasuj częstotliwości próbkowania.** Szept oczekuje 16 kHz. Jeśli dźwięk ma częstotliwość 44,1 kHz, spróbuj go ponownie — pamiętaj jednak, że próbkowanie w dół powoduje utratę informacji.
- **Zwiększ dane audio.** Dodaj szum tła, zmieniaj prędkość i wysokość dźwięku, symuluj różne mikrofony. To znacznie poprawia wytrzymałość.
- **Użyj wstępnie wytrenowanych modeli.** Whisper dla ASR i VITS/Bark dla TTS to doskonałe punkty wyjścia. Dopracowanie jest prawie zawsze lepsze niż szkolenie od zera.
- **Obsługa wyciszenia.** Wykrywanie aktywności głosowej (VAD) usuwa ciszę przed przetworzeniem, oszczędzając obliczenia i poprawiając dokładność. Popularnymi opcjami są Silero VAD i WebRTC VAD.
- **Normalizuj głośność.** Różne nagrania mają bardzo różne poziomy głośności. Normalizuj do spójnego poziomu przed przetwarzaniem.
---

## Streszczenie
Przetwarzanie mowy i dźwięku zostało zrewolucjonizowane dzięki głębokiemu uczeniu się. Nowoczesne systemy ASR, takie jak Whisper, zapewniają dokładność na poziomie ludzkim w dziesiątkach języków. Systemy TTS wytwarzają mowę, która jest coraz bardziej nie do odróżnienia od nagrań ludzkich. Klonowanie głosu działa już od kilku sekund dźwięku. Tworzenie muzyki, separacja źródeł i wykrywanie dźwięków otoczenia szybko się rozwijają. Branża ta stoi przed ciągłymi wyzwaniami – niskim poziomem zasobów językowych, hałaśliwym otoczeniem, problemami etycznymi związanymi z klonowaniem głosu – ale trajektoria jest jasna: maszyny stają się tak dobre, jak ludzie, jeśli chodzi o słyszenie, rozumienie i wytwarzanie dźwięku.