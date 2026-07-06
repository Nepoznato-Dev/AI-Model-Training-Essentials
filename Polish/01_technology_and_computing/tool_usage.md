# Użycie narzędzia

## Git — Kontrola wersji

Git to rozproszony system kontroli wersji. Każdy programista ma pełną kopię historii repozytorium na swoim komputerze lokalnym.

### Podstawowy przepływ pracy

CODEBLOCK_0_END

### Rozgałęzianie

CODEBLOCK_1_END

### Łączenie i zmiana bazy

CODEBLOCK_2_END

### Przepływ pracy z żądaniem ściągnięcia (PR).

1. Utwórz gałąź funkcji z INLINECODE_0_END .
2. Dokonaj zatwierdzeń w gałęzi funkcji.
3. Naciśnij gałąź: INLINECODE_1_END .
4. Otwórz żądanie ściągnięcia w GitHub/GitLab.
5. Informacje zwrotne dotyczące przeglądu kodu adresu z dodatkowymi zatwierdzeniami.
6. Po zatwierdzeniu połącz PR.

### Cofanie zmian

CODEBLOCK_3_END

---

## Menedżerowie pakietów

### pips (Python)

CODEBLOCK_4_END

Zawsze pracuj w środowisku wirtualnym, aby izolować zależności projektu.

### npm (Node.js / JavaScript)

CODEBLOCK_5_END

INLINECODE_2_END rejestruje dokładne wersje; przekaż to do kontroli źródła.

### Ładunek (rdza)

CODEBLOCK_6_END

### Moduły Przejdź (Przejdź)

CODEBLOCK_7_END

### apt (Debian/Ubuntu Linux)

CODEBLOCK_8_END

---

## Podstawy wiersza poleceń

### Nawigacja

CODEBLOCK_9_END

### Przetwarzanie tekstu

CODEBLOCK_10_END

### Potoki i przekierowania

CODEBLOCK_11_END

### Sieć i transfer plików

CODEBLOCK_12_END

### Uprawnienia

CODEBLOCK_13_END

### Zarządzanie procesami

CODEBLOCK_14_END

---

## Redaktorzy i IDE

### Kod VS

VS Code to lekki, wieloplatformowy edytor kodu z bogatym ekosystemem rozszerzeń.

- Otwórz folder: INLINECODE_3_END lub INLINECODE_4_END w terminalu.
- Paleta poleceń: INLINECODE_5_END (macOS: INLINECODE_6_END).
- Zintegrowany terminal: INLINECODE_7_END INLINECODE_8_END .
- Wiele kursorów: INLINECODE_9_END, aby umieścić dodatkowe kursory.
- Przejdź do definicji: INLINECODE_10_END .
- Zmień nazwę symbolu: INLINECODE_11_END .
- Formatuj dokument: INLINECODE_12_END .
- Rozszerzenia: zainstaluj obsługę języków (Python, Rust, Go itp.), linters i formatery z panelu Rozszerzenia (INLINECODE_13_END).
- INLINECODE_14_END (użytkownik lub obszar roboczy) kontroluje zachowanie edytora.
- INLINECODE_15_END konfiguruje debuger.

### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Inteligentne uzupełnianie i refaktoryzacja kodu to podstawowe funkcje.
- Konfiguracje uruchamiania/debugowania umożliwiają uruchamianie i debugowanie programów jednym kliknięciem.
- Wbudowana obsługa Git w menu VCS.
- INLINECODE_16_END otwiera okno dialogowe Szukaj wszędzie.
- INLINECODE_17_END (macOS: INLINECODE_18_END) ponownie formatuje kod.
- Wtyczki rozszerzają obsługę języków i dodają narzędzia.

### Wskazówki dotyczące terminala

- Użyj uzupełniania tabulatorów, aby szybko kończyć nazwy plików i polecenia.
- Naciśnij INLINECODE_19_END, aby interaktywnie przeszukać historię poleceń.
- INLINECODE_20_END tworzy skrót — dodaj go do INLINECODE_21_END lub INLINECODE_22_END.
- Użyj INLINECODE_23_END lub INLINECODE_24_END, aby utrzymać sesje przy życiu po rozłączeniu ze zdalnym serwerem.
- INLINECODE_25_END pokazuje stronę podręcznika dla dowolnego wbudowanego polecenia.

---

## Doker

Docker pakuje aplikacje i ich zależności do przenośnych kontenerów.

### Podstawowe pojęcia

- **Obraz**: szablon tylko do odczytu zbudowany na podstawie INLINECODE_26_END .
- **Kontener**: działająca instancja obrazu.
- **Rejestr**: usługa przechowywania i dystrybucji obrazów (Docker Hub, GHCR).
- **Wolumin**: pamięć trwała, która przetrwa dłużej niż kontener.

### Typowe polecenia

CODEBLOCK_15_END

### Przykład pliku Dockerfile

CODEBLOCK_16_END

### Tworzenie Dockera

Docker Compose zarządza aplikacjami wielokontenerowymi za pomocą pliku INLINECODE_27_END.

CODEBLOCK_17_END

CODEBLOCK_18_END