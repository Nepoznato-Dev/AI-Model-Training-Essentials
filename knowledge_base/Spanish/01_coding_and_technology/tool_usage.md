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
# Uso de herramientas
## Git — Control de versiones
Git es un sistema de control de versiones distribuido. Cada desarrollador tiene una copia completa del historial del repositorio en su máquina local.
### Flujo de trabajo principal
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

### Ramificación
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Fusionar y rebasar
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Flujo de trabajo de solicitud de extracción (PR)
1. Cree una rama de funciones desde `main`.
2. Realice confirmaciones en la rama de funciones.
3. Empuje la rama:`git push origin feature/new-thing`.
4. Abra una solicitud de extracción en GitHub/GitLab.
5. Aborde los comentarios de la revisión del código con confirmaciones adicionales.
6. Fusionar el RP una vez aprobado.
### Deshacer cambios
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Administradores de paquetes
### pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Trabaje siempre dentro de un entorno virtual para mantener aisladas las dependencias del proyecto.
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

`package-lock.json` registra versiones exactas; comprometerlo con el control de fuente.
### Carga (óxido)
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

### Ir a módulos (Ir)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apto (Debian/Ubuntu Linux)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## Conceptos básicos de la línea de comandos
### Navegación
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

### Procesamiento de texto
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

### Tuberías y redirección
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Red y transferencia de archivos
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Permisos
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Gestión de procesos
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Editores e IDE
### Código VS
VS Code es un editor de código ligero y multiplataforma con un rico ecosistema de extensiones.
- Abra una carpeta:`File > Open Folder`o`code .`en la terminal.
- Paleta de comandos:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`).
- Terminal integrado:`Ctrl+`` (backtick)` .
- Multicursor:`Alt+Click`para colocar cursores adicionales.
- Ir a la definición: `F12`.
- Cambiar nombre del símbolo: `F2`.
- Formato del documento: `Shift+Alt+F`.
- Extensiones: instale soporte de idiomas (Python, Rust, Go, etc.), linters y formateadores desde el panel Extensiones (`Ctrl+Shift+X`).
-`settings.json`(usuario o espacio de trabajo) controla el comportamiento del editor.
-`launch.json`configura el depurador.
### IDE de JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- La finalización y refactorización de código inteligente son características principales.
- Las configuraciones de ejecución/depuración le permiten iniciar y depurar programas con un solo clic.
- Soporte Git integrado en el menú VCS.
-`Shift+Shift`abre el cuadro de diálogo Buscar en todas partes.
-`Ctrl+Alt+L`(macOS: `Cmd+Option+L`) reformatea el código.
- Los complementos amplían el soporte de idiomas y agregan herramientas.
### Consejos para terminales
- Utilice la función de tabulación para finalizar rápidamente los nombres de archivos y los comandos.
- Presione`Ctrl+R`para buscar el historial de comandos de forma interactiva.
-`alias ll='ls -la'`crea un acceso directo: agréguelo a`~/.bashrc`o `~/.zshrc`.
- Utilice`tmux`o`screen`para mantener activas las sesiones cuando se desconecte de un servidor remoto.
-`man <command>`muestra la página del manual para cualquier comando integrado.
---

## acoplador
Docker empaqueta aplicaciones y sus dependencias en contenedores portátiles.
### Conceptos básicos
- **Imagen**: una plantilla de solo lectura creada a partir de `Dockerfile`.
- **Contenedor**: una instancia en ejecución de una imagen.
- **Registry**: un servicio de almacenamiento y distribución de imágenes (Docker Hub, GHCR).
- **Volumen**: almacenamiento persistente que sobrevive a un contenedor.
### Comandos comunes
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

### Ejemplo de archivo Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Componente acoplable
Docker Compose administra aplicaciones de múltiples contenedores con un archivo `docker-compose.yml`.
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
