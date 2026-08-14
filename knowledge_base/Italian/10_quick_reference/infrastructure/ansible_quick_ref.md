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
# Ansible e gestione della configurazione
Ansible è uno strumento di gestione e automazione della configurazione senza agente. Utilizza SSH (o WinRM per Windows) per connettersi ai server ed eseguire attività definite nei playbook YAML. A differenza degli strumenti che richiedono agenti installati su ogni macchina, Ansible è basato su push: esegui i comandi da un nodo di controllo. Viene utilizzato per il provisioning del server, la distribuzione delle applicazioni, la gestione della configurazione e l'esecuzione di attività ad hoc.
---

## Concetti fondamentali
| Concetto | Descrizione |
|---------|-----|
| **Inventario** | Elenco degli host gestiti (formato INI o YAML) |
| **Libro delle istruzioni** | File YAML che definisce una serie di attività da eseguire |
| **Gioca** | Una mappatura tra host e attività all'interno di un playbook |
| **Compito** | Una singola azione da eseguire su un host |
| **Modulo** | Un'unità di lavoro (ad esempio,`apt`,`copy`,`service`,`template`) |
| **Ruolo** | Raccolta riutilizzabile di attività, variabili, file e gestori |
| **Variabile** | Valori dinamici utilizzati nei playbook |
| **Gestore** | Attività attivata da una notifica (ad esempio, riavvio del servizio) |
| **Fatto** | Informazioni di sistema raccolte sugli host (sistema operativo, IP, ecc.) |
---

## Comandi comuni
| Comando | Descrizione |
|---------|-----|
| `ansible all -m ping`| Testare la connettività a tutti gli host |
| `ansible all -m shell -a "uptime"`| Esegui un comando shell su tutti gli host |
| `ansible-playbook site.yml`| Esegui un playbook |
| `ansible-playbook site.yml --check`| Funzionamento a secco (modalità di controllo) |
| `ansible-playbook site.yml --diff`| Mostra cosa cambierebbe |
| `ansible-playbook site.yml -l web`| Corri contro un gruppo specifico |
| `ansible-playbook site.yml --tags deploy`| Esegui solo attività con tag specifici |
| `ansible-playbook site.yml --skip-tags debug`| Salta attività con tag specifici |
| `ansible-vault encrypt secrets.yml`| Crittografare un file |
| `ansible-vault decrypt secrets.yml`| Decifrare un file |
| `ansible-vault edit secrets.yml`| Modifica un file crittografato |
| `ansible-galaxy install geerlingguy.nginx`| Installa un ruolo da Ansible Galaxy |
| `ansible-inventory --graph`| Visualizza l'inventario come grafico |
| `ansible-doc apt`| Mostra la documentazione per un modulo |
---

## Formati di inventario
### Formato INI
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

### Formato YAML
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

## Struttura del playbook
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

## Moduli comuni
| Modulo | Scopo | Esempio |
|--------|---------|---------|
| **apt / yum / dnf** | Gestione dei pacchetti | `apt: name=nginx state=present`|
| **copia** | Copia i file sugli host | `copy: src=file.txt dest=/tmp/`|
| **modello** | Copia file con variabili Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **file** | Gestire file e directory | `file: path=/tmp/dir state=directory`|
| **servizio** | Gestire servizi | `service: name=nginx state=restarted`|
| **utente/gruppo** | Gestisci utenti e gruppi | `user: name=deploy shell=/bin/bash`|
| **cron** | Gestisci i lavori cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **shell/comando** | Esegui comandi | `shell: echo "hello" > /tmp/test`|
| **git** | Repository clonati | `git: repo=https://... dest=/opt/app`|
| **sistemad** | Gestisci unità systemd | `systemd: name=myapp enabled=true`|
| **firewalld/ufw** | Gestisci le regole del firewall | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Gestisci le righe nei file | `lineinfile: path=/etc/hosts line="..."`|
| **file di blocco** | Gestisci blocchi di testo nei file | Inserimento/aggiornamento blocchi di configurazione |
| **recupera** | Copiare file dagli host | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Interagisci con i servizi web | `uri: url=https://api.example.com method=GET`|
| **debug** | Stampa messaggi | `debug: msg="Deployed {{ app_version }}"`|
---

## Struttura dei ruoli
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

## Suggerimenti e risoluzione dei problemi
| Suggerimento | Descrizione |
|-----|-------------|
| **Utilizza la modalità di controllo** | Sempre`--check --diff`prima di applicare le modifiche |
| **Utilizza tag** | Contrassegnare le attività per l'esecuzione selettiva |
| **Utilizza il vault per i segreti** | Non archiviare mai le password in testo semplice |
| **Idempotenza** | Le attività dovrebbero essere sicure da eseguire più volte |
| **Utilizzare diventare** | Utilizzare`become: true`per l'escalation dei privilegi |
| **Parallelismo limite** | Utilizzare`--forks`per controllare le connessioni simultanee |
| **Test con Vagrant / Docker** | Testare i playbook localmente prima di eseguirli in produzione |
| **Utilizzare `--step`** | Modalità interattiva: conferma ogni attività prima dell'esecuzione |
---

## Riepilogo
Ansible automatizza la configurazione del server e la distribuzione delle applicazioni tramite playbook YAML eseguiti su SSH. Il flusso di lavoro è: definire l'inventario → scrivere playbook → eseguire`ansible-playbook`. I concetti chiave includono moduli (unità di lavoro), ruoli (raccolte riutilizzabili), gestori (attività attivate) e variabili (valori dinamici). I moduli comuni riguardano la gestione dei pacchetti, le operazioni sui file, il controllo dei servizi e la gestione degli utenti. Utilizzare sempre la modalità di controllo prima di applicare; archiviare segreti in Ansible Vault; garantire che le attività siano idempotenti; e testare localmente prima di eseguirlo in produzione.