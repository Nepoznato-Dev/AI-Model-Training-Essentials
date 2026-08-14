# クイックリファレンス
プログラミング言語、コマンドライン ツール、インフラストラクチャ、DevOps に関するチートシートとクイック リファレンス ガイドの構造化されたコレクション。日常の作業中にすばやく検索できるように設計されています。
＃＃ 構造
```
10_quick_reference/
├── README.md                          ← You are here
├── programming/                       ← Language and tool syntax
│   ├── python_syntax.md                  Python syntax cheat sheet
│   ├── sql_quick_ref.md                  SQL query reference
│   ├── regular_expressions.md            Regex syntax and common patterns
│   └── git_commands.md                   Git commands and workflows
└── infrastructure/                    ← Systems, DevOps, and cloud
    ├── linux_commands.md                  Linux command line reference
    ├── bash_and_shell_scripting.md        Bash scripting and one-liners
    ├── docker_and_kubernetes.md           Docker, Compose, Kubernetes, Helm
    ├── cloud_services_comparison.md       AWS vs Azure vs GCP comparison
    ├── ansible_quick_ref.md               Ansible playbooks and automation
    ├── terraform_quick_ref.md             Terraform commands and IaC
    ├── cicd_pipeline_config.md            GitHub Actions, GitLab CI, Jenkins
    └── prometheus_and_grafana.md          PromQL, dashboards, alerting
```

## サブカテゴリ別のファイル
### プログラミング
|ファイル |説明 |
|------|---------------|
| [python_syntax.md](programming/python_syntax.md)| Python 構文のチートシート |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| SQL クエリのリファレンス |
| [regular_expressions.md](programming/regular_expressions.md)|正規表現構文、一般的なパターン、言語固有の使用法 |
| [git_commands.md](programming/git_commands.md)| Git コマンドとワークフロー |
### インフラストラクチャ
|ファイル |説明 |
|------|---------------|
| [linux_commands.md](infrastructure/linux_commands.md)| Linux コマンド ライン リファレンス |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Bash scripting, text processing, useful one-liners |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker, Docker Compose, Kubernetes, Helm cheat sheet |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| AWS、Azure、GCP を並べて比較 |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Ansible プレイブック、モジュール、ロール、自動化 |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| IaC concepts, Terraform commands, state management |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL、エクスポーター、ダッシュボード、アラート |
## 推奨される読書パス
### **DevOps エンジニア パス**
1.`infrastructure/linux_commands.md`— Linux の基礎
2.`infrastructure/bash_and_shell_scripting.md`— シェルスクリプト
3.`infrastructure/docker_and_kubernetes.md`— コンテナとオーケストレーション
4.`infrastructure/cicd_pipeline_config.md`— CI/CD パイプライン
5.`infrastructure/terraform_quick_ref.md`— コードとしてのインフラストラクチャ
6.`infrastructure/prometheus_and_grafana.md`— モニタリング
### **開発者向けエッセンシャル パス**
1.`programming/python_syntax.md`— Python リファレンス
2.`programming/sql_quick_ref.md`— データベースクエリ
3.`programming/git_commands.md`— バージョン管理
4.`programming/regular_expressions.md`— パターンマッチング