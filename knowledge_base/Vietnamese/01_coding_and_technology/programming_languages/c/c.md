<!--
---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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

-->
# C
C là ngôn ngữ lập trình thủ tục, có mục đích chung được tạo bởi Dennis Ritchie tại Bell Labs từ năm 1969 đến năm 1973. Nó được thiết kế để triển khai hệ điều hành Unix và nó vẫn là một trong những ngôn ngữ lập trình được sử dụng rộng rãi nhất trong hơn 50 năm sau. C cung cấp khả năng truy cập bộ nhớ cấp thấp, một thư viện tiêu chuẩn tối thiểu và ánh xạ rõ ràng tới các lệnh máy -- khiến nó trở thành nền tảng cho hầu hết các máy tính hiện đại được xây dựng.
C là ngôn ngữ đằng sau các hệ điều hành (Linux, nhân Windows, macOS), hệ thống nhúng, công cụ cơ sở dữ liệu (SQLite, PostgreSQL), trình biên dịch (CPython của Python, MRI của Ruby) và hầu như mọi thời gian chạy ngôn ngữ lập trình khác. Hiểu C là hiểu cách máy tính thực sự hoạt động.
---

## Tại sao C lại quan trọng
- **Gần với phần cứng**: C ánh xạ gần với mã máy. Không có trình thu gom rác, không có chi phí thời gian chạy, không có phân bổ ẩn.
- **Tính phổ biến**: Từ bộ vi điều khiển đến siêu máy tính, C chạy khắp mọi nơi.
- **Nền tảng điện toán**: Linux, Windows, nhân macOS, trình thông dịch Python, SQLite, Git -- tất cả đều được viết bằng C.
- **Hiệu suất**: Tốc độ thực thi gần như tối ưu với toàn quyền kiểm soát bố cục bộ nhớ.
- **Ảnh hưởng**: Cú pháp và khái niệm của C (con trỏ, mảng, cấu trúc, hàm) đã định hình C++, Java, C#, JavaScript, Go, Rust và hầu hết các ngôn ngữ tiếp theo.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Quản lý bộ nhớ thủ công** | Không có trình thu gom rác - bạn tự phân bổ và giải phóng bộ nhớ | Sử dụng cẩn thận malloc/free; Các mẫu RAII trong C++ |
| **Tràn bộ đệm** | Không có giới hạn kiểm tra trên mảng -- dễ dàng ghi vào cuối bộ đệm | Sử dụng strncpy thay vì strcpy; kích hoạt cảnh báo trình biên dịch |
| **Không có OOP tích hợp** | Chỉ thủ tục - không có lớp, kế thừa hoặc phương thức | Sử dụng cấu trúc + con trỏ hàm; hoặc chuyển sang C++ |
| **Thư viện tiêu chuẩn có giới hạn** | Chức năng tích hợp tối thiểu | Thư viện của bên thứ ba hoặc viết của riêng bạn |
| **Hành vi không xác định** | Nhiều lỗi biên dịch tốt nhưng bị lỗi khó lường | Sử dụng chất khử trùng, máy phân tích tĩnh điện |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
Mọi chương trình C đều bắt đầu tại`main()`. Ngôn ngữ được biên dịch - mã nguồn trở thành mã máy thông qua trình biên dịch (GCC, Clang, MSVC).
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

### Biến và kiểu
C được gõ tĩnh - mỗi biến có một kiểu cố định được biết đến tại thời điểm biên dịch.
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

### Con trỏ
Con trỏ là tính năng mạnh mẽ nhất và dễ bị hiểu lầm nhất của C. Một con trỏ chứa một địa chỉ bộ nhớ.
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

### Luồng điều khiển
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

### Hàm và ngăn xếp
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

## Bố cục bộ nhớ
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

| Vùng | Có Gì Ở Đó | Trọn đời | Ai quản lý nó |
|--------|-------|----------|----------------|
| **Chồng** | Biến cục bộ, tham số hàm | Cho đến khi hàm trả về | Trình biên dịch (tự động) |
| **Đống** | phân bổ malloc/calloc | Cho đến khi bạn gọi free() | Bạn (thủ công) |
| **Dữ liệu/BSS** | Biến toàn cục và tĩnh | Toàn bộ thời gian sử dụng chương trình | Trình biên dịch (tự động) |
| **Văn bản** | Mã máy | Toàn bộ thời gian sử dụng chương trình | Chỉ đọc |
---

## Thư viện chuẩn
| Tiêu đề | Mục đích | Chức năng chung |
|--------|----------|--------|
| `<stdio.h>`| Đầu vào/đầu ra | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Tiện ích chung | malloc, miễn phí, thoát, atoi, rand, qsort |
| `<string.h>`| Hoạt động chuỗi | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Toán học | sin, cos, sqrt, pow, fabs, trần, sàn |
| `<ctype.h>`| Phân loại nhân vật | isalpha, isdigit, toupper, tower |
| `<time.h>`| Ngày giờ | thời gian, đồng hồ, chênh lệch thời gian, strftime |
| `<assert.h>`| Xác nhận gỡ lỗi | khẳng định(điều kiện) |
| `<errno.h>`| Mã lỗi | errno, perror, strerror |
---

## Cú pháp & Mẫu nâng cao
### Macro tiền xử lý
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

### Con trỏ hàm và lệnh gọi lại
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

### Mẫu xử lý lỗi tùy chỉnh
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

## Đồng thời & Song song
### Chủ đề POSIX (pthread)
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

### Mutex và trạng thái chia sẻ
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

### C11 Nguyên tử và Chủ đề
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

###Tập tin tạo
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

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Kiểm tra đơn vị với một khung đơn giản
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

## Khả năng tương tác
### Gọi C từ Python (ctypes)
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

### Gọi C từ các ngôn ngữ khác
| Ngôn ngữ | Cơ chế | Ví dụ |
|----------|-------------|----------|
| Python | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| Ruby | Fiddle | `Fiddle.dlopen("./lib.so")`|
| Java | JNI | `System.loadLibrary("mylib")`|
| C++ | bên ngoài "C" | `extern "C" void my_func();`|
| rỉ sét | bên ngoài "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Mẫu thiết kế
### Con trỏ mờ (Thành ngữ Pimpl trong C)
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

### Bảng ảo (OOP trong C)
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Biên dịch chéo
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Triển khai Docker
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

## Các mẫu và thành ngữ phổ biến
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

## Biên dịch và tạo công cụ
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Công cụ | Mục đích |
|------|----------|
| **GCC / Clang** | Trình biên dịch |
| **Tạo / CMake** | Xây dựng hệ thống |
| **GDB** | Trình gỡ lỗi |
| **Valgrind** | Trình phát hiện lỗi bộ nhớ (rò rỉ, truy cập không hợp lệ) |
| **Khử trùng địa chỉ** | Kiểm tra bộ nhớ thời gian biên dịch |
| **cppcheck** | Phân tích tĩnh |
| **định dạng clang** | Định dạng mã |
---

## Khi nào nên sử dụng C
| Kịch bản | Tại sao C | Thay thế tốt hơn |
|----------|-------|-------------------|
| Hệ điều hành | Truy cập phần cứng trực tiếp, không tốn phí thời gian chạy | -- |
| Hệ thống nhúng / vi điều khiển | Dấu chân tối thiểu, chạy trên mọi thứ | Rust dành cho nhúng quan trọng về an toàn |
| Công cụ cơ sở dữ liệu | Hiệu suất tối đa, kiểm soát toàn bộ bộ nhớ | -- |
| Trình biên dịch và phiên dịch | Nhanh chóng, di động, hiểu rõ | C++ cho các dự án biên dịch lớn hơn |
| Trình điều khiển thiết bị | Được yêu cầu bởi hầu hết các API nhân hệ điều hành | -- |
| Thư viện quan trọng về hiệu suất | Tốc độ gần tối ưu | Rust để đảm bảo an toàn cho bộ nhớ |
| Phát triển ứng dụng chung | Quá nhiều công việc thủ công | Python, Java, Go, C# |
| Phát triển web | Công cụ sai hoàn toàn | JavaScript, Đi, Python |
| Khoa học dữ liệu / ML | Không có hệ sinh thái cho việc này | Python, R, Julia |
---

##C Tiêu chuẩn
| Tiêu chuẩn | Năm | Bổ sung chính |
|----------|------|--------------|
| C89/C90 | 1989/1990 | ANSI C ban đầu -- vẫn là đường cơ sở |
| C99 | 1999 | // nhận xét, kiểu bool, mảng có độ dài thay đổi, nội tuyến, stdint.h |
| C11 | 2011 | Hoạt động nguyên tử, chủ đề, cấu trúc ẩn danh, _Generic |
| C17 | 2018 | Sửa lỗi và làm rõ (không có tính năng mới) |
| C23 | 2024 | nullptr, typeof, constexpr, bộ tiền xử lý cải tiến |
Hầu hết mã sản xuất đều nhắm đến C11 hoặc C17. C23 mang lại tiện ích hiện đại nhưng việc áp dụng cần có thời gian.
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa con trỏ và mảng trong C là gì?
**A:** Mảng và con trỏ có liên quan nhưng khác nhau. Mảng là một khối bộ nhớ liền kề có kích thước cố định được xác định tại thời điểm biên dịch. Con trỏ là một biến chứa địa chỉ bộ nhớ. Mảng phân rã thành con trỏ khi được truyền cho các hàm, nhưng`sizeof(array)`cho biết tổng kích thước trong khi`sizeof(pointer)`chỉ cung cấp kích thước con trỏ (4 hoặc 8 byte). Tên mảng không phải là giá trị có thể sửa đổi - bạn không thể thực hiện`arr++`.
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

### Câu 2: Làm cách nào để quản lý bộ nhớ đúng cách và tránh rò rỉ?
**A:** Mỗi`malloc`/`calloc`phải có`free`tương ứng. Các lỗi thường gặp: quên giải phóng (rò rỉ), giải phóng hai lần (hành vi không xác định), sử dụng bộ nhớ sau khi giải phóng (use-after-free) và không kiểm tra giá trị trả về`malloc`(NULL khi thất bại). Cách thực hành tốt nhất: phân bổ và giải phóng trong cùng một mô-đun, sử dụng mẫu "dọn dẹp goto" để xử lý lỗi và luôn đặt con trỏ giải phóng thành NULL.
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

### Câu 3: Cách tốt nhất để xử lý lỗi trong C là gì?
**A:** C không có ngoại lệ. Xử lý lỗi sử dụng các giá trị trả về (mã lỗi, con trỏ NULL, giá trị âm). Mẫu chuẩn: các hàm trả về mã trạng thái hoặc NULL khi bị lỗi và đặt`errno`cho các lệnh gọi hệ thống. Sử dụng mẫu "goto cleanup" để dọn dẹp tài nguyên khi có lỗi. Luôn kiểm tra các giá trị trả về của`malloc`,`fopen`và các hàm khác có thể bị lỗi.
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

### Câu hỏi 4: Cấu trúc, liên kết và trường bit khác nhau như thế nào trong cách bố trí bộ nhớ?
**A:** Cấu trúc sắp xếp các thành viên một cách tuần tự với phần đệm có thể có để căn chỉnh. Các liên minh xếp chồng tất cả các thành viên tại cùng một vị trí bộ nhớ - kích thước bằng thành viên lớn nhất. Bitfield gói nhiều giá trị vào một số nguyên duy nhất. Cấu trúc dành cho dữ liệu không đồng nhất, các kết hợp để sắp xếp kiểu hoặc tiết kiệm dung lượng khi chỉ có một trường hoạt động và các trường bit để lưu trữ cờ nhỏ gọn.
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

### Câu 5: Con trỏ hàm là gì và khi nào tôi nên sử dụng chúng?
**A:** Con trỏ hàm lưu trữ địa chỉ của hàm và cho phép gọi lại, đa hình và kiến ​​trúc plugin. Chúng là nền tảng trong cách tiếp cận của C đối với các hàm bậc cao hơn (như`qsort`,`bsearch`). Khai báo chúng theo cú pháp: `return_type (*name)(parameter_types)`.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Bài toán 1: Triển khai mảng động (Vector)
**Báo cáo vấn đề:** Triển khai một mảng động trong C tự động phát triển khi các phần tử được thêm vào, hỗ trợ phần bổ sung khấu hao O(1) và cung cấp khả năng dọn dẹp thích hợp. Đây là C tương đương với C++`std::vector`.
**Bước 1 — Tìm hiểu vấn đề:**
Mảng động cần: (1) bộ đệm được phân bổ heap, (2) theo dõi kích thước (các phần tử đã sử dụng) và dung lượng (các vị trí được phân bổ), (3) phân bổ lại khi kích thước đạt đến dung lượng, (4) dọn dẹp bộ nhớ thích hợp. Hệ số tăng trưởng gấp 2 lần sẽ mang lại phần bổ sung khấu hao O(1).
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`malloc`để phân bổ ban đầu,`realloc`để tăng trưởng.
- Lưu trữ con trỏ dữ liệu, kích thước và dung lượng trong struct.
- Tăng trưởng gấp đôi công suất khi`size == capacity`.
- Cung cấp các hoạt động`push`,`pop`,`get`,`set`và `free`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Phân bổ O(1) push: nhân đôi nghĩa là mỗi phần tử được sao chép tổng cộng tối đa O(log n) lần.
- Việc kiểm tra giới hạn trong`vec_get`và`vec_pop`sẽ sớm phát hiện lỗi — cần thiết trong C nơi không có mạng an toàn khi chạy.
- Bộ nhớ: sau 100 lần đẩy bắt đầu từ dung lượng 4, dung lượng đạt 128 (4→8→16→32→64→128).
- Sản xuất: sử dụng`shrink_to_fit`(realloc theo kích thước chính xác) khi phát triển xong để lấy lại bộ nhớ chưa sử dụng.
### Bài toán 2: Xây dựng bảng băm đơn giản
**Báo cáo vấn đề:** Triển khai bảng băm với các khóa chuỗi và giá trị số nguyên bằng cách sử dụng chuỗi riêng biệt để giải quyết xung đột. Hỗ trợ các thao tác chèn, tra cứu và xóa.
**Bước 1 — Tìm hiểu vấn đề:**
Bảng băm ánh xạ các khóa tới các chỉ mục mảng thông qua hàm băm. Các va chạm (các khóa khác nhau ánh xạ tới cùng một chỉ mục) được giải quyết bằng chuỗi riêng biệt: mỗi nhóm là một danh sách các mục được liên kết. Chúng ta cần: hàm băm, chèn, tra cứu, xóa và dọn dẹp.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng hàm băm FNV-1a để phân phối khóa chuỗi tốt.
- Mảng con trỏ xô (đầu danh sách liên kết).
- Theo dõi hệ số tải; thay đổi kích thước khi hệ số tải vượt quá ngưỡng.
- Tất cả các phép toán đều có giá trị trung bình là O(1), trường hợp xấu nhất là O(n).
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Trung bình O(1) cho thao tác chèn/tra cứu/xóa với hàm băm tốt và hệ số tải hợp lý.
- FNV-1a cung cấp khả năng phân phối tuyệt vời cho các khóa chuỗi với khả năng tính toán tối thiểu.
- Kỹ thuật con trỏ tới con trỏ (`Entry **pp`) trong`hashmap_remove`xử lý một cách tinh tế cả việc xóa đầu danh sách và giữa danh sách mà không gặp trường hợp đặc biệt nào.
- Sản xuất: thêm tính năng thử lại khi hệ số tải vượt quá ngưỡng. Sử dụng địa chỉ mở (thăm dò tuyến tính) để có hiệu suất bộ đệm tốt hơn.
### Vấn đề 3: Triển khai bộ đệm vòng cho nhà sản xuất-người tiêu dùng
**Báo cáo vấn đề:** Triển khai bộ đệm vòng dành cho người tiêu dùng đơn lẻ dành cho một nhà sản xuất không khóa trong C để giao tiếp giữa các luồng hiệu suất cao mà không cần phân bổ động trong quá trình hoạt động.
**Bước 1 — Tìm hiểu vấn đề:**
Bộ đệm vòng (bộ đệm tròn) sử dụng mảng có kích thước cố định với các chỉ số đọc và ghi. Khi bộ đệm đầy, người ghi sẽ chặn hoặc ghi đè. Đối với SPSC (người tiêu dùng đơn một nhà sản xuất), chúng ta có thể sử dụng các thao tác nguyên tử thay vì khóa để có thông lượng tối đa.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Mảng có kích thước cố định được phân bổ một lần khi khởi tạo.
-`head`(vị trí đọc) và`tail`(vị trí ghi) là chỉ số nguyên tử.
- Tiến bộ của nhà sản xuất`tail`; tiến bộ của người tiêu dùng `head`.
- Bộ đệm trống khi `head == tail`; đầy khi`(tail + 1) % capacity == head`.
- Sử dụng nguyên tử C11 với thứ tự bộ nhớ phù hợp.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Không khóa: chỉ hoạt động nguyên tử - không có mutex, không chuyển đổi ngữ cảnh.
- Thứ tự bộ nhớ:`release`khi ghi đảm bảo dữ liệu được hiển thị trước khi cập nhật chỉ mục; `acquire`khi đọc đảm bảo chúng ta nhìn thấy dữ liệu sau khi đọc chỉ mục.
- Công suất Power-of-2: bật`& (capacity - 1)`thay vì`% capacity`— nhanh hơn đáng kể.
- Thông lượng: hàng tỷ thao tác mỗi giây trên phần cứng hiện đại.
- Sản xuất: thêm phần đệm giữa`head`và`tail`để ngăn chặn việc chia sẻ sai (mỗi phần trên dòng bộ đệm riêng).
---

## Bản tóm tắt
C là nền tảng của điện toán hiện đại. Nó cho phép bạn kiểm soát tối đa phần cứng với chi phí trừu tượng tối thiểu. Cái giá của việc kiểm soát đó là trách nhiệm -- bạn quản lý bộ nhớ, kiểm tra giới hạn và tự mình xử lý lỗi. Đối với lập trình hệ thống, phát triển nhúng và bất kỳ nơi nào có vấn đề về hiệu suất và hạn chế về tài nguyên, C vẫn không thể so sánh được. Đối với mọi thứ khác, các ngôn ngữ cấp cao hơn được xây dựng dựa trên C thường là những lựa chọn hiệu quả hơn.