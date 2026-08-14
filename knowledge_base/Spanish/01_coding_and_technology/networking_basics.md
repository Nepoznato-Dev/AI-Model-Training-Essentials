---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# Conceptos básicos de redes
Una referencia práctica para desarrolladores y administradores de sistemas: conceptos básicos, protocolos, comandos y solución de problemas.
---

## El modelo OSI (7 capas)
Un marco conceptual para comprender la comunicación en red.
| Capa | Nombre | Función | Protocolos de ejemplo |
|-------|------|----------|-------------------|
| 7 | Solicitud | Servicios al usuario final | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Presentación | Formateo, cifrado y compresión de datos | TLS, JPEG, ASCII |
| 5 | Sesión | Gestión de conexiones | NetBIOS, RPC |
| 4 | Transporte | Entrega de extremo a extremo, corrección de errores, control de flujo | TCP, UDP |
| 3 | Red | Enrutamiento, direccionamiento | IP, ICMP, OSPF, BGP |
| 2 | Enlace de datos | Framing, detección de errores, direcciones MAC | Ethernet, Wi-Fi, PPP |
| 1 | Físico | Transmisión de bits en bruto | Cables ethernet, fibra óptica, ondas de radio |
En la práctica, el **modelo TCP/IP** (4 capas: Enlace, Internet, Transporte, Aplicación) se usa más comúnmente para Internet.
---

## Direccionamiento IP
### IPv4
- Dirección de 32 bits, escrita en cuatro octetos:`192.168.1.1`
- Total: ~4.300 millones de direcciones (pero agotadas en la práctica).
### IPv6
- Dirección de 128 bits, escrita en hexadecimal:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Total: 2¹²⁸ direcciones (prácticamente infinitas).
### Rangos de IP privados (RFC 1918)
Estos no se pueden enrutar en Internet; utilizado dentro de redes locales:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16` (192.168.0.0 – 192.168.255.255)
### Notación CIDR
`192.168.1.0/24`significa que los primeros 24 bits son el prefijo de red; los últimos 8 bits son hosts. Incluye las direcciones`192.168.1.0`a `192.168.1.255`.
---

## DNS (Sistema de nombres de dominio)
Asigna nombres de dominio (por ejemplo, `example.com`) a direcciones IP.
### Tipos de registros
| Tipo | Propósito |
|------|---------|
| **A** | Asigna dominio a dirección IPv4 |
| **AAA** | Asigna dominio a dirección IPv6 |
| **CNOMBRE** | Alias ​​de otro nombre de dominio |
| **MX** | Servidor de intercambio de correo |
| **TEXTO** | Texto arbitrario (SPF, DKIM, verificación) |
| **NS** | Servidor de nombres para el dominio |
| **SRV** | Registro de servicio (por ejemplo, para SIP) |
### Herramientas comunes```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Puertos y protocolos
### Puertos conocidos (0–1023)
| Puerto | Protocolo | Servicio |
|------|----------|---------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telenet |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTP |
| 587 | TCP | SMTP (envío) |
| 993 | TCP | IMÁGENES |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | Mongo DB |
### Verificar puertos abiertos
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP frente a UDP
| Característica | TCP | UDP |
|---------|-----|-----|
| Conexión | Orientado a la conexión (apretón de manos) | Sin conexión |
| Fiabilidad | Entrega garantizada, retransmisión | Mejor esfuerzo (puede descartar paquetes) |
| Realizar pedidos | Conserva el orden | Sin garantía de pedido |
| Control de flujo | Sí (ventana corredera) | No |
| Casos de uso | Web (HTTP), correo electrónico, SSH, transferencia de archivos | DNS, streaming, VoIP, juegos, SNMP |
| Tamaño del encabezado | 20–60 bytes | 8 bytes |
---

##HTTP y HTTPS
### Métodos HTTP
| Método | Descripción |
|--------|-------------|
| **OBTENER** | Recuperar un recurso (idempotente, seguro) |
| **ENVÍO** | Enviar datos (no idempotente) |
| **PONER** | Actualizar/reemplazar un recurso (idempotente) |
| **PARCHE** | Actualización parcial |
| **ELIMINAR** | Eliminar un recurso (idempotente) |
### Códigos de estado
| Código | Significado |
|------|---------|
| **1xx** | Informativo (100 Continuar) |
| **2xx** | Éxito (200 OK, 201 creados, 204 sin contenido) |
| **3xx** | Redirección (301 movidos permanentemente, 302 encontrados, 304 no modificados) |
| **4xx** | Error del cliente (400 Solicitud incorrecta, 401 No autorizada, 403 Prohibida, 404 No encontrada, 429 Demasiadas solicitudes) |
| **5xx** | Error del servidor (500 Error interno del servidor, 502 Puerta de enlace incorrecta, 503 Servicio no disponible) |
### Encabezados
| Encabezado | Propósito |
|--------|---------|
| `Content-Type`| Tipo de medio (`application/json`, `text/html`) |
| `Authorization`| Credenciales (por ejemplo, `Bearer <token>`) |
| `Cache-Control`| Política de almacenamiento en caché |
| Encabezados CORS |  `Access-Control-Allow-Origin`, etc. |
---

## TLS/SSL
Cifra el tráfico HTTP (HTTPS = HTTP sobre TLS).
- Los certificados de las autoridades certificadoras (CA) autentican el servidor.
- Verificar la cadena de certificados y el nombre de host en el lado del cliente.
---

## Cortafuegos y NAT
### Cortafuegos
- Filtra el tráfico según reglas (IP de origen, IP de destino, puerto, protocolo).
- Los cortafuegos con estado rastrean los estados de conexión.
### NAT (Traducción de direcciones de red)
- Traduce IP privadas a una IP pública para acceso a Internet.
- Reenvío de puertos: asigna un puerto público a un host/puerto interno.
---

## Comandos de red comunes
### Pruebas de conectividad
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Enrutamiento
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Interfaces de red
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

### Conectividad a un puerto
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Cortafuegos (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Estadísticas de red
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Subredes (Referencia rápida)
| CIDR | máscara de red | Número de direcciones | Hosts utilizables |
|------|---------|---------------------|--------------|
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

## Equilibrio de carga y proxies inversos
### Nginx como proxy inverso
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

### Algoritmos de equilibrio de carga
- **Todos contra todos**
- **Menos conexiones**
- **Hash de IP** (fijación de la sesión)
- **Ronda ponderada**
### Herramientas
- **Nginx, HAProxy** (software)
- **AWS ELB, Azure Load Balancer, GCP Cloud Load Balancing** (nube)
---

## Lista de verificación para solucionar problemas
1. ¿Está activo el enlace físico? (Revisar cables, conexión wifi).
2. ¿Puedes hacer ping a la puerta de enlace? (por ejemplo, `ping 192.168.1.1`).
3. ¿Puedes hacer ping a una IP externa? (por ejemplo, `8.8.8.8`).
4. ¿Puedes resolver un dominio? (`dig google.com`).
5. ¿La aplicación está escuchando en el puerto esperado? (`ss -tulpn | grep 8080`).
6. ¿El firewall está bloqueando el puerto? (Consulte`iptables`/`ufw`o grupos de seguridad en la nube).
7. ¿Hay algún error en los registros de la aplicación?
8. ¿El certificado TLS es válido y confiable? (`openssl s_client -connect example.com:443`).