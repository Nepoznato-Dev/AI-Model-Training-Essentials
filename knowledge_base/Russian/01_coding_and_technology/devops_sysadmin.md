---
# Metadata
title: "DevOps and System Administration"
description: "SSH, systemd, logging, monitoring, backups, Docker, CI/CD"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, sysadmin, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "19 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# DevOps и системное администрирование
Практическое руководство по управлению серверами, автоматизации операций и поддержанию надежной инфраструктуры.
---

## SSH (безопасная оболочка)
### Генерация ключей
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Копирование открытого ключа на сервер
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Конфигурация SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Общие команды SSH
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Усиление SSH
- Отключить root-вход:`PermitRootLogin no`
– Использовать только аутентификацию на основе ключей: `PasswordAuthentication no`. 
- Изменить порт по умолчанию (необязательно, безопасность через неизвестность).
- Включите`AllowUsers`или `AllowGroups`, чтобы ограничить доступ.
---

## Systemd (Управление службами Linux)
### Общие команды
```bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
```

### Создание сервисного модуля systemd
Создайте `/etc/systemd/system/myapp.service`:
```ini
[Unit]
Description=My Python App
After=network.target

[Service]
User=myuser
Group=mygroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Restart=always
RestartSec=10
Environment="ENV=production"

[Install]
WantedBy=multi-user.target
```

Затем:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (просмотр журналов)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Стратегии ведения журналов
### Структурированное ведение журнала
Используйте формат JSON, чтобы сделать журналы пригодными для машинного анализа:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Уровни журнала
| Уровень | Цель |
|-------|---------|
| **ОТЛАДКА** | Подробная диагностическая информация |
| **ИНФОРМАЦИЯ** | Общие события (старт, стоп, обычные транзакции) |
| **ВНИМАНИЕ** | Неожиданно, но не смертельно |
| **ОШИБКА** | Ошибка, препятствующая выполнению определенной операции |
| **ФАТАЛЬНЫЙ/КРИТИЧЕСКИЙ** | Выключение системы |
### Агрегация журналов
- **ELK Stack** (Elasticsearch, Logstash, Kibana) или Elastic Cloud.
- **Локи + Графана** (облегченная альтернатива).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Ротация журналов (`logrotate`)
Предотвратите заполнение дисков журналами. Настройте `/etc/logrotate.d/myapp`:
```
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
```

---

## Мониторинг и оповещение
### Метрики для мониторинга
| Категория | Ключевые показатели |
|----------|-------------|
| **Система** | ЦП, ОЗУ, использование диска, средняя нагрузка, сетевой ввод-вывод |
| **Приложение** | Частота запросов, задержка (p50, p95, p99), частота ошибок, активные сеансы |
| **База данных** | Количество запросов, медленные запросы, использование пула соединений |
| **Бизнес** | Регистрации пользователей, коэффициент конверсии, доход |
### Инструменты
- **Prometheus + Grafana**: стандартный стек с открытым исходным кодом.
- **Node Exporter** для системных показателей.
- **Blackbox Exporter** для доступности конечных точек.
- **Alertmanager** для маршрутизации предупреждений.
- **Облако**: AWS CloudWatch, Azure Monitor, GCP Monitoring.
### Мониторинг работоспособности
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (самостоятельное размещение).
- Проверки работоспособности: выставьте конечную точку `/health`, которая возвращает 200, если служба работоспособна.
---

## Стратегии резервного копирования
### Правило 3-2-1
- **3** копии данных.
- **2** различных типа носителей (например, SSD + лента или локальный + облако).
- **1** копия за пределами площадки (например, в облаке или удаленном центре обработки данных).
### Типы резервного копирования
| Тип | Описание | Компромисс |
|------|-------------|-----------|
| **Полная** | Скопировать все | Медленный, тяжелый |
| **Дополнительно** | Копировать только изменения с момента последнего полного или инкрементального | Быстрое и комплексное восстановление |
| **Дифференциал** | Копировать изменения с момента последнего полного | Золотая середина |
### Резервные копии баз данных
```bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
```

### Резервные копии файлов
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Автоматическое планирование резервного копирования (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron и запланированные задания
### Синтаксис Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Примеры
```cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
```

### Управление Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Анакрон
Используется для систем, не работающих круглосуточно (например, ноутбуков); обеспечивает выполнение заданий в конечном итоге.
---

## Управление пакетами и обновления
### Debian/Ubuntu (`apt`)
```bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
```

### RHEL/CentOS/Fedora (`dnf`/`yum`)
```bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
```

### Обновления безопасности
Включите`unattended-upgrades`в Ubuntu для получения обновлений безопасности:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker в производстве
### Лучшие практики
– Используйте определенные теги изображений (`python:3.12-slim`), а не`latest`.
- Запускайте контейнеры от имени пользователя без полномочий root.
- Сканирование изображений на наличие уязвимостей (`docker scan`,`trivy`).
- Установите ограничения ресурсов (`--memory`,`--cpus`).
- Используйте секреты (с осторожностью через секреты Docker или среду).
- Сохраняйте изображения небольшими: многоэтапные сборки, альпийская база.
### Docker Compose в рабочей среде
Установите ограничения ресурсов в `docker-compose.yml`:
```yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
```

---

## Основы CI/CD
### Этапы конвейера
| Этап | Описание |
|-------|-------------|
| **Построить** | Скомпилировать код, установить зависимости |
| **Тест** | Запустите модульную проверку, проверку интеграции и проверку работоспособности |
| **Контейнеризация** | Сборка образа Docker |
| **Нажмите** | Отправить образ в реестр контейнеров |
| **Развертывание** | Обновить промежуточную/производственную среду |
### Инструменты
| Инструмент | Заметки |
|------|-------|
| **Действия GitHub** | Интегрировано с GitHub |
| **GitLab CI** | Встроенный в GitLab |
| **Дженкинс** | Традиционный, легко настраиваемый |
| **CircleCI, Трэвис CI** | Популярные сторонние |
| **АргоКД** | GitOps для Kubernetes |
### Пример действия GitHub
```yaml
name: CI
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## Настройка системы и устранение неполадок
### Проверьте место на диске
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Проверка использования памяти
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Проверьте загрузку процессора
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Проверить сеть
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Найти большие файлы
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Инфраструктура как код (IaC)
### Терраформировать
Объявите облачные ресурсы в HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Анзибль
Безагентное управление конфигурацией с использованием YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Лучшие практики
- Используйте модули и роли для повторного использования.
- Сохраняйте состояние удаленно (S3, Terraform Cloud).
- Используйте переменные и секреты (`AWS_SECRET_ACCESS_KEY`через среду, а не жестко закодированные).
- Контроль версий вашего кода IaC.
---

## Реагирование на инциденты (по вызову)
### Контрольный список на случай сбоя в обслуживании
1. Подтвердите оповещение.
2. Оцените масштаб: какие услуги/пользователи затронуты?
3. Определите проблему (просмотрите журналы, метрики, последние развертывания).
4. По возможности изолируйте (автоматические выключатели, функциональные флажки).
5. Откат назад или фиксация вперед.
6. Сообщайте статус заинтересованным сторонам и пользователям (страница статуса).
7. Задокументируйте график инцидента и действия.
8. Вскрытие: в течение 24–48 часов напишите анализ первопричин (RCA) и меры по предотвращению повторения.