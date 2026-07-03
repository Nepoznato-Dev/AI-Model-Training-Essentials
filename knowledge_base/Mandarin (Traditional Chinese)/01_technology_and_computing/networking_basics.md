# 網路基礎

面向開發者和系統管理員的實用參考資料——涵蓋核心概念、協定、指令與疑難排解。

---

## OSI 模型（7 層）

這是一個用於理解網路通訊的概念性框架。

| 層 | 名稱 | 功能 | 範例協定 |
|-------|------|----------|-------------------|
| 7 | 應用層 | 面向終端使用者的服務 | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | 表示層 | 資料格式化、加密、壓縮 | TLS, JPEG, ASCII |
| 5 | 會話層 | 連線管理 | NetBIOS, RPC |
| 4 | 傳輸層 | 端對端傳輸、糾錯、流量控制 | TCP, UDP |
| 3 | 網路層 | 路由、定址 | IP, ICMP, OSPF, BGP |
| 2 | 資料鏈結層 | 成幀、差錯檢測、MAC 位址 | Ethernet, Wi-Fi, PPP |
| 1 | 實體層 | 原始位元傳輸 | Ethernet cables, fiber optics, radio waves |

在實際應用中，**TCP/IP 模型**（4 層：Link、Internet、Transport、Application）更常用於網際網路。

---

## IP 定址

### IPv4
- 32 位元位址，以四組八位元表示：`192.168.1.1`
- 總量：約 43 億個位址（實際上已近乎耗盡）。

### IPv6
- 128 位元位址，以十六進位表示：`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 總量：2¹²⁸ 個位址（幾乎可視為無限）。

### 私有 IP 位址範圍（RFC 1918）
這些位址不能在網際網路上路由，用於區域網路內部：
- `10.0.0.0/8` (10.0.0.0 – 10.255.255.255)
- `172.16.0.0/12` (172.16.0.0 – 172.31.255.255)
- `192.168.0.0/16` (192.168.0.0 – 192.168.255.255)

### CIDR 表示法
`192.168.1.0/24` 表示前 24 位元是網路前綴，後 8 位元是主機位。涵蓋 `192.168.1.0` 至 `192.168.1.255` 之間的位址。

---

## DNS（網域名稱系統）

將網域名稱（例如 `example.com`）對應至 IP 位址。

### 記錄類型
| 類型 | 用途 |
|------|---------|
| **A** | 將網域名稱對應至 IPv4 位址 |
| **AAAA** | 將網域名稱對應至 IPv6 位址 |
| **CNAME** | 指向另一個網域名稱的別名 |
| **MX** | 郵件交換伺服器 |
| **TXT** | 任意文字（SPF、DKIM、驗證資訊） |
| **NS** | 網域名稱的權威名稱伺服器 |
| **SRV** | 服務記錄（例如用於 SIP） |

### 常用工具
```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)

連接埠與協定
知名連接埠（0–1023）
連接埠	協定	服務
20, 21	TCP	FTP
22	TCP	SSH
23	TCP	Telnet
25	TCP	SMTP
53	UDP/TCP	DNS
80	TCP	HTTP
110	TCP	POP3
123	UDP	NTP
143	TCP	IMAP
443	TCP	HTTPS
465	TCP	SMTPS
587	TCP	SMTP (submission)
993	TCP	IMAPS
995	TCP	POP3S
3306	TCP	MySQL
5432	TCP	PostgreSQL
6379	TCP	Redis
27017	TCP	MongoDB
查看開放連接埠
bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
TCP 與 UDP
特性	TCP	UDP
連線方式	連線導向（需握手）	無連線
可靠性	保證交付、支援重傳	盡力而為（可能丟包）
順序保證	保留順序	不保證順序
流量控制	有（滑動視窗）	無
使用場景	Web（HTTP）、電子郵件、SSH、檔案傳輸	DNS、串流媒體、VoIP、遊戲、SNMP
標頭大小	20–60 位元組	8 位元組
HTTP 與 HTTPS
HTTP 方法
GET：取得資源（冪等、安全）。

POST：提交資料（非冪等）。

PUT：更新或取代資源（冪等）。

PATCH：部分更新。

DELETE：刪除資源（冪等）。

狀態碼
1xx：資訊性（100 Continue）。

2xx：成功（200 OK、201 Created、204 No Content）。

3xx：重新導向（301 Moved Permanently、302 Found、304 Not Modified）。

4xx：客戶端錯誤（400 Bad Request、401 Unauthorized、403 Forbidden、404 Not Found、429 Too Many Requests）。

5xx：伺服器錯誤（500 Internal Server Error、502 Bad Gateway、503 Service Unavailable）。

標頭
Content-Type：媒體類型（application/json、text/html）。

Authorization：憑證（例如 Bearer <token>）。

Cache-Control：快取策略。

CORS 標頭：Access-Control-Allow-Origin 等。

TLS/SSL
加密 HTTP 流量（HTTPS = HTTP over TLS）。

憑證由憑證授權機構（CA）簽發，用於驗證伺服器身分。

用戶端需驗證憑證鏈與主機名稱。

防火牆與 NAT
防火牆
依據規則（來源 IP、目的 IP、連接埠、協定）過濾流量。

狀態型防火牆可追蹤連線狀態。

NAT（網路位址轉換）
將私有 IP 轉換為公用 IP 以連接網際網路。

連接埠轉發：將公用連接埠對應至內部主機與連接埠。

常用網路指令
連線測試
bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
路由
bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
網路介面
bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
DNS
bash
dig example.com
nslookup example.com
host example.com
連接埠連線測試
bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
防火牆（Linux iptables/nftables）
bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
網路統計
bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
子網路劃分（快速參考）
CIDR	子網路遮罩	位址總數	可用主機數
/32	255.255.255.255	1	1
/30	255.255.255.252	4	2
/29	255.255.255.248	8	6
/28	255.255.255.240	16	14
/27	255.255.255.224	32	30
/26	255.255.255.192	64	62
/25	255.255.255.128	128	126
/24	255.255.255.0	256	254
/23	255.255.254.0	512	510
/22	255.255.252.0	1,024	1,022
/16	255.255.0.0	65,536	65,534
/8	255.0.0.0	16,777,216	16,777,214
負載平衡與反向代理
Nginx 作為反向代理
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
負載平衡演算法
輪詢（Round-robin）

最少連線（Least connections）

IP 雜湊（IP hash，實現工作階段黏性）

加權輪詢（Weighted round-robin）

工具
Nginx、HAProxy（軟體）

AWS ELB、Azure Load Balancer、GCP Cloud Load Balancing（雲端）

疑難排解檢查清單
實體連結是否正常？（檢查網路線、Wi-Fi 連線）。

能否 ping 通閘道？（例如 ping 192.168.1.1）。

能否 ping 通外部 IP？（例如 8.8.8.8）。

能否解析網域名稱？（dig google.com）。

應用程式是否在預期連接埠上監聽？（ss -tulpn | grep 8080）。

防火牆是否封鎖該連接埠？（檢查 iptables/ufw 或雲端安全性群組）。

應用程式日誌是否有錯誤？

TLS 憑證是否有效且受信任？（openssl s_client -connect example.com:443）。

text

---

## 檔案 6：`devops_sysadmin.md`

```markdown
# DevOps 與系統管理

伺服器管理、運維自動化與維護可靠基礎設施的實用指南。

---

## SSH（Secure Shell）

### 金鑰生成
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
將公鑰複製至伺服器
bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
SSH 設定檔（~/.ssh/config）
ssh-config
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
常用 SSH 指令
bash
ssh user@host                    # Connect
ssh -J jumpuser@jumphost user@target   # Proxy jump
scp file.txt user@host:/path/     # Copy file to remote
scp user@host:/path/file.txt .    # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
強化 SSH 安全性
停用 root 登入：PermitRootLogin no

僅使用金鑰認證：PasswordAuthentication no

更改預設連接埠（選用，透過隱匿提升安全性）。

啟用 AllowUsers 或 AllowGroups 限制存取權限。

Systemd（Linux 服務管理）
常用指令
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
建立 systemd 服務單元
建立 /etc/systemd/system/myapp.service：

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
接著執行：

bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
Journalctl（查看日誌）
bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
日誌策略
結構化日誌
使用 JSON 格式使日誌可由機器解析：

python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
日誌等級
DEBUG：詳細的診斷資訊。

INFO：一般事件（啟動、停止、正常交易）。

WARN：意外但不致命的狀況。

ERROR：導致特定操作失敗的錯誤。

FATAL/CRITICAL：系統關閉。

日誌匯總
ELK Stack（Elasticsearch、Logstash、Kibana）或 Elastic Cloud。

Loki + Grafana（輕量替代方案）。

Datadog、Splunk、Sumo Logic（SaaS）。

日誌輪轉（logrotate）
防止日誌佔滿磁碟。設定 /etc/logrotate.d/myapp：

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
監控與告警
監控指標
系統：CPU、RAM、磁碟使用率、負載平均值、網路 I/O。

應用程式：請求速率、延遲（p50、p95、p99）、錯誤率、活躍工作階段數。

資料庫：查詢次數、慢查詢、連線池使用情況。

業務：使用者註冊數、轉換率、營收。

工具
Prometheus + Grafana：標準開源組合。

Node Exporter：用於系統指標。

Blackbox Exporter：用於端點可用性監控。

Alertmanager：用於告警路由。

雲端原生：AWS CloudWatch、Azure Monitor、GCP Monitoring。

運行時間監控
Pingdom、Statuspage、Better Uptime、Uptime Kuma（自架）。

健康檢查：公開 /health 端點，服務正常時回傳 200。

備份策略
3-2-1 原則
3 份資料副本。

2 種不同媒體類型（例如 SSD + 磁帶，或本地 + 雲端）。

1 份異地備份（例如雲端或遠端資料中心）。

備份類型
完整備份：複製所有資料（速度慢、空間需求大）。

增量備份：僅複製自上次完整或增量備份以來的變更（速度快，但還原較複雜）。

差異備份：複製自上次完整備份以來的變更（介於兩者之間）。

資料庫備份
bash
# PostgreSQL
pg_dump dbname > backup.sql
pg_dumpall > all_backup.sql

# MySQL / MariaDB
mysqldump -u root -p dbname > backup.sql

# Restore
psql dbname < backup.sql
mysql -u root -p dbname < backup.sql
檔案備份
bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
自動備份排程（cron）
cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
Cron 與排程任務
Cron 語法
text
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
範例
cron
# Every 5 minutes
*/5 * * * * /path/to/script

# Every day at 3:15 AM
15 3 * * * /path/to/script

# Every Monday at 4 AM
0 4 * * 1 /path/to/script

# Every hour
0 * * * * /path/to/script
管理 Cron
bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
Anacron
適用於未全天候運行的系統（例如筆記型電腦），確保任務最終會執行。

套件管理與更新
Debian/Ubuntu（apt）
bash
sudo apt update                # Update package list
sudo apt upgrade               # Upgrade all packages
sudo apt install git nginx
sudo apt remove git
sudo apt autoremove            # Remove unused dependencies
RHEL/CentOS/Fedora（dnf/yum）
bash
sudo dnf check-update
sudo dnf update
sudo dnf install git nginx
sudo dnf remove git
安全性更新
在 Ubuntu 上啟用 unattended-upgrades 以自動套用安全性修補程式：

bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
Docker 正式環境部署
最佳實踐
使用明確的映像標籤（如 python:3.12-slim），避免使用 latest。

以非 root 使用者執行容器。

掃描映像是否存在漏洞（docker scan、trivy）。

設定資源限制（--memory、--cpus）。

謹慎使用機密（透過 Docker secrets 或環境變數）。

保持映像精簡：使用多階段建置、alpine 基底映像。

Docker Compose 正式環境部署
在 docker-compose.yml 中設定資源限制：

yaml
services:
  app:
    image: myapp:1.0
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
CI/CD 基礎
流水線階段
建置（Build）：編譯程式碼、安裝相依套件。

測試（Test）：執行單元測試、整合測試與程式碼風格檢查。

容器化（Containerise）：建置 Docker 映像。

推送（Push）：將映像推送至容器登錄中心。

部署（Deploy）：更新預備環境或正式環境。

工具
GitHub Actions：與 GitHub 深度整合。

GitLab CI：內建於 GitLab。

Jenkins：傳統工具，高度可設定。

CircleCI、Travis CI：廣泛使用的第三方工具。

ArgoCD：適用於 Kubernetes 的 GitOps 工具。

GitHub Action 範例（簡單版）：
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
系統調校與疑難排解
查看磁碟空間
bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
查看記憶體使用情況
bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
查看 CPU 負載
bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
查看網路狀況
bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
尋找大型檔案
bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
基礎設施即程式碼（IaC）
Terraform
以 HCL 宣告雲端資源。

hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
Ansible
使用 YAML 進行無代理程式的組態管理。

yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
最佳實踐
使用模組與角色（roles）提升可重用性。

將狀態遠端儲存（S3、Terraform Cloud）。

使用變數與機密（透過環境變數傳入 AWS_SECRET_ACCESS_KEY，勿寫死）。

對 IaC 程式碼進行版本控制。

事件回應（On-call 值班）
服務中斷檢查清單
確認告警。

評估範圍：哪些服務或使用者受到影響？

找出問題（查看日誌、指標、近期部署）。

盡可能隔離問題（熔斷機制、功能旗標）。

回滾或向前修復。

向利害關係人與使用者溝通狀態（狀態頁面）。

記錄事件時間線與處理動作。

事後分析：在 24–48 小時內撰寫根本原因分析（RCA）及防止再發的行動項目。
