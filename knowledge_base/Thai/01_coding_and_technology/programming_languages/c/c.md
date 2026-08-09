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

#ซี
C เป็นภาษาโปรแกรมเชิงขั้นตอนสำหรับวัตถุประสงค์ทั่วไป สร้างขึ้นโดย Dennis Ritchie ที่ Bell Labs ระหว่างปี 1969 ถึง 1973 ออกแบบเพื่อใช้ระบบปฏิบัติการ Unix และยังคงเป็นหนึ่งในภาษาโปรแกรมที่ใช้กันอย่างแพร่หลายที่สุดในกว่า 50 ปีต่อมา C ให้การเข้าถึงหน่วยความจำระดับต่ำ ไลบรารีมาตรฐานขั้นต่ำ และการแมปคำสั่งเครื่องที่ชัดเจน ทำให้เป็นรากฐานในการสร้างคอมพิวเตอร์สมัยใหม่ส่วนใหญ่
C คือภาษาที่อยู่เบื้องหลังระบบปฏิบัติการ (Linux, Windows kernel, macOS), ระบบฝังตัว, โปรแกรมฐานข้อมูล (SQLite, PostgreSQL), คอมไพเลอร์ (CPython ของ Python, MRI ของ Ruby) และรันไทม์ภาษาโปรแกรมอื่นๆ แทบทุกภาษา การทำความเข้าใจ C คือการทำความเข้าใจว่าคอมพิวเตอร์ทำงานอย่างไร
---

## ทำไม C ถึงมีความสำคัญ
- **ความใกล้ชิดกับฮาร์ดแวร์**: C แมปอย่างใกล้ชิดกับรหัสเครื่อง ไม่มีตัวรวบรวมขยะ ไม่มีค่าใช้จ่ายรันไทม์ ไม่มีการจัดสรรที่ซ่อนอยู่
- **ความแพร่หลาย**: ตั้งแต่ไมโครคอนโทรลเลอร์ไปจนถึงซูเปอร์คอมพิวเตอร์ C ทำงานได้ทุกที่
- **รากฐานของการประมวลผล**: Linux, Windows, เคอร์เนล macOS, ตัวแปล Python, SQLite, Git -- ทั้งหมดเขียนด้วยภาษา C
- **ประสิทธิภาพ**: ความเร็วการดำเนินการใกล้เคียงที่สุดพร้อมการควบคุมเค้าโครงหน่วยความจำเต็มรูปแบบ
- **อิทธิพล**: ไวยากรณ์และแนวคิดของ C (พอยน์เตอร์ อาร์เรย์ โครงสร้าง ฟังก์ชัน) ที่มีรูปร่างเป็น C++, Java, C#, JavaScript, Go, Rust และภาษาส่วนใหญ่ที่ตามมา
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **การจัดการหน่วยความจำด้วยตนเอง** | ไม่มีตัวรวบรวมขยะ - คุณจัดสรรและเพิ่มหน่วยความจำด้วยตัวเอง | การใช้ malloc/ฟรี อย่างระมัดระวัง รูปแบบ RAII ใน C++ |
| **บัฟเฟอร์ล้น** | ไม่มีการตรวจสอบขอบเขตในอาร์เรย์ -- ง่ายต่อการเขียนบัฟเฟอร์ที่สิ้นสุด | ใช้ strncpy แทน strcpy เปิดใช้งานคำเตือนคอมไพเลอร์ |
| **ไม่มี OOP ในตัว** | ขั้นตอนเท่านั้น -- ไม่มีคลาส การสืบทอด หรือเมธอด | ใช้ structs + ตัวชี้ฟังก์ชัน หรือเปลี่ยนเป็น C++ |
| **ไลบรารี่มาตรฐานมีจำนวนจำกัด** | ฟังก์ชั่นในตัวน้อยที่สุด | ไลบรารีบุคคลที่สามหรือเขียน | ของคุณเอง
| **พฤติกรรมที่ไม่ได้กำหนด** | ข้อผิดพลาดมากมายคอมไพล์ได้ดีแต่เกิดข้อผิดพลาดอย่างคาดเดาไม่ได้ | ใช้น้ำยาฆ่าเชื้อ เครื่องวิเคราะห์ไฟฟ้าสถิต |
---

## พื้นฐานไวยากรณ์
### โครงสร้างพื้นฐาน
ทุกโปรแกรม C เริ่มต้นที่`main()`ภาษาถูกคอมไพล์ - ซอร์สโค้ดกลายเป็นรหัสเครื่องผ่านคอมไพเลอร์ (GCC, Clang, MSVC)
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

### ตัวแปรและประเภท
C ถูกพิมพ์แบบคงที่ - ทุกตัวแปรมีประเภทคงที่ซึ่งทราบ ณ เวลาคอมไพล์
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

### ตัวชี้
พอยน์เตอร์เป็นคุณสมบัติที่ทรงพลังที่สุดและถูกเข้าใจผิดมากที่สุดของ C ตัวชี้เก็บที่อยู่หน่วยความจำ
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

### การควบคุมการไหล
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

### ฟังก์ชั่นและสแต็ก
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

## เค้าโครงหน่วยความจำ
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

| ภูมิภาค | ไปที่นั่นอะไร | ตลอดชีวิต | ใครเป็นผู้จัดการ |
|----------------------|----------------|----------|----------------|
| **กองซ้อน** | ตัวแปรโลคัล พารามิเตอร์ฟังก์ชัน | จนกว่าฟังก์ชันจะส่งคืน | คอมไพเลอร์ (อัตโนมัติ) |
| **กอง** | การจัดสรร malloc/calloc | จนกว่าคุณจะโทรฟรี() | คุณ (ด้วยตนเอง) |
| **ข้อมูล/BSS** | ตัวแปรโกลบอลและสแตติก | อายุการใช้งานโปรแกรมทั้งหมด | คอมไพเลอร์ (อัตโนมัติ) |
| **ข้อความ** | รหัสเครื่อง | อายุการใช้งานโปรแกรมทั้งหมด | อ่านอย่างเดียว |
---

## ห้องสมุดมาตรฐาน
| ส่วนหัว | วัตถุประสงค์ | ฟังก์ชั่นทั่วไป |
|----------------------|---------|-----------------|
| `<stdio.h>`| อินพุต/เอาท์พุต | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| สาธารณูปโภคทั่วไป | malloc, ฟรี, ออก, atoi, rand, qsort |
| `<string.h>`| การดำเนินการสตริง | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| คณิตศาสตร์ | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| การจำแนกอักขระ | isalpha, isdigit, toupper, tolower |
| `<time.h>`| วันที่และเวลา | เวลา, นาฬิกา, difftime, strftime |
| `<assert.h>`| การยืนยันการแก้ไขจุดบกพร่อง | ยืนยัน (เงื่อนไข) |
| `<errno.h>`| รหัสข้อผิดพลาด | errno, perror, strerror |
---

## ไวยากรณ์และรูปแบบขั้นสูง
### มาโครตัวประมวลผลล่วงหน้า
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

### ตัวชี้ฟังก์ชันและการโทรกลับ
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

### รูปแบบการจัดการข้อผิดพลาดที่กำหนดเอง
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### เธรด POSIX (pthreads)
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

### Mutex และสถานะที่ใช้ร่วมกัน
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

### C11 อะตอมและเธรด
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
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

### เมคไฟล์
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

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### การทดสอบหน่วยด้วยกรอบงานอย่างง่าย
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

## การทำงานร่วมกัน
### โทร C จาก Python (ctypes)
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

### โทร C จากภาษาอื่น
| ภาษา | กลไก | ตัวอย่าง |
|----------|-----------|---------|
| หลาม | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| ทับทิม | ซอ | `Fiddle.dlopen("./lib.so")`|
| ชวา | เจเอ็นไอ | `System.loadLibrary("mylib")`|
| ซี++ | ภายนอก "C" | `extern "C" void my_func();`|
| สนิม | ภายนอก "C" + FFI | `extern "C" { fn my_func(); }`|
---

## รูปแบบการออกแบบ
### ตัวชี้ทึบแสง (Pimpl Idiom ในภาษา C)
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

### ตารางเสมือน (OOP ใน C)
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### การรวบรวมข้าม
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### การปรับใช้นักเทียบท่า
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

## รูปแบบและสำนวนทั่วไป
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

## การรวบรวมและการใช้เครื่องมือ
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **GCC / เสียงดังกราว** | คอมไพเลอร์ |
| **สร้าง / CMake** | สร้างระบบ |
| **จีดีบี** | ดีบักเกอร์ |
| **วาลกรินด์** | ตัวตรวจจับข้อผิดพลาดของหน่วยความจำ (การรั่วไหล, การเข้าถึงที่ไม่ถูกต้อง) |
| **น้ำยาฆ่าเชื้อที่อยู่** | การตรวจสอบหน่วยความจำเวลาคอมไพล์ |
| **cppcheck** | การวิเคราะห์แบบคงที่ |
| **รูปแบบเสียงดังกราว** | การจัดรูปแบบโค้ด |
---

## เมื่อใดควรใช้ C
| สถานการณ์ | ทำไมต้องซี | ทางเลือกที่ดีกว่า |
|----------|-------|-------------------|
| ระบบปฏิบัติการ | การเข้าถึงฮาร์ดแวร์โดยตรง ไม่มีค่าใช้จ่ายรันไทม์ | -- |
| ระบบสมองกลฝังตัว / ไมโครคอนโทรลเลอร์ | รอยเท้าน้อยที่สุด ทำงานบนทุกสิ่ง | สนิมสำหรับการฝังตัวที่มีความสำคัญด้านความปลอดภัย
| เอ็นจิ้นฐานข้อมูล | ประสิทธิภาพสูงสุด ควบคุมหน่วยความจำเต็ม | -- |
| คอมไพเลอร์และล่าม | รวดเร็ว พกพาสะดวก | C++ สำหรับโปรเจ็กต์คอมไพเลอร์ขนาดใหญ่ |
| ไดรเวอร์อุปกรณ์ | ต้องการโดย API เคอร์เนล OS ส่วนใหญ่ | -- |
| ไลบรารี่ที่เน้นประสิทธิภาพ | ความเร็วใกล้เคียงที่สุด | สนิมเพื่อรับประกันความปลอดภัยของหน่วยความจำ |
| การพัฒนาแอพพลิเคชั่นทั่วไป | การทำงานด้วยตนเองมากเกินไป | หลาม, Java, Go, C# |
| การพัฒนาเว็บ | เครื่องมือผิดทั้งหมด | JavaScript, Go, Python |
| วิทยาศาสตร์ข้อมูล / ML | ไม่มีระบบนิเวศสำหรับสิ่งนี้ | ไพธอน, อาร์, จูเลีย |
---

## มาตรฐานซี
| มาตรฐาน | ปี | การเพิ่มที่สำคัญ |
|----------|-|--------------|
| C89/C90 | 1989/1990 | ANSI C ดั้งเดิม -- ยังคงเป็นพื้นฐาน |
| C99 | 1999 | // ความคิดเห็น, ประเภทบูล, อาร์เรย์ที่มีความยาวผันแปรได้, อินไลน์, stdint.h |
| C11 | 2554 | การดำเนินการของอะตอมมิก, เธรด, โครงสร้างที่ไม่ระบุชื่อ, _Generic |
| C17 | 2018 | แก้ไขข้อผิดพลาดและชี้แจง (ไม่มีคุณสมบัติใหม่) |
| C23 | 2024 | nullptr, typeof, constexpr, ตัวประมวลผลล่วงหน้าที่ได้รับการปรับปรุง |
รหัสการผลิตส่วนใหญ่กำหนดเป้าหมายไปที่ C11 หรือ C17 C23 นำเสนอสิ่งอำนวยความสะดวกที่ทันสมัย ​​แต่การยอมรับต้องใช้เวลา
---

## สรุป
C คือรากฐานของคอมพิวเตอร์ยุคใหม่ ช่วยให้คุณควบคุมฮาร์ดแวร์ได้สูงสุดโดยมีค่าใช้จ่ายด้านนามธรรมน้อยที่สุด ค่าใช้จ่ายในการควบคุมนั้นเป็นความรับผิดชอบ คุณจัดการหน่วยความจำ ตรวจสอบขอบเขต และจัดการข้อผิดพลาดด้วยตนเอง สำหรับการเขียนโปรแกรมระบบ การพัฒนาแบบฝัง และข้อจำกัดด้านประสิทธิภาพและทรัพยากรทุกที่ C ยังคงไม่มีใครเทียบได้ สำหรับทุกสิ่งทุกอย่าง ภาษาระดับสูงที่สร้างจากภาษา C มักจะเป็นตัวเลือกที่มีประสิทธิผลมากกว่า