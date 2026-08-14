<!--
---
# Metadata
title: "Tool Usage"
description: "Development tools and utilities"
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
tags: [tool, usage, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Использование инструмента
## Git — контроль версий
Git — это распределенная система контроля версий. Каждый разработчик имеет полную копию истории репозитория на своем локальном компьютере.
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

### Слияние и перебазирование
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Рабочий процесс запроса на включение (PR)
1. Создайте ветку функции из `main`.
2. Сделайте коммиты в ветке функций.
3. Нажмите на ветку:`git push origin feature/new-thing`.
4. Откройте запрос на включение на GitHub/GitLab.
5. Адресуйте отзывы о проверке кода с дополнительными коммитами.
6. Объедините PR после утверждения.
### Отмена изменений
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Менеджеры пакетов
### пип (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Всегда работайте в виртуальной среде, чтобы изолировать зависимости проекта.
### npm (Node.js/JavaScript)
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

`package-lock.json` записывает точные версии; передать его в систему контроля версий.
### Груз (Ржавчина)
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

### Разрешения
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
### VS-код
VS Code — это легкий кроссплатформенный редактор кода с богатой экосистемой расширений.
- Откройте папку:`File > Open Folder`или`code .`в терминале.
— Палитра команд:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`).
- Встроенный терминал:`Ctrl+`` (backtick)` .
- Мультикурсор:`Alt+Click`для размещения дополнительных курсоров.
- Перейти к определению:`F12`.
- Переименуйте символ:`F2`.
- Формат документа:`Shift+Alt+F`.
- Расширения: установите языковую поддержку (Python, Rust, Go и т. д.), линтеры и форматтеры с панели расширений (`Ctrl+Shift+X`).
-`settings.json`(пользователь или рабочая область) управляет поведением редактора.
-`launch.json`настраивает отладчик.
### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Интеллектуальное завершение кода и рефакторинг являются основными функциями.
- Конфигурации запуска/отладки позволяют запускать и отлаживать программы одним щелчком мыши.
— Встроенная поддержка Git в меню VCS.
-`Shift+Shift`открывает диалоговое окно «Поиск повсюду».
-`Ctrl+Alt+L`(macOS: `Cmd+Option+L`) переформатирует код.
- Плагины расширяют языковую поддержку и добавляют инструменты.
### Советы по работе с терминалом
- Используйте завершение табуляции для быстрого завершения имен файлов и команд.
- Нажмите`Ctrl+R`для интерактивного поиска в истории команд.
-`alias ll='ls -la'`создает ярлык — добавьте его к`~/.bashrc`или`~/.zshrc`.
- Используйте`tmux`или `screen`, чтобы поддерживать сеансы при отключении от удаленного сервера.
-`man <command>`показывает страницу руководства для любой встроенной команды.
---

## Докер
Docker упаковывает приложения и их зависимости в портативные контейнеры.
### Основные понятия
- **Изображение**: шаблон, доступный только для чтения, созданный на основе`Dockerfile`.
- **Контейнер**: работающий экземпляр изображения.
- **Реестр**: служба хранения и распространения изображений (Docker Hub, GHCR).
- **Том**: постоянное хранилище, которое просуществует дольше контейнера.
### Общие команды
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

### Пример файла Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Создание Docker
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
