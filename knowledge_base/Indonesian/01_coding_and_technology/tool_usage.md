---
# Metadata
title: "Tool Usage"
description: "Development tools and utilities"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# Penggunaan Alat
## Git — Kontrol Versi
Git adalah sistem kontrol versi terdistribusi. Setiap pengembang memiliki salinan lengkap riwayat repositori di mesin lokal mereka.
### Alur kerja inti
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

### Bercabang
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Penggabungan dan rebasing
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Alur kerja permintaan tarik (PR).
1. Buat cabang fitur dari`main`.
2. Buat komitmen pada cabang fitur.
3. Dorong cabang:`git push origin feature/new-thing`.
4. Buka permintaan tarik di GitHub/GitLab.
5. Alamatkan umpan balik peninjauan kode dengan komitmen tambahan.
6. Gabungkan PR setelah disetujui.
### Membatalkan perubahan
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Manajer Paket
### pip (Piton)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Selalu bekerja di dalam lingkungan virtual untuk menjaga ketergantungan proyek tetap terisolasi.
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

`package-lock.json` mencatat versi persisnya; komit ke kontrol sumber.
### Kargo (Karat)
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

### Modul Go (Go)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### tepat (Debian / Ubuntu Linux)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## Dasar-dasar Baris Perintah
### Navigasi
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

### Pemrosesan teks
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

### Pipa dan pengalihan
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Jaringan dan transfer file
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Izin
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Manajemen proses
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Editor dan IDE
### Kode VS
VS Code adalah editor kode lintas platform yang ringan dengan ekosistem ekstensi yang kaya.
- Buka folder:`File > Open Folder`atau`code .`di terminal.
- Palet perintah:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- Terminal terintegrasi:`Ctrl+`` (backtick)` .
- Multi-kursor:`Alt+Click`untuk menempatkan kursor tambahan.
- Buka definisi:`F12`.
- Ganti nama simbol:`F2`.
- Format dokumen:`Shift+Alt+F`.
- Ekstensi: instal dukungan bahasa (Python, Rust, Go, dll.), linter, dan formatter dari panel Extensions (`Ctrl+Shift+X`).
-`settings.json`(pengguna atau ruang kerja) mengontrol perilaku editor.
-`launch.json`mengonfigurasi debugger.
### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Penyelesaian kode pintar dan pemfaktoran ulang adalah fitur inti.
- Konfigurasi run/debug memungkinkan Anda meluncurkan dan men-debug program dengan satu klik.
- Dukungan Git bawaan di menu VCS.
-`Shift+Shift`membuka dialog Cari di Mana Saja.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) memformat ulang kode.
- Plugin memperluas dukungan bahasa dan menambahkan alat.
### Tip terminal
- Gunakan penyelesaian tab untuk menyelesaikan nama file dan perintah dengan cepat.
- Tekan`Ctrl+R`untuk mencari riwayat perintah secara interaktif.
-`alias ll='ls -la'`membuat pintasan — tambahkan ke`~/.bashrc`atau`~/.zshrc`.
- Gunakan`tmux`atau`screen`untuk menjaga sesi tetap hidup ketika terputus dari server jauh.
-`man <command>`menampilkan halaman manual untuk setiap perintah bawaan.
---

## buruh pelabuhan
Docker mengemas aplikasi dan dependensinya ke dalam wadah portabel.
### Konsep inti
- **Gambar**: templat hanya-baca yang dibuat dari`Dockerfile`.
- **Container**: instance gambar yang sedang berjalan.
- **Registry**: layanan penyimpanan dan distribusi gambar (Docker Hub, GHCR).
- **Volume**: penyimpanan persisten yang umur kontainernya lebih lama.
### Perintah umum
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

### Contoh file Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Penulisan Docker
Docker Compose mengelola aplikasi multi-kontainer dengan file `docker-compose.yml`.
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
