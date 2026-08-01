<!-- 
This file was automatically translated from English to Korean.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 도구 사용법

## Git — 버전 관리

Git은 분산 버전 관리 시스템입니다. 각 개발자는 자신의 로컬 머신에 repository 전체 history의 복사본을 보유합니다.

### 핵심 워크플로

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

### 브랜치 작업

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### 병합과 리베이스

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull request (PR) 워크플로

1. `main`에서 feature branch를 만듭니다.
2. feature branch에서 commit을 쌓습니다.
3. branch를 push합니다: `git push origin feature/new-thing`.
4. GitHub 또는 GitLab에서 pull request를 엽니다.
5. code review feedback을 반영해 추가 commit을 만듭니다.
6. 승인이 끝나면 PR을 merge합니다.

### 변경 사항 되돌리기

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## 패키지 관리자

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

프로젝트 의존성을 분리하기 위해서는 항상 virtual environment 안에서 작업하는 것이 좋습니다.

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

`package-lock.json`에는 정확한 버전 정보가 기록되므로 source control에 함께 commit하는 것이 좋습니다.

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

### Go modules (Go)

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

## 명령줄 기본

### 탐색과 파일 작업

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

### 텍스트 처리

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

### 파이프와 리디렉션

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### 네트워크와 파일 전송

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### 권한 관리

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### 프로세스 관리

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## 에디터와 IDE

### VS Code

VS Code는 가볍고 여러 플랫폼에서 사용할 수 있는 코드 에디터이며, 확장 생태계가 매우 풍부합니다.

- 폴더 열기: `File > Open Folder` 또는 terminal에서 `code .`
- Command palette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`)
- 통합 terminal: `Ctrl+`` (backtick)
- 멀티 커서: `Alt+Click`으로 커서를 추가
- 정의로 이동: `F12`
- 심볼 이름 바꾸기: `F2`
- 문서 포맷: `Shift+Alt+F`
- Extensions 패널(`Ctrl+Shift+X`)에서 Python, Rust, Go 등 언어 지원과 linter, formatter를 설치할 수 있습니다.
- `settings.json`은 사용자 또는 workspace 단위의 에디터 동작을 제어합니다.
- `launch.json`은 debugger 설정에 사용됩니다.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- 강력한 code completion과 refactoring 기능이 핵심 장점입니다.
- 실행/디버그 설정(configuration)을 통해 클릭 한 번으로 프로그램을 실행하고 디버깅할 수 있습니다.
- Git 지원은 VCS 메뉴에 내장되어 있습니다.
- `Shift+Shift`로 Search Everywhere 대화상자를 엽니다.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`)로 코드를 재포맷합니다.
- plugin을 통해 언어 지원을 확장하고 추가 도구를 붙일 수 있습니다.

### 터미널 팁

- tab completion을 활용하면 파일명과 명령을 빠르게 완성할 수 있습니다.
- `Ctrl+R`을 누르면 command history를 대화식으로 검색할 수 있습니다.
- `alias ll='ls -la'`처럼 별칭을 만들고 `~/.bashrc`나 `~/.zshrc`에 추가해 둘 수 있습니다.
- 원격 서버에서 연결이 끊겨도 작업을 유지하려면 `tmux`나 `screen`을 사용합니다.
- `man <command>`는 각 built-in command나 유틸리티의 manual page를 보여줍니다.

---

## Docker

Docker는 애플리케이션과 그 의존성을 portable container로 묶어 배포할 수 있게 해 줍니다.

### 핵심 개념

- **Image**: `Dockerfile`로부터 만들어지는 읽기 전용 템플릿
- **Container**: image를 실행한 인스턴스
- **Registry**: image를 저장하고 배포하는 서비스(Docker Hub, GHCR)
- **Volume**: container 수명과 별개로 유지되는 영구 저장소

### 자주 쓰는 명령

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

### Dockerfile 예시

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose는 `docker-compose.yml` 파일 하나로 여러 container로 구성된 애플리케이션을 관리합니다.

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
