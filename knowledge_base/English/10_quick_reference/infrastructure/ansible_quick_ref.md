<!--
---
# Metadata
title: "Ansible and Configuration Management"
description: "Ansible playbooks, modules, roles, inventory, automation cheat sheet"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.1"
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
# Ansible and Configuration Management

Ansible is an agentless configuration management and automation tool. It uses SSH (or WinRM for Windows) to connect to servers and execute tasks defined in YAML playbooks. Unlike tools that require agents installed on every machine, Ansible is push-based — you run commands from a control node. It's used for server provisioning, application deployment, configuration management, and ad-hoc task execution.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Inventory** | List of managed hosts (INI or YAML format) |
| **Playbook** | YAML file defining a set of tasks to execute |
| **Play** | A mapping between hosts and tasks within a playbook |
| **Task** | A single action to perform on a host |
| **Module** | A unit of work (e.g., `apt`, `copy`, `service`, `template`) |
| **Role** | Reusable collection of tasks, variables, files, and handlers |
| **Variable** | Dynamic values used in playbooks |
| **Handler** | Task triggered by a notification (e.g., restart service) |
| **Fact** | System information gathered about hosts (OS, IP, etc.) |

---

## Common Commands

| Command | Description |
|---------|-------------|
| `ansible all -m ping` | Test connectivity to all hosts |
| `ansible all -m shell -a "uptime"` | Run a shell command on all hosts |
| `ansible-playbook site.yml` | Execute a playbook |
| `ansible-playbook site.yml --check` | Dry run (check mode) |
| `ansible-playbook site.yml --diff` | Show what would change |
| `ansible-playbook site.yml -l web` | Run against a specific group |
| `ansible-playbook site.yml --tags deploy` | Run only tasks with specific tags |
| `ansible-playbook site.yml --skip-tags debug` | Skip tasks with specific tags |
| `ansible-vault encrypt secrets.yml` | Encrypt a file |
| `ansible-vault decrypt secrets.yml` | Decrypt a file |
| `ansible-vault edit secrets.yml` | Edit an encrypted file |
| `ansible-galaxy install geerlingguy.nginx` | Install a role from Ansible Galaxy |
| `ansible-inventory --graph` | Display inventory as a graph |
| `ansible-doc apt` | Show documentation for a module |

---

## Inventory Formats

### INI Format

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

### YAML Format

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

## Playbook Structure

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

## Common Modules

| Module | Purpose | Example |
|--------|---------|---------|
| **apt / yum / dnf** | Package management | `apt: name=nginx state=present` |
| **copy** | Copy files to hosts | `copy: src=file.txt dest=/tmp/` |
| **template** | Copy files with Jinja2 variables | `template: src=conf.j2 dest=/etc/app.conf` |
| **file** | Manage files and directories | `file: path=/tmp/dir state=directory` |
| **service** | Manage services | `service: name=nginx state=restarted` |
| **user / group** | Manage users and groups | `user: name=deploy shell=/bin/bash` |
| **cron** | Manage cron jobs | `cron: name="backup" job="/usr/bin/backup.sh"` |
| **shell / command** | Run commands | `shell: echo "hello" > /tmp/test` |
| **git** | Clone repositories | `git: repo=https://... dest=/opt/app` |
| **systemd** | Manage systemd units | `systemd: name=myapp enabled=true` |
| **firewalld / ufw** | Manage firewall rules | `ufw: rule=allow port=80 proto=tcp` |
| **lineinfile** | Manage lines in files | `lineinfile: path=/etc/hosts line="..."` |
| **blockinfile** | Manage blocks of text in files | Insert/update blocks of configuration |
| **fetch** | Copy files from hosts | `fetch: src=/var/log/app.log dest=/local/` |
| **uri** | Interact with web services | `uri: url=https://api.example.com method=GET` |
| **debug** | Print messages | `debug: msg="Deployed {{ app_version }}"` |

---

## Role Structure

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

## Tips and Troubleshooting

| Tip | Description |
|-----|-------------|
| **Use check mode** | Always `--check --diff` before applying changes |
| **Use tags** | Tag tasks for selective execution |
| **Use vault for secrets** | Never store passwords in plain text |
| **Idempotency** | Tasks should be safe to run multiple times |
| **Use become** | Use `become: true` for privilege escalation |
| **Limit parallelism** | Use `--forks` to control concurrent connections |
| **Test with Vagrant / Docker** | Test playbooks locally before running on production |
| **Use `--step`** | Interactive mode: confirm each task before execution |

---

## Summary

Ansible automates server configuration and application deployment through YAML playbooks executed over SSH. The workflow is: define inventory → write playbooks → run `ansible-playbook`. Key concepts include modules (units of work), roles (reusable collections), handlers (triggered tasks), and variables (dynamic values). Common modules cover package management, file operations, service control, and user management. Always use check mode before applying; store secrets in Ansible Vault; ensure tasks are idempotent; and test locally before running on production.
