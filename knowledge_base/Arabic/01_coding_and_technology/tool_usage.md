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
#استخدام الأداة
## Git — التحكم في الإصدار
Git هو نظام للتحكم في الإصدار الموزع. يمتلك كل مطور نسخة كاملة من سجل المستودع على أجهزته المحلية.
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

### المتفرعة
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

### سير عمل طلب السحب (PR).
1. قم بإنشاء فرع ميزة من`main`.
2. قم بإجراء الالتزامات على فرع الميزة.
3. ادفع الفرع:`git push origin feature/new-thing`.
4. افتح طلب سحب على GitHub / GitLab.
5. معالجة تعليقات مراجعة التعليمات البرمجية مع الالتزامات الإضافية.
6. دمج العلاقات العامة بعد الموافقة عليها.
### التراجع عن التغييرات
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## مدراء الحزم
### النقطة (بايثون)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

اعمل دائمًا داخل بيئة افتراضية لعزل تبعيات المشروع.
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

يسجل`package-lock.json`الإصدارات الدقيقة؛ إلزامها بالتحكم في المصدر.
### البضائع (الصدأ)
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

### ملائمة (ديبيان / أوبونتو لينكس)
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
### ملاحة
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

### نقل الشبكة والملفات
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

## المحررين و IDEs
### كود VS
VS Code هو محرر أكواد برمجية خفيف الوزن ومتعدد المنصات مع نظام بيئي غني بالامتدادات.
- افتح المجلد:`File > Open Folder`أو`code .`في الجهاز.
- لوحة الأوامر:`Ctrl+Shift+P`(نظام التشغيل MacOS: `Cmd+Shift+P`).
- المحطة المتكاملة:`Ctrl+`` (backtick)`.
- مؤشر متعدد:`Alt+Click`لوضع مؤشرات إضافية.
- انتقل إلى التعريف:`F12`.
- إعادة تسمية الرمز:`F2`.
- تنسيق الوثيقة:`Shift+Alt+F`.
- الإضافات: تثبيت دعم اللغة (Python، وRust، وGo، وما إلى ذلك)، والنترات، والمنسقات من لوحة الإضافات (`Ctrl+Shift+X`).
- يتحكم`settings.json`(المستخدم أو مساحة العمل) في سلوك المحرر.
- يقوم`launch.json`بتكوين مصحح الأخطاء.
### بيئة تطوير متكاملة لـ JetBrains (IntelliJ IDEA وPyCharm وWebStorm وCLion وGoLand)
- يعد إكمال التعليمات البرمجية الذكية وإعادة البناء من الميزات الأساسية.
- تتيح لك تكوينات التشغيل/التصحيح تشغيل البرامج وتصحيح أخطائها بنقرة واحدة.
- دعم Git مدمج في قائمة VCS.
- يفتح`Shift+Shift`مربع حوار البحث في كل مكان.
-`Ctrl+Alt+L`(macOS: `Cmd+Option+L`) يعيد تنسيق الكود.
- تعمل المكونات الإضافية على توسيع دعم اللغة وإضافة الأدوات.
### نصائح المحطة
- استخدم إكمال علامة التبويب لإنهاء أسماء الملفات والأوامر بسرعة.
- اضغط على`Ctrl+R`للبحث في سجل الأوامر بشكل تفاعلي.
- ينشئ`alias ll='ls -la'`اختصارًا — أضفه إلى`~/.bashrc`أو `~/.zshrc`.
- استخدم`tmux`أو`screen`لإبقاء الجلسات حية عند قطع الاتصال بخادم بعيد.
- يعرض`man <command>`الصفحة اليدوية لأي أمر مضمن.
---

## عامل الميناء
يقوم Docker بتجميع التطبيقات وتبعياتها في حاويات محمولة.
### المفاهيم الأساسية
- **الصورة**: قالب للقراءة فقط تم إنشاؤه من`Dockerfile`.
- **الحاوية**: نسخة قيد التشغيل من الصورة.
- **التسجيل**: خدمة تخزين وتوزيع الصور (Docker Hub, GHCR).
- **الحجم**: تخزين مستمر يتجاوز عمر الحاوية.
### الأوامر المشتركة
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

### مثال على ملف Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### عامل الميناء يؤلف
يدير Docker Compose تطبيقات متعددة الحاويات باستخدام ملف `docker-compose.yml`.
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
