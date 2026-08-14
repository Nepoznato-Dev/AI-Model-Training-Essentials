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
# Confronto tra linguaggi: concorrenza e parallelismo
## Panoramica dei modelli di concorrenza
| Lingua | Modello | Meccanismo chiave | Memoria condivisa? |
|----------|-------|---------------|----------------|
| Pitone | GIL + discussioni | `threading`,`asyncio`| Sì (GIL limita il parallelismo) |
| JavaScript | Ciclo di eventi | Promesse,`async/await`| No (thread singolo) |
| Ruggine | Proprietà + Invia/Sincronizza | `std::thread`,`async/await`, canali | Sicurezza in fase di compilazione |
| Vai | Goroutine | `go func()`, canali | No (passaggio di messaggi) |
| Giava | Thread del sistema operativo | `Thread`,`ExecutorService`,`CompletableFuture`| Sì |
| Dattiloscritto | Ciclo di eventi | Promesse,`async/await`| No (thread singolo) |
| C| Discussioni POSIX |  `pthread`, OpenMP | Sì (sincronizzazione manuale) |
| C++ | Thread del sistema operativo | `std::thread`,`std::async`, coroutine | Sì (sincronizzazione manuale) |
| C# | asincrono/attendo | `Task`,`async/await`,`Parallel`| Sì |
| Rubino | GVL + fibre | `Thread`,`Fiber`,`Ractor`(3.0+) | Sì (GVL), Ractor: No |
| Veloce | Attori | `async/await`, attori,`Sendable`| No (isolamento dell'attore) |
| Kotlin | Coroutine | `suspend`,`launch`,`async`| Dipende dal dispatcher |
| PHP | Basato sul processo | `pcntl_fork`, fibre (8.1+) | No (processi separati) |
| Scala | Discussioni JVM | `Future`, attori Akka, ZIO, Cats Effect | Sì (JVM) |
| Haskell | Fili verdi |  `forkIO`, STM,`async`| Sì (STM per sicurezza) |
| Lua | Coroutine | `coroutine.create/resume/yield`| No (cooperativo) |
| R | Sequenziale + parallelo | `parallel`,`future`| No (processi separati) |
| Giulia | Attività + discussioni | `@async`,`@threads`,`Distributed`| Sì (tipi thread-safe) |
| Dardo | Isola | `Isolate`,`async/await`| No (passaggio di messaggi) |
| Perl | Discussioni + forchetta | `threads`,`fork`| Sì (ithread) |
| MATLAB | Piscina parallela | `parfor`,`spmd`,`gpuArray`| No (lavoratori) |
| SQL | N/D | Il database gestisce la concorrenza (MVCC, blocchi) | N/D |
| Conchiglia | Processi in background | `&`,`wait`,`xargs -P`| No (processi separati) |
| Fortran | Coarray + OpenMP |  `coarray`, `do concurrent`, OpenMP | Sì (memoria condivisa) |
| Ada | Compiti + protetti | `task`,`protected object`, appuntamento | Sì (oggetti protetti) |
| COBOL | N/D | Elaborazione batch, nessuna concorrenza nativa | N/D |
| Prologo | N/D | Sequenziale (alcune implementazioni hanno thread) | N/D |
| Lisp/Clojure | STM + agenti |  `future`, `promise`, `core.async`, STM | Clojure: STM (riferimenti, atomi) |
| Erlang/Elisir | Modello di attore | `spawn`, passaggio di messaggi,`receive`| No (passaggio di messaggi) |
| OCaml | Dominio + Effetto |  `Domain.spawn`, gestori di effetti (5.0+) | No (domini) |
| Assemblea | N/D | Dipendente dal sistema operativo (interrupt, chiamate di sistema) | N/D |
| Delfi | Discussioni | `TThread`,`TTask`| Sì (sincronizzazione manuale) |
| Gratta | Guidato dagli eventi | `when green flag clicked`, trasmissione | No (isolamento dello sprite) |
| V.B. | asincrono/attendo | `Async/Await`,`Task`| Sì |
## Creazione del thread
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

## Modelli di concorrenza chiave
### Produttore-Consumatore
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

### Mutex/Blocco
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

## Tabella riassuntiva
| Paradigma | Lingue |
|----------|-----------|
| **Thread del sistema operativo + memoria condivisa** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Blocco + Discussioni** | Pitone, Rubino, Perl |
| **Goroutine + Canali** | Vai |
| **Modello di attore** | Erlang, Elisir, Scala (Akka), Ruby (Ractor) |
| **asincrono/attende + Ciclo eventi** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Memoria transazionale software)** | Haskell, Clojure |
| **Coroutines (cooperativa)** | Lua, Kotlin |
| **Isola (nessuna memoria condivisa)** | Dardo, JavaScript, TypeScript |
| **Nessuna concorrenza nativa** | COBOL, Prolog, Scratch, SQL |