<!--
---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Blockchain i systemy rozproszone
Blockchain to specyficzny rodzaj systemu rozproszonego — zdecentralizowana księga przeznaczona tylko do dodawania, w której rekordy (bloki) są połączone za pomocą skrótów kryptograficznych. Systemy rozproszone to szersza dziedzina umożliwiająca współpracę wielu komputerów w jeden. Obie koncepcje są ważne dla zrozumienia nowoczesnej infrastruktury, od kryptowaluty, przez rozproszone bazy danych, po algorytmy konsensusu, które napędzają usługi globalne.
---

## Podstawy systemów rozproszonych
### Dlaczego systemy rozproszone?
| Motywacja | Opis |
|---------------|------------|
| **Skalowalność** | Dodaj więcej maszyn, aby obsłużyć większe obciążenie |
| **Tolerancja na błędy** | System kontynuuje pracę nawet w przypadku awarii niektórych maszyn |
| **Rozkład geograficzny** | Obsługuj użytkowników z pobliskich centrów danych |
| **Specjalizacja** | Różne maszyny wykonują różne zadania |
### Kluczowe pojęcia
| Koncepcja | Opis | Wyzwanie |
|--------|------------|---------|
| **Konsensus** | Uzyskanie zgody wszystkich węzłów na wartość | Partycje sieciowe; Błędy bizantyjskie |
| **Replikacja** | Kopiowanie danych pomiędzy wieloma węzłami | Spójność a dostępność |
| **Podział (sharding)** | Dzielenie danych pomiędzy węzłami | Gorące miejsca; zapytania między fragmentami |
| **Modele spójności** | Gwarancje dotyczące tego, co widzą różni czytelnicy | Silna konsystencja jest powolna; ostateczna spójność może zaskoczyć użytkowników |
| **Twierdzenie CAP** | Możesz mieć tylko 2 z: Spójność, Dostępność, Tolerancja partycji | W praktyce wymagana jest tolerancja podziału; wybierz C lub A |
### Twierdzenie WPR
| Wybór | Co dostajesz | Z czego rezygnujesz | Przykład |
|------------|------------|----------------|--------|
| **CP** | Spójne + tolerancja partycji | Niektóre węzły mogą być niedostępne podczas partycji | HBase, MongoDB, Redis |
| **AP** | Dostępne + tolerancja partycji | Odczyty mogą zwrócić nieaktualne dane | Cassandra, DynamoDB, CouchDB |
| **CA** | Spójne + dostępne | Nie toleruje partycji sieciowych | Jednowęzłowe bazy danych (niezupełnie rozproszone) |
---

## Algorytmy konsensusu
W jaki sposób rozproszone węzły zgadzają się co do stanu systemu?
| Algorytm | Wpisz | Tolerancja błędów | Używany w |
|----------|------|----------------|--------|
| **Paxos** | Odporny na awarie | Do f awarii z 2f+1 węzłami | Google Pulchny; teoria podstawowa |
| **Tratwa** | Odporny na awarie | Do f awarii z 2f+1 węzłami | itp., Konsul, TiKV |
| **PBFT** | Bizantyjski odporny na błędy | Do f awarii z 3f+1 węzłami | Tkanina Hyperledger |
| **Dowód pracy** | Bizantyjski odporny na błędy | Zależy od mocy mieszającej | Bitcoin |
| **Dowód stawki** | Bizantyjski odporny na błędy | Zależy od stawki | Ethereum 2.0, Cardano |
### Tratwa (uproszczona)
| Rola | Odpowiedzialność |
|------|----------------------------|
| **Lider** | Obsługuje wszystkie żądania klientów; wysyła wpisy dziennika do obserwujących |
| **Obserwator** | Odpowiada na prośby lidera; głosów w wyborach |
| **Kandydat** | Prosi o głosy, aby zostać liderem |
1. Wszystkie węzły zaczynają jako obserwujący
2. Jeśli zwolennik nie otrzyma wiadomości od lidera o przekroczeniu limitu czasu w wyborach, staje się kandydatem
3. Kandydaci proszą o głosy; liderem zostaje ten, który zdobędzie najwięcej głosów
4. Lider replikuje wpisy dziennika do obserwujących
5. Gdy większość potwierdzi, wpis zostaje zatwierdzony
---

## Łańcuch bloków
### Jak działa łańcuch bloków
| Składnik | Opis |
|---------------|------------|
| **Blok** | Partia transakcji + metadane + hash poprzedniego bloku |
| **Hasz** | Kryptograficzny odcisk palca zawartości bloku |
| **Łańcuch** | Każdy blok odwołuje się do skrótu poprzedniego bloku, tworząc niezmienny łańcuch |
| **Konsensus** | Uczestnicy sieci uzgadniają, które bloki dodać |
| **Drzewo Merkle** | Drzewo skrótów podsumowujące wszystkie transakcje w bloku |
### Dlaczego Blockchain trudno manipulować
1. Każdy blok zawiera skrót poprzedniego bloku
2. Zmiana dowolnej transakcji powoduje zmianę hasha bloku
3. Zmieniony hash przerywa łańcuch – wszystkie kolejne bloki tracą ważność
4. Osoba atakująca musiałaby ponownie eksplorować wszystkie kolejne bloki ORAZ kontrolować ponad 50% sieci
### Rodzaje łańcuchów bloków
| Wpisz | Dostęp | Walidator | Przykład |
|------|--------|-----------|---------|
| **Publiczne (bez uprawnień)** | Każdy potrafi czytać i pisać | Otwarty konsensus (PoW, PoS) | Bitcoin, Ethereum |
| **Prywatne (dozwolone)** | Ograniczony dostęp | Znane walidatory | Hyperledger, Corda |
| **Konsorcjum** | Zarządzane przez grupę organizacji | Wybrane walidatory | R3 Corda dla bankowości |
### Inteligentne kontrakty
Samowykonujący się kod przechowywany w łańcuchu bloków, który działa po spełnieniu określonych warunków.
| Platforma | Język | Godna uwagi funkcja |
|---------|----------|--------------------------------|
| **Etherium** | Solidność, Vyper | Największy ekosystem inteligentnych kontraktów |
| **Solana** | Rdza, C | Wysoka przepustowość; niskie opłaty |
| **Kardano** | Haskell (Plutus) | Recenzowane; weryfikacja formalna |
| **Hiperksięga** | Idź, Java, JavaScript | Przedsiębiorstwo; dozwolone |
---

## Kryptowaluta
| Waluta | Konsensus | podaż | Podstawowe zastosowanie |
|---------|-----------|--------|------------|
| **Bitcoin** | Dowód pracy | 21 milionów (ograniczone) | Magazyn wartości; cyfrowe złoto |
| **Etherium** | Dowód stawki | Brak twardego limitu | Inteligentne kontrakty; DeFi; NFT |
| **Solana** | Dowód stawki + dowód historii | Brak twardego limitu | Szybkie transakcje |
| **Kardano** | Dowód stawki (Uroboros) | 45 miliardów (ograniczony) | Podejście akademickie; zrównoważony rozwój |
---

## Rozproszone bazy danych
| Baza danych | Architektura | Spójność | Najlepsze dla |
|---------|-------------|-------------|--------------|
| **Kasandra** | Szeroka kolumna; peer-to-peer | Przestrajalny (ewentualnie do kworum) | Wysoka przepustowość zapisu; szereg czasowy |
| **MongoDB** | Dokument; zestawy replik | Ewentualne (z opcją spójności przyczynowej) | Elastyczny schemat; szybki rozwój |
| **KaraluchDB** | Rozproszony SQL; Konsensus tratwy | Silny | Rozproszony SQL; globalne wdrożenie |
| **TiDB** | Rozproszony SQL; Tratwa (przez TiKV) | Silny | Kompatybilny z MySQL; skalowanie poziome |
| **DynamoDB** | Klucz-wartość; udało się | Ewentualne (lub mocne przy spójnych odczytach) | Bezserwerowy; Zintegrowany z AWS |
| **Klucz** | Rozproszony SQL; Paxos | Silny | Chmura Google; globalna spójność |
---

## Wzorce systemów rozproszonych
| Wzór | Opis | Przypadek użycia |
|-------------|------------|---------|
| **Wybór lidera** | Wybierz jeden węzeł do koordynowania | Lider tratwy; Strażnik Zoo |
| **Replikacja** | Kopiuj dane w celu redundancji i odczytuj skalowanie | Repliki baz danych; CDN |
| **Rozbicie** | Podziel dane według zakresu kluczy lub skrótu | Wielkoskalowe bazy danych |
| **MapaReduce** | Podziel obliczenia na węzły; wyniki zbiorcze | Duże przetwarzanie danych |
| **Protokół plotek** | Węzły okresowo dzielą się stanem z losowymi urządzeniami równorzędnymi | członkostwo w klastrze; wykrywanie awarii |
| **Zatwierdzenie dwufazowe** | Koordynuj transakcje w wielu węzłach | Rozproszone bazy danych |
| **Wzór Sagi** | Seria transakcji lokalnych z działaniami kompensacyjnymi | Transakcje mikrousługowe |
| **Wyłącznik** | Przestań wywoływać nieudaną usługę; szybko zawieść | Odporność; zapobieganie kaskadowym awariom |
---

## Wyzwania w systemach rozproszonych
| Wyzwanie | Opis | Łagodzenie |
|---------------|------------|------------|
| **Partycje sieciowe** | Węzły nie mogą się komunikować | kompromis w zakresie WPR; spróbuj ponownie z wycofaniem |
| **Zegar przekrzywiony** | Różne węzły mają różne zegary | Używaj zegarów logicznych; NTP; unikaj polegania na czasie na zegarze ściennym |
| **Błędy bizantyjskie** | Węzły, które leżą lub zachowują się arbitralnie | konsensus BFT; blockchain |
| **Rozszczepiony mózg** | Obydwa dwa węzły myślą, że są liderem | Ogrodzenie; decyzje na podstawie kworum |
| **Kaskadowe awarie** | Jedna porażka wyzwala inne | Wyłączniki automatyczne; grodzie; pełna wdzięku degradacja |
| **Spójność danych** | Synchronizacja replik | modele spójności; rozwiązywanie konfliktów |
---

## Streszczenie
Dzięki systemom rozproszonym nowoczesne oprogramowanie skaluje się, przetrwa awarie i obsługuje użytkowników na całym świecie. Algorytmy konsensusu (Raft, Paxos) zapewniają zgodność węzłów. Blockchainy dodają weryfikację kryptograficzną i decentralizację, aby stworzyć niezaufane księgi rachunkowe. Rozproszone bazy danych (Cassandra, CockroachDB, DynamoDB) obsługują dane na dużą skalę. Podstawowy kompromis – ujęty w twierdzeniu CAP – dotyczy spójności i dostępności, gdy sieć jest zawodna. Zrozumienie tych koncepcji jest niezbędne do budowania systemów działających w skali internetowej.