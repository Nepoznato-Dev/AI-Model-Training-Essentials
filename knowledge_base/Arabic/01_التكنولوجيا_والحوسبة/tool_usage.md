<!-- 
This file was automatically translated from English to Arabic.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# استخدام الأدوات

## Git — التحكم في الإصدارات

Git هو نظام موزّع للتحكم في الإصدارات. يمتلك كل مطوّر نسخة كاملة من تاريخ المستودع على جهازه المحلي.

### سير العمل الأساسي

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

### التفرّع

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### الدمج وإعادة التأسيس

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### سير عمل طلب السحب (PR)

1. أنشئ فرع ميزة انطلاقًا من `main`.
2. سجّل التغييرات على فرع الميزة.
3. ادفع الفرع: `git push origin feature/new-thing`.
4. افتح طلب سحب على GitHub أو GitLab.
5. عالج ملاحظات مراجعة الشيفرة عبر تسجيل تغييرات إضافية.
6. ادمج طلب السحب بعد الموافقة عليه.

### التراجع عن التغييرات

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## أدوات إدارة الحزم

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

اعمل دائمًا داخل بيئة افتراضية للحفاظ على عزل تبعيات المشروع.

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

`package-lock.json` يسجّل الإصدارات الدقيقة؛ لذا أضِفه إلى نظام التحكم في الإصدارات.

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

### وحدات Go (Go)

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

## أساسيات سطر الأوامر

### التنقّل

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

### معالجة النصوص

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

### الأنابيب وإعادة التوجيه

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### الشبكة ونقل الملفات

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### الأذونات

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### إدارة العمليات

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## المحررات وبيئات التطوير المتكاملة

### VS Code

VS Code هو محرر شيفرة خفيف ومتعدد المنصات، ويتميّز بمنظومة غنية من الإضافات.

- افتح مجلدًا: `File > Open Folder` أو `code .` في الطرفية.
- لوحة الأوامر: `Ctrl+Shift+P` ‏(على macOS: `Cmd+Shift+P`).
- الطرفية المدمجة: `Ctrl+`` ‏(علامة الاقتباس الخلفية).
- المؤشرات المتعددة: `Alt+Click` لإضافة مؤشرات إضافية.
- الانتقال إلى التعريف: `F12`.
- إعادة تسمية الرمز: `F2`.
- تنسيق المستند: `Shift+Alt+F`.
- الإضافات: ثبّت دعم اللغات (Python وRust وGo وغيرها)، وأدوات التدقيق، وأدوات التنسيق من لوحة الامتدادات (`Ctrl+Shift+X`).
- يتحكم `settings.json` (على مستوى المستخدم أو مساحة العمل) في سلوك المحرر.
- يضبط `launch.json` إعدادات المنقّح.

### بيئات التطوير المتكاملة من JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- يُعدّ الإكمال الذكي للشيفرة وإعادة الهيكلة من الميزات الأساسية.
- تتيح لك إعدادات التشغيل/التنقيح تشغيل البرامج وتنقيحها بنقرة واحدة.
- يتوفر دعم Git مدمجًا ضمن قائمة VCS.
- يفتح `Shift+Shift` مربع حوار Search Everywhere.
- يعيد `Ctrl+Alt+L` ‏(على macOS: `Cmd+Option+L`) تنسيق الشيفرة.
- توسّع الإضافات دعم اللغات وتضيف أدوات جديدة.

### نصائح للطرفية

- استخدم الإكمال بعلامة التبويب لإتمام أسماء الملفات والأوامر بسرعة.
- اضغط `Ctrl+R` للبحث تفاعليًا في سجل الأوامر.
- ينشئ `alias ll='ls -la'` اختصارًا — أضِفه إلى `~/.bashrc` أو `~/.zshrc`.
- استخدم `tmux` أو `screen` للإبقاء على الجلسات قيد التشغيل عند انقطاع الاتصال بخادم بعيد.
- يعرض `man <command>` صفحة الدليل لأي أمر مضمّن.

---

## Docker

يجمع Docker التطبيقات وتبعياتها داخل حاويات محمولة.

### المفاهيم الأساسية

- **الصورة**: قالب للقراءة فقط يُبنى من ملف `Dockerfile`.
- **الحاوية**: مثيل قيد التشغيل من صورة.
- **السجل**: خدمة لتخزين الصور وتوزيعها (Docker Hub وGHCR).
- **وحدة التخزين**: مساحة تخزين دائمة تستمر بعد انتهاء الحاوية.

### الأوامر الشائعة

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

### مثال على Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

يدير Docker Compose التطبيقات متعددة الحاويات باستخدام ملف `docker-compose.yml`.

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
