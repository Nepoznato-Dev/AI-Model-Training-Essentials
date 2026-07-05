# Cách sử dụng công cụ

## Git — Kiểm soát phiên bản

Git là một hệ thống kiểm soát phiên bản phân tán. Mọi nhà phát triển đều có bản sao đầy đủ lịch sử kho lưu trữ trên máy cục bộ của họ.

### Quy trình làm việc cốt lõi

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

### Phân nhánh

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Hợp nhất và khởi động lại

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Quy trình yêu cầu kéo (PR)

1. Tạo nhánh đối tượng từ `main`.
2. Thực hiện các cam kết trên nhánh tính năng.
3. Đẩy nhánh: `git push origin feature/new-thing`.
4. Mở yêu cầu kéo trên GitHub/GitLab.
5. Phản hồi đánh giá mã địa chỉ với các cam kết bổ sung.
6. Hợp nhất PR sau khi được phê duyệt.

### Hoàn tác các thay đổi

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Người quản lý gói

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Luôn làm việc trong môi trường ảo để tách biệt các phần phụ thuộc của dự án.

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

`package-lock.json` ghi lại các phiên bản chính xác; cam kết kiểm soát nguồn.

### Hàng hóa (Rỉ sét)

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

### Mô-đun đi (Go)

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

## Thông tin cơ bản về dòng lệnh

### Điều hướng

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

### Xử lý văn bản

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

### Đường ống và chuyển hướng

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Truyền mạng và tập tin

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Quyền

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

###Quản lý quy trình

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Trình chỉnh sửa và IDE

### Mã VS

VS Code là trình soạn thảo mã nhẹ, đa nền tảng với hệ sinh thái tiện ích mở rộng phong phú.

- Mở thư mục: `File > Open Folder` hoặc `code .` trong thiết bị đầu cuối.
- Bảng lệnh: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Thiết bị đầu cuối tích hợp: `Ctrl+`` (backtick)`.
- Multi-cursor: `Alt+Click` to place additional cursors.
- Go to definition: `F12`.
- Rename symbol: `F2`.
- Format document: `Shift+Alt+F`.
- Extensions: install language support (Python, Rust, Go, etc.), linters, and formatters from the Extensions panel (`Ctrl+Shift+X`.
- Format document: `settings.jso n` (user or workspace) controls editor behaviour.
- `launch.json` configures the debugger.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Smart code completion and refactoring are core features.
- Run/debug configurations let you launch and debug programs with one click.
- Built-in Git support in the VCS menu.
- `Shift+Shift` opens the Search Everywhere dialog.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) reformats code.
- Plugins extend language support and add tools.

### Terminal tips

- Use tab completion to finish file names and commands quickly.
- Press `Ctrl+R` to search command history interactively.
- `bí danh ll='ls -la'` creates a shortcut — add it to `~/.bashrc` or `~/.zshrc`.
- Use `tmux` or `screen<<INLINE_CODE_23>>>người đàn ông <command>` shows the manual page for any built-in command.

---

## Docker

Docker packages applications and their dependencies into portable containers.

### Core concepts

- **Image**: a read-only template built from a `Tệp Dockerfile`.
- **Container**: a running instance of an image.
- **Registry**: a storage and distribution service for images (Docker Hub, GHCR).
- **Volume**: persistent storage that outlives a container.

### Common commands

<<<CODE_BLOCK_15>>>

### Dockerfile example

<<<CODE_BLOCK_16>>>

### Docker Compose

Docker Compose manages multi-container applications with a `tệp docker-compose.yml`.

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