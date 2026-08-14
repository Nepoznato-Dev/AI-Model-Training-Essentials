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
# Pamamahala ng Ansible at Configuration
Ang Ansible ay isang walang ahente na pamamahala sa pagsasaayos at tool sa automation. Gumagamit ito ng SSH (o WinRM para sa Windows) upang kumonekta sa mga server at magsagawa ng mga gawain na tinukoy sa mga playbook ng YAML. Hindi tulad ng mga tool na nangangailangan ng mga ahente na naka-install sa bawat makina, ang Ansible ay nakabatay sa push — nagpapatakbo ka ng mga command mula sa isang control node. Ginagamit ito para sa provisioning ng server, deployment ng application, pamamahala ng configuration, at ad-hoc task execution.
---

## Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Imbentaryo** | Listahan ng mga pinamamahalaang host (INI o YAML na format) |
| **Playbook** | YAML file na tumutukoy sa isang hanay ng mga gawain na isasagawa |
| **Play** | Isang pagmamapa sa pagitan ng mga host at mga gawain sa loob ng isang playbook |
| **Gawain** | Isang pagkilos na gagawin sa isang host |
| **Modyul** | Isang yunit ng trabaho (hal.,`apt`,`copy`,`service`,`template`) |
| **Tungkulin** | Magagamit muli na koleksyon ng mga gawain, variable, file, at tagapangasiwa |
| **Variable** | Mga dynamic na halaga na ginagamit sa mga playbook |
| **Handler** | Gawain na na-trigger ng isang notification (hal., i-restart ang serbisyo) |
| **Katotohanan** | Nakalap ang impormasyon ng system tungkol sa mga host (OS, IP, atbp.) |
---

## Mga Karaniwang Utos
| Utos | Paglalarawan |
|---------|-------------|
| `ansible all -m ping`| Subukan ang pagkakakonekta sa lahat ng host |
| `ansible all -m shell -a "uptime"`| Magpatakbo ng shell command sa lahat ng host |
| `ansible-playbook site.yml`| Magsagawa ng playbook |
| `ansible-playbook site.yml --check`| Dry run (check mode) |
| `ansible-playbook site.yml --diff`| Ipakita kung ano ang magbabago |
| `ansible-playbook site.yml -l web`| Tumakbo laban sa isang partikular na grupo |
| `ansible-playbook site.yml --tags deploy`| Patakbuhin lamang ang mga gawain na may mga partikular na tag |
| `ansible-playbook site.yml --skip-tags debug`| Laktawan ang mga gawain na may mga partikular na tag |
| `ansible-vault encrypt secrets.yml`| I-encrypt ang isang file |
| `ansible-vault decrypt secrets.yml`| I-decrypt ang isang file |
| `ansible-vault edit secrets.yml`| Mag-edit ng naka-encrypt na file |
| `ansible-galaxy install geerlingguy.nginx`| Mag-install ng tungkulin mula sa Ansible Galaxy |
| `ansible-inventory --graph`| Ipakita ang imbentaryo bilang isang graph |
| `ansible-doc apt`| Ipakita ang dokumentasyon para sa isang module |
---

## Mga Format ng Imbentaryo
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

### Format ng YAML
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

## Istraktura ng Playbook
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

## Mga Karaniwang Module
| Module | Layunin | Halimbawa |
|--------|---------|---------|
| **apt / yum / dnf** | Pamamahala ng package | `apt: name=nginx state=present`|
| **kopya** | Kopyahin ang mga file sa mga host | `copy: src=file.txt dest=/tmp/`|
| **template** | Kopyahin ang mga file na may mga variable ng Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **file** | Pamahalaan ang mga file at direktoryo | `file: path=/tmp/dir state=directory`|
| **serbisyo** | Pamahalaan ang mga serbisyo | `service: name=nginx state=restarted`|
| **user / pangkat** | Pamahalaan ang mga user at pangkat | `user: name=deploy shell=/bin/bash`|
| **cron** | Pamahalaan ang mga cron job | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **shell / command** | Patakbuhin ang mga utos | `shell: echo "hello" > /tmp/test`|
| **git** | I-clone ang mga repository | `git: repo=https://... dest=/opt/app`|
| **systemd** | Pamahalaan ang mga systemd unit | `systemd: name=myapp enabled=true`|
| **firewalld / ufw** | Pamahalaan ang mga panuntunan sa firewall | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Pamahalaan ang mga linya sa mga file | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | Pamahalaan ang mga bloke ng teksto sa mga file | Ipasok/i-update ang mga bloke ng configuration |
| **kunin** | Kopyahin ang mga file mula sa mga host | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Makipag-ugnayan sa mga serbisyo sa web | `uri: url=https://api.example.com method=GET`|
| **debug** | Mag-print ng mga mensahe | `debug: msg="Deployed {{ app_version }}"`|
---

## Istraktura ng Tungkulin
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

## Mga Tip at Pag-troubleshoot
| Tip | Paglalarawan |
|-----|-------------|
| **Gumamit ng check mode** | Palaging`--check --diff`bago ilapat ang mga pagbabago |
| **Gumamit ng mga tag** | I-tag ang mga gawain para sa piling pagpapatupad |
| **Gumamit ng vault para sa mga lihim** | Huwag kailanman mag-imbak ng mga password sa plain text |
| **Idempotency** | Ang mga gawain ay dapat na ligtas na tumakbo nang maraming beses |
| **Gamitin ang pagiging** | Gamitin ang`become: true`para sa pagtaas ng pribilehiyo |
| **Limitahan ang paralelismo** | Gamitin ang`--forks`upang kontrolin ang mga kasabay na koneksyon |
| **Pagsubok sa Vagrant / Docker** | Subukan ang mga playbook nang lokal bago tumakbo sa produksyon |
| **Gamitin ang`--step`** | Interactive mode: kumpirmahin ang bawat gawain bago isagawa |
---

## Buod
Ino-automate ng Ansible ang configuration ng server at pag-deploy ng application sa pamamagitan ng mga playbook ng YAML na isinasagawa sa SSH. Ang daloy ng trabaho ay: tukuyin ang imbentaryo → magsulat ng mga playbook → patakbuhin ang`ansible-playbook`. Kabilang sa mga pangunahing konsepto ang mga module (mga yunit ng trabaho), mga tungkulin (mga muling magagamit na koleksyon), mga tagapangasiwa (mga na-trigger na gawain), at mga variable (mga dynamic na halaga). Sinasaklaw ng mga karaniwang module ang pamamahala ng package, pagpapatakbo ng file, kontrol ng serbisyo, at pamamahala ng user. Palaging gumamit ng check mode bago mag-apply; mag-imbak ng mga lihim sa Ansible Vault; tiyakin na ang mga gawain ay idempotent; at subukan nang lokal bago tumakbo sa produksyon.