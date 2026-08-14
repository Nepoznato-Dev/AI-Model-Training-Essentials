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
# Ansible i zarządzanie konfiguracją
Ansible to bezagentowe narzędzie do zarządzania konfiguracją i automatyzacji. Wykorzystuje SSH (lub WinRM dla Windows) do łączenia się z serwerami i wykonywania zadań zdefiniowanych w podręcznikach YAML. W przeciwieństwie do narzędzi, które wymagają agentów zainstalowanych na każdym komputerze, Ansible działa w trybie push — polecenia uruchamiane są z węzła kontrolnego. Służy do udostępniania serwerów, wdrażania aplikacji, zarządzania konfiguracją i wykonywania zadań ad hoc.
---

## Podstawowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Inwentarz** | Lista zarządzanych hostów (format INI lub YAML) |
| **Poradnik** | Plik YAML definiujący zestaw zadań do wykonania |
| **Graj** | Mapowanie pomiędzy hostami i zadaniami w podręczniku |
| **Zadanie** | Pojedyncza akcja do wykonania na hoście |
| **Moduł** | Jednostka pracy (np.`apt`,`copy`,`service`,`template`) |
| **Rola** | Zbiór zadań, zmiennych, plików i procedur obsługi wielokrotnego użytku |
| **Zmienna** | Wartości dynamiczne używane w podręcznikach |
| **opiekun** | Zadanie wywołane powiadomieniem (np. ponowne uruchomienie usługi) |
| **Fakt** | Zebrane informacje systemowe o hostach (system operacyjny, adres IP itp.) |
---

## Typowe polecenia
| Polecenie | Opis |
|--------|------------|
| `ansible all -m ping`| Testuj łączność ze wszystkimi hostami |
| `ansible all -m shell -a "uptime"`| Uruchom polecenie powłoki na wszystkich hostach |
| `ansible-playbook site.yml`| Wykonaj podręcznik |
| `ansible-playbook site.yml --check`| Praca próbna (tryb sprawdzania) |
| `ansible-playbook site.yml --diff`| Pokaż co by się zmieniło |
| `ansible-playbook site.yml -l web`| Biegnij przeciwko określonej grupie |
| `ansible-playbook site.yml --tags deploy`| Uruchamiaj tylko zadania z określonymi tagami |
| `ansible-playbook site.yml --skip-tags debug`| Pomiń zadania z określonymi tagami |
| `ansible-vault encrypt secrets.yml`| Zaszyfruj plik |
| `ansible-vault decrypt secrets.yml`| Odszyfruj plik |
| `ansible-vault edit secrets.yml`| Edytuj zaszyfrowany plik |
| `ansible-galaxy install geerlingguy.nginx`| Zainstaluj rolę z Ansible Galaxy |
| `ansible-inventory --graph`| Wyświetl zapasy w formie wykresu |
| `ansible-doc apt`| Pokaż dokumentację modułu |
---

##Formaty zapasów
### Format INI
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

### Format YAML
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

## Struktura podręcznika
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

## Wspólne moduły
| Moduł | Cel | Przykład |
|--------|---------|--------|
| **apt / mniam / dnf** | Zarządzanie pakietami | `apt: name=nginx state=present`|
| **skopiuj** | Skopiuj pliki do hostów | `copy: src=file.txt dest=/tmp/`|
| **szablon** | Skopiuj pliki ze zmiennymi Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **plik** | Zarządzaj plikami i katalogami | `file: path=/tmp/dir state=directory`|
| **usługa** | Zarządzaj usługami | `service: name=nginx state=restarted`|
| **użytkownik / grupa** | Zarządzaj użytkownikami i grupami | `user: name=deploy shell=/bin/bash`|
| **crona** | Zarządzaj zadaniami cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **powłoka / polecenie** | Uruchom polecenia | `shell: echo "hello" > /tmp/test`|
| **git** | Repozytoria klonowania | `git: repo=https://... dest=/opt/app`|
| **system** | Zarządzaj jednostkami systemowymi | `systemd: name=myapp enabled=true`|
| **zapora ogniowa / ufw** | Zarządzaj regułami zapory | `ufw: rule=allow port=80 proto=tcp`|
| **plik liniowy** | Zarządzaj liniami w plikach | `lineinfile: path=/etc/hosts line="..."`|
| **plik blokowy** | Zarządzaj blokami tekstu w plikach | Wstaw/zaktualizuj bloki konfiguracji |
| **przynieś** | Skopiuj pliki z hostów | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Interakcja z usługami internetowymi | `uri: url=https://api.example.com method=GET`|
| **debugowanie** | Drukuj wiadomości | `debug: msg="Deployed {{ app_version }}"`|
---

## Struktura ról
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

## Wskazówki i rozwiązywanie problemów
| Wskazówka | Opis |
|-----|------------|
| **Użyj trybu sprawdzania** | Zawsze`--check --diff`przed zastosowaniem zmian |
| **Użyj tagów** | Oznacz zadania do selektywnego wykonania |
| **Użyj skarbca do przechowywania sekretów** | Nigdy nie przechowuj haseł w postaci zwykłego tekstu |
| **Idempotencja** | Zadania powinny być bezpieczne i można je uruchamiać wielokrotnie |
| **Użyj zostań** | Użyj`become: true`do eskalacji uprawnień |
| **Ogranicz równoległość** | Użyj`--forks`do kontrolowania współbieżnych połączeń |
| **Test z Vagrantem/Dockerem** | Przetestuj podręczniki lokalnie przed uruchomieniem w środowisku produkcyjnym |
| **Użyj`--step`** | Tryb interaktywny: potwierdzaj każde zadanie przed wykonaniem |
---

## Streszczenie
Ansible automatyzuje konfigurację serwera i wdrażanie aplikacji za pomocą podręczników YAML wykonywanych przez SSH. Przepływ pracy jest następujący: zdefiniuj zasoby → napisz podręczniki → uruchom`ansible-playbook`. Kluczowe pojęcia obejmują moduły (jednostki pracy), role (kolekcje wielokrotnego użytku), procedury obsługi (zadania wyzwalane) i zmienne (wartości dynamiczne). Wspólne moduły obejmują zarządzanie pakietami, operacje na plikach, kontrolę usług i zarządzanie użytkownikami. Zawsze używaj trybu sprawdzania przed zastosowaniem; przechowuj sekrety w Ansible Vault; upewnij się, że zadania są idempotentne; i przetestuj lokalnie przed uruchomieniem w środowisku produkcyjnym.