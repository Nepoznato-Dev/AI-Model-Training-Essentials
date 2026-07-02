# Werkzeugnutzung

## Git — Versionskontrolle

Git ist ein verteiltes Versionskontrollsystem. Jeder Entwickler besitzt auf seinem lokalen Rechner eine vollständige Kopie der Repository-Historie.

### Kern-Workflow

```bash
# Ein neues Repository starten
git init

# Ein bestehendes Repository klonen
git clone https://github.com/owner/repo.git

# Status und aktuelle Historie prüfen
git status
git log --oneline -10

# Änderungen stagen
git add file.py            # eine bestimmte Datei stagen
git add .                  # alle Änderungen im Arbeitsverzeichnis stagen

# Commit
git commit -m "Short, imperative description of change"

# In ein Remote pushen
git push origin main
```

### Branching

```bash
git branch feature/new-thing        # einen Branch erstellen
git checkout feature/new-thing      # zu ihm wechseln
# Kurzform: git checkout -b feature/new-thing

git branch -d feature/new-thing     # Branch nach dem Mergen löschen
```

### Merging und Rebasing

```bash
# Feature-Branch in main mergen
git checkout main
git merge feature/new-thing

# Rebase hält die Historie linear
git checkout feature/new-thing
git rebase main
```

### Pull-Request-(PR)-Workflow

1. Einen Feature-Branch von `main` erstellen.
2. Commits auf dem Feature-Branch machen.
3. Den Branch pushen: `git push origin feature/new-thing`.
4. Einen Pull Request auf GitHub / GitLab öffnen.
5. Code-Review-Feedback mit zusätzlichen Commits umsetzen.
6. Den PR nach der Freigabe mergen.

### Änderungen rückgängig machen

```bash
git restore file.py            # unstaged Änderungen verwerfen
git restore --staged file.py   # Staging für eine Datei rückgängig machen
git revert <commit-sha>        # einen neuen Commit erstellen, der einen früheren rückgängig macht
git reset --soft HEAD~1        # letzten Commit rückgängig machen, Änderungen gestaged behalten
```

---

## Paketmanager

### pip (Python)

```bash
pip install requests            # ein Paket installieren
pip install "requests>=2.28"    # mit Versionsvorgabe
pip install -r requirements.txt # aus einer Datei installieren
pip uninstall requests
pip list                        # installierte Pakete anzeigen
pip show requests               # Informationen zu einem Paket
```

Arbeite immer innerhalb einer virtuellen Umgebung, damit Projektabhängigkeiten isoliert bleiben.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # package.json erstellen
npm install express             # als Laufzeitabhängigkeit installieren
npm install --save-dev jest     # als Entwicklungsabhängigkeit installieren
npm uninstall express
npm update
npm run test                    # das Skript "test" aus package.json ausführen
npm run build
npx create-react-app my-app     # ein Paket ohne globale Installation ausführen
```

`package-lock.json` hält exakte Versionen fest; committe die Datei in die Versionskontrolle.

### Cargo (Rust)

```bash
cargo new my_project            # neues Binärprojekt
cargo new --lib my_lib          # neues Bibliotheksprojekt
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # linten
cargo fmt                       # formatieren
cargo update                    # Abhängigkeiten innerhalb der Vorgaben aktualisieren
```

### Go-Module (Go)

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
apt show package-name           # Details zu einem Paket
```

---

## Grundlagen der Kommandozeile

### Navigation

```bash
pwd                             # aktuelles Arbeitsverzeichnis ausgeben
ls                              # Verzeichnisinhalt auflisten
ls -la                          # detaillierte Liste inklusive versteckter Dateien
cd /path/to/dir                 # Verzeichnis wechseln
cd ..                           # eine Ebene nach oben gehen
cd ~                            # ins Home-Verzeichnis gehen
mkdir new_folder
rm file.txt                     # eine Datei entfernen
rm -r folder/                   # ein Verzeichnis rekursiv entfernen
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### Textverarbeitung

```bash
cat file.txt                    # Dateiinhalt ausgeben
less file.txt                   # durch eine Datei blättern
head -n 20 file.txt             # erste 20 Zeilen
tail -n 20 file.txt             # letzte 20 Zeilen
tail -f log.txt                 # einer wachsenden Logdatei folgen
grep "pattern" file.txt         # nach einem Muster suchen
grep -r "pattern" ./src/        # rekursive Suche
grep -i "pattern" file.txt      # Groß-/Kleinschreibung ignorieren
```

### Pipes und Umleitung

```bash
command1 | command2             # Ausgabe von command1 in command2 pipen
ls -la | grep ".py"             # nur Python-Dateien auflisten
cat file.txt | wc -l            # Zeilen zählen
command > output.txt            # stdout in eine Datei umleiten (überschreiben)
command >> output.txt           # stdout an eine Datei anhängen
command 2>&1                    # stderr mit stdout zusammenführen
```

### Netzwerk und Dateitransfer

```bash
curl https://example.com                     # eine URL abrufen
curl -o file.zip https://example.com/f.zip   # in eine Datei herunterladen
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # mit wget herunterladen
```

### Berechtigungen

```bash
chmod +x script.sh              # ausführbar machen
chmod 644 file.txt              # Besitzer lesen/schreiben, Gruppe/andere lesen
chown user:group file.txt       # Besitzer und Gruppe ändern
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

VS Code ist ein leichtgewichtiger, plattformübergreifender Code-Editor mit einem umfangreichen Erweiterungs-Ökosystem.

- Einen Ordner öffnen: `File > Open Folder` oder `code .` im Terminal.
- Befehlspalette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Integriertes Terminal: `Ctrl+`` (backtick)`.
- Mehrfachcursor: `Alt+Click`, um zusätzliche Cursor zu platzieren.
- Zur Definition springen: `F12`.
- Symbol umbenennen: `F2`.
- Dokument formatieren: `Shift+Alt+F`.
- Erweiterungen: Sprachunterstützung (Python, Rust, Go usw.), Linter und Formatter im Extensions-Panel (`Ctrl+Shift+X`) installieren.
- `settings.json` (Benutzer oder Workspace) steuert das Verhalten des Editors.
- `launch.json` konfiguriert den Debugger.

### JetBrains-IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Intelligente Codevervollständigung und Refactoring sind Kernfunktionen.
- Run/Debug-Konfigurationen ermöglichen das Starten und Debuggen von Programmen mit einem Klick.
- Integrierte Git-Unterstützung im VCS-Menü.
- `Shift+Shift` öffnet den Dialog „Search Everywhere“.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) formatiert Code neu.
- Plugins erweitern die Sprachunterstützung und fügen Werkzeuge hinzu.

### Terminal-Tipps

- Nutze Tab-Vervollständigung, um Dateinamen und Befehle schnell zu vervollständigen.
- Drücke `Ctrl+R`, um den Befehlsverlauf interaktiv zu durchsuchen.
- `alias ll='ls -la'` erstellt eine Abkürzung — füge sie zu `~/.bashrc` oder `~/.zshrc` hinzu.
- Nutze `tmux` oder `screen`, um Sitzungen aktiv zu halten, wenn die Verbindung zu einem Remote-Server getrennt wird.
- `man <command>` zeigt die Handbuchseite für jeden eingebauten Befehl an.

---

## Docker

Docker verpackt Anwendungen und ihre Abhängigkeiten in portable Container.

### Kernkonzepte

- **Image**: eine schreibgeschützte Vorlage, die aus einem `Dockerfile` erstellt wird.
- **Container**: eine laufende Instanz eines Images.
- **Registry**: ein Speicher- und Verteilungsdienst für Images (Docker Hub, GHCR).
- **Volume**: persistenter Speicher, der einen Container überdauert.

### Häufige Befehle

```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Container
docker run -it ubuntu:22.04 bash        # interaktive Shell
docker run -d -p 8080:80 nginx          # im Hintergrund, Port-Mapping
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
