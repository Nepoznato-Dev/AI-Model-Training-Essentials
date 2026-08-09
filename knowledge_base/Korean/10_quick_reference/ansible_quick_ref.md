---
# Metadata
title: "Ansible and Configuration Management"
description: "Ansible playbooks, modules, roles, inventory, automation cheat sheet"
category: "Quick Reference"
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
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ansible, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Ansible 및 구성 관리
Ansible은 에이전트 없는 구성 관리 및 자동화 도구입니다. SSH(또는 Windows용 WinRM)를 사용하여 서버에 연결하고 YAML 플레이북에 정의된 작업을 실행합니다. 모든 머신에 에이전트를 설치해야 하는 도구와 달리 Ansible은 푸시 기반이므로 제어 노드에서 명령을 실행합니다. 서버 프로비저닝, 애플리케이션 배포, 구성 관리 및 임시 작업 실행에 사용됩니다.
---

## 핵심 개념
| 개념 | 설명 |
|---------|-------------|
| **인벤토리** | 관리 호스트 목록(INI 또는 YAML 형식) |
| **플레이북** | 실행할 작업 세트를 정의하는 YAML 파일 |
| **플레이** | 플레이북 내 호스트와 작업 간의 매핑 |
| **작업** | 호스트에서 수행할 단일 작업 |
| **모듈** | 작업 단위(예:`apt`,`copy`,`service`,`template`) |
| **역할** | 작업, 변수, 파일 및 핸들러의 재사용 가능한 컬렉션 |
| **변수** | 플레이북에 사용되는 동적 값 |
| **핸들러** | 알림(예: 서비스 다시 시작)에 의해 트리거되는 작업 |
| **사실** | 호스트(OS, IP 등)에 대해 수집된 시스템 정보 |
---

## 일반적인 명령
| 명령 | 설명 |
|---------|-------------|
| `ansible all -m ping`| 모든 호스트에 대한 연결 테스트 |
| `ansible all -m shell -a "uptime"`| 모든 호스트에서 쉘 명령 실행 |
| `ansible-playbook site.yml`| 플레이북 실행 |
| `ansible-playbook site.yml --check`| 모의 실행(검사 모드) |
| `ansible-playbook site.yml --diff`| 무엇이 바뀔지 보여주세요 |
| `ansible-playbook site.yml -l web`| 특정 그룹에 대해 실행 |
| `ansible-playbook site.yml --tags deploy`| 특정 태그가 있는 작업만 실행 |
| `ansible-playbook site.yml --skip-tags debug`| 특정 태그가 있는 작업 건너뛰기 |
| `ansible-vault encrypt secrets.yml`| 파일 암호화 |
| `ansible-vault decrypt secrets.yml`| 파일 암호 해독 |
| `ansible-vault edit secrets.yml`| 암호화된 파일 편집 |
| `ansible-galaxy install geerlingguy.nginx`| Ansible Galaxy에서 역할 설치 |
| `ansible-inventory --graph`| 재고를 그래프로 표시 |
| `ansible-doc apt`| 모듈에 대한 문서 표시 |
---

## 인벤토리 형식
### INI 형식
```ini
[web]
web1.example.com
web2.example.com

[db]
db1.example.com ansible_user=deploy

[production:children]
web
db
```

### YAML 형식
```yaml
all:
  children:
    web:
      hosts:
        web1:
          ansible_host: 10.0.0.1
        web2:
          ansible_host: 10.0.0.2
    db:
      hosts:
        db1:
          ansible_user: deploy
```

---

## 플레이북 구조
```yaml
---
- name: Deploy web application
  hosts: web
  become: true
  vars:
    app_port: 8080
  
  tasks:
    - name: Install dependencies
      apt:
        name: ['nginx', 'python3', 'git']
        state: present
        update_cache: true

    - name: Copy application config
      template:
        src: templates/app.conf.j2
        dest: /etc/app/config.conf
      notify: Restart application

    - name: Ensure service is running
      service:
        name: myapp
        state: started
        enabled: true

  handlers:
    - name: Restart application
      service:
        name: myapp
        state: restarted
```

---

## 공통 모듈
| 모듈 | 목적 | 예 |
|---------|---------|---------|
| **적합 / 냠 / dnf** | 패키지 관리 | `apt: name=nginx state=present`|
| **복사** | 호스트에 파일 복사 | `copy: src=file.txt dest=/tmp/`|
| **템플릿** | Jinja2 변수를 사용하여 파일 복사 | `template: src=conf.j2 dest=/etc/app.conf`|
| **파일** | 파일 및 디렉터리 관리 | `file: path=/tmp/dir state=directory`|
| **서비스** | 서비스 관리 | `service: name=nginx state=restarted`|
| **사용자/그룹** | 사용자 및 그룹 관리 | `user: name=deploy shell=/bin/bash`|
| **크론** | 크론 작업 관리 | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **셸/명령** | 명령 실행 | `shell: echo "hello" > /tmp/test`|
| **자기** | 클론 저장소 | `git: repo=https://... dest=/opt/app`|
| **시스템** | 시스템 단위 관리 | `systemd: name=myapp enabled=true`|
| **방화벽 / ufw** | 방화벽 규칙 관리 | `ufw: rule=allow port=80 proto=tcp`|
| **라인 파일** | 파일의 줄 관리 | `lineinfile: path=/etc/hosts line="..."`|
| **블록인파일** | 파일의 텍스트 블록 관리 | 구성 블록 삽입/업데이트 |
| **가져오기** | 호스트에서 파일 복사 | `fetch: src=/var/log/app.log dest=/local/`|
| **우리** | 웹 서비스와 상호작용 | `uri: url=https://api.example.com method=GET`|
| **디버그** | 메시지 인쇄 | `debug: msg="Deployed {{ app_version }}"`|
---

## 역할 구조
```
role_name/
├── tasks/
│   └── main.yml       # Main task list
├── handlers/
│   └── main.yml       # Handlers
├── templates/
│   └── *.j2           # Jinja2 templates
├── files/
│   └── *              # Static files
├── vars/
│   └── main.yml       # Role variables (high priority)
├── defaults/
│   └── main.yml       # Default variables (low priority)
├── meta/
│   └── main.yml       # Role metadata and dependencies
└── README.md
```

---

## 팁 및 문제 해결
| 팁 | 설명 |
|------|-------------|
| **체크 모드 사용** | 변경 사항을 적용하기 전에 항상`--check --diff`|
| **태그 사용** | 선택적 실행을 위한 태그 작업 |
| **비밀 보관소 사용** | 비밀번호를 일반 텍스트로 저장하지 마세요 |
| **멱등성** | 작업은 여러 번 실행해도 안전해야 합니다 |
| **사용하기** | 권한 상승을 위해`become: true`사용 |
| **병렬성 제한** | `--forks`를 사용하여 동시 연결 제어 |
| **Vagrant/Docker로 테스트** | 프로덕션 환경에서 실행하기 전에 로컬에서 플레이북 테스트 |
| **`--step` 사용 ** | 대화형 모드: 실행 전 각 작업 확인 |
---

## 요약
Ansible은 SSH를 통해 실행되는 YAML 플레이북을 통해 서버 구성 및 애플리케이션 배포를 자동화합니다. 워크플로우는 인벤토리 정의 → 플레이북 작성 →`ansible-playbook`실행입니다. 주요 개념에는 모듈(작업 단위), 역할(재사용 가능한 컬렉션), 처리기(트리거된 작업) 및 변수(동적 값)가 포함됩니다. 공통 모듈에는 패키지 관리, 파일 작업, 서비스 제어 및 사용자 관리가 포함됩니다. 적용하기 전에 항상 확인 모드를 사용하십시오. Ansible Vault에 비밀을 저장합니다. 작업이 멱등성을 유지하는지 확인하세요. 프로덕션 환경에서 실행하기 전에 로컬에서 테스트하세요.