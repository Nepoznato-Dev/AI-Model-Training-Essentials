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

# ネットワークの基本
開発者とシステム管理者のための実用的なリファレンス - 中心的な概念、プロトコル、コマンド、トラブルシューティング。
---

## OSI モデル (7 層)
ネットワーク通信を理解するための概念的なフレームワーク。
|レイヤー |名前 |機能 |プロトコルの例 |
|------|------|----------|---------------------|
| 7 |アプリケーション |エンドユーザーサービス | HTTP、HTTPS、FTP、SMTP、DNS、SSH |
| 6 |プレゼンテーション |データのフォーマット、暗号化、圧縮 | TLS、JPEG、ASCII |
| 5 |セッション |接続管理 | NetBIOS、RPC |
| 4 |輸送 |エンドツーエンド配信、エラー修正、フロー制御 | TCP、UDP |
| 3 |ネットワーク |ルーティング、アドレス指定 | IP、ICMP、OSPF、BGP |
| 2 |データリンク |フレーミング、エラー検出、MAC アドレス |イーサネット、Wi-Fi、PPP |
| 1 |物理的 |生ビット送信 |イーサネットケーブル、光ファイバー、電波 |
実際には、**TCP/IP モデル** (4 層: リンク、インターネット、トランスポート、アプリケーション) がインターネットによく使用されます。
---

## IP アドレス指定
### IPv4
- 32 ビット アドレス、4 オクテットとして記述:`192.168.1.1`
- 合計: 約 43 億のアドレス (ただし、実際には使い果たされます)。
### IPv6
- 128 ビット アドレス、16 進数で記述:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 合計: 2¹²⁸ アドレス (実質的には無限)。
### プライベート IP 範囲 (RFC 1918)
これらはインターネット上でルーティングできません。ローカルネットワーク内で使用されます:
-`10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### CIDR 表記
`192.168.1.0/24`は、最初の 24 ビットがネットワーク プレフィックスであることを意味します。最後の 8 ビットはホストです。これには、アドレス`192.168.1.0`から`192.168.1.255`が含まれます。
---

## DNS (ドメインネームシステム)
ドメイン名 (例:`example.com`) を IP アドレスにマッピングします。
### レコードの種類
|タイプ |目的 |
|-----|----------|
| **A** |ドメインを IPv4 アドレスにマップします。
| **ああああ** |ドメインを IPv6 アドレスにマップします。
| **CNAME** |別のドメイン名のエイリアス |
| **MX** |メール交換サーバー |
| **TXT** |任意のテキスト (SPF、DKIM、検証) |
| **NS** |ドメインのネームサーバー |
| **SRV** |サービス記録 (SIP など) |
### 共通ツール```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## ポートとプロトコル
### 既知のポート (0 ～ 1023)
|ポート |プロトコル |サービス |
|------|----------|----------|
| 20、21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP |テルネット |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP |ポップ3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP (送信) |
| 993 | TCP | IMAP |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP |ポストグレSQL |
| 6379 | TCP |レディス |
| 27017 | TCP |モンゴDB |
### 開いているポートを確認する
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP と UDP の比較
|特集 | TCP | UDP |
|----------|-----|-----|
|接続 |接続指向 (ハンドシェイク) |コネクションレス |
|信頼性 |保証された配信、再送信 |ベスト エフォート (パケットがドロップされる可能性があります) |
|注文 |順序を保持します |注文保証なし |
|フロー制御 |はい (スライディング ウィンドウ) |いいえ |
|使用例 | Web (HTTP)、電子メール、SSH、ファイル転送 | DNS、ストリーミング、VoIP、ゲーム、SNMP |
|ヘッダー サイズ | 20 ～ 60 バイト | 8バイト |
---

## HTTP と HTTPS
### HTTP メソッド
|方法 |説明 |
|----------|---------------|
| **入手** |リソースを取得します (冪等、安全) |
| **投稿** |データを送信する (冪等ではない) |
| **置く** |リソースの更新/置換 (冪等) |
| **パッチ** |部分更新 |
| **削除** |リソースを削除する (冪等) |
### ステータスコード
|コード |意味 |
|-----|----------|
| **1xx** |情報 (100 継続) |
| **2xx** |成功 (200 OK、201 作成、204 コンテンツなし) |
| **3xx** |リダイレクト (301 は永続的に移動されました、302 は見つかりました、304 は変更されませんでした) |
| **4xx** |クライアント エラー (400 不正なリクエスト、401 不正、403 禁止、404 見つかりません、429 リクエストが多すぎます) |
| **5xx** |サーバー エラー (500 内部サーバー エラー、502 不正なゲートウェイ、503 サービス利用不可) |
### ヘッダー
|ヘッダー |目的 |
|--------|--------|
| `Content-Type`|メディア タイプ (`application/json`、`text/html`) |
| `Authorization`|資格情報 (例:`Bearer <token>`)
| `Cache-Control`|キャッシュポリシー |
| CORS ヘッダー | `Access-Control-Allow-Origin`など |
---

## TLS/SSL
HTTP トラフィックを暗号化します (HTTPS = HTTP over TLS)。
- 認証局 (CA) からの証明書によってサーバーが認証されます。
- クライアント側で証明書チェーンとホスト名を確認します。
---

## ファイアウォールと NAT
### ファイアウォール
- ルール (送信元 IP、宛先 IP、ポート、プロトコル) に基づいてトラフィックをフィルタリングします。
- ステートフル ファイアウォールは接続状態を追跡します。
### NAT (ネットワークアドレス変換)
- インターネット アクセス用にプライベート IP をパブリック IP に変換します。
- ポート転送: パブリック ポートを内部ホスト/ポートにマッピングします。
---

## 一般的なネットワーク コマンド
### 接続テスト
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

＃＃＃ ルーティング
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### ネットワークインターフェース
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

###DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### ポートへの接続
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### ファイアウォール (Linux iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### ネットワーク統計
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## サブネット化 (クイック リファレンス)
| CIDR |ネットマスク |アドレス数 |使用可能なホスト |
|-----|------|----------|--------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
---

## ロード バランシングとリバース プロキシ
### リバースプロキシとしての Nginx
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

### 負荷分散アルゴリズム
- **Round-robin**
- **Least connections**
- **IP ハッシュ** (セッション固定性)
- **加重ラウンドロビン**
### ツール
- **Nginx、HAProxy** (ソフトウェア)
- **AWS ELB、Azure Load Balancer、GCP クラウド ロード バランシング** (クラウド)
---

## トラブルシューティングのチェックリスト
1. 物理リンクはアップしていますか? (ケーブル、Wi-Fi 接続を確認してください)。
2. ゲートウェイに ping を送信できますか? (例:`ping 192.168.1.1`)。
3. 外部 IP に ping を実行できますか? (例:`8.8.8.8`)。
4. ドメインを解決できますか? (`dig google.com`)。
5. アプリケーションは予期されたポートでリッスンしていますか? (`ss -tulpn | grep 8080`)。
6. ファイアウォールがポートをブロックしていませんか? (`iptables` /`ufw`またはクラウド セキュリティ グループを確認してください)。
7. アプリケーション ログにエラーはありますか?
8. TLS 証明書は有効で信頼できるものですか? (`openssl s_client -connect example.com:443`)。