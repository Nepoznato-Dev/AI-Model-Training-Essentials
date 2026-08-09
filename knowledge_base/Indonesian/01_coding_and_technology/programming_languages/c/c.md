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
C adalah bahasa pemrograman prosedural untuk tujuan umum yang dibuat oleh Dennis Ritchie di Bell Labs antara tahun 1969 dan 1973. C dirancang untuk mengimplementasikan sistem operasi Unix, dan tetap menjadi salah satu bahasa pemrograman yang paling banyak digunakan selama 50 tahun kemudian. C menyediakan akses memori tingkat rendah, perpustakaan standar minimal, dan pemetaan yang bersih terhadap instruksi mesin -- menjadikannya fondasi di mana sebagian besar komputasi modern dibangun.
C adalah bahasa di balik sistem operasi (Linux, kernel Windows, macOS), sistem tertanam, mesin basis data (SQLite, PostgreSQL), kompiler (CPython Python, MRI Ruby), dan hampir semua runtime bahasa pemrograman lainnya. Memahami C adalah memahami cara kerja komputer sebenarnya.
---

## Mengapa C Penting
- **Kedekatan dengan perangkat keras**: C memetakan secara dekat dengan kode mesin. Tidak ada pengumpul sampah, tidak ada overhead runtime, tidak ada alokasi tersembunyi.
- **Ubiquity**: Dari mikrokontroler hingga superkomputer, C berjalan di mana saja.
- **Dasar komputasi**: Linux, Windows, kernel macOS, juru bahasa Python, SQLite, Git -- semuanya ditulis dalam C.
- **Kinerja**: Kecepatan eksekusi mendekati optimal dengan kontrol penuh atas tata letak memori.
- **Pengaruh**: Sintaks dan konsep C (pointer, array, struct, fungsi) berbentuk C++, Java, C#, JavaScript, Go, Rust, dan sebagian besar bahasa setelahnya.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Manajemen memori manual** | Tidak ada pengumpul sampah -- Anda mengalokasikan dan mengosongkan memori sendiri | Penggunaan malloc/gratis secara hati-hati; Pola RAII di C++ |
| **Buffer meluap** | Pemeriksaan array tanpa batas -- mudah untuk menulis melewati ujung buffer | Gunakan strncpy daripada strcpy; aktifkan peringatan kompiler |
| **Tidak ada OOP bawaan** | Hanya prosedural -- tanpa kelas, pewarisan, atau metode | Gunakan struct + pointer fungsi; atau beralih ke C++ |
| **Perpustakaan standar terbatas** | Fungsionalitas bawaan minimal | Perpustakaan pihak ketiga atau tulis |
| **Perilaku tidak terdefinisi** | Banyak kesalahan yang dikompilasi dengan baik tetapi crash secara tidak terduga | Gunakan pembersih, penganalisis statis |
---

## Dasar Sintaks
### Struktur Dasar
Setiap program C dimulai pada`main()`. Bahasa dikompilasi -- kode sumber menjadi kode mesin melalui kompiler (GCC, Clang, MSVC).
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

### Variabel dan Jenis
C diketik secara statis -- setiap variabel memiliki tipe tetap yang diketahui pada waktu kompilasi.
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

### Petunjuk
Pointer adalah fitur C yang paling kuat dan paling disalahpahami. Sebuah pointer menyimpan alamat memori.
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

### Aliran Kontrol
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

### Fungsi dan Stack
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

## Tata Letak Memori
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

| Wilayah | Apa yang Terjadi di Sana | Seumur Hidup | Siapa yang Mengelolanya |
|--------|----------------|----------|----------------|
| **Tumpukan** | Variabel lokal, parameter fungsi | Sampai fungsi kembali | Kompiler (otomatis) |
| **Tumpukan** | alokasi malloc/calloc | Sampai Anda menelepon free() | Anda (panduan) |
| **Data/BSS** | Variabel global dan statis | Seluruh program seumur hidup | Kompiler (otomatis) |
| **Teks** | Kode mesin | Seluruh program seumur hidup | Hanya baca |
---

## Perpustakaan Standar
| Tajuk | Tujuan | Fungsi Umum |
|--------|---------|-----------------|
| `<stdio.h>`| Masukan/keluaran | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Utilitas Umum | malloc, gratis, keluar, atoi, rand, qsort |
| `<string.h>`| Operasi string | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matematika | sin, cos, sqrt, pow, fabs, ceil, lantai |
| `<ctype.h>`| Klasifikasi karakter | isalpha, isdigit, toupper, tolower |
| `<time.h>`| Tanggal dan waktu | waktu, jam, waktu diff, waktu strf |
| `<assert.h>`| Men-debug pernyataan | menegaskan(kondisi) |
| `<errno.h>`| Kode kesalahan | errno, kesalahan, kesalahan |
---

## Sintaks & Pola Tingkat Lanjut
### Makro Praprosesor
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

### Penunjuk Fungsi dan Panggilan Balik
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

### Pola Penanganan Kesalahan Khusus
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

## Konkurensi & Paralelisme
### Utas POSIX (pthread)
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

### Mutex dan Status Bersama
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

### C11 Atom dan Benang
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek
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

### Saluran CI/CD (Tindakan GitHub)
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

## Pengujian
### Pengujian Unit dengan Kerangka Sederhana
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

## Interoperabilitas
### Memanggil C dari Python (ctypes)
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

### Memanggil C dari Bahasa Lain
| Bahasa | Mekanisme | Contoh |
|----------|-----------|---------|
| ular piton | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| rubi | Biola | `Fiddle.dlopen("./lib.so")`|
| Jawa | JNI | `System.loadLibrary("mylib")`|
| C++ | eksternal "C" | `extern "C" void my_func();`|
| Karat | eksternal "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Pola Desain
### Pointer Buram (Idiom Pimpl di C)
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

### Tabel Virtual (OOP di C)
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
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

### Teknik Optimasi
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

## Penerapan
### Kompilasi Silang
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Penerapan Docker
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

## Pola dan Idiom Umum
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

## Kompilasi dan Perkakas
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Alat | Tujuan |
|------|---------|
| **GCC / Dentang** | Kompiler |
| **Buat / CMake** | Membangun sistem |
| **GDB** | Debug |
| **Valgrind** | Detektor kesalahan memori (kebocoran, akses tidak valid) |
| **AlamatPembersih** | Pemeriksaan memori waktu kompilasi |
| **cppperiksa** | Analisis statis |
| **format dentang** | Pemformatan kode |
---

## Kapan Menggunakan C
| Skenario | Mengapa C | Alternatif Lebih Baik |
|----------|-------|-------------------|
| Sistem Operasi | Akses perangkat keras langsung, tanpa overhead runtime | -- |
| Sistem tertanam / mikrokontroler | Jejak minimal, dapat dijalankan pada apa pun | Karat untuk keselamatan sangat penting tertanam |
| Mesin basis data | Performa maksimal, kontrol memori penuh | -- |
| Kompiler dan juru bahasa | Cepat, portabel, dipahami dengan baik | C++ untuk proyek kompiler yang lebih besar |
| Driver perangkat | Diperlukan oleh sebagian besar API kernel OS | -- |
| Pustaka yang kritis terhadap kinerja | Kecepatan mendekati optimal | Karat untuk jaminan keamanan memori |
| Pengembangan aplikasi umum | Terlalu banyak pekerjaan manual | Python, Java, Buka, C# |
| Pengembangan web | Alat yang salah seluruhnya | JavaScript, Buka, Python |
| Ilmu data / ML | Tidak ada ekosistem untuk ini | Python, R, Julia |
---

## C Standar
| Standar | Tahun | Penambahan Kunci |
|----------|------|--------------|
| Bab 89/C90 | 1989/1990 | ANSI C asli -- masih menjadi dasar |
| Bab 99 | 1999 | // komentar, tipe bool, array dengan panjang variabel, inline, stdint.h |
| C11 | 2011 | Operasi atom, utas, struct anonim, _Generik |
| C17 | 2018 | Perbaikan bug dan klarifikasi (tidak ada fitur baru) |
| C23 | 2024 | nullptr, typeof, constexpr, praprosesor yang ditingkatkan |
Sebagian besar kode produksi menargetkan C11 atau C17. C23 menghadirkan kemudahan modern tetapi penerapannya memerlukan waktu.
---

## Ringkasan
C adalah landasan komputasi modern. Ini memberi Anda kontrol maksimum atas perangkat keras dengan overhead abstraksi minimal. Biaya kendali tersebut adalah tanggung jawab -- Anda mengelola memori, memeriksa batasan, dan menangani sendiri kesalahan. Untuk pemrograman sistem, pengembangan tertanam, dan di mana pun kendala kinerja dan sumber daya menjadi masalah, C tetap tak tertandingi. Selain itu, bahasa tingkat tinggi yang dibangun di atas C biasanya merupakan pilihan yang lebih produktif.