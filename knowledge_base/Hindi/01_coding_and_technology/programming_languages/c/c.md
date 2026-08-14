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
# सी
सी एक सामान्य-प्रयोजन, प्रक्रियात्मक प्रोग्रामिंग भाषा है जिसे 1969 और 1973 के बीच बेल लैब्स में डेनिस रिची द्वारा बनाया गया था। इसे यूनिक्स ऑपरेटिंग सिस्टम को लागू करने के लिए डिज़ाइन किया गया था, और यह 50 वर्षों के बाद भी सबसे व्यापक रूप से उपयोग की जाने वाली प्रोग्रामिंग भाषाओं में से एक बनी हुई है। सी निम्न-स्तरीय मेमोरी एक्सेस, एक न्यूनतम मानक लाइब्रेरी और मशीन निर्देशों के लिए एक साफ मैपिंग प्रदान करता है - जिससे यह वह आधार बन जाता है जिस पर अधिकांश आधुनिक कंप्यूटिंग का निर्माण किया जाता है।
C ऑपरेटिंग सिस्टम (लिनक्स, विंडोज कर्नेल, macOS), एम्बेडेड सिस्टम, डेटाबेस इंजन (SQLite, PostgreSQL), कंपाइलर (पायथन का CPython, रूबी का MRI), और वस्तुतः हर अन्य प्रोग्रामिंग भाषा रनटाइम के पीछे की भाषा है। सी को समझने का मतलब यह समझना है कि कंप्यूटर वास्तव में कैसे काम करते हैं।
---

## सी क्यों मायने रखता है
- **हार्डवेयर से निकटता**: सी मशीन कोड के करीब मैप करता है। कोई कचरा संग्रहकर्ता नहीं है, कोई रनटाइम ओवरहेड नहीं है, कोई छिपा हुआ आवंटन नहीं है।
- **सर्वव्यापकता**: माइक्रोकंट्रोलर से लेकर सुपर कंप्यूटर तक, C हर जगह चलता है।
- **कंप्यूटिंग का आधार**: Linux, Windows, macOS कर्नेल, Python इंटरप्रेटर, SQLite, Git - सभी C में लिखे गए हैं।
- **प्रदर्शन**: मेमोरी लेआउट पर पूर्ण नियंत्रण के साथ लगभग इष्टतम निष्पादन गति।
- **प्रभाव**: सी के सिंटैक्स और अवधारणाओं (पॉइंटर्स, एरे, स्ट्रक्चर्स, फ़ंक्शंस) ने सी++, जावा, सी#, जावास्क्रिप्ट, गो, रस्ट और उसके बाद आने वाली अधिकांश भाषाओं को आकार दिया।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **मैन्युअल मेमोरी प्रबंधन** | कोई कचरा संग्रहकर्ता नहीं - आप स्वयं मेमोरी आवंटित और मुक्त करते हैं | मॉलोक/फ्री का सावधानीपूर्वक उपयोग; C++ में RAII पैटर्न |
| **बफर ओवरफ्लो** | सरणियों पर जाँच की कोई सीमा नहीं - पिछले बफ़र सिरों को लिखना आसान है | strcpy के बजाय strncpy का प्रयोग करें; संकलक चेतावनियाँ सक्षम करें |
| **कोई अंतर्निहित OOP नहीं** | केवल प्रक्रियात्मक -- कोई वर्ग, वंशानुक्रम या विधियाँ नहीं | स्ट्रक्चर्स + फ़ंक्शन पॉइंटर्स का उपयोग करें; या C++ पर स्विच करें |
| **सीमित मानक पुस्तकालय** | न्यूनतम अंतर्निहित कार्यक्षमता | तृतीय-पक्ष पुस्तकालय या अपना स्वयं का लिखें |
| **अपरिभाषित व्यवहार** | कई गलतियाँ ठीक से संकलित होती हैं लेकिन अप्रत्याशित रूप से क्रैश हो जाती हैं | सैनिटाइज़र, स्टेटिक एनालाइज़र का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
प्रत्येक C प्रोग्राम`main()`से शुरू होता है। भाषा संकलित की जाती है - स्रोत कोड एक कंपाइलर (जीसीसी, क्लैंग, एमएसवीसी) के माध्यम से मशीन कोड बन जाता है।
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

### चर और प्रकार
C स्थिर रूप से टाइप किया गया है - प्रत्येक वेरिएबल का एक निश्चित प्रकार होता है जिसे संकलन समय पर जाना जाता है।
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

### सूचक
पॉइंटर्स सी की सबसे शक्तिशाली और सबसे गलत समझी जाने वाली विशेषता है। एक पॉइंटर एक मेमोरी एड्रेस रखता है।
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

### प्रवाह को नियंत्रित करें
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

### फ़ंक्शंस और स्टैक
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

## मेमोरी लेआउट
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

| क्षेत्र | वहां क्या होता है | जीवनकाल | इसका प्रबंधन कौन करता है |
|--------|----------------|-------|----------------|
| **स्टैक** | स्थानीय चर, फ़ंक्शन पैरामीटर | फ़ंक्शन वापस आने तक | कंपाइलर (स्वचालित) |
| **ढेर** | मॉलोक/कैलोक आवंटन | जब तक आप free() | पर कॉल नहीं करते आप (मैनुअल) |
| **डेटा/बीएसएस** | वैश्विक और स्थैतिक चर | संपूर्ण कार्यक्रम जीवनकाल | कंपाइलर (स्वचालित) |
| **पाठ** | मशीन कोड | संपूर्ण कार्यक्रम जीवनकाल | केवल पढ़ने के लिए |
---

## मानक पुस्तकालय
| हेडर | उद्देश्य | सामान्य कार्य |
|--------|--------||
| `<stdio.h>`| इनपुट/आउटपुट | प्रिंटफ, स्कैनएफ, फॉपेन, एफगेट्स, एफप्रिंटफ |
| `<stdlib.h>`| सामान्य उपयोगिताएँ | मॉलोक, फ्री, एग्जिट, एटोई, रैंड, क्यूसॉर्ट |
| `<string.h>`| स्ट्रिंग ऑपरेशन | स्ट्रलेन, स्ट्रैपी, स्ट्रंकपी, स्ट्रैम्प, मेम्सीपीई |
| `<math.h>`| गणित | पाप, क्योंकि, sqrt, पाउ, फैब्स, छत, फर्श |
| `<ctype.h>`| चरित्र वर्गीकरण | इसाल्फा, इसडिजिट, टॉपर, टोलोअर |
| `<time.h>`| दिनांक और समय | समय, घड़ी, अंतरसमय, स्ट्रफ़टाइम |
| `<assert.h>`| डिबगिंग दावे | जोर (शर्त) |
| `<errno.h>`| त्रुटि कोड | इरनो, पेररर, स्ट्रेरर |
---

## उन्नत सिंटैक्स और पैटर्न
### प्रीप्रोसेसर मैक्रोज़
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

### फ़ंक्शन पॉइंटर्स और कॉलबैक
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

### कस्टम त्रुटि प्रबंधन पैटर्न
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

## समवर्ती एवं समांतरता
### POSIX थ्रेड्स (pthreads)
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

### म्यूटेक्स और साझा स्थिति
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

### C11 परमाणु और धागे
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### मेकफ़ाइल
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### एक सरल रूपरेखा के साथ इकाई परीक्षण
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

## अंतरसंचालनीयता
### पायथन से C को कॉल करना (ctypes)
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

### अन्य भाषाओं से C को कॉल करना
| भाषा | तंत्र | उदाहरण |
|---|----|---|
| पायथन | सीटाइप्स, सीएफएफआई | `ctypes.CDLL("./lib.so")`|
| रूबी | बेला | `Fiddle.dlopen("./lib.so")`|
| जावा | जेएनआई | `System.loadLibrary("mylib")`|
| सी++ | बाहरी "सी" | `extern "C" void my_func();`|
| जंग | बाहरी "सी" + एफएफआई | `extern "C" { fn my_func(); }`|
---

## डिज़ाइन पैटर्न
### अपारदर्शी सूचक (सी में पिंपल मुहावरा)
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

### वर्चुअल टेबल (सी में ओओपी)
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

## तैनाती
### क्रॉस-संकलन
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### डॉकर परिनियोजन
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

## सामान्य पैटर्न और मुहावरे
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

## संकलन और टूलींग
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| उपकरण | उद्देश्य |
|------|---------|
| **जीसीसी/क्लैंग** | संकलक |
| **बनाओ/सीमेक** | सिस्टम बनाएं |
| **जीडीबी** | डिबगर |
| **वालग्रिंड** | मेमोरी त्रुटि डिटेक्टर (लीक, अमान्य पहुंच) |
| **एड्रेस सेनिटाइजर** | संकलन-समय स्मृति जाँच |
| **cppcheck** | स्थैतिक विश्लेषण |
| **क्लैंग-प्रारूप** | कोड फ़ॉर्मेटिंग |
---

## सी का उपयोग कब करें
| परिदृश्य | क्यों सी | बेहतर विकल्प |
|---|-------|-------------------|
| ऑपरेटिंग सिस्टम | डायरेक्ट हार्डवेयर एक्सेस, कोई रनटाइम ओवरहेड नहीं | -- |
| एंबेडेड सिस्टम/माइक्रोकंट्रोलर | न्यूनतम पदचिह्न, किसी भी चीज़ पर चलता है | सुरक्षा के लिए जंग-महत्वपूर्ण एम्बेडेड |
| डेटाबेस इंजन | अधिकतम प्रदर्शन, पूर्ण मेमोरी नियंत्रण | -- |
| संकलनकर्ता और दुभाषिए | तेज़, पोर्टेबल, अच्छी तरह से समझा गया | बड़े कंपाइलर प्रोजेक्ट के लिए C++ |
| डिवाइस ड्राइवर | अधिकांश OS कर्नेल API द्वारा आवश्यक | -- |
| प्रदर्शन-महत्वपूर्ण पुस्तकालय | लगभग-इष्टतम गति | गारंटीशुदा स्मृति सुरक्षा के लिए जंग |
| सामान्य अनुप्रयोग विकास | बहुत ज्यादा मैन्युअल काम | पायथन, जावा, गो, सी# |
| वेब विकास | पूरी तरह से गलत उपकरण | जावास्क्रिप्ट, गो, पायथन |
| डेटा साइंस/एमएल | इसके लिए कोई पारिस्थितिकी तंत्र नहीं | पायथन, आर, जूलिया |
---

## सी मानक
| मानक | वर्ष | मुख्य परिवर्धन |
|---|------|----|
| C89/C90 | 1989/1990 | मूल एएनएसआई सी - अभी भी आधार रेखा |
| C99 | 1999 | // टिप्पणियाँ, बूल प्रकार, चर-लंबाई सरणियाँ, इनलाइन, stdint.h |
| सी11 | 2011 | परमाणु संचालन, धागे, अनाम संरचनाएं, _जेनेरिक |
| सी17 | 2018 | बग समाधान और स्पष्टीकरण (कोई नई सुविधाएँ नहीं) |
| सी23 | 2024 | nullptr, typeof, constexpr, बेहतर प्रीप्रोसेसर |
अधिकांश उत्पादन कोड C11 या C17 को लक्षित करते हैं। C23 आधुनिक सुविधाएं लाता है लेकिन अपनाने में समय लगता है।
---

## सिंथेटिक प्रश्नोत्तर
### Q1: C में पॉइंटर्स और ऐरे के बीच क्या अंतर है?
**ए:** ऐरे और पॉइंटर्स संबंधित हैं लेकिन अलग-अलग हैं। एक सारणी मेमोरी का एक सन्निहित ब्लॉक है जिसका एक निश्चित आकार संकलन समय पर ज्ञात होता है। पॉइंटर एक वेरिएबल है जो मेमोरी एड्रेस रखता है। फ़ंक्शंस में पास होने पर ऐरे पॉइंटर्स में बदल जाते हैं, लेकिन`sizeof(array)`कुल आकार देता है जबकि`sizeof(pointer)`केवल पॉइंटर आकार (4 या 8 बाइट्स) देता है। सरणी नाम परिवर्तनीय मान नहीं हैं - आप`arr++`नहीं कर सकते।
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

### Q2: मैं मेमोरी को ठीक से कैसे प्रबंधित करूं और लीक से कैसे बचूं?
**ए:** प्रत्येक`malloc`/`calloc`में एक संगत`free`होना चाहिए। सामान्य गलतियाँ: फ्री करना भूल जाना (रिसाव), दो बार फ्री करना (अपरिभाषित व्यवहार), फ्री करने के बाद मेमोरी का उपयोग करना (उपयोग-बाद-फ्री), और`malloc`रिटर्न वैल्यू की जाँच न करना (विफलता पर शून्य)। सर्वोत्तम अभ्यास: एक ही मॉड्यूल में आवंटित और मुक्त करें, त्रुटि प्रबंधन के लिए "गोटो क्लीनअप" पैटर्न का उपयोग करें, और मुक्त पॉइंटर्स को हमेशा NULL पर सेट करें।
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

### Q3: C में त्रुटि प्रबंधन के लिए सर्वोत्तम अभ्यास क्या हैं?
**ए:** सी में कोई अपवाद नहीं है। त्रुटि प्रबंधन रिटर्न मान (त्रुटि कोड, NULL पॉइंटर्स, नकारात्मक मान) का उपयोग करता है। मानक पैटर्न: फ़ंक्शंस विफलता पर एक स्थिति कोड या NULL लौटाते हैं, और सिस्टम कॉल के लिए`errno`सेट करते हैं। त्रुटियों पर संसाधन सफाई के लिए "गोटो क्लीनअप" पैटर्न का उपयोग करें। हमेशा`malloc`,`fopen`और अन्य फ़ंक्शंस के रिटर्न मानों की जांच करें जो विफल हो सकते हैं।
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

### Q4: मेमोरी लेआउट में स्ट्रक्चर, यूनियन और बिटफील्ड कैसे भिन्न होते हैं?
**ए:** संरचनाएं संरेखण के लिए संभावित पैडिंग के साथ सदस्यों को क्रमिक रूप से प्रस्तुत करती हैं। यूनियन सभी सदस्यों को एक ही मेमोरी स्थान पर ओवरले करती है - आकार सबसे बड़े सदस्य के बराबर होता है। बिटफ़ील्ड एकाधिक मानों को एक पूर्णांक में पैक करते हैं। संरचनाएं विषम डेटा के लिए हैं, केवल एक फ़ील्ड सक्रिय होने पर टाइप-पनिंग या स्थान बचाने के लिए यूनियनें हैं, और कॉम्पैक्ट फ़्लैग स्टोरेज के लिए बिटफ़ील्ड हैं।
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

### Q5: फ़ंक्शन पॉइंटर्स क्या हैं, और मुझे उनका उपयोग कब करना चाहिए?
**ए:** फ़ंक्शन पॉइंटर्स किसी फ़ंक्शन का पता संग्रहीत करते हैं और कॉलबैक, बहुरूपता और प्लगइन आर्किटेक्चर को सक्षम करते हैं। वे उच्च-क्रम के कार्यों (जैसे `qsort`, `bsearch`) के लिए C के दृष्टिकोण की नींव हैं। उन्हें सिंटैक्स के साथ घोषित करें: `return_type (*name)(parameter_types)`।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक गतिशील सरणी (वेक्टर) लागू करें
**समस्या कथन:** C में एक गतिशील सरणी लागू करें जो तत्वों को जोड़ने पर स्वचालित रूप से बढ़ती है, O(1) परिशोधित परिशिष्ट का समर्थन करती है, और उचित सफाई प्रदान करती है। यह C++`std::vector`का C समकक्ष है।
**चरण 1 - समस्या को समझें:**
एक गतिशील सरणी की आवश्यकता है: (1) एक ढेर-आवंटित बफर, (2) आकार (प्रयुक्त तत्व) और क्षमता (आवंटित स्लॉट) की ट्रैकिंग, (3) आकार क्षमता तक पहुंचने पर पुनः आवंटन, (4) उचित मेमोरी क्लीनअप। 2x का वृद्धि कारक O(1) परिशोधित परिशिष्ट देता है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- प्रारंभिक आवंटन के लिए `malloc`, वृद्धि के लिए`realloc`का उपयोग करें।
- एक संरचना में डेटा पॉइंटर, आकार और क्षमता को स्टोर करें।
-`size == capacity`होने पर क्षमता दोगुनी करके बढ़ें।
-`push`,`pop`,`get`,`set`, और`free`संचालन प्रदान करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- परिशोधित O(1) पुश: दोहरीकरण का मतलब है कि प्रत्येक तत्व को कुल मिलाकर अधिकतम O(लॉग एन) बार कॉपी किया गया है।
-`vec_get`और`vec_pop`में सीमा जांच त्रुटियों को जल्दी पकड़ लेती है - C में आवश्यक है जहां कोई रनटाइम सुरक्षा जाल नहीं है।
- मेमोरी: क्षमता 4 से शुरू करके 100 पुश के बाद, क्षमता 128 (4→8→16→32→64→128) तक पहुंच जाती है।
- उत्पादन: अप्रयुक्त मेमोरी को पुनः प्राप्त करने के लिए बढ़ते समय`shrink_to_fit`(सटीक आकार में रीलोक) का उपयोग करें।
### समस्या 2: एक सरल हैश तालिका बनाएँ
**समस्या कथन:** टकराव समाधान के लिए अलग चेनिंग का उपयोग करके स्ट्रिंग कुंजियों और पूर्णांक मानों के साथ एक हैश तालिका लागू करें। सम्मिलित करने, देखने और हटाने के कार्यों का समर्थन करें।
**चरण 1 - समस्या को समझें:**
एक हैश तालिका हैश फ़ंक्शन के माध्यम से सरणी सूचकांकों की कुंजियों को मैप करती है। टकराव (एक ही सूचकांक पर अलग-अलग कुंजी मैपिंग) को अलग-अलग चेनिंग के साथ हल किया जाता है: प्रत्येक बाल्टी प्रविष्टियों की एक लिंक की गई सूची है। हमें चाहिए: हैश फ़ंक्शन, इंसर्ट, लुकअप, डिलीट और क्लीनअप।
**चरण 2 - दृष्टिकोण को पहचानें:**
- स्ट्रिंग कुंजियों के अच्छे वितरण के लिए FNV-1a हैश का उपयोग करें।
- बकेट पॉइंटर्स की सारणी (लिंक्ड सूची प्रमुख)।
- लोड फैक्टर ट्रैकिंग; जब लोड फैक्टर सीमा से अधिक हो जाए तो आकार बदलें।
- सभी ऑपरेशन O(1) औसत, O(n) सबसे खराब स्थिति में हैं।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- अच्छे हैश फ़ंक्शन और उचित लोड फैक्टर के साथ डालने/लुकअप/डिलीट के लिए औसत ओ(1)।
- FNV-1a न्यूनतम गणना के साथ स्ट्रिंग कुंजियों के लिए उत्कृष्ट वितरण प्रदान करता है।
-`hashmap_remove`में पॉइंटर-टू-पॉइंटर तकनीक (`Entry **pp`) विशेष मामलों के बिना हेड-ऑफ-लिस्ट और मिड-लिस्ट डिलीट दोनों को खूबसूरती से संभालती है।
- उत्पादन: लोड फैक्टर सीमा से अधिक होने पर रीहैशिंग जोड़ें। बेहतर कैश प्रदर्शन के लिए ओपन एड्रेसिंग (रैखिक जांच) का उपयोग करें।
### समस्या 3: निर्माता-उपभोक्ता के लिए रिंग बफ़र लागू करें
**समस्या कथन:** ऑपरेशन के दौरान गतिशील आवंटन के बिना उच्च-प्रदर्शन अंतर-थ्रेड संचार के लिए सी में लॉक-मुक्त एकल-निर्माता एकल-उपभोक्ता रिंग बफर लागू करें।
**चरण 1 - समस्या को समझें:**
एक रिंग बफ़र (गोलाकार बफ़र) पढ़ने और लिखने वाले सूचकांकों के साथ एक निश्चित आकार के सरणी का उपयोग करता है। जब बफ़र भर जाता है, तो लेखक ब्लॉक या ओवरराइट कर देता है। एसपीएससी (एकल-निर्माता एकल-उपभोक्ता) के लिए, हम अधिकतम थ्रूपुट के लिए लॉक के बजाय परमाणु संचालन का उपयोग कर सकते हैं।
**चरण 2 - दृष्टिकोण को पहचानें:**
- प्रारंभ में एक बार निश्चित आकार की सरणी आवंटित की गई।
- परमाणु सूचकांक के रूप में`head`(स्थिति पढ़ें) और`tail`(स्थिति लिखें)।
- निर्माता`tail`को आगे बढ़ाता है; उपभोक्ता अग्रिम `head`।
-`head == tail`होने पर बफर खाली होता है; पूर्ण जब`(tail + 1) % capacity == head`.
- उचित मेमोरी ऑर्डरिंग के साथ C11 एटॉमिक्स का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- लॉक-मुक्त: केवल परमाणु संचालन - कोई म्यूटेक्स नहीं, कोई संदर्भ स्विच नहीं।
- मेमोरी ऑर्डरिंग:`release`लिखने पर यह सुनिश्चित करता है कि डेटा इंडेक्स अपडेट से पहले दिखाई दे;  पढ़ने पर`acquire`यह सुनिश्चित करता है कि हम सूचकांक पढ़ने के बाद डेटा देखें।
- पावर-ऑफ-2 क्षमता:`% capacity`के बजाय`& (capacity - 1)`को सक्षम बनाता है - काफी तेज।
- थ्रूपुट: आधुनिक हार्डवेयर पर प्रति सेकंड अरबों ऑपरेशन।
- उत्पादन: गलत साझाकरण को रोकने के लिए`head`और`tail`के बीच पैडिंग जोड़ें (प्रत्येक अपनी कैश लाइन पर)।
---

## सारांश
सी आधुनिक कंप्यूटिंग का आधार है। यह आपको न्यूनतम अमूर्त ओवरहेड के साथ हार्डवेयर पर अधिकतम नियंत्रण प्रदान करता है। उस नियंत्रण की लागत जिम्मेदारी है - आप मेमोरी का प्रबंधन करते हैं, सीमाओं की जांच करते हैं, और त्रुटियों को स्वयं संभालते हैं। सिस्टम प्रोग्रामिंग, एंबेडेड डेवलपमेंट और कहीं भी प्रदर्शन और संसाधन की कमी के मामले में, सी बेजोड़ है। बाकी सभी चीज़ों के लिए, C के शीर्ष पर निर्मित उच्च-स्तरीय भाषाएँ आमतौर पर अधिक उत्पादक विकल्प होती हैं।