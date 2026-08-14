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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# Ansible と構成管理
Ansible は、エージェントレスの構成管理および自動化ツールです。 SSH (または Windows の場合は WinRM) を使用してサーバーに接続し、YAML Playbook で定義されたタスクを実行します。すべてのマシンにエージェントをインストールする必要があるツールとは異なり、Ansible はプッシュベースであり、制御ノードからコマンドを実行します。これは、サーバーのプロビジョニング、アプリケーションの展開、構成管理、およびアドホック タスクの実行に使用されます。
---

## コアコンセプト
|コンセプト |説明 |
|----------|---------------|
| **在庫** |管理対象ホストのリスト (INI または YAML 形式) |
| **プレイブック** |実行する一連のタスクを定義する YAML ファイル |
| **プレイ** |プレイブック内のホストとタスク間のマッピング |
| **タスク** |ホスト上で実行する単一のアクション |
| **モジュール** |作業単位 (例:`apt`、`copy`、`service`、`template`)
| **役割** |タスク、変数、ファイル、ハンドラーの再利用可能なコレクション |
| **変数** | Playbook で使用される動的値 |
| **ハンドラー** |通知によってトリガーされるタスク (サービスの再起動など) |
| **事実** |ホストに関して収集されたシステム情報 (OS、IP など) |
---

## 一般的なコマンド
|コマンド |説明 |
|----------|---------------|
| `ansible all -m ping`|すべてのホストへの接続をテストする |
| `ansible all -m shell -a "uptime"`|すべてのホストでシェル コマンドを実行します。
| `ansible-playbook site.yml`|プレイブックを実行する |
| `ansible-playbook site.yml --check`|ドライラン（チェックモード） |
| `ansible-playbook site.yml --diff`|何が変わるかを示す |
| `ansible-playbook site.yml -l web`|特定のグループに対して実行する |
| `ansible-playbook site.yml --tags deploy`|特定のタグを持つタスクのみを実行する |
| `ansible-playbook site.yml --skip-tags debug`|特定のタグを持つタスクをスキップする |
| `ansible-vault encrypt secrets.yml`|ファイルを暗号化する |
| `ansible-vault decrypt secrets.yml`|ファイルを復号化する |
| `ansible-vault edit secrets.yml`|暗号化されたファイルを編集する |
| `ansible-galaxy install geerlingguy.nginx`| Ansible Galaxy からロールをインストールする |
| `ansible-inventory --graph`|在庫をグラフで表示 |
| `ansible-doc apt`|モジュールのドキュメントを表示 |
---

## インベントリ形式
### INI フォーマット
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

### YAML 形式
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

## ハンドブックの構造
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

## 共通モジュール
|モジュール |目的 |例 |
|----------|-----------|----------|
| **apt / yum / dnf** |パッケージ管理 | `apt: name=nginx state=present`|
| **コピー** |ファイルをホストにコピーする | `copy: src=file.txt dest=/tmp/`|
| **テンプレート** | Jinja2 変数を使用してファイルをコピーする | `template: src=conf.j2 dest=/etc/app.conf`|
| **ファイル** |ファイルとディレクトリを管理する | `file: path=/tmp/dir state=directory`|
| **サービス** |サービスの管理 | `service: name=nginx state=restarted`|
| **ユーザー / グループ** |ユーザーとグループを管理する | `user: name=deploy shell=/bin/bash`|
| **クロン** | cron ジョブを管理する | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **シェル/コマンド** |コマンドを実行する | `shell: echo "hello" > /tmp/test`|
| **git** |リポジトリのクローンを作成する | `git: repo=https://... dest=/opt/app`|
| **システム** | systemd ユニットを管理する | `systemd: name=myapp enabled=true`|
| **ファイアウォール/ufw** |ファイアウォール ルールを管理する | `ufw: rule=allow port=80 proto=tcp`|
| **ラインインファイル** |ファイル内の行を管理する | `lineinfile: path=/etc/hosts line="..."`|
| **ブロックインファイル** |ファイル内のテキストのブロックを管理する |構成のブロックを挿入/更新する |
| **フェッチ** |ホストからファイルをコピーする | `fetch: src=/var/log/app.log dest=/local/`|
| **うり** | Web サービスと対話する | `uri: url=https://api.example.com method=GET`|
| **デバッグ** |メッセージを印刷する | `debug: msg="Deployed {{ app_version }}"`|
---

## 役割構造
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

## ヒントとトラブルシューティング
|ヒント |説明 |
|-----|---------------|
| **チェックモードを使用** |変更を適用する前に必ず`--check --diff`|
| **タグを使用する** |選択的に実行するためにタスクにタグを付ける |
| **シークレットにはボールトを使用** |パスワードをプレーンテキストで保存しないでください。
| **べき等性** |タスクは複数回実行しても安全である必要があります。
| **becomeを使用** |権限昇格には`become: true`を使用します。
| **並列処理を制限する** |`--forks`を使用して同時接続を制御する |
| **Vagrant / Docker を使用したテスト** |本番環境で実行する前にプレイブックをローカルでテストする |
| **`--step` を使用してください ** |インタラクティブモード: 実行前に各タスクを確認 |
---

＃＃ まとめ
Ansible は、SSH 経由で実行される YAML プレイブックを通じてサーバー構成とアプリケーションのデプロイメントを自動化します。ワークフローは次のとおりです。インベントリを定義→プレイブックを作成→`ansible-playbook`を実行します。主要な概念には、モジュール (作業単位)、ロール (再利用可能なコレクション)、ハンドラー (トリガーされたタスク)、および変数 (動的値) が含まれます。共通モジュールは、パッケージ管理、ファイル操作、サービス制御、およびユーザー管理をカバーします。適用する前に必ずチェック モードを使用してください。シークレットを Ansible Vault に保存します。タスクが冪等であることを確認します。運用環境で実行する前にローカルでテストします。