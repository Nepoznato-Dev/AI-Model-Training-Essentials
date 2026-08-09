---
# فراداده
عنوان: "استفاده از ابزار"
توضیحات: "ابزارها و ابزارهای توسعه"
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [ابزار، استفاده، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "13 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# استفاده از ابزار
## Git - کنترل نسخه
Git یک سیستم کنترل نسخه توزیع شده است. هر توسعه دهنده یک نسخه کامل از تاریخچه مخزن را در ماشین محلی خود دارد.
### گردش کار اصلی
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

### شعبه
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### ادغام و تغییر پایه
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### گردش کار درخواست کشش (PR).
1. یک شاخه ویژگی از`main`ایجاد کنید.
2. روی شاخه ویژگی تعهد بدهید.
3. شاخه را فشار دهید: `git push origin feature/new-thing`.
4. یک درخواست کشش را در GitHub / GitLab باز کنید.
5. بازخورد بررسی کد آدرس با تعهدات اضافی.
6. پس از تایید روابط عمومی را ادغام کنید.
### لغو تغییرات
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## مدیران بسته
### پیپ (پایتون)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

همیشه در یک محیط مجازی کار کنید تا وابستگی های پروژه را جدا نگه دارید.
### npm (Node.js / جاوا اسکریپت)
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

`package-lock.json` نسخه های دقیق را ثبت می کند. آن را به کنترل منبع متعهد کنید.
### بار (زنگ زدگی)
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

### ماژول های برو (برو)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Linux Ubuntu)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## اصول خط فرمان
### ناوبری
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

### پردازش متن
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

### لوله ها و تغییر مسیر
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### انتقال شبکه و فایل
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### مجوزها
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### مدیریت فرآیند
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## ویرایشگرها و IDEها
### در مقابل کد
VS Code یک ویرایشگر کد بین پلتفرمی سبک وزن با اکوسیستم افزونه غنی است.
- یک پوشه:`File > Open Folder`یا`code .`را در ترمینال باز کنید.
- پالت فرمان:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`).
- ترمینال یکپارچه:`Ctrl+`` (backtick)`.
- چند مکان نما:`Alt+Click`برای قرار دادن مکان نماهای اضافی.
- به تعریف بروید: `F12`.
- تغییر نام نماد: `F2`.
- فرمت سند:`Shift+Alt+F`.
- برنامه‌های افزودنی: پشتیبانی از زبان (Python، Rust، Go، و غیره)، linters، و قالب‌کننده‌ها را از پانل Extensions (`Ctrl+Shift+X`) نصب کنید.
-`settings.json`(کاربر یا فضای کاری) رفتار ویرایشگر را کنترل می کند.
-`launch.json`دیباگر را پیکربندی می کند.
### IDE های JetBrains (IntelliJ IDEA، PyCharm، WebStorm، CLion، GoLand)
- تکمیل کد هوشمند و refactoring ویژگی های اصلی هستند.
- تنظیمات Run/Debug به شما امکان می دهد برنامه ها را با یک کلیک راه اندازی و اشکال زدایی کنید.
- پشتیبانی داخلی Git در منوی VCS.
-`Shift+Shift`گفتگوی Search Everywhere را باز می کند.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) کد را دوباره قالب بندی می کند.
- افزونه ها پشتیبانی زبان را گسترش داده و ابزارهایی را اضافه می کنند.
### نکات ترمینال
- از تکمیل برگه برای تکمیل سریع نام فایل ها و دستورات استفاده کنید.
- برای جستجوی تعاملی تاریخچه فرمان،`Ctrl+R`را فشار دهید.
-`alias ll='ls -la'`میانبر ایجاد می کند — آن را به`~/.bashrc`یا`~/.zshrc`اضافه کنید.
- از`tmux`یا`screen`برای زنده نگه داشتن جلسات در صورت قطع ارتباط با سرور راه دور استفاده کنید.
-`man <command>`صفحه دستی هر دستور داخلی را نشان می دهد.
---

## داکر
Docker برنامه ها و وابستگی های آنها را در کانتینرهای قابل حمل بسته بندی می کند.
### مفاهیم اصلی
- **تصویر**: یک الگوی فقط خواندنی که از`Dockerfile`ساخته شده است.
- **Container**: یک نمونه در حال اجرا از یک تصویر.
- **رجیستری**: سرویس ذخیره و توزیع تصاویر (Docker Hub، GHCR).
- **حجم**: ذخیره سازی دائمی که بیشتر از یک ظرف عمر می کند.
### دستورات رایج
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

### مثال Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose
Docker Compose برنامه های چند کانتینری را با یک فایل`docker-compose.yml`مدیریت می کند.
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
