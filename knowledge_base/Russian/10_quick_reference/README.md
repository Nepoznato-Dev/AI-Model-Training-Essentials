# Краткий справочник
Структурированная коллекция шпаргалок и кратких справочных руководств по языкам программирования, инструментам командной строки, инфраструктуре и DevOps, предназначенная для быстрого поиска во время повседневной работы.
## Структура
```
10_quick_reference/
├── README.md                          ← You are here
├── programming/                       ← Language and tool syntax
│   ├── python_syntax.md                  Python syntax cheat sheet
│   ├── sql_quick_ref.md                  SQL query reference
│   ├── regular_expressions.md            Regex syntax and common patterns
│   └── git_commands.md                   Git commands and workflows
└── infrastructure/                    ← Systems, DevOps, and cloud
    ├── linux_commands.md                  Linux command line reference
    ├── bash_and_shell_scripting.md        Bash scripting and one-liners
    ├── docker_and_kubernetes.md           Docker, Compose, Kubernetes, Helm
    ├── cloud_services_comparison.md       AWS vs Azure vs GCP comparison
    ├── ansible_quick_ref.md               Ansible playbooks and automation
    ├── terraform_quick_ref.md             Terraform commands and IaC
    ├── cicd_pipeline_config.md            GitHub Actions, GitLab CI, Jenkins
    └── prometheus_and_grafana.md          PromQL, dashboards, alerting
```

## Файлы по подкатегориям
### Программирование
| Файл | Описание |
|------|-------------|
| [python_syntax.md](programming/python_syntax.md)| Шпаргалка по синтаксису Python |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| Справочник по SQL-запросам |
| [regular_expressions.md](programming/regular_expressions.md)| Синтаксис регулярных выражений, общие шаблоны, использование в зависимости от языка |
| [git_commands.md](programming/git_commands.md)| Команды и рабочие процессы Git |
### Инфраструктура
| Файл | Описание |
|------|-------------|
| [linux_commands.md](infrastructure/linux_commands.md)| Справочник по командной строке Linux |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Скрипты Bash, обработка текста, полезные однострочники |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Шпаргалка по Docker, Docker Compose, Kubernetes, Helm |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| Параллельное сравнение AWS, Azure и GCP |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Ansible playbooks, модули, роли, автоматизация |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| Концепции IaC, команды Terraform, управление состоянием |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| Действия GitHub, GitLab CI, Jenkins, шаблоны YAML конвейера |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL, экспортеры, информационные панели, оповещения |
## Рекомендуемые пути чтения
### **Путь DevOps-инженера**
1.`infrastructure/linux_commands.md`— основы Linux.
2.`infrastructure/bash_and_shell_scripting.md`— сценарии оболочки.
3.`infrastructure/docker_and_kubernetes.md`— Контейнеры и оркестровка.
4.`infrastructure/cicd_pipeline_config.md`— конвейеры CI/CD.
5.`infrastructure/terraform_quick_ref.md`— Инфраструктура как код
6.`infrastructure/prometheus_and_grafana.md`— Мониторинг
### **Путь разработчика**
1.`programming/python_syntax.md`— справочник Python
2.`programming/sql_quick_ref.md`— запросы к базе данных.
3.`programming/git_commands.md`— Контроль версий.
4.`programming/regular_expressions.md`— Сопоставление с образцом