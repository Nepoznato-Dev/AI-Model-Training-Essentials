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
# Manajemen Kemungkinan dan Konfigurasi
Ansible adalah alat otomatisasi dan manajemen konfigurasi tanpa agen. Ia menggunakan SSH (atau WinRM untuk Windows) untuk terhubung ke server dan menjalankan tugas yang ditentukan dalam buku pedoman YAML. Tidak seperti alat yang memerlukan agen diinstal pada setiap mesin, Ansible berbasis push — Anda menjalankan perintah dari node kontrol. Ini digunakan untuk penyediaan server, penerapan aplikasi, manajemen konfigurasi, dan eksekusi tugas ad-hoc.
---

## Konsep Inti
| Konsep | Deskripsi |
|---------|-------------|
| **Inventaris** | Daftar host yang dikelola (format INI atau YAML) |
| **Buku Pedoman** | File YAML yang mendefinisikan serangkaian tugas yang akan dijalankan |
| **Mainkan** | Pemetaan antara host dan tugas dalam buku pedoman |
| **Tugas** | Satu tindakan untuk dilakukan pada host |
| **Modul** | Satuan kerja (misalnya,`apt`,`copy`,`service`,`template`) |
| **Peran** | Kumpulan tugas, variabel, file, dan penangan yang dapat digunakan kembali |
| **Variabel** | Nilai dinamis yang digunakan dalam buku pedoman |
| **Penanganan** | Tugas dipicu oleh pemberitahuan (mis., mulai ulang layanan) |
| **Fakta** | Informasi sistem yang dikumpulkan tentang host (OS, IP, dll.) |
---

## Perintah Umum
| Perintah | Deskripsi |
|---------|-------------|
| `ansible all -m ping`| Uji konektivitas ke semua host |
| `ansible all -m shell -a "uptime"`| Jalankan perintah shell di semua host |
| `ansible-playbook site.yml`| Jalankan buku pedoman |
| `ansible-playbook site.yml --check`| Uji coba (mode periksa) |
| `ansible-playbook site.yml --diff`| Tunjukkan apa yang akan berubah |
| `ansible-playbook site.yml -l web`| Berlari melawan kelompok tertentu |
| `ansible-playbook site.yml --tags deploy`| Jalankan hanya tugas dengan tag tertentu |
| `ansible-playbook site.yml --skip-tags debug`| Lewati tugas dengan tag tertentu |
| `ansible-vault encrypt secrets.yml`| Enkripsi file |
| `ansible-vault decrypt secrets.yml`| Mendekripsi file |
| `ansible-vault edit secrets.yml`| Edit file terenkripsi |
| `ansible-galaxy install geerlingguy.nginx`| Instal peran dari Ansible Galaxy |
| `ansible-inventory --graph`| Tampilkan inventaris sebagai grafik |
| `ansible-doc apt`| Tampilkan dokumentasi untuk modul |
---

## Format Inventaris
### Format INI
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

### Format YAML
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

## Struktur Buku Pedoman
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

## Modul Umum
| Modul | Tujuan | Contoh |
|--------|---------|---------|
| **apt / enak / dnf** | Manajemen paket | `apt: name=nginx state=present`|
| **salin** | Salin file ke host | `copy: src=file.txt dest=/tmp/`|
| **templat** | Salin file dengan variabel Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **berkas** | Kelola file dan direktori | `file: path=/tmp/dir state=directory`|
| **layanan** | Kelola layanan | `service: name=nginx state=restarted`|
| **pengguna/grup** | Kelola pengguna dan grup | `user: name=deploy shell=/bin/bash`|
| **cron** | Kelola pekerjaan cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **kulit / perintah** | Jalankan perintah | `shell: echo "hello" > /tmp/test`|
| **git** | Repositori klon | `git: repo=https://... dest=/opt/app`|
| **sistemd** | Kelola unit systemd | `systemd: name=myapp enabled=true`|
| **firewall / ufw** | Kelola aturan firewall | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Kelola baris dalam file | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | Kelola blok teks dalam file | Sisipkan/perbarui blok konfigurasi |
| **ambil** | Salin file dari host | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Berinteraksi dengan layanan web | `uri: url=https://api.example.com method=GET`|
| **debug** | Cetak pesan | `debug: msg="Deployed {{ app_version }}"`|
---

## Struktur Peran
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

## Tips dan Pemecahan Masalah
| Kiat | Deskripsi |
|-----|-------------|
| **Gunakan mode pemeriksaan** | Selalu`--check --diff`sebelum menerapkan perubahan |
| **Gunakan tag** | Tandai tugas untuk eksekusi selektif |
| **Gunakan brankas untuk rahasia** | Jangan pernah menyimpan kata sandi dalam teks biasa |
| **Idempotensi** | Tugas harus aman untuk dijalankan beberapa kali |
| **Gunakan menjadi** | Gunakan`become: true`untuk peningkatan hak istimewa |
| **Batasi paralelisme** | Gunakan`--forks`untuk mengontrol koneksi bersamaan |
| **Uji dengan Vagrant / Docker** | Uji playbook secara lokal sebelum menjalankan produksi |
| **Gunakan`--step`** | Mode interaktif: konfirmasi setiap tugas sebelum dieksekusi |
---

## Ringkasan
Ansible mengotomatiskan konfigurasi server dan penerapan aplikasi melalui playbook YAML yang dijalankan melalui SSH. Alur kerjanya adalah: tentukan inventaris → tulis buku pedoman → jalankan`ansible-playbook`. Konsep utama mencakup modul (unit kerja), peran (koleksi yang dapat digunakan kembali), penangan (tugas yang dipicu), dan variabel (nilai dinamis). Modul umum mencakup manajemen paket, operasi file, kontrol layanan, dan manajemen pengguna. Selalu gunakan mode centang sebelum mendaftar; menyimpan rahasia di Ansible Vault; memastikan tugas bersifat idempoten; dan menguji secara lokal sebelum menjalankan produksi.