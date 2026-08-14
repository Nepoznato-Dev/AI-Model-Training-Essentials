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
# টুল ব্যবহার
## গিট — সংস্করণ নিয়ন্ত্রণ
গিট একটি বিতরণকৃত সংস্করণ নিয়ন্ত্রণ ব্যবস্থা। প্রতিটি ডেভেলপার তাদের স্থানীয় মেশিনে সংগ্রহস্থল ইতিহাসের একটি সম্পূর্ণ অনুলিপি আছে.
### মূল কর্মপ্রবাহ
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

### শাখা প্রশাখা
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### মার্জিং এবং রিবেসিং
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### পুল রিকোয়েস্ট (পিআর) ওয়ার্কফ্লো
1.`main`থেকে একটি বৈশিষ্ট্য শাখা তৈরি করুন৷
2. বৈশিষ্ট্য শাখায় প্রতিশ্রুতি দিন।
3. শাখাটি পুশ করুন: `git push origin feature/new-thing`।
4. GitHub/GitLab-এ একটি পুল অনুরোধ খুলুন।
5. অতিরিক্ত প্রতিশ্রুতি সহ ঠিকানা কোড পর্যালোচনা প্রতিক্রিয়া।
6. একবার অনুমোদিত হলে পিআর মার্জ করুন।
### পরিবর্তনগুলি পূর্বাবস্থায় ফিরিয়ে আনা হচ্ছে
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## প্যাকেজ ম্যানেজার
### পিপ (পাইথন)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

প্রকল্প নির্ভরতা বিচ্ছিন্ন রাখতে সর্বদা একটি ভার্চুয়াল পরিবেশের মধ্যে কাজ করুন।
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

`package-lock.json` সঠিক সংস্করণ রেকর্ড করে; উত্স নিয়ন্ত্রণে এটি প্রতিশ্রুতিবদ্ধ করুন।
### কার্গো (মরিচা)
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

### গো মডিউল (যাও)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (ডেবিয়ান / উবুন্টু লিনাক্স)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## কমান্ড-লাইন বেসিক
### নেভিগেশন
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

### পাঠ্য প্রক্রিয়াকরণ
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

### পাইপ এবং পুনঃনির্দেশ
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### নেটওয়ার্ক এবং ফাইল স্থানান্তর
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### অনুমতি
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### প্রক্রিয়া ব্যবস্থাপনা
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## সম্পাদক এবং আইডিই
### VS কোড
VS কোড হল একটি হালকা ওজনের, ক্রস-প্ল্যাটফর্ম কোড সম্পাদক যার একটি সমৃদ্ধ এক্সটেনশন ইকোসিস্টেম রয়েছে।
- টার্মিনালে একটি ফোল্ডার খুলুন:`File > Open Folder`বা `code .`৷
- কমান্ড প্যালেট:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`)।
- ইন্টিগ্রেটেড টার্মিনাল:`Ctrl+`` (backtick)`।
- মাল্টি-কারসার: অতিরিক্ত কার্সার রাখার জন্য `Alt+Click`।
- সংজ্ঞাতে যান: `F12`।
- চিহ্নের নাম পরিবর্তন করুন: `F2`।
- ফরম্যাট নথি: `Shift+Alt+F`।
- এক্সটেনশন: এক্সটেনশন প্যানেল (`Ctrl+Shift+X`) থেকে ভাষা সমর্থন (পাইথন, রাস্ট, গো, ইত্যাদি), লিন্টার এবং ফর্ম্যাটগুলি ইনস্টল করুন।
-`settings.json`(ব্যবহারকারী বা কর্মক্ষেত্র) সম্পাদকের আচরণ নিয়ন্ত্রণ করে।
-`launch.json`ডিবাগার কনফিগার করে।
### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- স্মার্ট কোড সমাপ্তি এবং রিফ্যাক্টরিং হল মূল বৈশিষ্ট্য।
- রান/ডিবাগ কনফিগারেশন আপনাকে এক ক্লিকে প্রোগ্রাম চালু এবং ডিবাগ করতে দেয়।
- ভিসিএস মেনুতে অন্তর্নির্মিত গিট সমর্থন।
-`Shift+Shift`সর্বত্র অনুসন্ধান ডায়ালগ খোলে।
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) কোড পুনরায় ফর্ম্যাট করে৷
- প্লাগইনগুলি ভাষা সমর্থন প্রসারিত করে এবং সরঞ্জাম যোগ করে।
### টার্মিনাল টিপস
- ফাইলের নাম এবং কমান্ড দ্রুত শেষ করতে ট্যাব সমাপ্তি ব্যবহার করুন।
- ইন্টারেক্টিভভাবে কমান্ড ইতিহাস অনুসন্ধান করতে`Ctrl+R`টিপুন।
-`alias ll='ls -la'`একটি শর্টকাট তৈরি করে — এটিকে`~/.bashrc`বা`~/.zshrc`এ যোগ করুন।
- দূরবর্তী সার্ভার থেকে সংযোগ বিচ্ছিন্ন হলে সেশনগুলিকে জীবিত রাখতে`tmux`বা`screen`ব্যবহার করুন৷
-`man <command>`যেকোনো বিল্ট-ইন কমান্ডের জন্য ম্যানুয়াল পৃষ্ঠা দেখায়।
---

## ডকার
ডকার পোর্টেবল পাত্রে অ্যাপ্লিকেশন এবং তাদের নির্ভরতা প্যাকেজ করে।
### মূল ধারণা
- **ছবি**: একটি`Dockerfile`থেকে নির্মিত একটি শুধুমাত্র পঠনযোগ্য টেমপ্লেট৷
- **ধারক**: একটি চিত্রের চলমান উদাহরণ।
- **রেজিস্ট্রি**: ছবির জন্য একটি স্টোরেজ এবং বিতরণ পরিষেবা (ডকার হাব, জিএইচসিআর)।
- **ভলিউম**: স্থায়ী সঞ্চয়স্থান যা একটি ধারককে ছাড়িয়ে যায়।
### সাধারণ কমান্ড
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

### ডকারফাইলের উদাহরণ
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### ডকার কম্পোজ
ডকার কম্পোজ একটি`docker-compose.yml`ফাইল সহ মাল্টি-কন্টেইনার অ্যাপ্লিকেশন পরিচালনা করে।
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
