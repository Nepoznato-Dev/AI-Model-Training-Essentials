# Referenz für Git-Befehle

Wichtige Git-Befehle für die Versionskontrolle.

---

## Einrichtung und Konfiguration

```bash
# Benutzerinformationen konfigurieren
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@beispiel.de"

# Konfiguration anzeigen
git config --list
git config user.name

# Standard-Branch-Namen festlegen
git config --global init.defaultBranch main
```

---

## Repository-Initialisierung

```bash
# Neues Repository initialisieren
git init

# Vorhandenes Repository klonen
git clone <url>
git clone <url> ordner-name

# Bestimmten Branch klonen
git clone -b branch-name <url>
```

---

## Grundlegender Workflow

```bash
# Status überprüfen
git status

# Änderungen anzeigen
git diff
git diff --staged

# Dateien zum Staging hinzufügen
git add datei.txt           # Bestimmte Datei
git add .                   # Alle Dateien
git add *.py                # Musterübereinstimmung

# Änderungen committen
git commit -m "Commit-Nachricht"
git commit -am "Nachricht"  # Stagen und committen verfolgter Dateien

# Commit-Historie anzeigen
git log
git log --oneline
git log --graph --oneline --all
```

---

## Branching

```bash
# Branches auflisten
git branch                  # Lokale Branches
git branch -a               # Alle Branches
git branch -r               # Remote-Branches

# Branch erstellen
git branch branch-name
git checkout -b branch-name # Erstellen und wechseln

# Branch wechseln
git checkout branch-name
git switch branch-name      # Neuere Syntax

# Aktuellen Branch umbenennen
git branch -m neuer-name

# Branch löschen
git branch -d branch-name   # Sicheres Löschen (gemerged)
git branch -D branch-name   # Erzwingen des Löschens

# Branch mergen
git merge branch-name

# Branch rebasen
git rebase main
```

---

## Remote-Operationen

```bash
# Remotes anzeigen
git remote -v

# Remote hinzufügen
git remote add origin <url>

# Von Remote holen
git fetch origin
git fetch --all

# Änderungen ziehen (fetch + merge)
git pull origin main
git pull --rebase origin main

# Änderungen pushen
git push origin main
git push -u origin main     # Upstream setzen
git push --force            # Force push (vorsichtig verwenden)
git push --force-with-lease # Sicherer Force push

# Tags pushen
git push --tags
```

---

## Änderungen rückgängig machen

```bash
# Datei unstagen (Änderungen behalten)
git reset HEAD datei.txt
git restore --staged datei.txt

# Arbeitsänderungen verwerfen
git checkout -- datei.txt
git restore datei.txt

# Letzten Commit ändern
git commit --amend -m "Neue Nachricht"
git commit --amend --no-edit

# Commit rückgängig machen (sicher für geteilte Repos)
git revert commit-hash

# Auf vorherigen Commit zurücksetzen
git reset --soft HEAD~1     # Änderungen gestaged behalten
git reset --mixed HEAD~1    # Änderungen ungestaged behalten (Standard)
git reset --hard HEAD~1     # Alle Änderungen verwerfen (gefährlich)
```

---

## Stashing

```bash
# Laufende Arbeit speichern
git stash
git stash save "Nachricht"

# Stashes auflisten
git stash list

# Stash anwenden
git stash apply             # Neuester
git stash apply stash@{1}   # Bestimmter Stash

# Anwenden und entfernen
git stash pop

# Stash verwerfen
git stash drop stash@{1}

# Alle Stashes löschen
git stash clear
```

---

## Tags

```bash
# Tags auflisten
git tag
git tag -l "v1.*"

# Tag erstellen
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # Annotierter Tag

# Tag auschecken
git checkout v1.0.0

# Tag löschen
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## Anzeige und Suche

```bash
# Commit-Details anzeigen
git show commit-hash
git show --stat commit-hash

# Blame (wer hat was geändert)
git blame datei.txt

# In Commits suchen
git log --grep="Schlüsselwort"
git log --author="Name"

# Code in Historie suchen
git log -S"funktionsname"

# Datei bei bestimmtem Commit anzeigen
git show commit-hash:datei.txt
```

---

## Erweiterte Operationen

```bash
# Cherry-pick Commit
git cherry-pick commit-hash

# Interaktives Rebase
git rebase -i HEAD~5

# Commits zusammenfassen (während Rebase)
# 'pick' zu 'squash' oder 's' im Editor ändern

# Patch erstellen
git format-patch -1 commit-hash

# Patch anwenden
git apply patch-datei.patch
git am patch-datei.patch

# Submodules
git submodule add <url> pfad
git submodule update --init --recursive
```

---

## Bereinigung

```bash
# Nicht verfolgte Dateien entfernen (Trockenlauf)
git clean -n
git clean -f                # Tatsächlich entfernen

# Nicht verfolgte Verzeichnisse entfernen
git clean -fd

# Gelöschte Remote-Branches bereinigen
git fetch --prune
git remote prune origin
```

---

## Häufige Workflows

### Neue Funktion starten
```bash
git checkout main
git pull
git checkout -b feature/neue-funktion
# ... arbeiten ...
git add .
git commit -m "Neue Funktion hinzufügen"
git push -u origin feature/neue-funktion
# PR/MR auf Plattform erstellen
```

### Mit Main synchronisieren
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Konflikte lösen falls nötig
git push --force-with-lease
```

### Hotfix-Workflow
```bash
git checkout main
git pull
git checkout -b hotfix/dringende-reparatur
# ... reparieren ...
git commit -am "Kritischen Fehler beheben"
git checkout main
git merge hotfix/dringende-reparatur
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore-Muster

```gitignore
# Bestimmte Datei ignorieren
dateiname.txt

# Alle .log-Dateien ignorieren
*.log

# Verzeichnis ignorieren
node_modules/
__pycache__/

# Negieren (trotz früherem Muster einschließen)
!important.log

# Kommentar
# Dies ist ein Kommentar
```

---

## Tastenkürzel (Git Bash)

| Kürzel | Aktion |
|----------|--------|
| `Ctrl+R` | Rückwärtssuche im Verlauf |
| `Tab` | Auto-Vervollständigung |
| `Ctrl+C` | Befehl abbrechen |
| `Ctrl+Z` | Prozess anhalten |
| `fg` | Angehaltenen Prozess fortsetzen |

---

## Best Practices

✅ **Empfohlen:**
- Klare, beschreibende Commit-Nachrichten schreiben
- Häufig mit logischen Gruppierungen committen
- Branches für Features/Fixes verwenden
- Vor Arbeitsbeginn pullen
- Oft `git status` überprüfen

❌ **Nicht empfohlen:**
- Sensible Daten committen (API-Schlüssel, Passwörter)
- Force push auf geteilte Branches
- Große Binärdateien committen
- Merge-Konflikte ignorieren
- Direkt auf main/master arbeiten

---

## Commit-Nachrichten-Konvention

```
typ(bereich): betreff

körper (optional)

fußzeile (optional)
```

**Typen:**
- `feat`: Neue Funktion
- `fix`: Fehlerbehebung
- `docs`: Dokumentation
- `style`: Formatierung
- `refactor`: Code-Umstrukturierung
- `test`: Tests
- `chore`: Wartung

**Beispiel:**
```
feat(auth): Passwort-Zurücksetzfunktion hinzufügen

Implementiere Passwort-Zurücksetzung per E-Mail mit
Token-basierter Verifizierung. Token läuft nach 24 Stunden ab.

Schließt #123
```

---

*Zuletzt aktualisiert: Juni 2025 | Git 2.x*
