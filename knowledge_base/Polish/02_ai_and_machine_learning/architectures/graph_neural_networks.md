<!--
---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
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
tags: [graph, neural, networks, ai-and-machine-learning]
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
# Wykres sieci neuronowych
Grafowe sieci neuronowe (GNN) to sieci neuronowe zaprojektowane do działania na danych o strukturze grafowej — sieciach węzłów połączonych krawędziami. Podczas gdy tradycyjne sieci neuronowe działają na siatkach (obrazach) lub sekwencjach (tekst), sieci GNN obsługują dowolne struktury relacyjne: sieci społecznościowe, wykresy molekularne, wykresy wiedzy, sieci drogowe, wykresy rekomendacji i inne. Stały się niezbędne w odkrywaniu leków, wykrywaniu oszustw, systemach rekomendacji i w każdej dziedzinie, w której liczą się relacje między podmiotami.
---

## Co to jest wykres?
| Składnik | Opis | Przykład |
|---------------|------------|--------|
| **Węzeł (wierzchołek)** | Podmiot | Osoba, atom cząsteczki, miasto |
| **Krawędź** | Relacja pomiędzy dwoma węzłami | Przyjaźń, więź chemiczna, droga |
| **Waga krawędzi** | Siła lub rodzaj związku | Odległość, podobieństwo, pojemność |
| **Funkcje węzła** | Atrybuty każdego węzła | Wiek, liczba atomowa, populacja |
| **Funkcje krawędzi** | Atrybuty każdej krawędzi | Rodzaj związku, odległość |
| **Macierz sąsiedztwa** | Macierz A, gdzie A[i][j] = 1, jeśli węzły i oraz j są połączone | Koduje strukturę wykresu |
### Rodzaje wykresów
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Nieskierowany** | Krawędzie nie mają kierunku | Sieć przyjaźni |
| **Reżyseria** | Krawędzie mają kierunek (A → B ≠ B → A) | Obserwujący na Twitterze |
| **Ważona** | Krawędzie mają wartości liczbowe | Sieć drogowa z odległościami |
| **Niejednorodny** | Wiele typów węzłów i krawędzi | Wykres akademicki (artykuły, autorzy, miejsca) |
| **Dynamiczny** | Struktura wykresu zmienia się w czasie | Sieć społecznościowa ewoluuje w czasie |
| **Dwustronny** | Dwa typy węzłów; krawędzie tylko pomiędzy typami | Wykres rekomendacji elementów użytkownika |
---

## Dlaczego nie zwykłe sieci neuronowe?
| Podejście | Dlaczego to się nie udaje |
|---------|------------|
| **Sieć przekazująca** | Wymaga danych wejściowych o stałym rozmiarze; wykresy różnią się wielkością i strukturą |
| **CNN** | Zakłada strukturę siatki; wykresy nie mają regularnej siatki |
| **RNN/Transformator** | Zakłada kolejność sekwencyjną; wykresy nie mają naturalnego porządku |
Sieci GNN rozwiązują ten problem, działając bezpośrednio na strukturze grafu, przetwarzając każdy węzeł w kontekście jego sąsiadów.
---

## Podstawowe architektury GNN
### Struktura przekazywania wiadomości
Większość sieci GNN działa według tego samego schematu: każdy węzeł zbiera informacje od swoich sąsiadów, łączy je i aktualizuje swoją własną reprezentację.
| Krok | Opis |
|------|------------|
| **1. Wiadomość** | Każdy węzeł wysyła wiadomość do swoich sąsiadów (w oparciu o swoje aktualne funkcje) |
| **2. Agregat** | Każdy węzeł zbiera i łączy wiadomości od wszystkich sąsiadów
| **3. Aktualizacja** | Każdy węzeł aktualizuje swoją własną reprezentację za pomocą zagregowanego komunikatu |
| **4. Powtórz** | Zrób to dla K warstw → każdy węzeł przechwytuje informacje z K przeskoków |
### Kluczowe modele GNN
| Modelka | Metoda agregacji | Kluczowa innowacja |
|-------|----------------------|----------------|
| **GCN** (Grafowa sieć konwolucyjna) | Średnia cech sąsiadujących | Prosty; skuteczny; motywacja widmowa |
| **WykresSAGE** | Próbka i agregat; można używać średniej, LSTM lub łączenia | Indukcyjny (obsługuje niewidoczne węzły); skalowalne |
| **GAT** (sieć uwagi graficznej) | Agregacja sąsiadów ważona uwagą | Dowiaduje się, którzy sąsiedzi są najważniejsi |
| **GIN** (Sieć izomorfizmu grafów) | Suma cech sąsiadujących | Maksymalnie wyrazisty; potrafi rozróżnić dowolne wykresy rozróżnialne testem WL |
| **MPNN** (sieć neuronowa przekazująca wiadomości) | Ogólne ramy przekazywania wiadomości | Ujednolica wiele wariantów GNN |
### Jak działa GCN (krok po kroku)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Po K warstw reprezentacja każdego węzła koduje informacje z K przeskoków na wykresie.
---

## Zadania na poziomie wykresu
| Zadanie | Opis | Przykład |
|------|------------|--------|
| **Klasyfikacja węzłów** | Przewiduj etykietę każdego węzła | Klasyfikuj użytkowników jako boty lub ludzi |
| **Przewidywanie linków** | Przewiduj, czy krawędź istnieje (lub będzie istnieć) | Przewiduj brakujące relacje; polecam połączenia |
| **Klasyfikacja wykresu** | Przewiduj etykietę dla całego wykresu | Klasyfikuj cząsteczki jako toksyczne i nietoksyczne |
| **Wykrywanie społeczności** | Znajdź skupiska gęsto połączonych węzłów | Identyfikacja grup społecznych |
| **Generowanie wykresu** | Generuj nowe wykresy o pożądanych właściwościach | Zaprojektuj nowe cząsteczki |
---

## Aplikacje
### Odkrywanie leków i przewidywanie właściwości molekularnych
| Zadanie | Jak sieci GNN pomagają |
|------|------------------|
| **Przewidywanie właściwości molekularnych** | Przedstaw cząsteczki jako wykresy (atomy=węzły, wiązania=krawędzie); przewidzieć toksyczność, rozpuszczalność, powinowactwo wiązania |
| **Interakcja leków** | Modeluj leki i cele w formie wykresu; przewidzieć niekorzystne interakcje |
| **Projekt leku od nowa** | Generuj nowe wykresy molekularne o pożądanych właściwościach |
### Systemy rekomendacji
| Podejście | Opis |
|---------|------------|
| **Wykres pozycji użytkownika** | Użytkownicy i elementy to węzły; zakupy/wyświetlenia to przewaga |
| **Wspólne filtrowanie oparte na wykresach** | GNN propagują preferencje poprzez graf |
| **Zalecenia dotyczące wykresów wiedzy** | Połącz preferencje użytkownika z wiedzą o przedmiotach (gatunki, aktorzy, reżyserzy) |
### Wykrywanie oszustw
| Aplikacja | Struktura wykresu |
|------------|----------------|
| **Oszustwo finansowe** | Transakcje tworzą wykres; fałszywe wzorce pojawiają się jako struktury podgrafów |
| **Oszustwo ubezpieczeniowe** | Wnioskodawcy, dostawcy i zasady tworzą wykres; wykryto kręgi oszustów |
| **Przejęcia kont** | Wzorce logowania tworzą wykres; anomalne połączenia sygnalizują kompromis |
### Wykresy wiedzy
| Zadanie | Opis |
|------|------------|
| **Przewidywanie linków** | Przewiduj brakujące fakty (np. „Paryż jest stolicą?”) |
| **Uchwała podmiotu** | Ustal, czy dwie wzmianki odnoszą się do tego samego podmiotu |
| **Odpowiedź na pytanie** | Nawiguj po wykresie, aby znaleźć odpowiedzi |
---

## Zaawansowane koncepcje GNN
### Nadmierne wygładzenie
| Problem | Opis | Rozwiązanie |
|-------------|------------|---------|
| **Nadmierne wygładzenie** | Po wielu warstwach wszystkie reprezentacje węzłów stają się podobne | Ogranicz głębokość (2-4 warstwy); użyj pozostałych połączeń; użyj wiedzy o skakaniu |
### Nadmierne zgniatanie
| Problem | Opis | Rozwiązanie |
|-------------|------------|---------|
| **Nadmierne zgniatanie** | Informacje z odległych węzłów są kompresowane do wektorów o stałym rozmiarze | Użyj transformatorów graficznych; łączenie hierarchiczne |
### Transformatory graficzne
| Modelka | Kluczowa funkcja |
|-------|------------|
| **Transformator wykresu** | Zastosuj standardową uwagę Transformatora do wszystkich par węzłów |
| **GPS** (system podpowiedzi graficznych) | Połącz lokalne warstwy GNN z globalnymi warstwami Transformatora |
| **Graforer** | Dodaj kodowanie pozycyjne w oparciu o strukturę wykresu |
### Heterogeniczne sieci grafowe
| Modelka | Opis |
|-------|------------|
| **R-GCN** | Relacyjny GCN; różne macierze wag dla różnych typów krawędzi |
| **HAN** | Heterogeniczna sieć uwagi; uwaga na różne typy węzłów i krawędzi |
| **HetGNN** | Sieć neuronowa o grafach heterogenicznych; obsługuje wiele typów węzłów |
---

## Skalowalność
| Wyzwanie | Rozwiązanie |
|----------|----------|
| **Duże wykresy** (miliony węzłów) | Szkolenia mini-partyjne; próbkowanie sąsiada |
| **Pamięć** | Podział wykresów na procesory graficzne |
| **Prędkość** | Rzadkie operacje na macierzach; biblioteki specjalistyczne |
### Strategie próbkowania
| Strategia | Opis |
|---------|------------|
| **Próbkowanie węzłów** | Próbka podzbioru węzłów i ich otoczenia K-hop |
| **Próbkowanie krawędzi** | Przykładowe krawędzie i węzły, które łączą |
| **Próbkowanie klastrów** | Podziel graf na grupy; pociąg na klastrach |
| **Próbkowanie losowego spaceru** | Przykładowe węzły poprzez losowe spacery z węzłów docelowych |
---

## Narzędzia i struktury
| Narzędzie | Cel |
|------|-------------|
| **Geometria PyTorch (PyG)** | Najpopularniejsza biblioteka GNN; bogaty zestaw modeli i zbiorów danych |
| **DGL** (Biblioteka głębokich wykresów) | Niezależny od frameworka; obsługuje PyTorch, TensorFlow, MXNet |
| **SiećX** | Klasyczne algorytmy grafowe; manipulacja danymi |
| **OGB** (test porównawczy otwartego wykresu) | Standardowe punkty odniesienia i zbiory danych dla badań GNN |
| **CogDL** | Głębokie uczenie się dla wykresów; zorientowany na badania |
| **Widmowy** | Biblioteka GNN dla TensorFlow/Keras |
---

## Streszczenie
Grafowe sieci neuronowe rozszerzają głębokie uczenie się na dane relacyjne — sieci, cząsteczki, wykresy wiedzy i każdy system, w którym jednostki są połączone. Działają poprzez przekazywanie wiadomości między sąsiadami, umożliwiając każdemu węzłowi uczenie się na podstawie lokalnego kontekstu. Sieci GNN znalazły swoje największe zastosowanie w odkrywaniu leków, systemach rekomendacji, wykrywaniu oszustw i wykresach wiedzy. Dziedzina ta ewoluuje w kierunku transformatorów grafowych, grafów heterogenicznych i skalowalnego szkolenia dla ogromnych sieci w świecie rzeczywistym. Jeśli Twoje dane mają relacje, prawdopodobnie warto rozważyć sieci GNN.