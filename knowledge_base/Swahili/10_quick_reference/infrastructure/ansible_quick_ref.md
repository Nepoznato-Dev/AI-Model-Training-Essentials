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
# Usimamizi unaowezekana na wa Usanidi
Ansible ni usimamizi wa usanidi usio na wakala na zana ya kiotomatiki. Inatumia SSH (au WinRM kwa Windows) kuunganisha kwenye seva na kutekeleza majukumu yaliyofafanuliwa katika vitabu vya kucheza vya YAML. Tofauti na zana zinazohitaji mawakala kusakinishwa kwenye kila mashine, Ansible inategemea programu-tumizi - unaendesha amri kutoka kwa nodi ya udhibiti. Inatumika kwa utoaji wa seva, upelekaji wa programu, usimamizi wa usanidi, na utekelezaji wa kazi ya ad-hoc.
---

## Dhana za Msingi
| Dhana | Maelezo |
|---------|-------------|
| **Mali** | Orodha ya wapangishi wanaosimamiwa (umbizo la INI au YAML) |
| **Kitabu cha kucheza** | faili ya YAML inayofafanua seti ya kazi za kutekeleza |
| **Cheza** | Ramani kati ya wapangishaji na kazi ndani ya kitabu cha kucheza |
| **Kazi** | Kitendo kimoja cha kuigiza kwa mwenyeji |
| **Moduli** | Kitengo cha kazi (k.m.,`apt`,`copy`,`service`,`template`) |
| **Jukumu** | Mkusanyiko unaoweza kutumika tena wa kazi, vigeu, faili na vidhibiti |
| **Kigezo** | Thamani zinazobadilika zinazotumika katika vitabu vya kucheza |
| **Kidhibiti** | Jukumu lililoanzishwa na arifa (k.m., anzisha huduma upya) |
| **Ukweli** | Taarifa za mfumo zilizokusanywa kuhusu seva pangishi (OS, IP, n.k.) |
---

## Amri za kawaida
| Amri | Maelezo |
|---------|-------------|
| `ansible all -m ping`| Jaribu muunganisho kwa wapangishi wote |
| `ansible all -m shell -a "uptime"`| Tekeleza amri ya ganda kwa wapangishaji wote |
| `ansible-playbook site.yml`| Tekeleza kitabu cha kucheza |
| `ansible-playbook site.yml --check`| Kukimbia kavu (hali ya kuangalia) |
| `ansible-playbook site.yml --diff`| Onyesha nini kitabadilika |
| `ansible-playbook site.yml -l web`| Kimbia dhidi ya kikundi maalum |
| `ansible-playbook site.yml --tags deploy`| Endesha kazi ukitumia lebo maalum |
| `ansible-playbook site.yml --skip-tags debug`| Ruka kazi zilizo na lebo maalum |
| `ansible-vault encrypt secrets.yml`| Simba faili |
| `ansible-vault decrypt secrets.yml`| Simbua faili |
| `ansible-vault edit secrets.yml`| Hariri faili iliyosimbwa kwa njia fiche |
| `ansible-galaxy install geerlingguy.nginx`| Sakinisha jukumu kutoka Ansible Galaxy |
| `ansible-inventory --graph`| Onyesha orodha kama grafu |
| `ansible-doc apt`| Onyesha hati za moduli |
---

## Miundo ya Malipo
### Umbizo la INI
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

### Umbizo la YAML
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

## Muundo wa Kitabu cha kucheza
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

## Moduli za Kawaida
| Moduli | Kusudi | Mfano |
|--------|--------------------|
| **apt / yum / dnf** | Usimamizi wa kifurushi | `apt: name=nginx state=present`|
| **nakala** | Nakili faili kwa wapangishi | `copy: src=file.txt dest=/tmp/`|
| **kiolezo** | Nakili faili zilizo na anuwai za Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **faili** | Dhibiti faili na saraka | `file: path=/tmp/dir state=directory`|
| **huduma** | Dhibiti huduma | `service: name=nginx state=restarted`|
| **mtumiaji / kikundi** | Dhibiti watumiaji na vikundi | `user: name=deploy shell=/bin/bash`|
| **cron** | Dhibiti kazi za cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **ganda / amri** | Endesha amri | `shell: echo "hello" > /tmp/test`|
| **git** | Hazina za Clone | `git: repo=https://... dest=/opt/app`|
| **mfumo** | Dhibiti vitengo vya mfumo | `systemd: name=myapp enabled=true`|
| **firewall / ufw** | Dhibiti sheria za ngome | `ufw: rule=allow port=80 proto=tcp`|
| **faili ya mstari** | Dhibiti mistari katika faili | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | Dhibiti vizuizi vya maandishi katika faili | Ingiza/sasisha vizuizi vya usanidi |
| **chota** | Nakili faili kutoka kwa wapangishi | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Wasiliana na huduma za wavuti | `uri: url=https://api.example.com method=GET`|
| **tatua** | Chapisha ujumbe | `debug: msg="Deployed {{ app_version }}"`|
---

## Muundo wa Wajibu
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

## Vidokezo na Utatuzi
| Kidokezo | Maelezo |
|-----|--------------|
| **Tumia hali ya kuangalia** | Daima`--check --diff`kabla ya kutumia mabadiliko |
| **Tumia lebo** | Tagi kazi za utekelezaji uliochaguliwa |
| **Tumia vault kwa siri** | Usiwahi kuhifadhi manenosiri katika maandishi wazi |
| **Upungufu** | Majukumu yanapaswa kuwa salama kutekeleza mara nyingi |
| **Tumia kuwa** | Tumia`become: true`kwa ukuzaji wa fursa |
| **Punguza usawaziko** | Tumia`--forks`ili kudhibiti miunganisho inayotumika wakati mmoja |
| **Jaribio na Vagrant / Docker** | Jaribu vitabu vya kucheza ndani ya nchi kabla ya kuendeshwa kwenye toleo la umma |
| **Tumia`--step`** | Hali ya mwingiliano: thibitisha kila kazi kabla ya utekelezaji |
---

## Muhtasari
Ansible huweka kiotomatiki usanidi wa seva na utumaji programu kupitia vitabu vya kucheza vya YAML vinavyotekelezwa kupitia SSH. Mtiririko wa kazi ni: fafanua orodha → andika vitabu vya kucheza → endesha`ansible-playbook`. Dhana muhimu ni pamoja na moduli (vitengo vya kazi), majukumu (mikusanyiko inayoweza kutumika tena), vidhibiti (kazi zilizoanzishwa), na vigeu (vigezo vinavyobadilika). Moduli za kawaida hufunika usimamizi wa kifurushi, uendeshaji wa faili, udhibiti wa huduma, na usimamizi wa mtumiaji. Daima tumia hali ya kuangalia kabla ya kutumia; kuhifadhi siri katika Vault Ansible; hakikisha kuwa kazi ni duni; na jaribu ndani ya nchi kabla ya kuanza uzalishaji.