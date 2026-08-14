# อ้างอิงด่วน
คอลเลกชันเอกสารสรุปที่มีโครงสร้างและคู่มืออ้างอิงด่วนสำหรับภาษาการเขียนโปรแกรม เครื่องมือบรรทัดคำสั่ง โครงสร้างพื้นฐาน และ DevOps — ออกแบบมาเพื่อการค้นหาที่รวดเร็วระหว่างการทำงานในแต่ละวัน
## โครงสร้าง
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

## ไฟล์ตามหมวดหมู่ย่อย
### การเขียนโปรแกรม
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [python_syntax.md](programming/python_syntax.md)| แผ่นโกงไวยากรณ์ Python |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| การอ้างอิงแบบสอบถาม SQL |
| [regular_expressions.md](programming/regular_expressions.md)| ไวยากรณ์ Regex รูปแบบทั่วไป การใช้งานเฉพาะภาษา |
| [git_commands.md](programming/git_commands.md)| คำสั่ง Git และเวิร์กโฟลว์ |
### โครงสร้างพื้นฐาน
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [linux_commands.md](infrastructure/linux_commands.md)| การอ้างอิงบรรทัดคำสั่ง Linux |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| การเขียนสคริปต์ Bash การประมวลผลข้อความ one-liners ที่มีประโยชน์ |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| เอกสารสรุปนักเทียบท่า, นักเทียบท่าเขียน, Kubernetes, Helm
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| การเปรียบเทียบ AWS กับ Azure กับ GCP แบบเคียงข้างกัน |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Playbooks, โมดูล, บทบาท, ระบบอัตโนมัติ |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| แนวคิด IaC, คำสั่ง Terraform, การจัดการสถานะ |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| การดำเนินการ GitHub, GitLab CI, Jenkins, รูปแบบ YAML ไปป์ไลน์ |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL ผู้ส่งออก แดชบอร์ด การแจ้งเตือน |
## เส้นทางการอ่านที่แนะนำ
### **เส้นทางวิศวกร DevOps**
1.`infrastructure/linux_commands.md`— พื้นฐานของ Linux
2.`infrastructure/bash_and_shell_scripting.md`— การเขียนสคริปต์เชลล์
3.`infrastructure/docker_and_kubernetes.md`— คอนเทนเนอร์และการจัดประสาน
4.`infrastructure/cicd_pipeline_config.md`— ไปป์ไลน์ CI/CD
5.`infrastructure/terraform_quick_ref.md`— โครงสร้างพื้นฐานเป็นโค้ด
6.`infrastructure/prometheus_and_grafana.md`— การตรวจสอบ
### **เส้นทางสำคัญของนักพัฒนา**
1.`programming/python_syntax.md`— การอ้างอิง Python
2.`programming/sql_quick_ref.md`— การสืบค้นฐานข้อมูล
3.`programming/git_commands.md`— การควบคุมเวอร์ชัน
4.`programming/regular_expressions.md`— การจับคู่รูปแบบ