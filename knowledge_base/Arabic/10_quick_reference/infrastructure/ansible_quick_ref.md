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
# إدارة Ansible والتكوين
Ansible هي أداة لإدارة التكوين والأتمتة بدون وكيل. ويستخدم SSH (أو WinRM لنظام التشغيل Windows) للاتصال بالخوادم وتنفيذ المهام المحددة في كتب تشغيل YAML. على عكس الأدوات التي تتطلب تثبيت الوكلاء على كل جهاز، يعتمد Ansible على الدفع - حيث تقوم بتشغيل الأوامر من عقدة التحكم. يتم استخدامه لتوفير الخادم ونشر التطبيقات وإدارة التكوين وتنفيذ المهام المخصصة.
---

## المفاهيم الأساسية
| المفهوم | الوصف |
|---------|------------|
| **المخزون** | قائمة المضيفين المدارين (تنسيق INI أو YAML) |
| ** كتاب اللعب ** | YAML يحدد مجموعة من المهام المطلوب تنفيذها |
| **العب** | تعيين بين المضيفين والمهام داخل قواعد اللعبة |
| **المهمة** | إجراء واحد يتم تنفيذه على المضيف |
| **الوحدة** | وحدة عمل (على سبيل المثال،`apt`،`copy`،`service`،`template`) |
| **الدور** | مجموعة قابلة لإعادة الاستخدام من المهام والمتغيرات والملفات والمعالجات |
| **متغير** | القيم الديناميكية المستخدمة في كتب اللعب |
| **المعالج** | المهمة التي يتم تشغيلها بواسطة إشعار (على سبيل المثال، إعادة تشغيل الخدمة) |
| **حقيقة** | معلومات النظام التي تم جمعها حول المضيفين (نظام التشغيل، IP، وما إلى ذلك) |
---

## الأوامر المشتركة
| الأمر | الوصف |
|---------|------------|
| `ansible all -m ping`| اختبار الاتصال بجميع المضيفين |
| `ansible all -m shell -a "uptime"`| قم بتشغيل أمر Shell على كافة الأجهزة المضيفة |
| `ansible-playbook site.yml`| تنفيذ قواعد اللعبة التي تمارسها |
| `ansible-playbook site.yml --check`| التشغيل الجاف (وضع الفحص) |
| `ansible-playbook site.yml --diff`| أظهر ما سيتغير |
| `ansible-playbook site.yml -l web`| تشغيل ضد مجموعة محددة |
| `ansible-playbook site.yml --tags deploy`| قم بتشغيل المهام ذات العلامات المحددة فقط |
| `ansible-playbook site.yml --skip-tags debug`| تخطي المهام بعلامات محددة |
| `ansible-vault encrypt secrets.yml`| تشفير ملف |
| `ansible-vault decrypt secrets.yml`| فك تشفير ملف |
| `ansible-vault edit secrets.yml`| تحرير ملف مشفر |
| `ansible-galaxy install geerlingguy.nginx`| تثبيت دور من Ansible Galaxy |
| `ansible-inventory --graph`| عرض المخزون كرسم بياني |
| `ansible-doc apt`| عرض وثائق الوحدة النمطية |
---

## تنسيقات المخزون
### تنسيق إيني
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

### تنسيق YAML
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

## هيكل كتاب اللعب
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

## الوحدات المشتركة
| الوحدة | الغرض | مثال |
|--------|---------|---------|
| **مناسبة/يم/dnf** | إدارة الحزم | `apt: name=nginx state=present`|
| **نسخ** | نسخ الملفات إلى المضيفين | `copy: src=file.txt dest=/tmp/`|
| **قالب** | نسخ الملفات بمتغيرات Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **ملف** | إدارة الملفات والدلائل | `file: path=/tmp/dir state=directory`|
| **الخدمة** | إدارة الخدمات | `service: name=nginx state=restarted`|
| **مستخدم/مجموعة** | إدارة المستخدمين والمجموعات | `user: name=deploy shell=/bin/bash`|
| **كرون** | إدارة وظائف كرون | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **الصدفة/الأمر** | تشغيل الأوامر | `shell: echo "hello" > /tmp/test`|
| **جيت** | مستودعات النسخ | `git: repo=https://... dest=/opt/app`|
| **سيستمد** | إدارة وحدات النظام | `systemd: name=myapp enabled=true`|
| ** جدار الحماية / ufw ** | إدارة قواعد جدار الحماية | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | إدارة الخطوط في الملفات | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | إدارة كتل النص في الملفات | إدراج/تحديث كتل التكوين |
| **جلب** | نسخ الملفات من المضيفين | `fetch: src=/var/log/app.log dest=/local/`|
| **يوري** | التفاعل مع خدمات الويب | `uri: url=https://api.example.com method=GET`|
| ** تصحيح ** | طباعة الرسائل | `debug: msg="Deployed {{ app_version }}"`|
---

## هيكل الدور
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

## النصائح واستكشاف الأخطاء وإصلاحها
| نصيحة | الوصف |
|-----|------------|
| ** استخدم وضع التحقق ** | قم دائمًا بـ`--check --diff`قبل تطبيق التغييرات |
| **استخدام العلامات** | مهام العلامة للتنفيذ الانتقائي |
| **استخدم قبو الأسرار** | لا تقم أبدًا بتخزين كلمات المرور في نص عادي |
| **العجز** | يجب أن تكون المهام آمنة للتشغيل عدة مرات |
| **استخدام يصبح** | استخدم`become: true`لتصعيد الامتيازات |
| **الحد من التوازي** | استخدم`--forks`للتحكم في الاتصالات المتزامنة |
| **اختبار مع Vagrant / Docker** | اختبر قواعد اللعبة محليًا قبل تشغيلها على الإنتاج |
| **استخدم`--step`** | الوضع التفاعلي: تأكيد كل مهمة قبل التنفيذ |
---

## ملخص
يقوم Ansible بأتمتة تكوين الخادم ونشر التطبيق من خلال قواعد تشغيل YAML التي يتم تنفيذها عبر SSH. سير العمل هو: تحديد المخزون ← كتابة أدلة التشغيل ← تشغيل`ansible-playbook`. تتضمن المفاهيم الأساسية الوحدات النمطية (وحدات العمل)، والأدوار (المجموعات القابلة لإعادة الاستخدام)، والمعالجات (المهام التي يتم تشغيلها)، والمتغيرات (القيم الديناميكية). تغطي الوحدات الشائعة إدارة الحزم وعمليات الملفات والتحكم في الخدمة وإدارة المستخدم. استخدم دائمًا وضع التحقق قبل التقديم؛ تخزين الأسرار في Ansible Vault؛ التأكد من أن المهام غير فعالة؛ واختباره محليًا قبل تشغيله على الإنتاج.