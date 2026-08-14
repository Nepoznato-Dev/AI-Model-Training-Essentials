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
# Ansible e gerenciamento de configuração
Ansible é uma ferramenta de automação e gerenciamento de configuração sem agente. Ele usa SSH (ou WinRM para Windows) para conectar-se a servidores e executar tarefas definidas em manuais YAML. Ao contrário das ferramentas que exigem agentes instalados em todas as máquinas, o Ansible é baseado em push – você executa comandos a partir de um nó de controle. É usado para provisionamento de servidores, implantação de aplicativos, gerenciamento de configuração e execução de tarefas ad-hoc.
---

## Conceitos Básicos
| Conceito | Descrição |
|--------|-------------|
| **Inventário** | Lista de hosts gerenciados (formato INI ou YAML) |
| **Manual** | Arquivo YAML definindo um conjunto de tarefas a serem executadas |
| **Jogar** | Um mapeamento entre hosts e tarefas em um manual |
| **Tarefa** | Uma única ação a ser executada em um host |
| **Módulo** | Uma unidade de trabalho (por exemplo,`apt`,`copy`,`service`,`template`) |
| **Função** | Coleção reutilizável de tarefas, variáveis, arquivos e manipuladores |
| **Variável** | Valores dinâmicos usados ​​em playbooks |
| **Manipulador** | Tarefa desencadeada por uma notificação (por exemplo, reiniciar serviço) |
| **Fato** | Informações do sistema coletadas sobre hosts (SO, IP, etc.) |
---

## Comandos Comuns
| Comando | Descrição |
|--------|-------------|
| `ansible all -m ping`| Teste a conectividade com todos os hosts |
| `ansible all -m shell -a "uptime"`| Execute um comando shell em todos os hosts |
| `ansible-playbook site.yml`| Execute um manual |
| `ansible-playbook site.yml --check`| Funcionamento a seco (modo de verificação) |
| `ansible-playbook site.yml --diff`| Mostre o que mudaria |
| `ansible-playbook site.yml -l web`| Executar contra um grupo específico |
| `ansible-playbook site.yml --tags deploy`| Execute apenas tarefas com tags específicas |
| `ansible-playbook site.yml --skip-tags debug`| Ignorar tarefas com tags específicas |
| `ansible-vault encrypt secrets.yml`| Criptografar um arquivo |
| `ansible-vault decrypt secrets.yml`| Descriptografar um arquivo |
| `ansible-vault edit secrets.yml`| Edite um arquivo criptografado |
| `ansible-galaxy install geerlingguy.nginx`| Instale uma função do Ansible Galaxy |
| `ansible-inventory --graph`| Exibir o estoque como um gráfico |
| `ansible-doc apt`| Mostrar documentação para um módulo |
---

## Formatos de inventário
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

## Estrutura do manual
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

## Módulos Comuns
| Módulo | Finalidade | Exemplo |
|--------|---------|---------|
| **apto/yum/dnf** | Gestão de pacotes | `apt: name=nginx state=present`|
| **copiar** | Copiar arquivos para hosts | `copy: src=file.txt dest=/tmp/`|
| **modelo** | Copiar arquivos com variáveis ​​Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **arquivo** | Gerenciar arquivos e diretórios | `file: path=/tmp/dir state=directory`|
| **serviço** | Gerenciar serviços | `service: name=nginx state=restarted`|
| **usuário/grupo** | Gerenciar usuários e grupos | `user: name=deploy shell=/bin/bash`|
| **cron** | Gerenciar tarefas cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **shell/comando** | Executar comandos | `shell: echo "hello" > /tmp/test`|
| **git** | Clonar repositórios | `git: repo=https://... dest=/opt/app`|
| **sistema** | Gerenciar unidades systemd | `systemd: name=myapp enabled=true`|
| **firewalld/ufw** | Gerenciar regras de firewall | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Gerenciar linhas em arquivos | `lineinfile: path=/etc/hosts line="..."`|
| **arquivo de bloqueio** | Gerenciar blocos de texto em arquivos | Inserir/atualizar blocos de configuração |
| **buscar** | Copiar arquivos de hosts | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Interaja com serviços web | `uri: url=https://api.example.com method=GET`|
| **depurar** | Imprimir mensagens | `debug: msg="Deployed {{ app_version }}"`|
---

## Estrutura de funções
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

## Dicas e solução de problemas
| Dica | Descrição |
|-----|-------------|
| **Use o modo de verificação** | Sempre`--check --diff`antes de aplicar alterações |
| **Usar tags** | Marcar tarefas para execução seletiva |
| **Use o cofre para segredos** | Nunca armazene senhas em texto simples |
| **Idempotência** | As tarefas devem ser seguras para serem executadas várias vezes |
| **Use tornar-se** | Use`become: true`para escalonamento de privilégios |
| **Limite o paralelismo** | Use`--forks`para controlar conexões simultâneas |
| **Teste com Vagrant/Docker** | Teste os manuais localmente antes de colocá-los em produção |
| **Usar `--step`** | Modo interativo: confirme cada tarefa antes da execução |
---

## Resumo
O Ansible automatiza a configuração do servidor e a implantação de aplicativos por meio de playbooks YAML executados por SSH. O fluxo de trabalho é: definir inventário → escrever manuais → executar`ansible-playbook`. Os principais conceitos incluem módulos (unidades de trabalho), funções (coleções reutilizáveis), manipuladores (tarefas acionadas) e variáveis ​​(valores dinâmicos). Módulos comuns cobrem gerenciamento de pacotes, operações de arquivos, controle de serviços e gerenciamento de usuários. Sempre use o modo de verificação antes de aplicar; armazenar segredos no Ansible Vault; garantir que as tarefas sejam idempotentes; e teste localmente antes de executar em produção.