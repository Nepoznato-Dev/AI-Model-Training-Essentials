<!--
---
# Metadata
title: "Go — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Go ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [go, golang, ecosystem, tooling, testing, web, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Đi — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Go.
---

## Chuỗi công cụ (Tích hợp sẵn)
| Công cụ | Mục đích |
|------|----------|
| **đi xây dựng** | Biên dịch các gói và phụ thuộc |
| **đi kiểm tra** | Chạy thử nghiệm |
| **đi khám thú y** | Phân tích tĩnh |
| **đi fmt** | Định dạng mã |
| **đi mod** | Quản lý mô-đun |
| **đi bác sĩ** | Trình xem tài liệu |
| **đi tạo** | Tạo mã |
| **đi cài đặt** | Biên dịch và cài đặt |
| **chạy đi** | Biên dịch và chạy |
```bash
go mod init example.com/project  # initialize module
go get github.com/pkg/errors     # add dependency
go mod tidy                      # clean up dependencies
go build -o app ./cmd/app       # build binary
go test ./...                    # run all tests
go test -race ./...              # with race detector
go test -cover ./...             # with coverage
go vet ./...                     # static analysis
```

---

## Công cụ của bên thứ ba
| Công cụ | Mục đích |
|------|----------|
| **golangci-lint** | Bộ tổng hợp nhiều linter |
| **ngốc** | Định dạng chặt chẽ hơn |
| **kiểm tra tĩnh** | Phân tích tĩnh nâng cao |
| **không khí** | Tải lại trực tiếp để phát triển |
| **gomock / mockgen** | Khung mô phỏng |
| **vui vẻ** | Trình tạo tài liệu vênh vang |
| **buf** | Công cụ bộ đệm giao thức |
---

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **mạng/http** | Thư viện chuẩn | API đơn giản, không phụ thuộc |
| **Rượu** | Hiệu suất | HTTP nhanh, phần mềm trung gian |
| **Tiếng vang** | Tối thiểu | Thiết kế API sạch |
| **Sợi** | Thích thể hiện | Quen thuộc với các nhà phát triển Node.js |
| **Chi** | Bộ định tuyến | Nhẹ, tương thích với stdlib |
| **Huma** | OpenAPI | Thiết kế ưu tiên API |
---

## gRPC & API
| Công cụ | Mục đích |
|------|----------|
| **google.golang.org/grpc** | khung gRPC |
| **kết nối-đi** | gRPC-Web, gRPC, REST |
| **protoc-gen-go** | Tạo mã Protobuf |
| **grpc-gateway** | REST tới proxy gRPC |
---

## Cơ sở dữ liệu
| Trọn gói | Cơ sở dữ liệu |
|----------|----------|
| **cơ sở dữ liệu/sql** | Giao diện SQL chuẩn |
| **pgx** | Trình điều khiển PostgreSQL (nhanh) |
| **GORM** | ORM đầy đủ |
| **sqlc** | Tạo kiểu Go an toàn từ SQL |
| **Ent** | Khung thực thể (Facebook) |
| **go-redis** | Khách hàng Redis |
| **mongo-go-driver** | Máy khách MongoDB |
---

##Thử nghiệm
| Công cụ | Mục đích |
|------|----------|
| **thử nghiệm** | Khung kiểm tra tích hợp |
| **làm chứng** | Khẳng định và chế nhạo |
| **go-cmp** | So sánh sâu sắc |
| **httptest** | Tiện ích kiểm tra HTTP |
| **lông tơ / lông tơ** | Kiểm tra lông tơ |
| **thống kê băng ghế dự bị** | So sánh điểm chuẩn |
```go
func TestAdd(t *testing.T) {
    got := Add(2, 3)
    if got != 5 {
        t.Errorf("Add(2, 3) = %d, want 5", got)
    }
}

// Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct{
        name string
        a, b, want int
    }{
        {"positive", 2, 3, 5},
        {"zero", 0, 0, 0},
        {"negative", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.want {
                t.Errorf("got %d, want %d", got, tt.want)
            }
        })
    }
}
```

---

## Công cụ CLI
| Trọn gói | Mục đích |
|----------|----------|
| **rắn hổ mang** | Khung CLI (kubectl sử dụng cái này) |
| **urfave/cli** | Trình tạo CLI đơn giản |
| **trà bong bóng** | Giao diện người dùng đầu cuối (Bùa chú) |
| **son bóng** | Kiểu dáng thiết bị đầu cuối |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + gopls** | Đi LSP chính thức |
| **GoLand** | JetBrains Go IDE đầy đủ |
| **Nevim + gopls** | Dựa trên thiết bị đầu cuối |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Nhị phân tĩnh** | `CGO_ENABLED=0 go build`|
| **Biên dịch chéo** | `GOOS=linux GOARCH=amd64 go build`|
| **Docker** | Bản dựng nhiều giai đoạn, không thể phân phối |
| **Hộp chứa** | Hình ảnh nhỏ (~10MB) |
---

## Bản tóm tắt
Hệ sinh thái của Go rất thực dụng và tối thiểu. Thư viện tiêu chuẩn bao gồm HTTP, JSON, thử nghiệm, v.v. — thường loại bỏ nhu cầu về khung. Ngăn xếp hiện đại là: **go module** cho phần phụ thuộc, **golangci-lint** cho linting, **Gin** hoặc **Chi** cho web, **pgx** hoặc **sqlc** cho cơ sở dữ liệu, **cobra** cho CLI và **nhị phân tĩnh** để triển khai. Điểm mạnh của Go là sự đơn giản: biên dịch nhanh, các tệp nhị phân nhỏ và mô hình triển khai nhị phân duy nhất.