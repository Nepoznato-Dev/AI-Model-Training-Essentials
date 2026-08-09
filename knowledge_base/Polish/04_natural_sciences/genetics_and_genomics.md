---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
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
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Genetyka i genomika
Genetyka to nauka o dziedziczności – o tym, jak cechy przekazywane są z rodziców na potomstwo poprzez DNA. Genomika to badanie całych genomów: wszystkich genów, regionów niekodujących, ich interakcji oraz różnic między jednostkami i populacjami. Przejście od genetyki do genomiki było napędzane technologią sekwencjonowania — przeszliśmy od badania jednego genu na raz do odczytywania całych genomów w ciągu kilku godzin, generując dane, które zmieniają medycynę, rolnictwo, kryminalistykę i nasze rozumienie ewolucji.
---

## Podstawy DNA
### Struktura DNA
| Składnik | Opis |
|---------------|------------|
| **Nukleotyd** | Element budulcowy DNA; składa się z cukru (dezoksyrybozy), grupy fosforanowej i zasady azotowej |
| **Bazy** | Adenina (A), Tymina (T), Guanina (G), Cytozyna (C) |
| **Parowanie podstawowe** | A tworzy parę z T (2 wiązania wodorowe); G paruje z C (3 wiązania wodorowe) |
| **Podwójna helisa** | Dwie nici biegnące przeciwrównolegle (5' do 3' i 3' do 5'); skręcony w helisę |
| **Chromosomy** | Pojedyncza, długa cząsteczka DNA owinięta wokół białek histonowych; ludzie mają 46 (23 pary) |
| **Genom** | Kompletny zestaw DNA w organizmie; ludzki genom ma ~3,2 miliarda par zasad |
### Centralny dogmat biologii molekularnej
| Krok | Proces | Lokalizacja | Produkt |
|------|---------|----------|---------|
| **Replikacja** | DNA → DNA | Jądro | Dwie identyczne cząsteczki DNA |
| **Transkrypcja** | DNA → mRNA | Jądro | Komunikator RNA |
| **Tłumaczenie** | mRNA → białko | Rybosom (cytoplazma) | Łańcuch polipeptydowy (białko) |
---

## Ekspresja genu
### Jak regulowane są geny
| Poziom | Mechanizm | Przykład |
|-------|-----------|--------|
| **Epigenetyczne** | metylacja DNA; modyfikacja histonów; przebudowa chromatyny | Wyciszenie jednego chromosomu X u kobiet |
| **Transkrypcja** | Czynniki transkrypcyjne wiążą promotory/wzmacniacze; aktywuj lub stłum | Operon Lac w bakteriach; geny reagujące na hormony |
| **Potranskrypcyjne** | Alternatywne łączenie; stabilność mRNA; mikroRNA | Jeden gen → wiele wariantów białka |
| **Tłumaczenie** | Dostępność rybosomów; regulacja czynnika inicjacji | Regulacja żelaza poprzez mRNA ferrytyny |
| **Potranslacyjne** | Modyfikacja białek (fosforylacja, ubikwitynacja); degradacja | Kontrola cyklu komórkowego |
---

## Wzorce dziedziczenia
### Genetyka mendlowska
| Wzór | Opis | Przykład |
|--------|-------------|--------|
| **Autosomalny dominujący** | Wystarczająca jest jedna kopia allelu | choroba Huntingtona; achondroplazja |
| **Autosomalny recesywny** | Wymagane dwie kopie | Mukowiscydoza; anemia sierpowata |
| **Dominant połączony z X** | Gen na chromosomie X; wystarczy jeden egzemplarz | Zespół Retta |
| **Recesywny sprzężony z X** | Gen na chromosomie X; mężczyźni bardziej dotknięci | Hemofilia; ślepota barw |
| **Kodominacja** | Oba allele wyrażone jednakowo | Grupy krwi ABO (A i B) |
| **Niepełna dominacja** | Heterozygota jest pośrednia | Różowe kwiaty od czerwonych i białych rodziców |
| **Poligeniczny** | Na jedną cechę składa się wiele genów | Wysokość; kolor skóry; inteligencja |
| **Plejotropia** | Jeden gen wpływa na wiele cech | Zespół Marfana (tkanka łączna, oczy, serce) |
---

## Genomika
### Rodzaje genomiki
| Wpisz | Skup się | Aplikacja |
|------|------------|------------|
| **Genomika strukturalna** | Struktura 3D wszystkich białek w genomie | Projektowanie leków; inżynieria białek |
| **Genomika funkcjonalna** | Co robią geny; interakcje genów; wzorce ekspresji | Zrozumienie mechanizmów chorobowych |
| **Genomika porównawcza** | Porównanie genomów różnych gatunków | Relacje ewolucyjne; identyfikacja regionów chronionych |
| **Metagenomika** | DNA z próbek środowiskowych (niehodowanych) | Badania mikrobiomu; odkrywanie nowych organizmów |
| **Farmakogenomika** | Jak geny wpływają na reakcję na lek | Medycyna spersonalizowana; dawkowanie leku |
| **Epigenomika** | Modyfikacje epigenetyczne obejmujące cały genom | Diagnoza raka; biologia rozwoju |
### Technologie sekwencjonowania DNA
| Pokolenie | Technologia | Przeczytaj Długość | Przepustowość | Kluczowa funkcja |
|---------------|-----------|------------|------------|------------|
| **Pierwsza generacja** | Sekwencjonowanie Sangera | ~1000 pz | Niski | Złoty standard dokładności; używany do walidacji |
| **Druga generacja** | Illumina (Solexa) | 50–300 pz | Bardzo wysoki | Krótkie lektury; dominująca platforma; niski koszt w przeliczeniu na bazę |
| **Druga generacja** | Potok jonowy | 200–400 pz | Wysoki | Oparte na półprzewodnikach; brak optyki |
| **Trzecia generacja** | PacBio (SMRT) | 10 000–100 000 p.n.e. | Umiarkowany | Długie lektury; rozwiązuje powtarzające się regiony |
| **Trzecia generacja** | Oxford Nanopor | Do milionów pz | Umiarkowany do wysokiego | Bardzo długie odczyty; przenośny (MinION); w czasie rzeczywistym |
---

## Zmienność genetyczna
### Rodzaje zmian
| Wpisz | Opis | Częstotliwość |
|------|------------|---------------|
| **SNP** (polimorfizm pojedynczego nukleotydu) | Pojedyncza zmiana bazy | Najczęściej; ~1 na 1000 zasad |
| **Wstawienie / Usunięcie (indel)** | Dodawanie lub usuwanie zasad | Może powodować mutacje przesunięcia ramki |
| **CNV** (zmiana numeru kopii) | Zduplikowane lub usunięte segmenty (1 kb – kilka Mb) | Przyczynia się do chorób i ewolucji |
| **Zróżnicowanie strukturalne** | Inwersje; translokacje; duże przegrupowania | Mniej powszechne; może być patogenny |
| **Mikrosatelita (STR)** | Krótkie powtórzenia w tandemie (powtórzone 2–6 pz) | kryminalistyka; badanie na ojcostwo |
### GWAS (badania asocjacyjne całego genomu)
| Krok | Opis |
|------|------------|
| **1. Zbierz próbki** | Przypadki (z chorobą) i kontrole (bez) |
| **2. Genotyp** | Użyj tablic SNP do genotypowania setek tysięcy wariantów |
| **3. Test statystyczny** | Przetestuj każdy SNP pod kątem powiązania z cechą |
| **4. Działka na Manhattanie** | Wizualizuj wyniki na wszystkich chromosomach |
| **5. Replikacja** | Potwierdź ustalenia w niezależnych próbach |
---

## Edycja genów
### CRISPR-Cas9
| Składnik | Funkcja |
|----------|----------|
| **Przewodnikowy RNA (gRNA)** | ~20 nukleotydów; pasuje do docelowej sekwencji DNA |
| **Białko Cas9** | Nożyczki molekularne; tnie DNA w miejscu docelowym |
| **Sekwencja PAM** | Krótki motyw (NGG) obok celu; wymagane do powiązania Cas9 |
| **HDR** (naprawa ukierunkowana na homologię) | Precyzyjna edycja z wykorzystaniem szablonu dawcy |
| **NHEJ** (łączenie końców niehomologicznych) | Naprawa podatna na błędy; tworzy wstawki/usunięcia (wybijanie) |
### Aplikacje do edycji genów
| Aplikacja | Opis |
|------------|------------|
| **Terapeutyczne** | Prawidłowe mutacje chorobotwórcze (sierpowatokrwinkowa; beta-talasemia) |
| **Rolnictwo** | Rośliny odporne na choroby; ulepszone zwierzęta gospodarskie |
| **Badania** | Twórz modele nokautów; badać funkcję genu |
| **Napęd genowy** | Rozprzestrzenianie modyfikacji genetycznej w populacji (np. komary odporne na malarię) |
---

## Względy etyczne
| Wydanie | Obawa |
|-------|-------------|
| **Prywatność genetyczna** | Kto jest właścicielem danych o Twoim genomie? Czy pracodawcy lub ubezpieczyciele mogą z tego skorzystać? |
| **Edycja genów w zarodkach** | Zmiany dziedziczne; designerskie dzieci; niezamierzone efekty odbiegające od celu |
| **Dyskryminacja genetyczna** | GINA (USA) chroni przed pewną dyskryminacją, ale ma luki |
| **Świadoma zgoda** | Dane genomowe ujawniają informacje o krewnych, którzy nie wyrazili zgody |
| **Przechowywanie danych** | Genomy są duże (~200 GB surowego); długoterminowe wyzwania związane z przechowywaniem i bezpieczeństwem |
| **Kapitał** | Medycyna genomowa stwarza ryzyko pogłębienia dysproporcji w zdrowiu, jeśli będzie dostępna tylko dla zamożnych populacji |
---

## Streszczenie
Genetyka bada sposób działania i dziedziczenia poszczególnych genów. Genomika bada całe genomy – wszystkie geny, ich interakcje i zmienność. DNA ulega transkrypcji na RNA, które ulega translacji na białka. Ekspresja genów jest regulowana na wielu poziomach: epigenetycznym, transkrypcyjnym, potranskrypcyjnym, translacyjnym i potranslacyjnym. Dziedziczenie następuje według wzorców (dominujący, recesywny, wielogenowy), które określają, w jaki sposób cechy przechodzą między pokoleniami. Nowoczesne technologie sekwencjonowania (Illumina, PacBio, Nanopore) pozwalają szybko i tanio odczytać całe genomy. CRISPR-Cas9 umożliwia precyzyjną edycję genów z potencjałem transformacyjnym w medycynie i rolnictwie. Największe wyzwania mają charakter etyczny: kto kontroluje dane genomiczne, jak regulować edycję genów w embrionach i jak zapewnić, że medycyna genomiczna przyniesie korzyści wszystkim, a nie tylko uprzywilejowanym.