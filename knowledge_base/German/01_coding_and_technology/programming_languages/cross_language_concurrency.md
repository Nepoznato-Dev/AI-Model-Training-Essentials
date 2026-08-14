---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Sprachübergreifender Vergleich – Parallelität und Parallelität
## Übersicht über Parallelitätsmodelle
| Sprache | Modell | Schlüsselmechanismus | Geteilter Speicher? |
|----------|-------|---------------|----------------|
| Python | GIL + Fäden | `threading`,`asyncio`| Ja (GIL begrenzt Parallelität) |
| JavaScript | Ereignisschleife | Versprechen,`async/await`| Nein (Single-Threaded) |
| Rost | Besitz + Senden/Synchronisieren | `std::thread`,`async/await`, Kanäle | Sicherheit zur Kompilierungszeit |
| Geh | Goroutinen | `go func()`, Kanäle | Nein (Nachrichtenübermittlung) |
| Java | Betriebssystem-Threads | `Thread`,`ExecutorService`,`CompletableFuture`| Ja |
| TypeScript | Ereignisschleife | Versprechen,`async/await`| Nein (Single-Threaded) |
| C | POSIX-Threads | `pthread`, OpenMP | Ja (manuelle Synchronisierung) |
| C++ | Betriebssystem-Threads | `std::thread`,`std::async`, Coroutinen | Ja (manuelle Synchronisierung) |
| C# | asynchron/warten | `Task`,`async/await`,`Parallel`| Ja |
| Rubin | GVL + Fasern |  `Thread`, `Fiber`,`Ractor`(3.0+) | Ja (GVL), Ractor: Nein |
| Schnell | Schauspieler | `async/await`, Schauspieler,`Sendable`| Nein (Schauspielerisolation) |
| Kotlin | Coroutinen | `suspend`,`launch`,`async`| Abhängig vom Dispatcher |
| PHP | Prozessbasiert | `pcntl_fork`, Fasern (8.1+) | Nein (getrennte Prozesse) |
| Scala | JVM-Threads | `Future`, Akka-Schauspieler, ZIO, Cats Effect | Ja (JVM) |
| Haskell | Grüne Fäden | `forkIO`, STM,`async`| Ja (STM aus Sicherheitsgründen) |
| Lua | Coroutinen | `coroutine.create/resume/yield`| Nein (kooperative) |
| R | Sequentiell + parallel | `parallel`,`future`| Nein (getrennte Prozesse) |
| Julia | Aufgaben + Threads | `@async`,`@threads`,`Distributed`| Ja (threadsichere Typen) |
| Dart | Isoliert | `Isolate`,`async/await`| Nein (Nachrichtenübermittlung) |
| Perl | Threads + Gabel | `threads`,`fork`| Ja (Threads) |
| MATLAB | Parallelpool | `parfor`,`spmd`,`gpuArray`| Nein (Arbeiter) |
| SQL | N/A | Datenbank verwaltet Parallelität (MVCC, Sperren) | N/A |
| Schale | Hintergrundprozesse | `&`,`wait`,`xargs -P`| Nein (getrennte Prozesse) |
| Fortran | Coarrays + OpenMP |  `coarray`, `do concurrent`, OpenMP | Ja (gemeinsamer Speicher) |
| Ada | Aufgaben + geschützt | `task`,`protected object`, Rendezvous | Ja (geschützte Objekte) |
| COBOL | N/A | Stapelverarbeitung, keine native Parallelität | N/A |
| Prolog | N/A | Sequentiell (einige Implementierungen haben Threads) | N/A |
| Lispeln/Clojure | STM + Agenten |  `future`, `promise`, `core.async`, STM | Clojure: STM (Refs, Atome) |
| Erlang/Elixier | Schauspielermodell | `spawn`, Nachrichtenübermittlung,`receive`| Nein (Nachrichtenübermittlung) |
| OCaml | Domäne + Wirkung | `Domain.spawn`, Effekthandler (5.0+) | Nein (Domänen) |
| Montage | N/A | Betriebssystemabhängig (Interrupts, Systemaufrufe) | N/A |
| Delphi | Themen | `TThread`,`TTask`| Ja (manuelle Synchronisierung) |
| Kratzer | Ereignisgesteuert | `when green flag clicked`, Sendung | Nein (Sprite-Isolation) |
| VB | asynchron/warten | `Async/Await`,`Task`| Ja |
## Thread-Erstellung
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

## Wichtige Parallelitätsmuster
### Produzent-Verbraucher
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

### Mutex / Sperrung
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

## Übersichtstabelle
| Paradigma | Sprachen |
|----------|-----------|
| **Betriebssystem-Threads + gemeinsam genutzter Speicher** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Sperre + Gewinde** | Python, Ruby, Perl |
| **Goroutinen + Kanäle** | Geh |
| **Schauspielermodell** | Erlang, Elixier, Scala (Akka), Ruby (Ractor) |
| **async/await + Ereignisschleife** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Software Transactional Memory)** | Haskell, Clojure |
| **Koroutinen (kooperativ)** | Lua, Kotlin |
| **Isoliert (kein gemeinsam genutzter Speicher)** | Dart, JavaScript, TypeScript |
| **Keine native Parallelität** | COBOL, Prolog, Scratch, SQL |