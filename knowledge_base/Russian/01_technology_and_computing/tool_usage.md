# Использование инструментов

## Git — контроль версий

Git — это распределённая система контроля версий. У каждого разработчика есть полная копия истории репозитория на локальной машине.

### Основной рабочий процесс

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

### Ветвление

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Слияние и rebase

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Рабочий процесс запроса на слияние (PR)

1. Создайте feature-ветку от `main`.
2. Делайте коммиты в feature-ветке.
3. Отправьте ветку: `git push origin feature/new-thing`.
4. Откройте запрос на слияние в GitHub / GitLab.
5. Внесите дополнительные коммиты по итогам проверки кода.
6. Слейте PR после одобрения.

### Отмена изменений

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Менеджеры пакетов

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Всегда работайте внутри виртуального окружения, чтобы зависимости проекта оставались изолированными.

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

`package-lock.json` фиксирует точные версии; добавляйте его в систему контроля версий.

### Cargo (Rust)

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

### Модули Go (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)

```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## Основы командной строки

### Навигация

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

### Обработка текста

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

### Каналы и перенаправление

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Сеть и передача файлов

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Права доступа

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Управление процессами

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Редакторы и IDE

### VS Code

VS Code — это лёгкий кроссплатформенный редактор кода с богатой экосистемой расширений.

- Открыть папку: `File > Open Folder` или `code .` в терминале.
- Палитра команд: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Встроенный терминал: `Ctrl+`` (backtick)`.
- Множественные курсоры: `Alt+Click`, чтобы поставить дополнительные курсоры.
- Перейти к определению: `F12`.
- Переименовать символ: `F2`.
- Форматировать документ: `Shift+Alt+F`.
- Расширения: устанавливайте поддержку языков (Python, Rust, Go и т. д.), линтеры и форматтеры из панели Extensions (`Ctrl+Shift+X`).
- `settings.json` (пользовательский или для рабочей области) управляет поведением редактора.
- `launch.json` настраивает отладчик.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Умное автодополнение кода и рефакторинг — ключевые возможности.
- Конфигурации запуска/отладки позволяют запускать и отлаживать программы в один клик.
- Встроенная поддержка Git находится в меню VCS.
- `Shift+Shift` открывает диалог Search Everywhere.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) переформатирует код.
- Плагины расширяют языковую поддержку и добавляют инструменты.

### Советы по терминалу

- Используйте автодополнение по Tab, чтобы быстро дописывать имена файлов и команды.
- Нажмите `Ctrl+R`, чтобы интерактивно искать по истории команд.
- `alias ll='ls -la'` создаёт сокращение — добавьте его в `~/.bashrc` или `~/.zshrc`.
- Используйте `tmux` или `screen`, чтобы сохранять сессии при отключении от удалённого сервера.
- `man <command>` показывает страницу руководства для любой встроенной команды.

---

## Docker

Docker упаковывает приложения и их зависимости в переносимые контейнеры.

### Основные понятия

- **Образ**: шаблон только для чтения, собранный из `Dockerfile`.
- **Container**: запущенный экземпляр образа.
- **Реестр**: сервис хранения и распространения образов (Docker Hub, GHCR).
- **Volume**: постоянное хранилище, которое живёт дольше контейнера.

### Часто используемые команды

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

### Пример Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose управляет многоконтейнерными приложениями с помощью файла `docker-compose.yml`.

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
