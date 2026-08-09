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

# Ansible 和配置管理
Ansible 是一种无代理配置管理和自动化工具。它使用 SSH（或 Windows 的 WinRM）连接到服务器并执行 YAML playbook 中定义的任务。与需要在每台机器上安装代理的工具不同，Ansible 是基于推送的——您从控制节点运行命令。它用于服务器配置、应用程序部署、配置管理和临时任务执行。
---

## 核心概念
|概念 |描述 |
|---------|-------------|
| **库存** |托管主机列表（INI 或 YAML 格式）|
| **剧本** | YAML 文件定义一组要执行的任务 |
| **玩** | Playbook 中主机和任务之间的映射 |
| **任务** |在主机上执行的单个操作 |
| **模块** |工作单元（例如`apt`、`copy`、`service`、`template`） |
| **角色** |可重用的任务、变量、文件和处理程序集合 |
| **变量** |剧本中使用的动态值 |
| **处理程序** |由通知触发的任务（例如，重新启动服务） |
| **事实** |收集有关主机的系统信息（操作系统、IP 等）|
---

## 常用命令
|命令 |描述 |
|---------|-------------|
| `ansible all -m ping`|测试与所有主机的连接 |
| `ansible all -m shell -a "uptime"`|在所有主机上运行 shell 命令 |
| `ansible-playbook site.yml`|执行剧本 |
| `ansible-playbook site.yml --check`|试运行（检查模式）|
| `ansible-playbook site.yml --diff`|显示会发生什么变化 |
| `ansible-playbook site.yml -l web`|针对特定群体 |
| `ansible-playbook site.yml --tags deploy`|仅运行具有特定标签的任务 |
| `ansible-playbook site.yml --skip-tags debug`|跳过带有特定标签的任务 |
| `ansible-vault encrypt secrets.yml`|加密文件 |
| `ansible-vault decrypt secrets.yml`|解密文件 |
| `ansible-vault edit secrets.yml`|编辑加密文件 |
| `ansible-galaxy install geerlingguy.nginx`|从 Ansible Galaxy 安装角色 |
| `ansible-inventory --graph`|以图表形式显示库存 |
| `ansible-doc apt`|显示模块的文档 |
---

## 库存格式
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

## 剧本结构
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

## 常用模块
|模块|目的|示例|
|--------|---------|---------|
| **apt / yum / dnf** |包管理 | `apt: name=nginx state=present`|
| **复制** |将文件复制到主机 | `copy: src=file.txt dest=/tmp/`|
| **模板** |使用 Jinja2 变量复制文件 | `template: src=conf.j2 dest=/etc/app.conf`|
| **文件** |管理文件和目录 | `file: path=/tmp/dir state=directory`|
| **服务** |管理服务 | `service: name=nginx state=restarted`|
| **用户/组** |管理用户和组 | `user: name=deploy shell=/bin/bash`|
| **计划** |管理 cron 作业 | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **外壳/命令** |运行命令 | `shell: echo "hello" > /tmp/test`|
| **git** |克隆存储库 | `git: repo=https://... dest=/opt/app`|
| **系统** |管理 systemd 单元 | `systemd: name=myapp enabled=true`|
| **防火墙/ufw** |管理防火墙规则 | `ufw: rule=allow port=80 proto=tcp`|
| **文件行** |管理文件中的行 | `lineinfile: path=/etc/hosts line="..."`|
| **块文件** |管理文件中的文本块 |插入/更新配置块 |
| **获取** |从主机复制文件 | `fetch: src=/var/log/app.log dest=/local/`|
| **乌里** |与网络服务交互 | `uri: url=https://api.example.com method=GET`|
| **调试** |打印消息 | `debug: msg="Deployed {{ app_version }}"`|
---

## 角色结构
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
| **使用检查模式** |应用更改之前始终`--check --diff`|
| **使用标签** |标记任务以选择性执行 |
| **使用保管库来保存秘密** |切勿以纯文本形式存储密码 |
| **幂等性** |任务应该可以安全地运行多次 |
| **使用成为** |使用`become: true`进行权限提升 |
| **限制并行性** |使用`--forks`控制并发连接 |
| **使用 Vagrant / Docker 进行测试** |在生产环境中运行之前在本地测试 playbook |
| **使用`--step`** |交互模式：执行前确认每项任务|
---

＃＃ 概括
Ansible 通过通过 SSH 执行的 YAML playbook 自动执行服务器配置和应用程序部署。工作流程是：定义清单→编写剧本→运行`ansible-playbook`。关键概念包括模块（工作单元）、角色（可重用集合）、处理程序（触发的任务）和变量（动态值）。常用模块涵盖包管理、文件操作、服务控制、用户管理等。申请前始终使用检查模式；将机密存储在 Ansible Vault 中；确保任务是幂等的；并在生产环境中运行之前进行本地测试。