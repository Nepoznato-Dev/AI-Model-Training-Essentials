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
# Matumizi ya zana
## Git - Udhibiti wa Toleo
Git ni mfumo wa kudhibiti toleo uliosambazwa. Kila msanidi ana nakala kamili ya historia ya hazina kwenye mashine yao ya karibu.
### Mtiririko wa kazi kuu
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

### Matawi
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Kuunganisha na kuweka upya
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Vuta ombi (PR) mtiririko wa kazi
1. Unda tawi la kipengele kutoka`main`.
2. Fanya ahadi kwenye tawi la kipengele.
3. Sukuma tawi:`git push origin feature/new-thing`.
4. Fungua ombi la kuvuta kwenye GitHub / GitLab.
5. Subiri maoni ya ukaguzi wa msimbo na ahadi za ziada.
6. Unganisha PR mara tu imeidhinishwa.
### Inatendua mabadiliko
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Wasimamizi wa Vifurushi
### bomba (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Daima fanya kazi ndani ya mazingira ya mtandaoni ili kuweka utegemezi wa mradi kutengwa.
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

`package-lock.json` hurekodi matoleo kamili; ikabidhi kwa udhibiti wa chanzo.
### Mizigo (Kutu)
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

### Nenda moduli (Nenda)
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

## Misingi ya Mstari wa Amri
### Urambazaji
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

### Uchakataji wa maandishi
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

### Mabomba na uelekezaji kwingine
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Uhamisho wa mtandao na faili
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Ruhusa
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Usimamizi wa mchakato
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Wahariri na IDE
### Msimbo wa VS
Msimbo wa VS ni kihariri chepesi, cha msimbo wa jukwaa tofauti na mfumo tajiri wa kiendelezi.
- Fungua folda:`File > Open Folder`au`code .`kwenye terminal.
- Paleti ya amri:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- terminal iliyojumuishwa:`Ctrl+`` (backtick)` .
- Multi-cursor:`Alt+Click`kuweka cursors ziada.
- Nenda kwa ufafanuzi:`F12`.
- Badilisha jina la ishara:`F2`.
- Hati ya umbizo:`Shift+Alt+F`.
- Viendelezi: sakinisha usaidizi wa lugha (Python, Rust, Go, n.k.), linters, na umbizo kutoka kwa paneli ya Viendelezi (`Ctrl+Shift+X`).
-`settings.json`(mtumiaji au nafasi ya kazi) inadhibiti tabia ya mhariri.
-`launch.json`inasanidi kitatuzi.
### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Ukamilishaji wa msimbo mahiri na urekebishaji upya ni vipengele vya msingi.
- Endesha/suluhisha usanidi hukuruhusu kuzindua na kurekebisha programu kwa mbofyo mmoja.
- Msaada wa Git uliojengwa ndani kwenye menyu ya VCS.
-`Shift+Shift`inafungua mazungumzo ya Tafuta Kila mahali.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) msimbo wa urekebishaji.
- Programu-jalizi huongeza usaidizi wa lugha na kuongeza zana.
### Vidokezo vya kituo
- Tumia ukamilishaji wa kichupo ili kumaliza majina ya faili na amri haraka.
- Bonyeza`Ctrl+R`ili kutafuta historia ya amri kwa maingiliano.
-`alias ll='ls -la'`huunda njia ya mkato — ongeza kwa`~/.bashrc`au`~/.zshrc`.
- Tumia`tmux`au`screen`kuweka vipindi hai wakati umetenganishwa na seva ya mbali.
-`man <command>`inaonyesha ukurasa wa mwongozo kwa amri yoyote iliyojumuishwa.
---

## Docker
Docker hupakia programu na utegemezi wao kwenye vyombo vinavyobebeka.
### Dhana kuu
- **Picha**: kiolezo cha kusoma pekee kilichoundwa kutoka kwa`Dockerfile`.
- **Kontena**: mfano unaoendelea wa picha.
- **Msajili**: huduma ya kuhifadhi na usambazaji wa picha (Docker Hub, GHCR).
- **Kiasi**: uhifadhi endelevu unaodumu kwa kontena.
### Amri za kawaida
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

### Mfano wa faili ya Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Utungaji wa Docker
Docker Compose inasimamia programu za vyombo vingi na faili ya `docker-compose.yml`.
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
