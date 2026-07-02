# Git-Befehle Kurzübersicht

Wesentliche Git-Befehle für die Versionskontrolle.

---

## Einrichtung & Konfiguration

```bash
# Benutzerinformationen konfigurieren
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Konfiguration anzeigen
git config --list
git config user.name

# Standard-Branch-Namen festlegen
git config --global init.defaultBranch main
```

---

## Initialisierung eines Repositorys

```bash
# Neues Repository initialisieren
git init

# Vorhandenes Repository klonen
git clone <url>
git clone <url> folder-name

# Bestimmten Branch klonen
git clone -b branch-name <url>
```

---

## Grundlegender Workflow

```bash
# Status prüfen
git status

# Änderungen anzeigen
git diff
git diff --staged

# Dateien stagen
git add file.txt          # Bestimmte Datei
git add .                 # Alle Dateien
git add *.py              # Musterabgleich

# Änderungen committen
git commit -m "Commit message"
git commit -am "Message"  # Nachverfolgte Dateien stagen und committen

# Commit-Historie anzeigen
git log
git log --oneline
git log --graph --oneline --all
```

---

## Branching

```bash
# Branches auflisten
git branch                # Lokale Branches
git branch -a             # Alle Branches
git branch -r             # Remote-Branches

# Branch erstellen
git branch branch-name
git checkout -b branch-name   # Erstellen und wechseln

# Branches wechseln
git checkout branch-name
git switch branch-name        # Neuere Syntax

# Aktuellen Branch umbenennen
git branch -m new-name

# Branch löschen
git branch -d branch-name     # Sicher löschen (gemergt)
git branch -D branch-name     # Erzwingt das Löschen

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

# Vom Remote abrufen
git fetch origin
git fetch --all

# Änderungen ziehen (fetch + merge)
git pull origin main
git pull --rebase origin main

# Änderungen pushen
git push origin main
git push -u origin main     # Upstream setzen
git push --force            # Erzwingt Push (vorsichtig verwenden)
git push --force-with-lease # Sichererer Force Push

# Tags pushen
git push --tags
```

---

## Änderungen rückgängig machen

```bash
# Datei aus Staging entfernen (Änderungen behalten)
git reset HEAD file.txt
git restore --staged file.txt

# Arbeitsänderungen verwerfen
git checkout -- file.txt
git restore file.txt

# Letzten Commit ändern
git commit --amend -m "New message"
git commit --amend --no-edit

# Commit zurücknehmen (sicher für gemeinsam genutzte Repos)
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
git stash save "message"

# Stashes auflisten
git stash list

# Stash anwenden
git stash apply             # Neuester
git stash apply stash@{1}   # Bestimmter Stash

# Anwenden und entfernen
git stash pop

# Stash löschen
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

## Anzeigen & Suchen

```bash
# Commit-Details anzeigen
git show commit-hash
git show --stat commit-hash

# Blame (wer hat was geändert)
git blame file.txt

# Commits durchsuchen
git log --grep="keyword"
git log --author="name"

# Code in der Historie suchen
git log -S"function_name"

# Datei in bestimmtem Commit anzeigen
git show commit-hash:file.txt
```

---

## Erweiterte Operationen

```bash
# Commit cherry-picken
git cherry-pick commit-hash

# Interaktiver Rebase
git rebase -i HEAD~5

# Commits squashen (während des Rebase)
# 'pick' im Editor in 'squash' oder 's' ändern

# Patch erstellen
git format-patch -1 commit-hash

# Patch anwenden
git apply patch-file.patch
git am patch-file.patch

# Submodule
git submodule add <url> path
git submodule update --init --recursive
```

---

## Aufräumen

```bash
# Unversionierte Dateien entfernen (Probelauf)
git clean -n
git clean -f                # Tatsächlich entfernen

# Unversionierte Verzeichnisse entfernen
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
git checkout -b feature/new-feature
# ... arbeiten ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# PR/MR auf der Plattform erstellen
```

### Mit Main synchronisieren
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Konflikte auflösen, falls vorhanden
git push --force-with-lease
```

### Hotfix-Workflow
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... beheben ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore-Muster

```gitignore
# Bestimmte Datei ignorieren
filename.txt

# Alle .log-Dateien ignorieren
*.log

# Verzeichnis ignorieren
node_modules/
__pycache__/

# Negation (trotz früherem Muster einschließen)
!important.log

# Kommentar
# Dies ist ein Kommentar
```

---

## Tastenkombinationen (Git Bash)

| Shortcut | Aktion |
|----------|--------|
| `Ctrl+R` | Verlauf rückwärts durchsuchen |
| `Tab` | Automatisch vervollständigen |
| `Ctrl+C` | Befehl abbrechen |
| `Ctrl+Z` | Prozess anhalten |
| `fg` | Angehaltenen Prozess fortsetzen |

---

## Best Practices

✅ **Tun:**
- Schreiben Sie klare, aussagekräftige Commit-Nachrichten
- Committen Sie häufig mit logischen Gruppierungen
- Verwenden Sie Branches für Features/Fixes
- Ziehen Sie Änderungen, bevor Sie mit der Arbeit beginnen
- Prüfen Sie `git status` regelmäßig

❌ **Nicht tun:**
- Sensible Daten committen (API-Schlüssel, Passwörter)
- Force Push auf gemeinsam genutzte Branches ausführen
- Große Binärdateien committen
- Merge-Konflikte ignorieren
- Direkt auf main/master arbeiten

---

## Konvention für Commit-Nachrichten

```
type(scope): subject

body (optional)

footer (optional)
```

**Typen:**
- `feat`: Neues Feature
- `fix`: Fehlerbehebung
- `docs`: Dokumentation
- `style`: Formatierung
- `refactor`: Umstrukturierung von Code
- `test`: Tests
- `chore`: Wartung

**Beispiel:**
```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*Zuletzt aktualisiert: Juni 2025 | Git 2.x*
