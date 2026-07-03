# Fundamentos de Redes

Uma referência prática para desenvolvedores e administradores de sistemas — conceitos centrais, protocolos, comandos e troubleshooting.

---

## O Modelo OSI (7 Camadas)

Um framework conceitual para entender a comunicação em rede.

| Camada | Nome | Função | Protocolos de exemplo |
|-------|------|----------|-------------------|
| 7 | Aplicação | Serviços para o usuário final | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Apresentação | Formatação de dados, criptografia, compressão | TLS, JPEG, ASCII |
| 5 | Sessão | Gerenciamento de conexão | NetBIOS, RPC |
| 4 | Transporte | Entrega ponta a ponta, correção de erros, controle de fluxo | TCP, UDP |
| 3 | Rede | Roteamento, endereçamento | IP, ICMP, OSPF, BGP |
| 2 | Enlace de Dados | Enquadramento, detecção de erros, endereços MAC | Ethernet, Wi-Fi, PPP |
| 1 | Física | Transmissão bruta de bits | Cabos Ethernet, fibra óptica, ondas de rádio |

Na prática, o **modelo TCP/IP** (4 camadas: Link, Internet, Transport, Application) é mais usado na internet.

---

## Endereçamento IP

### IPv4
- Endereço de 32 bits, escrito como quatro octetos: `192.168.1.1`
- Total: ~4,3 bilhões de endereços (mas já esgotados na prática).

### IPv6
- Endereço de 128 bits, escrito em hexadecimal: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ endereços (praticamente infinito).

### Faixas de IP Privado (RFC 1918)
Estas não são roteáveis na internet; são usadas dentro de redes locais:
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### Notação CIDR
`192.168.1.0/24` significa que os primeiros 24 bits são o prefixo da rede; os últimos 8 bits são hosts. Ela inclui os endereços `192.168.1.0` a `192.168.1.255`.

---

## DNS (Domain Name System)

Mapeia nomes de domínio (por exemplo, `example.com`) para endereços IP.

### Tipos de Registro
| Tipo | Finalidade |
|------|---------|
| **A** | Mapeia o domínio para um endereço IPv4 |
| **AAAA** | Mapeia o domínio para um endereço IPv6 |
| **CNAME** | Alias para outro nome de domínio |
| **MX** | Servidor de troca de e-mail |
| **TXT** | Texto arbitrário (SPF, DKIM, verificação) |
| **NS** | Nameserver do domínio |
| **SRV** | Registro de serviço (por exemplo, para SIP) |

### Ferramentas Comuns
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

Portas e Protocolos
Portas Bem Conhecidas (0–1023)
PortaProtocoloServiço
20, 21TCPFTP
22TCPSSH
23TCPTelnet
25TCPSMTP
53UDP/TCPDNS
80TCPHTTP
110TCPPOP3
123UDPNTP
143TCPIMAP
443TCPHTTPS
465TCPSMTPS
587TCPSMTP (submission)
993TCPIMAPS
995TCPPOP3S
3306TCPMySQL
5432TCPPostgreSQL
6379TCPRedis
27017TCPMongoDB
Verificar portas abertas
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP vs UDP
CaracterísticaTCPUDP
ConexãoOrientado à conexão (handshake)Sem conexão
ConfiabilidadeEntrega garantida, retransmissãoMelhor esforço (pode perder pacotes)
OrdenaçãoPreserva a ordemSem garantia de ordenação
Controle de fluxoSim (janela deslizante)Não
Casos de usoWeb (HTTP), e-mail, SSH, transferência de arquivosDNS, streaming, VoIP, jogos, SNMP
Tamanho do cabeçalho20–60 bytes8 bytes
HTTP e HTTPS
Métodos HTTP
GET: Recupera um recurso (idempotente, seguro).

POST: Envia dados (não idempotente).

PUT: Atualiza/substitui um recurso (idempotente).

PATCH: Atualização parcial.

DELETE: Remove um recurso (idempotente).

Códigos de Status
1xx: Informativo (100 Continue).

2xx: Sucesso (200 OK, 201 Created, 204 No Content).

3xx: Redirecionamento (301 Moved Permanently, 302 Found, 304 Not Modified).

4xx: Erro do cliente (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests).

5xx: Erro do servidor (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable).

Cabeçalhos
Content-Type: tipo de mídia (application/json, text/html).

Authorization: credenciais (por exemplo, Bearer <token>).

Cache-Control: política de cache.

Cabeçalhos CORS: Access-Control-Allow-Origin etc.

TLS/SSL
Criptografa o tráfego HTTP (HTTPS = HTTP sobre TLS).

Certificados de Certificate Authorities (CAs) autenticam o servidor.

Verifique a cadeia de certificados e o hostname no lado do cliente.

Firewalls e NAT
Firewall
Filtra o tráfego com base em regras (IP de origem, IP de destino, porta, protocolo).

Firewalls stateful acompanham os estados das conexões.

NAT (Network Address Translation)
Traduz IPs privados em um IP público para acesso à internet.

Port forwarding: mapeia uma porta pública para um host/porta interno.

Comandos Comuns de Rede
Testes de Conectividade
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
Roteamento
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
Interfaces de Rede
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
Conectividade com uma Porta
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
Firewall (Linux iptables/nftables)
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
Estatísticas de Rede
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
Sub-redes (Referência Rápida)
CIDRMáscara de redeNúmero de endereçosHosts utilizáveis
/32255.255.255.25511
/30255.255.255.25242
/29255.255.255.24886
/28255.255.255.2401614
/27255.255.255.2243230
/26255.255.255.1926462
/25255.255.255.128128126
/24255.255.255.0256254
/23255.255.254.0512510
/22255.255.252.01,0241,022
/16255.255.0.065,53665,534
/8255.0.0.016,777,21616,777,214
Balanceamento de Carga e Proxies Reversos
Nginx como Proxy Reverso
nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Algoritmos de Balanceamento de Carga
Round-robin

Least connections

IP hash (afinidade de sessão)

Weighted round-robin

Ferramentas
Nginx, HAProxy (software)

AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing (cloud)

Checklist de Troubleshooting
O link físico está ativo? (Verifique cabos, conexão Wi-Fi).

Você consegue pingar o gateway? (por exemplo, ping 192.168.1.1).

Você consegue pingar um IP externo? (por exemplo, 8.8.8.8).

Você consegue resolver um domínio? (dig google.com).

A aplicação está escutando na porta esperada? (ss -tulpn | grep 8080).

O firewall está bloqueando a porta? (Verifique iptables/ufw ou grupos de segurança na nuvem).

Há erros nos logs da aplicação?

O certificado TLS é válido e confiável? (openssl s_client -connect example.com:443).

texto

---

## Arquivo 6: `devops_sysadmin.md`

```markdown
# DevOps e Administração de Sistemas

Um guia prático para gerenciar servidores, automatizar operações e manter uma infraestrutura confiável.

---

## SSH (Secure Shell)

### Geração de Chaves
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
Copiar chave pública para o servidor
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
Configuração do SSH (~/.ssh/config)
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
Comandos SSH comuns
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
Protegendo o SSH
Disable root login: PermitRootLogin no

Use only key-based auth: PasswordAuthentication no

Change default port (optional, security through obscurity).

Enable AllowUsers or AllowGroups to restrict access.

systemd (Gerenciamento de Serviços no Linux)
Comandos comuns
bash
systemctl status nginx           # Check service status
systemctl start nginx            # Start service
systemctl stop nginx
systemctl restart nginx
systemctl reload nginx           # Graceful reload (re-read config)
systemctl enable nginx           # Start on boot
systemctl disable nginx
systemctl list-units --type=service --all   # List all services
systemctl daemon-reload          # Reload unit files after editing
Criando uma unidade de serviço systemd
Create /etc/systemd/system/myapp.service:

ini
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
Then:

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
journalctl (Ver logs)
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
Estratégias de logging
Logging estruturado
Use JSON format to make logs machine-parseable:

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
Níveis de log
DEBUG: diagnóstico detalhado.

INFO: eventos gerais (início, parada, transações normais).

WARN: inesperado, mas não fatal.

ERROR: erro que impede uma operação específica.

FATAL/CRITICAL: desligamento do sistema.

Agregação de logs
ELK Stack (Elasticsearch, Logstash, Kibana) ou Elastic Cloud.

Loki + Grafana (alternativa leve).

Datadog, Splunk, Sumo Logic (SaaS).

Rotação de logs (logrotate)
Evita que os logs encham os discos. Configure /etc/logrotate.d/myapp:

logrotate
/var/log/myapp/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 myuser mygroup
}
Monitoramento e Alertas
Métricas para monitorar
Sistema: CPU, RAM, uso de disco, load average, I/O de rede.

Aplicação: taxa de requisições, latência (p50, p95, p99), taxa de erros, sessões ativas.

Banco de dados: contagem de consultas, consultas lentas, uso do pool de conexões.

Negócio: cadastros de usuários, taxa de conversão, receita.

Ferramentas
Prometheus + Grafana: Stack open-source padrão.

Node Exporter para métricas de sistema.

Blackbox Exporter para disponibilidade de endpoints.

Alertmanager para roteamento de alertas.

Nativo de nuvem: AWS CloudWatch, Azure Monitor, GCP Monitoring.

Monitoramento de Uptime
Pingdom, Statuspage, Better Uptime, Uptime Kuma (self-hosted).

Health checks: exponha um endpoint /health que retorne 200 se o serviço estiver saudável.

Estratégias de Backup
A Regra 3-2-1
3 cópias dos dados.

2 tipos diferentes de mídia (por exemplo, SSD + fita, ou local + cloud).

1 cópia off-site (por exemplo, cloud ou data center remoto).

Tipos de Backup
Full backup: copiar tudo (lento, ocupa muito espaço).

Incremental backup: copiar apenas alterações desde o último full ou incremental (rápido, restauração complexa).

Differential backup: copiar alterações desde o último full (meio-termo).

Backups de Banco de Dados
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
Backups de Arquivos
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
Agendamento automatizado de backups (cron)
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron e tarefas agendadas
Sintaxe do Cron
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Dia da semana (0-7, 0=Dom)
│ │ │ └─── Mês (1-12)
│ │ └───── Dia do mês (1-31)
│ └─────── Hora (0-23)
└───────── Minuto (0-59)
Exemplos
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
Gerenciando o Cron
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
Usado para sistemas que não ficam ligados 24/7 (por exemplo, laptops), garantindo que os jobs sejam executados eventualmente.

Gerenciamento de Pacotes e Atualizações
Debian/Ubuntu (apt)
bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
RHEL/CentOS/Fedora (dnf/yum)
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
Atualizações de Segurança
Enable unattended-upgrades on Ubuntu for security patches:

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker em Produção
Boas Práticas
Use tags específicas de imagem (python:3.12-slim), não latest.

Execute containers como usuário não root.

Escaneie imagens em busca de vulnerabilidades (docker scan, trivy).

Defina limites de recursos (--memory, --cpus).

Use segredos (via Docker secrets ou variáveis de ambiente com cuidado).

Mantenha as imagens pequenas: multi-stage builds, base alpine.

Docker Compose em Produção
Defina limites de recursos em docker-compose.yml:

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
Fundamentos de CI/CD
Etapas do Pipeline
Build: compilar o código, instalar dependências.

Test: executar verificações unitárias, de integração e lint.

Containerise: construir a imagem Docker.

Push: enviar a imagem para o container registry.

Deploy: atualizar o ambiente de staging/produção.

Ferramentas
GitHub Actions: integrado ao GitHub.

GitLab CI: integrado ao GitLab.

Jenkins: tradicional, altamente configurável.

CircleCI, Travis CI: opções populares de terceiros.

ArgoCD: GitOps para Kubernetes.

Exemplo de GitHub Action (simples):
yaml
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
Ajuste e Troubleshooting do Sistema
Verificar Espaço em Disco
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
Verificar Uso de Memória
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
Verificar Carga de CPU
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
Verificar Rede
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
Encontrar Arquivos Grandes
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
Infrastructure as Code (IaC)
Terraform
Declarar recursos de cloud em HCL.

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
Gerenciamento de configuração sem agente usando YAML.

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
Boas Práticas
Use modules e roles para reutilização.

Armazene o state remotamente (S3, Terraform Cloud).

Use variáveis e segredos (AWS_SECRET_ACCESS_KEY via environment, não hardcoded).

Mantenha seu código de IaC em controle de versão.

Resposta a Incidentes (On-call)
Checklist para indisponibilidade de serviço
Reconheça o alerta.

Avalie o escopo: quais serviços/usuários foram afetados?

Identifique o problema (veja logs, métricas, deploys recentes).

Contenha, se possível (circuit breakers, feature flags).

Faça rollback ou siga em frente com a correção.

Comunique o status a stakeholders e usuários (status page).

Documente a linha do tempo do incidente e as ações tomadas.

Post-mortem: em 24–48 horas, escreva uma análise de causa raiz (RCA) e itens de ação para evitar recorrência.
