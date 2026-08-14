---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [concurrency, parallelism, cross-language, comparison, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Comparación entre idiomas: simultaneidad y paralelismo
## Descripción general de los modelos de concurrencia
| Idioma | Modelo | Mecanismo clave | ¿Memoria compartida? |
|----------|-------|---------------|----------------|
| Pitón | GIL + hilos | `threading`,`asyncio`| Sí (GIL limita el paralelismo) |
| JavaScript | Bucle de eventos | Promesas,`async/await`| No (un solo subproceso) |
| Óxido | Propiedad + Enviar/Sincronizar |  `std::thread`, `async/await`, canales | Seguridad en tiempo de compilación |
| Ir | Gorrutinas |  `go func()`, canales | No (paso de mensaje) |
| Java | Hilos del sistema operativo |  `Thread`, `ExecutorService`,`CompletableFuture`| Sí |
| Mecanografiado | Bucle de eventos | Promesas,`async/await`| No (un solo subproceso) |
| C | Hilos POSIX |  `pthread`, OpenMP | Sí (sincronización manual) |
| C++ | Hilos del sistema operativo |  `std::thread`, `std::async`, corrutinas | Sí (sincronización manual) |
| C# | asíncrono/espera |  `Task`, `async/await`,`Parallel`| Sí |
| Rubí | GVL + fibras |  `Thread`, `Fiber`,`Ractor`(3.0+) | Sí (GVL), Ractor: No |
| Rápido | Actores |  `async/await`, actores,`Sendable`| No (aislamiento de actores) |
| Kotlin | Corrutinas |  `suspend`, `launch`,`async`| Depende del despachador |
| PHP | Basado en procesos |  `pcntl_fork`, fibras (8.1+) | No (procesos separados) |
| Escala | Hilos JVM |  `Future`, Actores de Akka, ZIO, Efecto Gatos | Sí (JVM) |
| Haskel | Hilos verdes |  `forkIO`, STM,`async`| Sí (STM por seguridad) |
| Lúa | Corrutinas | `coroutine.create/resume/yield`| No (cooperativa) |
| R | Secuencial + paralelo |  `parallel`,`future`| No (procesos separados) |
| Julia | Tareas + hilos |  `@async`, `@threads`,`Distributed`| Sí (tipos seguros para subprocesos) |
| Dardo | Aislamientos |  `Isolate`,`async/await`| No (paso de mensaje) |
| Perla | Hilos + tenedor |  `threads`,`fork`| Sí (hilos) |
| MATLAB | Piscina paralela |  `parfor`, `spmd`,`gpuArray`| No (trabajadores) |
| SQL | N/A | La base de datos maneja la concurrencia (MVCC, bloqueos) | N/A |
| Concha | Procesos en segundo plano |  `&`, `wait`,`xargs -P`| No (procesos separados) |
| Fortrán | Coarrays + OpenMP |  `coarray`, `do concurrent`, OpenMP | Sí (memoria compartida) |
| Ada | Tareas + protegido |  `task`, `protected object`, cita | Sí (objetos protegidos) |
| COBOL | N/A | Procesamiento por lotes, sin concurrencia nativa | N/A |
| Prólogo | N/A | Secuencial (algunas implementaciones tienen subprocesos) | N/A |
| Ceceo/Clojure | STM + agentes |  `future`, `promise`, `core.async`, STM | Clojure: STM (referencias, átomos) |
| Erlang/Elixir | Modelo actor |  `spawn`, paso de mensajes,`receive`| No (paso de mensaje) |
| OCaml | Dominio + Efecto |  `Domain.spawn`, controladores de efectos (5.0+) | No (dominios) |
| Asamblea | N/A | Dependiente del sistema operativo (alarmas, llamadas al sistema) | N/A |
| Delfos | Temas |  `TThread`,`TTask`| Sí (sincronización manual) |
| Rascar | Impulsado por eventos |  `when green flag clicked`, transmisión | No (aislamiento de sprites) |
| V.B. | asíncrono/espera | `Async/Await`,`Task`| Sí |
## Creación de hilos
```python
# Python: threading
import threading
t = threading.Thread(target=worker, args=(data,))
t.start()
t.join()

# Python: asyncio
import asyncio
async def main():
    await asyncio.gather(task1(), task2())
asyncio.run(main())
```

```javascript
// JavaScript: Promises
const result = await Promise.all([task1(), task2()]);

// JavaScript: Web Workers
const worker = new Worker('worker.js');
worker.postMessage(data);
worker.onmessage = (e) => console.log(e.data);
```

```rust
// Rust: threads
use std::thread;
let handle = thread::spawn(|| {
    println!("Hello from thread!");
});
handle.join().unwrap();

// Rust: async (tokio)
#[tokio::main]
async fn main() {
    let task = tokio::spawn(async { /* work */ });
    task.await.unwrap();
}
```

```go
// Go: goroutines
go func() {
    fmt.Println("Hello from goroutine!")
}()

// Go: channels
ch := make(chan int)
go func() { ch <- 42 }()
value := <-ch
```

```java
// Java: threads
Thread t = new Thread(() -> System.out.println("Hello!"));
t.start();
t.join();

// Java: CompletableFuture
CompletableFuture.supplyAsync(() -> compute())
    .thenAccept(System.out::println);
```

```c
// C: POSIX threads
#include <pthread.h>
void* worker(void* arg) {
    printf("Hello from thread!\n");
    return NULL;
}
pthread_t t;
pthread_create(&t, NULL, worker, NULL);
pthread_join(t, NULL);
```

```go
// Go: worker pool pattern
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}
jobs := make(chan int, 100)
results := make(chan int, 100)
for w := 0; w < 3; w++ {
    go worker(w, jobs, results)
}
```

```erlang
% Erlang: spawn + message passing
Pid = spawn(fun() ->
    receive
        {From, Msg} -> From ! {response, Msg}
    end
end),
Pid ! {self(), hello},
receive
    {Pid, Response} -> io:format("~p~n", [Response])
end.
```

```elixir
# Elixir: Task (built on Erlang processes)
task = Task.async(fn -> compute() end)
result = Task.await(task)

# Elixir: GenServer (OTP behavior)
defmodule Worker do
  use GenServer
  def start_link(args), do: GenServer.start_link(__MODULE__, args)
  def handle_call(:work, _from, state), do: {:reply, result, state}
end
```

```swift
// Swift: async/await + actors
actor Counter {
    var count = 0
    func increment() { count += 1 }
}

let counter = Counter()
Task {
    await counter.increment()
}

// Swift: TaskGroup
await withTaskGroup(of: Int.self) { group in
    for i in 0..<10 {
        group.addTask { return i * i }
    }
}
```

```kotlin
// Kotlin: coroutines
import kotlinx.coroutines.*

runBlocking {
    val deferred = async { computeAsync() }
    println(deferred.await())
}

// Kotlin: coroutine scope
CoroutineScope(Dispatchers.Default).launch {
    val result = withContext(Dispatchers.IO) { fetchData() }
}
```

## Patrones de concurrencia clave
### Productor-Consumidor
```go
// Go: channels
func producer(ch chan<- int) {
    for i := 0; i < 10; i++ { ch <- i }
    close(ch)
}
func consumer(ch <-chan int) {
    for v := range ch { fmt.Println(v) }
}
ch := make(chan int)
go producer(ch)
consumer(ch)
```

```rust
// Rust: channels (mpsc)
use std::sync::mpsc;
use std::thread;
let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    for i in 0..10 { tx.send(i).unwrap(); }
});
for val in rx { println!("{}", val); }
```

```erlang
% Erlang: message passing
producer(Pid, 0) -> Pid ! done;
producer(Pid, N) -> Pid ! {data, N}, producer(Pid, N-1).

consumer() ->
    receive
        done -> ok;
        {data, N} -> io:format("~p~n", [N]), consumer()
    end.
```

### Mutex / Bloqueo
```java
// Java: synchronized
synchronized (lock) {
    sharedResource++;
}

// Java: ReentrantLock
ReentrantLock lock = new ReentrantLock();
lock.lock();
try { sharedResource++; }
finally { lock.unlock(); }
```

```python
# Python: threading.Lock
import threading
lock = threading.Lock()
with lock:
    shared_resource += 1
```

```rust
// Rust: Mutex (compile-time safety)
use std::sync::{Arc, Mutex};
let counter = Arc::new(Mutex::new(0));
let c = counter.clone();
thread::spawn(move || {
    let mut num = c.lock().unwrap();
    *num += 1;
});
```

```csharp
// C#: lock
lock (lockObj) {
    sharedResource++;
}

// C#: SemaphoreSlim
await semaphoreSlim.WaitAsync();
try { /* critical section */ }
finally { semaphoreSlim.Release(); }
```

## Tabla resumen
| paradigma | Idiomas |
|----------|-----------|
| **Subprocesos del sistema operativo + memoria compartida** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Bloqueo + Hilos** | Python, Rubí, Perl |
| **Gorutinas + Canales** | Ir |
| **Modelo actor** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/await + Bucle de eventos** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (memoria transaccional de software)** | Haskell, Clojure |
| **Corrutinas (cooperativa)** | Lúa, Kotlin |
| **Aislados (sin memoria compartida)** | Dardo, JavaScript, TypeScript |
| **Sin simultaneidad nativa** | COBOL, Prólogo, Scratch, SQL |