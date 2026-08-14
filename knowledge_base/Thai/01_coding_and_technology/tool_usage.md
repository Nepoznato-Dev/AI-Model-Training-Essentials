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
# การใช้เครื่องมือ
## Git - การควบคุมเวอร์ชัน
Git คือระบบควบคุมเวอร์ชันแบบกระจาย นักพัฒนาทุกคนมีสำเนาประวัติพื้นที่เก็บข้อมูลฉบับเต็มบนเครื่องภายในของตน
### ขั้นตอนการทำงานหลัก
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

### การแตกแขนง
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### การรวมและการรีบูต
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### เวิร์กโฟลว์คำขอดึง (PR)
1. สร้างสาขาคุณลักษณะจาก `main`
2. ทำการคอมมิตในสาขาฟีเจอร์
3. กดสาขา:`git push origin feature/new-thing`.
4. เปิดคำขอดึงบน GitHub / GitLab
5. ข้อเสนอแนะการตรวจสอบรหัสที่อยู่พร้อมข้อผูกพันเพิ่มเติม
6. รวม PR เมื่อได้รับการอนุมัติแล้ว
### กำลังเลิกทำการเปลี่ยนแปลง
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## ผู้จัดการแพ็คเกจ
### pip (หลาม)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

ทำงานในสภาพแวดล้อมเสมือนเสมอเพื่อแยกการพึ่งพาโครงการออกจากกัน
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

`package-lock.json` บันทึกเวอร์ชันที่แน่นอน ส่งมอบให้กับการควบคุมแหล่งที่มา
### สินค้า (สนิม)
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

### ไปโมดูล (ไป)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### ฉลาด (Debian / Ubuntu Linux)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## พื้นฐานบรรทัดคำสั่ง
### การนำทาง
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

### การประมวลผลข้อความ
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

### ไปป์และการเปลี่ยนเส้นทาง
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### เครือข่ายและการถ่ายโอนไฟล์
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### สิทธิ์
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### การจัดการกระบวนการ
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## บรรณาธิการและ IDE
### รหัส VS
VS Code เป็นตัวแก้ไขโค้ดข้ามแพลตฟอร์มน้ำหนักเบาพร้อมระบบนิเวศส่วนขยายที่หลากหลาย
- เปิดโฟลเดอร์:`File > Open Folder`หรือ`code .`ในเทอร์มินัล
- ชุดคำสั่ง:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`)
- เทอร์มินัลรวม:`Ctrl+`` (backtick)`
- เคอร์เซอร์หลายตัว:`Alt+Click`เพื่อวางเคอร์เซอร์เพิ่มเติม
- ไปที่คำจำกัดความ:`F12`.
- เปลี่ยนชื่อสัญลักษณ์:`F2`.
- รูปแบบเอกสาร:`Shift+Alt+F`.
- ส่วนขยาย: ติดตั้งการสนับสนุนภาษา (Python, Rust, Go ฯลฯ ) linters และตัวจัดรูปแบบจากแผงส่วนขยาย (`Ctrl+Shift+X`)
-`settings.json`(ผู้ใช้หรือพื้นที่ทำงาน) ควบคุมพฤติกรรมของเอดิเตอร์
-`launch.json`กำหนดค่าดีบักเกอร์
### JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- การเติมโค้ดอัจฉริยะและการปรับโครงสร้างใหม่เป็นคุณสมบัติหลัก
- การกำหนดค่ารัน/ดีบักช่วยให้คุณสามารถเปิดและดีบักโปรแกรมได้ด้วยคลิกเดียว
- รองรับ Git ในตัวในเมนู VCS
-`Shift+Shift`เปิดกล่องโต้ตอบค้นหาทุกที่
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) จัดรูปแบบโค้ดใหม่
- ปลั๊กอินขยายการรองรับภาษาและเพิ่มเครื่องมือ
### เคล็ดลับเทอร์มินัล
- ใช้การเติมแท็บเพื่อจบชื่อไฟล์และคำสั่งอย่างรวดเร็ว
- กด`Ctrl+R`เพื่อค้นหาประวัติคำสั่งแบบโต้ตอบ
-`alias ll='ls -la'`สร้างทางลัด - เพิ่มลงใน`~/.bashrc`หรือ `~/.zshrc`
- ใช้`tmux`หรือ`screen`เพื่อรักษาเซสชันให้คงอยู่เมื่อตัดการเชื่อมต่อจากเซิร์ฟเวอร์ระยะไกล
-`man <command>`แสดงหน้าคู่มือสำหรับคำสั่งในตัว
---

## นักเทียบท่า
นักเทียบท่าจัดแพคเกจแอปพลิเคชันและการขึ้นต่อกันลงในคอนเทนเนอร์แบบพกพา
### แนวคิดหลัก
- **รูปภาพ**: เทมเพลตแบบอ่านอย่างเดียวที่สร้างจาก `Dockerfile`
- **คอนเทนเนอร์**: อินสแตนซ์ที่รันอยู่ของรูปภาพ
- **Registry**: บริการจัดเก็บและจัดจำหน่ายรูปภาพ (Docker Hub, GHCR)
- **ปริมาณ**: พื้นที่จัดเก็บข้อมูลถาวรซึ่งมีอายุยืนยาวกว่าคอนเทนเนอร์
### คำสั่งทั่วไป
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

### ตัวอย่าง Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### นักเทียบท่าเขียน
Docker Compose จัดการแอปพลิเคชันหลายคอนเทนเนอร์ด้วยไฟล์ `docker-compose.yml`
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
