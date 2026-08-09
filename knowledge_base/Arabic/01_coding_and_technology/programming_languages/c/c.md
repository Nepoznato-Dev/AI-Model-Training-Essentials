---
# البيانات الوصفية
العنوان: "ج"
الوصف: "مرجع شامل للغة البرمجة C يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [ج، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "35 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
#ج
لغة C هي لغة برمجة إجرائية ذات أغراض عامة أنشأها دينيس ريتشي في مختبرات بيل بين عامي 1969 و1973. وقد تم تصميمها لتنفيذ نظام التشغيل يونكس، ولا تزال واحدة من لغات البرمجة الأكثر استخدامًا على نطاق واسع بعد أكثر من 50 عامًا. توفر لغة C وصولاً منخفض المستوى إلى الذاكرة، ومكتبة قياسية بسيطة، وتخطيطًا نظيفًا لتعليمات الآلة - مما يجعلها الأساس الذي بنيت عليه معظم الحوسبة الحديثة.
C هي اللغة وراء أنظمة التشغيل (Linux وWindows kernel وmacOS)، والأنظمة المدمجة، ومحركات قواعد البيانات (SQLite، وPostgreSQL)، والمترجمين (Python's CPython، وRuby's MRI)، وكل لغات البرمجة الأخرى تقريبًا. إن فهم لغة C هو فهم كيفية عمل أجهزة الكمبيوتر فعليًا.
---

## لماذا تعتبر لغة C مهمة؟
- **القرب من الأجهزة**: ترتبط لغة C بشكل وثيق برمز الجهاز. لا يوجد أداة تجميع البيانات المهملة، ولا يوجد حمل إضافي في وقت التشغيل، ولا توجد عمليات تخصيص مخفية.
- **التواجد المنتشر**: بدءًا من وحدات التحكم الدقيقة وحتى أجهزة الكمبيوتر العملاقة، تعمل لغة C في كل مكان.
- **أساسيات الحوسبة**: Linux، وWindows، وmacOS kernels، وPython Interpreter، وSQLite، وGit - جميعها مكتوبة بلغة C.
- **الأداء**: سرعة تنفيذ شبه مثالية مع تحكم كامل في تخطيط الذاكرة.
- **التأثير**: بناء جملة لغة C ومفاهيمها (المؤشرات، والمصفوفات، والبنيات، والوظائف) على شكل C++، وJava، وC#، وJavaScript، وGo، وRust، ومعظم اللغات التي تلت ذلك.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **إدارة الذاكرة اليدوية** | لا يوجد أداة تجميع البيانات المهملة - يمكنك تخصيص الذاكرة وتحريرها بنفسك | الاستخدام الدقيق لـ malloc/free؛ أنماط RAII في C++ |
| ** تجاوز سعة المخزن المؤقت ** | لا يوجد حدود للتحقق من المصفوفات - من السهل كتابة نهايات المخزن المؤقت السابقة | استخدم strncpy بدلاً من strcpy؛ تمكين تحذيرات المترجم |
| ** لا يوجد OOP مدمج ** | إجرائية فقط - لا توجد فئات أو وراثة أو طرق | استخدام الهياكل + مؤشرات الوظيفة؛ أو قم بالتبديل إلى C++ |
| **مكتبة قياسية محدودة** | الحد الأدنى من الوظائف المضمنة | مكتبات الطرف الثالث أو اكتب مكتباتك الخاصة |
| **سلوك غير محدد** | يتم تجميع العديد من الأخطاء بشكل جيد ولكنها تتعطل بشكل غير متوقع | استخدم المطهرات والمحللات الساكنة |
---

## أساسيات بناء الجملة
### البنية الأساسية
يبدأ كل برنامج بلغة C عند`main()`. يتم تجميع اللغة - يصبح كود المصدر كود الآلة عبر مترجم (GCC، Clang، MSVC).
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

### المتغيرات والأنواع
تتم كتابة لغة C بشكل ثابت - كل متغير له نوع ثابت معروف في وقت الترجمة.
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

### المؤشرات
المؤشرات هي الميزة الأقوى والأكثر سوء فهم في لغة C. يحمل المؤشر عنوان الذاكرة.
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

### التحكم في التدفق
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

### الوظائف والمكدس
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

## تخطيط الذاكرة
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

| المنطقة | ماذا يحدث هناك | العمر | من يديرها |
|--------|----------------|----------|----------------|
| **كومة** | المتغيرات المحلية، معلمات الدالة | حتى ترجع الدالة | مترجم (تلقائي) |
| ** كومة ** | تخصيصات مالوك/كالوك | حتى تتصل مجانًا () | أنت (دليل) |
| **البيانات/BSS** | المتغيرات العالمية والثابتة | عمر البرنامج بأكمله | مترجم (تلقائي) |
| **النص** | كود الآلة | عمر البرنامج بأكمله | للقراءة فقط |
---

## المكتبة القياسية
| رأس | الغرض | الوظائف المشتركة |
|--------|---------|----------------|
|  __محمي_0__ | الإدخال / الإخراج | printf، scanf، fopen، fgets، fprintf |
|  __محمي_1__ | المرافق العامة | مالوك، مجاني، خروج، أتوي، راند، قسورت |
|  __محمي_2__ | عمليات السلسلة | strlen، strcpy، strncpy، strcmp، memcpy |
|  __محمي_3__ | الرياضيات | الخطيئة، كوس، الجذر التربيعي، الأسرى، القوات المسلحة البوروندية، السقف، الطابق |
|  __محمي_4__ | تصنيف الشخصيات | isalpha، isdigit، ممتاز، tolower |
|  __محمي_5__ | التاريخ والوقت | الوقت، الساعة، difftime، strftime |
|  __محمي_6__ | تصحيح التأكيدات | تأكيد (الشرط) |
|  __محمي_7__ | رموز الخطأ | خطأ، خطأ، خطأ |
---

## بناء الجملة والأنماط المتقدمة
### وحدات الماكرو للمعالج المسبق
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

### مؤشرات الوظائف وعمليات الاسترجاعات
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

### أنماط معالجة الأخطاء المخصصة
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

## التزامن والتوازي
### خيوط POSIX (pthreads)
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

### Mutex والدولة المشتركة
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

### الذرات والخيوط C11
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### ملف تعريفي
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

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### اختبار الوحدة باستخدام إطار عمل بسيط
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

## إمكانية التشغيل البيني
### استدعاء C من بايثون (ctypes)
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

### الاتصال بـ C من لغات أخرى
| اللغة | آلية | مثال |
|----------|----------|---------|
| بايثون | أنواع، CFFI |  __محمي_0__ |
| روبي | كمان |  __محمي_1__ |
| جافا | جيني |  __محمي_2__ |
| سي++ | خارجي "C" |  __محمي_3__ |
| الصدأ | خارجي "C" + FFI |  __محمي_4__ |
---

## أنماط التصميم
### مؤشر معتم (مصطلح Pimpl في لغة C)
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

### الجدول الافتراضي (OOP في لغة C)
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

## الأداء والتحسين
### أدوات التنميط
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

### تقنيات التحسين
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

## النشر
### التجميع المتقاطع
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### نشر عامل الميناء
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

## الأنماط والتعابير الشائعة
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

## التجميع والأدوات
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| أداة | الغرض |
|------|---------|
| ** مجلس التعاون الخليجي / كلانج ** | المجمعون |
| **جعل / CMake** | بناء الأنظمة |
| **جي دي بي** | المصحح |
| ** فالجريند ** | كاشف أخطاء الذاكرة (تسربات، وصول غير صالح) |
| **مطهر العنوان** | فحص الذاكرة في وقت الترجمة |
| **cppcheck** | التحليل الساكن |
| ** تنسيق الرنة ** | تنسيق الكود |
---

## متى يجب استخدام لغة C
| السيناريو | لماذا ج | البديل الأفضل |
|----------|-------|------------------|
| أنظمة التشغيل | الوصول المباشر إلى الأجهزة، بدون أي تكاليف تشغيل إضافية | -- |
| الأنظمة المدمجة / المتحكمات الدقيقة | الحد الأدنى من البصمة، يعمل على أي شيء | الصدأ للسلامة الحرجة المضمنة |
| محركات قواعد البيانات | أقصى أداء، تحكم كامل في الذاكرة | -- |
| مترجمون ومترجمون فوريون | سريع ومحمول ومفهوم جيدًا | C++ لمشاريع المترجم الأكبر |
| برامج تشغيل الأجهزة | مطلوب من قبل معظم واجهات برمجة تطبيقات kernel لنظام التشغيل | -- |
| مكتبات الأداء الحرجة | السرعة شبه المثالية | الصدأ لضمان سلامة الذاكرة |
| تطوير التطبيقات العامة | كثرة العمل اليدوي | بايثون، جافا، غو، C# |
| تطوير الويب | أداة خاطئة تمامًا | جافا سكريبت، اذهب، بايثون |
| علم البيانات / تعلم الآلة | لا يوجد نظام بيئي لهذا | بايثون، ر، جوليا |
---

## معايير ج
| قياسي | سنة | الإضافات الرئيسية |
|----------|------|--------------|
| C89/C90 | 1989/1990 | ANSI C الأصلي - لا يزال خط الأساس |
| C99 | 1999 | // التعليقات، النوع المنطقي، المصفوفات ذات الطول المتغير، المضمنة، stdint.h |
| ج11 | 2011 | العمليات الذرية، المواضيع، الهياكل المجهولة، _عام |
| ج17 | 2018 | إصلاحات الأخطاء وتوضيحاتها (لا توجد ميزات جديدة) |
| ج23 | 2024 | nullptr، typeof، constexpr، معالج مسبق محسّن |
تستهدف معظم أكواد الإنتاج C11 أو C17. يوفر C23 وسائل الراحة الحديثة ولكن اعتمادها يستغرق وقتًا.
---

## ملخص
لغة C هي حجر الأساس للحوسبة الحديثة. فهو يمنحك أقصى قدر من التحكم في الأجهزة مع الحد الأدنى من الحمل الزائد. تكلفة هذا التحكم هي المسؤولية - فأنت تدير الذاكرة وتتحقق من الحدود وتتعامل مع الأخطاء بنفسك. بالنسبة لبرمجة الأنظمة، والتطوير المضمن، وفي أي مكان يهم فيه الأداء وقيود الموارد، تظل لغة C لا مثيل لها. بالنسبة لكل شيء آخر، عادةً ما تكون اللغات ذات المستوى الأعلى المبنية على لغة C خيارات أكثر إنتاجية.