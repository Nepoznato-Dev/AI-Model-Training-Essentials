# Języki kodowania

## Pythona

Python to interpretowany, dynamicznie typowany język programowania wysokiego poziomu ogólnego przeznaczenia. Podkreśla czytelność i używa znacznych wcięć jako ograniczników bloków.

### Podstawy składni

CODEBLOCK_0_END

### Funkcje i wskazówki dotyczące typów

CODEBLOCK_1_END

### Lista wyrażeń

CODEBLOCK_2_END

### Klasy i OOP

CODEBLOCK_3_END

### Typowe wzorce

- Użyj INLINECODE_0_END dla wejścia/wyjścia pliku.
- Preferuj ciągi f (INLINECODE_1_END) zamiast INLINECODE_2_END lub INLINECODE_3_END.
- Użyj INLINECODE_4_END w przypadku zajęć zawierających tylko dane.
- Użyj INLINECODE_5_END zamiast INLINECODE_6_END dla ścieżek plików.

### Oprzyrządowanie

- INLINECODE_7_END instaluje pakiety.
- INLINECODE_8_END tworzy środowisko wirtualne.
- INLINECODE_9_END zapisuje zależności.
- INLINECODE_10_END przywraca je.
- INLINECODE_11_END to nowoczesny standard konfiguracji projektu.

---

## JavaScript

JavaScript jest głównym językiem sieci. Działa w przeglądarkach i na serwerach poprzez Node.js. Jest dynamicznie wpisywany i oparty na prototypach.

### Nowoczesna składnia (ES6+)

CODEBLOCK_4_END

### Programowanie asynchroniczne

CODEBLOCK_5_END

### Metody tablicowe

CODEBLOCK_6_END

### Manipulacja DOM

CODEBLOCK_7_END

### Oprzyrządowanie

- INLINECODE_12_END inicjuje projekt.
- INLINECODE_13_END dodaje zależność.
- INLINECODE_14_END uruchamia skrypt zdefiniowany w INLINECODE_15_END .
- INLINECODE_16_END uruchamia skrypt w Node.js.

---

## Maszynopis

TypeScript to statycznie typowany nadzbiór kodu JavaScript, który kompiluje się do zwykłego kodu JavaScript. Dodaje adnotacje typów, interfejsy, typy generyczne i wyliczenia.

### Wpisz adnotacje

CODEBLOCK_8_END

### Interfejsy i typy

CODEBLOCK_9_END

### Ogólne

CODEBLOCK_10_END

### Klasy z modyfikatorami dostępu

CODEBLOCK_11_END

### Podstawowe informacje o pliku tsconfig.json

CODEBLOCK_12_END

### Oprzyrządowanie

- INLINECODE_17_END instaluje kompilator.
- INLINECODE_18_END kompiluje projekt.
- INLINECODE_19_END bezpośrednio uruchamia TypeScript.

---

## Rdza

Rust to język programowania systemów skupiający się na bezpieczeństwie, szybkości i współbieżności. Zapobiega błędom związanym z bezpieczeństwem pamięci w czasie kompilacji poprzez swój system własności.

### Własność i pożyczanie

Każda wartość w Rust ma dokładnie jednego właściciela. Gdy właściciel wyjdzie poza zakres, wartość zostanie usunięta. Wypożyczanie umożliwia referencje bez przeniesienia własności.

CODEBLOCK_13_END

Zmienne zapożyczenia (INLINECODE_20_END) wymagają, aby w tym samym czasie nie istniały żadne inne zapożyczenia.

### Całe życie

Okresy istnienia zapewniają, że referencje nie przetrwają dłużej niż dane, na które wskazują.

CODEBLOCK_14_END

### Wyliczenia i dopasowywanie wzorców

CODEBLOCK_15_END

### Obsługa błędów

CODEBLOCK_16_END

Operator INLINECODE_21_END automatycznie propaguje błędy wewnątrz funkcji zwracających INLINECODE_22_END.

### Oprzyrządowanie (ładunek)

- INLINECODE_23_END tworzy nowy projekt.
- INLINECODE_24_END się kompiluje.
- INLINECODE_25_END kompiluje i uruchamia.
- INLINECODE_26_END uruchamia testy.
- INLINECODE_27_END dodaje zależność do INLINECODE_28_END .
- INLINECODE_29_END formatuje kod. INLINECODE_30_END lint.

---

## Iść

Go (Golang) to skompilowany język ze statycznym typem, zaprojektowany z myślą o prostocie i wysokiej wydajności programów współbieżnych.

### Podstawy

CODEBLOCK_17_END

### Funkcje i wiele zwracanych wartości

CODEBLOCK_18_END

### Interfejsy

CODEBLOCK_19_END

Spełnia go każdy typ, który implementuje wszystkie metody interfejsu — nie jest wymagana żadna jawna deklaracja.

### Goroutines i kanały

CODEBLOCK_20_END

### Odłóż

CODEBLOCK_21_END

### Oprzyrządowanie

- INLINECODE_31_END inicjuje moduł.
- INLINECODE_32_END pobiera zależności.
- INLINECODE_33_END się kompiluje.
- INLINECODE_34_END uruchamia testy.
- INLINECODE_35_END formatuje kod.
- INLINECODE_36_END sprawdza typowe błędy.

---

## C i C++

C jest skompilowanym językiem proceduralnym niskiego poziomu. C++ rozszerza C o klasy, szablony i standardową bibliotekę szablonów (STL).

### Podstawy języka C

CODEBLOCK_22_END

### Wskazówki

Wskaźnik przechowuje adres pamięci innej zmiennej. INLINECODE_37_END usuwa odniesienie do tego; INLINECODE_38_END pobiera adres.

CODEBLOCK_23_END

### Klasy C++ i RAII

CODEBLOCK_24_END

RAII (Resource Acquisition Is Inicjalizacja) wiąże czasy życia zasobów z okresami istnienia obiektów, zapewniając, że czyszczenie w destruktorach odbywa się automatycznie.

### Kontenery STL

CODEBLOCK_25_END

### Najważniejsze cechy współczesnego C++ (C++17 / C++20).

- Odliczenie typu INLINECODE_39_END.
- Pętle INLINECODE_40_END oparte na zakresie: INLINECODE_41_END .
- Inteligentne wskaźniki: INLINECODE_42_END, INLINECODE_43_END — unikaj surowych INLINECODE_44_END / INLINECODE_45_END.
- Powiązania strukturalne: INLINECODE_46_END .
- INLINECODE_47_END, INLINECODE_48_END, INLINECODE_49_END.

### Kompilacja

- INLINECODE_50_END kompiluje C.
- INLINECODE_51_END kompiluje C++.
- INLINECODE_52_END automatyzuje kompilacje wielu plików za pomocą INLINECODE_53_END .
- INLINECODE_54_END to standardowy generator systemu kompilacji dla większych projektów.

---

## Szybki

Swift to nowoczesny język programowania ze statycznym typem opracowany przez firmę Apple dla systemów iOS, macOS, watchOS i tvOS. Jest również dostępny na Linuksie.

### Podstawy

CODEBLOCK_26_END

### Opcjonalne

Opcjonalny (INLINECODE_55_END) reprezentuje wartość, która może występować lub nie.

CODEBLOCK_27_END

### Funkcje i zamknięcia

CODEBLOCK_28_END

### Klasy i struktury

Swift ma zarówno klasy (typy referencyjne), jak i struktury (typy wartości). Preferuj struktury dla prostych modeli danych.

CODEBLOCK_29_END

### Protokoły

CODEBLOCK_30_END

### Kodowalne (kodowanie/dekodowanie JSON)

CODEBLOCK_31_END

### Podstawy SwiftUI

CODEBLOCK_32_END

### Oprzyrządowanie

- INLINECODE_56_END kompiluje projekt Swift Package Manager.
- INLINECODE_57_END uruchamia projekt.
- INLINECODE_58_END uruchamia testy.
- INLINECODE_59_END tworzy nowy projekt wykonywalny.
- Xcode jest podstawowym IDE do programowania platformy Apple.

---

## Podstawy kodowania (niezależnie od języka)

### Przepływ pracy związany z rozwiązywaniem problemów

1. Zdefiniuj dane wejściowe, wyjściowe i ograniczenia przed napisaniem kodu.
2. Podziel zadanie na mniejsze podproblemy.
3. Zacznij od prostego, prawidłowego rozwiązania, a następnie zoptymalizuj je, jeśli zajdzie taka potrzeba.
4. Sprawdź poprawność za pomocą testów, przypadków brzegowych i realistycznych danych wejściowych.

### Podstawowe struktury danych

- **Array / List**: uporządkowana kolekcja z szybkimi indeksowanymi odczytami.
- **Mapa skrótów / Słownik**: magazyn klucz-wartość ze średnim wyszukiwaniem O(1).
- **Set**: unikalne wartości, przydatne przy sprawdzaniu członkostwa.
- **Stos**: LIFO (ostatni na wejściu, pierwszy na wyjściu), powszechny w analizowaniu i rekurencji.
- **Kolejka**: FIFO (pierwsze weszło, pierwsze wyszło), przydatne do planowania i BFS.
- **Drzewo / Wykres**: relacje hierarchiczne i sieciowe.

### Złożoność algorytmiczna (duże O)

- Duże O opisuje, jak rośnie czas wykonania lub pamięć wraz z rozmiarem danych wejściowych.
- Typowe koszty:
  - O(1): wyszukiwanie w czasie stałym (np. dostęp do mapy mieszającej).
  - O(log n): wyszukiwanie binarne.
  - O(n): dane z pojedynczym przejściem.
  - O(n log n): efektywne sortowanie.
  - O(n²): zagnieżdżone pętle na wejściach o podobnym rozmiarze.
- Preferuj przejrzysty, łatwy w utrzymaniu kod, chyba że profilowanie wykryje wąskie gardło.

### Zasady debugowania

- Najpierw niezawodnie odtwórz błąd.
- Zminimalizuj przypadek niepowodzenia, aby wyizolować przyczynę.
- Sprawdź dzienniki, dane wejściowe i założenia.
- Zmieniaj jedną zmienną na raz podczas testowania.
- Dodaj testy regresyjne, aby ten sam błąd nie powrócił.

### Piramida testowania

- **Testy jednostkowe**: szybkie, ukierunkowane sprawdzenie małych jednostek logicznych.
- **Testy integracyjne**: weryfikują interakcje pomiędzy modułami/usługami.
- **Kompleksowe testy**: weryfikuj przepływy użytkowników w realistycznych środowiskach.
- Zrównoważony pakiet ma wiele testów jednostkowych i mniej powolnych testów kompleksowych.

### Praktyki dotyczące jakości kodu

- Używaj znaczących nazw i małych funkcji.
- Preferuj czyste funkcje (mniej skutków ubocznych), jeśli jest to praktyczne.
- Zachowaj spójność modułów i przejrzystość interfejsów.
- Aby zachować spójność, użyj lintersów/formatów.
- Przejrzyj kod pod kątem poprawności, przejrzystości i bezpieczeństwa.

### Podstawy bezpieczeństwa dla programistów

- Sprawdź i oczyść dane wejściowe z zewnątrz.
- Używaj sparametryzowanych zapytań, aby zapobiec wstrzykiwaniu SQL.
- Przechowuj hasła za pomocą silnych algorytmów mieszania (np. Argon2, bcrypt).
- Unikaj osadzania sekretów w kodzie źródłowym.
- Zastosuj najmniejsze uprawnienia do poświadczeń i usług.