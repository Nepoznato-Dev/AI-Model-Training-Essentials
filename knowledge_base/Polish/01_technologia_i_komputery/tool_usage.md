# Użycie narzędzia

## Git — Kontrola wersji

Git to rozproszony system kontroli wersji. Każdy programista ma pełną kopię historii repozytorium na swoim komputerze lokalnym.

### Podstawowy przepływ pracy

```bash
# Start a new repository
git init

# Clone an existing repository
git clone https://github.com/owner/repo.git

# Check status and recent history
git status
git log --oneline -10

# Stage changes
git add file.py            # stage a specific file
git add .                  # stage all changes in the working directory

# Commit
git commit -m "Short, imperative description of change"

# Push to a remote
git push origin main
```

### Rozgałęzianie

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Łączenie i zmiana bazy

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Przepływ pracy z żądaniem ściągnięcia (PR).

1. Utwórz gałąź funkcji z `main`.
2. Dokonaj zatwierdzeń w gałęzi funkcji.
3. Naciśnij gałąź: `git push origin feature/new-thing`.
4. Otwórz żądanie ściągnięcia w GitHub/GitLab.
5. Informacje zwrotne dotyczące przeglądu kodu adresu z dodatkowymi zatwierdzeniami.
6. Po zatwierdzeniu połącz PR.

### Cofanie zmian

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Menedżerowie pakietów

### pips (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Zawsze pracuj w środowisku wirtualnym, aby izolować zależności projektu.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # create package.json
npm install express             # install as a runtime dependency
npm install --save-dev jest     # install as a dev dependency
npm uninstall express
npm update
npm run test                    # run the "test" script from package.json
npm run build
npx create-react-app my-app     # run a package without installing globally
```

`package-lock.json` rejestruje dokładne wersje; przekaż to do kontroli źródła.

### Ładunek (rdza)

```bash
cargo new my_project            # new binary project
cargo new --lib my_lib          # new library project
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # lint
cargo fmt                       # format
cargo update                    # update dependencies within constraints
```

### Moduły Przejdź (Przejdź)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (Debian/Ubuntu Linux)

```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## Podstawy wiersza poleceń

### Nawigacja

```bash
pwd                             # print working directory
ls                              # list directory contents
ls -la                          # detailed listing including hidden files
cd /path/to/dir                 # change directory
cd ..                           # go up one level
cd ~                            # go to home directory
mkdir new_folder
rm file.txt                     # remove a file
rm -r folder/                   # remove a directory recursively
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### Przetwarzanie tekstu

```bash
cat file.txt                    # print file contents
less file.txt                   # scroll through a file
head -n 20 file.txt             # first 20 lines
tail -n 20 file.txt             # last 20 lines
tail -f log.txt                 # follow a growing log file
grep "pattern" file.txt         # search for a pattern
grep -r "pattern" ./src/        # recursive search
grep -i "pattern" file.txt      # case-insensitive
```

### Potoki i przekierowania

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Sieć i transfer plików

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Uprawnienia

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Zarządzanie procesami

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Redaktorzy i IDE

### Kod VS

VS Code to lekki, wieloplatformowy edytor kodu z bogatym ekosystemem rozszerzeń.

- Otwórz folder: `File > Open Folder` lub `code .` w terminalu.
- Paleta poleceń: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Zintegrowany terminal: `Ctrl+`` (backtick)`.
- Wiele kursorów: `Alt+Click`, aby umieścić dodatkowe kursory.
- Przejdź do definicji: `F12`.
- Zmień nazwę symbolu: `F2`.
- Formatuj dokument: `Shift+Alt+F`.
- Rozszerzenia: zainstaluj obsługę języków (Python, Rust, Go itp.), linters i formatery z panelu Rozszerzenia (<<INLINE_CODE_12>>>).
- `settings.json` (użytkownik lub obszar roboczy) kontroluje zachowanie edytora.
- `launch.json` konfiguruje debuger.

### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Inteligentne uzupełnianie i refaktoryzacja kodu to podstawowe funkcje.
- Konfiguracje uruchamiania/debugowania umożliwiają uruchamianie i debugowanie programów jednym kliknięciem.
- Wbudowana obsługa Git w menu VCS.
- `Shift+Shift` otwiera okno dialogowe Szukaj wszędzie.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) ponownie formatuje kod.
- Wtyczki rozszerzają obsługę języków i dodają narzędzia.

### Wskazówki dotyczące terminala

- Użyj uzupełniania tabulatorów, aby szybko kończyć nazwy plików i polecenia.
- Naciśnij `Ctrl+R`, aby interaktywnie przeszukać historię poleceń.
- `alias ll='ls -la'` tworzy skrót — dodaj go do `~/.bashrc` lub `~/.zshrc`.
- Użyj `tmux` lub `screen`, aby utrzymać sesje przy życiu po rozłączeniu ze zdalnym serwerem.
- `man <command>` pokazuje stronę podręcznika dla dowolnego wbudowanego polecenia.

---

## Doker

Docker pakuje aplikacje i ich zależności do przenośnych kontenerów.

### Podstawowe pojęcia

- **Obraz**: szablon tylko do odczytu zbudowany na podstawie `Dockerfile`.
- **Kontener**: działająca instancja obrazu.
- **Rejestr**: usługa przechowywania i dystrybucji obrazów (Docker Hub, GHCR).
- **Wolumin**: pamięć trwała, która przetrwa dłużej niż kontener.

### Typowe polecenia

```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Containers
docker run -it ubuntu:22.04 bash        # interactive shell
docker run -d -p 8080:80 nginx          # detached, port mapping
docker ps                               # running containers
docker ps -a                            # all containers
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # open shell in running container

# Building
docker build -t myapp:1.0 .
docker push myrepo/myapp:1.0
```

### Przykład pliku Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Tworzenie Dockera

Docker Compose zarządza aplikacjami wielokontenerowymi za pomocą pliku `docker-compose.yml`.

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
docker compose up -d       # start all services in the background
docker compose down        # stop and remove containers
docker compose logs -f     # stream logs
docker compose build       # rebuild images
```