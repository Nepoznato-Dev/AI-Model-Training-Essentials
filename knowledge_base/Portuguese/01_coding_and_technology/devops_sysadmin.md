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
# DevOps e Administração de Sistemas
Um guia prático para gerenciar servidores, automatizar operações e manter infraestrutura confiável.
---

## SSH (Shell Seguro)
### Geração de Chave
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### Copiar chave pública para o servidor
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Configuração SSH (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### Comandos SSH comuns
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### Endurecimento SSH
- Desativar login root:`PermitRootLogin no`
- Use apenas autenticação baseada em chave:`PasswordAuthentication no`
- Alterar porta padrão (opcional, segurança através da obscuridade).
- Ative`AllowUsers`ou`AllowGroups`para restringir o acesso.
---

## Systemd (gerenciamento de serviços Linux)
### Comandos Comuns
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

### Criando uma unidade de serviço systemd
Crie `/etc/systemd/system/myapp.service`:
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

Então:
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

## Estratégias de registro
### Registro estruturado
Use o formato JSON para tornar os logs analisáveis ​​por máquina:
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### Níveis de registro
| Nível | Finalidade |
|-------|---------|
| **DEBUGAR** | Informações detalhadas de diagnóstico |
| **INFORMAÇÕES** | Eventos gerais (início, parada, transações normais) |
| **AVISO** | Inesperado, mas não fatal |
| **ERRO** | Erro que impede uma operação específica |
| **FATAL/CRÍTICO** | Desligamento do sistema |
### Agregação de registros
- **ELK Stack** (Elasticsearch, Logstash, Kibana) ou Elastic Cloud.
- **Loki + Grafana** (alternativa leve).
- **Datadog, Splunk, Sumo Logic** (SaaS).
### Rotação de registro (`logrotate`)
Evite que os logs ocupem os discos. Configurar `/etc/logrotate.d/myapp`:
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

## Monitoramento e alertas
### Métricas para monitorar
| Categoria | Principais métricas |
|----------|------------|
| **Sistema** | CPU, RAM, uso de disco, média de carga, E/S de rede |
| **Inscrição** | Taxa de solicitação, latência (p50, p95, p99), taxa de erro, sessões ativas |
| **Banco de dados** | Contagem de consultas, consultas lentas, uso do pool de conexões |
| **Negócios** | Inscrições de usuários, taxa de conversão, receita |
### Ferramentas
- **Prometheus + Grafana**: Pilha padrão de código aberto.
- **Exportador de Node** para métricas do sistema.
- **Blackbox Exporter** para disponibilidade de endpoint.
- **Alertmanager** para roteamento de alertas.
- **Nativo na nuvem**: AWS CloudWatch, Azure Monitor, GCP Monitoring.
### Monitoramento de tempo de atividade
- Pingdom, Statuspage, Better Uptime, Uptime Kuma (auto-hospedado).
- Verificações de integridade: exponha um endpoint`/health`que retorna 200 se o serviço estiver íntegro.
---

## Estratégias de backup
### A regra 3-2-1
- **3** cópias de dados.
- **2** tipos de mídia diferentes (por exemplo, SSD + fita ou local + nuvem).
- **1** cópia fora do local (por exemplo, nuvem ou data center remoto).
### Tipos de backup
| Tipo | Descrição | Troca |
|------|-------------|-----------|
| **Completo** | Copie tudo | Lento, com muito espaço |
| **Incremental** | Copia apenas alterações desde a última completa ou incremental | Restauração rápida e complexa |
| **Diferencial** | Copiar alterações desde a última completa | Meio termo |
### Backups de banco de dados
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

### Backups de arquivos
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### Agendamento de backup automatizado (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron e trabalhos agendados
### Sintaxe Cron
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Exemplos
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

### Gerenciando Cron
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

###Anacron
Usado para sistemas que não funcionam 24 horas por dia, 7 dias por semana (por exemplo, laptops); garante que os trabalhos sejam executados eventualmente.
---

## Gerenciamento e atualizações de pacotes
###Debian/Ubuntu (`apt`)
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

### Atualizações de segurança
Habilite`unattended-upgrades`no Ubuntu para patches de segurança:
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Docker em produção
### Melhores Práticas
- Use tags de imagem específicas (`python:3.12-slim`) e não`latest`.
- Execute contêineres como usuário não root.
- Verificar imagens em busca de vulnerabilidades (`docker scan`,`trivy`).
- Definir limites de recursos (`--memory`,`--cpus`).
- Use segredos (via segredos do Docker ou ambiente com cuidado).
- Mantenha as imagens pequenas: construções em vários estágios, base alpina.
### Docker Compose em produção
Defina limites de recursos em `docker-compose.yml`:
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

## Noções básicas de CI/CD
### Estágios do pipeline
| Palco | Descrição |
|-------|------------|
| **Construir** | Compilar código, instalar dependências |
| **Teste** | Execute verificações de unidade, integração e lint |
| **Containerizar** | Construir imagem Docker |
| **Empurre** | Enviar imagem para registro de contêiner |
| **Implantar** | Atualizar ambiente de preparação/produção |
### Ferramentas
| Ferramenta | Notas |
|------|-------|
| **Ações do GitHub** | Integrado com GitHub |
| **GitLabCI** | Integrado ao GitLab |
| **Jenkins** | Tradicional, altamente configurável |
| **CírculoCI, Travis CI** | Terceiros populares |
| **ArgoCD** | GitOps para Kubernetes |
### Exemplo de ação do GitHub
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

## Ajuste e solução de problemas do sistema
### Verifique o espaço em disco
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### Verifique o uso da memória
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### Verifique a carga da CPU
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### Verifique a rede
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### Encontre arquivos grandes
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## Infraestrutura como código (IaC)
### Terraforma
Declare recursos de nuvem em HCL.
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
Gerenciamento de configuração sem agente usando YAML.
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Melhores Práticas
- Use módulos e funções para reutilização.
- Armazenar estado remotamente (S3, Terraform Cloud).
- Utilize variáveis ​​e segredos (`AWS_SECRET_ACCESS_KEY`via ambiente, não codificados).
- Controle de versão do seu código IaC.
---

## Resposta a incidentes (de plantão)
### Lista de verificação para interrupção do serviço
1. Confirme o alerta.
2. Avaliar o âmbito: Que serviços/utilizadores são afetados?
3. Identifique o problema (observe logs, métricas, implantações recentes).
4. Contenha, se possível (disjuntores, sinalizadores de recursos).
5. Reverter ou corrigir avanço.
6. Comunicar o status às partes interessadas e aos usuários (página de status).
7. Documente o cronograma e as ações do incidente.
8. Post-mortem: dentro de 24 a 48 horas, escreva uma análise de causa raiz (RCA) e itens de ação para prevenir a recorrência.