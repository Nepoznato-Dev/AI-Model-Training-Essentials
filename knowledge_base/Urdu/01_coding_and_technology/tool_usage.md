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
# آلے کا استعمال
## گٹ - ورژن کنٹرول
گٹ ایک تقسیم شدہ ورژن کنٹرول سسٹم ہے۔ ہر ڈویلپر کے پاس اپنی مقامی مشین پر مخزن کی تاریخ کی مکمل کاپی ہوتی ہے۔
### بنیادی ورک فلو
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

### برانچنگ
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### ضم کرنا اور دوبارہ ترتیب دینا
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### پل کی درخواست (PR) ورک فلو
1.`main`سے فیچر برانچ بنائیں۔
2. فیچر برانچ پر وعدے کریں۔
3. برانچ کو دبائیں:`git push origin feature/new-thing`۔
4. GitHub/GitLab پر پل کی درخواست کھولیں۔
5. اضافی کمٹ کے ساتھ ایڈریس کوڈ کا جائزہ لینے کے تاثرات۔
6. منظور ہونے کے بعد PR کو ضم کریں۔
### تبدیلیوں کو کالعدم کرنا
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## پیکیج مینیجرز
### پائپ (ازگر)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

پروجیکٹ کے انحصار کو الگ تھلگ رکھنے کے لیے ہمیشہ ورچوئل ماحول میں کام کریں۔
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

`package-lock.json` درست ورژن ریکارڈ کرتا ہے۔ ماخذ کے کنٹرول کے لیے اس کا ارتکاب کریں۔
### کارگو (زنگ)
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

### گو ماڈیولز (گو)
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

## کمانڈ لائن کی بنیادی باتیں
### نیویگیشن
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

### ٹیکسٹ پروسیسنگ
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

### پائپس اور ری ڈائریکشن
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### نیٹ ورک اور فائل ٹرانسفر
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### اجازتیں۔
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### عمل کا انتظام
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## ایڈیٹرز اور IDEs
### VS کوڈ
VS کوڈ ایک ہلکا پھلکا، کراس پلیٹ فارم کوڈ ایڈیٹر ہے جس میں ایک بھرپور ایکسٹینشن ایکو سسٹم ہے۔
- ایک فولڈر کھولیں:`File > Open Folder`یا`code .`ٹرمینل میں۔
- کمانڈ پیلیٹ:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`)۔
- مربوط ٹرمینل:`Ctrl+`` (backtick)`۔
- ملٹی کرسر: اضافی کرسر لگانے کے لیے `Alt+Click`۔
- تعریف پر جائیں:`F12`۔
- علامت کا نام تبدیل کریں:`F2`۔
- فارمیٹ دستاویز:`Shift+Alt+F`۔
- ایکسٹینشنز: ایکسٹینشن پینل (`Ctrl+Shift+X`) سے لینگویج سپورٹ (Python، Rust، Go، وغیرہ)، لنٹرز، اور فارمیٹرز انسٹال کریں۔
-`settings.json`(صارف یا ورک اسپیس) ایڈیٹر کے رویے کو کنٹرول کرتا ہے۔
-`launch.json`ڈیبگر کو کنفیگر کرتا ہے۔
### JetBrains IDEs (IntelliJ IDEA، PyCharm، WebStorm، CLion، GoLand)
- سمارٹ کوڈ کی تکمیل اور ری فیکٹرنگ بنیادی خصوصیات ہیں۔
- رن/ڈیبگ کنفیگریشنز آپ کو ایک کلک کے ساتھ پروگرام لانچ اور ڈیبگ کرنے دیتی ہیں۔
- VCS مینو میں بلٹ ان Git سپورٹ۔
-`Shift+Shift`ہر جگہ تلاش کا ڈائیلاگ کھولتا ہے۔
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) کوڈ کی اصلاح کرتا ہے۔
- پلگ انز زبان کی حمایت کو بڑھاتے ہیں اور ٹولز شامل کرتے ہیں۔
### ٹرمینل ٹپس
- فائل کے ناموں اور کمانڈز کو تیزی سے ختم کرنے کے لیے ٹیب کی تکمیل کا استعمال کریں۔
- کمانڈ ہسٹری کو انٹرایکٹو طریقے سے تلاش کرنے کے لیے`Ctrl+R`دبائیں۔
-`alias ll='ls -la'`ایک شارٹ کٹ بناتا ہے — اسے`~/.bashrc`یا`~/.zshrc`میں شامل کریں۔
- ریموٹ سرور سے منقطع ہونے پر سیشنز کو زندہ رکھنے کے لیے`tmux`یا`screen`استعمال کریں۔
-`man <command>`کسی بھی بلٹ ان کمانڈ کے لیے دستی صفحہ دکھاتا ہے۔
---

## ڈوکر
ڈوکر ایپلی کیشنز اور ان کے انحصار کو پورٹیبل کنٹینرز میں پیک کرتا ہے۔
### بنیادی تصورات
- **تصویر**: ایک`Dockerfile`سے بنایا گیا صرف پڑھنے کے لیے ٹیمپلیٹ۔
- **کنٹینر**: ایک تصویر کی چلتی ہوئی مثال۔
- **رجسٹری**: تصاویر کے لیے اسٹوریج اور ڈسٹری بیوشن سروس (Docker Hub, GHCR)۔
- **حجم**: مستقل اسٹوریج جو کنٹینر سے زیادہ زندہ رہتا ہے۔
### عام احکامات
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

### ڈاکر فائل کی مثال
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### ڈوکر کمپوز
ڈوکر کمپوز ایک`docker-compose.yml`فائل کے ساتھ ملٹی کنٹینر ایپلی کیشنز کا انتظام کرتا ہے۔
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
