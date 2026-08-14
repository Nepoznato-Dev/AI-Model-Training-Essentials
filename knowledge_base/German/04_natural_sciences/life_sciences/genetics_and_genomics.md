---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to life_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

# Genetik und Genomik
Genetik ist das Studium der Vererbung – wie Merkmale durch die DNA von den Eltern an die Nachkommen weitergegeben werden. Genomik ist die Untersuchung des gesamten Genoms: aller Gene, der nichtkodierenden Regionen, wie sie interagieren und wie sie sich zwischen Individuen und Populationen unterscheiden. Der Übergang von der Genetik zur Genomik wurde durch die Sequenzierungstechnologie vorangetrieben – wir gingen von der Untersuchung eines Gens nach dem anderen zum Lesen ganzer Genome in Stunden über und generierten Daten, die Medizin, Landwirtschaft, Forensik und unser Verständnis der Evolution verändern.
---

## DNA-Grundlagen
### DNA-Struktur
| Komponente | Beschreibung |
|-----------|-------------|
| **Nukleotid** | Baustein der DNA; besteht aus einem Zucker (Desoxyribose), einer Phosphatgruppe und einer stickstoffhaltigen Base |
| **Basen** | Adenin (A), Thymin (T), Guanin (G), Cytosin (C) |
| **Basenpaarung** | A paart sich mit T (2 Wasserstoffbrückenbindungen); G paart sich mit C (3 Wasserstoffbrückenbindungen) |
| **Doppelhelix** | Zwei antiparallel verlaufende Stränge (5' zu 3' und 3' zu 5'); zu einer Helix verdreht |
| **Chromosom** | Ein einzelnes, langes DNA-Molekül, das um Histonproteine ​​gewickelt ist; Menschen haben 46 (23 Paare) |
| **Genom** | Der vollständige DNA-Satz in einem Organismus; Das menschliche Genom umfasst etwa 3,2 Milliarden Basenpaare |
### Zentrales Dogma der Molekularbiologie
| Schritt | Prozess | Standort | Produkt |
|------|---------|----------|---------|
| **Replikation** | DNA → DNA | Kern | Zwei identische DNA-Moleküle |
| **Transkription** | DNA → mRNA | Kern | Messenger-RNA |
| **Übersetzung** | mRNA → Protein | Ribosom (Zytoplasma) | Polypeptidkette (Protein) |
---

## Genexpression
### Wie Gene reguliert werden
| Ebene | Mechanismus | Beispiel |
|-------|-----------|---------|
| **Epigenetisch** | DNA-Methylierung; Histonmodifikation; Chromatin-Remodellierung | Stummschaltung eines X-Chromosoms bei Frauen |
| **Transkriptionell** | Transkriptionsfaktoren binden Promotoren/Enhancer; aktivieren oder unterdrücken | Lac-Operon in Bakterien; auf Hormone reagierende Gene |
| **Posttranskriptionell** | Alternatives Spleißen; mRNA-Stabilität; microRNAs | Ein Gen → mehrere Proteinvarianten |
| **Übersetzung** | Verfügbarkeit von Ribosomen; Regulierung des Initiierungsfaktors | Eisenregulation über Ferritin-mRNA |
| **Posttranslational** | Proteinmodifikation (Phosphorylierung, Ubiquitinierung); Abbau | Zellzykluskontrolle |
---

## Vererbungsmuster
### Mendelsche Genetik
| Muster | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Autosomal-dominant** | Eine Kopie des Allels ist ausreichend | Huntington-Krankheit; Achondroplasie |
| **Autosomal-rezessiv** | Zwei Exemplare erforderlich | Mukoviszidose; Sichelzellenanämie |
| **X-chromosomal dominant** | Gen auf dem X-Chromosom; ein Exemplar ausreichend | Rett-Syndrom |
| **X-chromosomal rezessiv** | Gen auf dem X-Chromosom; Männer stärker betroffen | Hämophilie; Farbenblindheit |
| **Kodominanz** | Beide Allele werden gleichermaßen exprimiert | ABO-Blutgruppen (A und B) |
| **Unvollständige Dominanz** | Heterozygote ist intermediär | Rosa Blüten von roten und weißen Eltern |
| **Polygen** | Mehrere Gene tragen zu einem Merkmal bei | Höhe; Hautfarbe; Intelligenz |
| **Pleiotropie** | Ein Gen beeinflusst mehrere Merkmale | Marfan-Syndrom (Bindegewebe, Augen, Herz) |
---

## Genomik
### Arten der Genomik
| Geben Sie | ein Fokus | Bewerbung |
|------|-------|-------------|
| **Strukturelle Genomik** | 3D-Struktur aller Proteine ​​in einem Genom | Arzneimitteldesign; Protein-Engineering |
| **Funktionelle Genomik** | Was Gene bewirken; Geninteraktionen; Ausdrucksmuster | Krankheitsmechanismen verstehen |
| **Vergleichende Genomik** | Vergleich der Genome verschiedener Arten | Evolutionäre Beziehungen; Identifizierung geschützter Regionen |
| **Metagenomics** | DNA aus Umweltproben (nicht kultiviert) | Mikrobiomstudien; Entdeckung neuer Organismen |
| **Pharmakogenomik** | Wie Gene die Arzneimittelreaktion beeinflussen | Personalisierte Medizin; Medikamentendosierung |
| **Epigenomik** | Genomweite epigenetische Veränderungen | Krebsdiagnose; Entwicklungsbiologie |
### DNA-Sequenzierungstechnologien
| Generation | Technologie | Leselänge | Durchsatz | Hauptmerkmal |
|-----------|-----------|-------------|------------|-------------|
| **Erste Generation** | Sanger-Sequenzierung | ~1.000 bp | Niedrig | Goldstandard-Genauigkeit; zur Validierung verwendet |
| **Zweite Generation** | Illumina (Solexa) | 50–300 bp | Sehr hoch | Kurze Lektüre; dominante Plattform; niedrige Kosten pro Basis |
| **Zweite Generation** | Ionen-Torrent | 200–400 bp | Hoch | Halbleiterbasiert; keine Optik |
| **Dritte Generation** | PacBio (SMRT) | 10.000–100.000 bp | Mäßig | Lange Lektüre; löst sich wiederholende Regionen auf |
| **Dritte Generation** | Oxford Nanopore | Bis zu Millionen bp | Mäßig bis hoch | Ultralange Lesevorgänge; tragbar (MinION); Echtzeit |
---

## Genetische Variation
### Variationsarten
| Geben Sie | ein Beschreibung | Häufigkeit |
|------|-------------|-----------|
| **SNP** (Single Nucleotide Polymorphism) | Einzelner Basiswechsel | Am häufigsten; ~1 in 1.000 Basen |
| **Einfügung/Löschung (indel)** | Hinzufügen oder Entfernen von Basen | Kann Frameshift-Mutationen verursachen |
| **CNV** (Variation der Kopiennummer) | Duplizierte oder gelöschte Segmente (1 KB – mehrere MB) | Trägt zu Krankheit und Evolution bei |
| **Strukturelle Variation** | Inversionen; Translokationen; große Umstellungen | Seltener; kann pathogen sein |
| **Mikrosatellit (STR)** | Kurze Tandemwiederholungen (2–6 bp wiederholt) | Forensik; Vaterschaftstest |
### GWAS (Genomweite Assoziationsstudien)
| Schritt | Beschreibung |
|------|-------------|
| **1. Proben sammeln** | Fälle (mit Erkrankung) und Kontrollen (ohne) |
| **2. Genotyp** | Verwenden Sie SNP-Arrays, um Hunderttausende Varianten zu genotypisieren |
| **3. Statistischer Test** | Testen Sie jeden SNP auf seine Assoziation mit dem Merkmal |
| **4. Manhattan-Grundstück** | Visualisieren Sie Ergebnisse über alle Chromosomen hinweg |
| **5. Replikation** | Bestätigen Sie die Ergebnisse in unabhängigen Stichproben |
---

## Genbearbeitung
### CRISPR-Cas9
| Komponente | Funktion |
|-----------|----------|
| **Leit-RNA (gRNA)** | ~20 Nukleotide; entspricht der Ziel-DNA-Sequenz |
| **Cas9-Protein** | Molekulare Scheren; schneidet DNA an der Zielstelle |
| **PAM-Sequenz** | Kurzmotiv (NGG) neben dem Ziel; erforderlich für Cas9-Bindung |
| **HDR** (Homology-Directed Repair) | Präzise Bearbeitung anhand einer Spendervorlage |
| **NHEJ** (Nicht-homologe Endverbindung) | Fehleranfällige Reparatur; erstellt Einfügungen/Löschungen (Knockout) |
### Anwendungen zur Genbearbeitung
| Bewerbung | Beschreibung |
|-------------|-------------|
| **Therapeutisch** | Korrigieren Sie krankheitsverursachende Mutationen (Sichelzellenanämie; Beta-Thalassämie) |
| **Landwirtschaft** | Krankheitsresistente Pflanzen; verbessertes Vieh |
| **Forschung** | Knockout-Modelle erstellen; Genfunktion untersuchen |
| **Gene Drive** | Eine genetische Veränderung in einer Population verbreiten (z. B. malariaresistente Mücken) |
---

## Ethische Überlegungen
| Problem | Sorge |
|-------|---------|
| **Genetische Privatsphäre** | Wem gehören Ihre Genomdaten? Können Arbeitgeber oder Versicherer es nutzen? |
| **Genbearbeitung in Embryonen** | Erbliche Veränderungen; Designerbabys; unbeabsichtigte Off-Target-Effekte |
| **Genetische Diskriminierung** | GINA (USA) schützt vor Diskriminierung, weist jedoch Lücken auf |
| **Einverständniserklärung** | Genomdaten enthüllen Informationen über Verwandte, die nicht eingewilligt haben |
| **Datenspeicherung** | Die Genome sind groß (~200 GB roh); langfristige Speicher- und Sicherheitsherausforderungen |
| **Eigenkapital** | Genomische Medizin birgt die Gefahr einer Vergrößerung der gesundheitlichen Ungleichheiten, wenn sie nur wohlhabenden Bevölkerungsgruppen zur Verfügung steht |
---

## Zusammenfassung
Die Genetik untersucht, wie einzelne Gene funktionieren und vererbt werden. Die Genomik untersucht gesamte Genome – alle Gene, ihre Interaktionen und ihre Variation. DNA wird in RNA umgeschrieben, die in Proteine ​​übersetzt wird. Die Genexpression wird auf mehreren Ebenen reguliert: epigenetisch, transkriptionell, posttranskriptionell, translational und posttranslational. Die Vererbung folgt Mustern (dominant, rezessiv, polygen), die bestimmen, wie Merkmale zwischen den Generationen weitergegeben werden. Moderne Sequenzierungstechnologien (Illumina, PacBio, Nanopore) können ganze Genome schnell und kostengünstig lesen. CRISPR-Cas9 ermöglicht eine präzise Genbearbeitung mit transformativem Potenzial in Medizin und Landwirtschaft. Die größten Herausforderungen sind ethischer Natur: Wer kontrolliert die Genomdaten, wie reguliert man die Genbearbeitung in Embryonen und wie stellt man sicher, dass die Genommedizin allen zugute kommt, nicht nur den Privilegierten?