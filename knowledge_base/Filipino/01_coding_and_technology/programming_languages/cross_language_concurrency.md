<!--
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

-->
# Cross-Language Comparison — Concurrency at Parallelism
## Pangkalahatang-ideya ng Concurrency Models
| Wika | Modelo | Pangunahing Mekanismo | Nakabahaging Memorya? |
|----------|-------|----------------|----------------|
| Python | GIL + mga thread | `threading`,`asyncio`| Oo (nililimitahan ng GIL ang parallelism) |
| JavaScript | loop ng kaganapan | Mga Pangako,`async/await`| Hindi (single-threaded) |
| kalawang | Pagmamay-ari + Ipadala/I-sync | `std::thread`,`async/await`, mga channel | Pagtitipon-oras na kaligtasan |
| Pumunta | Mga Goroutine | `go func()`, mga channel | Hindi (message passing) |
| Java | Mga OS thread | `Thread`,`ExecutorService`,`CompletableFuture`| Oo |
| TypeScript | loop ng kaganapan | Mga Pangako,`async/await`| Hindi (single-threaded) |
| C | POSIX thread | `pthread`, OpenMP | Oo (manu-manong pag-sync) |
| C++ | Mga OS thread | `std::thread`,`std::async`, mga coroutine | Oo (manu-manong pag-sync) |
| C# | async/naghihintay | `Task`,`async/await`,`Parallel`| Oo |
| Ruby | GVL + fibers | `Thread`,`Fiber`,`Ractor`(3.0+) | Oo (GVL), Ractor: Hindi |
| matulin | Mga aktor | `async/await`, mga aktor,`Sendable`| Hindi (paghihiwalay ng aktor) |
| Kotlin | Mga Coroutine | `suspend`,`launch`,`async`| Depende sa dispatcher |
| PHP | Nakabatay sa proseso | `pcntl_fork`, mga hibla (8.1+) | Hindi (hiwalay na mga proseso) |
| Scala | Mga thread ng JVM | `Future`, Akka aktor, ZIO, Cats Effect | Oo (JVM) |
| Haskell | Mga berdeng thread | `forkIO`, STM,`async`| Oo (STM para sa kaligtasan) |
| Lua | Mga Coroutine | `coroutine.create/resume/yield`| Hindi (kooperatiba) |
| R | Sequential + parallel | `parallel`,`future`| Hindi (hiwalay na mga proseso) |
| Julia | Mga gawain + mga thread | `@async`,`@threads`,`Distributed`| Oo (mga uri na ligtas sa thread) |
| Dart | Isolates | `Isolate`,`async/await`| Hindi (message passing) |
| Perl | Mga thread + tinidor | `threads`,`fork`| Oo (ithreads) |
| MATLAB | Parallel pool | `parfor`,`spmd`,`gpuArray`| Hindi (manggagawa) |
| SQL | N/A | Pinangangasiwaan ng database ang concurrency (MVCC, mga kandado) | N/A |
| Shell | Mga proseso sa background | `&`,`wait`,`xargs -P`| Hindi (hiwalay na mga proseso) |
| Fortran | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | Oo (nakabahaging memorya) |
| Ada | Mga Gawain + protektado | `task`,`protected object`, pagtatagpo | Oo (mga protektadong bagay) |
| COBOL | N/A | Batch processing, walang native concurrency | N/A |
| Prolog | N/A | Sequential (may mga thread ang ilang pagpapatupad) | N/A |
| Lisp/Clojure | STM + mga ahente | `future`,`promise`,`core.async`, STM | Clojure: STM (refs, atoms) |
| Erlang/Elixir | Modelong artista | `spawn`, pagpasa ng mensahe,`receive`| Hindi (message passing) |
| OCaml | Domain + Effect | `Domain.spawn`, mga tagapangasiwa ng epekto (5.0+) | Walang (mga domain) |
| Assembly | N/A | Umaasa sa OS (mga interrupt, system call) | N/A |
| Delphi | Mga Thread | `TThread`,`TTask`| Oo (manu-manong pag-sync) |
| scratch | Dahil sa kaganapan | `when green flag clicked`, broadcast | Hindi (sprite isolation) |
| VB | async/naghihintay | `Async/Await`,`Task`| Oo |
## Paglikha ng Thread
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

## Mga Key Concurrency Pattern
### Producer-Consumer
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

### Mutex / Pag-lock
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

## Talahanayan ng Buod
| Paradigm | Mga Wika |
|----------|-----------|
| **Mga OS Thread + Nakabahaging Memory** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Lock + Thread** | Python, Ruby, Perl |
| **Goroutine + Mga Channel** | Pumunta |
| **Modelo ng Artista** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/wait + Event Loop** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Software Transactional Memory)** | Haskell, Clojure |
| **Coroutines (cooperative)** | Lua, Kotlin |
| **Isolates (walang shared memory)** | Dart, JavaScript, TypeScript |
| **Walang katutubong concurrency** | COBOL, Prolog, Scratch, SQL |