---
# Metadata
title: "Ansible and Configuration Management"
description: "Ansible playbooks, modules, roles, inventory, automation cheat sheet"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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
|  __BẢO VỆ_0__ | Kiểm tra kết nối tới tất cả các máy chủ |
|  __BẢO VỆ_1__ | Chạy lệnh shell trên tất cả các máy chủ |
|  __BẢO VỆ_2__ | Thực hiện một vở kịch |
|  __BẢO VỆ_3__ | Chạy khô (chế độ kiểm tra) |
|  __BẢO VỆ_4__ | Hiển thị những gì sẽ thay đổi |
|  __BẢO VỆ_5__ | Chạy đua với một nhóm cụ thể |
|  __BẢO VỆ_6__ | Chỉ chạy các tác vụ có thẻ cụ thể |
|  __BẢO VỆ_7__ | Bỏ qua nhiệm vụ với các thẻ cụ thể |
|  __BẢO VỆ_8__ | Mã hóa một tập tin |
|  __BẢO VỆ_9__ | Giải mã một tập tin |
|  __BẢO VỆ_10__ | Chỉnh sửa tệp được mã hóa |
|  __BẢO VỆ_11__ | Cài đặt vai trò từ Ansible Galaxy |
|  __BẢO VỆ_12__ | Hiển thị hàng tồn kho dưới dạng biểu đồ |
|  __BẢO VỆ_13__ | Hiển thị tài liệu cho một mô-đun |
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
| **apt / yum / dnf** | Quản lý trọn gói |  __BẢO VỆ_0__ |
| **sao chép** | Sao chép tập tin vào máy chủ |  __BẢO VỆ_1__ |
| **mẫu** | Sao chép tệp có biến Jinja2 |  __BẢO VỆ_2__ |
| **tập tin** | Quản lý tập tin và thư mục |  __BẢO VỆ_3__ |
| **dịch vụ** | Quản lý dịch vụ |  __BẢO VỆ_4__ |
| **người dùng / nhóm** | Quản lý người dùng và nhóm |  __BẢO VỆ_5__ |
| **cron** | Quản lý công việc định kỳ |  __BẢO VỆ_6__ |
| **vỏ / lệnh** | Chạy lệnh |  __BẢO VỆ_7__ |
| **git** | Kho nhân bản |  __BẢO VỆ_8__ |
| **systemd** | Quản lý đơn vị systemd |  __BẢO VỆ_9__ |
| **tường lửa / ufw** | Quản lý quy tắc tường lửa |  __BẢO VỆ_10__ |
| **lineinfile** | Quản lý dòng trong tập tin |  __BẢO VỆ_11__ |
| **blockinfile** | Quản lý khối văn bản trong tập tin | Chèn/cập nhật khối cấu hình |
| **tìm nạp** | Sao chép tập tin từ máy chủ |  __BẢO VỆ_12__ |
| **uri** | Tương tác với các dịch vụ web |  __BẢO VỆ_13__ |
| **gỡ lỗi** | In tin nhắn |  __BẢO VỆ_14__ |
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
Ansible tự động hóa việc cấu hình máy chủ và triển khai ứng dụng thông qua các playbook YAML được thực thi qua SSH. Quy trình làm việc là: xác định khoảng không quảng cáo → viết sách giải trí → chạy`ansible-playbook`. Các khái niệm chính bao gồm mô-đun (đơn vị công việc), vai trò (bộ sưu tập có thể sử dụng lại), trình xử lý (tác vụ được kích hoạt) và biến (giá trị động). Các mô-đun phổ biến bao gồm quản lý gói, vận hành tệp, kiểm soát dịch vụ và quản lý người dùng. Luôn sử dụng chế độ kiểm tra trước khi áp dụng; lưu trữ bí mật trong Ansible Vault; đảm bảo nhiệm vụ bình thường; và kiểm tra cục bộ trước khi chạy trên sản xuất.