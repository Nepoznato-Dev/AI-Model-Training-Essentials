---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [c, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C
C to proceduralny język programowania ogólnego przeznaczenia stworzony przez Dennisa Ritchiego w Bell Labs w latach 1969–1973. Został zaprojektowany do implementacji systemu operacyjnego Unix i ponad 50 lat później pozostaje jednym z najczęściej używanych języków programowania. C zapewnia niski poziom dostępu do pamięci, minimalną standardową bibliotekę i przejrzyste mapowanie do instrukcji maszynowych – co czyni go podstawą, na której zbudowana jest większość współczesnych komputerów.
C to język systemów operacyjnych (Linux, jądro Windows, macOS), systemów wbudowanych, silników baz danych (SQLite, PostgreSQL), kompilatorów (CPython w Pythonie, MRI Ruby) i praktycznie każdego innego środowiska wykonawczego języka programowania. Zrozumienie C oznacza zrozumienie, jak faktycznie działają komputery.
---

## Dlaczego C ma znaczenie
- **Bliskość sprzętu**: C odwzorowuje kod maszynowy. Nie ma modułu zbierającego elementy bezużyteczne, żadnych narzutów w czasie wykonywania, żadnych ukrytych alokacji.
- **Wszechobecność**: od mikrokontrolerów po superkomputery, język C działa wszędzie.
- **Podstawy informatyki**: Linux, Windows, jądra macOS, interpreter Pythona, SQLite, Git – wszystko napisane w C.
- **Wydajność**: Prawie optymalna prędkość wykonywania z pełną kontrolą nad układem pamięci.
- **Wpływ**: składnia i koncepcje języka C (wskaźniki, tablice, struktury, funkcje) ukształtowały C++, Java, C#, JavaScript, Go, Rust i większość późniejszych języków.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Ręczne zarządzanie pamięcią** | Brak modułu zbierającego elementy bezużyteczne – sam przydzielasz i zwalniasz pamięć | Ostrożne korzystanie z malloc/free; Wzorce RAII w C++ |
| **Przepełnienia bufora** | Brak sprawdzania granic na tablicach - łatwe zapisywanie poza końcami buforów | Użyj strncpy zamiast strcpy; włącz ostrzeżenia kompilatora |
| **Brak wbudowanego OOP** | Tylko proceduralne — bez klas, dziedziczenia i metod | Użyj struktur + wskaźników funkcji; lub przejdź do C++ |
| **Ograniczona biblioteka standardowa** | Minimalna wbudowana funkcjonalność | Biblioteki stron trzecich lub napisz własne |
| **Nieokreślone zachowanie** | Wiele błędów kompiluje się dobrze, ale zawiesza się w nieprzewidywalny sposób | Używaj środków dezynfekcyjnych, analizatorów statycznych |
---

## Podstawy składni
### Podstawowa struktura
Każdy program C zaczyna się od`main()`. Język jest kompilowany — kod źródłowy staje się kodem maszynowym za pomocą kompilatora (GCC, Clang, MSVC).
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int result = add(3, 5);
    printf("Result: %d\n", result);
    return 0;
}
```

### Zmienne i typy
C jest typem statycznym — każda zmienna ma stały typ znany w czasie kompilacji.
```c
int count = 42;              // 4 bytes (typically)
float pi = 3.14159f;         // 4 bytes
double precise = 3.14159;    // 8 bytes
char letter = 'A';           // 1 byte
long big = 1000000L;         // 4 or 8 bytes depending on platform

#define MAX_SIZE 1024
const float GRAVITY = 9.81f;

int numbers[5] = {1, 2, 3, 4, 5};
char name[] = "Hello";       // Size inferred: 6 bytes (includes \0)

struct Point {
    float x;
    float y;
};
struct Point p;
p.x = 3.0f;
p.y = 4.0f;
```

### Wskazówki
Wskaźniki są najpotężniejszą i najbardziej niezrozumianą funkcją języka C. Wskaźnik przechowuje adres pamięci.
```c
int value = 42;
int *ptr = &value;     // ptr holds the address of value

printf("%d\n", *ptr);  // Dereference: prints 42
printf("%p\n", ptr);   // Prints the memory address

// Pointers and arrays are closely related
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;          // p points to arr[0]
printf("%d\n", *(p+2)); // prints 30 (arr[2])

// Dynamic memory allocation
int *dynamic = (int *)malloc(10 * sizeof(int));
if (dynamic == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1);
}
dynamic[0] = 100;
free(dynamic);   // Always free what you malloc!
dynamic = NULL;  // Prevent use-after-free
```

### Przepływ sterowania
```c
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}

for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

while (running) {
    process_input();
}

do {
    check_status();
} while (status == PENDING);

switch (command) {
    case START:   run();     break;
    case STOP:    halt();    break;
    case PAUSE:   suspend(); break;
    default:      printf("Unknown command\n");
}
```

### Funkcje i stos
```c
// Pass by value (default)
void increment(int x) {
    x++;  // Only modifies the local copy
}

// Pass by pointer -- function can modify the original
void increment_ptr(int *x) {
    (*x)++;
}

// Variadic functions (like printf)
#include <stdarg.h>
double average(int count, ...) {
    va_list args;
    va_start(args, count);
    double sum = 0;
    for (int i = 0; i < count; i++) {
        sum += va_arg(args, double);
    }
    va_end(args);
    return sum / count;
}
```

---

## Układ pamięci
```
+---------------------+ High addresses
|     Stack           | <- Local variables, function call frames
|       | grows       |   (automatically cleaned up when function returns)
+---------------------+
|       | grows       |
|      Heap           | <- malloc/calloc allocations
|                     |   (you must free() these manually)
+---------------------+
|  BSS segment        | <- Uninitialised global/static variables
+---------------------+
|  Data segment       | <- Initialised global/static variables
+---------------------+
|  Text segment       | <- Compiled machine code (read-only)
+---------------------+ Low addresses
```

| Region | Co tam się dzieje | Całe życie | Kto tym zarządza |
|------------|----------------|---------|----------------|
| **Stos** | Zmienne lokalne, parametry funkcji | Dopóki funkcja nie zwróci | Kompilator (automatyczny) |
| **Sterta** | przydziały malloc/calloc | Dopóki nie wywołasz funkcji free() | Ty (instrukcja) |
| **Dane/BSS** | Zmienne globalne i statyczne | Cały czas trwania programu | Kompilator (automatyczny) |
| **Tekst** | Kod maszynowy | Cały czas trwania programu | Tylko do odczytu |
---

## Biblioteka standardowa
| Nagłówek | Cel | Wspólne funkcje |
|--------|---------|--------------------------------|
| `<stdio.h>`| Wejście/wyjście | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Narzędzia ogólne | malloc, bezpłatny, wyjdź, atoi, rand, qsort |
| `<string.h>`| Operacje na ciągach | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matematyka | grzech, cos, sqrt, pow, fabs, ceil, podłoga |
| `<ctype.h>`| Klasyfikacja postaci | isalpha, isdigit, toupper, toniższy |
| `<time.h>`| Data i godzina | czas, zegar, czas różnicowy, czas strftime |
| `<assert.h>`| Debugowanie twierdzeń | twierdzić (warunek) |
| `<errno.h>`| Kody błędów | errno, perror, strerror |
---

## Zaawansowana składnia i wzorce
### Makra preprocesora
```c
// Safe macro with do-while wrapper
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Conditional compilation
#ifdef DEBUG
    #define LOG(fmt, ...) fprintf(stderr, fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) ((void)0)
#endif

// Stringify and concatenation
#define STR(x) #x
#define CONCAT(a, b) a##b
```

### Wskaźniki funkcji i wywołania zwrotne
```c
#include <stdio.h>

// Function pointer type
typedef int (*Comparator)(const void *, const void *);

// Using function pointers for callbacks
int ascending(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int descending(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void) {
    int data[] = {5, 2, 8, 1, 9, 3};
    int n = ARRAY_LEN(data);

    // qsort uses function pointers for custom comparison
    qsort(data, n, sizeof(int), ascending);
    print_array(data, n);  // 1 2 3 5 8 9

    qsort(data, n, sizeof(int), descending);
    print_array(data, n);  // 9 8 5 3 2 1

    return 0;
}
```

### Niestandardowe wzorce obsługi błędów
```c
#include <stdio.h>
#include <stdlib.h>

// Error code enum
typedef enum {
    ERR_OK = 0,
    ERR_NULL_PTR = -1,
    ERR_ALLOC = -2,
    ERR_IO = -3,
    ERR_INVALID_ARG = -4,
} ErrorCode;

// Error string lookup
const char *error_string(ErrorCode code) {
    switch (code) {
        case ERR_OK:           return "Success";
        case ERR_NULL_PTR:     return "Null pointer";
        case ERR_ALLOC:        return "Allocation failed";
        case ERR_IO:           return "IO error";
        case ERR_INVALID_ARG:  return "Invalid argument";
        default:               return "Unknown error";
    }
}

// Error propagation pattern (goto cleanup)
ErrorCode process_file(const char *path) {
    FILE *fp = NULL;
    char *buffer = NULL;
    ErrorCode err = ERR_OK;

    if (path == NULL) { err = ERR_NULL_PTR; goto cleanup; }

    fp = fopen(path, "r");
    if (!fp) { err = ERR_IO; goto cleanup; }

    buffer = (char *)malloc(4096);
    if (!buffer) { err = ERR_ALLOC; goto cleanup; }

    // ... process file ...

cleanup:
    free(buffer);
    if (fp) fclose(fp);
    if (err != ERR_OK)
        fprintf(stderr, "Error: %s\n", error_string(err));
    return err;
}
```

---

## Współbieżność i równoległość
### Wątki POSIX (pthreads)
```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// Thread function
void *worker(void *arg) {
    int id = *(int *)arg;
    printf("Thread %d running\n", id);
    return NULL;
}

int main(void) {
    pthread_t threads[5];
    int ids[5];

    for (int i = 0; i < 5; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

### Mutex i stan współdzielony
```c
#include <pthread.h>

typedef struct {
    int count;
    pthread_mutex_t lock;
} Counter;

void *increment(void *arg) {
    Counter *c = (Counter *)arg;
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&c->lock);
        c->count++;
        pthread_mutex_unlock(&c->lock);
    }
    return NULL;
}

int main(void) {
    Counter counter = {0, PTHREAD_MUTEX_INITIALIZER};
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, &counter);
    pthread_create(&t2, NULL, increment, &counter);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Final count: %d\n", counter.count);
    pthread_mutex_destroy(&counter.lock);
    return 0;
}
```

### C11 Atomy i wątki
```c
#include <stdatomic.h>
#include <threads.h>

atomic_int shared_count = 0;

int worker(void *arg) {
    for (int i = 0; i < 1000; i++) {
        atomic_fetch_add(&shared_count, 1);
    }
    return 0;
}

int main(void) {
    thrd_t t1, t2;
    thrd_create(&t1, worker, NULL);
    thrd_create(&t2, worker, NULL);
    thrd_join(t1, NULL);
    thrd_join(t2, NULL);
    printf("Count: %d\n", atomic_load(&shared_count));
    return 0;
}
```

---

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
```
my_project/
+-- CMakeLists.txt        # CMake build configuration
+-- Makefile              # Alternative: Make build
+-- src/
|   +-- main.c
|   +-- utils.c
|   +-- utils.h
|   +-- parser.c
|   +-- parser.h
+-- include/
|   +-- config.h
|   +-- types.h
+-- tests/
|   +-- test_utils.c
|   +-- test_parser.c
+-- lib/                  # Third-party libraries
+-- build/                # Build output (gitignored)
+-- .clang-format         # Code style configuration
+-- .clang-tidy           # Linter configuration
```

### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project VERSION 1.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Compiler warnings
add_compile_options(-Wall -Wextra -Wpedantic)

# Source files
set(SOURCES
    src/main.c
    src/utils.c
    src/parser.c
)

# Main executable
add_executable(my_app ${SOURCES})
target_include_directories(my_app PRIVATE include)

# Link math library on Unix
if(UNIX)
    target_link_libraries(my_app m pthread)
endif()

# Release build optimisation
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_options(my_app PRIVATE -O2)
endif()

# Testing
enable_testing()
add_executable(test_utils tests/test_utils.c src/utils.c)
target_include_directories(test_utils PRIVATE include)
add_test(NAME UtilsTest COMMAND test_utils)
```

### Plik Makefile
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -std=c17 -Iinclude
LDFLAGS = -lm -lpthread

SRCS = src/main.c src/utils.c src/parser.c
OBJS = $(SRCS:.c=.o)
TARGET = my_app

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	find . -name "*.o" -delete
	find . -name "$(TARGET)" -delete

debug: CFLAGS += -g -DDEBUG -fsanitize=address
debug: clean all

.PHONY: all clean debug
```

### Potok CI/CD (akcje w GitHub)
```yaml
name: C CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: cmake -B build -DCMAKE_BUILD_TYPE=Debug
      - run: cmake --build build
      - run: ctest --test-dir build --output-on-failure
```

---

## Testowanie
### Testowanie jednostkowe z prostą strukturą
```c
#include <stdio.h>
#include <assert.h>
#include "utils.h"

// Simple test macros
#define TEST(name) void name(void)
#define ASSERT_EQ(a, b) do { \
    if ((a) != (b)) { \
        fprintf(stderr, "FAIL: %s:%d: %d != %d\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

#define ASSERT_STR_EQ(a, b) do { \
    if (strcmp((a), (b)) != 0) { \
        fprintf(stderr, "FAIL: %s:%d: \"%s\" != \"%s\"\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

TEST(test_add) {
    ASSERT_EQ(add(2, 3), 5);
    ASSERT_EQ(add(-1, 1), 0);
    ASSERT_EQ(add(0, 0), 0);
}

TEST(test_string_trim) {
    char buf[64];
    strcpy(buf, "  hello  ");
    trim(buf);
    ASSERT_STR_EQ(buf, "hello");
}

int main(void) {
    test_add();
    printf("test_add passed\n");
    test_string_trim();
    printf("test_string_trim passed\n");
    printf("All tests passed!\n");
    return 0;
}
```

```bash
# Compile and run tests
gcc -Wall -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils

# Run with AddressSanitizer
gcc -fsanitize=address -g -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils
```

---

## Interoperacyjność
### Wywoływanie C z Pythona (ctypes)
```c
// mathlib.c -- compile to shared library
// gcc -shared -fPIC -o libmathlib.so mathlib.c
int c_add(int a, int b) { return a + b; }
double c_sqrt(double x) {
    if (x < 0) return -1.0;
    // Newton's method
    double guess = x / 2.0;
    for (int i = 0; i < 100; i++)
        guess = (guess + x / guess) / 2.0;
    return guess;
}
```

```python
# Python side
import ctypes
lib = ctypes.CDLL("./libmathlib.so")
lib.c_add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_add.restype = ctypes.c_int
print(lib.c_add(3, 5))  # 8
```

### Wywoływanie C z innych języków
| Język | Mechanizm | Przykład |
|---------|-----------|---------|
| Pythona | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| Rubin | Skrzypce | `Fiddle.dlopen("./lib.so")`|
| Jawa | JNI | `System.loadLibrary("mylib")`|
| C++ | zewnętrzne „C” | `extern "C" void my_func();`|
| Rdza | zewnętrzne „C” + FFI | `extern "C" { fn my_func(); }`|
---

## Wzorce projektowe
### Nieprzezroczysty wskaźnik (idiom Pimpl w C)
```c
// stack.h -- public interface (implementation hidden)
typedef struct Stack Stack;

Stack *stack_create(void);
void stack_destroy(Stack *s);
void stack_push(Stack *s, int value);
int stack_pop(Stack *s);
int stack_is_empty(const Stack *s);

// stack.c -- private implementation
struct Stack {
    int *data;
    int top;
    int capacity;
};

Stack *stack_create(void) {
    Stack *s = malloc(sizeof(Stack));
    s->data = malloc(16 * sizeof(int));
    s->top = -1;
    s->capacity = 16;
    return s;
}

void stack_push(Stack *s, int value) {
    if (++s->top == s->capacity) {
        s->capacity *= 2;
        s->data = realloc(s->data, s->capacity * sizeof(int));
    }
    s->data[s->top] = value;
}
```

### Wirtualny stół (OOP w C)
```c
typedef struct {
    void (*speak)(const void *self);
    void (*destroy)(void *self);
} AnimalVTable;

typedef struct {
    const AnimalVTable *vtable;
    char name[64];
} Animal;

void animal_speak(const Animal *a) { a->vtable->speak(a); }

// Dog implementation
typedef struct { Animal base; int trick_count; } Dog;
void dog_speak(const void *self) { printf("Woof!\n"); }
void dog_destroy(void *self) { free(self); }

static const AnimalVTable dog_vtable = { dog_speak, dog_destroy };
Animal *dog_create(const char *name) {
    Dog *d = calloc(1, sizeof(Dog));
    d->base.vtable = &dog_vtable;
    strncpy(d->base.name, name, 63);
    return (Animal *)d;
}
```

---

## Wydajność i optymalizacja
### Narzędzia do profilowania
```bash
# GCC profiling with gprof
gcc -pg -O2 -o my_app main.c
./my_app
gprof my_app gmon.out > profile.txt

# perf (Linux)
perf record -g ./my_app
perf report

# Valgrind for cache profiling
valgrind --tool=cachegrind ./my_app

# Memory leak detection
valgrind --tool=memcheck --leak-check=full ./my_app

# AddressSanitizer (compile-time)
gcc -fsanitize=address,undefined -g -o my_app main.c
```

### Techniki optymalizacji
```c
// Struct packing to reduce memory
#pragma pack(push, 1)
typedef struct {
    uint8_t type;
    uint32_t id;
    uint16_t value;
} PackedRecord;  // 7 bytes instead of 12 (with padding)
#pragma pack(pop)

// Cache-friendly access patterns (row-major order)
for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
        matrix[i][j] = 0;  // Sequential memory access

// Branch prediction hints
#define LIKELY(x)   __builtin_expect(!!(x), 1)
#define UNLIKELY(x) __builtin_expect(!!(x), 0)

if (LIKELY(ptr != NULL)) {
    // Fast path
}
```

---

## Zastosowanie
### Kompilacja krzyżowa
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Wdrożenie Dockera
```dockerfile
FROM gcc:13 AS builder
WORKDIR /app
COPY src/ ./
RUN gcc -O2 -Wall -o my_app main.c utils.c

FROM debian:bookworm-slim
COPY --from=builder /app/my_app /usr/local/bin/my_app
CMD ["my_app"]
```

---

## Typowe wzorce i idiomy
```c
// Safe string copy (prevents buffer overflow)
#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Macro for array length
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

// Typedef for cleaner struct usage
typedef struct {
    float x, y, z;
} Vec3;

// Linked list node
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

---

## Kompilacja i oprzyrządowanie
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Narzędzie | Cel |
|------|-------------|
| **GCC / Brzęk** | Kompilatory |
| **Utwórz / CMake** | Buduj systemy |
| **GDB** | Debuger |
| **Valgrind** | Detektor błędów pamięci (wycieki, nieprawidłowy dostęp) |
| **Adres środka dezynfekującego** | Sprawdzanie pamięci w czasie kompilacji |
| **cppcheck** | Analiza statyczna |
| **format brzęku** | Formatowanie kodu |
---

## Kiedy używać C
| Scenariusz | Dlaczego C | Lepsza alternatywa |
|---------|-------|--------------------------------|
| Systemy operacyjne | Bezpośredni dostęp do sprzętu, bez narzutów na czas wykonania | -- |
| Systemy wbudowane / mikrokontrolery | Minimalna powierzchnia, działa na wszystkim | Rdza do osadzonych elementów krytycznych dla bezpieczeństwa |
| Silniki baz danych | Maksymalna wydajność, pełna kontrola pamięci | -- |
| Kompilatory i interpretery | Szybki, przenośny, dobrze zrozumiany | C++ dla większych projektów kompilatorów |
| Sterowniki urządzeń | Wymagane przez większość interfejsów API jądra systemu operacyjnego | -- |
| Biblioteki krytyczne pod względem wydajności | Prawie optymalna prędkość | Rdza gwarantująca bezpieczeństwo pamięci |
| Ogólne tworzenie aplikacji | Za dużo pracy ręcznej | Python, Java, Go, C# |
| Tworzenie stron internetowych | Całkowicie niewłaściwe narzędzie | JavaScript, Go, Python |
| Nauka o danych / ML | Nie ma do tego ekosystemu | Python, R, Julia |
---

## Standardy C
| Standardowe | Rok | Kluczowe dodatki |
|---------|------|-------------|
| C89/C90 | 1989/1990 | Oryginalny ANSI C – nadal podstawa |
| C99 | 1999 | // komentarze, typ bool, tablice o zmiennej długości, inline, stdint.h |
| C11 | 2011 | Operacje atomowe, wątki, struktury anonimowe, _Generic |
| C17 | 2018 | Poprawki błędów i wyjaśnienia (brak nowych funkcji) |
| C23 | 2024 | nullptr, typeof, constexpr, ulepszony preprocesor |
Większość kodu produkcyjnego jest przeznaczona dla C11 lub C17. C23 zapewnia nowoczesne udogodnienia, ale wdrożenie wymaga czasu.
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między wskaźnikami a tablicami w C?
**O:** Tablice i wskaźniki są powiązane, ale różne. Tablica to ciągły blok pamięci o stałym rozmiarze znanym w czasie kompilacji. Wskaźnik to zmienna przechowująca adres pamięci. Tablice rozpadają się na wskaźniki po przekazaniu do funkcji, ale`sizeof(array)`podaje całkowity rozmiar, podczas gdy`sizeof(pointer)`podaje tylko rozmiar wskaźnika (4 lub 8 bajtów). Nazwy tablic nie są modyfikowalnymi wartościami — nie można wykonać`arr++`.
```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;       // Array decays to pointer to first element

printf("%zu\n", sizeof(arr));   // 20 (5 * sizeof(int))
printf("%zu\n", sizeof(ptr));   // 8 (on 64-bit system)

// arr++;        // Error: array is not a modifiable lvalue
ptr++;           // OK: pointer arithmetic

// They behave the same for indexing
printf("%d\n", arr[2]);   // 3
printf("%d\n", ptr[2]);   // 3
printf("%d\n", *(arr + 2)); // 3 — pointer arithmetic
```

### P2: Jak prawidłowo zarządzać pamięcią i unikać wycieków?
**A:** Każdy`malloc`/`calloc`musi mieć odpowiedni`free`. Typowe błędy: zapomnienie o zwolnieniu (wyciek), dwukrotne zwolnienie (niezdefiniowane zachowanie), użycie pamięci po zwolnieniu (użycie po zwolnieniu) i niezatwierdzenie zwracanej wartości`malloc`(NULL w przypadku niepowodzenia). Najlepsza praktyka: przydzielaj i zwalniaj w tym samym module, używaj wzorca „goto cleanup” do obsługi błędów i zawsze ustawiaj zwolnione wskaźniki na NULL.
```c
// Proper allocation pattern with cleanup
char *load_file(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buf = malloc(size + 1);
    if (!buf) {
        fclose(f);
        return NULL;
    }

    if (fread(buf, 1, size, f) != (size_t)size) {
        free(buf);
        buf = NULL;   // Prevent dangling pointer
        fclose(f);
        return NULL;
    }
    buf[size] = '\0';

    fclose(f);
    return buf;
}

// Usage
char *data = load_file("config.txt");
if (data) {
    process(data);
    free(data);
    data = NULL;  // Defensive: catch use-after-free
}
```

### P3: Jakie są najlepsze praktyki dotyczące obsługi błędów w języku C?
**A:** C nie ma wyjątków. Obsługa błędów wykorzystuje wartości zwracane (kody błędów, wskaźniki NULL, wartości ujemne). Standardowy wzorzec: funkcje zwracają kod stanu lub NULL w przypadku niepowodzenia i ustawiają`errno`dla wywołań systemowych. Użyj wzorca „goto cleanup” do czyszczenia zasobów w przypadku błędów. Zawsze sprawdzaj zwracane wartości`malloc`,`fopen`i inne funkcje, które mogą zakończyć się niepowodzeniem.
```c
#include <errno.h>
#include <string.h>

// Error code pattern
typedef enum {
    OK = 0,
    ERR_NULL_PTR = -1,
    ERR_NOT_FOUND = -2,
    ERR_IO = -3,
} Status;

Status read_config(const char *path, Config *out) {
    if (!path || !out) return ERR_NULL_PTR;

    FILE *f = fopen(path, "r");
    if (!f) {
        fprintf(stderr, "Cannot open %s: %s\n", path, strerror(errno));
        return ERR_IO;
    }

    // ... parse config ...

    fclose(f);
    return OK;
}

// Usage
Config cfg;
Status s = read_config("app.conf", &cfg);
if (s != OK) {
    fprintf(stderr, "Config error: %d\n", s);
    exit(EXIT_FAILURE);
}
```

### P4: Czym struktury, unie i pola bitowe różnią się pod względem układu pamięci?
**A:** Konstrukcje układają elementy sekwencyjnie z możliwym uzupełnieniem w celu wyrównania. Unie nakładają się na wszystkie elementy w tym samym miejscu pamięci — rozmiar jest równy największemu elementowi. Pola bitowe pakują wiele wartości w jedną liczbę całkowitą. Struktury służą do heterogenicznych danych, unie do rozróżniania typów lub oszczędzania miejsca, gdy aktywne jest tylko jedno pole, a pola bitowe do kompaktowego przechowywania flag.
```c
// Struct — sequential layout with padding
struct Point {
    double x;  // offset 0, 8 bytes
    double y;  // offset 8, 8 bytes
};               // sizeof = 16

// Union — overlapping storage
union Value {
    int    i;
    float  f;
    char   s[8];
};               // sizeof = 8 (largest member)

// Tagged union — safe union usage
typedef enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } ValueType;

struct TaggedValue {
    ValueType type;
    union {
        int   i;
        float f;
        char  s[32];
    } data;
};

// Bitfields — pack flags into minimal space
struct Flags {
    unsigned int read    : 1;  // 1 bit
    unsigned int write   : 1;
    unsigned int execute : 1;
    unsigned int sticky  : 1;
    unsigned int reserved : 4;  // 4 bits padding
};  // Total: 1 byte instead of 4 ints
```

### P5: Co to są wskaźniki funkcji i kiedy należy ich używać?
**O:** Wskaźniki funkcji przechowują adres funkcji i umożliwiają wywołania zwrotne, polimorfizm i architekturę wtyczek. Stanowią one podstawę podejścia C do funkcji wyższego rzędu (takich jak`qsort`,`bsearch`). Zadeklaruj je za pomocą składni:`return_type (*name)(parameter_types)`.
```c
// Function pointer declaration
int (*operation)(int, int);

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

operation = add;
printf("%d\n", operation(3, 4));  // 7
operation = mul;
printf("%d\n", operation(3, 4));  // 12

// Callback pattern — qsort
int compare_ints(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int arr[] = {5, 2, 8, 1, 9, 3};
qsort(arr, 6, sizeof(int), compare_ints);
// arr is now {1, 2, 3, 5, 8, 9}

// Strategy pattern
struct Strategy {
    void (*init)(void);
    void (*process)(const char *data);
    void (*cleanup)(void);
};

void run_pipeline(const struct Strategy *s, const char *data) {
    s->init();
    s->process(data);
    s->cleanup();
}
```

---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zaimplementuj tablicę dynamiczną (wektorową)
**Opis problemu:** Zaimplementuj dynamiczną tablicę w C, która automatycznie rośnie po dodaniu elementów, obsługuje amortyzowane dołączanie O(1) i zapewnia odpowiednie czyszczenie. Jest to odpowiednik języka C++`std::vector`w języku C.
**Krok 1 — Zrozum problem:**
Tablica dynamiczna wymaga: (1) bufora przydzielonego do sterty, (2) śledzenia rozmiaru (używane elementy) i pojemności (przydzielone miejsca), (3) ponownej alokacji, gdy rozmiar osiągnie pojemność, (4) odpowiedniego czyszczenia pamięci. Współczynnik wzrostu 2x daje zamortyzowany dodatek O(1).
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`malloc`do początkowej alokacji,`realloc`do wzrostu.
- Przechowuj wskaźnik danych, rozmiar i pojemność w strukturze.
- Rozwijaj się, podwajając pojemność, gdy`size == capacity`.
- Zapewnij operacje`push`,`pop`,`get`,`set`i `free`.
**Krok 3 — Wdróż rozwiązanie:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int    *data;
    size_t  size;
    size_t  capacity;
} IntVec;

// Initialize with default capacity
void vec_init(IntVec *v, size_t initial_capacity) {
    v->data = malloc(initial_capacity * sizeof(int));
    if (!v->data) { perror("malloc"); exit(EXIT_FAILURE); }
    v->size = 0;
    v->capacity = initial_capacity;
}

// Ensure capacity for at least one more element
static void vec_grow(IntVec *v) {
    if (v->size < v->capacity) return;
    size_t new_cap = v->capacity * 2;
    int *new_data = realloc(v->data, new_cap * sizeof(int));
    if (!new_data) { perror("realloc"); exit(EXIT_FAILURE); }
    v->data = new_data;
    v->capacity = new_cap;
}

// Append element — O(1) amortized
void vec_push(IntVec *v, int value) {
    vec_grow(v);
    v->data[v->size++] = value;
}

// Remove last element — O(1)
int vec_pop(IntVec *v) {
    if (v->size == 0) { fprintf(stderr, "pop from empty vector\n"); exit(EXIT_FAILURE); }
    return v->data[--v->size];
}

// Access element
int vec_get(const IntVec *v, size_t index) {
    if (index >= v->size) { fprintf(stderr, "index %zu out of bounds (size %zu)\n", index, v->size); exit(EXIT_FAILURE); }
    return v->data[index];
}

// Free all memory
void vec_free(IntVec *v) {
    free(v->data);
    v->data = NULL;
    v->size = v->capacity = 0;
}

// Usage
int main(void) {
    IntVec v;
    vec_init(&v, 4);

    for (int i = 0; i < 100; i++) {
        vec_push(&v, i * i);
    }

    printf("Size: %zu, Capacity: %zu\n", v.size, v.capacity);
    printf("Last: %d\n", vec_get(&v, v.size - 1));  // 9801

    vec_free(&v);
    return 0;
}
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Amortyzowane wypychanie O(1): podwojenie oznacza, że każdy element jest kopiowany łącznie maksymalnie O(log n) razy.
- Sprawdzanie granic w`vec_get`i`vec_pop`wcześnie wychwytuje błędy — jest to niezbędne w C, gdzie nie ma siatki bezpieczeństwa w czasie wykonywania.
- Pamięć: po 100 naciśnięciach, zaczynając od pojemności 4, pojemność osiąga 128 (4 → 8 → 16 → 32 → 64 → 128).
- Produkcja: użyj`shrink_to_fit`(realokacja do dokładnego rozmiaru) po zakończeniu powiększania, aby odzyskać nieużywaną pamięć.
### Problem 2: Zbuduj prostą tabelę mieszającą
**Opis problemu:** Zaimplementuj tabelę skrótów z kluczami łańcuchowymi i wartościami całkowitymi, używając oddzielnego łączenia łańcuchowego w celu rozwiązania kolizji. Obsługa operacji wstawiania, wyszukiwania i usuwania.
**Krok 1 — Zrozum problem:**
Tabela skrótów odwzorowuje klucze na indeksy tablicy za pomocą funkcji skrótu. Kolizje (różne klucze przypisane do tego samego indeksu) są rozwiązywane za pomocą oddzielnego łączenia w łańcuch: każdy segment jest połączoną listą wpisów. Potrzebujemy: funkcji skrótu, wstawiania, wyszukiwania, usuwania i czyszczenia.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj skrótu FNV-1a, aby zapewnić dobrą dystrybucję kluczy łańcuchowych.
- Tablica wskaźników segmentów (połączone głowy list).
- Śledzenie współczynnika obciążenia; zmienić rozmiar, gdy współczynnik obciążenia przekracza próg.
- Wszystkie operacje to średnia O(1), najgorszy przypadek O(n).
**Krok 3 — Wdróż rozwiązanie:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_BUCKETS 64
#define LOAD_FACTOR_THRESHOLD 0.75

typedef struct Entry {
    char *key;
    int   value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry  **buckets;
    size_t   num_buckets;
    size_t   size;
} HashMap;

// FNV-1a hash function
static unsigned long hash(const char *key) {
    unsigned long h = 14695981039346656037ULL;
    while (*key) {
        h ^= (unsigned char)*key++;
        h *= 1099511628211ULL;
    }
    return h;
}

void hashmap_init(HashMap *m) {
    m->num_buckets = INITIAL_BUCKETS;
    m->buckets = calloc(m->num_buckets, sizeof(Entry *));
    m->size = 0;
}

// Insert or update
void hashmap_put(HashMap *m, const char *key, int value) {
    size_t idx = hash(key) % m->num_buckets;

    // Check if key already exists
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            e->value = value;
            return;
        }
    }

    // New entry — prepend to bucket
    Entry *entry = malloc(sizeof(Entry));
    entry->key = strdup(key);
    entry->value = value;
    entry->next = m->buckets[idx];
    m->buckets[idx] = entry;
    m->size++;
}

// Lookup — returns 1 if found, 0 if not
int hashmap_get(const HashMap *m, const char *key, int *out_value) {
    size_t idx = hash(key) % m->num_buckets;
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            *out_value = e->value;
            return 1;
        }
    }
    return 0;
}

// Delete — returns 1 if removed, 0 if not found
int hashmap_remove(HashMap *m, const char *key) {
    size_t idx = hash(key) % m->num_buckets;
    Entry **pp = &m->buckets[idx];

    while (*pp) {
        if (strcmp((*pp)->key, key) == 0) {
            Entry *to_free = *pp;
            *pp = to_free->next;
            free(to_free->key);
            free(to_free);
            m->size--;
            return 1;
        }
        pp = &(*pp)->next;
    }
    return 0;
}

// Cleanup
void hashmap_free(HashMap *m) {
    for (size_t i = 0; i < m->num_buckets; i++) {
        Entry *e = m->buckets[i];
        while (e) {
            Entry *next = e->next;
            free(e->key);
            free(e);
            e = next;
        }
    }
    free(m->buckets);
    m->buckets = NULL;
    m->size = m->num_buckets = 0;
}

// Usage
int main(void) {
    HashMap m;
    hashmap_init(&m);

    hashmap_put(&m, "alice", 95);
    hashmap_put(&m, "bob", 87);
    hashmap_put(&m, "charlie", 92);

    int score;
    if (hashmap_get(&m, "alice", &score)) {
        printf("Alice: %d\n", score);  // Alice: 95
    }

    hashmap_remove(&m, "bob");
    hashmap_free(&m);
    return 0;
}
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Średnia O(1) dla wstawiania/wyszukiwania/usuwania z dobrą funkcją skrótu i rozsądnym współczynnikiem obciążenia.
- FNV-1a zapewnia doskonałą dystrybucję kluczy łańcuchowych przy minimalnych obliczeniach.
- Technika wskaźnik-wskaźnik (`Entry **pp`) w`hashmap_remove`elegancko obsługuje usuwanie zarówno początku listy, jak i środkowej listy, bez specjalnych przypadków.
- Produkcja: dodaj ponowne mieszanie, gdy współczynnik obciążenia przekracza próg. Użyj otwartego adresowania (sondowanie liniowe), aby uzyskać lepszą wydajność pamięci podręcznej.
### Problem 3: Zaimplementuj bufor pierścieniowy dla producenta-konsumenta
**Opis problemu:** Zaimplementuj wolny od blokad bufor pierścieniowy jednego producenta i jednego konsumenta w języku C, aby zapewnić wysoką wydajność komunikacji między wątkami bez dynamicznej alokacji podczas działania.
**Krok 1 — Zrozum problem:**
Bufor pierścieniowy (bufor kołowy) wykorzystuje tablicę o stałym rozmiarze z indeksami odczytu i zapisu. Gdy bufor jest pełny, moduł zapisujący blokuje lub nadpisuje. W przypadku SPSC (single-producer single-consumer) zamiast blokad możemy zastosować operacje atomowe, aby uzyskać maksymalną przepustowość.
**Krok 2 — Zidentyfikuj podejście:**
- Tablica o stałym rozmiarze przydzielana raz podczas inicjalizacji.
-`head`(pozycja odczytu) i`tail`(pozycja zapisu) jako indeksy atomowe.
- Zaliczki producenta`tail`; zaliczki konsumenckie`head`.
- Bufor jest pusty, gdy`head == tail`; pełny, gdy`(tail + 1) % capacity == head`.
- Użyj atomów C11 z odpowiednim uporządkowaniem pamięci.
**Krok 3 — Wdróż rozwiązanie:**
```c
#include <stdio.h>
#include <stdatomic.h>
#include <stdlib.h>
#include <string.h>
#include <threads.h>

typedef struct {
    int              *buffer;
    size_t            capacity;  // Must be power of 2
    atomic_size_t     head;      // Consumer reads from here
    atomic_size_t     tail;      // Producer writes to here
} RingBuffer;

void ring_init(RingBuffer *rb, size_t capacity) {
    // Round up to power of 2 for efficient modulo
    size_t cap = 1;
    while (cap < capacity) cap <<= 1;
    rb->buffer = malloc(cap * sizeof(int));
    rb->capacity = cap;
    atomic_store(&rb->head, 0);
    atomic_store(&rb->tail, 0);
}

// Producer: try to push an item. Returns 1 on success, 0 if full.
int ring_push(RingBuffer *rb, int value) {
    size_t tail = atomic_load_explicit(&rb->tail, memory_order_relaxed);
    size_t next_tail = (tail + 1) & (rb->capacity - 1);  // Fast modulo

    if (next_tail == atomic_load_explicit(&rb->head, memory_order_acquire)) {
        return 0;  // Buffer full
    }

    rb->buffer[tail] = value;
    atomic_store_explicit(&rb->tail, next_tail, memory_order_release);
    return 1;
}

// Consumer: try to pop an item. Returns 1 on success, 0 if empty.
int ring_pop(RingBuffer *rb, int *out) {
    size_t head = atomic_load_explicit(&rb->head, memory_order_relaxed);

    if (head == atomic_load_explicit(&rb->tail, memory_order_acquire)) {
        return 0;  // Buffer empty
    }

    *out = rb->buffer[head];
    atomic_store_explicit(&rb->head, (head + 1) & (rb->capacity - 1),
                          memory_order_release);
    return 1;
}

void ring_free(RingBuffer *rb) {
    free(rb->buffer);
    rb->buffer = NULL;
}

// Producer thread
int producer_thread(void *arg) {
    RingBuffer *rb = arg;
    for (int i = 0; i < 1000000; i++) {
        while (!ring_push(rb, i)) {
            // Spin — buffer full
            thrd_yield();
        }
    }
    return 0;
}

// Consumer thread
int consumer_thread(void *arg) {
    RingBuffer *rb = arg;
    long long sum = 0;
    int count = 0;
    int val;
    while (count < 1000000) {
        if (ring_pop(rb, &val)) {
            sum += val;
            count++;
        } else {
            thrd_yield();  // Spin — buffer empty
        }
    }
    printf("Consumed %d items, sum = %lld\n", count, sum);
    return 0;
}
```

**Krok 4 — Weryfikacja i optymalizacja:**
- Bez blokady: tylko operacje atomowe - bez muteksów, bez przełączania kontekstu.
- Uporządkowanie pamięci:`release`przy zapisie zapewnia widoczność danych przed aktualizacją indeksu; `acquire`przy odczycie gwarantuje, że zobaczymy dane po odczytaniu indeksu.
- Pojemność mocy 2: umożliwia`& (capacity - 1)`zamiast`% capacity`— znacznie szybciej.
- Przepustowość: miliardy operacji na sekundę na nowoczesnym sprzęcie.
- Produkcja: dodaj dopełnienie między`head`i `tail`, aby zapobiec fałszywemu udostępnianiu (każdy na własnej linii pamięci podręcznej).
---

## Streszczenie
C jest podstawą współczesnej informatyki. Zapewnia maksymalną kontrolę nad sprzętem przy minimalnym obciążeniu abstrakcją. Kosztem tej kontroli jest odpowiedzialność — samodzielnie zarządzasz pamięcią, sprawdzasz granice i radzisz sobie z błędami. W przypadku programowania systemów, programowania systemów wbudowanych i wszędzie tam, gdzie liczą się ograniczenia wydajności i zasobów, język C pozostaje niezrównany. W pozostałych przypadkach języki wyższego poziomu zbudowane na bazie języka C są zwykle bardziej produktywnymi wyborami.