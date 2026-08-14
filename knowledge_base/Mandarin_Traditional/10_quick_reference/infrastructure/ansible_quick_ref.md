<!--
---
# Metadata
title: "Ansible and Configuration Management"
description: "Ansible playbooks, modules, roles, inventory, automation cheat sheet"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

-->
# Ansible 與設定管理
Ansible 是一種無代理程式設定管理和自動化工具。它使用 SSH（或 Windows 的 WinRM）連接到伺服器並執行 YAML playbook 中定義的任務。與需要在每台機器上安裝代理程式的工具不同，Ansible 是基於推送的——您從控制節點運行命令。它用於伺服器配置、應用程式部署、組態管理和臨時任務執行。
---

## 核心概念
|概念 |描述 |
|---------|-------------|
| **庫存** |託管主機清單（INI 或 YAML 格式）|
| **劇本** | YAML 檔案定義一組要執行的任務 |
| **玩** | Playbook 中主機與任務之間的對應 |
| **任務** |在主機上執行的單一操作 |
| **模組** |工作單元（例如`apt`、`copy`、`service`、`template`） |
| **角色** |可重複使用的任務、變數、檔案和處理程序集合 |
| **變數** |劇本中使用的動態值 |
| **處理程序** |由通知觸發的任務（例如，重新啟動服務） |
| **事實** |收集有關主機的系統資訊（作業系統、IP 等）|
---

## 常用指令
|命令 |描述 |
|---------|-------------|
|`ansible all -m ping`|測試與所有主機的連線 |
|`ansible all -m shell -a "uptime"`|在所有主機上執行 shell 指令 |
|`ansible-playbook site.yml`|執行劇本 |
|`ansible-playbook site.yml --check`|試運行（檢查模式）|
|`ansible-playbook site.yml --diff`|顯示會發生什麼變化 |
|`ansible-playbook site.yml -l web`|針對特定群體 |
|`ansible-playbook site.yml --tags deploy`|僅執行具有特定標籤的任務 |
|`ansible-playbook site.yml --skip-tags debug`|跳過帶有特定標籤的任務 |
|`ansible-vault encrypt secrets.yml`|加密檔案 |
|`ansible-vault decrypt secrets.yml`|解密檔 |
|`ansible-vault edit secrets.yml`|編輯加密檔案 |
|`ansible-galaxy install geerlingguy.nginx`|從 Ansible Galaxy 安裝角色 |
|`ansible-inventory --graph`|以圖表形式顯示庫存 |
|`ansible-doc apt`|顯示模組的文檔 |
---

## 庫存格式
### INI 格式
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

### YAML 格式
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

## 劇本結構
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

## 常用模組
|模組|目的|範例|
|--------|---------|---------|
| **apt / yum / dnf** |套件管理 |`apt: name=nginx state=present`|
| **複製** |將檔案複製到主機 |`copy: src=file.txt dest=/tmp/`|
| **模板** |使用 Jinja2 變數複製檔案 |`template: src=conf.j2 dest=/etc/app.conf`|
| **檔案** |管理檔案與目錄 |`file: path=/tmp/dir state=directory`|
| **服務** |管理服務 |`service: name=nginx state=restarted`|
| **使用者/群組** |管理使用者和群組 |`user: name=deploy shell=/bin/bash`|
| **計劃** |管理 cron 作業 |`cron: name="backup" job="/usr/bin/backup.sh"`|
| **外殼/指令** |執行指令 |`shell: echo "hello" > /tmp/test`|
| **git** |克隆儲存庫 |`git: repo=https://... dest=/opt/app`|
| **系統** |管理 systemd 單元 |`systemd: name=myapp enabled=true`|
| **防火牆/ufw** |管理防火牆規則 |`ufw: rule=allow port=80 proto=tcp`|
| **文件行** |管理文件中的行 |`lineinfile: path=/etc/hosts line="..."`|
| **區塊檔案** |管理文件中的文字區塊 |插入/更新設定區塊 |
| **取得** |從主機複製檔案 |`fetch: src=/var/log/app.log dest=/local/`|
| **烏裡** |與網路服務互動 |`uri: url=https://api.example.com method=GET`|
| **調試** |列印訊息 |`debug: msg="Deployed {{ app_version }}"`|
---

## 角色結構
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

## 提示和故障排除
|提示 |描述 |
|-----|-------------|
| **使用檢查模式** |應用更改之前始終`--check --diff`|
| **使用標籤** |標記任務以選擇性執行 |
| **使用保管庫來保存秘密** |切勿以純文字形式儲存密碼 |
| **冪等性** |任務應該可以安全地運行多次 |
| **使用成為** |使用`become: true`進行權限提升 |
| **限制並行性** |使用`--forks`控制同時連線 |
| **使用 Vagrant / Docker 進行測試** |在生產環境中運行之前在本地測試 playbook |
| **使用`--step`** |互動模式：執行前確認每項任務 |
---

＃＃ 概括
Ansible 透過透過 SSH 執行的 YAML playbook 自動執行伺服器設定和應用程式部署。工作流程是：定義清單→寫劇本→執行`ansible-playbook`。關鍵概念包括模組（工作單元）、角色（可重複使用集合）、處理程序（觸發的任務）和變數（動態值）。常用模組涵蓋套件管理、檔案操作、服務控制、使用者管理等。申請前始終使用檢查模式；將機密儲存在 Ansible Vault 中；確保任務是冪等的；並在生產環境中運行之前進行本地測試。