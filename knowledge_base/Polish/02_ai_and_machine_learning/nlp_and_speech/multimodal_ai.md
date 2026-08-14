<!--
---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
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
tags: [multimodal, ai, ai-and-machine-learning]
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
# Multimodalna sztuczna inteligencja
Multimodalne systemy AI przetwarzają i łączą informacje z wielu typów danych — tekstu, obrazów, dźwięku, wideo i innych — jednocześnie. Podczas gdy wcześniejsze systemy sztucznej inteligencji były zazwyczaj jednomodalne (tylko tekst, tylko obraz), nowoczesne systemy o największych możliwościach są wielomodalne. GPT-4V odczytuje razem obrazy i tekst; Gemini natywnie przetwarza tekst, obrazy, dźwięk i wideo; a systemy takie jak Sora generują wideo na podstawie opisów tekstowych. W tym pliku opisano, jak działa multimodalna sztuczna inteligencja, stojące za nią architektury i dlaczego łączenie modalności jest tak skuteczne.
---

## Dlaczego multimodalny?
| Korzyści | Opis | Przykład |
|--------|------------|--------|
| **Większe zrozumienie** | Różne sposoby dostarczają informacji uzupełniających | Wideo przekazuje ruch, dźwięk i kontekst, których sam tekst nie jest w stanie |
| **Lepsza generalizacja** | Uczenie się między modalnościami tworzy solidniejsze reprezentacje | Modelka, która widziała zarówno zdjęcia, jak i opisy tekstowe „kota”, lepiej rozumie tę koncepcję |
| **Bardziej naturalna interakcja** | Ludzie komunikują się wieloma kanałami | Asystenci głosowi, którzy widzą, na co wskazujesz |
| **Transfer międzymodalny** | Wiedza z jednej modalności pomaga w innej | Rozumienie obrazu poprawia generowanie tekstu i odwrotnie
---

## Podstawowe architektury
### Modele języka wizyjnego (VLM)
Modele przetwarzające jednocześnie obrazy i tekst.
| Architektura | Jak to działa | Przykłady |
|------------|------------|--------|
| **Podwójny koder** | Oddzielne kodery dla obrazu i tekstu; połączyć na późniejszym etapie | ZACISK, WYRÓWNANIE |
| **Koder Fusion** | Tokeny obrazowe i tekstowe są przeplatane i przetwarzane razem | Flaming, Bliźnięta |
| **Wzajemna uwaga** | Tokeny tekstowe obsługują funkcje obrazu (lub odwrotnie) | Flaming, CoCa |
| **Ujednolicony tokeniser** | Obrazy są konwertowane na tokeny i przetwarzane razem z tokenami tekstowymi | Bliźnięta, Kameleon |
### Jak działają modele języka wizyjnego
| Krok | Opis |
|------|------------|
| **1. Zakoduj obraz** | Koder wizyjny (ViT, SigLIP) konwertuje obraz na zbiór wektorów cech |
| **2. Zakoduj tekst** | Koder języka przetwarza tokeny tekstowe |
| **3. Modyfikacje bezpieczników** | Cechy obrazu są rzutowane na przestrzeń osadzania modelu języka |
| **4. Generuj** | Model języka tworzy tekst uwarunkowany zarówno obrazem, jak i tekstem wejściowym |
### Kluczowe modele wizjonersko-językowe
| Modelka | Deweloper | Architektura | Godna uwagi funkcja |
|-------|-----------|------------|----------------|
| **KLIP** | OpenAI | Podwójny koder (ViT + koder tekstu) | Klasyfikacja obrazu zero-shot za pomocą tekstu |
| **LLaVA** | Otwarte oprogramowanie | Koder wizualny LLaMA + CLIP | VLM typu open source; silna społeczność |
| **GPT-4V / 4o** | OpenAI | Ujednolicony multimodalny | Przetwarza razem tekst, obrazy i dźwięk |
| **Bliźnięta** | Google DeepMind | Natywnie multimodalny ze szkoleń | Zbudowany od podstaw z myślą o transporcie multimodalnym |
| **Claude** | Antropiczny | Wizja + tekst | Dobrze radzi sobie ze zrozumieniem dokumentów i wykresów |
| **Qwen-VL** | Alibaby | Otwarta waga VLM | Konkurencja z modelami zamkniętymi |
| **StażystaVL** | Otwarte oprogramowanie | Wieloskalowy koder wizyjny | Silna opcja open source |
---

## Modele dźwięku i mowy
### Rozpoznawanie mowy (ASR)
| Modelka | Architektura | Godna uwagi funkcja |
|-------|------------|--------------------------------|
| **Szept** (OpenAI) | Enkoder-dekoder Transformator | Przeszkolony na 680 000 godzin wielojęzycznego dźwięku; solidny |
| **Konformer** | Splot + samouważność | Łączy funkcje lokalne i globalne |
| **wav2vec 2.0** | Samonadzorowany | Uczy się z nieoznaczonej mowy |
| **USM** (Google) | Uniwersalny model mowy | 2 miliony godzin oznakowanych danych; Ponad 300 języków |
### Zamiana tekstu na mowę (TTS)
| Modelka | Podejście | Godna uwagi funkcja |
|-------|----------|--------------------------------|
| **VALL-E** (Microsoft) | Kodek neuronowy | Klonowanie głosu z 3-sekundowej próbki |
| **Kora** (Suno) | Oparte na transformatorze | Wielojęzyczny; zawiera dźwięki inne niż mowa |
| **JedenaścieLab** | Komercyjne | Wysokiej jakości klonowanie głosu |
| **CzatTTS** | Otwarte oprogramowanie | Mowa konwersacyjna z naturalną prozodią |
| **Mowa Ryby** | Otwarte oprogramowanie | Wielojęzyczny; szybkie wnioskowanie |
### Rozumienie dźwięku
| Modelka | Zdolność |
|-------|-----------|
| **AudioLDM** | Generowanie efektu dźwiękowego z tekstu |
| **MusicGen** (Meta) | Generowanie tekstu na muzykę |
| **Qwen-Audio** | Rozumienie dźwięku (mowa, muzyka, dźwięki otoczenia) |
| **ŁOSOSI** | Rozumienie mowy, dźwięku, języka, muzyki i hałasu |
---

## Modele wideo
Wideo łączy obrazy, dźwięk, tekst i czas, co czyni go najbardziej złożoną modalnością.
| Modelka | Wpisz | Zdolność |
|-------|------|------------|
| **Sora** (OpenAI) | Tekst na wideo | Do 1080p; rozumie fizykę |
| **Bliźnięta** | Rozumienie wideo | Potrafi analizować długie filmy z dźwiękiem |
| **Wideo-LLaVA** | Wideo + tekst | Zrozumienie wideo typu open source |
| **Pas startowy Gen-3** | Tekst/obraz do wideo | Komercyjna generacja wideo |
| **Kling** | Tekst na wideo | Generowanie wideo w długiej formie |
### Wyzwania dotyczące zrozumienia wideo
| Wyzwanie | Opis |
|---------------|------------|
| **Rozumowanie tymczasowe** | Zrozumienie wydarzeń rozwijających się w czasie |
| **Długi kontekst** | Filmy mogą trwać godzinami; przetwarzanie wszystkich klatek jest drogie |
| **Synchronizacja audiowizualna** | Łączenie tego, co zostało powiedziane z tym, co zostało pokazane |
| **Przyczynowość** | Zrozumienie przyczyny i skutku w sekwencjach wideo |
---

## Pobieranie międzymodalne
Znajdowanie odpowiednich treści w różnych modalnościach.
| Zadanie | Opis | Przykład |
|------|------------|--------|
| **Tekst → Obraz** | Znajdź obrazy pasujące do zapytania tekstowego | Wyszukaj „zachód słońca nad górami” w bibliotece zdjęć |
| **Obraz → Tekst** | Znajdź tekst odnoszący się do obrazu | Generowanie podpisów do obrazów |
| **Tekst → Dźwięk** | Znajdź dźwięki pasujące do opisu | Projekt dźwiękowy: „ślady na żwirze” |
| **Obraz → Obraz** | Znajdź wizualnie podobne obrazy | Wyszukiwanie produktów według obrazu |
### CLIP do pobierania międzymodalnego
Wspólna przestrzeń do osadzania CLIP umożliwia natychmiastowe pobieranie międzymodalne:
| Krok | Opis |
|------|------------|
| 1 | Zakoduj wszystkie obrazy za pomocą kodera wizyjnego |
| 2 | Zakoduj zapytanie tekstowe za pomocą kodera tekstu |
| 3 | Oblicz podobieństwo cosinusa pomiędzy osadzeniem tekstu i wszystkimi osadzeniem obrazu |
| 4 | Zwróć obrazy o najwyższym podobieństwie |
Działa to bez żadnego szkolenia dotyczącego konkretnego zadania — jest to właściwość zwana **możliwością zerowego strzału**.
---

## Wcielona sztuczna inteligencja
Ucieleśniona sztuczna inteligencja łączy percepcję multimodalną z działaniem fizycznym.
| Systemu | Modalność | Aplikacja |
|--------|----------|------------|
| **RT-2** (Google) | Wizja + język → działania robota | Sterowanie robotem ogólnego przeznaczenia z instrukcji tekstowych |
| **Październik** | Polityka dotycząca robotów typu open source | Przeszkolony w oparciu o różnorodne dane robota |
| **Tesla Optimus** | Wizja + język → zadania fizyczne | Robot humanoidalny do zadań ogólnych |
| **Rysunek 01** | Wizja + język + mowa | Humanoidalny robot potrafiący rozmawiać |
### Wyzwania związane z ucieleśnioną sztuczną inteligencją
| Wyzwanie | Dlaczego to jest trudne |
|----------|-------------|
| **Przerwa między Simem a prawdziwym** | Symulacja nie oddaje doskonale fizyki świata rzeczywistego |
| **Zręczność** | Drobna kontrola motoryczna (dłonie, palce) jest niezwykle trudna |
| **Bezpieczeństwo** | Fizyczne roboty mogą wyrządzić prawdziwą krzywdę |
| **Przetwarzanie w czasie rzeczywistym** | Musisz dostrzec, zdecydować i działać w milisekundach |
| **Uogólnienie** | Robot przeszkolony do podnoszenia czerwonych kubków może zawieść w przypadku niebieskich |
---

## Dane i szkolenia
### Dane dotyczące treningu multimodalnego
| Zbiór danych | modalności | Rozmiar |
|--------|-----------|------|
| **LAION-5B** | Pary obraz-tekst | 5,85 miliarda par |
| **Komputer danych** | Wyselekcjonowany obraz-tekst | Punkt odniesienia w projektowaniu zbiorów danych |
| **WIT** (Wikipedia) | Tekst obrazu z Wikipedii | 11,5 mln par |
| **JakTo100M** | Wideo-tekst (filmy instruktażowe) | 100 milionów klipów |
| **LibriMowa** | Tekst mowy | 1000 godzin języka angielskiego |
| **Wspólny głos** | Tekst mowy | Wielojęzyczny; wniesione przez społeczność |
### Strategie szkoleniowe
| Strategia | Opis | Kiedy stosować |
|--------------|------------|------------|
| **Wspólne szkolenie** | Trenuj jednocześnie na wszystkich modalnościach | Po dostosowaniu danych multimodalnych |
| **Nauka w ramach programu nauczania** | Zacznij od prostych przykładów; zwiększ trudność | Poprawia konwergencję |
| **Uczenie się kontrastowe** | Naucz się dopasowywać powiązane pary w różnych modalnościach (w stylu CLIP) | Budowanie wspólnych reprezentacji |
| **Instrukcja strojenia** | Pociąg na multimodalnych parach instrukcja-odpowiedź | Tworzenie modeli zgodnie z instrukcjami multimodalnymi |
---

## Ocena
| punkt odniesienia | modalności | Co testuje |
|----------|-----------|--------------|
| **MMLU** | Tekst | Wiedza z 57 przedmiotów |
| **MMMU** | Tekst + obrazy | Rozumowanie na poziomie uczelni za pomocą diagramów |
| **Matematyka** | Tekst + obrazy | Rozumowanie matematyczne z danymi wizualnymi |
| **Wideo-MME** | Tekst + wideo | Rozumienie wideo i rozumowanie czasowe |
| **KASK** | Tekst + dźwięk | Długokontekstowa ocena multimodalna |
| **Ławka SWE** | Tekst + kod | Zadania inżynierii oprogramowania w świecie rzeczywistym |
---

## Streszczenie
Multimodalna sztuczna inteligencja reprezentuje przejście od modeli przeznaczonych do jednego celu do systemów, które postrzegają i rozumują we wszystkich formach danych. Modele języka wizyjnego, takie jak GPT-4V i Gemini, potrafią jednocześnie rozumieć obrazy i tekst; modele mowy, takie jak Whisper i VALL-E, obsługują dźwięk; modele wideo zaczynają przetwarzać pełną złożoność ruchomych obrazów z dźwiękiem. Trend jest jasny: najpotężniejsze systemy sztucznej inteligencji przyszłości będą natywnie wielomodalne i przetwarzają wszystkie rodzaje informacji jednocześnie. Wyzwania – dostosowanie danych, koszty obliczeniowe, ocena i wdrożenie – są znaczące, ale postęp w latach 2024–2026 jest szybki.