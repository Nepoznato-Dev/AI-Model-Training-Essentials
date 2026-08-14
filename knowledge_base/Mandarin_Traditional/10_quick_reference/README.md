# 快速參考
針對程式語言、命令列工具、基礎設施和 DevOps 的備忘單和快速參考指南的結構化集合 - 專為日常工作中的快速查找而設計。
＃＃ 結構
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

## 檔案（按子類別）
### 編程
|文件|描述 |
|------|-------------|
|[python_syntax.md](programming/python_syntax.md)| Python 語法備忘單 |
|[sql_quick_ref.md](programming/sql_quick_ref.md)| SQL查詢參考|
|[regular_expressions.md](programming/regular_expressions.md)|正規表示式語法、常見模式、特定語言的用法 |
|[git_commands.md](programming/git_commands.md)| Git 指令與工作流程 |
### 基礎設施
|文件|描述 |
|------|-------------|
|[linux_commands.md](infrastructure/linux_commands.md)| Linux 命令列參考 |
|[bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Bash 腳本、文字處理、有用的俏皮話 |
|[docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker、Docker Compose、Kubernetes、Helm 備忘單 |
|[cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| AWS、Azure 與 GCP 並排比較 |
|[ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Ansible 劇本、模組、角色、自動化 |
|[terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| IaC 概念、Terraform 指令、狀態管理 |
|[cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions、GitLab CI、Jenkins、管道 YAML 模式 |
|[prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL、導出器、儀表板、警報 |
## 建議的閱讀路徑
### **DevOps 工程師路徑**
1.`infrastructure/linux_commands.md`— Linux 基礎知識
2.`infrastructure/bash_and_shell_scripting.md`— Shell 腳本
3.`infrastructure/docker_and_kubernetes.md`— 容器與編排
4.`infrastructure/cicd_pipeline_config.md`— CI/CD 管道
5.`infrastructure/terraform_quick_ref.md`— 基礎設施即程式碼
6.`infrastructure/prometheus_and_grafana.md`— 監控
### **開發者必備路徑**
1.`programming/python_syntax.md`— Python 參考
2.`programming/sql_quick_ref.md`— 資料庫查詢
3.`programming/git_commands.md`— 版本控制
4.`programming/regular_expressions.md`— 模式匹配