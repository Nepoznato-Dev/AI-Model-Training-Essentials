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
# برو - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم Go را پوشش می‌دهد.
---

## زنجیره ابزار (توکار)
| ابزار | هدف |
|------|---------|
| **برو بساز** | کامپایل بسته ها و وابستگی ها |
| **برو تست** | اجرای تست ها |
| **برو دامپزشک** | تجزیه و تحلیل استاتیک |
| **go fmt** | قالب بندی کد |
| **go mod** | مدیریت ماژول |
| **برو دکتر** | نمایشگر اسناد |
| **برو تولید** | تولید کد |
| **برو نصب** | کامپایل و نصب |
| **برو بدو** | کامپایل و اجرا |
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

## ابزارهای شخص ثالث
| ابزار | هدف |
|------|---------|
| **golangci-lint** | جمع کننده چند لیتری |
| **gofumpt** | فرمت ساز دقیق تر |
| **استاتیک چک** | تجزیه و تحلیل استاتیک پیشرفته |
| **هوا** | بارگذاری مجدد زنده برای توسعه |
| **gomock / mockgen** | چارچوب تمسخر آمیز |
| **سوگ** | مولد اسناد Swagger |
| **باف** | ابزار بافر پروتکل |
---

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **net/http** | کتابخانه استاندارد | API های ساده، بدون وابستگی |
| **جین** | عملکرد | HTTP سریع، میان افزار |
| **اکو** | حداقل | طراحی Clean API |
| **فیبر** | اکسپرس مانند | آشنا به توسعه دهندگان Node.js |
| **چی** | روتر | سبک وزن، سازگار با stdlib |
| **هما** | OpenAPI | طراحی API-first |
---

## gRPC و API
| ابزار | هدف |
|------|---------|
| **google.golang.org/grpc** | چارچوب gRPC |
| **connect-go** | gRPC-Web، gRPC، REST |
| **protoc-gen-go** | تولید کد پروتوباف |
| **grpc-gateway** | REST به پروکسی gRPC |
---

## پایگاه داده
| پکیج | پایگاه داده |
|---------|----------|
| **پایگاه داده/sql** | رابط استاندارد SQL |
| **pgx** | درایور PostgreSQL (سریع) |
| **GORM** | ORM کامل |
| **sqlc** | Go-safe از SQL | ایجاد کنید
| **نت** | چارچوب نهاد (فیس بوک) |
| **go-redis** | مشتری Redis |
| **راننده مونگو** | مشتری MongoDB |
---

## تست
| ابزار | هدف |
|------|---------|
| **تست** | چارچوب تست داخلی |
| **شهادت دادن** | ادعاها و تمسخر |
| **go-cmp** | مقایسه عمیق |
| **httptest** | ابزارهای تست HTTP |
| **گو-فاز/فاز** | تست فاز |
| **benchstat** | مقایسه معیار |
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

## ابزارهای CLI
| پکیج | هدف |
|---------|---------|
| **کبری** | چارچوب CLI (kubectl از این استفاده می کند) |
| **urfave/cli** | ساز ساده CLI |
| **چای حبابی** | رابط کاربری ترمینال (Charm) |
| **رژلب** | یک ظاهر طراحی ترمینال |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + gopls** | Official Go LSP |
| **Goland** | Full JetBrains Go IDE |
| **Neovim + gopls** | مبتنی بر ترمینال |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | `CGO_ENABLED=0 go build`|
| **تقاطع کامپایل** | `GOOS=linux GOARCH=amd64 go build`|
| **داکر** | ساخت های چند مرحله ای، بدون توزیع |
| **ظروف** | تصاویر کوچک (~10MB) |
---

## خلاصه
اکوسیستم Go عملگرا و حداقلی است. کتابخانه استاندارد HTTP، JSON، تست و موارد دیگر را پوشش می‌دهد - اغلب نیاز به چارچوب‌ها را از بین می‌برد. پشته مدرن عبارتند از: **go modules** برای وابستگی ها، **golangci-lint** برای linting، **Gin** یا **Chi** برای وب، **pgx** یا **sqlc** برای پایگاه های داده، **cobra** برای CLIها، و **باینری های استاتیک** برای استقرار. نقطه قوت Go سادگی است: کامپایل سریع، باینری های کوچک و یک مدل استقرار باینری تک.