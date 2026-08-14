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
1. Tạo một nhánh tính năng từ`main`.
2. Thực hiện các cam kết trên nhánh tính năng.
3. Đẩy nhánh:`git push origin feature/new-thing`.
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
- Mở thư mục:`File > Open Folder`hoặc`code .`trong terminal.
- Bảng lệnh:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- Thiết bị đầu cuối tích hợp:`Ctrl+`` (backtick)` .
- Nhiều con trỏ:`Alt+Click`để đặt thêm con trỏ.
- Đi tới định nghĩa:`F12`.
- Ký hiệu đổi tên:`F2`.
- Định dạng tài liệu:`Shift+Alt+F`.
- Tiện ích mở rộng: cài đặt hỗ trợ ngôn ngữ (Python, Rust, Go, v.v.), linters và trình định dạng từ bảng Tiện ích mở rộng (`Ctrl+Shift+X`).
-`settings.json`(người dùng hoặc không gian làm việc) kiểm soát hành vi của người chỉnh sửa.
-`launch.json`định cấu hình trình gỡ lỗi.
### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Hoàn thiện và tái cấu trúc mã thông minh là những tính năng cốt lõi.
- Cấu hình chạy/gỡ lỗi cho phép bạn khởi chạy và gỡ lỗi chương trình chỉ bằng một cú nhấp chuột.
- Hỗ trợ Git tích hợp trong menu VCS.
-`Shift+Shift`mở hộp thoại Tìm kiếm ở mọi nơi.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) định dạng lại mã.
- Plugin mở rộng hỗ trợ ngôn ngữ và thêm công cụ.
### Mẹo về thiết bị đầu cuối
- Sử dụng tính năng hoàn thành tab để hoàn thành tên tệp và lệnh một cách nhanh chóng.
- Nhấn`Ctrl+R`để tìm kiếm lịch sử lệnh một cách tương tác.
-`alias ll='ls -la'`tạo lối tắt — thêm lối tắt đó vào`~/.bashrc`hoặc`~/.zshrc`.
- Sử dụng`tmux`hoặc`screen`để duy trì phiên hoạt động khi ngắt kết nối với máy chủ từ xa.
-`man <command>`hiển thị trang hướng dẫn cho bất kỳ lệnh tích hợp nào.
---

## Docker
Docker đóng gói các ứng dụng và phần phụ thuộc của chúng vào các thùng chứa di động.
### Khái niệm cốt lõi
- **Hình ảnh**: mẫu chỉ đọc được tạo từ`Dockerfile`.
- **Container**: một phiên bản đang chạy của một hình ảnh.
- **Registry**: dịch vụ lưu trữ và phân phối hình ảnh (Docker Hub, GHCR).
- **Khối lượng**: dung lượng lưu trữ liên tục tồn tại lâu hơn vùng chứa.
### Các lệnh thông dụng
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

### Ví dụ về tệp Docker
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Soạn Docker
Docker Compose quản lý các ứng dụng nhiều vùng chứa bằng tệp `docker-compose.yml`.
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
