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
C, Dennis Ritchie tarafından 1969 ile 1973 yılları arasında Bell Laboratuvarlarında oluşturulan genel amaçlı, prosedürel bir programlama dilidir. Unix işletim sistemini uygulamak için tasarlanmıştır ve 50 yıl sonra en yaygın kullanılan programlama dillerinden biri olmaya devam etmektedir. C, düşük seviyeli bellek erişimi, minimum standartta bir kitaplık ve makine talimatlarına temiz bir eşleme sağlar; bu da onu çoğu modern bilgi işlemin üzerine kurulduğu temel haline getirir.
C, işletim sistemlerinin (Linux, Windows çekirdeği, macOS), gömülü sistemlerin, veritabanı motorlarının (SQLite, PostgreSQL), derleyicilerin (Python'un CPython'u, Ruby'nin MRI'sı) ve neredeyse tüm diğer programlama dillerinin çalışma zamanlarının arkasındaki dildir. C'yi anlamak, bilgisayarların gerçekte nasıl çalıştığını anlamaktır.
---

## C Neden Önemlidir
- **Donanımlara yakınlık**: C, makine koduyla yakından eşleşir. Çöp toplayıcı yok, çalışma zamanı ek yükü yok, gizli tahsis yok.
- **Ubiquity**: Mikrodenetleyicilerden süper bilgisayarlara kadar C her yerde çalışır.
- **Bilgisayarın temeli**: Linux, Windows, macOS çekirdekleri, Python yorumlayıcısı, SQLite, Git -- tümü C dilinde yazılmıştır.
- **Performans**: Bellek düzeni üzerinde tam kontrol ile optimuma yakın yürütme hızı.
- **Etki**: C'nin sözdizimi ve kavramları (işaretçiler, diziler, yapılar, işlevler), C++, Java, C#, JavaScript, Go, Rust ve takip eden dillerin çoğunu şekillendirdi.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Manuel bellek yönetimi** | Çöp toplayıcı yok; belleği kendiniz ayırır ve serbest bırakırsınız | Malloc/free'nin dikkatli kullanımı; C++'daki RAII desenleri |
| **Arabellek taşmaları** | Dizilerde sınır yok denetimi - arabellek sonlarının ötesine yazmak kolay | Strcpy yerine strncpy kullanın; derleyici uyarılarını etkinleştir |
| **Yerleşik OOP yok** | Yalnızca prosedürle ilgili -- sınıf, miras veya yöntem yok | Yapıları + işlev işaretçilerini kullanın; veya C++'a geçin |
| **Sınırlı standart kütüphane** | Minimum yerleşik işlevsellik | Üçüncü taraf kitaplıkları veya kendi kitaplığınızı yazın |
| **Tanımlanmamış davranış** | Birçok hata sorunsuz bir şekilde derleniyor ancak tahmin edilemeyecek şekilde çöküyor | Temizleyiciler, statik analizörler kullanın |
---

## Söz Diziminin Temelleri
### Temel Yapı
Her C programı `main()`'de başlar. Dil derlenir; kaynak kodu bir derleyici (GCC, Clang, MSVC) aracılığıyla makine koduna dönüşür.
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

### Değişkenler ve Türler
C statik olarak yazılmıştır; her değişkenin derleme zamanında bilinen sabit bir türü vardır.
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

### İşaretçiler
İşaretçiler C'nin en güçlü ve en yanlış anlaşılan özelliğidir. Bir işaretçi bir bellek adresini tutar.
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

### Kontrol Akışı
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

### İşlevler ve Yığın
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

## Bellek Düzeni
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

| Bölge | Oraya Ne Gidiyor | Ömür boyu | Kim Yönetiyor |
|----------|----------------|----------|----------------|
| **Yığın** | Yerel değişkenler, fonksiyon parametreleri | İşlev dönene kadar | Derleyici (otomatik) |
| **Yığın** | malloc/calloc tahsisleri | free() | diyene kadar Siz (manuel) |
| **Veri/BSS** | Global ve statik değişkenler | Programın kullanım ömrünün tamamı | Derleyici (otomatik) |
| **Metin** | Makine kodu | Programın kullanım ömrünün tamamı | Salt okunur |
---

## Standart Kütüphane
| Başlık | Amaç | Ortak İşlevler |
|----------|------------|------|
| `<stdio.h>`| Giriş/çıkış | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Genel hizmetler | malloc, ücretsiz, çıkış, atoi, rand, qsort |
| `<string.h>`| Dize işlemleri | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matematik | günah, cos, sqrt, pow, fabs, tavan, zemin |
| `<ctype.h>`| Karakter sınıflandırması | isalpha, isdigit, toupper, tolower |
| `<time.h>`| Tarih ve saat | zaman, saat, farkzamanı, strftime |
| `<assert.h>`| Hata ayıklama iddiaları | iddia(koşul) |
| `<errno.h>`| Hata kodları | hata yok, hata, hata |
---

## Gelişmiş Sözdizimi ve Desenler
### Önişlemci Makroları
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

### İşlev İşaretçileri ve Geri Aramalar
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

### Özel Hata İşleme Modelleri
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

## Eşzamanlılık ve Paralellik
### POSIX Konuları (pthread'ler)
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

### Mutex ve Paylaşılan Durum
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

### C11 Atomlar ve Konular
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### Makefile
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Basit Bir Çerçeveyle Birim Testi
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

## Birlikte Çalışabilirlik
### Python'dan C'yi çağırmak (ctypes)
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

### Diğer Dillerden C'yi Aramak
| Dil | Mekanizma | Örnek |
|----------|-----------|-----------|
| Python | türler, cffi | `ctypes.CDLL("./lib.so")`|
| Yakut | Keman | `Fiddle.dlopen("./lib.so")`|
| Java | JNI | `System.loadLibrary("mylib")`|
| C++ | harici "C" | `extern "C" void my_func();`|
| Pas | harici "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Tasarım Desenleri
### Opak İşaretçi (C'de Pimpl Deyim)
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

### Sanal Tablo (C'de OOP)
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Çapraz Derleme
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Docker Dağıtımı
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

## Ortak Kalıplar ve Deyimler
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

## Derleme ve Araç Oluşturma
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Araç | Amaç |
|------|------------|
| **GCC / Clang** | Derleyiciler |
| **Yap / CMake** | Sistem oluşturma |
| **GDB** | Hata ayıklayıcı |
| **Valgrind** | Bellek hatası algılayıcı (sızıntılar, geçersiz erişim) |
| **AdresSanitizer** | Derleme zamanı hafıza kontrolü |
| **cppcheck** | Statik analiz |
| **clang-formatı** | Kod biçimlendirme |
---

## C Ne Zaman Kullanılmalı
| Senaryo | Neden C | Daha İyi Alternatif |
|----------|-----------|--------|
| İşletim sistemleri | Doğrudan donanım erişimi, çalışma zamanı yükü yok | -- |
| Gömülü sistemler / mikrodenetleyiciler | Minimal ayak izi, her şeyde çalışır | Güvenlik açısından kritik gömülü paslar |
| Veritabanı motorları | Maksimum performans, tam bellek kontrolü | -- |
| Derleyiciler ve tercümanlar | Hızlı, taşınabilir, iyi anlaşılmış | Daha büyük derleyici projeleri için C++ |
| Aygıt sürücüleri | Çoğu işletim sistemi çekirdek API'si için gereklidir | -- |
| Performans açısından kritik kitaplıklar | İdeale yakın hız | Garantili bellek güvenliği için pas |
| Genel uygulama geliştirme | Çok fazla manuel çalışma | Python, Java, Go, C# |
| Web geliştirme | Tamamen yanlış araç | JavaScript, Git, Python |
| Veri bilimi / ML | Bunun için ekosistem yok | Python, R, Julia |
---

## C Standartları
| Standart | Yıl | Önemli İlaveler |
|----------|------|-------------|
| C89/C90 | 1989/1990 | Orijinal ANSI C -- hala temel |
| C99 | 1999 | // yorumlar, bool türü, değişken uzunluklu diziler, satır içi, stdint.h |
| C11 | 2011 | Atomik işlemler, iş parçacıkları, anonim yapılar, _Generic |
| C17 | 2018 | Hata düzeltmeleri ve açıklamalar (yeni özellik yok) |
| C23 | 2024 | nullptr, typeof, constexpr, geliştirilmiş önişlemci |
Çoğu üretim kodu C11 veya C17'yi hedefler. C23 modern kolaylıklar getiriyor ancak benimsenmesi zaman alıyor.
---

## Sentetik Soru-Cevap
### S1: C'deki işaretçiler ve diziler arasındaki fark nedir?
**C:** Diziler ve işaretçiler birbiriyle ilişkilidir ancak farklıdır. Dizi, derleme zamanında bilinen sabit boyutlu, bitişik bir bellek bloğudur. İşaretçi, bellek adresini tutan bir değişkendir. Diziler, işlevlere aktarıldığında işaretçilere dönüşür, ancak`sizeof(array)`toplam boyutu verirken`sizeof(pointer)`yalnızca işaretçi boyutunu (4 veya 8 bayt) verir. Dizi adları değiştirilebilir değerler değildir;`arr++`yapamazsınız.
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

### S2: Belleği nasıl düzgün şekilde yönetebilirim ve sızıntıları nasıl önleyebilirim?
**A:** Her`malloc`/ `calloc`'nin karşılık gelen bir `free`'si olmalıdır. Yaygın hatalar: serbest bırakmayı unutmak (sızıntı), iki kez serbest bırakmak (tanımsız davranış), serbest bıraktıktan sonra belleği kullanmak (boşaldıktan sonra kullan) ve`malloc`dönüş değerini kontrol etmemek (arıza durumunda NULL). En iyi uygulama: aynı modülde tahsis edin ve serbest bırakın, hata işleme için "temizlemeye git" modelini kullanın ve serbest bırakılan işaretçileri her zaman NULL olarak ayarlayın.
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

### S3: C'de hata işlemeye yönelik en iyi uygulamalar nelerdir?
**A:** C'nin istisnası yoktur. Hata işleme, dönüş değerlerini (hata kodları, NULL işaretçileri, negatif değerler) kullanır. Standart model: işlevler, arıza durumunda bir durum kodu veya NULL döndürür ve sistem çağrıları için`errno`değerini ayarlar. Hatalarda kaynak temizliği için "temizlemeye git" modelini kullanın. Her zaman `malloc`,`fopen`ve başarısız olabilecek diğer işlevlerin dönüş değerlerini kontrol edin.
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

### S4: Yapılar, birleşimler ve bit alanları bellek düzeninde nasıl farklılık gösterir?
**A:** Yapılar, hizalama için olası dolgularla birlikte üyeleri sıralı olarak yerleştirir. Birleşimler tüm üyeleri aynı bellek konumuna yerleştirir; boyut en büyük üyeye eşittir. Bit alanları birden fazla değeri tek bir tamsayıya paketler. Yapılar, heterojen veriler içindir, yalnızca bir alan etkin olduğunda tür değiştirme veya yerden tasarruf için birleşimler ve kompakt bayrak depolama için bit alanlarıdır.
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

### S5: İşlev işaretçileri nedir ve bunları ne zaman kullanmalıyım?
**C:** İşlev işaretçileri bir işlevin adresini saklar ve geri çağırmaları, polimorfizmi ve eklenti mimarilerini etkinleştirir. Bunlar C'nin üst düzey işlevlere yaklaşımının temelini oluşturur (`qsort`,`bsearch`gibi). Bunları şu söz dizimi ile bildirin: `return_type (*name)(parameter_types)`.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Dinamik Dizi Uygulama (Vektör)
**Sorun Açıklaması:** C'de öğeler eklendiğinde otomatik olarak büyüyen, O(1) amortize eklemeyi destekleyen ve uygun temizleme sağlayan dinamik bir dizi uygulayın. Bu, C++ `std::vector`'nin C eşdeğeridir.
**1. Adım — Sorunu Anlayın:**
Dinamik bir dizi şunları gerektirir: (1) yığınla ayrılmış bir arabellek, (2) boyutun (kullanılan öğeler) ve kapasitenin (ayrılmış yuvalar) izlenmesi, (3) boyut kapasiteye ulaştığında yeniden tahsis, (4) uygun bellek temizliği. 2x büyüme faktörü, O(1) amortize edilmiş eklentiyi verir.
**2. Adım — Yaklaşımı Belirleyin:**
- İlk tahsis için `malloc`'yi, büyüme için `realloc`'yi kullanın.
- Veri işaretçisini, boyutunu ve kapasitesini bir yapıda saklayın.
-`size == capacity`olduğunda kapasiteyi iki katına çıkararak büyütün.
-`push`,`pop`,`get`,`set`ve`free`işlemlerini sağlayın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Amortize edilmiş O(1) itme: iki katına çıkarma, her bir öğenin toplamda en fazla O(log n) katı kopyalandığı anlamına gelir.
-`vec_get`ve `vec_pop`'deki sınır kontrolü, hataları erkenden yakalar; çalışma zamanı güvenlik ağının olmadığı C'de çok önemlidir.
- Bellek: Kapasite 4'ten başlayarak 100 basmadan sonra kapasite 128'e ulaşır (4→8→16→32→64→128).
- Üretim: Büyütme işlemi tamamlandığında kullanılmayan belleği geri kazanmak için`shrink_to_fit`(tam boyuta yeniden tahsis) kullanın.
### Sorun 2: Basit Bir Hash Tablosu Oluşturun
**Sorun Açıklaması:** Çarpışma çözümü için ayrı zincirleme kullanarak dize anahtarları ve tamsayı değerleri içeren bir karma tablosu uygulayın. Ekleme, arama ve silme işlemlerini destekleyin.
**1. Adım — Sorunu Anlayın:**
Bir karma tablosu, bir karma işlevi aracılığıyla anahtarları dizi endekslerine eşler. Çarpışmalar (aynı dizine eşlenen farklı anahtarlar) ayrı zincirleme ile çözülür: her paket, bağlantılı bir giriş listesidir. İhtiyacımız olan: karma işlevi, ekleme, arama, silme ve temizleme.
**2. Adım — Yaklaşımı Belirleyin:**
- Dize tuşlarının iyi dağıtımı için FNV-1a karmasını kullanın.
- Kova işaretçileri dizisi (bağlantılı liste başlıkları).
- Yük faktörü takibi; Yük faktörü eşiği aştığında yeniden boyutlandırın.
- Tüm işlemler O(1) ortalama, O(n) en kötü durumdur.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- İyi bir karma işlevi ve makul yük faktörü ile ekleme/arama/silme için ortalama O(1).
- FNV-1a, minimum hesaplamayla dize tuşları için mükemmel dağıtım sağlar.
- `hashmap_remove`'deki işaretçiden işaretçiye tekniği (`Entry **pp`), özel durumlar olmadan hem liste başı hem de liste ortası silme işlemini zarif bir şekilde gerçekleştirir.
- Üretim: yük faktörü eşiği aştığında yeniden karma oluşturma ekleyin. Daha iyi önbellek performansı için açık adreslemeyi (doğrusal araştırma) kullanın.
### Sorun 3: Üretici-Tüketici için Halka Arabelleğinin Uygulanması
**Sorun Açıklaması:** Çalışma sırasında dinamik ayırma olmadan yüksek performanslı iş parçacıkları arası iletişim için C'de kilitsiz, tek üreticili, tek tüketicili halka arabelleği uygulayın.
**1. Adım — Sorunu Anlayın:**
Halka arabellek (dairesel arabellek), okuma ve yazma endekslerine sahip sabit boyutlu bir dizi kullanır. Arabellek dolduğunda yazar bloke eder veya üzerine yazar. SPSC'de (tek üretici tek tüketici), maksimum verim için kilitler yerine atomik işlemleri kullanabiliriz.
**2. Adım — Yaklaşımı Belirleyin:**
- Başlatma sırasında bir kez tahsis edilen sabit boyutlu dizi.
- Atomik indeksler olarak`head`(okuma konumu) ve`tail`(yazma konumu).
- Üretici `tail`'yi ilerletir; tüketici avansları`head`.
-`head == tail`olduğunda arabellek boştur;`(tail + 1) % capacity == head`olduğunda dolu.
- Uygun bellek sıralamasıyla C11 atomlarını kullanın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Kilitsiz: yalnızca atomik işlemler — muteks yok, bağlam anahtarı yok.
- Bellek sıralaması: Yazma sırasında `release`, verilerin dizin güncellemesinden önce görünür olmasını sağlar; `acquire`on read, dizini okuduktan sonra verileri görmemizi sağlar.
- 2'nin gücü kapasitesi:`% capacity`yerine `& (capacity - 1)`'yi etkinleştirir — çok daha hızlı.
- Verim: Modern donanımda saniyede milyarlarca işlem.
- Üretim: Yanlış paylaşımı önlemek için`head`ve`tail`arasına dolgu ekleyin (her biri kendi önbellek hattında).
---

## Özet
C, modern bilgisayarların temelidir. Minimum soyutlama yüküyle donanım üzerinde maksimum kontrol sağlar. Bu kontrolün maliyeti sorumluluktur; hafızayı yönetirsiniz, sınırları kontrol edersiniz ve hataları kendiniz halledersiniz. Sistem programlama, yerleşik geliştirme ve performans ile kaynak kısıtlamalarının önemli olduğu her yerde C'nin eşsizliği devam etmektedir. Diğer her şey için, C üzerine kurulu yüksek seviyeli diller genellikle daha verimli seçimlerdir.