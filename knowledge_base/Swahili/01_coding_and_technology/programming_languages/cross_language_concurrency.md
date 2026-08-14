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
# Ulinganisho wa Lugha Mtambuka - Upatanishi na Usambamba
## Muhtasari wa Miundo ya Sarafu
| Lugha | Mfano | Utaratibu Muhimu | Kumbukumbu iliyoshirikiwa? |
|----------|-------|---------------|----------------|
| Chatu | GIL + nyuzi | `threading`,`asyncio`| Ndiyo (GIL inaweka mipaka ya usawa) |
| JavaScript | Kitanzi cha tukio | Ahadi,`async/await`| Hapana (yenye uzi mmoja) |
| Kutu | Umiliki + Tuma/Sawazisha | `std::thread`,`async/await`, njia | Kukusanya usalama wa wakati |
| Nenda | Goroutines | `go func()`, njia | Hapana (ujumbe kupita) |
| Java | nyuzi za OS | `Thread`,`ExecutorService`,`CompletableFuture`| Ndiyo |
| TypeScript | Kitanzi cha tukio | Ahadi,`async/await`| Hapana (yenye uzi mmoja) |
| C | nyuzi POSIX | `pthread`, OpenMP | Ndiyo (usawazishaji wa mikono) |
| C++ | nyuzi za OS | `std::thread`,`std::async`, coroutines | Ndiyo (usawazishaji wa mikono) |
| C# | async/subiri | `Task`,`async/await`,`Parallel`| Ndiyo |
| Ruby | GVL + nyuzi | `Thread`,`Fiber`,`Ractor`(3.0+) | Ndiyo (GVL), Ractor: Hapana |
| Mwepesi | Waigizaji | `async/await`, watendaji,`Sendable`| Hapana (kutengwa kwa muigizaji) |
| Kotlin | Kanuni | `suspend`,`launch`,`async`| Inategemea dispatcher |
| PHP | Kulingana na mchakato | `pcntl_fork`, nyuzi (8.1+) | Hapana (michakato tofauti) |
| Scala | nyuzi za JVM | `Future`, Waigizaji wa Akka, ZIO, Athari ya Paka | Ndiyo (JVM) |
| Haskell | Nyuzi za kijani | `forkIO`, STM,`async`| Ndiyo (STM kwa usalama) |
| Lua | Kanuni | `coroutine.create/resume/yield`| Hapana (ushirika) |
| R | Mfuatano + sambamba | `parallel`,`future`| Hapana (michakato tofauti) |
| Julia | Majukumu + nyuzi | `@async`,`@threads`,`Distributed`| Ndiyo (aina salama za nyuzi) |
| Dart | Kujitenga | `Isolate`,`async/await`| Hapana (ujumbe kupita) |
| Perl | Nyuzi + uma | `threads`,`fork`| Ndiyo (mazungumzo) |
| MATLAB | Bwawa la kuogelea | `parfor`,`spmd`,`gpuArray`| Hapana (wafanyakazi) |
| SQL | N/A | Hifadhidata hushughulikia concurrency (MVCC, kufuli) | N/A |
| Sheli | Michakato ya usuli | `&`,`wait`,`xargs -P`| Hapana (michakato tofauti) |
| Fortran | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | Ndiyo (kumbukumbu iliyoshirikiwa) |
| Ada | Kazi + zinazolindwa | `task`,`protected object`, mikutano | Ndiyo (vitu vilivyolindwa) |
| COBOL | N/A | Uchakataji wa bechi, hakuna upatanishi wa asili | N/A |
| Matangazo | N/A | Mfuatano (utekelezaji fulani una nyuzi) | N/A |
| Lisp/Clojure | STM + mawakala | `future`,`promise`,`core.async`, STM | Clojure: STM (rejelea, atomi) |
| Erlang/Elixir | Muigizaji mfano | `spawn`, ujumbe kupita,`receive`| Hapana (ujumbe kupita) |
| OCaml | Kikoa + Athari | `Domain.spawn`, vidhibiti vya athari (5.0+) | Hapana (vikoa) |
| Bunge | N/A | Inategemea OS (kukatiza, simu za mfumo) | N/A |
| Delphi | Mizizi | `TThread`,`TTask`| Ndiyo (usawazishaji wa mikono) |
| Mwanga | Inaendeshwa na tukio | `when green flag clicked`, matangazo | Hapana (kutengwa kwa sprite) |
| VB | async/subiri | `Async/Await`,`Task`| Ndiyo |
## Uundaji wa nyuzi
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

## Miundo Muhimu ya Upatanisho
### Mtayarishaji-Mtumiaji
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

### Mutex / Kufunga
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

## Jedwali la Muhtasari
| Dhana | Lugha |
|----------|-----------|
| **Nzizi za Mfumo wa Uendeshaji + Kumbukumbu Inayoshirikiwa** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Funga + Nyuzi** | Chatu, Ruby, Perl |
| **Taratibu + Vituo** | Nenda |
| **Mfano wa Mwigizaji** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/subiri + Kitanzi cha Tukio** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Kumbukumbu ya Muamala wa Programu)** | Haskell, Clojure |
| **Coroutines (ushirika)** | Lua, Kotlin |
| **Isolates (hakuna kumbukumbu iliyoshirikiwa)** | Dart, JavaScript, TypeScript |
| **Hakuna upatanisho wa asili** | COBOL, Prolog, Scratch, SQL |