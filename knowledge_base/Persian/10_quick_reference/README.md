# مرجع سریع
مجموعه ای ساختاریافته از برگه های تقلب و راهنماهای مرجع سریع برای زبان های برنامه نویسی، ابزارهای خط فرمان، زیرساخت ها و DevOps – طراحی شده برای جستجوی سریع در طول کار روزانه.
## ساختار
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

## فایل ها بر اساس زیر شاخه
### برنامه نویسی
| فایل | توضیحات |
|------|-------------|
| [python_syntax.md](programming/python_syntax.md)| برگه تقلب دستور زبان پایتون |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| مرجع پرس و جوی SQL |
| [regular_expressions.md](programming/regular_expressions.md)| نحو Regex، الگوهای رایج، استفاده خاص زبان |
| [git_commands.md](programming/git_commands.md)| دستورات Git و گردش کار |
### زیرساخت
| فایل | توضیحات |
|------|-------------|
| [linux_commands.md](infrastructure/linux_commands.md)| مرجع خط فرمان لینوکس |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| برنامه نویسی Bash، پردازش متن، تک خط های مفید |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker, Docker Compose, Kubernetes, Helm Cheat Sheet |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| مقایسه کنار هم AWS در مقابل Azure و GCP |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| کتاب های بازی Ansible، ماژول ها، نقش ها، اتوماسیون |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| مفاهیم IaC، دستورات Terraform، مدیریت حالت |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions، GitLab CI، Jenkins، خط لوله الگوهای YAML |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL، صادرکنندگان، داشبوردها، هشدار |
## مسیرهای خواندن پیشنهادی
### **مسیر مهندس DevOps**
1.`infrastructure/linux_commands.md`- اصول لینوکس
2.`infrastructure/bash_and_shell_scripting.md`- برنامه نویسی پوسته
3.`infrastructure/docker_and_kubernetes.md`- کانتینرها و ارکستراسیون
4.`infrastructure/cicd_pipeline_config.md`- خطوط لوله CI/CD
5.`infrastructure/terraform_quick_ref.md`- زیرساخت به عنوان کد
6.`infrastructure/prometheus_and_grafana.md`- نظارت
### **مسیر ضروری توسعه دهندگان**
1.`programming/python_syntax.md`- مرجع پایتون
2.`programming/sql_quick_ref.md`- پرس و جوهای پایگاه داده
3.`programming/git_commands.md`- کنترل نسخه
4.`programming/regular_expressions.md`- تطبیق الگو