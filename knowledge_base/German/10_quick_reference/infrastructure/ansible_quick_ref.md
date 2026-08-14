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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Ansible und Konfigurationsmanagement
Ansible ist ein agentenloses Konfigurationsmanagement- und Automatisierungstool. Es verwendet SSH (oder WinRM für Windows), um eine Verbindung zu Servern herzustellen und in YAML-Playbooks definierte Aufgaben auszuführen. Im Gegensatz zu Tools, die die Installation von Agenten auf jedem Computer erfordern, ist Ansible Push-basiert – Sie führen Befehle von einem Kontrollknoten aus aus. Es wird für die Serverbereitstellung, Anwendungsbereitstellung, Konfigurationsverwaltung und Ad-hoc-Aufgabenausführung verwendet.
---

## Kernkonzepte
| Konzept | Beschreibung |
|---------|-------------|
| **Inventar** | Liste der verwalteten Hosts (INI- oder YAML-Format) |
| **Spielbuch** | YAML-Datei, die eine Reihe auszuführender Aufgaben definiert |
| **Spielen** | Eine Zuordnung zwischen Hosts und Aufgaben innerhalb eines Playbooks |
| **Aufgabe** | Eine einzelne Aktion, die auf einem Host ausgeführt werden soll |
| **Modul** | Eine Arbeitseinheit (z. B. `apt`, `copy`, `service`, `template`) |
| **Rolle** | Wiederverwendbare Sammlung von Aufgaben, Variablen, Dateien und Handlern |
| **Variable** | In Playbooks verwendete dynamische Werte |
| **Handler** | Durch eine Benachrichtigung ausgelöste Aufgabe (z. B. Dienst neu starten) |
| **Tatsache** | Gesammelte Systeminformationen über Hosts (Betriebssystem, IP usw.) |
---

## Allgemeine Befehle
| Befehl | Beschreibung |
|---------|-------------|
| `ansible all -m ping`| Konnektivität zu allen Hosts testen |
| `ansible all -m shell -a "uptime"`| Führen Sie einen Shell-Befehl auf allen Hosts aus |
| `ansible-playbook site.yml`| Führen Sie ein Playbook aus |
| `ansible-playbook site.yml --check`| Trockenlauf (Prüfmodus) |
| `ansible-playbook site.yml --diff`| Zeigen Sie, was sich ändern würde |
| `ansible-playbook site.yml -l web`| Gegen eine bestimmte Gruppe ausführen |
| `ansible-playbook site.yml --tags deploy`| Nur Aufgaben mit bestimmten Tags ausführen |
| `ansible-playbook site.yml --skip-tags debug`| Aufgaben mit bestimmten Tags überspringen |
| `ansible-vault encrypt secrets.yml`| Eine Datei verschlüsseln |
| `ansible-vault decrypt secrets.yml`| Eine Datei entschlüsseln |
| `ansible-vault edit secrets.yml`| Eine verschlüsselte Datei bearbeiten |
| `ansible-galaxy install geerlingguy.nginx`| Installieren Sie eine Rolle von Ansible Galaxy |
| `ansible-inventory --graph`| Lagerbestand als Diagramm anzeigen |
| `ansible-doc apt`| Dokumentation für ein Modul anzeigen |
---

## Inventarformate
### INI-Format
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

### YAML-Format
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

## Playbook-Struktur
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

## Gemeinsame Module
| Modul | Zweck | Beispiel |
|--------|---------|---------|
| **apt / yum / dnf** | Paketverwaltung | `apt: name=nginx state=present`|
| **kopieren** | Dateien auf Hosts kopieren | `copy: src=file.txt dest=/tmp/`|
| **Vorlage** | Dateien mit Jinja2-Variablen kopieren | `template: src=conf.j2 dest=/etc/app.conf`|
| **Datei** | Dateien und Verzeichnisse verwalten | `file: path=/tmp/dir state=directory`|
| **Dienst** | Dienste verwalten | `service: name=nginx state=restarted`|
| **Benutzer / Gruppe** | Benutzer und Gruppen verwalten | `user: name=deploy shell=/bin/bash`|
| **cron** | Cron-Jobs verwalten | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **Shell/Befehl** | Befehle ausführen | `shell: echo "hello" > /tmp/test`|
| **git** | Repositorys klonen | `git: repo=https://... dest=/opt/app`|
| **systemd** | Systemd-Einheiten verwalten | `systemd: name=myapp enabled=true`|
| **firewalld / ufw** | Firewallregeln verwalten | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Zeilen in Dateien verwalten | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | Textblöcke in Dateien verwalten | Konfigurationsblöcke einfügen/aktualisieren |
| **holen** | Dateien von Hosts kopieren | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Mit Webdiensten interagieren | `uri: url=https://api.example.com method=GET`|
| **Debug** | Nachrichten drucken | `debug: msg="Deployed {{ app_version }}"`|
---

## Rollenstruktur
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

## Tipps und Fehlerbehebung
| Tipp | Beschreibung |
|-----|-------------|
| **Prüfmodus verwenden** | Immer`--check --diff`vor dem Anwenden von Änderungen |
| **Tags verwenden** | Aufgaben zur selektiven Ausführung markieren |
| **Tresor für Geheimnisse verwenden** | Speichern Sie Passwörter niemals im Klartext |
| **Idempotenz** | Aufgaben sollten sicher mehrmals ausgeführt werden können |
| **Verwenden Sie werden** | Verwenden Sie`become: true`für die Rechteausweitung |
| **Parallelität begrenzen** | Verwenden Sie `--forks`, um gleichzeitige Verbindungen zu steuern |
| **Test mit Vagrant / Docker** | Testen Sie Playbooks lokal, bevor Sie sie in der Produktion ausführen |
| **Verwenden Sie`--step`** | Interaktiver Modus: Bestätigen Sie jede Aufgabe vor der Ausführung |
---

## Zusammenfassung
Ansible automatisiert die Serverkonfiguration und Anwendungsbereitstellung durch YAML-Playbooks, die über SSH ausgeführt werden. Der Workflow ist: Inventar definieren → Playbooks schreiben →`ansible-playbook`ausführen. Zu den Schlüsselkonzepten gehören Module (Arbeitseinheiten), Rollen (wiederverwendbare Sammlungen), Handler (ausgelöste Aufgaben) und Variablen (dynamische Werte). Gemeinsame Module umfassen Paketverwaltung, Dateioperationen, Dienststeuerung und Benutzerverwaltung. Benutzen Sie vor der Anwendung immer den Prüfmodus; Geheimnisse in Ansible Vault speichern; Stellen Sie sicher, dass Aufgaben idempotent sind. und testen Sie es lokal, bevor Sie es in der Produktion ausführen.