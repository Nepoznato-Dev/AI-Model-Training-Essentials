# Araç Kullanımı

## Git — Sürüm Kontrolü

Git, dağıtık bir sürüm kontrol sistemidir. Her geliştirici, depo geçmişinin tam bir kopyasını kendi yerel makinesinde tutar.

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

### Birleştirme ve rebase

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull request (PR) iş akışı

1. `main` dalından bir özellik dalı oluşturun.
2. Commit'leri özellik dalında yapın.
3. Dalı gönderin: `git push origin feature/new-thing`.
4. GitHub / GitLab üzerinde bir pull request açın.
5. Kod incelemesi geri bildirimlerini ek commit'lerle ele alın.
6. Onaylandıktan sonra PR'yi birleştirin.

### Değişiklikleri geri alma

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

Proje bağımlılıklarını yalıtılmış tutmak için her zaman bir sanal ortam içinde çalışın.

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

`package-lock.json` tam sürümleri kaydeder; bunu kaynak kontrole ekleyin.

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

### Gezinme

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

## Editörler ve IDE'ler

### VS Code

VS Code, zengin eklenti ekosistemine sahip, hafif ve çok platformlu bir kod editörüdür.

- Bir klasör açın: terminalde `File > Open Folder` veya `code .`.
- Komut paleti: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Tümleşik terminal: `Ctrl+`` (backtick).
- Çoklu imleç: ek imleç yerleştirmek için `Alt+Click`.
- Tanıma git: `F12`.
- Sembol yeniden adlandır: `F2`.
- Belgeyi biçimlendir: `Shift+Alt+F`.
- Eklentiler: Extensions panelinden (`Ctrl+Shift+X`) dil desteği (Python, Rust, Go vb.), linter ve formatter yükleyin.
- `settings.json` (kullanıcı veya çalışma alanı), editör davranışını kontrol eder.
- `launch.json`, hata ayıklayıcıyı yapılandırır.

### JetBrains IDE'leri (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Akıllı kod tamamlama ve refactoring temel özelliklerdir.
- Çalıştırma/hata ayıklama yapılandırmaları, programları tek tıkla başlatıp ayıklamanızı sağlar.
- VCS menüsünde yerleşik Git desteği bulunur.
- `Shift+Shift`, Search Everywhere iletişim kutusunu açar.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) kodu yeniden biçimlendirir.
- Eklentiler dil desteğini genişletir ve araçlar ekler.

### Terminal ipuçları

- Dosya adlarını ve komutları hızla tamamlamak için sekme tamamlama kullanın.
- Komut geçmişinde etkileşimli arama yapmak için `Ctrl+R` tuşlarına basın.
- `alias ll='ls -la'` bir kısayol oluşturur — bunu `~/.bashrc` veya `~/.zshrc` dosyanıza ekleyin.
- Uzak bir sunucudan bağlantınız kesildiğinde oturumları açık tutmak için `tmux` veya `screen` kullanın.
- `man <command>`, herhangi bir yerleşik komutun kılavuz sayfasını gösterir.

---

## Docker

Docker, uygulamaları ve bağımlılıklarını taşınabilir konteynerlere paketler.

### Temel kavramlar

- **Image**: `Dockerfile` dosyasından oluşturulan salt okunur şablon.
- **Container**: bir image'ın çalışan örneği.
- **Registry**: image'lar için depolama ve dağıtım hizmeti (Docker Hub, GHCR).
- **Volume**: konteynerden bağımsız, kalıcı depolama alanı.

### Yaygın komutlar

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

### Dockerfile örneği

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose, çoklu konteyner uygulamalarını `docker-compose.yml` dosyasıyla yönetir.

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
