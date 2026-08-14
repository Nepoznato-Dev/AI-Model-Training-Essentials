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
# Quản lý cấu hình và Ansible
Ansible là một công cụ tự động hóa và quản lý cấu hình không cần tác nhân. Nó sử dụng SSH (hoặc WinRM cho Windows) để kết nối với máy chủ và thực thi các tác vụ được xác định trong sổ tay YAML. Không giống như các công cụ yêu cầu cài đặt tác nhân trên mọi máy, Ansible dựa trên cơ chế đẩy — bạn chạy lệnh từ nút điều khiển. Nó được sử dụng để cung cấp máy chủ, triển khai ứng dụng, quản lý cấu hình và thực thi tác vụ đặc biệt.
---

## Khái niệm cốt lõi
| Khái niệm | Mô tả |
|----------|-------------|
| **Hàng tồn kho** | Danh sách máy chủ được quản lý (định dạng INI hoặc YAML) |
| **Sách hướng dẫn** | Tệp YAML xác định một tập hợp các tác vụ cần thực thi |
| **Chơi** | Ánh xạ giữa máy chủ và tác vụ trong sổ chơi |
| **Nhiệm vụ** | Một hành động duy nhất để thực hiện trên máy chủ |
| **Mô-đun** | Một đơn vị công việc (ví dụ:`apt`,`copy`,`service`,`template`) |
| **Vai trò** | Bộ sưu tập các tác vụ, biến, tệp và trình xử lý có thể tái sử dụng |
| **Biến** | Giá trị động được sử dụng trong sách giải trí |
| **Người xử lý** | Tác vụ được kích hoạt bởi một thông báo (ví dụ: khởi động lại dịch vụ) |
| **Sự thật** | Thông tin hệ thống được thu thập về máy chủ (OS, IP, v.v.) |
---

## Các lệnh chung
| Lệnh | Mô tả |
|----------|-------------|
| `ansible all -m ping`| Kiểm tra kết nối tới tất cả các máy chủ |
| `ansible all -m shell -a "uptime"`| Chạy lệnh shell trên tất cả các máy chủ |
| `ansible-playbook site.yml`| Thực hiện một vở kịch |
| `ansible-playbook site.yml --check`| Chạy khô (chế độ kiểm tra) |
| `ansible-playbook site.yml --diff`| Hiển thị những gì sẽ thay đổi |
| `ansible-playbook site.yml -l web`| Chạy đua với một nhóm cụ thể |
| `ansible-playbook site.yml --tags deploy`| Chỉ chạy các tác vụ có thẻ cụ thể |
| `ansible-playbook site.yml --skip-tags debug`| Bỏ qua nhiệm vụ với các thẻ cụ thể |
| `ansible-vault encrypt secrets.yml`| Mã hóa một tập tin |
| `ansible-vault decrypt secrets.yml`| Giải mã một tập tin |
| `ansible-vault edit secrets.yml`| Chỉnh sửa tệp được mã hóa |
| `ansible-galaxy install geerlingguy.nginx`| Cài đặt vai trò từ Ansible Galaxy |
| `ansible-inventory --graph`| Hiển thị hàng tồn kho dưới dạng biểu đồ |
| `ansible-doc apt`| Hiển thị tài liệu cho một mô-đun |
---

## Định dạng khoảng không quảng cáo
### Định dạng INI
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

### Định dạng YAML
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

## Cấu trúc sổ tay
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

## Các mô-đun chung
| Mô-đun | Mục đích | Ví dụ |
|--------|----------|---------|
| **apt / yum / dnf** | Quản lý trọn gói | `apt: name=nginx state=present`|
| **sao chép** | Sao chép tập tin vào máy chủ | `copy: src=file.txt dest=/tmp/`|
| **mẫu** | Sao chép tệp có biến Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **tập tin** | Quản lý tập tin và thư mục | `file: path=/tmp/dir state=directory`|
| **dịch vụ** | Quản lý dịch vụ | `service: name=nginx state=restarted`|
| **người dùng / nhóm** | Quản lý người dùng và nhóm | `user: name=deploy shell=/bin/bash`|
| **cron** | Quản lý công việc định kỳ | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **vỏ / lệnh** | Chạy lệnh | `shell: echo "hello" > /tmp/test`|
| **git** | Kho nhân bản | `git: repo=https://... dest=/opt/app`|
| **systemd** | Quản lý đơn vị systemd | `systemd: name=myapp enabled=true`|
| **tường lửa / ufw** | Quản lý quy tắc tường lửa | `ufw: rule=allow port=80 proto=tcp`|
| **lineinfile** | Quản lý dòng trong tập tin | `lineinfile: path=/etc/hosts line="..."`|
| **blockinfile** | Quản lý khối văn bản trong tập tin | Chèn/cập nhật khối cấu hình |
| **tìm nạp** | Sao chép tập tin từ máy chủ | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Tương tác với các dịch vụ web | `uri: url=https://api.example.com method=GET`|
| **gỡ lỗi** | In tin nhắn | `debug: msg="Deployed {{ app_version }}"`|
---

## Cấu trúc vai trò
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

## Mẹo và khắc phục sự cố
| Mẹo | Mô tả |
|------|-------------|
| **Sử dụng chế độ kiểm tra** | Luôn`--check --diff`trước khi áp dụng thay đổi |
| **Sử dụng thẻ** | Gắn thẻ nhiệm vụ để thực hiện có chọn lọc |
| **Sử dụng kho lưu trữ bí mật** | Không bao giờ lưu trữ mật khẩu ở dạng văn bản thuần túy |
| **Idempotence** | Nhiệm vụ phải an toàn để chạy nhiều lần |
| **Sử dụng trở thành** | Sử dụng`become: true`để leo thang đặc quyền |
| **Hạn chế song song** | Sử dụng`--forks`để kiểm soát các kết nối đồng thời |
| **Thử nghiệm với Vagrant/Docker** | Kiểm tra playbook cục bộ trước khi chạy trên sản xuất |
| **Sử dụng`--step`** | Chế độ tương tác: xác nhận từng nhiệm vụ trước khi thực hiện |
---

## Bản tóm tắt
Ansible tự động hóa việc cấu hình máy chủ và triển khai ứng dụng thông qua các playbook YAML được thực thi qua SSH. Quy trình làm việc là: xác định khoảng không quảng cáo → viết sách giải trí → chạy`ansible-playbook`. Các khái niệm chính bao gồm các mô-đun (đơn vị công việc), vai trò (bộ sưu tập có thể tái sử dụng), trình xử lý (tác vụ được kích hoạt) và các biến (giá trị động). Các mô-đun phổ biến bao gồm quản lý gói, vận hành tệp, kiểm soát dịch vụ và quản lý người dùng. Luôn sử dụng chế độ kiểm tra trước khi áp dụng; lưu trữ bí mật trong Ansible Vault; đảm bảo nhiệm vụ bình thường; và kiểm tra cục bộ trước khi chạy trên sản xuất.