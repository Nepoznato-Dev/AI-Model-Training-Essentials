---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
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

# Terraform und Infrastruktur als Code
Terraform ist das am weitesten verbreitete IaC-Tool (Infrastructure as Code) – Sie können damit Cloud-Infrastruktur (Server, Datenbanken, Netzwerke, Berechtigungen) in deklarativen Konfigurationsdateien definieren, die versioniert, überprüft, getestet und automatisiert werden können. Anstatt sich durch eine Cloud-Konsole zu klicken, schreiben Sie Code, der den gewünschten Zustand Ihrer Infrastruktur beschreibt, und Terraform ermittelt, welche Änderungen vorgenommen werden müssen.
---

## Kernkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Anbieter** | Plugin, das eine bestimmte Cloud-Plattform (AWS, Azure, GCP usw.) verwaltet |
| **Ressource** | Ein Infrastrukturobjekt (Server, Datenbank, Netzwerk) |
| **Staat** | Terraforms Aufzeichnung der vorhandenen Infrastruktur; in einer Statusdatei | gespeichert
| **Plan** | Vorschau auf die Änderungen, die Terraform vornehmen wird |
| **Anwenden** | Führen Sie den Plan aus. Infrastruktur erstellen/aktualisieren/zerstören |
| **Modul** | Wiederverwendbare Sammlung von Ressourcen |
| **Variable** | Eingabeparameter für Konfigurationen |
| **Ausgabe** | Aus einem Modul oder einer Konfiguration exportierter Wert |
| **Datenquelle** | Informationen aus bestehender Infrastruktur lesen |
---

## Grundlegender Arbeitsablauf
| Schritt | Befehl | Beschreibung |
|------|---------|-------------|
| **1. Konfiguration schreiben** | Erstellen Sie `.tf`-Dateien | Definieren Sie Anbieter, Ressourcen, Variablen |
| **2. Initialisieren** | `terraform init`| Download-Anbieter; Backend einrichten |
| **3. Formatieren** | `terraform fmt`| Formatierung standardisieren |
| **4. Validieren** | `terraform validate`| Syntax und Konfiguration prüfen |
| **5. Plan** | `terraform plan`| Vorschau der Änderungen (Probelauf) |
| **6. Bewerben** | `terraform apply`| Infrastruktur erstellen oder aktualisieren |
| **7. Zerstören** | `terraform destroy`| Sämtliche verwaltete Infrastruktur abreißen |
---

## Allgemeine Befehle
| Befehl | Beschreibung |
|---------|-------------|
| `terraform init`| Arbeitsverzeichnis initialisieren; Download-Anbieter und Module |
| `terraform plan`| Zeigen Sie, welche Änderungen vorgenommen werden |
| `terraform apply`| Änderungen übernehmen;`-auto-approve`hinzufügen, um die Bestätigung zu überspringen |
| `terraform destroy`| Alle verwalteten Ressourcen zerstören |
| `terraform fmt`| Konfigurationsdateien im Standardstil formatieren |
| `terraform validate`| Konfigurationssyntax validieren |
| `terraform output`| Ausgabewerte anzeigen |
| `terraform state list`| Alle Ressourcen im Status | auflisten
| `terraform state show <resource>`| Details einer bestimmten Ressource anzeigen |
| `terraform import <resource> <id>`| Vorhandene Infrastruktur in den Zustand importieren |
| `terraform taint <resource>`| Markieren Sie eine Ressource zur Erholung bei der nächsten Bewerbung |
| `terraform refresh`| Status aktualisieren, damit er mit der realen Infrastruktur übereinstimmt |
| `terraform graph`| Erzeugen Sie ein visuelles Abhängigkeitsdiagramm (DOT-Format) |
| `terraform console`| Interaktive Konsole zum Testen von Ausdrücken |
---

## Staatsverwaltung
| Best Practice | Beschreibung |
|--------------|-------------|
| **Fernzustand** | Speichern Sie den Status in S3, GCS, Azure Blob oder Terraform Cloud – niemals lokal |
| **Statussperre** | Verwenden Sie DynamoDB (S3-Backend) oder natives Sperren, um gleichzeitige Änderungen zu verhindern |
| **Staatliche Verschlüsselung** | Aktivieren Sie die Verschlüsselung im Ruhezustand für Statusdateien (sie enthalten vertrauliche Daten) |
| **Staatstrennung** | Verwenden Sie separate Statusdateien für verschiedene Umgebungen oder Teams |
| **Statussicherung** | Remote-Backends automatisch Versionsstatus; Lassen Sie dies aktiviert |
| **Bearbeiten Sie den Status niemals manuell** | Verwenden Sie stattdessen`terraform state mv`,`rm`,`import`|
---

## Modulstruktur
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Variablentypen
| Geben Sie | ein Beispiel | Anwendungsfall |
|------|---------|----------|
| **Zeichenfolge** | `variable "region" { type = string }`| Einzelner Textwert |
| **Nummer** | `variable "count" { type = number }`| Numerischer Wert |
| **bool** | `variable "enable" { type = bool }`| Wahr/Falsch-Flag |
| **Liste** | `variable "zones" { type = list(string) }`| Geordnete Sammlung |
| **Karte** | `variable "tags" { type = map(string) }`| Schlüssel-Wert-Paare |
| **Objekt** | `variable "config" { type = object({...}) }`| Strukturierte Konfiguration |
---

## Gemeinsame Muster
| Muster | Beschreibung |
|---------|-------------|
| **Anzahl** | `count = 3`erstellt mehrere Instanzen einer Ressource |
| **Für jeden** | `for_each = var.items`iteriert über eine Karte oder einen Satz |
| **Dynamische Blöcke** | Generieren Sie wiederholt verschachtelte Blöcke (z. B. Eingangsregeln) |
| **Lokale Werte** | `locals { ... }`für berechnete Werte und Reduzierung von Wiederholungen |
| **Datenquellen** | Vorhandene Infrastruktur lesen (z. B. eine vorhandene VPC finden) |
| **Versorger** | Führen Sie nach der Erstellung Skripts für Ressourcen aus (sparsam verwenden) |
| **Arbeitsbereiche** | Separater Status für verschiedene Umgebungen innerhalb derselben Konfiguration |
---

## Fehlerbehebung
| Problem | Lösung |
|---------|----------|
| **Zustandsdrift** | Führen Sie`terraform plan`aus, um Unterschiede anzuzeigen. `terraform apply`zum Abgleichen |
| **Gesperrter Zustand** | Überprüfen Sie, wer das Schloss hat; verwenden Sie `terraform force-unlock`, wenn sicher |
| **Anbieterfehler** | Überprüfen Sie Ihre Anmeldeinformationen. Anbieterversion aktualisieren; API-Grenzwerte prüfen |
| **Importkonflikte** | Ressource bereits im Status; Verwenden Sie zuerst`terraform state rm`|
| **Zirkuläre Abhängigkeiten** | Ressourcen umstrukturieren; verwenden Sie`depends_on`sorgfältig |
| **Großer Staat** | In Module aufgeteilt; Verwenden Sie`-target`für Teiloperationen |
---

## Zusammenfassung
Terraform verwaltet die Infrastruktur über deklarative Konfigurationsdateien. Der Workflow ist: Konfiguration schreiben → Init → Plan → Anwenden. Der Status verfolgt, was vorhanden ist und per Sperrung remote gespeichert werden muss. Module ermöglichen die Wiederverwendung. Variablen parametrisieren Konfigurationen. Die wichtigsten Prinzipien sind: Infrastruktur als Code behandeln (Versionskontrolle; Überprüfung; Test); Bearbeiten Sie den Status niemals manuell. vor der Bewerbung planen; Remote-Status mit Sperre verwenden; und Strukturkonfigurationen mit Modulen für Wartbarkeit.