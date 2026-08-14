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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Ansible และการจัดการการกำหนดค่า
Ansible คือเครื่องมือการจัดการการกำหนดค่าและการทำงานอัตโนมัติแบบไม่ใช้เอเจนต์ ใช้ SSH (หรือ WinRM สำหรับ Windows) เพื่อเชื่อมต่อกับเซิร์ฟเวอร์และดำเนินงานที่กำหนดไว้ใน Playbooks ของ YAML ไม่เหมือนกับเครื่องมือที่ต้องติดตั้งเอเจนต์บนทุกเครื่อง Ansible เป็นแบบพุช — คุณรันคำสั่งจากโหนดควบคุม ใช้สำหรับการจัดเตรียมเซิร์ฟเวอร์ การปรับใช้แอปพลิเคชัน การจัดการการกำหนดค่า และการดำเนินงานเฉพาะกิจ
---

## แนวคิดหลัก
| แนวคิด | คำอธิบาย |
|---------|-------------|
| **สินค้าคงคลัง** | รายชื่อโฮสต์ที่ได้รับการจัดการ (รูปแบบ INI หรือ YAML) |
| **เพลย์บุ๊ก** | ไฟล์ YAML ที่กำหนดชุดของงานที่จะดำเนินการ |
| **เล่น** | การแมประหว่างโฮสต์และงานภายใน Playbook |
| **งาน** | การดำเนินการเดียวที่จะดำเนินการบนโฮสต์ |
| **โมดูล** | หน่วยงาน (เช่น`apt`,`copy`,`service`,`template`) |
| **บทบาท** | การรวบรวมงาน ตัวแปร ไฟล์ และตัวจัดการที่นำมาใช้ซ้ำได้
| **ตัวแปร** | ค่าไดนามิกที่ใช้ใน Playbooks |
| **ตัวจัดการ** | งานที่ทริกเกอร์โดยการแจ้งเตือน (เช่น เริ่มบริการใหม่) |
| **ข้อเท็จจริง** | ข้อมูลระบบที่รวบรวมเกี่ยวกับโฮสต์ (OS, IP ฯลฯ) |
---

## คำสั่งทั่วไป
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `ansible all -m ping`| ทดสอบการเชื่อมต่อกับโฮสต์ทั้งหมด |
| `ansible all -m shell -a "uptime"`| รันคำสั่งเชลล์บนโฮสต์ทั้งหมด |
| `ansible-playbook site.yml`| ดำเนินการ Playbook |
| `ansible-playbook site.yml --check`| ดรายรัน (โหมดตรวจสอบ) |
| `ansible-playbook site.yml --diff`| แสดงสิ่งที่จะเปลี่ยนแปลง |
| `ansible-playbook site.yml -l web`| วิ่งแข่งกับกลุ่มเฉพาะ |
| `ansible-playbook site.yml --tags deploy`| รันเฉพาะงานที่มีแท็กเฉพาะ |
| `ansible-playbook site.yml --skip-tags debug`| ข้ามงานด้วยแท็กเฉพาะ |
| `ansible-vault encrypt secrets.yml`| เข้ารหัสไฟล์ |
| `ansible-vault decrypt secrets.yml`| ถอดรหัสไฟล์ |
| `ansible-vault edit secrets.yml`| แก้ไขไฟล์ที่เข้ารหัส |
| `ansible-galaxy install geerlingguy.nginx`| ติดตั้งบทบาทจาก Ansible Galaxy |
| `ansible-inventory --graph`| แสดงสินค้าคงคลังเป็นกราฟ |
| `ansible-doc apt`| แสดงเอกสารสำหรับโมดูล |
---

## รูปแบบสินค้าคงคลัง
### รูปแบบ INI
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

### รูปแบบ YAML
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

## โครงสร้างเพลย์บุ๊ก
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

## โมดูลทั่วไป
| โมดูล | วัตถุประสงค์ | ตัวอย่าง |
|--------|---------|---------|
| **ฉลาด / ยำ / dnf** | การจัดการแพ็คเกจ | `apt: name=nginx state=present`|
| **สำเนา** | คัดลอกไฟล์ไปยังโฮสต์ | `copy: src=file.txt dest=/tmp/`|
| **แม่แบบ** | คัดลอกไฟล์ด้วยตัวแปร Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **ไฟล์** | จัดการไฟล์และไดเร็กทอรี | `file: path=/tmp/dir state=directory`|
| **บริการ** | จัดการบริการ | `service: name=nginx state=restarted`|
| **ผู้ใช้ / กลุ่ม** | จัดการผู้ใช้และกลุ่ม | `user: name=deploy shell=/bin/bash`|
| **ครอน** | จัดการงาน cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **เชลล์ / คำสั่ง** | เรียกใช้คำสั่ง | `shell: echo "hello" > /tmp/test`|
| **คอมไพล์** | ที่เก็บโคลน | `git: repo=https://... dest=/opt/app`|
| **systemd** | จัดการหน่วย systemd | `systemd: name=myapp enabled=true`|
| **ไฟร์วอลล์ / ufw** | จัดการกฎไฟร์วอลล์ | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | จัดการบรรทัดในไฟล์ | `lineinfile: path=/etc/hosts line="..."`|
| **ไฟล์บล็อคอิน** | จัดการบล็อกข้อความในไฟล์ | แทรก/อัพเดตบล็อคการกำหนดค่า |
| **ดึง** | คัดลอกไฟล์จากโฮสต์ | `fetch: src=/var/log/app.log dest=/local/`|
| **ยูริ** | โต้ตอบกับบริการเว็บ | `uri: url=https://api.example.com method=GET`|
| **แก้ไขข้อบกพร่อง** | พิมพ์ข้อความ | `debug: msg="Deployed {{ app_version }}"`|
---

## โครงสร้างบทบาท
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

## เคล็ดลับและการแก้ไขปัญหา
| เคล็ดลับ | คำอธิบาย |
|-----|-------------|
| **ใช้โหมดตรวจสอบ** |`--check --diff`ทุกครั้งก่อนที่จะใช้การเปลี่ยนแปลง |
| **ใช้แท็ก** | แท็กงานสำหรับการดำเนินการแบบเลือก |
| **ใช้ห้องนิรภัยเพื่อความลับ** | อย่าเก็บรหัสผ่านเป็นข้อความธรรมดา |
| **ความเป็นอมตะ** | งานควรจะปลอดภัยในการทำงานหลายครั้ง |
| **ใช้เป็น** | ใช้`become: true`เพื่อยกระดับสิทธิ์ |
| **จำกัดความเท่าเทียม** | ใช้`--forks`เพื่อควบคุมการเชื่อมต่อพร้อมกัน |
| **ทดสอบกับ Vagrant / Docker** | ทดสอบ Playbooks ในเครื่องก่อนใช้งานจริง |
| **ใช้`--step`** | โหมดโต้ตอบ: ยืนยันแต่ละงานก่อนดำเนินการ |
---

## สรุป
Ansible ทำให้การกำหนดค่าเซิร์ฟเวอร์และการปรับใช้แอปพลิเคชันเป็นอัตโนมัติผ่าน Playbooks YAML ที่ดำเนินการผ่าน SSH ขั้นตอนการทำงานคือ: กำหนดสินค้าคงคลัง → เขียน playbooks → เรียกใช้`ansible-playbook`แนวคิดหลักประกอบด้วยโมดูล (หน่วยของงาน) บทบาท (คอลเลกชันที่ใช้ซ้ำได้) ตัวจัดการ (งานที่ทริกเกอร์) และตัวแปร (ค่าไดนามิก) โมดูลทั่วไปครอบคลุมถึงการจัดการแพ็คเกจ การทำงานของไฟล์ การควบคุมบริการ และการจัดการผู้ใช้ ใช้โหมดตรวจสอบก่อนสมัครเสมอ เก็บความลับใน Ansible Vault; ตรวจสอบให้แน่ใจว่างานต่างๆ นั้นไร้อำนาจ; และทดสอบในเครื่องก่อนดำเนินการใช้งานจริง