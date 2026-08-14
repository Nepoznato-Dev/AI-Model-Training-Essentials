---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Materialwissenschaft
In der Materialwissenschaft wird untersucht, wie die Struktur eines Materials (auf atomarer, mikroskopischer und makroskopischer Ebene) seine Eigenschaften bestimmt und wie Verarbeitungsmethoden verwendet werden können, um diese Struktur zu steuern, um die gewünschte Leistung zu erzielen. Es ist das Fachgebiet, das Fragen beantwortet wie: Warum ist Stahl stark, aber schwer? Warum ist Glas transparent, aber spröde? Wie können wir Batterien herstellen, die schneller aufladen? Welche Materialien überstehen die Bedingungen auf dem Mars? Jede Technologie, die Sie jemals verwendet haben, besteht aus Materialien, und Fortschritte in der Technologie erfordern fast immer Fortschritte in den Materialien.
---

## Das materialwissenschaftliche Tetraeder
Die vier miteinander verbundenen Elemente, die das Feld definieren:
| Element | Beschreibung |
|---------|-------------|
| **Struktur** | Wie Atome und Moleküle angeordnet sind (Kristallstruktur; Korngrenzen; Defekte) |
| **Eigenschaften** | Wie sich das Material verhält (mechanisch; elektrisch; thermisch; optisch; magnetisch) |
| **Verarbeitung** | Wie das Material hergestellt und geformt wird (Gießen; Sintern; Dotieren; Glühen) |
| **Leistung** | Wie das Material in einer realen Anwendung funktioniert |
Die wichtigste Erkenntnis: Eine Änderung der Verarbeitung ändert die Struktur, wodurch sich die Eigenschaften ändern, wodurch sich die Leistung ändert.
---

## Materialklassen
### Übersicht
| Klasse | Verklebung | Schlüsseleigenschaften | Beispiele |
|-------|---------|---------------|---------|
| **Metalle** | Metallisch (delokalisierte Elektronen) | Stark; duktil; leitfähig; undurchsichtig | Stahl; Aluminium; Kupfer; Titan |
| **Keramik** | Ionisch / kovalent | Hart; spröde; hitzebeständig; isolierend | Aluminiumoxid; Siliziumkarbid; Glas; Porzellan |
| **Polymere** | Kovalent (Ketten) + van der Waals | Leicht; flexibel; isolierend; niedriger Schmelzpunkt | Polyethylen; Nylon; Gummi; Epoxidharz |
| **Verbundwerkstoffe** | Kombination von zwei oder mehr Klassen | Maßgeschneiderte Immobilien; hohes Festigkeits-/Gewichtsverhältnis | Kohlefaser; Glasfaser; Beton |
| **Halbleiter** | Kovalent (mit kontrollierten Verunreinigungen) | Einstellbare Leitfähigkeit; Grundlagen der Elektronik | Silizium; Germanium; Galliumarsenid |
| **Biomaterialien** | Verschieden; biokompatibel erforderlich | Mit biologischen Systemen interagieren | Titanimplantate; Kollagen; Hydroxylapatit |
---

## Kristallstrukturen
### Häufige metallische Kristallstrukturen
| Struktur | Atome pro Elementarzelle | Packungsanteil | Beispiele |
|-----------|----|-----------------|---------|
| **FCC** (Flächenzentrierter Kubischer) | 4 | 0,74 (dichteste Packung) | Aluminium; Kupfer; Gold; Nickel; Austenit (γ-Eisen) |
| **BCC** (Körperzentriertes Kubisches) | 2 | 0,68 | Eisen (α-Eisen); Chrom; Wolfram; Molybdän |
| **HCP** (Hexagonal dicht gepackt) | 6 | 0,74 (dichteste Packung) | Titan; Zink; Magnesium; Kobalt |
### Warum die Kristallstruktur wichtig ist
| Eigentum | Einfluss der Kristallstruktur |
|----------|----------------|
| **Stärke** | Gleitsysteme (Ebenen, entlang derer Atome gleiten) unterscheiden sich in ihrer Struktur; FCC-Metalle sind duktiler als HCP |
| **Dichte** | Der Packungsanteil bestimmt, wie dicht Atome gepackt sind |
| **Phasentransformationen** | Eisen wandelt sich bei 912 °C von BCC in FCC um – dies ist die Grundlage der Stahlwärmebehandlung |
| **Anisotropie** | Die Eigenschaften können in nichtkubischen Kristallen je nach Richtung variieren |
---

## Mechanische Eigenschaften
### Schlüsselmetriken
| Eigentum | Definition | Einheiten | Typische Werte |
|----------|-----------|-------|----------------|
| **E-Modul (E)** | Steifheit; Spannung/Dehnung im elastischen Bereich | GPa | Stahl: 200; Aluminium: 70; Gummi: 0,01–0,1 |
| **Streckgrenze** | Spannung, bei der eine dauerhafte (plastische) Verformung beginnt | MPa | Stahl: 250–1000; Aluminium: 40–500 |
| **Zugfestigkeit (UTS)** | Maximale Belastung vor dem Scheitern | MPa | Stahl: 400–2000; Aluminium: 90–600 |
| **Duktilität (% Dehnung)** | Wie stark dehnt sich ein Material, bevor es bricht | % | Stahl: 10–50; Glas: <1 |
| **Zähigkeit** | Vor dem Bruch absorbierte Energie (Fläche unter der Spannungs-Dehnungs-Kurve) | MJ/m³ | Stahl: hoch; Keramik: niedrig |
| **Härte** | Beständigkeit gegen Oberflächeneindrücke | Verschiedene Maßstäbe | Diamant: am härtesten; Talk: am weichsten |
### Stärkung der Mechanismen
| Mechanismus | Wie es funktioniert | Beispiel |
|-----------|-------------|---------|
| **Körnungsverfeinerung** | Kleinere Körner = mehr Korngrenzen = schwerer für Versetzungen zu bewegen | Hall-Petch-Beziehung |
| **Mischkristallverstärkung** | Fremdatome verzerren das Gitter; Versetzungsbewegung behindern | Hinzufügen von Zink zu Kupfer → Messing |
| **Ausscheidungshärtung** | Kleine Partikel blockieren die Versetzungsbewegung | Auslagerungsgehärtete Aluminiumlegierungen |
| **Kaltverfestigung (Kaltverfestigung)** | Plastische Verformung erhöht die Versetzungsdichte; sie verheddern und behindern sich gegenseitig | Kaltwalzstahl |
| **Verbundverstärkung** | Starke Fasern in einer weicheren Matrix tragen die Last | Kohlenstofffaserverstärktes Polymer |
---

## Elektrische und thermische Eigenschaften
### Elektrische Leitfähigkeit
| Materialtyp | Leitfähigkeit (S/m) | Mechanismus |
|--------------|------|-----------|
| **Leiter** (Kupfer, Silber) | 10^7 – 10^8 | Freie Elektronen in metallischen Bindungen |
| **Halbleiter** (Silizium, GaAs) | 10^-6 – 10^4 | Durch Dotierung abstimmbar; Bandlückentechnik |
| **Isolatoren** (Glas, Gummi) | 10^-12 – 10^-20 | Große Bandlücke; Elektronen gebunden |
| **Supraleiter** | Unendlich (unterhalb der kritischen Temperatur) | Null elektrischer Widerstand; Meissner-Effekt |
### Thermische Eigenschaften
| Eigentum | Beschreibung | Wichtig für |
|----------|-------------|---------------|
| **Wärmeleitfähigkeit** | Wie gut fließt Wärme durch das Material | Kühlkörper; Isolierung |
| **Wärmeausdehnung** | Wie stark dehnt sich ein Material bei Erwärmung aus | Passende Materialien in Verbundwerkstoffen; Brücken; Schienen |
| **Spezifische Wärmekapazität** | Energie, die benötigt wird, um die Temperatur um 1°C zu erhöhen | Wärmeenergiespeicher |
| **Schmelzpunkt** | Temperatur, bei der ein Feststoff flüssig wird | Hochtemperaturanwendungen |
---

## Polymere
### Arten von Polymeren
| Geben Sie | ein Struktur | Eigenschaften | Beispiele |
|------|-----------|-----------|---------|
| **Thermoplaste** | Lineare oder verzweigte Ketten; schwache intermolekulare Kräfte | Beim Erhitzen schmelzen; recycelbar | Polyethylen; Polystyrol; Nylon |
| **Duroplaste** | Vernetztes Netzwerk; kovalente Bindungen zwischen Ketten | Nicht schmelzen; zersetzen sich bei hoher Temperatur | Epoxidharz; vulkanisierter Gummi; Bakelit |
| **Elastomere** | Leicht vernetzt; Spiralketten | Dehnen und wieder in Form bringen | Naturkautschuk; Silikon; Neopren |
### Polymereigenschaften
| Eigentum | Beschreibung |
|----------|-------------|
| **Glasübergangstemperatur (Tg)** | Unterhalb von Tg: hart und spröde. Über Tg: weich und flexibel |
| **Kristallinität** | Teilkristalline Polymere sind stärker und undurchsichtiger; amorph sind transparent |
| **Molekulargewicht** | Höheres MW = stärker; schwerer zu verarbeiten |
| **Polymerisationsgrad** | Anzahl der Monomereinheiten; wirkt sich auf Eigenschaften aus |
---

## Phasendiagramme
### Eisen-Kohlenstoff-Phasendiagramm (vereinfacht)
| Phase | Kohlenstoffgehalt | Struktur | Eigenschaften |
|-------|---------------|-----------|-----------|
| **Ferrit (α)** | Bis zu 0,022 % | BCC-Eisen | Weich; duktil; magnetisch |
| **Austenit (γ)** | Bis zu 2,14 % | FCC-Eisen | Nicht magnetisch; formbar |
| **Zementit (Fe₃C)** | 6,67 % | Orthorhombisch | Hart; spröde |
| **Perlit** | 0,76 % (Eutektoid) | Abwechselnde Schichten aus Ferrit und Zementit | Stark; hart |
| **Martensit** | Beliebig (durch schnelles Abschrecken entstanden) | BCT (körperzentriertes Tetragonal) | Sehr hart; spröde |
---

## Moderne und neue Materialien
| Material | Beschreibung | Bewerbung |
|----------|-------------|-------------|
| **Graphen** | Einzelne Schicht aus Kohlenstoffatomen; stärkstes bekanntes Material; ausgezeichneter Dirigent | Elektronik; Verbundwerkstoffe; Sensoren |
| **Kohlenstoffnanoröhren** | Aufgerollte Graphenzylinder; extremes Verhältnis von Festigkeit zu Gewicht | Verbundwerkstoffe; Elektronik; Energiespeicher |
| **Perowskite** | Kristallstruktur ABX₃; einstellbare Bandlücke | Solarzellen; LEDs; Detektoren |
| **Metallorganische Gerüste (MOFs)** | Poröse kristalline Materialien; enorme Oberfläche | Gasspeicherung; Katalyse; Arzneimittelabgabe |
| **Formgedächtnislegierungen** | Bei Erwärmung wieder in die ursprüngliche Form zurückkehren | Stents; Aktoren; selbstreparierende Strukturen |
| **Metamaterialien** | Die konstruierte Mikrostruktur verleiht Eigenschaften, die in der Natur nicht zu finden sind | Negativer Brechungsindex; Tarnung |
| **Hochentropielegierungen** | Mehrere Hauptelemente; ungewöhnliche Kombinationen von Eigenschaften | Extreme Umgebungen; Luft- und Raumfahrt |
---

## Zusammenfassung
Die Materialwissenschaft verbindet die atomare Struktur eines Materials mit seinen makroskopischen Eigenschaften und seiner Leistung in der Praxis. Metalle sind stark und leitfähig, aber schwer. Keramik ist hart und hitzebeständig, aber spröde. Polymere sind leicht und flexibel, aber durch die Temperatur begrenzt. Verbundwerkstoffe vereinen das Beste aus verschiedenen Klassen. Die Kristallstruktur bestimmt das mechanische Verhalten. Die Verarbeitung – Wärmebehandlung, Legierung, Kaltverfestigung – steuert die Mikrostruktur und damit die Eigenschaften. Moderne Materialien wie Graphen, Perowskite und MOFs verschieben die Grenzen des Möglichen. Das Fachgebiet ist grundsätzlich interdisziplinär: Physik erklärt Bindungen, Chemie erklärt Reaktionen, Technik erklärt Leistung, und all das ist für jede Technologie von Bedeutung, vom Smartphone bis zum Raumschiff.