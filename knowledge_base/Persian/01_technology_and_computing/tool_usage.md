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

1. یک شاخه ویژگی از `main` ایجاد کنید.
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

- یک پوشه را باز کنید: `File > Open Folder` یا `code .` در ترمینال.
- پالت فرمان: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- ترمینال یکپارچه: "Ctrl+"". (بک تیک)`.
- Multi-cursor: `Alt+Click` to place additional cursors.
- Go to definition: `F12`.
- Rename symbol: `F2<<<INLI NE_CODE_10>>>Shift+Alt+F<<INLINE_CODE_11>>>Ctrl+Shift+X`).
- `settings.jso n<<INLINE_CODE_13>>>launch.json<<INLINE_CODE_14>>>Shift+Shift` opens the Search Everywhere dialog.
- `Ctrl+ Alt+L<<INLINE_CODE_16>>>Cmd+Option+L`) reformats code.
- Plugins extend language support and add tools.

### Terminal tips

- Use tab completion to finish file names and commands quickly.
- Press `Ctrl+R` to search command history interactively.
- `نام مستعار ll='ls -la'` creates a shortcut — add it to `~/.bashrc` or `~/.zshrc`.
- Use `tmux` or `صفحه نمایش` to keep sessions alive when disconnected from a remote server.
- `man <command>` shows the manual page for any built-in command.

---

## Docker

Docker packages applications and their dependencies into portable containers.

### Core concepts

- **Image**: a read-only template built from a `Dockerfile<<INLINE_CODE_25>>>فایل docker-compose.yml`.

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