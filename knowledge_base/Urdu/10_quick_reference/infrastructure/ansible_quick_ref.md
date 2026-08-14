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
# جوابدہ اور کنفیگریشن مینجمنٹ
جوابدہ ایک ایجنٹ لیس کنفیگریشن مینجمنٹ اور آٹومیشن ٹول ہے۔ یہ سرورز سے منسلک ہونے اور YAML پلے بکس میں بیان کردہ کاموں کو انجام دینے کے لیے SSH (یا WinRM for Windows) کا استعمال کرتا ہے۔ ان ٹولز کے برعکس جن کے لیے ہر مشین پر ایجنٹوں کو انسٹال کرنے کی ضرورت ہوتی ہے، Ansible پش بیسڈ ہے — آپ کنٹرول نوڈ سے کمانڈ چلاتے ہیں۔ یہ سرور کی فراہمی، ایپلیکیشن کی تعیناتی، کنفیگریشن مینجمنٹ، اور ایڈہاک ٹاسک ایگزیکیوشن کے لیے استعمال ہوتا ہے۔
---

## بنیادی تصورات
| تصور | تفصیل |
|---------|---------------|
| **انوینٹری** | منظم میزبانوں کی فہرست (INI یا YAML فارمیٹ) |
| **پلے بک** | YAML فائل کو انجام دینے کے لئے کاموں کے ایک سیٹ کی وضاحت |
| **کھیلیں** | پلے بک کے اندر میزبانوں اور کاموں کے درمیان میپنگ |
| **ٹاسک** | میزبان پر انجام دینے کے لیے ایک ہی کارروائی |
| **ماڈیول** | کام کی اکائی (مثلاً`apt`,`copy`,`service`,`template`) |
| **کردار** | کاموں، متغیرات، فائلوں اور ہینڈلرز کا دوبارہ قابل استعمال مجموعہ |
| **متغیر** | پلے بکس میں استعمال ہونے والی متحرک اقدار |
| **ہینڈلر** | ایک اطلاع سے شروع ہونے والا ٹاسک (جیسے، سروس دوبارہ شروع کریں) |
| **حقیقت** | میزبانوں (OS، IP، وغیرہ) کے بارے میں جمع کردہ سسٹم کی معلومات |
---

## کامن کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `ansible all -m ping`| تمام میزبانوں سے رابطے کی جانچ کریں |
| `ansible all -m shell -a "uptime"`| تمام میزبانوں پر شیل کمانڈ چلائیں |
| `ansible-playbook site.yml`| پلے بک پر عمل کریں |
| `ansible-playbook site.yml --check`| ڈرائی رن (چیک موڈ) |
| `ansible-playbook site.yml --diff`| دکھائیں کیا تبدیلی آئے گی |
| `ansible-playbook site.yml -l web`| ایک مخصوص گروپ کے خلاف چلائیں |
| `ansible-playbook site.yml --tags deploy`| مخصوص ٹیگز کے ساتھ صرف کام چلائیں |
| `ansible-playbook site.yml --skip-tags debug`| مخصوص ٹیگز کے ساتھ کاموں کو چھوڑیں |
| `ansible-vault encrypt secrets.yml`| ایک فائل کو خفیہ کریں |
| `ansible-vault decrypt secrets.yml`| فائل کو ڈکرپٹ کریں |
| `ansible-vault edit secrets.yml`| ایک خفیہ کردہ فائل میں ترمیم کریں |
| `ansible-galaxy install geerlingguy.nginx`| Ansible Galaxy | سے ایک کردار انسٹال کریں۔
| `ansible-inventory --graph`| انوینٹری کو بطور گراف دکھائیں |
| `ansible-doc apt`| ماڈیول کے لیے دستاویزات دکھائیں |
---

## انوینٹری فارمیٹس
### INI فارمیٹ
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

### YAML فارمیٹ
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

## پلے بک کا ڈھانچہ
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

## عام ماڈیولز
| ماڈیول | مقصد | مثال |
|---------|---------|---------|
| **apt/yum/dnf** | پیکیج مینجمنٹ | `apt: name=nginx state=present`|
| **کاپی** | فائلوں کو میزبانوں میں کاپی کریں | `copy: src=file.txt dest=/tmp/`|
| **ٹیمپلیٹ** | Jinja2 متغیر کے ساتھ فائلوں کو کاپی کریں | `template: src=conf.j2 dest=/etc/app.conf`|
| **فائل** | فائلوں اور ڈائریکٹریوں کا نظم کریں | `file: path=/tmp/dir state=directory`|
| **خدمت** | خدمات کا نظم کریں | `service: name=nginx state=restarted`|
| **صارف / گروپ** | صارفین اور گروپس کا نظم کریں | `user: name=deploy shell=/bin/bash`|
| **کرون** | کرون جابز کا نظم کریں | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **شیل / کمانڈ** | کمانڈز چلائیں | `shell: echo "hello" > /tmp/test`|
| **گٹ** | کلون ریپوزٹریز | `git: repo=https://... dest=/opt/app`|
| **سسٹم ڈی** | سسٹمڈ یونٹس کا نظم کریں | `systemd: name=myapp enabled=true`|
| **فائر والڈ / ufw** | فائر وال کے قواعد کا نظم کریں | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | فائلوں میں لائنوں کا نظم کریں | `lineinfile: path=/etc/hosts line="..."`|
| **بلاک ان فائل** | فائلوں میں متن کے بلاکس کا نظم کریں | کنفیگریشن کے بلاکس داخل/اپ ڈیٹ کریں |
| **لائیں** | میزبانوں سے فائلیں کاپی کریں | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | ویب سروسز کے ساتھ بات چیت | `uri: url=https://api.example.com method=GET`|
| **ڈیبگ** | پیغامات پرنٹ کریں | `debug: msg="Deployed {{ app_version }}"`|
---

## کردار کا ڈھانچہ
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

## ٹپس اور ٹربل شوٹنگ
| ٹپ | تفصیل |
|------|---------------|
| **چیک موڈ استعمال کریں** | تبدیلیاں لاگو کرنے سے پہلے ہمیشہ`--check --diff`|
| **ٹیگز استعمال کریں** | انتخابی عمل کے لیے کاموں کو ٹیگ کریں |
| **راز کے لیے والٹ کا استعمال کریں** | کبھی بھی سادہ متن میں پاس ورڈ ذخیرہ نہ کریں |
| **آدمی** | کاموں کو کئی بار چلانے کے لیے محفوظ ہونا چاہیے |
| **بن کا استعمال کریں** | استحقاق میں اضافے کے لیے`become: true`استعمال کریں۔
| **حد متوازی** | کنکرنٹ کنکشنز کو کنٹرول کرنے کے لیے`--forks`استعمال کریں۔
| ** Vagrant / Docker کے ساتھ ٹیسٹ ** | پروڈکشن پر چلنے سے پہلے مقامی طور پر پلے بکس کی جانچ کریں۔
| **`--step` استعمال کریں ** | انٹرایکٹو موڈ: عملدرآمد سے پہلے ہر کام کی تصدیق کریں |
---

## خلاصہ
جواب دہ SSH پر عمل درآمد YAML پلے بکس کے ذریعے سرور کی ترتیب اور ایپلیکیشن کی تعیناتی کو خودکار بناتا ہے۔ ورک فلو یہ ہے: انوینٹری کی وضاحت کریں → پلے بکس لکھیں →`ansible-playbook`چلائیں۔ کلیدی تصورات میں ماڈیولز (کام کی اکائیاں)، کردار (دوبارہ استعمال کے قابل مجموعہ)، ہینڈلرز (متحرک کام) اور متغیرات (متحرک اقدار) شامل ہیں۔ عام ماڈیول پیکیج مینجمنٹ، فائل آپریشنز، سروس کنٹرول، اور یوزر مینجمنٹ کا احاطہ کرتے ہیں۔ درخواست دینے سے پہلے ہمیشہ چیک موڈ استعمال کریں۔ جوابی والٹ میں راز ذخیرہ کریں؛ اس بات کو یقینی بنائیں کہ کام بے اختیار ہیں؛ اور پیداوار پر چلنے سے پہلے مقامی طور پر جانچ کریں۔