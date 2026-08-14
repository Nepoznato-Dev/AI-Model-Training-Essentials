<!--
---
# Metadata
title: "Go"
description: "Comprehensive reference for the Go programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# Идти
Go (часто называемый «Golang» в честь оригинального доменного имени) — это статически типизированный компилируемый язык программирования, разработанный в Google Робертом Гриземером, Робом Пайком и Кеном Томпсоном. Впервые он был выпущен в 2012 году с явной целью стать лучшим языком для системного программирования, сочетающим в себе производительность C с производительностью динамических языков, таких как Python. Go известен своей простотой, быстрой компиляцией, встроенными возможностями параллелизма (горутины и каналы) и отличными инструментами.
Go поддерживает большую часть экосистемы облачной инфраструктуры: Docker, Kubernetes, Terraform, Prometheus и т. д., а HTTP-сервер стандартной библиотеки Go написаны на Go. Он стал языком по умолчанию для облачной разработки, микросервисов и инструментов CLI.
---

## Почему важно идти
- **Простота дизайна**: в Go всего 25 ключевых слов. Язык намеренно маленький и его легко выучить.
- **Быстрая компиляция**: компилируется непосредственно в машинный код за считанные секунды, даже для больших проектов.
- **Встроенный параллелизм**: горутины и каналы делают параллельное программирование доступным и эффективным.
- **Отличная стандартная библиотека**: HTTP-сервер, кодирование JSON, тестирование, криптография — все встроено.
- **Статические двоичные файлы**: компилируются в один двоичный файл без внешних зависимостей. Развертывание тривиально.
- **Происхождение в масштабах Google**: разработано инженерами, создавшими Unix, UTF-8 и большую часть инфраструктуры Google.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Нет типов сумм и сопоставлений с образцом** | Никаких перечислений со связанными данными, никаких алгебраических типов | Используйте интерфейсы и переключатели типов |
| **Ошибка обработки подробностей** | Явный if err != nil проверяет везде | Примите шаблон; делает обработку ошибок видимой |
| **Меньшая экосистема** | Меньше библиотек, чем Python, Java или JavaScript | Стандартная библиотека покрывает большинство потребностей; общественные пакеты растут |
| **Нет инфраструктуры графического интерфейса** | Не подходит для настольных и мобильных интерфейсов | Используйте веб-интерфейсы пользователя (WASM) или другой язык |
| **Сборщик мусора** | Имеет GC -- паузы маленькие, но ненулевые | Настройте GC для рабочих нагрузок, чувствительных к задержкам; использовать sync.Pool |
---

## Основы синтаксиса
### Базовая структура
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

### Функции
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

### Структуры и интерфейсы
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

### Обработка ошибок
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

### Параллелизм — горутины и каналы
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

## Расширенный синтаксис и шаблоны
### Дженерики (Go 1.18+)
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

### Расширенное сопоставление шаблонов (переключатели типов)
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

### Пользовательская упаковка ошибок
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

## Параллелизм и параллелизм (глубокое погружение)
### Шаблон пула рабочих
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

### Контекст отмены
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

### Выберите для мультиплексирования
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

## Конфигурация проекта и система сборки
### Структура проекта
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

### go.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Основные команды
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

### Конвейер CI/CD (действия GitHub)
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

## Тестирование
### Модульные тесты
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

### HTTP-тесты на основе таблиц
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

## Совместимость
### CGo (вызов C из Go)
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

### FFI с другими языками
| Направление | Механизм |
|-----------|-----------|
| Позвоните C | cgo (`import "C"`) |
| Звоните в C++ | cgo + функции-оболочки C |
| C вызывает Go | Экспортируйте функции Go с помощью`//export`|
| Вызовите Python | Используйте gopy или подпроцесс |
---

## Шаблоны проектирования
### Шаблон промежуточного программного обеспечения (HTTP)
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

### Шаблон опций
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

## Производительность и оптимизация
### Профилирование
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Советы по оптимизации
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

## Развертывание
### Кросс-компиляция
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Развертывание Docker
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

## Стандартная библиотека
| Пакет | Цель |
|---------|---------|
| ФМТ | Форматированный ввод-вывод |
| сеть/http | HTTP-клиент и сервер |
| кодировка/json | Кодирование/декодирование JSON |
| ОС | Операции на уровне ОС |
| ио | Примитивы ввода-вывода |
| строки / strconv | Манипулирование строками |
| синхронизировать | Мьютекс, группа ожидания, один раз |
| контекст | Сроки, отмена |
| тестирование | Встроенная среда тестирования |
| журнал / журнал/слог | Ведение журнала |
| время | Время и продолжительность |
| крипто | Криптография (TLS, хеширование) |
| база данных/sql | Абстракция базы данных |
---

## Инструменты
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

## Когда использовать Go
| Сценарий | Зачем идти | Лучшая альтернатива |
|----------|--------|-------------------|
| Облачные сервисы/микросервисы | Быстрые, небольшие двоичные файлы, отличный HTTP | Rust для максимальной производительности |
| Инструменты CLI | Быстрая компиляция, одиночный двоичный файл | Rust для сложных CLI |
| Веб-серверы/API | Встроенный HTTP, быстро, просто | Node.js/Express для быстрого прототипирования |
| Инструменты DevOps | Docker, Kubernetes, Terraform — это Go | Python для написания сценариев |
| Параллельные системы | Горутины легкие и элегантные | Erlang/Elixir для отказоустойчивого параллелизма |
| Сетевое программирование | Отличный чистый пакет | C/C++ для управления на самом низком уровне |
| Наука о данных / ML | Не та экосистема | Питон, Р |
| Графический интерфейс для настольных/мобильных устройств | Нет инфраструктуры графического интерфейса | Используйте веб-интерфейс или родной язык |
| Встраиваемые системы | Слишком тяжелый (GC, время выполнения) | С, Ржавчина |
---

## Синтетические вопросы и ответы
### В1: Почему в Go нет исключений? Как мне обрабатывать ошибки?
**A:** Go использует явные возвраты ошибок вместо исключений. Каждая функция, которая может завершиться неудачно, возвращает`error`в качестве своего последнего возвращаемого значения. Это заставляет вызывающую сторону явно обрабатывать ошибки — никаких скрытых сбоев или забытых блоков catch. Идиоматический шаблон — `if err != nil`. Используйте`fmt.Errorf`с`%w`для переноса ошибок и `errors.Is`/`errors.As` для проверки типов ошибок. Для неисправимых ошибок (ошибок программирования) используйте `panic`.
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

### Вопрос 2: Что такое горутины и чем они отличаются от потоков ОС?
**О:** Горутины — это легкие потоки пользовательского пространства, управляемые средой выполнения Go. Они начинаются с ~2 КБ стека (по сравнению с ~1 МБ для потоков ОС), планировщиком мультиплексируются в потоки ОС и могут создаваться миллионами за раз. Для связи между горутинами используются каналы (или примитивы`sync`для общего состояния). Всегда используйте`sync.WaitGroup`или отмену контекста, чтобы избежать утечек горутины.
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

### Вопрос 3. Когда для параллельного выполнения следует использовать каналы, а не мьютексы?
**A:** Используйте каналы, когда горутинам необходимо передавать данные — они реализуют философию «совместного использования памяти путем обмена данными». Используйте мьютексы (`sync.Mutex`), когда горутинам необходимо защитить общее состояние (кеши, счетчики, пулы соединений). Хорошее правило: если данные передаются между горутинами, используйте каналы; если к данным обращаются несколько горутин, используйте мьютекс. Для простых атомарных операций используйте `sync/atomic`.
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

### Q4: В чем разница между срезами/картами`nil`и пустыми?
**A:** Срез`nil`(`var s []int`) не имеет базового массива, длина 0, емкость 0. Пустой срез (`s := []int{}`или`make([]int, 0)`) имеет базовый массив, но длина 0. Оба работают одинаково с`append`,`len`,`cap`и `range`. Маршалинг JSON отличается: нулевые фрагменты становятся`null`, пустые фрагменты становятся`[]`. Лучшая практика: предпочитайте нулевые фрагменты для возвращаемых значений (они указывают «нет данных») и пустые фрагменты, когда важен вывод JSON.
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

### Q5: Как работают интерфейсы в Go и что такое пустой интерфейс?
**A:** Интерфейсы Go удовлетворяются неявно — тип реализует интерфейс, реализуя его методы, без ключевого слова `implements`. Это обеспечивает разделение и композицию. Пустой интерфейс`interface{}`(или`any`в Go 1.18+) подходит для любого типа — используйте его экономно (обобщенные интерфейсы часто лучше). Значения интерфейса представляют собой пары: `(type, value)`. В нулевом интерфейсе оба значения равны нулю.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создайте параллельный веб-скребок с ограничением скорости
**Постановка задачи.** Создайте программу на Go, которая одновременно извлекает URL-адреса из списка, извлекает заголовки страниц, соблюдает ограничение скорости в 10 запросов в секунду и собирает результаты без гонок за данными.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) одновременная выборка HTTP с помощью горутин, (2) ограничение скорости, чтобы избежать перегрузки серверов, (3) сбор результатов без гонок, (4) правильная обработка ошибок для неудачных запросов. Примитивы параллелизма Go (goroutines,channels,`errgroup`) идеально подходят для этого.
**Шаг 2. Определите подход:**
- Используйте`golang.org/x/time/rate`для ограничения скорости корзины токенов.
- Используйте`sync.WaitGroup`или`errgroup.Group`для управления горутинами.
- Используйте канал результатов для безопасного сбора результатов.
- Используйте`context.Context`для отмены и тайм-аутов.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Никаких гонок данных: каждая горутина записывает в свой собственный индекс в`results`— мьютекс не требуется.
-`errgroup.SetLimit`ограничивает параллелизм независимо от ограничителя скорости.
—`io.LimitReader`предотвращает чтение слишком больших страниц.
-`http.NewRequestWithContext`гарантирует отмену запросов после завершения контекста.
- Для производства: добавьте логику повторов с экспоненциальной задержкой, настройкой пула соединений и метриками.
### Проблема 2: реализация универсального кэша LRU
**Постановка проблемы:** Реализуйте в Go потокобезопасный универсальный кеш LRU (наименее недавно использованный), используя дженерики (Go 1.18+). Он должен поддерживать`Get`,`Set`и`Delete`с временной сложностью O(1).
**Шаг 1. Поймите проблему:**
Кэш LRU требует поиска O(1) (хеш-карта) и обновлений порядка O(1) (двусвязный список). На `Get`: переместите элемент на передний план. На `Set`: вставьте спереди; выселить сзади, если превышает вместимость. Потокобезопасность требует мьютекса.
**Шаг 2. Определите подход:**
- Используйте`container/list`(двухсвязный список) для O(1) перемещения вперед и удаления сзади.
- Используйте`map[K]*list.Element`для поиска O(1).
- Используйте`sync.Mutex`для обеспечения безопасности потоков.
— Обобщенные шаблоны (`[K comparable, V any]`) для обеспечения безопасности типов.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- O(1) для`Get`,`Set`,`Delete`: средний поиск по карте составляет O(1); Все операции со списками (`MoveToFront`,`PushFront`,`Remove`,`Back`) относятся к O(1).
- Потокобезопасность:`sync.Mutex`гарантирует, что только одна горутина обращается к кешу одновременно. Для рабочих нагрузок с большим объемом чтения используйте`sync.RWMutex`.
- Обобщенные:`[K comparable, V any]`обеспечивает поддержку ключей`==`(требуется для ключей карты), а значения могут быть любого типа.
- Производство: рассмотрите`github.com/hashicorp/golang-lru/v2`— проверенный в бою с поддержкой TTL и сегментированием для уменьшения конфликтов блокировок.
### Проблема 3. Создайте TCP-сервер чата
**Постановка задачи:** Создайте одновременный TCP-сервер чата, к которому клиенты смогут подключаться, транслировать сообщения всем другим подключенным клиентам и корректно отключаться. Обслуживайте медленных клиентов, не блокируя других.
**Шаг 1. Поймите проблему:**
Нам нужно: (1) принимать TCP-соединения, (2) одну горутину для чтения на каждого клиента, (3) широковещательный механизм для отправки сообщений всем клиентам, (4) обработку отключений и медленных клиентов. Это классический узор веера.
**Шаг 2. Определите подход:**
- Используйте`net.Listener`для TCP-соединений.
- Используйте центральную горутину`hub`с каналами регистрации/отмены регистрации/трансляции клиентов.
— Каждый клиент получает выделенную горутину записи с буферизованным каналом — медленные клиенты не блокируют других.
- Используйте`context.Context`для плавного завершения работы.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Медленная обработка клиента: широковещательная рассылка`select`с`default`предотвращает блокировку. Медленные клиенты отключаются, если их буфер заполняется.
- Никаких гонок: горутина хаба является единственным автором карты `clients`; `mu`защищает чтение во время трансляции.
- Грациозное завершение работы: добавьте`context.Context`и обработчик сигнала, чтобы закрыть соединения прослушивателя и стока.
- Производство: рассмотрите возможность использования`golang.org/x/net/websocket`для клиентов браузера и добавьте аутентификацию, историю сообщений и комнаты.
---

## Краткое содержание
Go — это язык, который сознательно предпочитает простоту функциональности. В нем меньше конструкций, чем в большинстве языков — нет наследования, нет перегрузки методов, нет исключений, нет макросов — и в этом его преимущество. В результате получается код, который легко читать, легко писать и легко поддерживать. Модель параллелизма Go (горутины и каналы) — одна из лучших на любом языке. Go — отличный выбор для облачной инфраструктуры, микросервисов, инструментов CLI и сетевого программирования.