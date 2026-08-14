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
# Comparação entre idiomas - simultaneidade e paralelismo
## Visão geral dos modelos de simultaneidade
| Idioma | Modelo | Mecanismo Chave | Memória compartilhada? |
|----------|-------|---------------|----------------|
| Pitão | GIL + fios | `threading`,`asyncio`| Sim (GIL limita o paralelismo) |
| JavaScript | Ciclo de eventos | Promessas,`async/await`| Não (thread único) |
| Ferrugem | Propriedade + Enviar/Sincronizar |  `std::thread`, `async/await`, canais | Segurança em tempo de compilação |
| Vá | Gorotinas |  `go func()`, canais | Não (passagem de mensagem) |
| Java | Threads do sistema operacional | `Thread`,`ExecutorService`,`CompletableFuture`| Sim |
| Datilografado | Ciclo de eventos | Promessas,`async/await`| Não (thread único) |
| C | Tópicos POSIX |  `pthread`, OpenMP | Sim (sincronização manual) |
| C++ | Threads do sistema operacional | `std::thread`,`std::async`, corrotinas | Sim (sincronização manual) |
| C# | assíncrono/aguarda | `Task`,`async/await`,`Parallel`| Sim |
| Rubi | GVL + fibras |  `Thread`, `Fiber`,`Ractor`(3.0+) | Sim (GVL), Rator: Não |
| Rápido | Atores |  `async/await`, atores,`Sendable`| Não (isolamento do ator) |
| Kotlin | Corrotinas | `suspend`,`launch`,`async`| Depende do despachante |
| PHP | Baseado em processos |  `pcntl_fork`, fibras (8.1+) | Não (processos separados) |
| Escala | Encadeamentos JVM |  `Future`, atores Akka, ZIO, Efeito Gatos | Sim (JVM) |
| Haskel | Fios verdes |  `forkIO`, STM,`async`| Sim (STM para segurança) |
| Lua | Corrotinas | `coroutine.create/resume/yield`| Não (cooperativa) |
| R | Sequencial + paralelo | `parallel`,`future`| Não (processos separados) |
| Júlia | Tarefas + tópicos | `@async`,`@threads`,`Distributed`| Sim (tipos thread-safe) |
| Dardo | Isolados | `Isolate`,`async/await`| Não (passagem de mensagem) |
| Perl | Fios + garfo | `threads`,`fork`| Sim (threads) |
| MATLAB | Piscina paralela |  `parfor`, `spmd`,`gpuArray`| Não (trabalhadores) |
| SQL | N/A | Banco de dados lida com simultaneidade (MVCC, bloqueios) | N/A |
| Concha | Processos em segundo plano | `&`,`wait`,`xargs -P`| Não (processos separados) |
| Fortran | Coarrays + OpenMP |  `coarray`, `do concurrent`, OpenMP | Sim (memória compartilhada) |
| Ada | Tarefas + protegidas | `task`,`protected object`, encontro | Sim (objetos protegidos) |
| COBOL | N/A | Processamento em lote, sem simultaneidade nativa | N/A |
| Prólogo | N/A | Sequencial (algumas implementações possuem threads) | N/A |
| Lisp/Clojure | Agentes STM + | `future`,`promise`,`core.async`, STM | Clojure: STM (refs, átomos) |
| Erlang/Elixir | Modelo de ator | `spawn`, passagem de mensagem,`receive`| Não (passagem de mensagem) |
| OCaml | Domínio + Efeito | `Domain.spawn`, manipuladores de efeitos (5.0+) | Não (domínios) |
| Montagem | N/A | Dependente do sistema operacional (interrupções, chamadas de sistema) | N/A |
| Delfos | Tópicos | `TThread`,`TTask`| Sim (sincronização manual) |
| Arranhar | Orientado a eventos |  `when green flag clicked`, transmissão | Não (isolamento de sprites) |
| VB | assíncrono/aguarda | `Async/Await`,`Task`| Sim |
## Criação de Tópico
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

## Principais padrões de simultaneidade
### Produtor-Consumidor
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

### Mutex / Bloqueio
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

## Tabela Resumo
| Paradigma | Idiomas |
|----------|-----------|
| **Threads do SO + Memória Compartilhada** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Lock + Fios** | Python, Ruby, Perl |
| **Goroutines + Canais** | Vá |
| **Modelo de ator** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **assíncrono/aguarda + Loop de Evento** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (memória transacional de software)** | Haskell, Clojure |
| **Corrotinas (cooperativas)** | Lua, Kotlin |
| **Isolados (sem memória compartilhada)** | Dardo, JavaScript, TypeScript |
| **Sem simultaneidade nativa** | COBOL, Prolog, Scratch, SQL |