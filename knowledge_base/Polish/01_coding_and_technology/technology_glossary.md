<!--
---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
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

-->
# Słowniczek technologii
Glosariusz referencyjny obejmujący modele sztucznej inteligencji, sprzęt, testy porównawcze i podstawowe koncepcje
we współczesnym krajobrazie sztucznej inteligencji i obliczeń.
---

## Modele językowe AI i asystenci
### CzatGPT
ChatGPT to chatbot AI opracowany przez OpenAI, wydany po raz pierwszy w listopadzie 2022 r.
Jest zasilany przez serię dużych modeli językowych GPT (LLM). ChatGPT jest jednym
najszybciej rozwijających się konsumenckich produktów AI w historii, osiągając 100 milionów
użytkowników w ciągu dwóch miesięcy od premiery. Obsługuje konwersację tekstową, kod
generowanie, podsumowanie i twórcze pisanie. Płatne poziomy zapewniają dostęp do
mocniejsze modele, takie jak GPT-4 i GPT-4o.
### GPT (wstępnie przeszkolony transformator generatywny)
GPT to rodzina dużych modeli językowych stworzonych przez OpenAI. Architektura
używa transformatora przeznaczonego wyłącznie do dekodera, wytrenowanego z włączonym celem przewidywania następnego żetonu
ogromne korpusy tekstowe. Kluczowe wersje obejmują GPT-2 (2019, parametry 1.5B, godne uwagi
za rozgłos „zbyt niebezpieczne, aby je opublikować”), GPT-3 (2020, parametry 175B, powszechnie
używany przez API), GPT-3.5 (szkielet oryginalnego ChatGPT) i GPT-4
(2023, multimodalny, w wielu testach wydajność zbliżona do poziomu ludzkiego eksperta).
### Klaudiusz
Claude to asystent AI opracowany przez firmę Anthropic. Został nazwany na cześć Claude'a
Shannona, twórcy teorii informacji. Anthropic zostało założone przez byłego
badaczy OpenAI i koncentruje się na „konstytucyjnej sztucznej inteligencji” — technice, którą można zastosować
modele bezpieczniejsze, ucząc je przestrzegania zestawu zasad. Modele Claude'a
(Claude 1, 2, 3 Haiku / Sonnet / Opus) znane są z długich okien kontekstowych (do góry
do 200 000 tokenów), zniuansowane rozumowanie i zmniejszona szkodliwość w porównaniu do
podstawowe LLM.
### Bliźnięta
Gemini to rodzina multimodalnych modeli sztucznej inteligencji firmy Google DeepMind, ogłoszona w r
Grudzień 2023 r. Gemini jest natywnie multimodalny — przeszkolony od podstaw
jednocześnie tekst, obrazy, dźwięk i wideo, w przeciwieństwie do wcześniejszych modeli
modalności dodane poprzez dostrajanie. Wersje obejmują Gemini Nano (na urządzeniu),
Gemini Flash (szybki, ekonomiczny) i Gemini Ultra (najwyższa wydajność).
Gemini obsługuje chatbota Google AI Bard (przemianowanego na Gemini) i sztuczną inteligencję wyszukiwarki Google
Przeglądy.
### Phi-3-mini
Phi-3-mini to model małego języka (SLM) opracowany przez firmę Microsoft w wersji 3.8B
parametry. Został wydany w kwietniu 2024 roku. W przeciwieństwie do większości dużych modeli, Phi-3-mini
został przeszkolony na starannie dobranym zbiorze danych o jakości podręcznikowej – jest to technika
którego pionierem jest dział Microsoft Research — który przedkłada jakość danych nad ich surową objętość.
Pomimo tego, że jest znacznie mniejszy niż GPT-4 lub Claude 3 Opus, Phi-3-mini pasuje lub
przewyższa modele kilka razy większe w testach porównawczych rozumowania, takich jak MMLU i
HumanEval. Obsługuje okno kontekstowe tokena 4k w wariancie podstawowym i 128k
okno w wariancie długokontekstowym. Phi-3-mini może działać na pojedynczym konsumenckim procesorze graficznym
lub nawet na urządzeniu na nowoczesnym smartfonie z wystarczającą ilością pamięci RAM.
### Lama (Meta AI)
Lama (Large Language Model Meta AI) to rodzina modeli z otwartymi ciężarami
wydany przez Metę. Lama 2 (2023) została wypuszczona do celów badawczych i komercyjnych
o rozmiarach w zakresie parametrów od 7B do 70B. Ulepszona Lama 3 (2024).
znacznie wydajność, w przypadku modeli od 8B do 70B (a później 400B+).
Ponieważ ciężary można pobrać publicznie, podstawą są modele lamy
dla dużego ekosystemu dopracowanych wariantów (Mistral, Alpaca, Vicuna itp.)
i są szeroko stosowane w lokalnych/prywatnych wdrożeniach sztucznej inteligencji.
### Mistrala
Mistral AI to francuska firma zajmująca się sztuczną inteligencją, która rozwija otwarte i zastrzeżone LLM.
Mistral 7B (2023) wykazał, że model o parametrach 7B może odpowiadać
wydajność znacznie większych modeli przy użyciu wydajnych technik, takich jak przesuwanie
uwaga okna i uwaga skupiona na zapytaniach. Mixtral 8x7B (2023) to mieszanka-
model ekspertów — kieruje każdy token do podzbioru 8 sieci eksperckich,
osiągnięcie wydajności na poziomie GPT-3.5, będąc jednocześnie tańszym obliczeniowo.
Modele Mistrala są w pełni otwarte i można je uruchamiać lokalnie.
---

## Sprzęt GPU i karty graficzne
### GPU (jednostka przetwarzania grafiki)
Procesor graficzny to procesor zaprojektowany do obliczeń masowo równoległych. Pierwotnie
Zbudowane do renderowania grafiki 3D, procesory graficzne stały się niezbędne w szkoleniu AI/ML
i wnioskowanie, ponieważ mogą wykonywać tysiące operacji zmiennoprzecinkowych
jednocześnie wykorzystując tysiące małych rdzeni. Dwóch głównych producentów procesorów graficznych
dla AI są NVIDIA i AMD.
### Seria NVIDIA GeForce RTX
Seria RTX (Ray Tracing Texel eXtreme) to linia konsumenckich procesorów graficznych firmy NVIDIA. RTX
Do generacji 30xx (Ampere, 2020) i RTX 40xx (Ada Lovelace, 2022) zaliczają się
dedykowane rdzenie Tensor do przyspieszania operacji AI. VRAM (pamięć wideo) to
ma kluczowe znaczenie dla lokalnego uruchamiania modeli AI — procesor graficzny 8 GB może obsłużyć parametr 7B
modele w kwantyzacji 4-bitowej; procesor graficzny o pojemności 24 GB może obsłużyć modele 70B w trybie 4-bitowym.
### Seria NVIDIA A i H (centrum danych)
A100 (Ampere, 2020) i H100 (Hopper, 2022) to profesjonalna sztuczna inteligencja firmy NVIDIA
akceleratory. H100 ma do 80 GB pamięci HBM3 i jest standardem
sprzęt stojący za większością dzisiejszych szkoleń LLM na dużą skalę. Te procesory graficzne kosztują 25 000 USD–
40 000 dolarów za sztukę, ale oferują 10–30 razy większą przepustowość AI niż konsumenckie karty RTX.
### Seria AMD Radeon RX
Linia konsumenckich procesorów graficznych AMD. RX 7900 XTX (2022) ma 24 GB pamięci VRAM i może działać
lokalne LLM za pośrednictwem ROCm (stos obliczeniowy GPU AMD). Procesory graficzne AMD są generalnie mniejsze
dobrze obsługiwane niż NVIDIA dla platform AI, chociaż obsługa ulega poprawie.
### Łuk Intela
Intel Arc to linia dyskretnych produktów GPU firmy Intel, wprowadzana na rynek od 2022 roku. Arc
Procesory graficzne obsługują XeSS (superpróbkowanie firmy Intel) i mają ograniczone, ale rosnące wsparcie
do zadań wnioskowania AI za pośrednictwem platform OpenVINO i IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK to oficjalna baza danych specyfikacji produktów firmy Intel pod adresem ark.intel.com. To
zapewnia szczegółowe specyfikacje techniczne dla każdego procesora Intel, procesora graficznego, FPGA i
Produkt NUC, w tym liczba rdzeni, prędkość zegara, TDP, obsługiwane typy pamięci,
i funkcje zestawu instrukcji. Kiedy usłyszysz „sprawdź specyfikacje ARK”, oznacza to
odwiedzanie tej bazy danych w celu uzyskania wiarygodnych informacji o sprzęcie.
---

## Testy wydajności AI
### MMLU (rozumienie języków wielozadaniowych)
MMLU to benchmark testujący wiedzę LLM z 57 przedmiotów akademickich, w tym
matematyka, historia, prawo, medycyna i informatyka. Składa się z
pytania wielokrotnego wyboru zaczerpnięte z prawdziwych egzaminów na poziomie uniwersyteckim. Wynik
70% to mniej więcej poziom licencjata człowieka; GPT-4 i Claude 3 uzyskały wynik powyżej 86%.
Pomimo niewielkich rozmiarów Phi-3-mini uzyskuje około 70% punktów.
###Ewaluacja Człowieka
HumanEval to punkt odniesienia OpenAI do generowania kodu. Składa się ze 164 Pythonów
problemy programistyczne przy użyciu zautomatyzowanych przypadków testowych. Modele są mierzone
pass@k — prawdopodobieństwo, że co najmniej jedno z k wygenerowanych rozwiązań przejdzie wszystkie
testy. Wynik GPT-4 ~87% (zaliczenie@1); dobrze dostrojony model 7B może osiągnąć ~ 50–60%.
### HellaSwag
HellaSwag to punkt odniesienia oparty na zdrowym rozsądku. Modelki otrzymują wyrok
opisując przyziemną czynność i musi wybrać najbardziej prawdopodobną kontynuację
cztery opcje. Nieprawidłowe opcje zostały specjalnie zaprojektowane tak, aby były wiarygodne, ale
subtelnie błędne. Testuje, czy model ma ugruntowaną wiedzę na temat fizyki
i sytuacjach społecznych.
### ARC (wyzwanie polegające na rozumowaniu AI2)
ARC jest punktem odniesienia opracowanym przez Allen Institute for AI. Składa się ze szkoły podstawowej
pytania naukowe, podzielone na zestawy „Łatwe” i „Wyzwanie”. Zestaw Wyzwania
zawiera pytania dotyczące metod wyszukiwania i prostych modeli statystycznych
borykać się z problemami, wymagającymi wieloetapowego rozumowania.
---

## Podstawowe koncepcje AI/ML
### RAG (generacja wzmocniona odzyskiwaniem)
RAG to technika łącząca system wyszukiwania (zazwyczaj wektor
baza danych) z modelem języka. Zamiast polegać wyłącznie na modelu
parametrycznej, RAG najpierw pobiera odpowiednie dokumenty z zewnątrz
bazę wiedzy, a następnie włącza ją do kontekstu modelu. Pozwala to
model umożliwiający odpowiadanie na pytania dotyczące informacji aktualnych lub specyficznych dla domeny
bez przekwalifikowania się. Potato.ai używa formy RAG — pobiera ze swojej bazy danych
i uwzględnia wyniki w kontekście przed wygenerowaniem odpowiedzi.
### Dostrajanie
Dostrajanie to proces ciągłego uczenia wcześniej wytrenowanego modelu na platformie
mniejszy, specyficzny dla domeny zbiór danych. Spowoduje to dostosowanie ciężaru modelu do:
konkretne zadanie lub dziedzina. Na przykład podstawowy LLM może zostać dostrojony
dokumentację medyczną, aby stworzyć asystenta medycznego Q&A. Dostrajanie jest
kosztowne obliczeniowo, ale znacznie tańsze niż szkolenie od zera.
### Kwantyzacja
Kwantyzacja zmniejsza precyzję numeryczną wag modeli (np. z 32-bitowych
float do 4-bitowej liczby całkowitej). To radykalnie zmniejsza zużycie pamięci — model 7B
w 16-bitowej precyzji wymaga ~14 GB VRAM; ten sam model w wersji 4-bitowej (format GGUF)
wymaga ~4 GB. Kwantyzacja zazwyczaj zapewnia niewielką, ale akceptowalną dokładność
degradacji i jest główną techniką umożliwiającą uruchamianie dużych modeli na rynku konsumenckim
sprzętu, a nawet urządzeń mobilnych.
### Okno kontekstowe
Okno kontekstowe to maksymalna liczba tokenów, które model może przetworzyć jednocześnie,
włączając zarówno monit, jak i wygenerowaną odpowiedź. GPT-3.5 miał 4096 tokenów
okno; GPT-4 Turbo i Claude 3 obsługują 128 000 tokenów; Bliźnięta 1.5 Pro
obsługuje 1 000 000 tokenów. Większe okno kontekstowe pozwala modelowi „widzieć”
bardziej rozmowę lub dokument na raz, poprawiając spójność na dłużej
wymiany.
### RLHF (uczenie się ze wzmocnieniem na podstawie informacji zwrotnej od ludzi)
RLHF to technika szkoleniowa, która przekształca model języka podstawowego (który
po prostu przewiduje następny żeton) do asystenta, który postępuje zgodnie z instrukcjami i
zachowuje się pomocnie. Osoby oceniające oceniają wyniki modelu, szkolony jest model nagrody
na ich preferencjach, a model języka jest następnie optymalizowany pod tym kątem
model nagrody wykorzystujący uczenie się przez wzmacnianie. Używają ChatGPT, Claude i Gemini
warianty RLHF lub podobnych technik dopasowywania (np. konstytucyjna AI,
Bezpośrednia optymalizacja preferencji).
### Architektura transformatorowa
Transformer to architektura sieci neuronowej leżąca u podstaw wszystkich nowoczesnych LLM.
Zaprezentowany w artykule Vaswani i in. z 2017 r. „Attention Is All You Need”
wykorzystuje mechanizmy samouważności do przetwarzania wszystkich tokenów równolegle, a nie
sekwencyjnie. Transformatory tylko z enkoderem (BERT) służą do zrozumienia zadań;
Do zadań generacyjnych wykorzystywane są transformatory wyłącznie dekoderowe (GPT, Lama, Mistral);
enkoder-dekoder Transformatory (T5, BART) służą do translacji i podsumowania.
### Osadzania i bazy danych wektorowych
Osadzenia to gęste numeryczne reprezentacje tekstu (lub obrazów) utworzone przez
sieć neuronowa. Teksty podobne semantycznie mają zbliżone osadzania
przestrzeń wektorowa. Sklep z wektorowymi bazami danych (ChromaDB, Pinecone, Weaviate, Qdrant).
te osadzania i obsługują szybkie przybliżone wyszukiwanie najbliższego sąsiada. Są
szkielet pamięci masowej systemów RAG, obejmujący warstwę pamięci zimnej Potato.ai.