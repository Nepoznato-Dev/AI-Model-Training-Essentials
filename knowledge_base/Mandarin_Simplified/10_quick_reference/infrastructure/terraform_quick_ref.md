<!--
---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
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
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Terraform 和基础设施即代码
Terraform 是使用最广泛的基础设施即代码 (IaC) 工具 - 它允许您在声明性配置文件中定义云基础设施（服务器、数据库、网络、权限），这些文件可以进行版本控制、审查、测试和自动化。您无需单击云控制台，而是编写描述基础设施所需状态的代码，然后 Terraform 确定要进行哪些更改。
---

## 核心概念
|概念 |描述 |
|---------|-------------|
| **提供商** |管理特定云平台（AWS、Azure、GCP 等）的插件 |
| **资源** |基础设施对象（服务器、数据库、网络）|
| **状态** | Terraform 对现有基础设施的记录；存储在状态文件中|
| **计划** |预览 Terraform 将做出哪些改变 |
| **申请** |执行计划；创建/更新/销毁基础设施|
| **模块** |可重复使用的资源集合|
| **变量** |配置的输入参数 |
| **输出** |从模块或配置导出的值 |
| **数据来源** |从现有基础设施中读取信息 |
---

## 基本工作流程
|步骤|命令 |描述 |
|------|---------|-------------|
| **1.写入配置** |创建`.tf`文件 |定义提供者、资源、变量 |
| **2.初始化** | `terraform init`|下载提供商；设置后台 |
| **3.格式** | `terraform fmt`|标准化格式 |
| **4.验证** | `terraform validate`|检查语法和配置 |
| **5.计划** | `terraform plan`|预览更改（试运行）|
| **6。申请** | `terraform apply`|创建或更新基础设施 |
| **7.摧毁** | `terraform destroy`|拆除所有托管基础设施|
---

## 常用命令
|命令 |描述 |
|---------|-------------|
| `terraform init`|初始化工作目录；下载提供程序和模块|
| `terraform plan`|显示将进行哪些更改 |
| `terraform apply`|应用更改；添加`-auto-approve`跳过确认 |
| `terraform destroy`|销毁所有托管资源 |
| `terraform fmt`|将配置文件格式化为标准样式 |
| `terraform validate`|验证配置语法 |
| `terraform output`|显示输出值 |
| `terraform state list`|列出状态 | 的所有资源
| `terraform state show <resource>`|显示特定资源的详细信息 |
| `terraform import <resource> <id>`|将现有基础设施导入州政府 |
| `terraform taint <resource>`|在下次申请时标记供娱乐的资源 |
| `terraform refresh`|更新状态以匹配真实的基础设施 |
| `terraform graph`|生成可视化依赖图（DOT 格式） |
| `terraform console`|用于测试表达式的交互式控制台 |
---

## 状态管理
|最佳实践|描述 |
|--------------|-------------|
| **远程状态** |将状态存储在 S3、GCS、Azure Blob 或 Terraform Cloud 中 — 绝不是在本地 |
| **状态锁定** |使用 DynamoDB（S3 后端）或本机锁定来防止并发修改 |
| **状态加密** |为状态文件启用静态加密（它们包含敏感数据）|
| **状态分离** |为不同的环境或团队使用单独的状态文件 |
| **状态备份** |远程后端自动版本状态；保持启用 |
| **切勿手动编辑状态** |使用`terraform state mv`、`rm`、`import`代替 |
---

## 模块结构
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## 变量类型
|类型 |示例|使用案例|
|------|---------|----------|
| **字符串** | `variable "region" { type = string }`|单个文本值 |
| **数量** | `variable "count" { type = number }`|数值 |
| **布尔** | `variable "enable" { type = bool }`|真/假标志 |
| **列表** | `variable "zones" { type = list(string) }`|已订购收藏|
| **地图** | `variable "tags" { type = map(string) }`|键值对 |
| **对象** | `variable "config" { type = object({...}) }`|结构化配置|
---

## 常见模式
|图案|描述 |
|---------|-------------|
| **计数** | `count = 3`创建资源的多个实例 |
| **对于每个** | `for_each = var.items`迭代映射或集合 |
| **动态块** |生成重复的嵌套块（例如入口规则）|
| **当地价值观** | `locals { ... }`用于计算值并减少重复 |
| **数据来源** |读取现有基础设施（例如，查找现有 VPC）|
| **供应商** |创建后在资源上运行脚本（谨慎使用）|
| **工作空间** |同一配置中不同环境的单独状态 |
---

## 故障排除
|问题 |解决方案 |
|---------|----------|
| **状态漂移** |运行`terraform plan`查看差异； `terraform apply`调和|
| **锁定状态** |检查谁拥有锁；如果安全，请使用`terraform force-unlock`|
| **提供商错误** |检查凭据；更新提供商版本；检查 API 限制 |
| **导入冲突** |资源已处于状态；首先使用`terraform state rm` |
| **循环依赖** |重组资源；小心使用`depends_on` |
| **大州** |分成模块；使用`-target`进行部分操作 |
---

＃＃ 概括
Terraform 通过声明性配置文件管理基础设施。工作流程为：编写配置→初始化→计划→应用。状态跟踪存在的内容并且必须通过锁定远程存储。模块可实现重用。变量参数化配置。关键原则是： 将基础设施视为代码（版本控制；审查；测试）；切勿手动编辑状态；申请前做好计划；使用带有锁定的远程状态；以及具有可维护性模块的结构配置。