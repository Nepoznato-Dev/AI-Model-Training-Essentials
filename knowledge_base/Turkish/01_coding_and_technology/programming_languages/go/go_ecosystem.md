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
# Go — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz Go ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Takım Zinciri (Yerleşik)
| Araç | Amaç |
|------|------------|
| **inşa etmeye başlayın** | Paketleri ve bağımlılıkları derleyin |
| **teste git** | Testleri çalıştırın |
| **veterinere gidin** | Statik analiz |
| **fmt'ye git** | Kod biçimlendirme |
| **moda git** | Modül yönetimi |
| **belgeye git** | Belge görüntüleyici |
| **oluşturmaya git** | Kod oluşturma |
| **kurmaya gidin** | Derleyin ve yükleyin |
| **koşmaya git** | Derleyin ve çalıştırın |
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

## Üçüncü Taraf Araçlar
| Araç | Amaç |
|------|------------|
| **golangci-lint** | Çoklu-internet toplayıcı |
| **gofumpt** | Daha sıkı biçimlendirici |
| **statik kontrol** | Gelişmiş statik analiz |
| **hava** | Geliştirme için canlı yeniden yükleme |
| **gomock / maket** | Alaycı çerçeve |
| **ganimet** | Swagger dokümantasyon oluşturucu |
| **buf** | Protokol Tamponları araçları |
---

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **net/http** | Standart kütüphane | Basit API'ler, bağımlılık yok |
| **Cin** | Performans | Hızlı HTTP, ara katman yazılımı |
| **Yankı** | Asgari | Temiz API tasarımı |
| **Elyaf** | Ekspres benzeri | Node.js geliştiricilerine aşina |
| **Chi** | Yönlendirici | Hafif, stdlib uyumlu |
| **Huma** | OpenAPI | API öncelikli tasarım |
---

## gRPC ve API'ler
| Araç | Amaç |
|------|------------|
| **google.golang.org/grpc** | gRPC çerçevesi |
| **bağlan-git** | gRPC-Web, gRPC, REST |
| **protoc-gen-go** | Protobuf kodu oluşturma |
| **grpc-ağ geçidi** | REST'ten gRPC proxy'sine |
---

## Veritabanı
| Paket | Veritabanı |
|-----------|----------|
| **veritabanı/sql** | Standart SQL arayüzü |
| **pgx** | PostgreSQL sürücüsü (hızlı) |
| **GORM** | Tam ORM |
| **sqlc** | SQL'den tür uyumlu Go oluşturun |
| **Giriş** | Varlık çerçevesi (Facebook) |
| **go-redis** | Redis istemcisi |
| **mongo-go sürücüsü** | MongoDB istemcisi |
---

## Test etme
| Araç | Amaç |
|------|------------|
| **test** | Yerleşik test çerçevesi |
| **ifade ver** | İddialar ve alay |
| **go-cmp** | Derin karşılaştırma |
| **httptest** | HTTP test yardımcı programları |
| **go-fuzz / fuzz** | Fuzz testi |
| **karşılaştırma durumu** | Karşılaştırma karşılaştırması |
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

## CLI Araçları
| Paket | Amaç |
|-----------|-----------|
| **kobra** | CLI çerçevesi (kubectl bunu kullanır) |
| **urfave/cli** | Basit CLI oluşturucu |
| **kabarcık çayı** | Terminal Kullanıcı Arayüzü (Cazibe) |
| **dudak parlatıcısı** | Terminal stili |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + gopls** | Resmi Go LSP |
| **GoLand** | Tam JetBrains IDE'ye Geçin |
| **Neovim + gopls** | Terminal tabanlı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | `CGO_ENABLED=0 go build`|
| **Çapraz derleme** | `GOOS=linux GOARCH=amd64 go build`|
| **Docker** | Çok aşamalı yapılar, dağıtımız |
| **Konteynerler** | Küçük resimler (~10MB) |
---

## Özet
Go'nun ekosistemi pragmatik ve minimaldir. Standart kitaplık HTTP, JSON, test ve daha fazlasını kapsar; çoğu zaman çerçeve ihtiyacını ortadan kaldırır. Modern yığın şunlardır: bağımlılıklar için **go modülleri**, linting için **golangci-lint**, web için **Gin** veya **Chi**, veritabanları için **pgx** veya **sqlc**, CLI'ler için **cobra** ve dağıtım için **statik ikili dosyalar**. Go'nun gücü basitliğinden gelir: hızlı derleme, küçük ikili dosyalar ve tek bir ikili dağıtım modeli.