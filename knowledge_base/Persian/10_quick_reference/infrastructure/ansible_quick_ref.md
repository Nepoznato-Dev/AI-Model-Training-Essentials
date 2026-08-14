<!--
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

-->
# Ansible و مدیریت پیکربندی
Ansible یک ابزار مدیریت پیکربندی و اتوماسیون بدون عامل است. از SSH (یا WinRM برای ویندوز) برای اتصال به سرورها و اجرای وظایف تعریف شده در کتابهای پخش YAML استفاده می کند. برخلاف ابزارهایی که نیاز به عوامل نصب شده روی هر ماشینی دارند، Ansible مبتنی بر فشار است - شما دستورات را از یک گره کنترل اجرا می کنید. این برای تامین سرور، استقرار برنامه، مدیریت پیکربندی، و اجرای تکالیف ad-hoc استفاده می شود.
---

## مفاهیم اصلی
| مفهوم | توضیحات |
|---------|-------------|
| **موجودی** | لیست میزبان های مدیریت شده (فرمت INI یا YAML) |
| **کتاب بازی** | فایل YAML مجموعه ای از وظایف را برای اجرا تعریف می کند |
| **بازی** | نقشه برداری بین میزبان ها و وظایف در یک کتاب بازی |
| **وظیفه** | یک عمل واحد برای انجام در یک میزبان |
| **ماژول** | یک واحد کار (به عنوان مثال،`apt`,`copy`,`service`,`template`) |
| **نقش** | مجموعه ای قابل استفاده مجدد از وظایف، متغیرها، فایل ها و کنترل کننده ها |
| **متغیر** | مقادیر دینامیک مورد استفاده در کتابهای بازی |
| **هندلر** | کار با یک اعلان (به عنوان مثال، راه اندازی مجدد سرویس) |
| **واقعیت** | اطلاعات سیستم جمع آوری شده در مورد هاست (OS، IP و غیره) |
---

## دستورات رایج
| فرمان | توضیحات |
|---------|-------------|
| `ansible all -m ping`| تست اتصال به همه هاست ها |
| `ansible all -m shell -a "uptime"`| یک فرمان پوسته را روی همه هاست ها اجرا کنید |
| `ansible-playbook site.yml`| اجرای کتاب بازی |
| `ansible-playbook site.yml --check`| اجرای خشک (حالت بررسی) |
| `ansible-playbook site.yml --diff`| نشان دهید که چه چیزی تغییر می کند |
| `ansible-playbook site.yml -l web`| در مقابل یک گروه خاص اجرا کنید |
| `ansible-playbook site.yml --tags deploy`| فقط وظایف با برچسب های خاص را اجرا کنید |
| `ansible-playbook site.yml --skip-tags debug`| رد شدن از وظایف با برچسب های خاص |
| `ansible-vault encrypt secrets.yml`| رمزگذاری یک فایل |
| `ansible-vault decrypt secrets.yml`| رمزگشایی یک فایل |
| `ansible-vault edit secrets.yml`| ویرایش یک فایل رمزگذاری شده |
| `ansible-galaxy install geerlingguy.nginx`| نصب نقش از Ansible Galaxy |
| `ansible-inventory --graph`| نمایش موجودی به صورت نمودار |
| `ansible-doc apt`| نمایش مستندات برای یک ماژول |
---

## فرمت های موجودی
### فرمت INI
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

### فرمت YAML
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

## ساختار کتاب راهنما
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

## ماژول های رایج
| ماژول | هدف | مثال |
|--------|---------|---------|
| **apt / yum / dnf ** | مدیریت بسته بندی | `apt: name=nginx state=present`|
| **کپی** | کپی فایل ها در هاست | `copy: src=file.txt dest=/tmp/`|
| **قالب** | کپی فایل ها با متغیرهای Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **فایل** | مدیریت فایل ها و دایرکتوری ها | `file: path=/tmp/dir state=directory`|
| **سرویس** | مدیریت خدمات | `service: name=nginx state=restarted`|
| **کاربر/گروه** | مدیریت کاربران و گروه ها | `user: name=deploy shell=/bin/bash`|
| **cron** | مدیریت cron jobs | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **پوسته / فرمان** | اجرای دستورات | `shell: echo "hello" > /tmp/test`|
| **git** | مخازن کلون | `git: repo=https://... dest=/opt/app`|
| **سیستم** | مدیریت واحدهای systemd | `systemd: name=myapp enabled=true`|
| **فایروال / ufw** | مدیریت قوانین فایروال | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | مدیریت خطوط در فایل ها | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | مدیریت بلوک های متن در فایل ها | درج/به‌روزرسانی بلوک‌های پیکربندی |
| **واکشی** | کپی فایل ها از هاست | `fetch: src=/var/log/app.log dest=/local/`|
| **وری** | تعامل با خدمات وب | `uri: url=https://api.example.com method=GET`|
| **اشکال زدایی** | چاپ پیام ها | `debug: msg="Deployed {{ app_version }}"`|
---

## ساختار نقش
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

## نکات و عیب یابی
| نکته | توضیحات |
|-----|-------------|
| **از حالت چک استفاده کنید** | همیشه قبل از اعمال تغییرات`--check --diff`|
| **استفاده از برچسب** | تگ وظایف برای اجرای انتخابی |
| **از طاق برای اسرار** | هرگز رمزهای عبور را در متن ساده ذخیره نکنید |
| **بی توانی** | وظایف باید ایمن باشند تا چندین بار اجرا شوند |
| **استفاده از تبدیل** | از`become: true`برای افزایش امتیاز استفاده کنید |
| **توازی را محدود کنید** | از`--forks`برای کنترل اتصالات همزمان |
| **تست با Vagrant / Docker** | قبل از اجرا در مرحله تولید، راهنماها را به صورت محلی تست کنید |
| **از`--step`** | حالت تعاملی: هر کار را قبل از اجرا تأیید کنید |
---

## خلاصه
Ansible پیکربندی سرور و استقرار برنامه‌ها را از طریق کتاب‌های پخش YAML که از طریق SSH اجرا می‌شوند، خودکار می‌کند. گردش کار عبارت است از: تعریف موجودی → نوشتن کتاب های بازی → اجرای `ansible-playbook`. مفاهیم کلیدی شامل ماژول ها (واحدهای کار)، نقش ها (مجموعه های قابل استفاده مجدد)، کنترل کننده ها (وظایف راه اندازی شده) و متغیرها (مقادیر پویا) است. ماژول های رایج مدیریت بسته، عملیات فایل، کنترل سرویس و مدیریت کاربر را پوشش می دهند. همیشه قبل از اعمال از حالت بررسی استفاده کنید. ذخیره اسرار در Ansible Vault. اطمینان حاصل شود که وظایف ناتوان هستند. و قبل از شروع تولید به صورت محلی تست کنید.