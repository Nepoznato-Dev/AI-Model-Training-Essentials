---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Technologie und Informatik
Computer sind überall – in Ihrem Telefon, Ihrem Auto, Ihrem Kühlschrank, Ihren medizinischen Geräten und der Infrastruktur, die die moderne Gesellschaft betreibt. Sie müssen kein Programmierer sein, um zu verstehen, wie alles funktioniert. In dieser Datei werden die Grundlagen behandelt: Was ein Computer ist, wie das Internet funktioniert, wie Software erstellt wird und welche Konzepte die digitale Welt prägen.
> **Möchten Sie tiefer gehen?** Diese Datei bietet einen umfassenden Überblick. Eine detaillierte Abdeckung aller Themen finden Sie in den entsprechenden Dateien in[`01_coding_and_technology/`](../01_coding_and_technology/)– einschließlich [database systems](../01_coding_and_technology/database_systems.md), [cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)und.
---

## Was ist ein Computer?
Im Kern macht jeder Computer – vom Smartphone bis zum Supercomputer – das Gleiche: Er nimmt Eingaben entgegen, verarbeitet sie gemäß Anweisungen (ein Programm) und erzeugt Ausgaben. Der Zauber liegt in der Geschwindigkeit und dem Ausmaß.
### Die Von-Neumann-Architektur
Fast alle modernen Computer folgen diesem grundlegenden Design:
| Komponente | Was es tut | Analogie |
|-----------|-------------|---------|
| **CPU** (Zentraleinheit) | Führt Anweisungen aus; das „Gehirn“ | Der Koch folgt einem Rezept |
| **RAM** (Speicher) | Speichert Daten, die die CPU aktiv nutzt; geht verloren, wenn der Strom ausgeschaltet ist | Die Arbeitsplatte – schneller Zugriff, begrenzter Platz |
| **Speicher** (SSD/HDD) | Speichert Daten dauerhaft | Die Speisekammer – langsamerer Zugang, viel mehr Platz |
| **Eingabe/Ausgabe** | Tastatur, Maus, Bildschirm, Netzwerk | Wie der Koch Bestellungen entgegennimmt und Essen liefert |
| **GPU** (Grafikprozessor) | Spezialisierter Prozessor für parallele Aufgaben (Grafik, KI) | Ein Team von Assistenten, die alle gleichzeitig die gleiche Aufgabe erledigen |
**Wichtige Erkenntnis**: RAM ist schnell, aber temporär. Die Speicherung ist langsam, aber dauerhaft. Wenn sich Ihr Computer „langsam anfühlt“, liegt das häufig daran, dass ihm der Arbeitsspeicher ausgeht und er Speicher als temporären Speicher (Auslagerung) verwenden muss, was viel langsamer ist.
---

## Programmiersprachen – Mit Computern sprechen
Eine Programmiersprache ist eine Reihe von Anweisungen, die ein Computer ausführen kann. Verschiedene Sprachen werden für unterschiedliche Zwecke entwickelt. Eine detaillierte Abdeckung von 34 einzelnen Sprachen finden Sie im Ordner [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Sprache | Am besten für | Warum es wählen |
|----------|---------|---------------|
| **Python** | Datenwissenschaft, KI, Automatisierung, Web-Backends | Einfache Syntax; riesiges Ökosystem; ideal für Anfänger |
| **JavaScript** | Web-Frontends, Full-Stack (Node.js) | Läuft in jedem Browser; unverzichtbar für die Webentwicklung |
| **Java** | Unternehmenssoftware, Android-Apps | Plattformunabhängig (JVM); großes Ökosystem |
| **C/C++** | Systemprogrammierung, Spiele, eingebettet | Maximale Leistung; direkte Hardwaresteuerung |
| **Rost** | Systemprogrammierung mit Sicherheitsgarantien | Speichersicherheit ohne Garbage Collection |
| **Los** | Cloud-Dienste, Microservices, CLI-Tools | Einfach; ausgezeichnete Parallelität; schnelle Zusammenstellung |
| **SQL** | Datenbankabfragen | Die universelle Sprache für die Arbeit mit Daten |
| **TypeScript** | Große Webanwendungen | JavaScript mit Typprüfung; fängt Fehler frühzeitig ein |
---

## Wie das Internet funktioniert
Das Internet ist nicht dasselbe wie das Web. Das Internet ist das physische Netzwerk – Kabel, Router, Server und Protokolle, die Milliarden von Geräten verbinden. Das World Wide Web ist ein Dienst, der im Internet läuft (zusammen mit E-Mail, Dateiübertragung, Streaming, Spielen usw.).
### Der Weg einer Webanfrage
Wenn Sie`https://www.example.com`in Ihren Browser eingeben:
1. **DNS-Suche**: Ihr Browser fordert einen DNS-Server auf, „www.example.com“ in eine IP-Adresse (z. B. 93.184.216.34) zu übersetzen.
2. **TCP-Verbindung**: Ihr Gerät stellt über TCP (ein Protokoll, das eine zuverlässige Zustellung garantiert) eine Verbindung zu dieser IP-Adresse her.
3. **TLS-Handshake**: Bei Verwendung von HTTPS handeln Ihr Browser und der Server eine verschlüsselte Verbindung aus.
4. **HTTP-Anfrage**: Ihr Browser sendet eine Anfrage: „Gib mir die Seite unter /index.html.“
5. **Serververarbeitung**: Der Webserver findet die Seite, fragt möglicherweise eine Datenbank ab und bereitet eine Antwort vor.
6. **HTTP-Antwort**: Der Server sendet HTML, CSS und JavaScript zurück.
7. **Rendering**: Ihr Browser analysiert den HTML-Code, wendet CSS-Stile an und führt JavaScript aus, um die Seite anzuzeigen.
Dieser gesamte Vorgang dauert normalerweise weniger als eine Sekunde.
### Schlüsselprotokolle
| Protokoll | Was es tut | Schicht |
|----------|-------------|-------|
| **IP** (Internetprotokoll) | Leitet Pakete zwischen Netzwerken weiter | Netzwerk |
| **TCP** | Zuverlässige, geordnete Lieferung (überträgt verlorene Pakete erneut) | Transport |
| **UDP** | Schnelle, unzuverlässige Lieferung (keine erneute Übertragung) | Transport |
| **HTTP/HTTPS** | Webseitenübertragung (HTTPS fügt Verschlüsselung hinzu) | Bewerbung |
| **DNS** | Übersetzt Domänennamen in IP-Adressen | Bewerbung |
| **SSH** | Sicherer Fernzugriff auf Computer | Bewerbung |
| **SMTP/IMAP** | E-Mail-Versand und -Empfang | Bewerbung |
---

## Softwareentwicklung – Wie Programme erstellt werden
### Der Entwicklungsprozess
1. **Code schreiben**: Entwickler schreiben Anweisungen in einer Programmiersprache.
2. **Code testen**: Führen Sie den Code aus, um zu überprüfen, ob er ordnungsgemäß funktioniert.
3. **Versionskontrolle**: Verfolgen Sie Änderungen mit Git – dem universellen Standard.
4. **Überprüfung**: Andere Entwickler überprüfen den Code auf Fehler und Qualität.
5. **Build**: Quellcode in ein ausführbares Programm konvertieren (Kompilierung).
6. **Bereitstellen**: Geben Sie das Programm für Benutzer frei (Server, App-Stores usw.).
7. **Überwachen**: Achten Sie auf Fehler und Leistungsprobleme in der Produktion.
### Schlüsselkonzepte
| Konzept | Was es bedeutet | Warum es wichtig ist |
|---------|---------------|----------------|
| **Versionskontrolle (Git)** | Verfolgen Sie jede Änderung am Code im Laufe der Zeit | Zusammenarbeit; Fähigkeit, Fehler rückgängig zu machen |
| **API** (Anwendungsprogrammierschnittstelle) | Eine definierte Art und Weise für die Kommunikation von Softwarekomponenten | Ermöglicht die Zusammenarbeit verschiedener Systeme |
| **Datenbank** | Organisierte Speicherung von Daten | Jede Anwendung muss Daten speichern und abrufen |
| **Testen** | Automatisierte Überprüfung, ob der Code ordnungsgemäß funktioniert | Verhindert, dass Fehler Benutzer erreichen |
| **CI/CD** (Continuous Integration/Delivery) | Automatisierte Pipeline vom Code-Commit bis zur Produktion | Schnellere und sicherere Freigaben |
| **Containerisierung (Docker)** | Verpacken Sie eine Anwendung mit allen ihren Abhängigkeiten | „Funktioniert auf meinem Computer“ wird zu „Funktioniert überall“ |
---

## Datenbanken – Wo Daten leben
Jede Anwendung muss Daten speichern. Datenbanken sind die Systeme, die dies effizient und zuverlässig leisten.
| Geben Sie | ein Wie Daten gespeichert werden | Am besten für | Beispiele |
|------|-----|----------|---------|
| **Relational (SQL)** | Tabellen mit Zeilen und Spalten; strenges Schema | Strukturierte Daten; komplexe Abfragen; Transaktionen | PostgreSQL, MySQL, SQLite |
| **Dokument (NoSQL)** | JSON-ähnliche Dokumente; flexibles Schema | Halbstrukturierte Daten; schnelle Iteration | MongoDB, CouchDB |
| **Schlüsselwert** | Einfacher Schlüssel → Wertepaare | Caching; Sitzungsspeicher; schnelle Suchvorgänge | Redis, DynamoDB |
| **Grafik** | Knoten und Kanten (Beziehungen) | Soziale Netzwerke; Empfehlungsmaschinen | Neo4j, JanusGraph |
| **Zeitreihe** | Optimiert für zeitgestempelte Daten | Überwachung; Analytik; IoT | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) ist die Standardsprache für relationale Datenbanken. Es handelt sich um eine der wertvollsten technischen Fähigkeiten, die Sie erlernen können – fast jede Organisation verwendet Datenbanken, und mit SQL kommunizieren Sie mit ihnen.
---

## Betriebssysteme
Das Betriebssystem (OS) ist die Softwareschicht zwischen Ihnen (und Ihren Programmen) und der Hardware. Es verwaltet Speicher, Prozesse, Dateien und Geräte.
| Betriebssystem | Wo es dominiert | Hauptmerkmal |
|----|-----|-------------|
| **Windows** | Desktop-/Laptop-PCs (~72 % Marktanteil) | Größte Software-/Hardware-Kompatibilität |
| **macOS** | Kreativprofis, Entwickler | Unix-basiert; polierte Benutzeroberfläche; Apple-Ökosystem |
| **Linux** | Server (~96 %), Supercomputer (100 %), eingebettet, Entwickler | Open Source; frei; extrem anpassbar |
| **Android** | Mobil (~72 % globaler Marktanteil) | Basierend auf dem Linux-Kernel; Open Source |
| **iOS** | Mobil (~27 % weltweit, aber höherer Umsatz) | Geschlossenes Ökosystem; poliert; datenschutzorientiert |
Linux verdient besondere Erwähnung: Es unterstützt den Großteil des Internets, jeden Top-500-Supercomputer, den Großteil der Cloud-Infrastruktur und alle Android-Telefone. Es ist kostenlos, Open Source und wird von einer globalen Community gepflegt.
---

## Cloud Computing
Cloud Computing bedeutet, Rechenressourcen (Server, Speicher, Datenbanken usw.) über das Internet zu mieten, anstatt eigene Hardware zu kaufen und zu warten. Eine umfassende Anleitung zu Cloud-Architektur, Servicemodellen und Anbietervergleichen finden Sie unter[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Servicemodell | Was Sie bekommen | Analogie | Beispiele |
|---------------|-------------|---------|---------|
| **IaaS** (Infrastruktur) | Virtuelle Server, Speicher, Netzwerk | Ein Grundstück mieten und bauen, was Sie wollen | AWS EC2, Google Compute Engine |
| **PaaS** (Plattform) | Laufzeitumgebung; Du bringst Code mit | Eine möblierte Wohnung mieten | Heroku, Google App Engine |
| **SaaS** (Software) | Vollständige Bewerbung; du benutzt es einfach | Übernachten in einem Hotel | Gmail, Slack, Salesforce |
Die drei größten Cloud-Anbieter sind **AWS** (Amazon, ~32 % Marktanteil), **Azure** (Microsoft, ~23 %) und **GCP** (Google, ~10 %). Sie bieten Hunderte von Diensten in den Bereichen Rechenleistung, Speicher, Datenbanken, KI, Netzwerke und mehr.
---

## Cybersicherheit – Schutz digitaler Systeme
Unter Cybersicherheit versteht man den Schutz von Computern, Netzwerken und Daten vor Angriffen. Das ist wichtig, weil alles miteinander verbunden ist und die Kosten von Verstößen enorm sind. Eine vollständige Anleitung zu den Top 10 von OWASP, dem sicheren Entwicklungslebenszyklus und der Verwaltung von Geheimnissen finden Sie unter.
### Häufige Bedrohungen
| Bedrohung | Was es ist | Prävention |
|--------|-----------|------------|
| **Malware** | Schädliche Software (Viren, Würmer, Trojaner) | Antivirus; Software auf dem neuesten Stand halten |
| **Phishing** | Gefälschte E-Mails/Nachrichten, die Sie dazu verleiten, Informationen preiszugeben | Ausbildung; E-Mail-Filterung; Skepsis |
| **Ransomware** | Verschlüsselt Ihre Daten; verlangt Bezahlung des Schlüssels | Backups; Patch-Systeme; nicht bezahlen |
| **DDoS** | Überlastet einen Dienst mit Datenverkehr | Verkehrsfilterung; CDN-Schutz |
| **SQL-Injection** | Einfügen bösartiger SQL-Anweisungen in Eingabefelder | Parametrisierte Abfragen; Eingabevalidierung |
| **Mann-in-der-Mitte** | Abfangen der Kommunikation zwischen zwei Parteien | HTTPS/TLS-Verschlüsselung |
### Sicherheitsgrundlagen
- **Verschlüsselung**: Daten verschlüsseln, damit nur autorisierte Parteien sie lesen können. HTTPS verwendet TLS, um den Webverkehr zu verschlüsseln.
- **Authentifizierung**: Identität überprüfen. Verwenden Sie die Multi-Faktor-Authentifizierung (MFA) – Passwort + etwas anderes (Code, biometrisch).
- **Autorisierung**: Berechtigungen überprüfen. Nur weil Sie angemeldet sind, bedeutet das nicht, dass Sie auf alles zugreifen sollten.
- **Prinzip der geringsten Rechte**: Gewähren Sie Benutzern und Systemen nur den Zugriff, den sie benötigen, nicht mehr.
- **Patch-Management**: Halten Sie die Software auf dem neuesten Stand. Bei den meisten Verstößen werden bekannte Schwachstellen ausgenutzt, für die es bereits Patches gibt.
---

## Datenformate
Programme tauschen Daten in bestimmten Formaten aus. Am häufigsten:
| Formatieren | Struktur | Verwendet für |
|--------|-----------|----------|
| **JSON** | Schlüssel-Wert-Paare; für Menschen lesbar | APIs; Konfiguration; Datenaustausch |
| **XML** | Tag-basiert; ausführlich, aber flexibel | Legacy-Systeme; Unterlagen; SOAP-APIs |
| **YAML** | Einrückungsbasiert; sehr lesenswert | Konfiguration (Docker, Kubernetes, CI/CD) |
| **CSV** | Nur-Text-Zeilen und -Spalten | Datenimport/-export; Tabellenkalkulationen |
---

## Zusammenfassung
Informatik ist keine Zauberei – es ist Ingenieurskunst. Computer folgen Anweisungen mit unglaublicher Geschwindigkeit. Das Internet verbindet Milliarden von ihnen über standardisierte Protokolle. Software wird von Teams erstellt, die in iterativen Zyklen Code schreiben, testen und bereitstellen. Datenbanken speichern und rufen Daten ab. Mit Cloud Computing kann jeder bei Bedarf auf riesige Rechenressourcen zugreifen. Und bei der Cybersicherheit geht es darum, all dies vor Menschen zu schützen, die es ausnutzen wollen. Das Verständnis dieser Grundlagen hilft Ihnen, sich in der digitalen Welt zurechtzufinden – egal, ob Sie ein Benutzer, ein Entwickler oder einfach nur jemand sind, der versucht, die Technologie, die das moderne Leben prägt, zu verstehen.