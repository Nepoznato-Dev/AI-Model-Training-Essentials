---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cybersecurity, coding-and-technology]
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

# Grundlagen der Cybersicherheit
Sicherheit ist eine Disziplin, die von Anfang an in jede Schicht eines Systems integriert werden muss und nicht erst nachträglich hinzugefügt werden darf. Ganz gleich, ob Sie eine Webanwendung erstellen, die Infrastruktur verwalten oder eine API bereitstellen: Das Verständnis der Bedrohungslandschaft und der Grundlagen der Verteidigung ist von entscheidender Bedeutung.
---

## Verschlüsselung und Kryptographie
### Symmetrische vs. asymmetrische Verschlüsselung
| Geben Sie | ein Wie es funktioniert | Geschwindigkeit | Schlüsselverteilung | Beispiele |
|------|-------------|-------|-----------------|----------|
| **Symmetrisch** | Gleicher Schlüssel für Verschlüsselung und Entschlüsselung | Schnell | Herausforderung: Wie teilt man den Schlüssel? | AES-256, ChaCha20 |
| **Asymmetrisch** | Öffentlicher Schlüssel verschlüsselt, privater Schlüssel entschlüsselt | Langsamer | Öffentlicher Schlüssel kann offen geteilt werden | RSA, ECC (Elliptische Kurve) |
In der Praxis verwenden die meisten Systeme **beides**: asymmetrische Verschlüsselung, um einen symmetrischen Schlüssel sicher auszutauschen, und dann symmetrische Verschlüsselung für den Großteil der Daten. So funktioniert TLS/HTTPS.
### Hashing
Hashing ist eine Einwegfunktion: Es wandelt Eingaben in eine Zeichenfolge fester Größe um. Man kann es nicht umkehren, aber die gleiche Eingabe erzeugt immer die gleiche Ausgabe.
| Anwendungsfall | Empfohlener Algorithmus | Vermeiden |
|----------|-------|-------|
| **Passwortspeicher** | Argon2id, bcrypt, scrypt | MD5, SHA-1, einfaches SHA-256 (zu schnell) |
| **Datenintegrität** | SHA-256, SHA-3 | MD5 (defekt), SHA-1 (defekt) |
| **Digitale Signaturen** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS ist HTTP über TLS (Transport Layer Security). Es bietet:
- **Verschlüsselung**: Daten während der Übertragung können nicht von Abhörern gelesen werden.
- **Authentifizierung**: Der Server weist seine Identität über ein Zertifikat nach.
- **Integrität**: Daten können während der Übertragung nicht unbemerkt geändert werden.
Verwenden Sie TLS 1.2 oder 1.3. Deaktivieren Sie TLS 1.0 und 1.1. Aktivieren Sie HSTS (HTTP Strict Transport Security), um Browser zu zwingen, immer HTTPS zu verwenden.
---

## Authentifizierung und Autorisierung
### Authentifizierung: Wer sind Sie?
| Methode | Sicherheitsstufe | Anwendungsfall |
|--------|---------------|----------|
| **Passwort** | Niedrig–Mittel | Basiskonten (mehr als 12 Zeichen erzwingen, auf Verstöße prüfen) |
| **MFA (TOTP)** | Hoch | Standard für sensible Konten (Google Authenticator, Authy) |
| **Hardwareschlüssel (FIDO2/WebAuthn)** | Sehr hoch | Hochsicherheitskonten (YubiKey) |
| **Biometrisch** | Mittel–Hoch | Geräteentsperrung (Fingerabdruck, Gesicht) – als einziger Faktor nicht besonders gut |
| **OAuth2 / OIDC** | Hoch | Drittanbieter-Login („Mit Google anmelden“) |
**Passwortregeln**: Erzwingen Sie eine Mindestlänge (12–16 Zeichen), prüfen Sie anhand von Listen mit verletzten Passwörtern, verwenden Sie Argon2id oder bcrypt für das Hashing mit Salts pro Benutzer.
### Autorisierung: Was können Sie tun?
| Modell | Beschreibung | Beispiel |
|-------|-------------|---------|
| **RBAC** (Rollenbasierte Zugriffskontrolle) | Rollen zugewiesene Berechtigungen; Benutzer erhalten Rollen | Admin, Redakteur, Betrachter |
| **ABAC** (attributbasiert) | Regeln basierend auf Benutzerattributen, Ressourcen, Umgebung | „Manager können die Anfragen ihres Teams genehmigen“ |
| **ACL** (Zugriffskontrollliste) | Explizite Berechtigungen pro Benutzer/Ressource | Dateiberechtigungen (Lesen/Schreiben/Ausführen) |
**Prinzip der geringsten Rechte**: Gewähren Sie jedem Benutzer, Dienst und Prozess nur den minimalen Zugriff, den er benötigt.
### JWT (JSON-Web-Tokens)
| Aspekt | Empfehlung |
|--------|---------------|
| **Signieren** | RS256 oder ES256 (asymmetrisch) bevorzugt; HS256 akzeptabel mit verwalteten Geheimnissen |
| **Ablauf** | 15–60 Minuten für Zugangstoken; Verwenden Sie Aktualisierungstoken für längere Sitzungen |
| **Speicher** | Nur HTTP-Cookies (nicht localStorage – anfällig für XSS) |
| **Validierung** | Überprüfen Sie stets Signatur, Aussteller, Zielgruppe und Ablaufdatum |
---

## OWASP Top 10 (2021)
Die OWASP Top 10 sind das Standarddokument zur Sensibilisierung für die Sicherheit von Webanwendungen. Es stellt die kritischsten Risiken dar:
| # | Risiko | Was es bedeutet |
|---|------|--------------|
| 1 | **Defekte Zugriffskontrolle** | Benutzer können auf Ressourcen zugreifen, für die sie keinen Zugriff haben |
| 2 | **Kryptografische Fehler** | Schwache oder fehlende Verschlüsselung sensibler Daten |
| 3 | **Injektion** | SQL-, NoSQL-, OS-Befehls- oder LDAP-Injection |
| 4 | **Unsicheres Design** | Architekturmängel, die durch Implementierung nicht behoben werden können |
| 5 | **Sicherheitsfehlkonfiguration** | Standardkennwörter, offene Ports, ausführliche Fehlermeldungen |
| 6 | **Gefährdete Komponenten** | Bekannte CVEs in Abhängigkeiten |
| 7 | **Authentifizierungsfehler** | Schwache Passwörter, Missmanagement von Sitzungen |
| 8 | **Integritätsfehler** | Angriffe auf die Lieferkette, nicht signierte Updates |
| 9 | **Protokollierungs-/Überwachungsfehler** | Keine Feststellung von Verstößen |
| 10 | **SSRF** | Server wurde dazu verleitet, Anfragen an interne Systeme zu stellen |
---

## Sichere Codierungspraktiken
### Eingabevalidierung
| Regel | Warum |
|------|-----|
| **Whitelist > Blacklist** | Definieren Sie, was erlaubt ist und nicht, was blockiert ist |
| **Parametrisierte Abfragen** | Verketten Sie niemals Benutzereingaben in SQL – verwenden Sie vorbereitete Anweisungen oder ORM |
| **HTML-Kodierung** | Codieren Sie `<`, `>`, `&`, `"`, `'`, um XSS zu verhindern
| **Shell entkommt** | Vermeiden Sie es, Shell-Befehle aus Benutzereingaben zu erstellen. verwenden Sie`shlex.quote()`|
| **Längenbeschränkungen** | Erzwingen Sie maximale Längen, um Pufferüberläufe und DoS zu verhindern
| **Typprüfung** | Stellen Sie sicher, dass ganze Zahlen ganze Zahlen und boolesche Werte boolesche Werte sind |
### Häufige Schwachstellen
| Sicherheitslücke | Angriff | Verteidigung |
|--------------|--------|---------|
| **SQL-Injection** | `' OR 1=1 --`im Anmeldeformular | Parametrisierte Abfragen |
| **XSS** | `<script>alert('hacked')</script>`im Kommentarfeld | Ausgabekodierung, Inhaltssicherheitsrichtlinie |
| **CSRF** | Den Browser des Benutzers dazu verleiten, nicht autorisierte Anfragen zu stellen | CSRF-Tokens, SameSite-Cookies |
| **Pfadüberquerung** | `../../etc/passwd`im Dateiparameter | Dateipfade validieren und bereinigen |
| **IDOR** | Ändern Sie`/user/123`in `/user/124`, um die Daten einer anderen Person anzuzeigen | Berechtigungsprüfung bei jeder Anfrage |
---

## Netzwerksicherheit
### Firewalls
| Geben Sie | ein Beschreibung |
|------|-------------|
| **Paketfilterung** | Regeln basierend auf IP, Port, Protokoll |
| **Zustandsbehaftet** | Verfolgt den Verbindungsstatus; intelligentere Filterung |
| **Anwendungsebene (WAF)** | Überprüft den HTTP-Verkehr; blockiert SQL-Injection, XSS usw. |
| **Cloud-Sicherheitsgruppen** | Virtuelle Firewalls für Cloud-Instanzen (AWS SGs, Azure NSGs) |
**Faustregel**: Blockieren Sie standardmäßig den gesamten eingehenden Datenverkehr. Öffnen Sie nur das, was ausdrücklich benötigt wird (80, 443 für das Web).
### Netzwerksegmentierung
Platzieren Sie Datenbanken und Caches in privaten Subnetzen ohne direkten Internetzugang. Verwenden Sie eine DMZ für öffentlich zugängliche Dienste (Webserver, Load Balancer). Wenden Sie beim Netzwerkzugriff das Prinzip der geringsten Rechte an.
---

## Geheimnismanagement
### Die goldene Regel
**Kodieren Sie niemals Geheimnisse fest.** Keine API-Schlüssel, Passwörter oder Datenbank-URLs im Quellcode. Keine Geheimnisse in Umgebungsvariablen, die an Git übergeben wurden. Keine Geheimnisse in Docker-Images.
### Werkzeuge
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **HashiCorp-Tresor** | Manager für Unternehmensgeheimnisse | Dynamische Geheimnisse, Verschlüsselung als Service |
| **AWS Secrets Manager** | Cloud-nativ | AWS-Umgebungen |
| **Azure Key Vault** | Cloud-nativ | Azure-Umgebungen |
| **SOPS** | Verschlüsselte Dateien | Geheimnisse in Git verschlüsseln (mit KMS oder GPG) |
| **Docker-Geheimnisse** | Containernativ | Docker Swarm (für K8s siehe Secrets Store CSI) |
| **dotenv (.env)** | Lokale Entwicklung | Nur Entwicklung – nie in Produktion oder festgeschrieben |
### Rotation
Rotieren Sie Geheimnisse regelmäßig und automatisch. Wenn ein Geheimnis durchgesickert ist (z. B. an ein öffentliches Repo übergeben), rotieren Sie es sofort – auch wenn Sie glauben, dass es niemand gesehen hat.
---

## Abhängigkeitssicherheit
Ihre Anwendung ist nur so sicher wie ihre schwächste Abhängigkeit.
### Scan-Tools
| Sprache | Werkzeuge |
|----------|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Rost** | `cargo audit`|
| **Los** | `govulncheck`|
| **Allgemein** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Integrität der Lieferkette
- Verwenden Sie Sperrdateien (`package-lock.json`, `Cargo.lock`, `go.sum`) für reproduzierbare Builds.
- Überprüfen Sie die Prüfsummen der heruntergeladenen Abhängigkeiten.
- Bevorzugen Sie offizielle Register und verifizierte Herausgeber.
- Automatisieren Sie kleinere/Patch-Updates über Dependabot oder Renovate.
---

## Sicherheitsentwicklungslebenszyklus (SDL)
| Phase | Aktivität |
|-------|----------|
| **Schulung** | Stellen Sie sicher, dass Entwickler häufige Schwachstellen verstehen |
| **Bedrohungsmodellierung** | Identifizieren Sie potenzielle Bedrohungen während des Entwurfs |
| **Sichere Codierungsstandards** | Durchsetzung über Linters und Code-Review-Checklisten |
| **SAST** | Statische Analyse des Quellcodes (SonarQube, CodeQL) |
| **DAST** | Dynamische Analyse laufender Anwendungen (OWASP ZAP, Burp Suite) |
| **SCA** | Analyse der Softwarezusammensetzung – Abhängigkeiten scannen |
| **Penetrationstests** | Regelmäßige ethische Hacking-Übungen |
| **Bug Bounty** | Ermutigen Sie externe Forscher, Schwachstellen zu finden |
| **Vorfallreaktionsplan** | Haben Sie einen klaren Plan für den Fall, dass ein Verstoß festgestellt wird |
---

## Notfall-Checkliste
Wenn Sie einen Verstoß vermuten:
1. **Keine Panik** – aber handeln Sie schnell.
2. **Isolieren** betroffene Systeme (trennen Sie ggf. die Verbindung zum Netzwerk).
3. **Beweise sichern**: Protokolle, Speicherauszüge und Disk-Images erfassen.
4. **Umfang identifizieren**: Welche Systeme, welche Daten?
5. **Rotieren** Sie alle kompromittierten Anmeldeinformationen und Geheimnisse.
6. **Patchen** Sie die Schwachstelle.
7. **Benachrichtigen** Sie betroffene Benutzer und Regulierungsbehörden bei Bedarf (innerhalb der gesetzlichen Fristen).
8. **Post-Mortem**: Dokumentieren Sie die Grundursache und die Maßnahmen innerhalb von 24–48 Stunden.