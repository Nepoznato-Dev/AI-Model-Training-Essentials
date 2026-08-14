---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
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
tags: [networking, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Noções básicas de rede
Uma referência prática para desenvolvedores e administradores de sistemas — conceitos básicos, protocolos, comandos e solução de problemas.
---

## O modelo OSI (7 camadas)
Uma estrutura conceitual para compreender a comunicação em rede.
| Camada | Nome | Função | Protocolos de exemplo |
|-------|------|----------|-------------------|
| 7 | Aplicação | Serviços ao utilizador final | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Apresentação | Formatação de dados, criptografia, compactação | TLS, JPEG, ASCII |
| 5 | Sessão | Gerenciamento de conexões | NetBIOS,RPC |
| 4 | Transporte | Entrega ponta a ponta, correção de erros, controle de fluxo | TCP, UDP |
| 3 | Rede | Roteamento, endereçamento | IP, ICMP, OSPF, BGP |
| 2 | Link de dados | Enquadramento, detecção de erros, endereços MAC | Ethernet, Wi-Fi, PPP |
| 1 | Físico | Transmissão de bits brutos | Cabos Ethernet, fibra óptica, ondas de rádio |
Na prática, o **modelo TCP/IP** (4 camadas: Link, Internet, Transporte, Aplicação) é mais comumente usado para a Internet.
---

## Endereçamento IP
###IPv4
- Endereço de 32 bits, escrito como quatro octetos:`192.168.1.1`
- Total: ~4,3 bilhões de endereços (mas esgotados na prática).
###IPv6
- Endereço de 128 bits, escrito em hexadecimal:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ endereços (praticamente infinitos).
### Intervalos de IP Privados (RFC 1918)
Eles não são roteáveis na Internet; usado dentro de redes locais:
-`10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16` (192.168.0.0 – 192.168.255.255)
### Notação CIDR
`192.168.1.0/24`significa que os primeiros 24 bits são o prefixo da rede; os últimos 8 bits são hosts. Inclui endereços`192.168.1.0`a`192.168.1.255`.
---

## DNS (sistema de nomes de domínio)
Mapeia nomes de domínio (por exemplo,`example.com`) para endereços IP.
### Tipos de registro
| Tipo | Finalidade |
|------|---------|
| **A** | Mapeia domínio para endereço IPv4 |
| **AAAA** | Mapeia domínio para endereço IPv6 |
| **CNAME** | Alias ​​para outro nome de domínio |
| **MX** | Servidor de troca de correio |
| **Texto** | Texto arbitrário (SPF, DKIM, verificação) |
| **NS** | Servidor de nomes para o domínio |
| **SRV** | Registro de serviço (por exemplo, para SIP) |
### Ferramentas Comuns```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Portas e protocolos
### Portas conhecidas (0–1023)
| Porto | Protocolo | Serviço |
|------|----------|--------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | http |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTP |
| 587 | TCP | SMTP (envio) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Verifique as portas abertas
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

##TCP x UDP
| Recurso | TCP | UDP |
|--------|-----|-----|
| Conexão | Orientado à conexão (handshake) | Sem conexão |
| Confiabilidade | Entrega garantida, retransmissão | Melhor esforço (pode descartar pacotes) |
| Pedidos | Preserva a ordem | Nenhuma garantia de pedido |
| Controle de fluxo | Sim (janela deslizante) | Não |
| Casos de uso | Web (HTTP), e-mail, SSH, transferência de arquivos | DNS, streaming, VoIP, jogos, SNMP |
| Tamanho do cabeçalho | 20–60 bytes | 8 bytes |
---

##HTTP e HTTPS
### Métodos HTTP
| Método | Descrição |
|--------|------------|
| **OBTER** | Recuperar um recurso (idempotente, seguro) |
| **PUBLICAÇÃO** | Enviar dados (não idempotentes) |
| **COLOCAR** | Atualizar/substituir um recurso (idempotente) |
| **PATCH** | Atualização parcial |
| **EXCLUIR** | Remover um recurso (idempotente) |
### Códigos de status
| Código | Significado |
|------|---------|
| **1xx** | Informativo (100 Continuar) |
| **2xx** | Sucesso (200 OK, 201 Criado, 204 Sem Conteúdo) |
| **3xx** | Redirecionamento (301 movido permanentemente, 302 encontrado, 304 não modificado) |
| **4xx** | Erro do cliente (400 Solicitação incorreta, 401 Não autorizada, 403 Proibida, 404 Não encontrada, 429 Solicitações demais) |
| **5xx** | Erro de servidor (500 erro interno do servidor, 502 gateway inválido, 503 serviço indisponível) |
### Cabeçalhos
| Cabeçalho | Finalidade |
|--------|---------|
| `Content-Type`| Tipo de mídia (`application/json`,`text/html`) |
| `Authorization`| Credenciais (por exemplo,`Bearer <token>`) |
| `Cache-Control`| Política de cache |
| Cabeçalhos CORS |  `Access-Control-Allow-Origin`, etc. |
---

##TLS/SSL
Criptografa o tráfego HTTP (HTTPS = HTTP sobre TLS).
- Certificados de Autoridades de Certificação (CAs) autenticam o servidor.
- Verifique a cadeia de certificados e o nome do host no lado do cliente.
---

## Firewalls e NAT
###Firewall
- Filtra o tráfego com base em regras (IP de origem, IP de destino, porta, protocolo).
- Firewalls com estado rastreiam estados de conexão.
### NAT (tradução de endereço de rede)
- Traduz IPs privados em um IP público para acesso à Internet.
- Encaminhamento de porta: mapeia uma porta pública para um host/porta interno.
---

## Comandos de rede comuns
### Testes de conectividade
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Roteamento
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Interfaces de rede
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

### DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### Conectividade a uma porta
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Firewall (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Estatísticas de rede
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Sub-rede (referência rápida)
| CIDR | Máscara de rede | Número de endereços | Hosts utilizáveis ​​|
|------|---------|----------|-------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1.024 | 1.022 |
| /16 | 255.255.0.0 | 65.536 | 65.534 |
| /8 | 255.0.0.0 | 16.777.216 | 16.777.214 |
---

## Balanceamento de carga e proxies reversos
### Nginx como proxy reverso
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Algoritmos de balanceamento de carga
- **Round-robin**
- **Mínimo conexões**
- **Hash de IP** (persistência da sessão)
- **Round-robin ponderado**
### Ferramentas
- **Nginx, HAProxy** (software)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (nuvem)
---

## Lista de verificação para solução de problemas
1. O link físico está ativo? (Verifique cabos, conexão Wi-Fi).
2. Você consegue executar ping no gateway? (por exemplo,`ping 192.168.1.1`).
3. Você consegue executar ping em um IP externo? (por exemplo,`8.8.8.8`).
4. Você consegue resolver um domínio? (`dig google.com`).
5. O aplicativo está escutando na porta esperada? (`ss -tulpn | grep 8080`).
6. O firewall está bloqueando a porta? (Verifique `iptables`/`ufw` ou grupos de segurança em nuvem).
7. Há algum erro nos logs do aplicativo?
8. O certificado TLS é válido e confiável? (`openssl s_client -connect example.com:443`).