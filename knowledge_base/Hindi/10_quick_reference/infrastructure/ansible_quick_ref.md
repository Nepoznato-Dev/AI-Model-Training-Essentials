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
# Ansible और कॉन्फ़िगरेशन प्रबंधन
Ansible एक एजेंट रहित कॉन्फ़िगरेशन प्रबंधन और स्वचालन उपकरण है। यह सर्वर से कनेक्ट करने और YAML प्लेबुक में परिभाषित कार्यों को निष्पादित करने के लिए SSH (या Windows के लिए WinRM) का उपयोग करता है। उन उपकरणों के विपरीत, जिनके लिए प्रत्येक मशीन पर एजेंट स्थापित करने की आवश्यकता होती है, Ansible पुश-आधारित है - आप एक नियंत्रण नोड से कमांड चलाते हैं। इसका उपयोग सर्वर प्रोविजनिंग, एप्लिकेशन परिनियोजन, कॉन्फ़िगरेशन प्रबंधन और तदर्थ कार्य निष्पादन के लिए किया जाता है।
---

## मूल अवधारणाएँ
| संकल्पना | विवरण |
|---------|-----------------|
| **इन्वेंटरी** | प्रबंधित होस्ट की सूची (INI या YAML प्रारूप) |
| **प्लेबुक** | निष्पादित करने के लिए कार्यों के एक सेट को परिभाषित करने वाली YAML फ़ाइल |
| **खेलें** | प्लेबुक के भीतर मेजबानों और कार्यों के बीच मानचित्रण |
| **कार्य** | होस्ट पर निष्पादित करने के लिए एक एकल क्रिया |
| **मॉड्यूल** | कार्य की एक इकाई (जैसे,`apt`,`copy`,`service`,`template`) |
| **भूमिका** | कार्यों, वेरिएबल्स, फ़ाइलों और हैंडलर का पुन: प्रयोज्य संग्रह |
| **परिवर्तनीय** | प्लेबुक में प्रयुक्त गतिशील मान |
| **हैंडलर** | कार्य एक अधिसूचना द्वारा ट्रिगर किया गया (उदाहरण के लिए, सेवा पुनरारंभ करें) |
| **तथ्य** | होस्ट (ओएस, आईपी, आदि) के बारे में सिस्टम जानकारी एकत्रित की गई |
---

## सामान्य आदेश
| आदेश | विवरण |
|---------|-----------------|
| `ansible all -m ping`| सभी होस्ट से कनेक्टिविटी का परीक्षण करें |
| `ansible all -m shell -a "uptime"`| सभी होस्ट पर शेल कमांड चलाएँ |
| `ansible-playbook site.yml`| प्लेबुक निष्पादित करें |
| `ansible-playbook site.yml --check`| ड्राई रन (चेक मोड) |
| `ansible-playbook site.yml --diff`| दिखाओ क्या बदलेगा |
| `ansible-playbook site.yml -l web`| एक विशिष्ट समूह के विरुद्ध चलाएँ |
| `ansible-playbook site.yml --tags deploy`| केवल विशिष्ट टैग वाले कार्य चलाएँ |
| `ansible-playbook site.yml --skip-tags debug`| विशिष्ट टैग वाले कार्यों को छोड़ें |
| `ansible-vault encrypt secrets.yml`| किसी फ़ाइल को एन्क्रिप्ट करें |
| `ansible-vault decrypt secrets.yml`| किसी फ़ाइल को डिक्रिप्ट करें |
| `ansible-vault edit secrets.yml`| एक एन्क्रिप्टेड फ़ाइल संपादित करें |
| `ansible-galaxy install geerlingguy.nginx`| अन्सिबल गैलेक्सी से एक भूमिका स्थापित करें |
| `ansible-inventory --graph`| इन्वेंट्री को ग्राफ़ के रूप में प्रदर्शित करें |
| `ansible-doc apt`| मॉड्यूल के लिए दस्तावेज़ दिखाएं |
---

## इन्वेंटरी प्रारूप
### आईएनआई प्रारूप
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

### YAML प्रारूप
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

## प्लेबुक संरचना
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

## सामान्य मॉड्यूल
| मॉड्यूल | उद्देश्य | उदाहरण |
|--------|------|------|
| **उपयुक्त/यम/डीएनएफ** | पैकेज प्रबंधन | `apt: name=nginx state=present`|
| **कॉपी** | होस्ट में फ़ाइलें कॉपी करें | `copy: src=file.txt dest=/tmp/`|
| **टेम्पलेट** | Jinja2 वेरिएबल के साथ फ़ाइलें कॉपी करें | `template: src=conf.j2 dest=/etc/app.conf`|
| **फ़ाइल** | फ़ाइलें और निर्देशिकाएँ प्रबंधित करें | `file: path=/tmp/dir state=directory`|
| **सेवा** | सेवाएँ प्रबंधित करें | `service: name=nginx state=restarted`|
| **उपयोगकर्ता/समूह** | उपयोगकर्ताओं और समूहों को प्रबंधित करें | `user: name=deploy shell=/bin/bash`|
| **क्रोन** | क्रॉन जॉब्स प्रबंधित करें | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **शेल/कमांड** | आदेश चलाएँ | `shell: echo "hello" > /tmp/test`|
| **गिट** | क्लोन रिपॉजिटरी | `git: repo=https://... dest=/opt/app`|
| **सिस्टमडी** | सिस्टमडी इकाइयों को प्रबंधित करें | `systemd: name=myapp enabled=true`|
| **फ़ायरवॉलड/यूएफडब्ल्यू** | फ़ायरवॉल नियम प्रबंधित करें | `ufw: rule=allow port=80 proto=tcp`|
| **लाइनइनफाइल** | फ़ाइलों में पंक्तियाँ प्रबंधित करें | `lineinfile: path=/etc/hosts line="..."`|
| **ब्लॉकइनफ़ाइल** | फ़ाइलों में पाठ के ब्लॉक प्रबंधित करें | कॉन्फ़िगरेशन के ब्लॉक डालें/अपडेट करें |
| **लाओ** | होस्ट से फ़ाइलें कॉपी करें | `fetch: src=/var/log/app.log dest=/local/`|
| **उरी** | वेब सेवाओं के साथ इंटरैक्ट करें | `uri: url=https://api.example.com method=GET`|
| **डीबग** | संदेश प्रिंट करें | `debug: msg="Deployed {{ app_version }}"`|
---

## भूमिका संरचना
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

## युक्तियाँ और समस्या निवारण
| युक्ति | विवरण |
|----|-----|
| **चेक मोड का उपयोग करें** | परिवर्तन लागू करने से पहले हमेशा`--check --diff`|
| **टैग का प्रयोग करें** | चयनात्मक निष्पादन के लिए टैग कार्य |
| **रहस्यों के लिए तिजोरी का उपयोग करें** | पासवर्ड को कभी भी सादे टेक्स्ट में संग्रहित न करें |
| **नपुंसकता** | कार्य कई बार चलाने के लिए सुरक्षित होने चाहिए |
| **उपयोग बन** | विशेषाधिकार वृद्धि के लिए`become: true`का उपयोग करें |
| **समानांतरता को सीमित करें** | समवर्ती कनेक्शन को नियंत्रित करने के लिए`--forks`का उपयोग करें |
| **वैग्रांट/डॉकर के साथ परीक्षण** | उत्पादन पर चलने से पहले स्थानीय स्तर पर प्लेबुक का परीक्षण करें |
| **`--step` का प्रयोग करें** | इंटरैक्टिव मोड: निष्पादन से पहले प्रत्येक कार्य की पुष्टि करें |
---

## सारांश
Ansible SSH पर निष्पादित YAML प्लेबुक के माध्यम से सर्वर कॉन्फ़िगरेशन और एप्लिकेशन परिनियोजन को स्वचालित करता है। वर्कफ़्लो है: इन्वेंट्री परिभाषित करें → प्लेबुक लिखें →`ansible-playbook`चलाएं। मुख्य अवधारणाओं में मॉड्यूल (कार्य की इकाइयाँ), भूमिकाएँ (पुन: प्रयोज्य संग्रह), हैंडलर (ट्रिगर किए गए कार्य), और चर (गतिशील मान) शामिल हैं। सामान्य मॉड्यूल पैकेज प्रबंधन, फ़ाइल संचालन, सेवा नियंत्रण और उपयोगकर्ता प्रबंधन को कवर करते हैं। आवेदन करने से पहले हमेशा चेक मोड का उपयोग करें; अन्सिबल वॉल्ट में रहस्य संग्रहीत करें; सुनिश्चित करें कि कार्य निष्प्रभावी हों; और उत्पादन चालू करने से पहले स्थानीय स्तर पर परीक्षण करें।