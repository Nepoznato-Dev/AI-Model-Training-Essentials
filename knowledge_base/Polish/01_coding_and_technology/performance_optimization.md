---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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
tags: [performance, optimization, coding-and-technology]
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
# Optymalizacja wydajności
Optymalizacja wydajności to praktyka polegająca na przyspieszaniu oprogramowania — skracaniu czasu reakcji, zwiększaniu przepustowości, zmniejszaniu zużycia pamięci i eliminowaniu wąskich gardeł. Jest to jedna z najbardziej wpływowych umiejętności, jakie może posiadać programista, ponieważ wolne oprogramowanie powoduje utratę użytkowników, marnowanie zasobów i frustrację wszystkich. Ale jest to również jeden z najczęściej popełnianych błędów, ponieważ programiści optymalizują niewłaściwe rzeczy w oparciu o intuicję, a nie dowody.
---

## Złota zasada
> **Najpierw mierz, potem optymalizuj.** Nigdy nie optymalizuj w oparciu o założenia. Sprofiluj kod, znajdź faktyczne wąskie gardło i napraw je.
| Antywzorzec | Dlaczego jest źle |
|------------|------------|
| **Przedwczesna optymalizacja** | Spędzanie czasu na przyspieszaniu kodu, który nie jest powolny |
| **Optymalizacja bez pomiaru** | Naprawienie niewłaściwego wąskiego gardła; nie ma możliwości sprawdzenia poprawy |
| **Poświęcenie czytelności na rzecz szybkości** | Nieczytelny kod kosztuje więcej niż wzrost wydajności |
| **Buforowanie wszystkiego** | Nieaktualne dane, wzdęcia pamięci, złożoność |
---

## Profilowanie
Zanim będziesz mógł zrobić coś szybciej, musisz wiedzieć *gdzie* spędzasz czas.
| Typ narzędzia | Co to mierzy | Przykłady |
|----------|--------------------------------|---------|
| **Profil procesora** | Które funkcje zużywają najwięcej czasu procesora | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Profil pamięci** | Alokacja pamięci i wycieki | tracemalloc (Python), Valgrind, ścieżka sterty |
| **Profil we/wy** | Wąskie gardła we/wy dysków i sieci | iotop, strace, Wireshark |
| **APM (monitorowanie wydajności aplikacji)** | Termin realizacji żądania od początku do końca | Nowa relikt, Datadog, Jaeger |
| **Narzędzia deweloperskie przeglądarki** | Renderowanie frontendu, wykonanie JavaScript, sieć | Chrome DevTools, Firefox Profiler |
### Proces profilowania
| Krok | Opis |
|------|------------|
| 1. Zidentyfikuj powolną operację | Użytkownicy zgłaszają powolne ładowanie strony; monitorowanie wykazuje duże opóźnienia |
| 2. Profiluj pełną ścieżkę | Znajdź, który komponent zajmuje najwięcej czasu |
| 3. Przejdź do szczegółów | Sprofiluj ten konkretny komponent, aby znaleźć gorącą funkcję |
| 4. Napraw wąskie gardło | Zastosuj odpowiednią optymalizację |
| 5. Zmierz ponownie | Zweryfikuj poprawę; sprawdź regresje |
---

## Optymalizacja algorytmiczna
Największy wzrost wydajności wynika z wyboru lepszych algorytmów, a nie z mikrooptymalizacji.
| Zmień | Poprawa |
|------------|------------|
| Przeszukiwanie liniowe O(n) → Przeszukiwanie tablicy mieszającej O(1) | 100x+ dla dużych zbiorów danych |
| Zagnieżdżona pętla O(n²) → Sortowanie + wyszukiwanie binarne O(n log n) | Rzędy wielkości dla dużego n |
| Powtarzane obliczenia → Zapamiętywanie / buforowanie | Eliminuje zbędną pracę |
| Łączenie ciągów w pętli → Konstruktor / łączenie | Pozwala uniknąć kopiowania ciągów kwadratowych |
| Dane nieposortowane → Dane posortowane przy wyszukiwaniu binarnym | O(log n) zamiast O(n) na wyszukiwanie |
---

## Strategie buforowania
Buforowanie przechowuje obliczone wyniki, więc nie trzeba ich ponownie obliczać.
| Typ pamięci podręcznej | Lokalizacja | Prędkość | Całe życie |
|----------|------|-------|--------------|
| **Pamięć podręczna procesora** | L1/L2/L3 | ~1 ns | Automatyczny |
| **W pamięci** | RAM aplikacji (dykt, HashMap) | ~100 ns | Do czasu oczyszczenia lub eksmisji |
| **Rozproszona pamięć podręczna** | Redis, Memcached | ~1 ms | Konfigurowalny TTL |
| **CDN** | Serwery brzegowe na całym świecie | ~10-50 ms | Konfigurowalny TTL |
| **Pamięć podręczna przeglądarki** | Przeglądarka użytkownika | ~1 ms | Nagłówki pamięci podręcznej HTTP |
| **Pamięć podręczna zapytań do bazy danych** | Poziom bazy danych lub ORM | ~1-10 ms | Do czasu zmiany danych |
### Wzorce buforowania
| Wzór | Opis | Kiedy stosować |
|--------|------------|------------|
| **Odłóż na bok** | Aplikacja sprawdza pamięć podręczną; ładuje z DB w przypadku braku; przechowuje w pamięci podręcznej | Najczęściej; proste |
| **Przepisanie** | Zapisuj jednocześnie do pamięci podręcznej i bazy danych | Kiedy czyta >> pisze; ważna konsekwencja |
| **Zapis z tyłu** | Zapisz w pamięci podręcznej; asynchronicznie zapisuj do DB | Wysoka przepustowość zapisu; pewne ryzyko utraty danych |
| **TTL (czas życia)** | Wpisy w pamięci podręcznej wygasają po określonym czasie | Kiedy dane zmieniają się okresowo |
| **Unieważnienie** | Jawnie usuń nieaktualne wpisy pamięci podręcznej | Kiedy wiesz dokładnie, kiedy dane się zmieniają |
### Unieważnienie pamięci podręcznej
Dwa najtrudniejsze problemy w informatyce: unieważnianie pamięci podręcznej, nadawanie nazw i błędy o jeden.
| Strategia | Opis |
|--------------|------------|
| **Na podstawie TTL** | Wpisy wygasają po N sekundach; proste, ale może obsługiwać nieaktualne dane |
| **Sterowane zdarzeniami** | Unieważnij w przypadku zmiany danych; bardziej złożone, ale dokładne |
| **Oparte na wersji** | Dołącz numer wersji; przyrost zmian |
| **Oparte na tagach** | Oznacz powiązane wpisy pamięci podręcznej; unieważnia wszystkie wpisy ze znacznikiem |
---

## Optymalizacja bazy danych
Bazy danych są często największym wąskim gardłem w aplikacjach internetowych.
| Technika | Opis | Wpływ |
|----------|------------|-------|
| **Indeksowanie** | Dodaj indeksy do kolumn używanych w WHERE, DOŁĄCZ, ORDER BY | 10-1000x szybsze zapytania |
| **Optymalizacja zapytań** | Unikaj WYBIERZ *; użyj EXPLAIN do analizy zapytań | Zmniejsz liczbę wejść/wyjść |
| **Łączenie połączeń** | Wykorzystuj ponownie połączenia z bazą danych zamiast tworzyć nowe | Wyeliminuj obciążenie połączenia |
| **Przeczytaj repliki** | Kieruj zapytania odczytu do baz danych replik | Rozłóż obciążenie odczytu |
| **Podział** | Podziel duże tabele na mniejsze partycje | Szybsze zapytania na dużych zbiorach danych |
| **Denormalizacja** | Dodaj nadmiarowe dane, aby uniknąć złączeń | Szybsze odczyty; wolniej pisze |
| **Zmaterializowane widoki** | Wstępnie obliczone wyniki zapytania | Natychmiastowe złożone zapytania |
| **N+1 zapobieganie** | Użyj JOIN, szybkiego ładowania lub zapytań wsadowych | Wyeliminuj tysiące zapytań |
---

## Współbieżność i równoległość
| Koncepcja | Opis | Kiedy stosować |
|--------|------------|------------|
| **Gwintowanie** | Wiele wątków w jednym procesie | Zadania związane z we/wy (sieć, dysk) |
| **Przetwarzanie wieloprocesowe** | Wiele procesów (omija GIL w Pythonie) | Zadania związane z procesorem |
| **Asynchronizacja/oczekiwanie** | Wielozadaniowość kooperacyjna; pojedynczy wątek | We/wy o wysokiej współbieżności (serwery sieciowe) |
| **Obliczenia GPU** | Tysiące równoległych rdzeni | Operacje na macierzach; przetwarzanie obrazu; ML |
### Asynchronizacja a wątkowanie
| Aspekt | Asynchronizacja/Oczekiwanie | Gwintowanie |
|------------|------------|---------------|
| **Modelka** | Spółdzielnia (kontrola wydajności zadań) | Wywłaszczający (system operacyjny przełącza wątki) |
| **Nad głową** | Bardzo niski (bez przełączania kontekstu) | Wyższe (tworzenie wątku, przełączanie kontekstu) |
| **Złożoność** | Prostsze rozumowanie (pojedynczy wątek) | Warunki wyścigu, impas, blokady |
| **Najlepsze dla** | Wiele jednoczesnych operacji we/wy | Blokowanie operacji, których nie można wykonać asynchronicznie |
| **Ograniczenie** | Nie można używać kodu powiązanego z procesorem bez blokowania | GIL w Pythonie ogranicza prawdziwą równoległość |
---

## Wydajność interfejsu
| Technika | Opis | Wpływ |
|----------|------------|-------|
| **Minifikacja** | Usuń spacje i skróć nazwy zmiennych | 20-40% mniejsze pliki |
| **Łączenie** | Połącz wiele plików w mniejszą liczbę żądań | Mniej żądań HTTP |
| **Podział kodu** | Załaduj tylko kod potrzebny dla bieżącej strony | Szybsze ładowanie początkowe |
| **Leniwe ładowanie** | Załaduj obrazy i komponenty, gdy są potrzebne | Szybsze renderowanie początkowe |
| **Drzewo się trzęsie** | Usuń nieużywany kod z pakietów | Mniejsze pakiety |
| **Optymalizacja obrazu** | Użyj WebP/AVIF; responsywne obrazy; leniwe ładowanie | 50-80% mniejsze obrazy |
| **CDN** | Obsługuj zasoby statyczne z serwerów brzegowych | Mniejsze opóźnienia na całym świecie |
| **HTTP/2 i HTTP/3** | Multipleksowanie; kompresja nagłówka; 0-RTT | Szybszy narzut protokołu |
| **Pracownicy usług** | Zasoby w pamięci podręcznej do użytku offline; powiadomienia push | Szybsze powtarzające się wizyty |
---

## Optymalizacja pamięci
| Technika | Opis |
|---------------|------------|
| **Łączenie obiektów** | Wykorzystuj obiekty ponownie zamiast tworzyć nowe |
| **Przesyłanie strumieniowe** | Przetwarzaj dane fragmentami zamiast ładować wszystko do pamięci |
| **Generatory / iteratory** | Uzyskuj wartości pojedynczo, zamiast tworzyć listy |
| **Pliki mapowane w pamięci** | Uzyskaj dostęp do dużych plików bez ładowania ich w całości |
| **Trening zbierania śmieci** | Dostosuj parametry GC do swojego obciążenia |
| **Wybór struktury danych** | Używaj tablic zamiast połączonych list dla lokalizacji pamięci podręcznej; użyj zbiorów do testowania członkostwa |
---

## Optymalizacja sieci
| Technika | Opis |
|---------------|------------|
| **Kompresja** | gzip, brotli dla odpowiedzi HTTP |
| **Ponowne wykorzystanie połączenia** | Utrzymuj połączenia; Multipleksowanie HTTP/2 |
| **Zażądaj grupowania** | Połącz wiele wywołań API w jedno |
| **Paginacja** | Ładuj dane na stronach zamiast wszystkich na raz |
| **Ucisk w spoczynku** | Kompresuj dane w bazach danych i pamięciach podręcznych |
| **Wybór protokołu** | gRPC (binarny, wydajny) vs REST (czytelny dla człowieka) |
---

## Monitorowanie i ostrzeganie
| Metryczne | Co ci to mówi |
|------------|--------------------------------|
| **Opóźnienie P50 / P95 / P99** | Czas reakcji w różnych percentylach |
| **Przepustowość** | Żądania na sekundę |
| **Współczynnik błędów** | Procent nieudanych żądań |
| **Wykorzystanie procesora** | Ile mocy obliczeniowej jest wykorzystywane |
| **Wykorzystanie pamięci** | Zużycie pamięci RAM; zbliżanie się do granic? |
| **Czas zapytania do bazy danych** | Powolne zapytania wymagające optymalizacji |
---

## Streszczenie
Optymalizacja wydajności to systematyczny proces: zmierz, zidentyfikuj wąskie gardło, napraw je, zmierz ponownie. Największe zwycięstwa wynikają z ulepszeń algorytmicznych i eliminacji niepotrzebnej pracy, a nie z mikrooptymalizacji. Buforowanie, indeksowanie baz danych i współbieżność to najpotężniejsze narzędzia. Wydajność frontonu zależy od minimalizacji rozmiaru ładunku i podróży w obie strony. A najważniejsza zasada jest zawsze taka sama: nie zgaduj – profil.