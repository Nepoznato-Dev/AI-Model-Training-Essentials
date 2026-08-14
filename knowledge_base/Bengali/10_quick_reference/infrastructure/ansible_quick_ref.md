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
# উত্তরযোগ্য এবং কনফিগারেশন ব্যবস্থাপনা
Ansible হল একটি এজেন্টহীন কনফিগারেশন ম্যানেজমেন্ট এবং অটোমেশন টুল। এটি সার্ভারের সাথে সংযোগ করতে এবং YAML প্লেবুকগুলিতে সংজ্ঞায়িত কাজগুলি সম্পাদন করতে SSH (বা উইন্ডোজের জন্য WinRM) ব্যবহার করে। প্রতিটি মেশিনে এজেন্ট ইনস্টল করা প্রয়োজন এমন সরঞ্জামগুলির বিপরীতে, Ansible হল পুশ-ভিত্তিক — আপনি একটি নিয়ন্ত্রণ নোড থেকে কমান্ড চালান। এটি সার্ভার প্রভিশনিং, অ্যাপ্লিকেশন স্থাপন, কনফিগারেশন ম্যানেজমেন্ট এবং অ্যাড-হক টাস্ক এক্সিকিউশনের জন্য ব্যবহৃত হয়।
---

## মূল ধারণা
| ধারণা | বর্ণনা |
|---------|---------------|
| **জায়** | পরিচালিত হোস্টের তালিকা (INI বা YAML ফর্ম্যাট) |
| **প্লেবুক** | YAML ফাইল কার্যকর করার জন্য একটি সেট সংজ্ঞায়িত করে |
| **খেলা** | একটি প্লেবুকের মধ্যে হোস্ট এবং কাজের মধ্যে একটি ম্যাপিং |
| **টাস্ক** | একটি হোস্টে সঞ্চালনের জন্য একটি একক ক্রিয়া |
| **মডিউল** | কাজের একটি ইউনিট (যেমন,`apt`,`copy`,`service`,`template`) |
| **ভূমিকা** | কার্য, ভেরিয়েবল, ফাইল এবং হ্যান্ডলারের পুনঃব্যবহারযোগ্য সংগ্রহ |
| **পরিবর্তনশীল** | প্লেবুকগুলিতে ব্যবহৃত গতিশীল মান |
| **হ্যান্ডলার** | একটি বিজ্ঞপ্তি দ্বারা ট্রিগার করা টাস্ক (যেমন, পরিষেবা পুনরায় চালু করুন) |
| **সত্য** | হোস্ট (OS, IP, ইত্যাদি) সম্পর্কে সংগৃহীত সিস্টেম তথ্য |
---

## কমন কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `ansible all -m ping`| সমস্ত হোস্টের সাথে সংযোগ পরীক্ষা করুন |
| `ansible all -m shell -a "uptime"`| সমস্ত হোস্টে একটি শেল কমান্ড চালান |
| `ansible-playbook site.yml`| একটি প্লেবুক চালান |
| `ansible-playbook site.yml --check`| ড্রাই রান (চেক মোড) |
| `ansible-playbook site.yml --diff`| দেখান কি পরিবর্তন হবে |
| `ansible-playbook site.yml -l web`| একটি নির্দিষ্ট দলের বিরুদ্ধে চালান |
| `ansible-playbook site.yml --tags deploy`| শুধুমাত্র নির্দিষ্ট ট্যাগ দিয়ে কাজ চালান |
| `ansible-playbook site.yml --skip-tags debug`| নির্দিষ্ট ট্যাগ সহ কাজগুলি এড়িয়ে যান |
| `ansible-vault encrypt secrets.yml`| একটি ফাইল এনক্রিপ্ট করুন |
| `ansible-vault decrypt secrets.yml`| একটি ফাইল ডিক্রিপ্ট করুন |
| `ansible-vault edit secrets.yml`| একটি এনক্রিপ্ট করা ফাইল সম্পাদনা করুন |
| `ansible-galaxy install geerlingguy.nginx`| Ansible Galaxy থেকে একটি ভূমিকা ইনস্টল করুন |
| `ansible-inventory --graph`| একটি গ্রাফ হিসাবে ইনভেন্টরি প্রদর্শন করুন |
| `ansible-doc apt`| একটি মডিউলের জন্য ডকুমেন্টেশন দেখান |
---

## ইনভেন্টরি ফরম্যাট
### INI ফরম্যাট
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

### YAML ফরম্যাট
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

## প্লেবুক স্ট্রাকচার
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

## সাধারণ মডিউল
| মডিউল | উদ্দেশ্য | উদাহরণ |
|---------|---------|---------|
| **apt/yum/dnf** | প্যাকেজ ব্যবস্থাপনা | `apt: name=nginx state=present`|
| **কপি** | হোস্টে ফাইল কপি করুন | `copy: src=file.txt dest=/tmp/`|
| **টেমপ্লেট** | Jinja2 ভেরিয়েবল দিয়ে ফাইল কপি করুন | `template: src=conf.j2 dest=/etc/app.conf`|
| **ফাইল** | ফাইল এবং ডিরেক্টরি পরিচালনা করুন | `file: path=/tmp/dir state=directory`|
| **পরিষেবা** | পরিষেবাগুলি পরিচালনা করুন | `service: name=nginx state=restarted`|
| **ব্যবহারকারী/গোষ্ঠী** | ব্যবহারকারী এবং গোষ্ঠী পরিচালনা করুন | `user: name=deploy shell=/bin/bash`|
| **ক্রন** | ক্রোন কাজ পরিচালনা করুন | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **শেল / কমান্ড** | কমান্ড চালান | `shell: echo "hello" > /tmp/test`|
| **গিট** | ক্লোন সংগ্রহস্থল | `git: repo=https://... dest=/opt/app`|
| **সিস্টেমড** | সিস্টেমড ইউনিট পরিচালনা করুন | `systemd: name=myapp enabled=true`|
| **ফায়ারওয়াল্ড / ufw** | ফায়ারওয়াল নিয়ম পরিচালনা করুন | `ufw: rule=allow port=80 proto=tcp`|
| **লাইনইনফাইল** | ফাইলে লাইন পরিচালনা করুন | `lineinfile: path=/etc/hosts line="..."`|
| **ব্লকইনফাইল** | ফাইলগুলিতে পাঠ্যের ব্লকগুলি পরিচালনা করুন | কনফিগারেশনের ব্লক সন্নিবেশ/আপডেট করুন |
| **আনয়** | হোস্ট থেকে ফাইল কপি করুন | `fetch: src=/var/log/app.log dest=/local/`|
| **উরি** | ওয়েব পরিষেবার সাথে ইন্টারঅ্যাক্ট | `uri: url=https://api.example.com method=GET`|
| **ডিবাগ** | প্রিন্ট বার্তা | `debug: msg="Deployed {{ app_version }}"`|
---

## ভূমিকা গঠন
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

## টিপস এবং সমস্যা সমাধান
| টিপ | বর্ণনা |
|------|---------------|
| **চেক মোড ব্যবহার করুন** | পরিবর্তনগুলি প্রয়োগ করার আগে সর্বদা`--check --diff`|
| **ট্যাগ ব্যবহার করুন** | নির্বাচনী সম্পাদনের জন্য ট্যাগ টাস্ক |
| **গোপনের জন্য ভল্ট ব্যবহার করুন** | প্লেইন টেক্সটে পাসওয়ার্ড সংরক্ষণ করবেন না |
| **আদমশক্তি** | টাস্ক একাধিকবার চালানোর জন্য নিরাপদ হওয়া উচিত |
| **ব্যবহার করুন** | বিশেষাধিকার বৃদ্ধির জন্য`become: true`ব্যবহার করুন |
| ** সীমা সমান্তরালতা** | সমবর্তী সংযোগ নিয়ন্ত্রণ করতে`--forks`ব্যবহার করুন |
| **ভ্যাগ্রান্ট / ডকারের সাথে পরীক্ষা করুন** | উত্পাদন চালানোর আগে স্থানীয়ভাবে প্লেবুক পরীক্ষা করুন |
| **`--step` ব্যবহার করুন ** | ইন্টারেক্টিভ মোড: কার্যকর করার আগে প্রতিটি কাজ নিশ্চিত করুন |
---

## সারাংশ
উত্তরযোগ্য সার্ভার কনফিগারেশন এবং এসএসএইচ-এ কার্যকর করা YAML প্লেবুকের মাধ্যমে অ্যাপ্লিকেশন স্থাপনাকে স্বয়ংক্রিয় করে। ওয়ার্কফ্লো হল: ইনভেন্টরি সংজ্ঞায়িত করুন → প্লেবুক লিখুন →`ansible-playbook`চালান। মূল ধারণার মধ্যে রয়েছে মডিউল (কাজের একক), ভূমিকা (পুনঃব্যবহারযোগ্য সংগ্রহ), হ্যান্ডলার (ট্রিগার করা কাজ), এবং ভেরিয়েবল (গতিশীল মান)। সাধারণ মডিউলগুলি প্যাকেজ পরিচালনা, ফাইল অপারেশন, পরিষেবা নিয়ন্ত্রণ এবং ব্যবহারকারী ব্যবস্থাপনাকে কভার করে। আবেদন করার আগে সর্বদা চেক মোড ব্যবহার করুন; উত্তরীয় ভল্টে গোপনীয়তা সংরক্ষণ করুন; নিশ্চিত করুন কাজগুলো অদম্য; এবং উত্পাদন চালানোর আগে স্থানীয়ভাবে পরীক্ষা করুন।