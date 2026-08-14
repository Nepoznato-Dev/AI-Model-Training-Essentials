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
# Ir: Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Go.
---

## Cadena de herramientas (integrada)
| Herramienta | Propósito |
|------|---------|
| **ir a construir** | Compilar paquetes y dependencias |
| **ir a prueba** | Ejecutar pruebas |
| **ve al veterinario** | Análisis estático |
| **ir fmt** | Formato de código |
| **ir mod** | Gestión de módulos |
| **ir al doctor** | Visor de documentación |
| **ir a generar** | Generación de código |
| **ir a instalar** | Compilar e instalar |
| **ve a correr** | Compilar y ejecutar |
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

## Herramientas de terceros
| Herramienta | Propósito |
|------|---------|
| **golangci-lint** | Agregador multilinter |
| **gofumar** | Formateador más estricto |
| **comprobación estática** | Análisis estático avanzado |
| **aire** | Recarga en vivo para el desarrollo |
| **gomock/mockgen** | Marco burlón |
| **botín** | Generador de documentación Swagger |
| **buf** | Herramientas de buffers de protocolo |
---

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **net/http** | Biblioteca estándar | API simples, sin dependencias |
| **Ginebra** | Rendimiento | HTTP rápido, middleware |
| **Eco** | Mínimo | Diseño API limpio |
| **Fibra** | Como expreso | Familiar para los desarrolladores de Node.js |
| **Chi** | Enrutador | Ligero, compatible con stdlib |
| **Huma** | API abierta | Diseño API primero |
---

## gRPC y API
| Herramienta | Propósito |
|------|---------|
| **google.golang.org/grpc** | Marco gRPC |
| **conectar-ir** | gRPC-Web, gRPC, REST |
| **protoc-gen-go** | Generación de código Protobuf |
| **puerta de enlace grpc** | REST al proxy gRPC |
---

## Base de datos
| Paquete | Base de datos |
|---------|----------|
| **base de datos/sql** | Interfaz SQL estándar |
| **página** | Controlador PostgreSQL (rápido) |
| **GORM** | ORM completo |
| **sqlc** | Generar Go con seguridad de tipos desde SQL |
| **Entrada** | Marco de entidad (Facebook) |
| **ir-redis** | Cliente Redis |
| **mongo-go-conductor** | Cliente MongoDB |
---

## Pruebas
| Herramienta | Propósito |
|------|---------|
| **prueba** | Marco de prueba incorporado |
| **testificar** | Afirmaciones y burlas |
| **ir-cmp** | Comparación profunda |
| **prueba http** | Utilidades de prueba HTTP |
| **go-fuzz / fuzz** | Pruebas de fuzz |
| **estadística comparativa** | Comparación de referencia |
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

## Herramientas CLI
| Paquete | Propósito |
|---------|---------|
| **cobra** | Marco CLI (kubectl usa esto) |
| **urfave/cli** | Constructor CLI simple |
| **té de burbujas** | Interfaz de usuario de terminal (encanto) |
| **brillo de labios** | Estilo de terminal |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + gopls** | Go LSP oficial |
| **Ir a Tierra** | JetBrains completo se convierte en IDE |
| **Neovim + gopls** | Basado en terminal |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Binario estático** | `CGO_ENABLED=0 go build`|
| **Compilación cruzada** | `GOOS=linux GOARCH=amd64 go build`|
| **Acoplador** | Construcciones de varias etapas, sin distribución |
| **Contenedores** | Imágenes pequeñas (~10 MB) |
---

## Resumen
El ecosistema de Go es pragmático y mínimo. La biblioteca estándar cubre HTTP, JSON, pruebas y más, lo que a menudo elimina la necesidad de marcos. La pila moderna es: **go módulos** para dependencias, **golangci-lint** para linting, **Gin** o **Chi** para web, **pgx** o **sqlc** para bases de datos, **cobra** para CLI y **binarios estáticos** para implementación. La fortaleza de Go es la simplicidad: compilación rápida, binarios pequeños y un modelo de implementación binario único.