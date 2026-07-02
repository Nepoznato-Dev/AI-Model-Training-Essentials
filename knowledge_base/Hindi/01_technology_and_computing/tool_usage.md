# टूल उपयोग

## Git — संस्करण नियंत्रण

Git एक वितरित संस्करण नियंत्रण प्रणाली है। हर डेवलपर के पास अपनी लोकल मशीन पर repository के इतिहास की पूरी प्रति होती है।

### मुख्य कार्यप्रवाह

```bash
# नई repository शुरू करें
git init

# मौजूदा repository को clone करें
git clone https://github.com/owner/repo.git

# स्थिति और हाल का इतिहास जाँचें
git status
git log --oneline -10

# बदलाव stage करें
git add file.py            # किसी विशेष file को stage करें
git add .                  # working directory के सभी बदलावों को stage करें

# Commit करें
git commit -m "बदलाव का छोटा, आदेशात्मक विवरण"

# remote पर push करें
git push origin main
```

### Branches का उपयोग

```bash
git branch feature/new-thing        # branch बनाएँ
git checkout feature/new-thing      # उस पर स्विच करें
# शॉर्टकट: git checkout -b feature/new-thing

git branch -d feature/new-thing     # merge के बाद branch हटाएँ
```

### Merge और rebase

```bash
# feature branch को main में merge करें
git checkout main
git merge feature/new-thing

# रीबेस इतिहास को रैखिक रखता है
git checkout feature/new-thing
git rebase main
```

### Pull request (PR) कार्यप्रवाह

1. `main` से feature branch बनाएँ।
2. Feature branch पर commits करें।
3. Branch को push करें: `git push origin feature/new-thing`.
4. GitHub / GitLab पर pull request खोलें।
5. अतिरिक्त commits के साथ code review feedback को संबोधित करें।
6. स्वीकृत होने पर PR को merge करें।

### बदलाव वापस लेना

```bash
git restore file.py            # stage न किए गए बदलावों को हटाएँ
git restore --staged file.py   # किसी file को unstage करें
git revert <commit-sha>        # नया commit बनाएँ जो पिछले commit को undo करे
git reset --soft HEAD~1        # आख़िरी commit undo करें, बदलाव staged रखें
```

---

## Package managers

### pip (Python)

```bash
pip install requests            # package install करें
pip install "requests>=2.28"    # version constraint के साथ
pip install -r requirements.txt # file से install करें
pip uninstall requests
pip list                        # install किए गए packages दिखाएँ
pip show requests               # package की जानकारी
```

Project dependencies को अलग-थलग रखने के लिए हमेशा virtual environment के भीतर काम करें।

### npm (Node.js / JavaScript)

```bash
npm init -y                     # package.json बनाएँ
npm install express             # runtime dependency के रूप में install करें
npm install --save-dev jest     # dev dependency के रूप में install करें
npm uninstall express
npm update
npm run test                    # package.json से "test" script चलाएँ
npm run build
npx create-react-app my-app     # globally install किए बिना package चलाएँ
```

`package-lock.json` सटीक versions दर्ज करता है; इसे source control में commit करें।

### Cargo (Rust)

```bash
cargo new my_project            # नया binary project
cargo new --lib my_lib          # नया library project
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # lint चलाएँ
cargo fmt                       # format करें
cargo update                    # constraints के भीतर dependencies अपडेट करें
```

### Go modules (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # unused dependencies हटाएँ
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)

```bash
sudo apt update                 # package lists refresh करें
sudo apt install git curl wget  # packages install करें
sudo apt remove package-name
sudo apt upgrade                # सभी install किए गए packages upgrade करें
apt search keyword              # packages खोजें
apt show package-name           # package का विवरण
```

---

## Command-line की मूल बातें

### नेविगेशन

```bash
pwd                             # working directory प्रिंट करें
ls                              # directory की contents सूचीबद्ध करें
ls -la                          # hidden files सहित विस्तृत सूची
cd /path/to/dir                 # directory बदलें
cd ..                           # एक स्तर ऊपर जाएँ
cd ~                            # home directory पर जाएँ
mkdir new_folder
rm file.txt                     # file हटाएँ
rm -r folder/                   # directory को recursive रूप से हटाएँ
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### टेक्स्ट प्रोसेसिंग

```bash
cat file.txt                    # file की contents प्रिंट करें
less file.txt                   # file में स्क्रॉल करें
head -n 20 file.txt             # पहली 20 पंक्तियाँ
tail -n 20 file.txt             # आख़िरी 20 पंक्तियाँ
tail -f log.txt                 # बढ़ती हुई log file को follow करें
grep "pattern" file.txt         # pattern खोजें
grep -r "pattern" ./src/        # recursive खोज
grep -i "pattern" file.txt      # case-insensitive खोज
```

### Pipes और redirection

```bash
command1 | command2             # command1 का output command2 में pipe करें
ls -la | grep ".py"             # केवल Python files सूचीबद्ध करें
cat file.txt | wc -l            # पंक्तियाँ गिनें
command > output.txt            # stdout को file में redirect करें (overwrite)
command >> output.txt           # stdout को file में append करें
command 2>&1                    # stderr को stdout में merge करें
```

### Network और file transfer

```bash
curl https://example.com                     # URL fetch करें
curl -o file.zip https://example.com/f.zip   # file में download करें
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # wget से download करें
```

### Permissions

```bash
chmod +x script.sh              # executable बनाएँ
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # owner और group बदलें
```

### Process management

```bash
ps aux                          # चल रही processes सूचीबद्ध करें
kill <PID>                      # process को SIGTERM भेजें
kill -9 <PID>                   # force kill करें
top / htop                      # interactive process monitor
```

---

## Editors और IDEs

### VS Code

VS Code एक हल्का, cross-platform code editor है, जिसमें extensions का समृद्ध ecosystem है।

- Folder खोलें: `File > Open Folder` या terminal में `code .`.
- Command palette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Integrated terminal: `Ctrl+`` (backtick).
- Multi-cursor: अतिरिक्त cursors रखने के लिए `Alt+Click`.
- Definition पर जाएँ: `F12`.
- Symbol का नाम बदलें: `F2`.
- Document format करें: `Shift+Alt+F`.
- Extensions panel (`Ctrl+Shift+X`) से language support (Python, Rust, Go, आदि), linters, और formatters install करें।
- `settings.json` (user या workspace) editor के व्यवहार को नियंत्रित करता है।
- `launch.json` debugger को configure करता है।

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Smart code completion और refactoring इसकी मुख्य विशेषताएँ हैं।
- Run/debug configurations आपको एक click में programs launch और debug करने देती हैं।
- VCS menu में built-in Git support मिलता है।
- `Shift+Shift` Search Everywhere dialog खोलता है।
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) code को reformat करता है।
- Plugins language support बढ़ाते हैं और नए tools जोड़ते हैं।

### Terminal tips

- File names और commands को जल्दी पूरा करने के लिए tab completion का उपयोग करें।
- Command history को interactively खोजने के लिए `Ctrl+R` दबाएँ।
- `alias ll='ls -la'` एक shortcut बनाता है — इसे `~/.bashrc` या `~/.zshrc` में जोड़ें।
- Remote server से disconnect होने पर sessions जीवित रखने के लिए `tmux` या `screen` का उपयोग करें।
- `man <command>` किसी भी built-in command का manual page दिखाता है।

---

## Docker

Docker applications और उनकी dependencies को portable containers में पैकेज करता है।

### मुख्य अवधारणाएँ

- **Image**: `Dockerfile` से बना read-only template।
- **Container**: image का चल रहा instance।
- **Registry**: images के लिए storage और distribution service (Docker Hub, GHCR)।
- **Volume**: स्थायी storage जो container के बाद भी बनी रहती है।

### सामान्य commands

```bash
# छवियां
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# कंटेनर
docker run -it ubuntu:22.04 bash        # interactive shell
docker run -d -p 8080:80 nginx          # detached mode, port mapping
docker ps                               # चल रहे containers
docker ps -a                            # सभी containers
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # चल रहे container में shell खोलें

# निर्माण
docker build -t myapp:1.0 .
docker push myrepo/myapp:1.0
```

### Dockerfile उदाहरण

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose, `docker-compose.yml` file की मदद से multi-container applications को manage करता है।

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
docker compose up -d       # सभी services को background में शुरू करें
docker compose down        # containers को रोकें और हटाएँ
docker compose logs -f     # logs stream करें
docker compose build       # images दोबारा बनाएँ
```
