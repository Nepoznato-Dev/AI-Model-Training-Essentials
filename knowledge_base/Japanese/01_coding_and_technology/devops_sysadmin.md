---
# Metadata
title: "DevOps and System Administration"
description: "SSH, systemd, logging, monitoring, backups, Docker, CI/CD"
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

# DevOps とシステム管理
サーバーの管理、運用の自動化、信頼性の高いインフラストラクチャの維持に関する実践的なガイド。
---

## SSH (セキュアシェル)
### 鍵の生成
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"   # Modern and secure
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # Fallback
```

### 公開キーをサーバーにコピー
```bash
ssh-copy-id user@host
# Manual alternative:
cat ~/.ssh/id_ed25519.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### SSH 構成 (`~/.ssh/config`)
```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/mykey
    Port 2222
```

### 一般的な SSH コマンド
```bash
ssh user@host                              # Connect
ssh -J jumpuser@jumphost user@target       # Proxy jump
scp file.txt user@host:/path/              # Copy file to remote
scp user@host:/path/file.txt .             # Copy from remote
rsync -avz -e ssh ./local/ user@host:/remote/  # Efficient sync
```

### SSH の強化
- root ログインを無効にする:`PermitRootLogin no`
- キーベースの認証のみを使用します:`PasswordAuthentication no`
- デフォルトのポートを変更します (オプション、隠蔽によるセキュリティ)。
-`AllowUsers`または`AllowGroups`を有効にしてアクセスを制限します。
---

## Systemd (Linux サービス管理)
### 一般的なコマンド
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

### systemd サービスユニットの作成
`/etc/systemd/system/myapp.service` を作成します。
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

それから：
```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## Journalctl (ログの表示)
```bash
journalctl -u myapp              # Logs for service
journalctl -f                    # Follow (tail) logs
journalctl --since "1 hour ago"
journalctl _PID=1234             # Filter by process ID
```

---

## ロギング戦略
### 構造化ロギング
JSON 形式を使用して、ログを機械で解析できるようにします。
```python
import structlog
logger = structlog.get_logger()
logger.info("user_login", user_id=123, ip="192.168.1.1")
```

### ログレベル
|レベル |目的 |
|------|-----------|
| **デバッグ** |詳細な診断情報 |
| **情報** |一般イベント (開始、停止、通常のトランザクション) |
| **警告** |予想外だが致命的ではない |
| **エラー** |特定の操作を妨げるエラー |
| **致命的/重大** |システムのシャットダウン |
### ログの集約
- **ELK スタック** (Elasticsearch、Logstash、Kibana) または Elastic Cloud。
- **Loki + Grafana** (軽量の代替品)。
- **Datadog、Splunk、Sumo Logic** (SaaS)。
### ログローテーション (`logrotate`)
ログがディスクをいっぱいにするのを防ぎます。`/etc/logrotate.d/myapp`を構成します。
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

## 監視とアラート
### 監視するメトリクス
|カテゴリー |主要な指標 |
|----------|---------------|
| **システム** | CPU、RAM、ディスク使用量、負荷平均、ネットワーク I/O |
| **アプリケーション** |リクエスト率、レイテンシー (p50、p95、p99)、エラー率、アクティブなセッション |
| **データベース** |クエリ数、遅いクエリ、接続プールの使用率 |
| **ビジネス** |ユーザーのサインアップ、コンバージョン率、収益 |
### ツール
- **Prometheus + Grafana**: 標準のオープンソース スタック。
- システム メトリクスの **ノード エクスポーター**。
- エンドポイントの可用性のための **Blackbox Exporter**。
- **Alertmanager** アラート ルーティング用。
- **クラウド ネイティブ**: AWS CloudWatch、Azure Monitor、GCP モニタリング。
### 稼働時間の監視
- Pingdom、Statuspage、Better Uptime、Uptime Kuma (自己ホスト型)。
- ヘルスチェック: サービスが正常な場合に 200 を返す`/health`エンドポイントを公開します。
---

## バックアップ戦略
### 3-2-1 ルール
- データの **3** コピー。
- **2** の異なるメディア タイプ (例: SSD + テープ、またはローカル + クラウド)。
- **1** オフサイト (クラウドまたはリモート データ センターなど) にコピーします。
### バックアップの種類
|タイプ |説明 |トレードオフ |
|------|---------------|----------|
| **フル** |すべてをコピー |遅い、スペースが重い |
| **増分** |前回の完全または増分以降の変更のみをコピーします。高速で複雑な復元 |
| **差分** |前回のフル以降の変更をコピー |中間点 |
### データベースのバックアップ
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

### ファイルのバックアップ
```bash
# Tar archive
tar -czf backup.tar.gz /var/lib/data

# Rsync to remote
rsync -avz /local/data/ user@backup-server:/backup/data/

# Cloud CLI (e.g., AWS S3)
aws s3 sync /local/data s3://my-bucket/backup/
```

### 自動バックアップ スケジュール (cron)
```cron
# Run daily at 2am
0 2 * * * /usr/local/bin/backup_script.sh
```

---

## Cron ジョブとスケジュールされたジョブ
### Cron 構文
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0=Sun)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### 例
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

### Cron の管理
```bash
crontab -l          # List current user's cron jobs
crontab -e          # Edit
crontab -r          # Remove all
```

### アナクロン
24 時間年中無休で稼働していないシステム (ラップトップなど) に使用されます。最終的にジョブが確実に実行されるようにします。
---

## パッケージの管理と更新
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

### セキュリティアップデート
セキュリティ パッチのために Ubuntu で`unattended-upgrades`を有効にします。
```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 本番環境の Docker
### ベストプラクティス
-`latest`ではなく、特定のイメージ タグ (`python:3.12-slim`) を使用します。
- 非 root ユーザーとしてコンテナを実行します。
- イメージをスキャンして脆弱性を探します (`docker scan`、`trivy`)。
- リソース制限を設定します (`--memory`、`--cpus`)。
- シークレットを使用します (Docker シークレットまたは環境を使用する場合は注意してください)。
- 画像を小さく保ちます: マルチステージビルド、アルパインベース。
### 本番環境での Docker Compose
`docker-compose.yml` でリソース制限を設定します。
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

## CI/CD の基本
### パイプラインのステージ
|ステージ |説明 |
|------|-----------|
| **ビルド** |コードをコンパイルし、依存関係をインストールする |
| **テスト** |ユニット、統合、lint チェックを実行する |
| **コンテナ化** | Docker イメージをビルドする |
| **プッシュ** |イメージをコンテナー レジストリにプッシュする |
| **展開** |ステージング/実稼働環境を更新する |
### ツール
|ツール |メモ |
|------|------|
| **GitHub アクション** | GitHub との統合 |
| **GitLab CI** | GitLab に組み込まれています |
| **ジェンキンス** |従来型、高度に構成可能 |
| **CircleCI、トラビス CI** |人気のサードパーティ |
| **アルゴCD** | Kubernetes 向け GitOps |
### GitHub アクションの例
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

## システムのチューニングとトラブルシューティング
### ディスク容量を確認する
```bash
df -h                      # Human-readable disk usage
du -sh /* | sort -h        # Size of top-level directories
```

### メモリ使用量を確認する
```bash
free -m                    # Memory in MB
vmstat 1 10                # Virtual memory statistics
top -o %MEM                # Sort processes by memory
```

### CPU 負荷を確認する
```bash
uptime                     # Load average over 1,5,15 minutes
top -o %CPU                # Sort processes by CPU
mpstat -P ALL 1 5          # Per-core CPU usage
```

### ネットワークを確認してください
```bash
netstat -i                 # Interface statistics
iftop                      # Live bandwidth usage (requires install)
nload                      # Another bandwidth monitor
```

### 大きなファイルを検索する
```bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
```

---

## コードとしてのインフラストラクチャ (IaC)
### テラフォーム
HCL でクラウド リソースを宣言します。
```hcl
provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### アンシブル
YAML を使用したエージェントレス構成管理。
```yaml
- name: Install nginx
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### ベストプラクティス
- 再利用可能にするためにモジュールとロールを使用します。
- 状態をリモートに保存します (S3、Terraform Cloud)。
- 変数とシークレットを使用します (ハードコードされていない環境経由の `AWS_SECRET_ACCESS_KEY`)。
- IaC コードのバージョン管理。
---

## インシデント対応 (オンコール)
### サービス停止のチェックリスト
1. アラートを確認します。
2. Assess scope: Which services/users are affected?
3. Identify the issue (look at logs, metrics, recent deployments).
4. Contain if possible (circuit breakers, feature flags).
5. ロールバックまたは修正を進めます。
6. Communicate status to stakeholders and users (status page).
7. インシデントのタイムラインとアクションを文書化します。
8. Post-mortem: within 24–48 hours, write a root cause analysis (RCA) and action items to prevent recurrence.