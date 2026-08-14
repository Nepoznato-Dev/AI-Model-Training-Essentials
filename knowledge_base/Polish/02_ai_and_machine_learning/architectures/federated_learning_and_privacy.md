---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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
# Sfederowane uczenie się i prywatność
Uczenie federacyjne to technika uczenia modeli uczenia maszynowego na wielu urządzeniach lub w wielu organizacjach bez udostępniania surowych danych. Zamiast wysyłać dane do centralnego serwera, każde urządzenie trenuje model lokalny i udostępnia jedynie aktualizacje modelu (gradienty lub wagi). Serwer centralny agreguje te aktualizacje w celu utworzenia modelu globalnego. Został zaprojektowany przez Google do uczenia modeli języków klawiatury na telefonach z Androidem i od tego czasu stał się kluczową techniką sztucznej inteligencji chroniącej prywatność.
---

## Dlaczego uczenie się stowarzyszone?
| Motywacja | Opis | Przykład |
|------------|------------|--------|
| **Prywatność danych** | Surowe dane nigdy nie opuszczają urządzenia | Dokumentacja medyczna pozostaje w szpitalu; zdjęcia zostają w telefonie |
| **Zgodność z przepisami** | RODO, HIPAA i inne regulacje ograniczają udostępnianie danych | Banki mogą współpracować bez udostępniania danych klientów |
| **Objętość danych** | Przenoszenie danych jest drogie i powolne | Szkolenie na miliardach telefonów jest niepraktyczne, jeśli trzeba przesyłać dane
| **Wrażliwość danych** | Niektóre dane są zbyt wrażliwe, aby je udostępniać, nawet za zgodą | Wywiad rządowy; dane osobowe dotyczące zdrowia |
---

## Jak działa stowarzyszone uczenie się
### Protokół podstawowy (FedAvg)
| Krok | Co się dzieje |
|------|------------|
| **1. Zainicjuj** | Serwer centralny tworzy model globalny z losowymi wagami |
| **2. Rozpowszechniaj** | Serwer wysyła aktualny model globalny do wybranych urządzeń |
| **3. Szkolenia lokalne** | Każde urządzenie trenuje model na swoich lokalnych danych przez kilka epok |
| **4. Prześlij** | Urządzenia wysyłają zaktualizowane masy modeli (nie dane) z powrotem do serwera |
| **5. Agregat** | Serwer uśrednia wagi (Federated Averaging), aby utworzyć nowy model globalny |
| **6. Powtórz** | Wracaj do kroku 2, aż model będzie zbieżny |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Właściwości klucza
| Nieruchomość | Opis |
|---------|------------|
| **Dane inne niż IID** | Każde urządzenie ma inne rozkłady danych (nie są niezależne i jednakowo rozłożone) |
| **Dane niezbilansowane** | Niektóre urządzenia mają dużo danych, inne bardzo mało |
| **Częściowy udział** | Nie wszystkie urządzenia są dostępne w każdej rundzie |
| **Efektywność komunikacji** | Wąskim gardłem jest komunikacja, a nie obliczenia |
---

## Warianty uczenia się stowarzyszonego
| Wariant | Opis | Zaleta |
|--------|------------|----------|
| **Średnia Fed** | Średnie masy modeli na różnych urządzeniach | Prosty; działa dobrze dla danych IID |
| **FedProx** | Dodaje termin proksymalny do lokalnego szkolenia | Lepsze dla danych innych niż IID |
| **RUSZTOWANIE** | Wykorzystuje zmienne kontrolne w celu skorygowania heterogeniczności danych | Szybsza zbieżność danych innych niż IID |
| **FedSGD** | Podobnie jak FedAvg, ale z jednym krokiem gradientu na rundę | Niższy koszt komunikacji na rundę |
| **Spersonalizowany FL** | Każde urządzenie ma swój spersonalizowany model obok modelu globalnego | Lepsza wydajność na urządzeniu |
| **Pionowy FL** | Różne funkcje (nie różne próbki) pomiędzy stronami | Kiedy strony posiadają różne aspekty tych samych danych |
---

## Prywatność różnicowa
Prywatność różnicowa (DP) zapewnia matematyczną gwarancję, że wynik algorytmu nie ujawni, czy uwzględniono dane jakiejkolwiek osoby.
### Definicja rdzenia
Mechanizm M spełnia (ε, δ)-różnicową prywatność, jeśli dla dowolnych dwóch zbiorów danych D i D', które różnią się jednym rekordem:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parametr | Znaczenie |
|---------------|--------|
| **ε (epsilon)** | Budżet prywatności. Mniejszy = bardziej prywatny. Typowe wartości: 0,1–10. |
| **δ (delta)** | Prawdopodobieństwo niepowodzenia gwarancji prywatności. Zwykle ustawiane na 1/N (odwrotność rozmiaru zbioru danych). |
### Mechanizmy zwiększające prywatność
| Mechanizm | Jak to działa | Przypadek użycia |
|----------|------------|---------|
| **Mechanizm Gaussa** | Dodaj szum Gaussa skalibrowany do czułości zapytania | Wartości ciągłe (wagi modeli) |
| **Mechanizm Laplace’a** | Dodaj szum Laplace'a | Liczenie zapytań |
| **Mechanizm wykładniczy** | Wybierz wyjścia z prawdopodobieństwem proporcjonalnym do ich użyteczności | Dyskretne wybory |
### DP-SGD (różnicowo prywatne stochastyczne opadanie gradientu)
| Krok | Opis |
|------|------------|
| 1. Oblicz gradienty dla każdej próbki | Zamiast gradientów wsadowych |
| 2. Gradienty klipu | Ograniczona maksymalna norma każdego gradientu (ogranicza wpływ pojedynczej próbki) |
| 3. Dodaj szum | Dodaj skalibrowany szum Gaussa do zagregowanego gradientu |
| 4. Aktualizuj parametry | Standardowy stopień zejścia gradientowego |
| Kompromis | Opis |
|---------------|------------|
| **Prywatność a dokładność** | Większa prywatność (niższe ε) wymaga większego szumu, co zmniejsza dokładność modelu |
| **Prywatność a czas szkolenia** | Większy szum oznacza wolniejszą zbieżność |
| **Śledzenie budżetu prywatności** | Każdy etap szkolenia pochłania część budżetu przeznaczonego na prywatność; raz wydane, nie można go odzyskać |
---

## Łączenie nauczania stowarzyszonego z prywatnością różnicową
| Warstwa | Ochrona |
|-------|-----------|
| **Uczenie się stowarzyszone** | Surowe dane pozostają na urządzeniach |
| **Prywatność różnicowa** | Nawet aktualizacje modeli są hałaśliwe, chroniąc indywidualne wkłady |
| **Bezpieczna agregacja** | Serwer widzi tylko sumę wszystkich aktualizacji, a nie pojedyncze |
Ta kombinacja zapewnia silną gwarancję prywatności: nawet jeśli serwer zostanie naruszony, nie będzie w stanie określić, czy dane konkretnej osoby zostały wykorzystane podczas szkolenia.
---

## Inne techniki ochrony prywatności
### Bezpieczne obliczenia wielostronne (SMPC)
Wiele stron oblicza funkcję na podstawie połączonych danych bez ujawniania indywidualnych danych wejściowych.
| Funkcja | Opis |
|--------|------------|
| **Jak to działa** | Dane są dzielone na udziały dystrybuowane pomiędzy stronami; obliczenia odbywają się na udziałach |
| **Gwarancja** | Żadna ze stron nie dowiaduje się niczego o wkładach innych |
| **Nad głową** | Znaczące koszty komunikacji i obliczeń |
| **Przypadek użycia** | Banki obliczające wspólne modele ryzyka bez udostępniania danych klientów |
### Szyfrowanie homomorficzne (HE)
Wykonuj obliczenia bezpośrednio na zaszyfrowanych danych.
| Wpisz | Co obsługuje | Nad głową |
|------|-----------------|---------|
| **Częściowo ON** | Jedna operacja (dodawanie LUB mnożenie) | Niski |
| **Trochę ON** | Ograniczona liczba obu operacji | Średni |
| **W pełni HE** | Obliczenia arbitralne | Bardzo wysokie (spowolnienie 100-1000x) |
| Aplikacja | Opis |
|------------|------------|
| **Prywatne wnioski** | Uruchamiaj modele ML na zaszyfrowanych danych; zwróć zaszyfrowane prognozy |
| **Zaszyfrowane szkolenie** | Trenuj na zaszyfrowanych danych (wciąż głównie teoretycznych do głębokiego uczenia się) |
| **Prywatne zapytania** | Zapytanie do bazy danych bez ujawniania zapytania lub danych |
### Zaufane środowiska wykonawcze (TEE)
Izolacja sprzętowa (Intel SGX, ARM Trustzone), która chroni dane nawet przed systemem operacyjnym.
| Zaleta | Ograniczenie |
|--------------|------------|
| Wydajność niemal natywna | Wymaga określonego sprzętu |
| Silne gwarancje bezpieczeństwa | Ograniczona pamięć (rozmiar enklawy) |
| Brak narzutu kryptograficznego | Możliwe ataki z kanału bocznego |
---

## Regulamin prywatności i ML
| Rozporządzenie | Region | Wpływ na ML |
|------------|------------|------------|
| **RODO** | UE | Prawo do wyjaśnień; minimalizacja danych; zgoda na przetwarzanie; prawo do usunięcia |
| **CCPA** | Kalifornia | Prawo do informacji, usunięcia i rezygnacji ze sprzedaży danych |
| **HIPA** | USA (opieka zdrowotna) | Ścisła kontrola danych dotyczących zdrowia; wymogi dotyczące deidentyfikacji |
| **PIPL** | Chiny | Lokalizacja danych; wymagania dotyczące zgody; zasady transferu transgranicznego |
| **Ustawa o sztucznej inteligencji** | UE | Wymogi dotyczące przejrzystości; klasyfikacja ryzyka; praktyki zabronione |
### Wpływ na przepływy pracy uczenia maszynowego
| Zasada RODO | Implikacja ML |
|----------------|----------------------------|
| **Minimalizacja danych** | Zbieraj tylko to, co jest potrzebne; stowarzyszone uczenie się pomaga |
| **Ograniczenie celu** | Nie można ponownie wykorzystać danych bez nowej zgody |
| **Prawo do usunięcia** | Musi być w stanie usunąć dane osoby z wyszkolonego modelu (oduczenie maszynowe) |
| **Prawo do wyjaśnień** | Modele muszą być wystarczająco interpretowalne, aby wyjaśnić indywidualne przewidywania
| **Prywatność już w fazie projektowania** | Prywatność musi być wbudowana w systemy od początku |
---

## Wyzwania
| Wyzwanie | Opis |
|---------------|------------|
| **Koszt komunikacji** | Wysyłanie aktualizacji modeli na miliony urządzeń jest drogie |
| **Dane inne niż IID** | Urządzenia mają bardzo różne rozkłady danych, co szkodzi konwergencji |
| **Maruderzy** | Powolne urządzenia opóźniają całą rundę |
| **Kompromis między prywatnością a użytecznością** | Większa prywatność oznacza gorszą wydajność modelu |
| **Ataki zatrucia** | Złośliwi uczestnicy mogą zepsuć model globalny |
| **Ekstrakcja modelu** | Nawet udostępnione aktualizacje modeli mogą powodować wyciek informacji o danych szkoleniowych
| **Niejednorodność sprzętu** | Różne urządzenia mają różne możliwości obliczeniowe |
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **Kwiat** | Sfederowana platforma uczenia się typu open source; niezależny od frameworka |
| **Stowarzyszenie TensorFlow** | Framework Google FL dla modeli TensorFlow |
| **PySyft** (OpenMined) | ML chroniące prywatność w PyTorch |
| **Los** (Webank) | Sfederowana platforma edukacyjna klasy przemysłowej |
| **LIŚĆ** | Zestaw testów porównawczych do stowarzyszonych badań nad uczeniem się |
| **Nieprzezroczystość** (Meta) | Prywatność różnicowa dla PyTorch |
| **Prywatność Google TF** | Prywatność różnicowa dla TensorFlow |
---

## Streszczenie
Techniki stowarzyszonego uczenia się i ochrony prywatności rozwiązują podstawowe napięcie: jak zbudować potężne modele sztucznej inteligencji, gdy dane są rozproszone, wrażliwe lub podlegają przepisom? Uczenie federacyjne przechowuje dane na urządzeniach i udostępnia tylko aktualizacje modeli. Prywatność różnicowa dodaje matematyczne gwarancje, że indywidualne wkłady nie zostaną wykryte. Bezpieczne obliczenia i szyfrowanie homomorficzne idą dalej, umożliwiając obliczenia na zaszyfrowanych danych. Każda technika wiąże się z kosztami — narzutami na komunikację, zmniejszoną dokładnością, kosztami obliczeniowymi — ale razem tworzą one zestaw narzędzi do tworzenia sztucznej inteligencji, która szanuje prywatność, a jednocześnie uczy się na podstawie danych ze świata.