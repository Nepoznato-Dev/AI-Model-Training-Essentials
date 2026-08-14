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
# Araç Kullanımı
## Git — Sürüm Kontrolü
Git dağıtılmış bir sürüm kontrol sistemidir. Her geliştiricinin yerel makinesinde depo geçmişinin tam bir kopyası vardır.
### Temel iş akışı
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

### Dallanma
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Birleştirme ve yeniden temellendirme
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Çekme isteği (PR) iş akışı
1.`main`adresinden bir özellik dalı oluşturun.
2. Özellik dalında taahhütlerde bulunun.
3. Şubeye basın:`git push origin feature/new-thing`.
4. GitHub/GitLab'da bir çekme isteği açın.
5. Ek taahhütlerle kod inceleme geri bildirimini ele alın.
6. Onaylandıktan sonra PR'yi birleştirin.
### Değişiklikler geri alınıyor
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Paket Yöneticileri
### pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Proje bağımlılıklarını izole tutmak için her zaman sanal bir ortamda çalışın.
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

`package-lock.json` tam sürümleri kaydeder; kaynak kontrolüne aktarın.
### Kargo (Pas)
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

### Go modülleri (Go)
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

## Komut Satırı Temelleri
### Navigasyon
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

### Metin işleme
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

### Borular ve yönlendirme
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Ağ ve dosya aktarımı
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### İzinler
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Süreç yönetimi
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Düzenleyiciler ve IDE'ler
### VS Kodu
VS Code, zengin uzantı ekosistemine sahip, hafif, platformlar arası bir kod düzenleyicisidir.
- Terminalde`File > Open Folder`veya`code .`klasörünü açın.
- Komut paleti:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- Entegre terminal:`Ctrl+`` (backtick)` .
- Çoklu imleç: Ek imleçler yerleştirmek için `Alt+Click`.
- Tanıma gidin:`F12`.
- Sembolü yeniden adlandırın:`F2`.
- Belgeyi biçimlendirin:`Shift+Alt+F`.
- Uzantılar: Uzantılar panelinden (`Ctrl+Shift+X`) dil desteğini (Python, Rust, Go vb.), linter'ları ve biçimlendiricileri yükleyin.
-`settings.json`(kullanıcı veya çalışma alanı) düzenleyici davranışını kontrol eder.
-`launch.json`hata ayıklayıcıyı yapılandırır.
### JetBrains IDE'leri (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Akıllı kod tamamlama ve yeniden düzenleme temel özelliklerdir.
- Çalıştırma/hata ayıklama yapılandırmaları, programları tek tıklamayla başlatmanıza ve hata ayıklamanıza olanak tanır.
- VCS menüsünde yerleşik Git desteği.
-`Shift+Shift`Her Yerde Ara iletişim kutusunu açar.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) kodu yeniden biçimlendirir.
- Eklentiler dil desteğini genişletir ve araçlar ekler.
### Terminal ipuçları
- Dosya adlarını ve komutları hızlı bir şekilde tamamlamak için sekme tamamlamayı kullanın.
- Komut geçmişini etkileşimli olarak aramak için`Ctrl+R`tuşuna basın.
-`alias ll='ls -la'`bir kısayol oluşturur — bunu`~/.bashrc`veya `~/.zshrc`'ye ekleyin.
- Uzak sunucuyla bağlantı kesildiğinde oturumları canlı tutmak için`tmux`veya`screen`kullanın.
-`man <command>`herhangi bir yerleşik komutun kılavuz sayfasını gösterir.
---

## Docker
Docker, uygulamaları ve bağımlılıklarını taşınabilir konteynerlere paketler.
### Temel kavramlar
- **Resim**:`Dockerfile`öğesinden oluşturulmuş salt okunur bir şablon.
- **Kapsayıcı**: bir görüntünün çalışan örneği.
- **Kayıt Defteri**: görüntüler için bir depolama ve dağıtım hizmeti (Docker Hub, GHCR).
- **Birim**: Bir konteynerden daha uzun süre dayanan kalıcı depolama.
### Ortak komutlar
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

### Docker dosyası örneği
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Oluşturma
Docker Compose, çok kapsayıcılı uygulamaları`docker-compose.yml`dosyasıyla yönetir.
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
