<!-- 
This file was automatically translated from English to German.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Tool-Nutzung

## Git — Versionskontrolle

Git ist ein verteiltes Versionskontrollsystem. Jeder Entwickler hat eine vollständige Kopie der Repository-Historie auf seinem lokalen Rechner.

### Kern-Workflow

```bash
# Ein neues Repository initialisieren
git init

# Ein bestehendes Repository klonen
git clone https://github.com/owner/repo.git

# Status und aktuelle Historie prüfen
git status
git log --oneline -10

# Änderungen stagen
git add file.py            # eine bestimmte Datei stagen
git add .                  # alle Änderungen im Arbeitsverzeichnis stagen

# Committen
git commit -m "Kurze, imperativische Beschreibung der Änderung"

# Zu einem Remote pushen
git push origin main
```

### Branching

```bash
git branch feature/new-thing        # einen Branch erstellen
git checkout feature/new-thing      # dorthin wechseln
# Abkürzung: git checkout -b feature/new-thing

git branch -d feature/new-thing     # Branch nach dem Mergen löschen
```

### Merging und Rebasing

```bash
# Feature-Branch in main mergen
git checkout main
git merge feature/new-thing

# Rebase hält eine lineare Historie
git checkout feature/new-thing
git rebase main
```

### Pull-Request (PR)-Workflow

1. Erstelle einen Feature-Branch von `main`.
2. Mache Commits auf dem Feature-Branch.
3. Pushe den Branch: `git push origin feature/new-thing`.
4. Öffne einen Pull Request auf GitHub / GitLab.
5. Adressiere Code-Review-Feedback mit zusätzlichen Commits.
6. Merge den PR, sobald er genehmigt wurde.

### Änderungen rückgängig machen

```bash
git restore file.py            # unstaged Änderungen verwerfen
git restore --staged file.py   # eine Datei unstagen
git revert <commit-sha>        # erstellt einen neuen Commit, der einen vorherigen rückgängig macht
git reset --soft HEAD~1        # letzten Commit rückgängig machen, Änderungen gestaged lassen
```

---

## Paketmanager

### pip (Python)

```bash
pip install requests            # ein Paket installieren
pip install "requests>=2.28"    # mit Versionsbeschränkung
pip install -r requirements.txt # aus einer Datei installieren
pip uninstall requests
pip list                        # installierte Pakete anzeigen
pip show requests               # Informationen über ein Paket
```

Arbeite immer in einer virtuellen Umgebung, um Projektabhängigkeiten isoliert zu halten.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # package.json erstellen
npm install express             # als Runtime-Abhängigkeit installieren
npm install --save-dev jest     # als Entwicklungsabhängigkeit installieren
npm uninstall express
npm update
npm run test                    # das "test"-Skript aus package.json ausführen
npm run build
npx create-react-app my-app     # ein Paket ausführen, ohne es global zu installieren
```

`package-lock.json` erfasst exakte Versionen; commite es zur Quellcodeverwaltung.

### Cargo (Rust)

```bash
cargo new my_project            # neues Binary-Projekt
cargo new --lib my_lib          # neues Bibliotheksprojekt
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # Linten
cargo fmt                       # Formatieren
cargo update                    # Abhängigkeiten innerhalb der Beschränkungen aktualisieren
```

### Go Modules (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # ungenutzte Abhängigkeiten entfernen
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)

```bash
sudo apt update                 # Paketlisten aktualisieren
sudo apt install git curl wget  # Pakete installieren
sudo apt remove package-name
sudo apt upgrade                # alle installierten Pakete aktualisieren
apt search keyword              # nach Paketen suchen
apt show package-name           # Details über ein Paket
```

---

## Kommandozeilen-Grundlagen

### Navigation

```bash
pwd                             # aktuelles Verzeichnis ausgeben
ls                              # Verzeichnisinhalt auflisten
ls -la                          # detaillierte Auflistung einschließlich versteckter Dateien
cd /path/to/dir                 # Verzeichnis wechseln
cd ..                           # eine Ebene nach oben gehen
cd ~                            # zum Home-Verzeichnis gehen
mkdir new_folder
rm file.txt                     # eine Datei löschen
rm -r folder/                   # ein Verzeichnis rekursiv löschen
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### Textverarbeitung

```bash
cat file.txt                    # Dateiinhalte ausgeben
less file.txt                   # durch eine Datei scrollen
head -n 20 file.txt             # erste 20 Zeilen
tail -n 20 file.txt             # letzte 20 Zeilen
tail -f log.txt                 # einer wachsenden Logdatei folgen
grep "pattern" file.txt         # nach einem Muster suchen
grep -r "pattern" ./src/        # rekursive Suche
grep -i "pattern" file.txt      # case-insensitive
```

### Pipes und Umleitung

```bash
command1 | command2             # Ausgabe von command1 in command2 leiten
ls -la | grep ".py"             # nur Python-Dateien auflisten
cat file.txt | wc -l            # Zeilen zählen
command > output.txt            # stdout in eine Datei umleiten (überschreiben)
command >> output.txt           # stdout an eine Datei anhängen
command 2>&1                    # stderr in stdout zusammenführen
```

### Netzwerk und Dateiübertragung

```bash
curl https://example.com                     # eine URL abrufen
curl -o file.zip https://example.com/f.zip   # in eine Datei herunterladen
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # mit wget herunterladen
```

### Berechtigungen

```bash
chmod +x script.sh              # ausführbar machen
chmod 644 file.txt              # Owner lesen/schreiben, Gruppe/andere lesen
chown user:group file.txt       # Owner und Gruppe ändern
```

### Prozessverwaltung

```bash
ps aux                          # laufende Prozesse auflisten
kill <PID>                      # SIGTERM an einen Prozess senden
kill -9 <PID>                   # gewaltsam beenden
top / htop                      # interaktiver Prozessmonitor
```

---

## Editoren und IDEs

### VS Code

VS Code ist ein leichter, plattformübergreifender Code-Editor mit einem reichen Erweiterungsökosystem.

- Ordner öffnen: `File > Open Folder` oder `code .` im Terminal.
- Befehlspalette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Integriertes Terminal: `Ctrl+`` (Backtick)`.
- Multi-Cursor: `Alt+Click`, um zusätzliche Cursor zu platzieren.
- Zur Definition gehen: `F12`.
- Symbol umbenennen: `F2`.
- Dokument formatieren: `Shift+Alt+F`.
- Erweiterungen: Installiere Sprachunterstützung (Python, Rust, Go usw.), Linter und Formatter aus dem Erweiterungen-Panel (`Ctrl+Shift+X`).
- `settings.json` (Benutzer oder Workspace) steuert das Editorverhalten.
- `launch.json` konfiguriert den Debugger.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Smart Code Completion und Refactoring sind Kernfunktionen.
- Run/Debug-Konfigurationen ermöglichen das Starten und Debuggen von Programmen mit einem Klick.
- Eingebaute Git-Unterstützung im VCS-Menü.
- `Shift+Shift` öffnet den „Search Everywhere"-Dialog.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) formatiert Code neu.
- Plugins erweitern die Sprachunterstützung und fügen Tools hinzu.

### Terminal-Tipps

- Verwende Tab-Vervollständigung, um Dateinamen und Befehle schnell zu vervollständigen.
- Drücke `Ctrl+R`, um die Befehlshistorie interaktiv zu durchsuchen.
- `alias ll='ls -la'` erstellt eine Abkürzung — füge sie zu `~/.bashrc` oder `~/.zshrc` hinzu.
- Verwende `tmux` oder `screen`, um Sitzungen am Leben zu erhalten, wenn du von einem Remote-Server getrennt wirst.
- `man <command>` zeigt die Manual-Seite für jeden eingebauten Befehl.

---

## Docker

Docker packt Anwendungen und ihre Abhängigkeiten in portable Container.

### Kernkonzepte

- **Image**: Eine schreibgeschützte Vorlage, die aus einer `Dockerfile` erstellt wird.
- **Container**: Eine laufende Instanz eines Images.
- **Registry**: Ein Speicher- und Verteildienst für Images (Docker Hub, GHCR).
- **Volume**: Persistenter Speicher, der einen Container überlebt.

### Häufige Befehle

```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Containers
docker run -it ubuntu:22.04 bash        # interaktive Shell
docker run -d -p 8080:80 nginx          # detached, Port-Mapping
docker ps                               # laufende Container
docker ps -a                            # alle Container
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # Shell in laufendem Container öffnen

# Building
docker build -t myapp:1.0 .
docker push myrepo/myapp:1.0
```

### Dockerfile-Beispiel

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose verwaltet Multi-Container-Anwendungen mit einer `docker-compose.yml`-Datei.

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://db:5432/mydb
    depends_on:
      - db
  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d       # alle Services im Hintergrund starten
docker compose down        # Container stoppen und entfernen
docker compose logs -f     # Logs streamen
docker compose build       # Images neu bauen
```
