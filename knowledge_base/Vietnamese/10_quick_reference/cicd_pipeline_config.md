---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
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
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Cấu hình đường ống CI/CD
Các quy trình Tích hợp liên tục (CI) và Triển khai liên tục (CD) tự động hóa quá trình xây dựng, thử nghiệm và triển khai phần mềm. Tài liệu tham khảo này bao gồm các mẫu cấu hình cho các nền tảng CI/CD phổ biến nhất: GitHub Actions, GitLab CI và các nguyên tắc thiết kế quy trình chung.
---

## Hành động GitHub
### Cấu trúc quy trình làm việc
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### Các tác nhân kích hoạt phổ biến
| Kích hoạt | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Mỗi lần đẩy |
|  __BẢO VỆ_1__ | Về PR mở, cập nhật, mở lại |
|  __BẢO VỆ_2__ | Lịch trình dựa trên Cron |
|  __BẢO VỆ_3__ | Kích hoạt thủ công |
|  __BẢO VỆ_4__ | Khi tạo bản phát hành |
|  __BẢO VỆ_5__ | Được gọi bởi một quy trình làm việc khác (có thể tái sử dụng) |
### Các tính năng chính
| Tính năng | Mô tả |
|----------|-------------|
| **Chiến lược ma trận** | Chạy cùng một công việc với các cấu hình khác nhau |
| **Bí mật** | Biến môi trường được mã hóa (`${{ secrets.MY_SECRET }}`) |
| **Môi trường** | Mục tiêu triển khai với quy tắc bảo vệ |
| **Bộ nhớ đệm** | Sự phụ thuộc vào bộ đệm giữa các lần chạy |
| **Hiện vật** | Tải tệp lên từ công việc (báo cáo thử nghiệm, bản dựng) |
| **Quy trình làm việc có thể tái sử dụng** | Chia sẻ logic quy trình công việc trên các kho lưu trữ |
| **Hành động tổng hợp** | Kết hợp nhiều bước thành một hành động |
### Chiến lược ma trận
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## CI GitLab
### Cấu trúc đường ống
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### Từ khóa chính
| Từ khóa | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Xác định các giai đoạn của quy trình và thứ tự của chúng |
|  __BẢO VỆ_1__ | Phân công công việc cho một giai đoạn |
|  __BẢO VỆ_2__ | Các lệnh thực thi |
|  __BẢO VỆ_3__ | Các lệnh chạy trước script chính |
|  __BẢO VỆ_4__ | Các lệnh chạy sau tập lệnh chính (ngay cả khi bị lỗi) |
|  __BẢO VỆ_5__ | Kiểm soát khi công việc chạy (nhánh, thẻ) |
|  __BẢO VỆ_6__ | Phiên bản linh hoạt hơn của chỉ/ngoại trừ |
|  __BẢO VỆ_7__ | Xác định các biến CI/CD |
|  __BẢO VỆ_8__ | Tệp bộ đệm giữa các lần chạy đường ống |
|  __BẢO VỆ_9__ | Các tập tin cần chuyển giữa các công việc |
|  __BẢO VỆ_10__ | Môi trường triển khai |
|  __BẢO VỆ_11__ | Kiểm soát việc thực hiện công việc (on_success, on_failure, thủ công, luôn luôn) |
|  __BẢO VỆ_12__ | Chỉ định phụ thuộc công việc (chế độ DAG) |
|  __BẢO VỆ_13__ | Kế thừa cấu hình từ công việc khác |
|  __BẢO VỆ_14__ | Nhập tệp YAML bên ngoài |
### Biến được xác định trước
| Biến | Mô tả |
|----------|-------------|
|  __BẢO VỆ_0__ | Băm cam kết hiện tại |
|  __BẢO VỆ_1__ | Tên chi nhánh hoặc thẻ |
|  __BẢO VỆ_2__ | ID đường ống |
|  __BẢO VỆ_3__ | Mã công việc |
|  __BẢO VỆ_4__ | Đường dẫn đầy đủ đến dự án |
|  __BẢO VỆ_5__ | URL đăng ký vùng chứa |
|  __BẢO VỆ_6__ | Tên chi nhánh mặc định |
---

## Mẫu thiết kế đường ống
### Các mẫu phổ biến
| Mẫu | Mô tả |
|----------|-------------|
| **Xây một lần, triển khai nhiều** | Xây dựng hiện vật một lần; triển khai cùng một tạo phẩm cho từng môi trường |
| **Kiểm tra cổng** | Phê duyệt thủ công trước khi triển khai sản xuất |
| **Cờ tính năng** | Triển khai vào sản xuất nhưng ẩn sau cờ tính năng |
| **Triển khai Canary** | Triển khai với tỷ lệ phần trăm nhỏ; màn hình; triển khai |
| **Triển khai xanh-xanh** | Hai môi trường giống hệt nhau; chuyển giao thông |
| **Thử nghiệm song song** | Chạy song song các bộ thử nghiệm để giảm thời gian xử lý |
| **Lông đầu tiên** | Chạy linters trước các bài kiểm tra đắt tiền; thất bại nhanh chóng |
| **Phụ thuộc vào bộ đệm** | Cache node_modules, pip, Maven để tăng tốc độ xây dựng |
### Các giai đoạn đường ống (Điển hình)
| Sân khấu | Mục đích |
|-------|----------|
| **Lông** | Kiểu mã và phân tích tĩnh |
| **Xây dựng** | Biên dịch; bó; tạo hiện vật |
| **Kiểm tra đơn vị** | Kiểm tra nhanh; không phụ thuộc bên ngoài |
| **Thử nghiệm tích hợp** | Kiểm tra với cơ sở dữ liệu; API; dịch vụ bên ngoài |
| **Quét an ninh** | Lỗ hổng phụ thuộc; quét bí mật; SAST |
| **Gói** | Tạo hình ảnh Docker; xây dựng các hiện vật phát hành |
| **Triển khai dàn dựng** | Triển khai vào môi trường dàn dựng |
| **Thử nghiệm E2E** | Kiểm tra toàn bộ hệ thống dựa trên dàn dựng |
| **Triển khai sản xuất** | Triển khai vào sản xuất (thủ công hoặc tự động) |
| **Thử khói** | Xác minh việc triển khai diễn ra tốt đẹp |
---

## Chiến lược bộ nhớ đệm
| Ngôn ngữ / Công cụ | Đường dẫn bộ đệm | Ví dụ |
|-------|----------||---------|
| **Python (pip)** |  __BẢO VỆ_0__ | `actions/cache`với khóa từ hàm băm`requirements.txt`|
| **Node.js (npm)** |  __BẢO VỆ_3__ | `actions/setup-node`với bộ nhớ đệm tích hợp |
| **Java (Maven)** |  __BẢO VỆ_5__ | Bộ nhớ đệm có khóa từ hàm băm`pom.xml`|
| **Java (Gradle)** |  __BẢO VỆ_7__ | Bộ nhớ đệm có khóa từ hàm băm`build.gradle`|
| **Đi** |  __BẢO VỆ_9__ | Bộ nhớ đệm có khóa từ hàm băm`go.sum`|
| **Rỉ sét (Hàng hóa)** |  __BẢO VỆ_11__ | Bộ nhớ đệm có khóa từ hàm băm`Cargo.lock`|
| **Docker** | Bộ nhớ đệm lớp Docker | `docker/build-push-action`với bộ đệm từ |
---

## Khắc phục sự cố
| Vấn đề | Giải pháp |
|----------|----------|
| **Đường ống chậm** | Phụ thuộc bộ đệm; công việc song song; sử dụng hình ảnh cơ sở nhỏ hơn |
| **Bí mật không có** | Kiểm tra tên bí mật; xác minh phạm vi môi trường; kiểm tra các hạn chế PR của ngã ba |
| **Tạo tác quá lớn** | Loại trừ các tập tin không cần thiết; nén; sử dụng thời gian lưu giữ ngắn hơn |
| **Ma trận quá lớn** | Giảm sự kết hợp; sử dụng`include`/`exclude`|
| **Thử nghiệm không ổn định** | Kiểm dịch kiểm tra không ổn định; khắc phục nguyên nhân gốc rễ; thử lại với`retry:`|
| **Quyền bị từ chối** | Kiểm tra phạm vi mã thông báo; xác minh quyền của người chạy |
---

## Bản tóm tắt
Đường dẫn CI/CD tự động hóa việc xây dựng, thử nghiệm và triển khai phần mềm. GitHub Actions sử dụng quy trình làm việc YAML được kích hoạt bởi các sự kiện trong kho lưu trữ; GitLab CI sử dụng các giai đoạn và công việc với các quy tắc linh hoạt. Các mẫu chính bao gồm: xây dựng một lần triển khai nhiều lần; kiểm tra cổng trước khi sản xuất; lint đầu tiên để có phản hồi nhanh; phụ thuộc bộ đệm để tăng tốc độ xây dựng; và kiểm tra song song. Các giai đoạn quy trình thường tiến triển từ lint → build → test → security → package → triển khai → smoke test. Các chiến lược bộ nhớ đệm khác nhau tùy theo ngôn ngữ nhưng tuân theo cùng một nguyên tắc: các thư mục phụ thuộc bộ nhớ đệm được khóa bằng hàm băm tệp khóa. Mục tiêu là phản hồi nhanh chóng, đáng tin cậy về mọi thay đổi và triển khai an toàn, có thể lặp lại vào sản xuất.