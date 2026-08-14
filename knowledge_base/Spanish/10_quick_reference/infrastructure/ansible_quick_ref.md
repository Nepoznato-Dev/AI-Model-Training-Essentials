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

# Ansible y gestión de configuración
Ansible es una herramienta de automatización y gestión de configuración sin agentes. Utiliza SSH (o WinRM para Windows) para conectarse a servidores y ejecutar tareas definidas en los manuales YAML. A diferencia de las herramientas que requieren agentes instalados en cada máquina, Ansible se basa en push: ejecuta comandos desde un nodo de control. Se utiliza para el aprovisionamiento de servidores, la implementación de aplicaciones, la gestión de la configuración y la ejecución de tareas ad hoc.
---

## Conceptos básicos
| Concepto | Descripción |
|---------|-------------|
| **Inventario** | Lista de hosts administrados (formato INI o YAML) |
| **Libro de jugadas** | Archivo YAML que define un conjunto de tareas a ejecutar |
| **Reproducir** | Un mapeo entre hosts y tareas dentro de un libro de jugadas |
| **Tarea** | Una única acción a realizar en un host |
| **Módulo** | Una unidad de trabajo (por ejemplo,`apt`,`copy`,`service`,`template`) |
| **Rol** | Colección reutilizable de tareas, variables, archivos y controladores |
| **Variables** | Valores dinámicos utilizados en los playbooks |
| **Manejador** | Tarea activada por una notificación (por ejemplo, reiniciar el servicio) |
| **Hecho** | Información del sistema recopilada sobre los hosts (SO, IP, etc.) |
---

## Comandos comunes
| Comando | Descripción |
|---------|-------------|
| `ansible all -m ping`| Probar la conectividad con todos los hosts |
| `ansible all -m shell -a "uptime"`| Ejecute un comando de shell en todos los hosts |
| `ansible-playbook site.yml`| Ejecutar un libro de jugadas |
| `ansible-playbook site.yml --check`| Funcionamiento en seco (modo de verificación) |
| `ansible-playbook site.yml --diff`| Muestre lo que cambiaría |
| `ansible-playbook site.yml -l web`| Corre contra un grupo específico |
| `ansible-playbook site.yml --tags deploy`| Ejecute solo tareas con etiquetas específicas |
| `ansible-playbook site.yml --skip-tags debug`| Saltar tareas con etiquetas específicas |
| `ansible-vault encrypt secrets.yml`| Cifrar un archivo |
| `ansible-vault decrypt secrets.yml`| Descifrar un archivo |
| `ansible-vault edit secrets.yml`| Editar un archivo cifrado |
| `ansible-galaxy install geerlingguy.nginx`| Instalar un rol de Ansible Galaxy |
| `ansible-inventory --graph`| Mostrar el inventario en forma de gráfico |
| `ansible-doc apt`| Mostrar documentación de un módulo |
---

## Formatos de inventario
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

## Estructura del libro de jugadas
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

## Módulos comunes
| Módulo | Propósito | Ejemplo |
|--------|---------|---------|
| **apt/yum/dnf** | Gestión de paquetes | `apt: name=nginx state=present`|
| **copia** | Copiar archivos a hosts | `copy: src=file.txt dest=/tmp/`|
| **plantilla** | Copiar archivos con variables Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **archivo** | Administrar archivos y directorios | `file: path=/tmp/dir state=directory`|
| **servicio** | Gestionar servicios | `service: name=nginx state=restarted`|
| **usuario/grupo** | Administrar usuarios y grupos | `user: name=deploy shell=/bin/bash`|
| **cron** | Administrar trabajos cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **shell/comando** | Ejecutar comandos | `shell: echo "hello" > /tmp/test`|
| **git** | Clonar repositorios | `git: repo=https://... dest=/opt/app`|
| **sistema** | Administrar unidades systemd | `systemd: name=myapp enabled=true`|
| **cortafuegos/ufw** | Administrar reglas de firewall | `ufw: rule=allow port=80 proto=tcp`|
| **archivo de línea** | Administrar líneas en archivos | `lineinfile: path=/etc/hosts line="..."`|
| **bloqueararchivo** | Administrar bloques de texto en archivos | Insertar/actualizar bloques de configuración |
| **buscar** | Copiar archivos de hosts | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Interactuar con servicios web | `uri: url=https://api.example.com method=GET`|
| **depurar** | Imprimir mensajes | `debug: msg="Deployed {{ app_version }}"`|
---

## Estructura de roles
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

## Consejos y solución de problemas
| Consejo | Descripción |
|-----|-------------|
| **Usar modo de verificación** | Siempre`--check --diff`antes de aplicar cambios |
| **Usar etiquetas** | Tareas de etiquetas para ejecución selectiva |
| **Usar bóveda para secretos** | Nunca almacene contraseñas en texto plano |
| **Idempotencia** | Las tareas deben ser seguras para ejecutarse varias veces |
| **Usar convertirse** | Utilice`become: true`para escalar privilegios |
| **Limitar paralelismo** | Utilice`--forks`para controlar conexiones simultáneas |
| **Prueba con Vagrant/Docker** | Pruebe los manuales de estrategias localmente antes de ejecutarlos en producción |
| **Utilice`--step`** | Modo interactivo: confirme cada tarea antes de ejecutarla |
---

## Resumen
Ansible automatiza la configuración del servidor y la implementación de aplicaciones a través de guías YAML ejecutadas a través de SSH. El flujo de trabajo es: definir inventario → escribir guías → ejecutar `ansible-playbook`. Los conceptos clave incluyen módulos (unidades de trabajo), roles (colecciones reutilizables), controladores (tareas activadas) y variables (valores dinámicos). Los módulos comunes cubren la gestión de paquetes, operaciones de archivos, control de servicios y gestión de usuarios. Utilice siempre el modo de verificación antes de aplicar; almacenar secretos en Ansible Vault; garantizar que las tareas sean idempotentes; y pruebe localmente antes de ejecutarlo en producción.