---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
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
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Prometheus và Grafana
Prometheus là bộ công cụ cảnh báo và giám sát nguồn mở được thiết kế để đảm bảo độ tin cậy và khả năng mở rộng. Grafana là nền tảng nguồn mở hàng đầu để trực quan hóa dữ liệu chuỗi thời gian. Cùng nhau, chúng tạo thành hệ thống giám sát phổ biến nhất cho các ứng dụng và cơ sở hạ tầng hiện đại. Prometheus thu thập và lưu trữ số liệu; Grafana hiển thị chúng trong bảng thông tin.
---

## Kiến trúc Prometheus
| Thành phần | Mô tả |
|----------||-------------|
| **Máy chủ Prometheus** | Xóa số liệu khỏi mục tiêu; lưu trữ dữ liệu chuỗi thời gian; đánh giá các quy tắc cảnh báo |
| **Nhà xuất khẩu** | Hiển thị số liệu từ hệ thống (Node Xuất khẩu, cAdvisor, v.v.) |
| **Cổng đẩy** | Nhận số liệu từ các công việc ngắn hạn (công việc hàng loạt, CI) |
| **Quản lý cảnh báo** | Xử lý các cảnh báo: nhóm, im lặng, định tuyến, ức chế |
| **Khám phá dịch vụ** | Tự động phát hiện mục tiêu (Kubernetes, Consul, EC2, v.v.) |
---

## Các khái niệm chính
| Khái niệm | Mô tả |
|----------|-------------|
| **Số liệu** | Phép đo được đặt tên với các nhãn tùy chọn và giá trị |
| **Chuỗi thời gian** | Luồng điểm dữ liệu cho kết hợp số liệu + nhãn cụ thể |
| **Công việc** | Tập hợp các mục tiêu có cùng mục đích |
| **Phiên bản** | Một mục tiêu duy nhất để cạo (thường là một quá trình) |
| **Cạo** | Prometheus lấy số liệu từ mục tiêu theo định kỳ |
| **Nhãn** | Cặp khóa-giá trị đo kích thước của số liệu (ví dụ:`method="GET"`) |
| **Mẫu** | Một giá trị tại một thời điểm: (dấu thời gian, giá trị) |
---

## Loại số liệu
| Loại | Mô tả | Trường hợp sử dụng |
|------|-------------|----------|
| **Bộ đếm** | Giá trị tăng đơn điệu (chỉ tăng) | Số lượng yêu cầu; lỗi; nhiệm vụ đã hoàn thành |
| **Máy đo** | Giá trị có thể tăng hoặc giảm | Nhiệt độ; sử dụng bộ nhớ; chiều dài hàng đợi |
| **Biểu đồ** | Quan sát được nhóm theo giá trị | Yêu cầu độ trễ; kích thước phản hồi |
| **Tóm tắt** | Tương tự như biểu đồ; tính toán lượng tử phía khách hàng | Phần trăm độ trễ |
---

## PromQL (Ngôn ngữ truy vấn)
### Truy vấn cơ bản
| Truy vấn | Mô tả |
|-------|-------------|
| `http_requests_total`| Chuỗi thời gian thô |
| `http_requests_total{method="GET"}`| Lọc theo nhãn |
| `http_requests_total{method="GET", status="200"}`| Nhiều bộ lọc nhãn |
| `rate(http_requests_total[5m])`| Tỷ lệ mỗi giây trên 5 phút |
| `increase(http_requests_total[1h])`| Tổng mức tăng hơn 1 giờ |
| `sum(rate(http_requests_total[5m])) by (status)`| Tỷ lệ tổng hợp theo trạng thái |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Độ trễ phân vị thứ 95 |
| `avg(node_cpu_seconds_total{mode="idle"})`| CPU nhàn rỗi trung bình |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Sử dụng CPU |
### Chức năng chung
| Chức năng | Mô tả | Ví dụ |
|----------|-------------|----------|
| `rate()`| Tốc độ tăng trung bình mỗi giây | `rate(requests_total[5m])`|
| `irate()`| Tốc độ mỗi giây dựa trên hai điểm dữ liệu cuối cùng | `irate(requests_total[1m])`|
| `increase()`| Tổng mức tăng theo phạm vi thời gian | `increase(errors_total[1h])`|
| `sum()`| Tổng theo chuỗi | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Trung bình trên toàn bộ loạt | `avg(node_memory_usage)`|
| `histogram_quantile()`| Tính lượng tử từ biểu đồ | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Dòng K hàng đầu theo giá trị | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Dự đoán tuyến tính | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Kiểm tra xem số liệu có bị thiếu không | `absent(up{job="myapp"})`|
---

## Nhà xuất khẩu chung
| Nhà xuất khẩu | Nó giám sát những gì |
|----------|-------------------|
| **Trình xuất nút** | Số liệu máy chủ Linux/Unix (CPU, bộ nhớ, đĩa, mạng) |
| **cCố vấn** | Số liệu vùng chứa (CPU, bộ nhớ, mạng, hệ thống tệp) |
| **Trình xuất MySQL** | Số liệu cơ sở dữ liệu MySQL |
| **Trình xuất PostgreSQL** | Số liệu cơ sở dữ liệu PostgreSQL |
| **Nhà xuất khẩu Redis** | Số liệu Redis |
| **Nhà xuất khẩu hộp đen** | Thăm dò điểm cuối qua HTTP, HTTPS, DNS, TCP, ICMP |
| **Nhà xuất khẩu SNMP** | Số liệu thiết bị mạng qua SNMP |
| **Nhà xuất khẩu JSON** | Số liệu tùy chỉnh từ API JSON |
---

## Grafana
### Các khái niệm chính
| Khái niệm | Mô tả |
|----------|-------------|
| **Nguồn dữ liệu** | Kết nối với Prometheus (hoặc các chương trình phụ trợ khác) |
| **Bảng điều khiển** | Bộ sưu tập các tấm được sắp xếp theo bố cục |
| **Bảng điều khiển** | Trực quan hóa đơn (biểu đồ, thước đo, bảng, bản đồ nhiệt) |
| **Biến** | Bộ lọc động cho bảng thông tin (ví dụ: chọn phiên bản) |
| **Chú thích** | Đánh dấu các sự kiện trên biểu đồ (triển khai, sự cố) |
| **Quy tắc cảnh báo** | Cảnh báo dựa trên ngưỡng trong Grafana |
| **Tạo khuôn mẫu** | Các mẫu bảng điều khiển có thể tái sử dụng với các biến |
### Các mẫu bảng điều khiển hữu ích
| Mẫu | Mô tả |
|----------|-------------|
| **Hàng tổng quan** | Sơ lược về các số liệu chính: tỷ lệ lỗi, độ trễ, thông lượng |
| **Chi tiết sâu** | Nhấp từ chế độ xem tóm tắt đến chế độ xem chi tiết bằng cách sử dụng các biến |
| **Phương pháp ĐỎ** | Tỷ lệ, Lỗi, Thời lượng — ba số liệu dịch vụ chính |
| **Phương pháp SỬ DỤNG** | Sử dụng, Bão hòa, Lỗi — đối với cơ sở hạ tầng |
| **Tín hiệu vàng** | Độ trễ, lưu lượng truy cập, lỗi, bão hòa (Sách SRE của Google) |
---

## Cảnh báo
### Cấu trúc quy tắc cảnh báo
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Định tuyến trình quản lý cảnh báo
| Khái niệm | Mô tả |
|----------|-------------|
| **Nhóm** | Kết hợp các cảnh báo tương tự thành một thông báo |
| **Tuyến đường** | Cây so khớp xác định nơi cảnh báo sẽ đi |
| **Bộ thu** | Nơi gửi thông báo (email, Slack, PagerDuty, webhook) |
| **Ức chế** | Ngăn chặn cảnh báo khi một cảnh báo khác đang kích hoạt |
| **Im lặng** | Tạm thời tắt tiếng cảnh báo bằng công cụ so khớp nhãn |
---

## Khắc phục sự cố
| Vấn đề | Giải pháp |
|----------|----------|
| **Hạ mục tiêu** | Kiểm tra xem nhà xuất khẩu có đang chạy hay không; kiểm tra mạng/tường lửa; xác minh cấu hình cạo |
| **Không có dữ liệu** | Kiểm tra chính tả tên số liệu; kiểm tra bộ lọc nhãn; xác minh phạm vi thời gian |
| **Số lượng cao** | Quá nhiều kết hợp nhãn; giảm giá trị nhãn; sử dụng quy tắc ghi âm |
| **Truy vấn chậm** | Sử dụng quy tắc ghi cho các truy vấn phức tạp; tăng khoảng thời gian cạo |
| **Cảnh báo mệt mỏi** | Ngưỡng điều chỉnh; thêm thời lượng `for`; cảnh báo liên quan đến nhóm |
| **Thiếu số liệu sau khi khởi động lại** | Prometheus lưu trữ dữ liệu cục bộ; kiểm tra cài đặt lưu giữ |
---

## Bản tóm tắt
Prometheus giám sát các hệ thống bằng cách thu thập số liệu từ các nhà xuất khẩu theo định kỳ. Số liệu có bốn loại: bộ đếm (chỉ tăng), thước đo (lên và xuống), biểu đồ (quan sát theo nhóm) và tóm tắt (lượng tử). PromQL là ngôn ngữ truy vấn —`rate()`,`increase()`,`histogram_quantile()`và các hàm tổng hợp (`sum`,`avg`) là các hoạt động phổ biến nhất. Grafana trực quan hóa dữ liệu Prometheus trong bảng thông tin bằng bảng điều khiển, biến và chú thích. Cảnh báo sử dụng Alertmanager để nhóm, định tuyến, tắt tiếng và ngăn chặn cảnh báo. Các mẫu giám sát chính là tín hiệu vàng của Google (độ trễ, lưu lượng truy cập, lỗi, độ bão hòa) và phương pháp RED (tốc độ, lỗi, thời lượng) cho các dịch vụ và phương pháp USE (mức sử dụng, độ bão hòa, lỗi) cho cơ sở hạ tầng.