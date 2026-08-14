<!--
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

-->
# DevOps y administración de sistemas
Una guía práctica para administrar servidores, automatizar operaciones y mantener una infraestructura confiable.
---

## SSH (Shell seguro)
### Generación de claves
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Copiar clave pública al servidor
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Configuración SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Comandos SSH comunes
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Endurecimiento de SSH
- Deshabilitar el inicio de sesión raíz:`PermitRootLogin no`
- Utilice únicamente autenticación basada en clave:`PasswordAuthentication no`
- Cambiar el puerto predeterminado (opcional, seguridad por oscuridad).
- Habilite`AllowUsers`o`AllowGroups`para restringir el acceso.
---

## Systemd (Gestión de servicios de Linux)
### Comandos comunes
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

### Creando una unidad de servicio systemd
Crear`/etc/systemd/system/myapp.service`:
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

Entonces:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (Ver registros)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## Estrategias de registro
### Registro estructurado
Utilice el formato JSON para que los registros sean analizables por máquina:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Niveles de registro
| Nivel | Propósito |
|-------|---------|
| **DEPURACIÓN** | Información de diagnóstico detallada |
| **INFORMACIÓN** | Eventos generales (inicio, parada, transacciones normales) |
| **ADVERTENCIA** | Inesperado pero no fatal |
| **ERROR** | Error que impide una operación específica |
| **FATAL/CRÍTICO** | Apagado del sistema |
### Agregación de registros
- **ELK Stack** (Elasticsearch, Logstash, Kibana) o Elastic Cloud.
- **Loki + Grafana** (alternativa ligera).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Rotación de registros (`logrotate`)
Evite que los registros llenen los discos. Configurar`/etc/logrotate.d/myapp`:
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

## Monitoreo y alertas
### Métricas a monitorear
| Categoría | Métricas clave |
|----------|-------------|
| **Sistema** | CPU, RAM, uso de disco, carga promedio, E/S de red |
| **Solicitud** | Tasa de solicitudes, latencia (p50, p95, p99), tasa de errores, sesiones activas |
| **Base de datos** | Recuento de consultas, consultas lentas, uso del grupo de conexiones |
| **Negocios** | Registros de usuarios, tasa de conversión, ingresos |
### Herramientas
- **Prometheus + Grafana**: pila estándar de código abierto.
- **Exportador de nodos** para métricas del sistema.
- **Blackbox Exporter** para disponibilidad de terminales.
- **Alertmanager** para enrutamiento de alertas.
- **Nativo de la nube**: AWS CloudWatch, Azure Monitor, Monitoreo de GCP.
### Monitoreo del tiempo de actividad
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (autohospedado).
- Comprobaciones de estado: expone un punto final`/health`que devuelve 200 si el servicio está en buen estado.
---

## Estrategias de respaldo
### La regla 3-2-1
- **3** copias de datos.
- **2** tipos de medios diferentes (por ejemplo, SSD + cinta o local + nube).
- **1** copia fuera del sitio (por ejemplo, nube o centro de datos remoto).
### Tipos de copia de seguridad
| Tipo | Descripción | Compensación |
|------|-------------|-----------|
| **Completo** | Copiar todo | Lento, con mucho espacio |
| **Incremental** | Copiar sólo los cambios desde el último total o incremental | Restauración rápida y compleja |
| **Diferencial** | Copiar cambios desde el último completo | Punto medio |
### Copias de seguridad de bases de datos
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

### Copias de seguridad de archivos
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Programación de copias de seguridad automatizada (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron y trabajos programados
### Sintaxis cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Ejemplos
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

### Administrar cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### Anacrón
Se utiliza para sistemas que no funcionan las 24 horas del día, los 7 días de la semana (por ejemplo, computadoras portátiles); garantiza que los trabajos se ejecuten eventualmente.
---

## Gestión de paquetes y actualizaciones
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

### Actualizaciones de seguridad
Habilite`unattended-upgrades`en Ubuntu para parches de seguridad:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker en producción
### Mejores prácticas
- Utilice etiquetas de imagen específicas (`python:3.12-slim`) no`latest`.
- Ejecutar contenedores como usuario no root.
- Escanear imágenes en busca de vulnerabilidades (`docker scan`,`trivy`).
- Establecer límites de recursos (`--memory`,`--cpus`).
- Utilice los secretos (a través de los secretos de Docker o del entorno con cuidado).
- Mantenga las imágenes pequeñas: construcciones de varias etapas, base alpina.
### Docker Compose en producción
Establecer límites de recursos en`docker-compose.yml`:
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

## Conceptos básicos de CI/CD
### Etapas del proceso de tramitación
| Etapa | Descripción |
|-------|-------------|
| **Construir** | Compilar código, instalar dependencias |
| **Prueba** | Ejecutar comprobaciones de unidad, integración y pelusa |
| **Contenedor** | Crear imagen de Docker |
| **Empujar** | Enviar imagen al registro de contenedores |
| **Implementar** | Actualizar el entorno de ensayo/producción |
### Herramientas
| Herramienta | Notas |
|------|-------|
| **Acciones de GitHub** | Integrado con GitHub |
| **GitLab CI** | Integrado en GitLab |
| **Jenkins** | Tradicional, altamente configurable |
| **CírculoCI, Travis CI** | Terceros populares |
| **ArgoCD** | GitOps para Kubernetes |
### Ejemplo de acción de GitHub
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

## Ajuste del sistema y solución de problemas
### Comprobar espacio en disco
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Verificar el uso de la memoria
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Comprobar la carga de la CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Verificar red
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Buscar archivos grandes
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infraestructura como código (IaC)
### Terraformar
Declare recursos de la nube en HCL.
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### Ansible
Gestión de configuración sin agentes mediante YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Mejores prácticas
- Utilizar módulos y roles para su reutilización.
- Almacenar el estado de forma remota (S3, Terraform Cloud).
- Utilice variables y secretos (`AWS_SECRET_ACCESS_KEY`a través del entorno, no codificados).
- Control de versiones de tu código IaC.
---

## Respuesta a incidentes (de guardia)
### Lista de verificación para interrupciones del servicio
1. Confirme la alerta.
2. Evaluar el alcance: ¿Qué servicios/usuarios se ven afectados?
3. Identifique el problema (consulte registros, métricas, implementaciones recientes).
4. Contener si es posible (disyuntores, indicadores de características).
5. Revertir o corregir hacia adelante.
6. Comunicar el estado a las partes interesadas y usuarios (página de estado).
7. Documentar el cronograma y las acciones del incidente.
8. Post-mortem: dentro de 24 a 48 horas, escriba un análisis de causa raíz (RCA) y medidas de acción para evitar que se repita.