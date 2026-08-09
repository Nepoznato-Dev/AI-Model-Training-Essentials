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
# 도구 사용법
## Git — 버전 관리
Git은 분산 버전 관리 시스템입니다. 모든 개발자는 자신의 로컬 컴퓨터에 저장소 기록의 전체 복사본을 가지고 있습니다.
### 핵심 워크플로우
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

### 분기
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### 병합 및 리베이스
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### 끌어오기 요청(PR) 워크플로
1.`main`에서 기능 분기를 생성합니다.
2. 기능 분기에 커밋을 수행합니다.
3. 분기를 푸시합니다:`git push origin feature/new-thing`.
4. GitHub/GitLab에서 풀 요청을 엽니다.
5. 추가 커밋을 통해 코드 검토 피드백을 처리합니다.
6. 승인되면 PR을 병합합니다.
### 변경사항 취소 중
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## 패키지 관리자
### 핍(파이썬)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

프로젝트 종속성을 격리하려면 항상 가상 환경 내에서 작업하세요.
### npm(Node.js/자바스크립트)
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

`package-lock.json`은 정확한 버전을 기록합니다. 소스 제어에 커밋합니다.
### 화물(러스트)
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

### Go 모듈(Go)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (데비안/우분투 리눅스)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## 명령줄 기본 사항
### 탐색
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

### 파이프 및 리디렉션
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### 네트워크 및 파일 전송
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### 권한
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

## 편집기 및 IDE
### VS 코드
VS Code는 풍부한 확장 에코시스템을 갖춘 경량의 크로스 플랫폼 코드 편집기입니다.
- 터미널에서`File > Open Folder`또는`code .`폴더를 엽니다.
- 명령 팔레트:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`).
- 통합 터미널:`Ctrl+`` (backtick)` .
- 다중 커서:`Alt+Click`추가 커서를 배치합니다.
- 정의로 이동:`F12`.
- 기호 이름 바꾸기:`F2`.
- 문서 형식:`Shift+Alt+F`.
- 확장: 확장 패널(`Ctrl+Shift+X`)에서 언어 지원(Python, Rust, Go 등), 린터 및 포맷터를 설치합니다.
- `settings.json`(사용자 또는 작업공간)은 편집기 동작을 제어합니다.
- `launch.json`는 디버거를 구성합니다.
### JetBrains IDE(IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- 스마트 코드 완성 및 리팩토링이 핵심 기능입니다.
- 실행/디버그 구성을 사용하면 한 번의 클릭으로 프로그램을 시작하고 디버그할 수 있습니다.
- VCS 메뉴에 Git 지원이 내장되어 있습니다.
- `Shift+Shift`는 모든 곳에서 검색 대화 상자를 엽니다.
- `Ctrl+Alt+L`(macOS: `Cmd+Option+L`)은 코드 형식을 다시 지정합니다.
- 플러그인은 언어 지원을 확장하고 도구를 추가합니다.
### 터미널 팁
- 탭 완성을 사용하여 파일 이름과 명령을 빠르게 완료합니다.
- 대화형으로 명령 기록을 검색하려면 `Ctrl+R`을 누르세요.
- `alias ll='ls -la'`은 바로가기를 생성합니다. 이를`~/.bashrc`또는 `~/.zshrc`에 추가하세요.
- 원격 서버와의 연결이 끊어졌을 때 세션을 활성 상태로 유지하려면`tmux`또는 `screen`를 사용하십시오.
- `man <command>`은 내장 명령에 대한 매뉴얼 페이지를 표시합니다.
---

## 도커
Docker는 애플리케이션과 해당 종속성을 휴대용 컨테이너로 패키징합니다.
### 핵심 개념
- **이미지**:`Dockerfile`에서 빌드된 읽기 전용 템플릿입니다.
- **컨테이너**: 실행 중인 이미지 인스턴스입니다.
- **레지스트리**: 이미지 저장 및 배포 서비스(Docker Hub, GHCR).
- **볼륨**: 컨테이너보다 수명이 긴 영구 스토리지입니다.
### 일반적인 명령
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

### Dockerfile 예
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### 도커 작성
Docker Compose는`docker-compose.yml`파일을 사용하여 다중 컨테이너 애플리케이션을 관리합니다.
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
