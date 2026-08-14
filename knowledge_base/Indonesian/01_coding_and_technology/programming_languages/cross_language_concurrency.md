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
# Perbandingan Lintas Bahasa — Konkurensi & Paralelisme
## Ikhtisar Model Konkurensi
| Bahasa | Model | Mekanisme Kunci | Memori Bersama? |
|----------|-------|---------------|----------------|
| ular piton | GIL + benang | `threading`,`asyncio`| Ya (GIL membatasi paralelisme) |
| JavaScript | Lingkaran peristiwa | Janji,`async/await`| Tidak (utas tunggal) |
| Karat | Kepemilikan + Kirim/Sinkronisasi | `std::thread`,`async/await`, saluran | Keamanan waktu kompilasi |
| Pergi | Goroutine | `go func()`, saluran | Tidak (pesan lewat) |
| Jawa | utas OS | `Thread`,`ExecutorService`,`CompletableFuture`| Ya |
| Skrip Ketik | Lingkaran peristiwa | Janji,`async/await`| Tidak (utas tunggal) |
| C | Utas POSIX |  `pthread`, OpenMP | Ya (sinkronisasi manual) |
| C++ | utas OS | `std::thread`,`std::async`, coroutine | Ya (sinkronisasi manual) |
| C#| async/menunggu | `Task`,`async/await`,`Parallel`| Ya |
| rubi | GVL + serat | `Thread`,`Fiber`,`Ractor`(3.0+) | Ya (GVL), Raktor: Tidak |
| Cepat | Aktor | `async/await`, aktor,`Sendable`| Tidak (isolasi aktor) |
| Kotlin | Coroutine | `suspend`,`launch`,`async`| Tergantung pada operator |
| PHP | Berbasis proses | `pcntl_fork`, serat (8.1+) | Tidak (proses terpisah) |
| Skala | utas JVM | `Future`, Aktor Akka, ZIO, Efek Kucing | Ya (JVM) |
| Haskell | Benang hijau | `forkIO`, STM,`async`| Ya (STM untuk keselamatan) |
| Lua | Coroutine | `coroutine.create/resume/yield`| Tidak (koperasi) |
| R | Berurutan + paralel | `parallel`,`future`| Tidak (proses terpisah) |
| Julia | Tugas + thread | `@async`,`@threads`,`Distributed`| Ya (tipe thread-safe) |
| Anak panah | Isolat | `Isolate`,`async/await`| Tidak (pesan lewat) |
| Perl | Benang + garpu | `threads`,`fork`| Ya (utas) |
| MATLAB | Kolam paralel | `parfor`,`spmd`,`gpuArray`| Tidak (pekerja) |
| SQL | T/A | Database menangani konkurensi (MVCC, kunci) | T/A |
| cangkang | Proses latar belakang | `&`,`wait`,`xargs -P`| Tidak (proses terpisah) |
| Fortran | Coarray + OpenMP | `coarray`,`do concurrent`, OpenMP | Ya (memori bersama) |
| Ada | Tugas + dilindungi | `task`,`protected object`, pertemuan | Ya (objek yang dilindungi) |
| COBOL | T/A | Pemrosesan batch, tanpa konkurensi asli | T/A |
| Prolog | T/A | Berurutan (beberapa implementasi memiliki thread) | T/A |
| Cadel/Clojure | Agen STM+ | `future`,`promise`,`core.async`, STM | Clojure: STM (ref, atom) |
| Erlang/Ramuan | Model aktor | `spawn`, penyampaian pesan,`receive`| Tidak (pesan lewat) |
| OCaml | Domain + Efek | `Domain.spawn`, penangan efek (5.0+) | Tidak (domain) |
| Majelis | T/A | Tergantung OS (interupsi, panggilan sistem) | T/A |
| Delfi | Utas | `TThread`,`TTask`| Ya (sinkronisasi manual) |
| Gores | Didorong oleh peristiwa | `when green flag clicked`, siaran | Tidak (isolasi sprite) |
| VB | async/menunggu | `Async/Await`,`Task`| Ya |
## Pembuatan Benang
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

## Pola Konkurensi Utama
### Produsen-Konsumen
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

### Mutex / Mengunci
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

## Tabel Ringkasan
| Paradigma | Bahasa |
|----------|-----------|
| **Untaian OS + Memori Bersama** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Kunci + Utas** | Python, Ruby, Perl |
| **Goroutine + Saluran** | Pergi |
| **Model Aktor** | Erlang, Elixir, Scala (Akka), Ruby (Raktor) |
| **async/menunggu + Perulangan Peristiwa** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Memori Transaksional Perangkat Lunak)** | Haskell, Clojure |
| **Coroutine (koperasi)** | Lua, Kotlin |
| **Isolasi (tidak ada memori bersama)** | Dart, JavaScript, TypeScript |
| **Tidak ada konkurensi asli** | COBOL, Prolog, Gores, SQL |