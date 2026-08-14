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

# Ansible ve Konfigürasyon Yönetimi
Ansible, aracısız bir konfigürasyon yönetimi ve otomasyon aracıdır. Sunuculara bağlanmak ve YAML oyun kitaplarında tanımlanan görevleri yürütmek için SSH'yi (veya Windows için WinRM) kullanır. Her makineye aracıların yüklenmesini gerektiren araçların aksine, Ansible push tabanlıdır; komutları bir kontrol düğümünden çalıştırırsınız. Sunucu provizyonu, uygulama dağıtımı, konfigürasyon yönetimi ve anlık görev yürütme için kullanılır.
---

## Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Envanter** | Yönetilen ana bilgisayarların listesi (INI veya YAML biçimi) |
| **Başucu Kitabı** | yürütülecek bir dizi görevi tanımlayan YAML dosyası |
| **Oynat** | Bir başucu kitabı içindeki ana bilgisayarlar ve görevler arasındaki eşleme |
| **Görev** | Ana Bilgisayarda gerçekleştirilecek tek bir eylem |
| **Modül** | Bir iş birimi (örneğin,`apt`,`copy`,`service`,`template`) |
| **Rol** | Yeniden kullanılabilir görevler, değişkenler, dosyalar ve işleyiciler koleksiyonu |
| **Değişken** | Başucu kitaplarında kullanılan dinamik değerler |
| **İşleyici** | Bir bildirimle tetiklenen görev (ör. hizmeti yeniden başlatma) |
| **Gerçek** | Ana bilgisayarlar hakkında toplanan sistem bilgileri (İşletim Sistemi, IP vb.) |
---

## Ortak Komutlar
| Komut | Açıklama |
|-----------|------------|
| `ansible all -m ping`| Tüm ana bilgisayarlara bağlantıyı test edin |
| `ansible all -m shell -a "uptime"`| Tüm ana bilgisayarlarda bir kabuk komutu çalıştırın |
| `ansible-playbook site.yml`| Bir oyun kitabını yürütün |
| `ansible-playbook site.yml --check`| Deneme çalışması (kontrol modu) |
| `ansible-playbook site.yml --diff`| Neyin değişeceğini gösterin |
| `ansible-playbook site.yml -l web`| Belirli bir gruba karşı koşun |
| `ansible-playbook site.yml --tags deploy`| Yalnızca belirli etiketlere sahip görevleri çalıştırın |
| `ansible-playbook site.yml --skip-tags debug`| Belirli etiketlere sahip görevleri atlayın |
| `ansible-vault encrypt secrets.yml`| Dosyayı şifreleyin |
| `ansible-vault decrypt secrets.yml`| Dosyanın şifresini çözme |
| `ansible-vault edit secrets.yml`| Şifrelenmiş bir dosyayı düzenleyin |
| `ansible-galaxy install geerlingguy.nginx`| Ansible Galaxy'den bir rol yükleyin |
| `ansible-inventory --graph`| Envanteri grafik olarak göster |
| `ansible-doc apt`| Bir modülün belgelerini göster |
---

## Envanter Formatları
### INI Formatı
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

### YAML Formatı
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

## Başucu Kitabı Yapısı
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

## Ortak Modüller
| Modül | Amaç | Örnek |
|-----------|------------|------------|
| **apt / yum / dnf** | Paket yönetimi | `apt: name=nginx state=present`|
| **kopyala** | Dosyaları ana bilgisayarlara kopyalayın | `copy: src=file.txt dest=/tmp/`|
| **şablon** | Dosyaları Jinja2 değişkenleriyle kopyalayın | `template: src=conf.j2 dest=/etc/app.conf`|
| **dosya** | Dosyaları ve dizinleri yönetin | `file: path=/tmp/dir state=directory`|
| **hizmet** | Hizmetleri yönetin | `service: name=nginx state=restarted`|
| **kullanıcı / grup** | Kullanıcıları ve grupları yönetin | `user: name=deploy shell=/bin/bash`|
| **cron** | Cron işlerini yönetin | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **kabuk / komut** | Komutları çalıştır | `shell: echo "hello" > /tmp/test`|
| **git** | Klon depoları | `git: repo=https://... dest=/opt/app`|
| **sistemd** | Sistem birimlerini yönetme | `systemd: name=myapp enabled=true`|
| **güvenlik duvarı / ufw** | Güvenlik duvarı kurallarını yönetin | `ufw: rule=allow port=80 proto=tcp`|
| **satırdosyası** | Dosyalardaki satırları yönetin | `lineinfile: path=/etc/hosts line="..."`|
| **dosyayı engelle** | Dosyalardaki metin bloklarını yönetin | Yapılandırma bloklarını ekleme/güncelleme |
| **getir** | Ana bilgisayarlardan dosya kopyalayın | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Web hizmetleriyle etkileşime geçin | `uri: url=https://api.example.com method=GET`|
| **hata ayıklama** | Mesajları yazdır | `debug: msg="Deployed {{ app_version }}"`|
---

## Rol Yapısı
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

## İpuçları ve Sorun Giderme
| İpucu | Açıklama |
|-----|-------------|
| **Kontrol modunu kullan** | Değişiklikleri uygulamadan önce daima`--check --diff`|
| **Etiketleri kullanın** | Seçici yürütme için görevleri etiketleme |
| **Gizli dosyalar için kasayı kullanın** | Parolaları asla düz metin olarak saklamayın |
| **İdempotans** | Görevlerin birden çok kez çalıştırılması güvenli olmalıdır |
| **Dönüşümü kullan** | Ayrıcalık yükseltme için`become: true`kullanın |
| **Paralelliği sınırlayın** | Eşzamanlı bağlantıları kontrol etmek için`--forks`kullanın |
| **Vgrant / Docker ile test edin** | Üretime geçmeden önce taktik kitaplarını yerel olarak test edin |
| **`--step` kullanın ** | Etkileşimli mod: yürütmeden önce her görevi onaylayın |
---

## Özet
Ansible, SSH üzerinden yürütülen YAML taktik kitapları aracılığıyla sunucu yapılandırmasını ve uygulama dağıtımını otomatikleştirir. İş akışı şu şekildedir: envanteri tanımlayın → başucu kitaplarını yazın → `ansible-playbook`'yi çalıştırın. Anahtar kavramlar arasında modüller (iş birimleri), roller (yeniden kullanılabilir koleksiyonlar), işleyiciler (tetiklenen görevler) ve değişkenler (dinamik değerler) bulunur. Ortak modüller paket yönetimini, dosya işlemlerini, hizmet kontrolünü ve kullanıcı yönetimini kapsar. Başvuru yapmadan önce daima kontrol modunu kullanın; sırları Ansible Vault'ta saklayın; görevlerin eş güce sahip olmasını sağlayın; ve üretime geçmeden önce yerel olarak test edin.