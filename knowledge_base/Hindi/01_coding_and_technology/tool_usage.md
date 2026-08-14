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
# उपकरण का उपयोग
## गिट - संस्करण नियंत्रण
Git एक वितरित संस्करण नियंत्रण प्रणाली है। प्रत्येक डेवलपर के पास अपनी स्थानीय मशीन पर रिपॉजिटरी इतिहास की पूरी प्रति होती है।
### कोर वर्कफ़्लो
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

### शाखाकरण
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### विलय और पुनः आधार बनाना
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### पुल अनुरोध (पीआर) वर्कफ़्लो
1.`main`से एक फीचर शाखा बनाएं।
2. फीचर ब्रांच पर कमिट बनाएं।
3. शाखा को पुश करें: `git push origin feature/new-thing`।
4. GitHub/GitLab पर एक पुल अनुरोध खोलें।
5. अतिरिक्त प्रतिबद्धताओं के साथ पता कोड समीक्षा प्रतिक्रिया।
6. स्वीकृत होने पर पीआर को मर्ज करें।
### परिवर्तनों को पूर्ववत करना
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## पैकेज प्रबंधक
### पिप (पायथन)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

प्रोजेक्ट निर्भरता को अलग रखने के लिए हमेशा आभासी वातावरण के अंदर काम करें।
### एनपीएम (नोड.जेएस/जावास्क्रिप्ट)
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

`package-lock.json` सटीक संस्करण रिकॉर्ड करता है; इसे स्रोत नियंत्रण के लिए प्रतिबद्ध करें।
### कार्गो (जंग)
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

### गो मॉड्यूल (जाओ)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### उपयुक्त (डेबियन/उबंटू लिनक्स)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## कमांड-लाइन मूल बातें
### मार्गदर्शन
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

### पाठ प्रसंस्करण
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

### पाइप और पुनर्निर्देशन
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### नेटवर्क और फ़ाइल स्थानांतरण
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### अनुमतियाँ
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### प्रक्रिया प्रबंधन
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## संपादक और आईडीई
### वीएस कोड
वीएस कोड एक समृद्ध विस्तार पारिस्थितिकी तंत्र के साथ एक हल्का, क्रॉस-प्लेटफॉर्म कोड संपादक है।
- टर्मिनल में एक फ़ोल्डर खोलें:`File > Open Folder`या `code .`।
- कमांड पैलेट:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`)।
- एकीकृत टर्मिनल:`Ctrl+`` (backtick)`।
- मल्टी-कर्सर: अतिरिक्त कर्सर लगाने के लिए `Alt+Click`।
- परिभाषा पर जाएँ: `F12`।
- प्रतीक का नाम बदलें: `F2`।
- प्रारूप दस्तावेज़: `Shift+Alt+F`।
- एक्सटेंशन: एक्सटेंशन पैनल (`Ctrl+Shift+X`) से भाषा समर्थन (पायथन, रस्ट, गो, आदि), लिंटर और फ़ॉर्मेटर स्थापित करें।
-`settings.json`(उपयोगकर्ता या कार्यक्षेत्र) संपादक के व्यवहार को नियंत्रित करता है।
-`launch.json`डिबगर को कॉन्फ़िगर करता है।
### जेटब्रेन आईडीई (इंटेलिजे आईडीईए, पाइचार्म, वेबस्टॉर्म, सीएलियन, गोलैंड)
- स्मार्ट कोड पूर्णता और रीफैक्टरिंग मुख्य विशेषताएं हैं।
- रन/डीबग कॉन्फ़िगरेशन आपको एक क्लिक से प्रोग्राम लॉन्च और डीबग करने देता है।
- वीसीएस मेनू में अंतर्निहित गिट समर्थन।
-`Shift+Shift`हर जगह खोजें संवाद खोलता है।
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) कोड को पुन: स्वरूपित करता है।
- प्लगइन्स भाषा समर्थन बढ़ाते हैं और टूल जोड़ते हैं।
### टर्मिनल युक्तियाँ
- फ़ाइल नाम और आदेशों को शीघ्रता से पूरा करने के लिए टैब पूर्णता का उपयोग करें।
- इंटरैक्टिव रूप से कमांड इतिहास खोजने के लिए`Ctrl+R`दबाएँ।
-`alias ll='ls -la'`एक शॉर्टकट बनाता है - इसे`~/.bashrc`या`~/.zshrc`में जोड़ें।
- दूरस्थ सर्वर से डिस्कनेक्ट होने पर सत्र को चालू रखने के लिए`tmux`या`screen`का उपयोग करें।
-`man <command>`किसी भी अंतर्निहित कमांड के लिए मैनुअल पेज दिखाता है।
---

## डॉकर
डॉकर अनुप्रयोगों और उनकी निर्भरताओं को पोर्टेबल कंटेनरों में पैकेज करता है।
### मूल अवधारणाएँ
- **छवि**:`Dockerfile`से निर्मित केवल पढ़ने योग्य टेम्पलेट।
- **कंटेनर**: एक छवि का चालू उदाहरण।
- **रजिस्ट्री**: छवियों के लिए एक भंडारण और वितरण सेवा (डॉकर हब, जीएचसीआर)।
- **वॉल्यूम**: लगातार भंडारण जो एक कंटेनर से अधिक समय तक चलता है।
### सामान्य आदेश
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

### डॉकरफ़ाइल उदाहरण
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### डॉकर कम्पोज़
डॉकर कंपोज़`docker-compose.yml`फ़ाइल के साथ मल्टी-कंटेनर एप्लिकेशन प्रबंधित करता है।
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
