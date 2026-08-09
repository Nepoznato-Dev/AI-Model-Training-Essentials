---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Metodologie testowania
Testowanie pozwala zyskać pewność, że Twój kod działa — a co ważniejsze, że zmiany w nim nie psują tego, co już działa. Dobre testowanie wychwytuje błędy, zanim zrobią to użytkownicy, dokumentuje oczekiwane zachowanie i umożliwia nieustraszoną refaktoryzację. Ten plik obejmuje pełne spektrum strategii testowania, od testów jednostkowych po testy typu end-to-end, a także zasady, które sprawiają, że testowanie jest skuteczne.
---

## Piramida testowania
Piramida testowania opisuje idealny rozkład testów w projekcie.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Poziom | Hrabia | Prędkość | Koszt | Co testuje |
|-------|-------|-------|------|--------------|
| **Jednostka** | Wiele | Szybki (ms) | Niski | Poszczególne funkcje, klasy, metody |
| **Integracja** | Niektóre | Średni (100 ms-s) | Średni | Jak komponenty oddziałują na siebie; zapytania do baz danych; Wywołania API |
| **E2E** | Niewiele | Wolno (sekundy-minuty) | Wysoki | Pełny użytkownik przepływa przez rzeczywisty system |
---

## Testowanie jednostkowe
Testowanie poszczególnych jednostek kodu w izolacji.
### Zasady
| Zasada | Opis |
|---------------|------------|
| **Szybko** | Każdy test powinien działać w milisekundach |
| **Izolowane** | Testy nie są od siebie zależne; brak wspólnego stanu |
| **Deterministyczny** | To samo wejście → to samo wyjście za każdym razem (bez losowości, bez zależności od czasu) |
| **Samokontrola** | Test kończy się sukcesem lub niepowodzeniem automatycznie; brak ręcznej kontroli |
| **Na czasie** | Zapisane obok lub przed kodem (TDD) |
### Anatomia testu
| Faza | Opis |
|-------|------------|
| **Ułóż** | Skonfiguruj dane testowe i zależności |
| **Akt** | Wywołaj testowaną funkcję lub metodę |
| **Twierdzenie** | Sprawdź, czy wynik odpowiada oczekiwaniom |
### Co przetestować
| Kategoria | Przykłady |
|--------------|--------|
| **Szczęśliwa ścieżka** | Normalne dane wejściowe dają oczekiwane wyniki |
| **Przypadki Edge** | Puste wejście, null, zero, wartości maksymalne, pojedynczy element |
| **Przypadki błędów** | Nieprawidłowe dane wejściowe, brakujące dane, odmowa pozwolenia |
| **Warunki brzegowe** | Off-by-one; dokładnie na granicy |
### Wyśmiewanie i stukanie
| Termin | Opis | Kiedy stosować |
|------|------------|------------|
| **Próba** | Fałszywy przedmiot, który rejestruje, jak został nazwany | Weryfikacja interakcji (jak nazywała się ta metoda?) |
| **Odcinek** | Fałszywy obiekt, który zwraca z góry określone wartości | Udostępnienie danych testowych (zwróć tego użytkownika z bazy) |
| **Szpieg** | Opakowanie rejestrujące wywołania rzeczywistego obiektu | Częściowa weryfikacja |
| **Fałszywe** | Uproszczona, ale działająca implementacja | Baza danych w pamięci do testów |
| Kpiąca biblioteka | Język |
|----------------|------------|
| **test jednostki.próba** | Pythona |
| **Jest** | JavaScript/TypeScript |
| **Mockito** | Jawa |
| **Moq** | C# |
| **zeznaj / żart** | Idź |
---

## Testowanie integracyjne
Testowanie współpracy wielu komponentów.
| Co testować | Przykład |
|------------|------------|
| **Zapytania do bazy danych** | Czy ORM generuje poprawny kod SQL? Czy używane są indeksy? |
| **Punkty końcowe API** | Czy działa pełny cykl żądanie-odpowiedź? |
| **Interakcje serwisowe** | Czy usługa A poprawnie wywołuje usługę B? |
| **Zależności zewnętrzne** | Czy integracja z bramką płatniczą działa? |
### Strategie
| Strategia | Opis | Kompromis |
|---------|-------------|----------|
| **Prawdziwe zależności** | Użyj prawdziwej bazy danych, prawdziwej kolejki komunikatów | Najbardziej realistyczny; wolniej; trudniejsze do skonfigurowania |
| **Pojemniki testowe** | Rozkręcaj kontenery Dockera dla każdego uruchomienia testowego | Dobra równowaga; powtarzalne |
| **Alternatywy w pamięci** | H2 zamiast PostgreSQL; magistrala komunikatów w pamięci | Szybko; może pominąć problemy ze świata rzeczywistego |
| **Testowanie kontraktu** | Sprawdź, czy usługi honorują swoje umowy API | Przechwytuje zmiany interfejsu |
---

## Kompleksowe testowanie (E2E).
Testowanie całego systemu z perspektywy użytkownika.
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **dramaturg** | Automatyzacja przeglądarki | Aplikacje internetowe; w różnych przeglądarkach |
| **Cyprys** | Automatyzacja przeglądarki | Aplikacje internetowe; doświadczenie programisty |
| **Selen** | Automatyzacja przeglądarki | Dziedzictwo; szeroka obsługa języków |
| **Detoks** | Komórka E2E | Reaguj aplikacje natywne |
| **Appium** | Komórka E2E | Natywne i hybrydowe aplikacje mobilne |
| **Mistrz** | Komórka E2E | aplikacje mobilne; prosta składnia YAML |
| **k6 / Szarańcza** | Testowanie obciążenia | Wydajność pod obciążeniem |
### Najlepsze praktyki E2E
| Praktyka | Dlaczego |
|---------|-----|
| **Testuj tylko ścieżki krytyczne** | Testy E2E są powolne; skoncentruj się na tym, co najważniejsze |
| **Użyj fabryk danych testowych** | Twórz programowo dane testowe; nie polegaj na danych początkowych |
| **Posprzątaj po testach** | Każdy test powinien pozostawić system w znanym stanie |
| **Unikaj testowania szczegółów interfejsu użytkownika** | Zachowanie testowe, a nie klasy CSS lub pozycje elementów |
| **Uruchom w CI** | Testy E2E muszą uruchamiać się automatycznie przy każdej zmianie |
---

## Rozwój oparty na testach (TDD)
Najpierw napisz test, a następnie napisz kod, który go zaliczy.
| Krok | Opis |
|------|------------|
| **1. Czerwony** | Napisz nieudany test opisujący pożądane zachowanie |
| **2. Zielony** | Napisz minimalny kod, aby test przeszedł pomyślnie |
| **3. Refaktor** | Wyczyść kod, zachowując zielone testy |
| Korzyści | Opis |
|--------|------------|
| **Opinie dotyczące projektu** | Testy zmuszają do przemyślenia interfejsów przed wdrożeniem |
| **Bezpieczeństwo regresyjne** | Każdy błąd przechodzi test; błąd nie może nigdy powrócić |
| **Dokumentacja** | Testy służą jako żywa dokumentacja oczekiwanego zachowania |
| **Pewność** | Wysoki zasięg testów umożliwia nieustraszoną refaktoryzację |
---

## Rozwój oparty na zachowaniu (BDD)
BDD rozszerza TDD pisząc testy w języku naturalnym, które opisują zachowanie z perspektywy użytkownika.
### Format „kiedy-wtedy”.
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Narzędzie | Język |
|------|--------------|
| **Ogórek** | Java, JavaScript, Ruby i inne |
| **Zachowuj się** | Pythona |
| **SpecFlow** | C# |
| **Jest** (z opisem/it) | JavaScript |
---

## Inne typy testów
| Wpisz | Co testuje | Narzędzia |
|------|------------------|------|
| **Wydajność/obciążenie** | Zachowanie systemu pod obciążeniem | k6, JMeter, Szarańcza, Gatling |
| **Bezpieczeństwo** | Luki i wektory ataków | OWASP ZAP, Burp Suite, Snyk |
| **Dostępność** | Zgodność z WCAG | topór, Latarnia Morska, pa11y |
| **Umowa** | Zgodność API między usługami | Pakt, wiosenny kontrakt na chmurę |
| **Mutacja** | Jakość samego zestawu testów | Stryker, mutmut, PIT |
| **Regresja wizualna** | Zmiany interfejsu użytkownika pomiędzy wersjami | Percy, Chromatyczny, BackstopJS |
| **Chaos** | Odporność systemu na awarie | Małpa Chaosu, Lakmus, Gremlin |
| **Dym** | Podstawowa funkcjonalność po wdrożeniu | Niestandardowe skrypty; kontrole stanu zdrowia |
| **Moczyć** | Zachowanie systemu przez dłuższy czas | Długotrwałe testy obciążeniowe |
---

## Organizacja testowa
| Wzór | Opis | Kiedy stosować |
|--------|------------|------------|
| **Wspólna lokalizacja** | Testy obok testowanego kodu (`src/utils.test.ts`) | Większość projektów; łatwo znaleźć |
| **Oddzielny katalog** | Testy w folderze`tests/`lub`__tests__/`| Duże projekty; wyraźna separacja |
| **Osprzęt testowy** | Udostępnione dane testowe w katalogu`fixtures/`| Gdy wiele testów potrzebuje tych samych danych |
| **Narzędzia testowe** | Udostępnione pomocniki w katalogu`test-utils/`| Gdy logika konfiguracji jest złożona |
---

## Zasięg kodu
| Metryczne | Co to mierzy | Ograniczenie |
|------------|-------|------------|
| **Zasięg linii** | Procent linii kodu wykonanych przez testy | Nie mierzy jakości twierdzeń |
| **Zasięg oddziału** | Procent wykorzystanych oddziałów (jeśli/inny) | Lepszy niż zasięg linii; nadal nie wyłapuje wszystkich błędów |
| **Zasięg ścieżki** | Procent wykorzystanych ścieżek wykonania | Najbardziej dokładny; wykładniczy w złożonym kodzie |
| **Wynik mutacji** | Procent mutacji wykrytych w testach | Najlepsza miara jakości testu |
**Cel**: 80% pokrycia linii to rozsądne ustawienie domyślne. Jednak zasięg jest wskazówką, a nie celem — 100% pokrycia przy słabych asercjach jest gorsze niż 70% pokrycia przy dokładnych testach.
---

## Ciągła integracja i testowanie
| Praktyka | Opis |
|--------------|------------|
| **Uruchom wszystkie testy jednostkowe przy każdym zatwierdzeniu** | Szybka informacja zwrotna; natychmiast łapie regresje |
| **Przeprowadź testy integracyjne na PR** | Wychwytuje problemy, które pomijają testy jednostkowe |
| **Uruchamiaj testy E2E co noc lub po połączeniu z głównym** | Powolny, ale dokładny |
| **Szybka porażka** | Zatrzymaj rurociąg w przypadku pierwszego niepowodzenia oszczędzania czasu |
| **Niestabilna polityka testowa** | Natychmiast poddaj kwarantannie lub usuń niestabilne testy; nigdy nie ignoruj ​​|
| **Test równoległy** | Uruchom testy równolegle, aby skrócić czas CI |
---

## Praktyczne wskazówki
- **Wyraźnie nazwij testy.**`test_calculates_tax_for_high_earner`mówi ci, co się zepsuło. `test_1`nic ci nie mówi.
- **Jedno stwierdzenie na test (jeśli jest to praktyczne).** Ułatwia diagnozowanie usterek.
- **Nie testuj szczegółów implementacji.** Testuj zachowanie. Jeśli dokonasz refaktoryzacji elementów wewnętrznych, testy nie powinny się zepsuć.
- **Unikaj testowania kodu stron trzecich.** Próbuj bibliotek zewnętrznych; przetestuj interakcję swojego kodu z nimi.
- **Testuj szybko.** Jeśli Twój zestaw testów zajmie 10 minut, programiści przestaną go uruchamiać. Optymalizuj bez przerwy.
- **Usuń martwe testy.** Testy, które zawsze przechodzą pomyślnie lub testują usunięty kod, są szumem.
- **Traktuj kod testowy jak kod produkcyjny.** Powinien być czytelny, łatwy w utrzymaniu i mieć dobrą strukturę.
---

## Streszczenie
Testowanie nie jest opcjonalne — w ten sposób tworzy się oprogramowanie, które się nie psuje. Piramida testowania prowadzi Cię do wielu szybkich testów jednostkowych, niektórych testów integracyjnych i kilku testów E2E. TDD i BDD zapewniają podejście strukturalne. Wyśmiewanie izoluje jednostki do testowania. Pokrycie kodu mierzy szerokość, ale nie głębokość. Najważniejsza zasada jest następująca: jeśli coś nie zostało przetestowane, oznacza to, że jest zepsute – po prostu jeszcze o tym nie wiesz.