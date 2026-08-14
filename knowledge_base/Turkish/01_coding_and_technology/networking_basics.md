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
# Ağ Temelleri
Geliştiriciler ve sistem yöneticileri için pratik bir referans — temel kavramlar, protokoller, komutlar ve sorun giderme.
---

## OSI Modeli (7 Katman)
Ağ iletişimini anlamak için kavramsal bir çerçeve.
| Katman | İsim | İşlev | Örnek protokoller |
|----------|------|----------|-----------|
| 7 | Başvuru | Son kullanıcı hizmetleri | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | Sunum | Veri biçimlendirme, şifreleme, sıkıştırma | TLS, JPEG, ASCII |
| 5 | Oturum | Bağlantı yönetimi | NetBIOS, RPC |
| 4 | Taşıma | Uçtan uca teslimat, hata düzeltme, akış kontrolü | TCP, UDP |
| 3 | Ağ | Yönlendirme, adresleme | IP, ICMP, OSPF, BGP |
| 2 | Veri Bağlantısı | Çerçeveleme, hata tespiti, MAC adresleri | Ethernet, Wi-Fi, PPP |
| 1 | Fiziksel | Ham bit iletimi | Ethernet kabloları, fiber optikler, radyo dalgaları |
Uygulamada **TCP/IP modeli** (4 katman: Bağlantı, İnternet, Aktarım, Uygulama) daha çok internet için kullanılır.
---

## IP Adresleme
### IPv4
- 32 bitlik adres, dört sekizli olarak yazılır:`192.168.1.1`
- Toplam: ~4,3 milyar adres (ancak pratikte tükendi).
### IPv6
- 128 bitlik adres, onaltılı olarak yazılmıştır:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Toplam: 2¹²⁸ adres (pratik olarak sonsuz).
### Özel IP Aralıkları (RFC 1918)
Bunlar internette yönlendirilemez; yerel ağlarda kullanılır:
-`10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16` (192.168.0.0 – 192.168.255.255)
### CIDR Notasyonu
 `192.168.1.0/24`, ilk 24 bitin ağ öneki olduğu anlamına gelir; son 8 bit ana bilgisayarlardır.`192.168.1.0`ile`192.168.1.255`arasındaki adresleri içerir.
---

## DNS (Alan Adı Sistemi)
Etki alanı adlarını (ör. `example.com`) IP adresleriyle eşler.
### Kayıt Türleri
| Tür | Amaç |
|------|------------|
| **Bir** | Etki alanını IPv4 adresiyle eşler |
| **AAAA** | Etki alanını IPv6 adresiyle eşler |
| **CNAME** | Başka bir alan adının takma adı |
| **MX** | Posta değişim sunucusu |
| **TXT** | Rastgele metin (SPF, DKIM, doğrulama) |
| **NS** | Alan adı için ad sunucusu |
| **SRV** | Hizmet kaydı (örn. SIP için) |
### Ortak Araçlar```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## Bağlantı Noktaları ve Protokoller
### Tanınmış Bağlantı Noktaları (0–1023)
| Liman | Protokol | Hizmet |
|------|----------|-----------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet'te |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTP'LER |
| 587 | TCP | SMTP (gönderim) |
| 993 | TCP | IMAP'ler |
| 995 | TCP | POP3'LER |
| 3306 | TCP | MySQL |
| 5432 | TCP | PostgreSQL |
| 6379 | TCP | Redis |
| 27017 | TCP | MongoDB |
### Açık Bağlantı Noktalarını Kontrol Edin
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP ve UDP
| Özellik | TCP | UDP |
|-----------|-----|-----|
| Bağlantı | Bağlantı odaklı (tokalaşma) | Bağlantısız |
| Güvenilirlik | Garantili teslimat, yeniden iletim | En iyi çaba (paketlerin düşmesine neden olabilir) |
| Sipariş | Siparişi korur | Sipariş garantisi yok |
| Akış kontrolü | Evet (sürgülü pencere) | Hayır |
| Kullanım durumları | Web (HTTP), e-posta, SSH, dosya aktarımı | DNS, akış, VoIP, oyun, SNMP |
| Başlık boyutu | 20–60 bayt | 8 bayt |
---

## HTTP ve HTTPS
### HTTP Yöntemleri
| Yöntem | Açıklama |
|----------|----------------|
| **ALIN** | Bir kaynağı alın (idempotent, güvenli) |
| **GÖNDERİ** | Verileri gönderin (idampotent değil) |
| **koy** | Kaynağı güncelleme/değiştirme (idempotent) |
| **YAMA** | Kısmi güncelleme |
| **SİL** | Kaynağı kaldırma (idempotent) |
### Durum Kodları
| Kod | Anlamı |
|------|------------|
| **1xx** | Bilgilendirici (100 Devam) |
| **2xx** | Başarılı (200 Tamam, 201 Oluşturuldu, 204 İçerik Yok) |
| **3xx** | Yönlendirme (301 Kalıcı Olarak Taşındı, 302 Bulundu, 304 Değiştirilmedi) |
| **4xx** | İstemci hatası (400 Hatalı İstek, 401 Yetkisiz, 403 Yasak, 404 Bulunamadı, 429 Çok Fazla İstek) |
| **5xx** | Sunucu hatası (500 Dahili Sunucu Hatası, 502 Bozuk Ağ Geçidi, 503 Hizmet Kullanılamıyor) |
### Başlıklar
| Başlık | Amaç |
|----------|------------|
| `Content-Type`| Ortam türü (`application/json`, `text/html`) |
| `Authorization`| Kimlik bilgileri (ör.`Bearer <token>`) |
| `Cache-Control`| Önbelleğe alma politikası |
| CORS başlıkları | `Access-Control-Allow-Origin`, vb. |
---

## TLS/SSL
HTTP trafiğini şifreler (HTTPS = TLS üzerinden HTTP).
- Sertifika Yetkililerinden (CA'lar) alınan sertifikalar sunucunun kimliğini doğrular.
- İstemci tarafında sertifika zincirini ve ana bilgisayar adını doğrulayın.
---

## Güvenlik Duvarları ve NAT
### Güvenlik Duvarı
- Trafiği kurallara (kaynak IP, hedef IP, bağlantı noktası, protokol) göre filtreler.
- Durum bilgisi olan güvenlik duvarları bağlantı durumlarını izler.
### NAT (Ağ Adresi Çevirisi)
- İnternet erişimi için özel IP'leri genel IP'ye çevirir.
- Bağlantı noktası yönlendirme: genel bağlantı noktasını dahili bir ana bilgisayar/bağlantı noktasıyla eşler.
---

## Ortak Ağ Komutları
### Bağlantı Testleri
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### Yönlendirme
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### Ağ Arayüzleri
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

### Bir Bağlantı Noktasına Bağlantı
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### Güvenlik Duvarı (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### Ağ İstatistikleri
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## Alt Ağ Oluşturma (Hızlı Başvuru)
| CIDR | Ağ Maskesi | Adres sayısı | Kullanılabilir ana bilgisayarlar |
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

## Yük Dengeleme ve Ters Proxy'ler
### Ters Proxy olarak Nginx
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

### Yük Dengeleme Algoritmaları
- **Ground-robin**
- **En az bağlantı**
- **IP karması** (oturumun tutarlılığı)
- **Ağırlıklı hepsini bir kez deneme**
### Aletler
- **Nginx, HAProxy** (yazılım)
- **AWS ELB, Azure Yük Dengeleyici, GCP Bulut Yük Dengeleme** (bulut)
---

## Sorun Giderme Kontrol Listesi
1. Fiziksel bağlantı kurulu mu? (Kabloları, Wi-Fi bağlantısını kontrol edin).
2. Ağ geçidine ping atabiliyor musunuz? (örneğin,`ping 192.168.1.1`).
3. Harici bir IP'ye ping atabiliyor musunuz? (örneğin,`8.8.8.8`).
4. Bir alan adını çözebilir misiniz? (`dig google.com`).
5. Uygulama beklenen bağlantı noktasını dinliyor mu? (`ss -tulpn | grep 8080`).
6. Güvenlik duvarı bağlantı noktasını engelliyor mu? (`iptables` /`ufw`veya bulut güvenlik gruplarını kontrol edin).
7. Uygulama günlüklerinde herhangi bir hata var mı?
8. TLS sertifikası geçerli ve güvenilir mi? (`openssl s_client -connect example.com:443`).