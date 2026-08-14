# 快速参考
针对编程语言、命令行工具、基础设施和 DevOps 的备忘单和快速参考指南的结构化集合 - 专为日常工作中的快速查找而设计。
＃＃ 结构
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

## 文件（按子类别）
### 编程
|文件|描述 |
|------|-------------|
| [python_syntax.md](programming/python_syntax.md)| Python 语法备忘单 |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| SQL查询参考|
| [regular_expressions.md](programming/regular_expressions.md)|正则表达式语法、常见模式、特定于语言的用法 |
| [git_commands.md](programming/git_commands.md)| Git 命令和工作流程 |
### 基础设施
|文件|描述 |
|------|-------------|
| [linux_commands.md](infrastructure/linux_commands.md)| Linux 命令行参考 |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Bash 脚本、文本处理、有用的俏皮话 |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker、Docker Compose、Kubernetes、Helm 备忘单 |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| AWS、Azure 与 GCP 并排比较 |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Ansible 剧本、模块、角色、自动化 |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| IaC 概念、Terraform 命令、状态管理 |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions、GitLab CI、Jenkins、管道 YAML 模式 |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL、导出器、仪表板、警报 |
## 建议的阅读路径
### **DevOps 工程师路径**
1.`infrastructure/linux_commands.md`— Linux 基础知识
2.`infrastructure/bash_and_shell_scripting.md`— Shell 脚本
3.`infrastructure/docker_and_kubernetes.md`— 容器和编排
4.`infrastructure/cicd_pipeline_config.md`— CI/CD 管道
5.`infrastructure/terraform_quick_ref.md`— 基础设施即代码
6.`infrastructure/prometheus_and_grafana.md`— 监控
### **开发者必备路径**
1.`programming/python_syntax.md`— Python 参考
2.`programming/sql_quick_ref.md`— 数据库查询
3.`programming/git_commands.md`— 版本控制
4.`programming/regular_expressions.md`— 模式匹配