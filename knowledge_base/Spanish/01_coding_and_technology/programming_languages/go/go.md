---
# Metadata
title: "Go"
description: "Comprehensive reference for the Go programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [go, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Ir
Go (a menudo llamado "Golang" por su nombre de dominio original) es un lenguaje de programación compilado y tipado estáticamente diseñado en Google por Robert Griesemer, Rob Pike y Ken Thompson. Fue lanzado por primera vez en 2012 con el objetivo explícito de ser un mejor lenguaje para la programación de sistemas, uno que combine el rendimiento de C con la productividad de lenguajes dinámicos como Python. Go es conocido por su simplicidad, compilación rápida, simultaneidad integrada (gorrutinas y canales) y excelentes herramientas.
Go impulsa gran parte del ecosistema de infraestructura de la nube: Docker, Kubernetes, Terraform, Prometheus, etc. y el servidor HTTP de la biblioteca estándar de Go están todos escritos en Go. Se ha convertido en el lenguaje predeterminado para el desarrollo nativo de la nube, los microservicios y las herramientas CLI.
---

## Por qué es importante ir
- **Simplicidad por diseño**: Go tiene solo 25 palabras clave. El idioma es deliberadamente pequeño y fácil de aprender.
- **Compilación rápida**: compila directamente en código máquina en segundos, incluso para proyectos grandes.
- **Simultaneidad integrada**: las rutinas y los canales hacen que la programación simultánea sea accesible y eficiente.
- **Excelente biblioteca estándar**: servidor HTTP, codificación JSON, pruebas, criptografía, todo integrado.
- **Binarios estáticos**: se compila en un único binario sin dependencias externas. El despliegue es trivial.
- **Pedigrí a escala de Google**: Diseñado por ingenieros que construyeron Unix, UTF-8 y gran parte de la infraestructura de Google.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **No hay coincidencias de tipos/patrones de suma** | Sin enumeraciones con datos asociados, sin tipos algebraicos | Utilice interfaces y interruptores de tipo |
| **Error al manejar la detalle** | Explícito si err! = nil controles en todas partes | Acepta el patrón; hace visible el manejo de errores |
| **Ecosistema más pequeño** | Menos bibliotecas que Python, Java o JavaScript | La biblioteca estándar cubre la mayoría de las necesidades; paquetes comunitarios crecen |
| **Sin marco GUI** | No apto para interfaces de usuario móviles o de escritorio | Utilice UI basadas en web (WASM) u otro idioma |
| **Recolector de basura** | Tiene un GC: las pausas son pequeñas pero distintas de cero | Ajuste GC para cargas de trabajo sensibles a la latencia; utilizar sync.Pool |
---

## Fundamentos de sintaxis
### Estructura básica
```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    name := "World"
    fmt.Printf("Hello, %s!\n", name)

    age := 30
    score := 9.5
    active := true
    message := "Hello"

    upper := strings.ToUpper(message)
    fmt.Println(upper)
}
```

### Funciones
```go
// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

result, err := divide(10, 3)
if err != nil {
    fmt.Println("Error:", err)
    return
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

// Variadic functions
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
```

### Estructuras e interfaces
```go
type Animal struct {
    Name string
    Age  int
}

func (a Animal) Speak() string {
    return a.Name + " makes a sound"
}

// Embedding (composition, not inheritance)
type Dog struct {
    Animal
    Breed string
}

func (d Dog) Speak() string {
    return d.Name + " says woof"
}

// Interface -- implicitly satisfied
type Speaker interface {
    Speak() string
}

func announce(s Speaker) {
    fmt.Println(s.Speak())
}

dog := Dog{Animal: Animal{Name: "Rex"}, Breed: "Labrador"}
announce(dog)
```

### Manejo de errores
```go
type InsufficientFundsError struct {
    Balance float64
    Amount  float64
}

func (e *InsufficientFundsError) Error() string {
    return fmt.Sprintf("cannot withdraw $%.2f from $%.2f", e.Amount, e.Balance)
}

func withdraw(balance, amount float64) (float64, error) {
    if amount > balance {
        return balance, &InsufficientFundsError{Balance: balance, Amount: amount}
    }
    return balance - amount, nil
}

newBalance, err := withdraw(100, 150)
if err != nil {
    var fundsErr *InsufficientFundsError
    if errors.As(err, &fundsErr) {
        fmt.Printf("Need $%.2f more\n", fundsErr.Amount-fundsErr.Balance)
    }
}
```

### Concurrencia: Gorrutinas y canales
```go
// Goroutine
go func() {
    fmt.Println("Running concurrently")
}()

// Channels
func producer(ch chan<- int) {
    for i := 0; i < 5; i++ { ch <- i }
    close(ch)
}

func consumer(ch <-chan int) {
    for value := range ch {
        fmt.Println("Received:", value)
    }
}

ch := make(chan int)
go producer(ch)
consumer(ch)

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Printf("Worker %d done\n", id)
    }(i)
}
wg.Wait()
```

---

## Sintaxis y patrones avanzados
### Genéricos (Go 1.18+)
```go
// Generic function
func Map[T any, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}

// Type constraints
type Number interface {
    ~int | ~float64 | ~float32
}

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}

// Generic struct
type Set[T comparable] struct {
    items map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
    return &Set[T]{items: make(map[T]struct{})}
}

func (s *Set[T]) Add(item T)  { s.items[item] = struct{}{} }
func (s *Set[T]) Has(item T) bool {
    _, ok := s.items[item]
    return ok
}
```

### Coincidencia de patrones avanzada (cambios de tipo)
```go
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("Integer: %d", v)
    case string:
        return fmt.Sprintf("String: %q", v)
    case bool:
        return fmt.Sprintf("Bool: %t", v)
    case []int:
        return fmt.Sprintf("Int slice of length %d", len(v))
    default:
        return fmt.Sprintf("Unknown type: %T", v)
    }
}

// Comma-ok idiom
var i interface{} = "hello"
s, ok := i.(string)
if ok {
    fmt.Println("String:", s)
}
```

### Ajuste de errores personalizado
```go
import "errors"

var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

type ValidationError struct {
    Field   string
    Message string
    Err     error
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation: %s: %s", e.Field, e.Message)
}

func (e *ValidationError) Unwrap() error { return e.Err }

func validateAge(age int) error {
    if age < 0 {
        return &ValidationError{
            Field: "age", Message: "must be non-negative",
        }
    }
    return nil
}

// Error wrapping and checking
func getUser(id int) (*User, error) {
    user, err := db.Find(id)
    if err != nil {
        return nil, fmt.Errorf("getUser(%d): %w", id, ErrNotFound)
    }
    return user, nil
}

// Usage
_, err := getUser(42)
if errors.Is(err, ErrNotFound) {
    fmt.Println("User not found")
}
```

---

## Simultaneidad y paralelismo (análisis profundo)
### Patrón de grupo de trabajadores
```go
func workerPool(jobs <-chan int, results chan<- int, workerCount int) {
    var wg sync.WaitGroup
    for w := 0; w < workerCount; w++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            for j := range jobs {
                results <- j * 2  // Process job
            }
        }(w)
    }
    wg.Wait()
    close(results)
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)

    go workerPool(jobs, results, 5)

    for j := 1; j <= 20; j++ {
        jobs <- j
    }
    close(jobs)

    for r := range results {
        fmt.Println("Result:", r)
    }
}
```

### Contexto de cancelación
```go
func fetchWithTimeout(ctx context.Context, url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```

### Seleccionar para multiplexación
```go
func fanIn(ch1, ch2 <-chan string) <-chan string {
    merged := make(chan string)
    go func() {
        for {
            select {
            case v := <-ch1:
                merged <- v
            case v := <-ch2:
                merged <- v
            }
        }
    }()
    return merged
}
```

---

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto
```
my_project/
+-- go.mod
+-- go.sum
+-- main.go
+-- internal/
|   +-- handlers/
|   |   +-- api.go
|   +-- models/
|   |   +-- user.go
|   +-- service/
|       +-- user_service.go
+-- pkg/
|   +-- utils/
|       +-- helpers.go
+-- cmd/
|   +-- server/
|       +-- main.go
|   +-- cli/
|       +-- main.go
+-- api/
|   +-- openapi.yaml
+-- configs/
|   +-- config.yaml
+-- deployments/
|   +-- Dockerfile
+-- .golangci.yml
```

### ir.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Comandos esenciales
```bash
go mod init myproject         # Initialise module
go mod tidy                   # Download and clean dependencies
go build -o myapp             # Build binary
go run main.go                # Run without building
go test ./...                 # Run all tests
go vet ./...                  # Static analysis
gofmt -w .                    # Format code
go generate ./...             # Run code generators
```

### Canalización de CI/CD (acciones de GitHub)
```yaml
name: Go CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go vet ./...
      - run: go test -race -coverprofile=coverage.out ./...
      - run: go build ./...
```

---

## Pruebas
### Pruebas unitarias
```go
// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
        {"mixed", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
            }
        })
    }
}

func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(2, 3)
    }
}
```

### Pruebas HTTP basadas en tablas
```go
func TestHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/health", nil)
    w := httptest.NewRecorder()
    healthHandler(w, req)

    if w.Code != http.StatusOK {
        t.Errorf("expected 200, got %d", w.Code)
    }
}
```

```bash
go test ./...                    # All tests
go test -v ./...                 # Verbose
go test -race ./...              # Race detector
go test -cover ./...             # Coverage
go test -bench=. ./...           # Benchmarks
go test -fuzz=Fuzz ./...         # Fuzz testing
```

---

## Interoperabilidad
### CGo (llamando a C desde Go)
```go
package main

// #include <stdio.h>
// #include <stdlib.h>
//
// void print_hello() {
//     printf("Hello from C!\n");
// }
import "C"
import "unsafe"

func main() {
    C.print_hello()

    // Passing strings to C
    cs := C.CString("Hello from Go")
    defer C.free(unsafe.Pointer(cs))
    // Use cs in C function calls
}
```

### FFI con otros idiomas
| Dirección | Mecanismo |
|-----------|-----------|
| Ir a llamar a C | cgo (`import "C"`) |
| Vaya a llamar a C++ | funciones contenedoras cgo + C |
| C llamando Ir | Exportar funciones de Go con`//export`|
| Ir a llamar a Python | Utilice gopy o subproceso |
---

## Patrones de diseño
### Patrón de middleware (HTTP)
```go
type Middleware func(http.Handler) http.Handler

func Logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}

func Auth(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Authorization")
        if token == "" {
            http.Error(w, "Unauthorized", http.StatusUnauthorized)
            return
        }
        next.ServeHTTP(w, r)
    })
}

func Chain(h http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        h = middlewares[i](h)
    }
    return h
}
```

### Patrón de opciones
```go
type Server struct {
    host    string
    port    int
    timeout time.Duration
}

type Option func(*Server)

func WithHost(host string) Option    { return func(s *Server) { s.host = host } }
func WithPort(port int) Option       { return func(s *Server) { s.port = port } }
func WithTimeout(d time.Duration) Option { return func(s *Server) { s.timeout = d } }

func NewServer(opts ...Option) *Server {
    s := &Server{host: "localhost", port: 8080, timeout: 30 * time.Second}
    for _, opt := range opts { opt(s) }
    return s
}

srv := NewServer(WithHost("0.0.0.0"), WithPort(3000))
```

---

## Rendimiento y optimización
### Perfilado
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Consejos de optimización
```go
// Pre-allocate slices when size is known
result := make([]int, 0, 1000)

// Use sync.Pool for frequently allocated objects
var bufPool = sync.Pool{
    New: func() interface{} { return new(bytes.Buffer) },
}

// Avoid string concatenation in loops
var b strings.Builder
for i := 0; i < 1000; i++ {
    b.WriteString("hello")
}
result := b.String()
```

---

## Implementación
### Compilación cruzada
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Implementación de Docker
```dockerfile
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY src/ ./
RUN CGO_ENABLED=0 go build -o myapp .

FROM alpine:latest
COPY --from=builder /app/myapp /usr/local/bin/myapp
CMD ["myapp"]
```

---

## La biblioteca estándar
| Paquete | Propósito |
|---------|---------|
| fmt | E/S formateadas |
| red/http | Cliente y servidor HTTP |
| codificación/json | Codificación/decodificación JSON |
| sistema operativo | Operaciones a nivel de sistema operativo |
| yo | Primitivas de E/S |
| cadenas/strconv | Manipulación de cadenas |
| sincronización | Mutex, grupo de espera, una vez |
| contexto | Plazos, cancelación |
| pruebas | Marco de prueba incorporado |
| iniciar sesión / iniciar sesión/slog | Registro |
| tiempo | Hora y duración |
| cripto | Criptografía (TLS, hash) |
| base de datos/sql | Abstracción de base de datos |
---

## Herramientas
```bash
go mod init myproject
go run main.go
go build -o myapp
go test ./...
gofmt -w .
go vet ./...
go mod tidy
```

---

## Cuándo utilizar Go
| Escenario | ¿Por qué ir? Mejor alternativa |
|----------|--------|-------------------|
| Servicios/microservicios nativos de la nube | Binarios rápidos y pequeños, excelente HTTP | Óxido para máximo rendimiento |
| Herramientas CLI | Compilación rápida, binario único | Rust para CLI complejas |
| Servidores web/API | HTTP integrado, rápido y sencillo | Node.js/Express para creación rápida de prototipos |
| Herramientas DevOps | Docker, Kubernetes y Terraform están listos | Python para secuencias de comandos |
| Sistemas concurrentes | Las gorutinas son ligeras y elegantes | Erlang/Elixir para concurrencia tolerante a fallas |
| Programación de redes | Excelente paquete neto | C/C++ para control de nivel más bajo |
| Ciencia de datos / ML | No es el ecosistema adecuado | Pitón, R |
| GUI de escritorio/móvil | Sin marco GUI | Utilice una interfaz web o un idioma nativo |
| Sistemas integrados | Demasiado pesado (GC, tiempo de ejecución) | C, óxido |
---

## Preguntas y respuestas sintéticas
### P1: ¿Por qué Go no tiene excepciones? ¿Cómo debo manejar los errores?
**R:** Go utiliza devoluciones de errores explícitos en lugar de excepciones. Cada función que puede fallar devuelve un`error`como último valor de retorno. Esto obliga a la persona que llama a manejar los errores explícitamente: sin fallas silenciosas ni bloques de captura olvidados. El patrón idiomático es `if err != nil`. Utilice`fmt.Errorf`con`%w`para ajustar errores y`errors.Is`/`errors.As`para comprobar tipos de errores. Para errores irrecuperables (errores de programación), utilice `panic`.
```go
func readConfig(path string) (Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return Config{}, fmt.Errorf("reading config %s: %w", path, err)
    }
    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return Config{}, fmt.Errorf("parsing config %s: %w", path, err)
    }
    return cfg, nil
}
```

### P2: ¿Qué son las gorutinas y en qué se diferencian de los subprocesos del sistema operativo?
**R:** Las gorutinas son subprocesos livianos en el espacio de usuario administrados por el tiempo de ejecución de Go. Comienzan con ~2 KB de pila (frente a ~1 MB para subprocesos del sistema operativo), el programador los multiplexa en subprocesos del sistema operativo y se pueden crear millones a la vez. La comunicación entre gorutinas utiliza canales (o primitivas`sync`para estado compartido). Utilice siempre`sync.WaitGroup`o cancelación de contexto para evitar fugas de rutinas.
```go
// Launch thousands of goroutines — perfectly fine
var wg sync.WaitGroup
for i := 0; i < 10000; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        process(id)
    }(i)
}
wg.Wait()
```

### P3: ¿Cuándo debo usar canales versus mutex para la concurrencia?
**R:** Utilice canales cuando las gorutinas necesiten comunicar datos: imponen la filosofía de "compartir memoria comunicando". Utilice mutex (`sync.Mutex`) cuando las rutinas necesiten proteger el estado compartido (cachés, contadores, grupos de conexiones). Una buena regla: si se pasan datos entre gorutinas, utilice canales; Si varias gorutinas acceden a los datos, utilice un mutex. Para operaciones atómicas simples, use `sync/atomic`.
```go
// Channel pattern — pipeline
func producer(nums chan<- int) {
    for i := 0; i < 10; i++ { nums <- i }
    close(nums)
}
func consumer(nums <-chan int, results chan<- int) {
    for n := range nums { results <- n * n }
    close(results)
}

// Mutex pattern — shared cache
type SafeCache struct {
    mu    sync.RWMutex
    items map[string]string
}
func (c *SafeCache) Get(key string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.items[key]
    return v, ok
}
```

### P4: ¿Cuál es la diferencia entre los sectores/mapas`nil`y los vacíos?
**R:** Un segmento`nil`(`var s []int`) no tiene una matriz subyacente, longitud 0, capacidad 0. Un segmento vacío (`s := []int{}`o`make([]int, 0)`) tiene una matriz subyacente pero longitud 0. Ambos funcionan de manera idéntica con`append`,`len`,`cap`y `range`. La clasificación JSON es diferente: los sectores nulos se convierten en `null`, los sectores vacíos se convierten en `[]`. Mejores prácticas: prefiera sectores nulos para los valores de retorno (indican "sin datos"), sectores vacíos cuando la salida JSON es importante.
```go
var nilSlice []int          // nil, len=0, cap=0
emptySlice := []int{}       // not nil, len=0, cap=0

// Both work with append
nilSlice = append(nilSlice, 1)   // Now len=1
emptySlice = append(emptySlice, 1) // Now len=1

// JSON difference
json.Marshal(nilSlice)     // "null"
json.Marshal(emptySlice)   // "[]"
```

### P5: ¿Cómo funcionan las interfaces en Go y qué es la interfaz vacía?
**R:** Las interfaces Go se satisfacen implícitamente: un tipo implementa una interfaz implementando sus métodos, sin ninguna palabra clave `implements`. Esto permite el desacoplamiento y la composición. La interfaz vacía`interface{}`(o`any`en Go 1.18+) se adapta a todos los tipos; úsela con moderación (los genéricos suelen ser mejores). Los valores de la interfaz son pares: `(type, value)`. Una interfaz nula tiene ambos como nulos.
```go
// Implicit interface satisfaction
type Writer interface {
    Write(p []byte) (n int, err error)
}

// MyWriter implements Writer without declaring it
type MyWriter struct { buf *bytes.Buffer }
func (w *MyWriter) Write(p []byte) (int, error) { return w.buf.Write(p) }

// Type assertion and type switch
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("integer: %d", v)
    case string:
        return fmt.Sprintf("string: %q", v)
    default:
        return fmt.Sprintf("unknown: %T", v)
    }
}
```

---

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: crear un Web Scraper simultáneo con limitación de velocidad
**Declaración del problema:** Cree un programa Go que obtenga URL de una lista simultáneamente, extraiga títulos de páginas, respete un límite de velocidad de 10 solicitudes por segundo y recopile resultados sin carreras de datos.
**Paso 1: comprenda el problema:**
Necesitamos: (1) recuperación HTTP simultánea con gorutinas, (2) limitación de velocidad para evitar saturar los servidores, (3) recopilación de resultados sin carreras, (4) manejo adecuado de errores para solicitudes fallidas. Las primitivas de concurrencia de Go (gorrutinas, canales, `errgroup`) son ideales para esto.
**Paso 2: Identifique el enfoque:**
- Utilice`golang.org/x/time/rate`para limitar la tasa de depósito de tokens.
- Utilice`sync.WaitGroup`o`errgroup.Group`para gestionar gorutinas.
- Utilizar un canal de resultados para recopilar resultados de forma segura.
- Utilice`context.Context`para cancelaciones y tiempos de espera.
**Paso 3: Implementar la solución:**
```go
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "regexp"
    "sync"
    "time"

    "golang.org/x/sync/errgroup"
    "golang.org/x/time/rate"
)

type Result struct {
    URL   string
    Title string
    Error error
}

var titleRegex = regexp.MustCompile(`<title[^>]*>(.*?)</title>`)

func fetchTitle(ctx context.Context, client *http.Client, url string) Result {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    resp, err := client.Do(req)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(io.LimitReader(resp.Body, 1<<20)) // 1MB limit
    if err != nil {
        return Result{URL: url, Error: err}
    }

    matches := titleRegex.FindSubmatch(body)
    if matches == nil {
        return Result{URL: url, Title: "(no title)"}
    }
    return Result{URL: url, Title: string(matches[1])}
}

func scrapeAll(ctx context.Context, urls []string, rps int) []Result {
    limiter := rate.NewLimiter(rate.Limit(rps), rps)
    client := &http.Client{Timeout: 10 * time.Second}
    results := make([]Result, len(urls))

    g, ctx := errgroup.WithContext(ctx)
    g.SetLimit(20) // Max 20 concurrent goroutines

    for i, url := range urls {
        i, url := i, url // Capture loop variables
        g.Go(func() error {
            if err := limiter.Wait(ctx); err != nil {
                return err
            }
            results[i] = fetchTitle(ctx, client, url)
            return nil
        })
    }

    if err := g.Wait(); err != nil {
        fmt.Fprintf(os.Stderr, "Error: %v\n", err)
    }
    return results
}
```

**Paso 4: Verificar y optimizar:**
- Sin carreras de datos: cada goroutine escribe en su propio índice en `results`, no se necesita mutex.
-`errgroup.SetLimit`limita la concurrencia independientemente del limitador de tasa.
-`io.LimitReader`evita la lectura de páginas excesivamente grandes.
-`http.NewRequestWithContext`garantiza que las solicitudes se cancelen cuando finalice el contexto.
- Para producción: agregue lógica de reintento con retroceso exponencial, ajuste de agrupación de conexiones y métricas.
### Problema 2: implementar una caché LRU genérica
**Declaración del problema:** Implemente una caché LRU (menos utilizada recientemente) genérica y segura para subprocesos en Go usando genéricos (Go 1.18+). Debería admitir `Get`,`Set`y`Delete`con complejidad temporal O(1).
**Paso 1: comprenda el problema:**
Una caché LRU necesita búsqueda O(1) (mapa hash) y actualizaciones de orden O(1) (lista doblemente enlazada). En `Get`: mueve el elemento al frente. En `Set`: inserción en la parte delantera; desalojar desde atrás si se excede la capacidad. La seguridad de los subprocesos requiere un mutex.
**Paso 2: Identifique el enfoque:**
- Utilice`container/list`(lista doblemente enlazada) para O(1) mover al frente y quitar desde atrás.
- Utilice`map[K]*list.Element`para la búsqueda O(1).
- Utilice`sync.Mutex`para seguridad del hilo.
- Genéricos (`[K comparable, V any]`) para seguridad de tipos.
**Paso 3: Implementar la solución:**
```go
type entry[K comparable, V any] struct {
    key   K
    value V
}

type LRUCache[K comparable, V any] struct {
    capacity int
    items    map[K]*list.Element
    order    *list.List
    mu       sync.Mutex
}

func NewLRU[K comparable, V any](capacity int) *LRUCache[K, V] {
    return &LRUCache[K, V]{
        capacity: capacity,
        items:    make(map[K]*list.Element),
        order:    list.New(),
    }
}

func (c *LRUCache[K, V]) Get(key K) (V, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        return elem.Value.(*entry[K, V]).value, true
    }
    var zero V
    return zero, false
}

func (c *LRUCache[K, V]) Set(key K, value V) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        elem.Value.(*entry[K, V]).value = value
        return
    }

    if c.order.Len() >= c.capacity {
        oldest := c.order.Back()
        if oldest != nil {
            c.order.Remove(oldest)
            delete(c.items, oldest.Value.(*entry[K, V]).key)
        }
    }

    e := &entry[K, V]{key: key, value: value}
    elem := c.order.PushFront(e)
    c.items[key] = elem
}

func (c *LRUCache[K, V]) Delete(key K) bool {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.Remove(elem)
        delete(c.items, key)
        return true
    }
    return false
}

func (c *LRUCache[K, V]) Len() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.order.Len()
}
```

**Paso 4: Verificar y optimizar:**
- O(1) para `Get`, `Set`, `Delete`: la búsqueda de mapas es O(1) promedio; las operaciones de lista (`MoveToFront`,`PushFront`,`Remove`,`Back`) son todas O(1).
- Seguridad de subprocesos:`sync.Mutex`garantiza que solo una rutina acceda al caché a la vez. Para cargas de trabajo con mucha lectura, utilice `sync.RWMutex`.
- Genéricos:`[K comparable, V any]`garantiza que las claves admitan`==`(requerido para las claves de mapas), mientras que los valores pueden ser de cualquier tipo.
- Producción: considere `github.com/hashicorp/golang-lru/v2`: probado en batalla con soporte TTL y fragmentación para reducir la contención de bloqueos.
### Problema 3: construir un servidor de chat TCP
**Declaración del problema:** Cree un servidor de chat TCP simultáneo donde los clientes puedan conectarse, transmitir mensajes a todos los demás clientes conectados y desconectarse sin problemas. Maneje clientes lentos sin bloquear a otros.
**Paso 1: comprenda el problema:**
Necesitamos: (1) aceptar conexiones TCP, (2) una rutina de lectura por cliente, (3) un mecanismo de transmisión para enviar mensajes a todos los clientes, (4) manejar desconexiones y clientes lentos. Este es un patrón clásico en abanico.
**Paso 2: Identifique el enfoque:**
- Utilice`net.Listener`para conexiones TCP.
- Utilizar una rutina central`hub`con canales para alta/baja/emisión de clientes.
- Cada cliente obtiene una rutina de escritura dedicada con un canal almacenado en búfer; los clientes lentos no bloquean a otros.
- Utilice`context.Context`para un cierre elegante.
**Paso 3: Implementar la solución:**
```go
package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "sync"
)

type Client struct {
    conn net.Conn
    name string
    send chan string
}

type Hub struct {
    clients    map[*Client]bool
    broadcast  chan string
    register   chan *Client
    unregister chan *Client
    mu         sync.RWMutex
}

func NewHub() *Hub {
    return &Hub{
        clients:    make(map[*Client]bool),
        broadcast:  make(chan string, 256),
        register:   make(chan *Client),
        unregister: make(chan *Client),
    }
}

func (h *Hub) Run() {
    for {
        select {
        case client := <-h.register:
            h.mu.Lock()
            h.clients[client] = true
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s joined", client.name)

        case client := <-h.unregister:
            h.mu.Lock()
            if _, ok := h.clients[client]; ok {
                delete(h.clients, client)
                close(client.send)
            }
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s left", client.name)

        case msg := <-h.broadcast:
            h.mu.RLock()
            for client := range h.clients {
                select {
                case client.send <- msg:
                default:
                    // Slow client — disconnect
                    go func(c *Client) {
                        h.unregister <- c
                        c.conn.Close()
                    }(client)
                }
            }
            h.mu.RUnlock()
        }
    }
}

func handleClient(hub *Hub, conn net.Conn) {
    defer conn.Close()
    scanner := bufio.NewScanner(conn)

    // Read first line as name
    if !scanner.Scan() { return }
    name := scanner.Text()

    client := &Client{
        conn: conn,
        name: name,
        send: make(chan string, 64),
    }
    hub.register <- client
    defer func() { hub.unregister <- client }()

    // Write goroutine
    go func() {
        for msg := range client.send {
            fmt.Fprintf(conn, "%s\n", msg)
        }
    }()

    // Read loop
    for scanner.Scan() {
        text := scanner.Text()
        hub.broadcast <- fmt.Sprintf("[%s] %s", name, text)
    }
}

func main() {
    hub := NewHub()
    go hub.Run()

    listener, err := net.Listen("tcp", ":8080")
    if err != nil { log.Fatal(err) }
    log.Println("Chat server listening on :8080")

    for {
        conn, err := listener.Accept()
        if err != nil { log.Println(err); continue }
        go handleClient(hub, conn)
    }
}
```

**Paso 4: Verificar y optimizar:**
- Manejo lento del cliente: el`select`con`default`en transmisión evita el bloqueo. Los clientes lentos se desconectan si se llena su búfer.
- Sin carreras: la rutina central es el único escritor del mapa `clients`; `mu`protege las lecturas durante la transmisión.
- Apagado elegante: agregue`context.Context`y un controlador de señal para cerrar las conexiones del oyente y drenar.
- Producción: considere usar`golang.org/x/net/websocket`para clientes de navegador y agregue autenticación, historial de mensajes y salas.
---

## Resumen
Go es un lenguaje que elige deliberadamente la simplicidad sobre las funciones. Tiene menos construcciones que la mayoría de los lenguajes (sin herencia, sin sobrecarga de métodos, sin excepciones, sin macros) y esto es una fortaleza. El resultado es un código fácil de leer, escribir y mantener. El modelo de concurrencia de Go (gorrutinas y canales) es uno de los mejor diseñados en cualquier idioma. Para infraestructura en la nube, microservicios, herramientas CLI y programación de redes, Go es una excelente opción.