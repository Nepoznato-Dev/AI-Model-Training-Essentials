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

# Ansible и управление конфигурациями
Ansible — это безагентный инструмент управления и автоматизации конфигурации. Он использует SSH (или WinRM для Windows) для подключения к серверам и выполнения задач, определенных в сборниках сценариев YAML. В отличие от инструментов, требующих установки агентов на каждом компьютере, Ansible основан на принудительной отправке — вы запускаете команды с узла управления. Он используется для подготовки серверов, развертывания приложений, управления конфигурацией и выполнения специальных задач.
---

## Основные понятия
| Концепция | Описание |
|---------|-------------|
| **Инвентарь** | Список управляемых хостов (формат INI или YAML) |
| **Пособие** | YAML-файл, определяющий набор задач для выполнения |
| **Играть** | Сопоставление хостов и задач в сборнике сценариев |
| **Задание** | Одно действие, выполняемое на хосте |
| **Модуль** | Единица работы (например, `apt`, `copy`, `service`, `template`) |
| **Роль** | Многоразовая коллекция задач, переменных, файлов и обработчиков |
| **Переменная** | Динамические значения, используемые в сборниках сценариев |
| **Обработчик** | Задача, запускаемая уведомлением (например, перезапуск службы) |
| **Факт** | Системная информация, собранная об хостах (ОС, IP и т. д.) |
---

## Общие команды
| Команда | Описание |
|---------|-------------|
| `ansible all -m ping`| Проверка подключения ко всем хостам |
| `ansible all -m shell -a "uptime"`| Запустите команду оболочки на всех хостах |
| `ansible-playbook site.yml`| Выполнить сценарий |
| `ansible-playbook site.yml --check`| Пробный прогон (режим проверки) |
| `ansible-playbook site.yml --diff`| Покажите, что изменится |
| `ansible-playbook site.yml -l web`| Состязаться с определенной группой |
| `ansible-playbook site.yml --tags deploy`| Запускать только задачи с определенными тегами |
| `ansible-playbook site.yml --skip-tags debug`| Пропускать задачи с определенными тегами |
| `ansible-vault encrypt secrets.yml`| Зашифровать файл |
| `ansible-vault decrypt secrets.yml`| Расшифровать файл |
| `ansible-vault edit secrets.yml`| Редактировать зашифрованный файл |
| `ansible-galaxy install geerlingguy.nginx`| Установите роль из Ansible Galaxy |
| `ansible-inventory --graph`| Отображение запасов в виде графика |
| `ansible-doc apt`| Показать документацию к модулю |
---

## Форматы инвентаря
### INI-формат
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

### Формат YAML
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

## Структура книги действий
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

## Общие модули
| Модуль | Цель | Пример |
|--------|---------|---------|
| **аппт / ням / днф** | Управление пакетами | `apt: name=nginx state=present`|
| **копия** | Копирование файлов на хосты | `copy: src=file.txt dest=/tmp/`|
| **шаблон** | Копирование файлов с переменными Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **файл** | Управление файлами и каталогами | `file: path=/tmp/dir state=directory`|
| **сервис** | Управление услугами | `service: name=nginx state=restarted`|
| **пользователь/группа** | Управление пользователями и группами | `user: name=deploy shell=/bin/bash`|
| **крон** | Управление заданиями cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **оболочка/команда** | Выполнять команды | `shell: echo "hello" > /tmp/test`|
| **мерзавец** | Репозитории клонов | `git: repo=https://... dest=/opt/app`|
| **системный** | Управление системными модулями | `systemd: name=myapp enabled=true`|
| **firewalld / ufw** | Управление правилами брандмауэра | `ufw: rule=allow port=80 proto=tcp`|
| **строковыйфайл** | Управление строками в файлах | `lineinfile: path=/etc/hosts line="..."`|
| **блокинфайл** | Управление блоками текста в файлах | Вставить/обновить блоки конфигурации |
| **принести** | Копирование файлов с хостов | `fetch: src=/var/log/app.log dest=/local/`|
| **ури** | Взаимодействие с веб-сервисами | `uri: url=https://api.example.com method=GET`|
| **отладка** | Печать сообщений | `debug: msg="Deployed {{ app_version }}"`|
---

## Ролевая структура
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

## Советы и устранение неполадок
| Совет | Описание |
|-----|-------------|
| **Использовать режим проверки** | Всегда`--check --diff`перед применением изменений |
| **Используйте теги** | Пометить задачи для выборочного выполнения |
| **Используйте хранилище для секретов** | Никогда не храните пароли в виде обычного текста |
| **Идемпотентность** | Задачи должны быть безопасными для многократного запуска |
| **Используйте стать** | Используйте`become: true`для повышения привилегий |
| **Ограничить параллелизм** | Используйте`--forks`для управления одновременными соединениями |
| **Тестирование с помощью Vagrant/Docker** | Тестируйте плейбуки локально перед запуском в рабочей среде |
| **Используйте`--step`** | Интерактивный режим: подтверждайте каждую задачу перед выполнением |
---

## Краткое содержание
Ansible автоматизирует настройку сервера и развертывание приложений с помощью плейбуков YAML, выполняемых через SSH. Рабочий процесс таков: определить инвентарь → написать сценарии → запустить`ansible-playbook`. Ключевые понятия включают модули (единицы работы), роли (многоразовые коллекции), обработчики (запускаемые задачи) и переменные (динамические значения). Общие модули охватывают управление пакетами, файловые операции, контроль служб и управление пользователями. Всегда используйте режим проверки перед применением; хранить секреты в Ansible Vault; обеспечить идемпотентность задач; и тестируйте локально перед запуском в производство.