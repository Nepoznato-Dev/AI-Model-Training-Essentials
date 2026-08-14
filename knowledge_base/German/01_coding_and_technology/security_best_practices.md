<!--
---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Best Practices für die Sicherheit
Ein praktischer Leitfaden zur Sicherung von Anwendungen, Infrastruktur und Daten – von der Entwicklung bis zur Produktion.
---

## OWASP Top 10 (2021) – Übersicht
1. **Defekte Zugriffskontrolle**: Benutzer können auf Ressourcen zugreifen, die sie nicht haben sollten.
2. **Kryptografische Fehler**: Schwache oder fehlende Verschlüsselung.
3. **Injektion**: SQL-, NoSQL-, OS-Befehls- oder LDAP-Injektion.
4. **Unsicheres Design**: Architekturmängel.
5. **Sicherheitsfehlkonfiguration**: Standardkennwörter, offene Ports, ausführliche Fehler.
6. **Anfällige und veraltete Komponenten**: Bekannte CVEs in Abhängigkeiten.
7. **Identifizierungs- und Authentifizierungsfehler**: Schwache Passwörter, schlechte Sitzungsverwaltung.
8. **Software- und Datenintegritätsfehler**: Angriffe auf die Lieferkette, nicht signierte Updates.
9. **Sicherheitsprotokollierungs- und Überwachungsfehler**: Keine Erkennung von Verstößen.
10. **Server-Side Request Forgery (SSRF)**: Missbrauch des Servers, um Anfragen an interne Systeme zu stellen.
---

## Eingabevalidierung und Ausgabekodierung
### Validierungsregeln
- **Whitelist > Blacklist**: Definieren Sie zulässige Muster (z. B. Regex für E-Mail), anstatt bekannte fehlerhafte Muster zu blockieren.
- **Längenbeschränkungen**: Erzwingen Sie maximale Längen, um Pufferüberläufe und DoS zu verhindern.
- **Typprüfung**: Stellen Sie sicher, dass Ganzzahlen Ganzzahlen und Boolesche Werte sind.
- **Verwenden Sie gut getestete Bibliotheken**: Verwenden Sie für die E-Mail-, URL- und Datumsvalidierung Standardbibliotheken (z. B.`email-validator`in Python,`validator.js`in Node).
### Ausgabekodierung
- **HTML-Codierung**: Codieren Sie `<`, `>`, `&`, `"`, `'`, um XSS zu verhindern.
- **SQL-Parametrierung**: Verketten Sie niemals Benutzereingaben in SQL-Abfragen. Verwenden Sie parametrisierte Abfragen (vorbereitete Anweisungen) oder ein ORM.
- **Shell-Escape**: Vermeiden Sie das Erstellen von Shell-Befehlen aus Benutzereingaben; Wenn dies unvermeidlich ist, verwenden Sie`shlex.quote()`oder ähnliches.
---

## Authentifizierung und Autorisierung
### Passwortverwaltung
- **Hashing**: Speichern Sie Passwörter mit einem starken, langsamen Hashing-Algorithmus: **Argon2id** (bevorzugt), **bcrypt**, **scrypt** oder **PBKDF2**.
- **Salzen**: Fügen Sie ein einzigartiges Salz pro Benutzer hinzu.
- **Mindestlänge**: Erzwingen Sie mindestens 12–16 Zeichen.
- **MFA (Multi-Faktor-Authentifizierung)**: Für sensible Vorgänge ist ein zweiter Faktor (TOTP, SMS, Hardwareschlüssel) erforderlich.
- **Ratenbegrenzung**: Verhindern Sie Brute-Force-Versuche an Anmeldeendpunkten (z. B. 5 Versuche pro 5 Minuten pro IP/Benutzer).
### Sitzungsverwaltung
- Verwenden Sie sichere, reine HTTP-SameSite-Cookies für Sitzungstoken.
- Legen Sie angemessene Ablaufzeiten fest.
- Sitzungen beim Abmelden und bei Passwortänderung ungültig machen.
– Vermeiden Sie die Offenlegung von Sitzungs-IDs in URLs.
### OAuth2 / OIDC
- Verwenden Sie etablierte Bibliotheken (z. B. Authlib, PyJWT, Passport.js, Spring Security).
- Validieren Sie ID-Tokens gründlich (Signatur, Aussteller, Zielgruppe, Ablauf).
- Verwenden Sie Statusparameter, um CSRF zu verhindern.
- Behandeln Sie Kundengeheimnisse vertraulich.
### JWT (JSON-Web-Tokens)
- **Signieren**: Verwenden Sie RS256 oder ES256 (asymmetrisch) für bessere Sicherheit; HS256 (symmetrisch) ist akzeptabel, wenn gemeinsame Geheimnisse gut verwaltet werden.
- **Validieren**: Überprüfen Sie immer Signatur, Aussteller (`iss`), Zielgruppe (`aud`) und Ablaufdatum (`exp`).
- **Kurzes Ablaufdatum beibehalten**: 15–60 Minuten für Zugriffstoken; Verwenden Sie Aktualisierungstoken für längere Sitzungen.
- **Sicher speichern**: Speichern Sie JWTs niemals in localStorage (anfällig für XSS); Verwenden Sie stattdessen reine HTTP-Cookies.
---

## API-Sicherheit
### Authentifizierung
- API-Aufrufe immer authentifizieren (außer öffentliche Endpunkte).
- Bevorzugen Sie API-Schlüssel oder OAuth2-Token gegenüber der Basisauthentifizierung (die bei jeder Anfrage Anmeldeinformationen sendet).
### Ratenbegrenzung und -drosselung
- Wenden Sie Ratenbegrenzungen pro Benutzer und pro IP an, um Missbrauch und DoS zu verhindern.
– Geben Sie`429 Too Many Requests`mit einem `Retry-After`-Header zurück.
### CORS (Cross-Origin Resource Sharing)
- Nur bestimmte Ursprünge zulassen (niemals`*`in der Produktion).
– Validieren Sie den Header`Origin`auf der Serverseite.
### Eingabevalidierung
- Validieren Sie alle Anforderungsparameter, einschließlich Header und Text.
- Unerwartete Felder ablehnen (`"strict": true`oder`additionalProperties: false`im JSON-Schema).
### HTTPS / TLS
- Erzwingen Sie HTTPS in der Produktion.
- Verwenden Sie HSTS (HTTP Strict Transport Security), um Browser zur Verwendung von HTTPS zu zwingen.
- Verwenden Sie TLS 1.2 oder 1.3 (deaktivieren Sie TLS 1.0/1.1).
---

## Geheimnismanagement
### Kodieren Sie niemals Geheimnisse fest
- Übergeben Sie keine Geheimnisse (API-Schlüssel, Passwörter, Datenbank-URLs) an die Quellcodeverwaltung.
- Verwenden Sie Umgebungsvariablen oder Secret-Management-Tools.
### Werkzeuge
| Werkzeug | Beschreibung |
|------|-------------|
| **HashiCorp-Tresor** | Dynamische Geheimnisse der Enterprise-Klasse |
| **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** | Cloud-nativ |
| **SOPS** | Geheimnisse in Dateien verschlüsseln und festschreiben (mit KMS oder GPG) |
| **Docker-Geheimnisse** | Für den Schwarmmodus; Kubernetes-Geheimnisse (externen Secrets Store-CSI-Treiber in Betracht ziehen) |
### Rotation
- Wechseln Sie regelmäßig Geheimnisse und Dienstkonten.
- Automatisieren Sie die Rotation nach Möglichkeit.
---

## Abhängigkeitsmanagement
### Schwachstellenscan
| Sprache/Plattform | Werkzeuge |
|-----|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Knoten** | `npm audit`,`yarn audit`,`snyk`|
| **Rost** | `cargo audit`|
| **Los** | `govulncheck`|
| **Allgemein** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Patchen
- Halten Sie Abhängigkeiten auf dem neuesten Stand und achten Sie auf gepatchte Versionen.
- Richten Sie automatisierte Pull-Anfragen für kleinere/Patch-Updates ein.
- Überprüfen Sie die Änderungsprotokolle auf wichtige Änderungen.
### Integrität der Lieferkette
– Verwenden Sie Paketsperrdateien (`package-lock.json`,`Cargo.lock`,`go.sum`), um reproduzierbare Builds sicherzustellen.
- Überprüfen Sie die Prüfsummen der heruntergeladenen Abhängigkeiten.
- Bevorzugen Sie offizielle Register und vertrauen Sie nur verifizierten Herausgebern.
---

## Infrastruktursicherheit
### Firewalls
- Blockieren Sie alle eingehenden Ports außer den explizit benötigten (z. B. 80, 443).
- Beschränken Sie den SSH-Zugriff auf bestimmte IP-Bereiche (oder verwenden Sie einen VPN/Bastion-Host).
- Verwenden Sie Sicherheitsgruppen (AWS) oder NSGs (Azure) für eine differenzierte Kontrolle.
### OS-Härtung
- Wenden Sie regelmäßig Sicherheitsupdates an (`sudo apt upgrade`,`yum update`).
- Deaktivieren Sie unnötige Dienste und Standardkonten.
- Verwenden Sie fail2ban, um Brute-Force-Versuche auf SSH zu blockieren.
- SSH härten: Root-Anmeldung deaktivieren, schlüsselbasierte Authentifizierung verwenden, Standardport ändern (optional).
### Netzwerksegmentierung
- Platzieren Sie Datenbanken und Caches in privaten Subnetzen ohne Internetzugang.
- Verwenden Sie eine DMZ für öffentlich zugängliche Dienste.
- Wenden Sie beim Netzwerkzugriff das Prinzip der geringsten Rechte an.
### Geheimnisse in der Infrastruktur
- Speichern Sie niemals Geheimnisse in CI/CD-Umgebungsvariablen, es sei denn, sie sind verschlüsselt.
– Verwenden Sie die IAM-Rollen des Cloud-Anbieters für EC2/VM-Instanzen anstelle langlebiger Schlüssel.
---

## Protokollierung und Überwachung
### Was protokolliert werden soll
- Authentifizierungsereignisse (Erfolg/Fehler).
- Entscheidungen zur Zugangskontrolle (Berechtigungsfehler).
- Admin-Aktionen (Benutzererstellung, Löschung, Berechtigungsänderungen).
- Änderungen des Datenbankschemas.
- Systemfehler und Ausnahmen.
- API-Anfragen und -Antworten (Sensible Daten redigieren).
### Was Sie nicht protokollieren sollten
- Passwörter, Geheimnisse, Token, PII (persönlich identifizierbare Informationen), sofern nicht gehasht/geschwärzt.
- Vollständige Kreditkartennummern.
### Alarmierung
- Richten Sie Benachrichtigungen ein für:
  - Mehrere fehlgeschlagene Anmeldungen (potenzielle Brute-Force-Anmeldung).
  - Ungewöhnliche Zugriffsmuster (z. B. von neuen Standorten aus, zu ungeraden Zeiten).
  - Neue Administratorkonten erstellt.
  - Hohe Fehlerraten oder Latenzspitzen.
- Verwenden Sie ein SIEM (Security Information and Event Management) für eine erweiterte Korrelation.
### Protokollaufbewahrung
- Bewahren Sie Protokolle je nach gesetzlichen Anforderungen mindestens 30–90 Tage lang auf.
- Speichern Sie Protokolle in einem zentralen, manipulationssicheren System (z. B. ELK Stack, Splunk, Datadog).
---

## Sicherer Entwicklungslebenszyklus (SDL)
1. **Schulung**: Stellen Sie sicher, dass Entwickler häufige Schwachstellen verstehen.
2. **Bedrohungsmodellierung**: Identifizieren Sie potenzielle Bedrohungen frühzeitig im Design.
3. **Sichere Codierungsstandards**: Durchsetzung über Linters und Code-Review-Checklisten.
4. **SAST** (Static Application Security Testing): Scannen Sie den Quellcode auf Schwachstellen (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): Laufende Anwendungen scannen (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Abhängigkeiten scannen.
7. **Penetrationstests**: Regelmäßige ethische Hacking-Übungen.
8. **Bug Bounty**: Ermutigen Sie externe Forscher, Schwachstellen verantwortungsvoll zu finden.
9. **Plan zur Reaktion auf Vorfälle**: Erstellen Sie einen klaren Plan für den Fall, dass ein Verstoß festgestellt wird.
---

## Notfall-Checkliste (bei Verdacht auf einen Verstoß)
1. **Keine Panik** – aber handeln Sie schnell.
2. **Isolieren** Sie die betroffenen Systeme (trennen Sie bei Bedarf die Verbindung zum Netzwerk).
3. **Beweise sichern**: Erfassen Sie Protokolle, Speicherauszüge und Festplatten-Images.
4. **Identifizieren** Sie den Umfang: welche Systeme, welche Daten.
5. **Rotieren** Sie alle kompromittierten Anmeldeinformationen und Geheimnisse.
6. **Patchen** Sie die Schwachstelle.
7. **Benachrichtigen** Sie bei Bedarf betroffene Benutzer und Aufsichtsbehörden (innerhalb der gesetzlichen Fristen).
8. **Führen Sie eine Obduktion durch**, um die Grundursache zu verstehen und Prozesse zu verbessern.