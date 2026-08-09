---
# Metadatos
título: "C"
descripción: "Referencia completa para el lenguaje de programación C que cubre descripción general, compensaciones, fundamentos de sintaxis, ecosistema y cuándo usarlo".
categoría: "Codificación y tecnología"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [c, lenguaje-de-programación, sintaxis, ecosistema, codificación-y-tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "35 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
#C
C es un lenguaje de programación procedimental de propósito general creado por Dennis Ritchie en Bell Labs entre 1969 y 1973. Fue diseñado para implementar el sistema operativo Unix y sigue siendo uno de los lenguajes de programación más utilizados más de 50 años después. C proporciona acceso a memoria de bajo nivel, una biblioteca estándar mínima y una asignación limpia a las instrucciones de la máquina, lo que lo convierte en la base sobre la que se construye la informática más moderna.
C es el lenguaje detrás de los sistemas operativos (Linux, kernel de Windows, macOS), sistemas integrados, motores de bases de datos (SQLite, PostgreSQL), compiladores (CPython de Python, MRI de Ruby) y prácticamente todos los demás lenguajes de programación en tiempo de ejecución. Comprender C es comprender cómo funcionan realmente las computadoras.
---

## Por qué es importante C
- **Proximidad al hardware**: C se corresponde estrechamente con el código de máquina. No hay recolector de basura, ni sobrecarga de tiempo de ejecución, ni asignaciones ocultas.
- **Ubicuidad**: Desde microcontroladores hasta supercomputadoras, C se ejecuta en todas partes.
- **Fundamentos de la informática**: Linux, Windows, kernels de macOS, intérprete de Python, SQLite, Git, todos escritos en C.
- **Rendimiento**: velocidad de ejecución casi óptima con control total sobre el diseño de la memoria.
- **Influencia**: la sintaxis y los conceptos de C (punteros, matrices, estructuras, funciones) dieron forma a C++, Java, C#, JavaScript, Go, Rust y la mayoría de los lenguajes posteriores.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Gestión manual de memoria** | Sin recolector de basura: usted mismo asigna y libera memoria | Uso cuidadoso de malloc/free; Patrones RAII en C++ |
| **Desbordamientos del búfer** | Comprobación sin límites en matrices: fácil de escribir más allá de los extremos del búfer | Utilice strncpy en lugar de strcpy; habilitar advertencias del compilador |
| **Sin programación orientada a objetos integrada** | Sólo de procedimiento: sin clases, herencia ni métodos | Utilice estructuras + punteros de función; o cambiar a C++ |
| **Biblioteca estándar limitada** | Funcionalidad integrada mínima | Bibliotecas de terceros o escribe las tuyas propias |
| **Comportamiento no definido** | Muchos errores se compilan bien pero fallan de manera impredecible | Utilice desinfectantes, analizadores estáticos |
---

## Fundamentos de sintaxis
### Estructura básica
Cada programa en C comienza en `main()`. El lenguaje se compila: el código fuente se convierte en código de máquina mediante un compilador (GCC, Clang, MSVC).
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

### Variables y tipos
C tiene un tipo estático: cada variable tiene un tipo fijo conocido en el momento de la compilación.
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

### Consejos
Los punteros son la característica más poderosa y menos entendida de C. Un puntero contiene una dirección de memoria.
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

### Flujo de control
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

### Funciones y la pila
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

## Diseño de memoria
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

| Región | ¿Qué pasa allí? Toda la vida | Quién lo gestiona |
|--------|----------------|----------|----------------|
| **Pila** | Variables locales, parámetros de función | Hasta que la función regrese | Compilador (automático) |
| **Montón** | asignaciones malloc/calloc | Hasta que llames gratis() | Tú (manual) |
| **Datos/BSS** | Variables globales y estáticas | Toda la vida del programa | Compilador (automático) |
| **Texto** | Código de máquina | Toda la vida del programa | Sólo lectura |
---

## La biblioteca estándar
| Encabezado | Propósito | Funciones comunes |
|--------|---------|-----------------|
| `<stdio.h>`| Entrada/salida | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Utilidades generales | malloc, libre, salida, atoi, rand, qsort |
| `<string.h>`| Operaciones con cadenas | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matemáticas | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| Clasificación de personajes | isalfa, isdigit, toupper, tolower |
| `<time.h>`| Fecha y hora | hora, reloj, difftime, strftime |
| `<assert.h>`| Depuración de afirmaciones | afirmar (condición) |
| `<errno.h>`| Códigos de error | errno, perror, strerror |
---

## Sintaxis y patrones avanzados
### Macros de preprocesador
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

### Punteros de función y devoluciones de llamada
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

### Patrones de manejo de errores personalizados
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

## Concurrencia y paralelismo
### Hilos POSIX (pthreads)
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

### Mutex y estado compartido
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

### C11 Atómicas y subprocesos
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto
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

### Archivo MAKE
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

### Canalización de CI/CD (acciones de GitHub)
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

## Pruebas
### Pruebas unitarias con un marco simple
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

## Interoperabilidad
### Llamar a C desde Python (ctypes)
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

### Llamar a C desde otros idiomas
| Idioma | Mecanismo | Ejemplo |
|----------|-----------|---------|
| Pitón | tipos c, cffi | `ctypes.CDLL("./lib.so")`|
| Rubí | violín | `Fiddle.dlopen("./lib.so")`|
| Java | JNI | `System.loadLibrary("mylib")`|
| C++ | "C" externa | `extern "C" void my_func();`|
| Óxido | externa "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Patrones de diseño
### Puntero opaco (idioma de Pimpl en C)
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

### Tabla virtual (OOP en C)
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Técnicas de optimización
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

## Implementación
### Compilación cruzada
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Implementación de Docker
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

## Patrones y modismos comunes
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

## Compilación y herramientas
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Herramienta | Propósito |
|------|---------|
| **CCG / Sonido metálico** | Compiladores |
| **Crear / CCrear** | Construir sistemas |
| **BGF** | Depurador |
| **Valgrind** | Detector de errores de memoria (fugas, acceso no válido) |
| **Desinfectante de direcciones** | Comprobación de memoria en tiempo de compilación |
| **cppcheck** | Análisis estático |
| **formato clang** | Formato de código |
---

## Cuándo usar C
| Escenario | ¿Por qué C | Mejor alternativa |
|----------|-------|-------------------|
| Sistemas operativos | Acceso directo al hardware, sin sobrecarga de tiempo de ejecución | -- |
| Sistemas integrados / microcontroladores | Huella mínima, funciona con cualquier cosa | Óxido para elementos integrados críticos para la seguridad |
| Motores de bases de datos | Máximo rendimiento, control total de la memoria | -- |
| Compiladores e intérpretes | Rápido, portátil, bien entendido | C++ para proyectos de compiladores más grandes |
| Controladores de dispositivos | Requerido por la mayoría de las API del kernel del sistema operativo | -- |
| Bibliotecas críticas para el rendimiento | Velocidad casi óptima | Óxido para garantizar la seguridad de la memoria |
| Desarrollo de aplicaciones generales | Demasiado trabajo manual | Python, Java, Go, C# |
| Desarrollo web | Herramienta totalmente equivocada | JavaScript, Ir, Python |
| Ciencia de datos / ML | No hay ecosistema para esto | Pitón, R, Julia |
---

## Estándares C
| Estándar | Año | Adiciones clave |
|----------|------|--------------|
| C89/C90 | 1989/1990 | El ANSI C original: sigue siendo la base |
| C99 | 1999 | // comentarios, tipo bool, matrices de longitud variable, en línea, stdint.h |
| C11 | 2011 | Operaciones atómicas, subprocesos, estructuras anónimas, _Generic |
| C17 | 2018 | Corrección de errores y aclaraciones (sin funciones nuevas) |
| C23 | 2024 | nullptr, typeof, constexpr, preprocesador mejorado |
La mayoría del código de producción apunta a C11 o C17. C23 ofrece comodidades modernas, pero su adopción lleva tiempo.
---

## Resumen
C es la base de la informática moderna. Le brinda el máximo control sobre el hardware con una mínima sobrecarga de abstracción. El costo de ese control es la responsabilidad: usted mismo administra la memoria, verifica los límites y maneja los errores. Para la programación de sistemas, el desarrollo integrado y cualquier lugar donde las limitaciones de recursos y rendimiento sean importantes, C sigue siendo inigualable. Para todo lo demás, los lenguajes de nivel superior construidos sobre C suelen ser opciones más productivas.