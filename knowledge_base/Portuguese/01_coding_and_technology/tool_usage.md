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
# Uso de ferramentas
## Git — Controle de Versão
Git é um sistema de controle de versão distribuído. Cada desenvolvedor possui uma cópia completa do histórico do repositório em sua máquina local.
### Fluxo de trabalho principal
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

### Ramificação
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Mesclando e rebaseando
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Fluxo de trabalho de solicitação pull (PR)
1. Crie uma ramificação de recurso de`main`.
2. Faça commits no branch do recurso.
3. Empurre o branch:`git push origin feature/new-thing`.
4. Abra uma solicitação pull no GitHub/GitLab.
5. Aborde o feedback da revisão do código com confirmações adicionais.
6. Mescle o PR depois de aprovado.
### Desfazendo alterações
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Gerenciadores de pacotes
###pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Sempre trabalhe dentro de um ambiente virtual para manter as dependências do projeto isoladas.
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

`package-lock.json` registra versões exatas; confirme-o no controle de origem.
### Carga (ferrugem)
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

### Módulos Go (Go)
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

## Noções básicas de linha de comando
### Navegação
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

### Processamento de texto
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

### Pipes e redirecionamento
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Rede e transferência de arquivos
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Permissões
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Gerenciamento de processos
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Editores e IDEs
### Código VS
VS Code é um editor de código leve e multiplataforma com um rico ecossistema de extensões.
- Abra uma pasta:`File > Open Folder`ou`code .`no terminal.
- Paleta de comandos:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`).
- Terminal integrado:`Ctrl+`` (backtick)` .
- Multicursor:`Alt+Click`para colocar cursores adicionais.
- Vá para a definição:`F12`.
- Renomear símbolo:`F2`.
- Formatar documento:`Shift+Alt+F`.
- Extensões: instale suporte a idiomas (Python, Rust, Go, etc.), linters e formatadores no painel Extensões (`Ctrl+Shift+X`).
-`settings.json`(usuário ou espaço de trabalho) controla o comportamento do editor.
-`launch.json`configura o depurador.
### IDEs JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- A conclusão inteligente e a refatoração de código são recursos essenciais.
- As configurações de execução/depuração permitem iniciar e depurar programas com um clique.
- Suporte Git integrado no menu VCS.
-`Shift+Shift`abre a caixa de diálogo Pesquisar em todos os lugares.
-`Ctrl+Alt+L`(macOS: `Cmd+Option+L`) reformata o código.
- Plugins ampliam o suporte a idiomas e adicionam ferramentas.
### Dicas de terminais
- Use o preenchimento de tabulação para finalizar nomes de arquivos e comandos rapidamente.
- Pressione`Ctrl+R`para pesquisar o histórico de comandos de forma interativa.
-`alias ll='ls -la'`cria um atalho – adicione-o a`~/.bashrc`ou`~/.zshrc`.
- Use`tmux`ou`screen`para manter as sessões ativas quando desconectado de um servidor remoto.
-`man <command>`mostra a página de manual de qualquer comando integrado.
---

## Docker
O Docker empacota aplicativos e suas dependências em contêineres portáteis.
### Conceitos básicos
- **Imagem**: um modelo somente leitura criado a partir de um`Dockerfile`.
- **Container**: uma instância em execução de uma imagem.
- **Registro**: serviço de armazenamento e distribuição de imagens (Docker Hub, GHCR).
- **Volume**: armazenamento persistente que sobrevive a um contêiner.
### Comandos comuns
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

### Exemplo de Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compor
Docker Compose gerencia aplicativos de vários contêineres com um arquivo `docker-compose.yml`.
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
