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
# Межъязыковое сравнение — параллелизм и параллелизм
## Обзор моделей параллелизма
| Язык | Модель | Ключевой механизм | Общая память? |
|----------|-------|---------------|----------------|
| Питон | GIL + темы | `threading`,`asyncio`| Да (GIL ограничивает параллелизм) |
| JavaScript | Цикл событий | Обещания,`async/await`| Нет (однопоточный) |
| Ржавчина | Владение + Отправить/Синхронизация |  `std::thread`, `async/await`, каналы | Безопасность во время компиляции |
| Перейти | Горутины | `go func()`, каналы | Нет (передача сообщений) |
| Ява | Потоки ОС | `Thread`,`ExecutorService`,`CompletableFuture`| Да |
| TypeScript | Цикл событий | Обещания,`async/await`| Нет (однопоточный) |
| С | POSIX-потоки | `pthread`, OpenMP | Да (ручная синхронизация) |
| С++ | Потоки ОС |  `std::thread`, `std::async`, сопрограммы | Да (ручная синхронизация) |
| С# | асинхронный/ожидание | `Task`,`async/await`,`Parallel`| Да |
| Руби | ГВЛ + волокна | `Thread`,`Fiber`,`Ractor`(3.0+) | Да (ГВЛ), Рактор: Нет |
| Свифт | Актеры | `async/await`, актеры,`Sendable`| Нет (изоляция актера) |
| Котлин | Сопрограммы | `suspend`,`launch`,`async`| Зависит от диспетчера |
| PHP | Процессно-ориентированный | `pcntl_fork`, волокна (8.1+) | Нет (отдельные процессы) |
| Скала | JVM-потоки | `Future`, Актеры Акка, ЗИО, Эффект кошек | Да (JVM) |
| Хаскелл | Зеленые нити | `forkIO`, STM,`async`| Да (STM для безопасности) |
| Луа | Сопрограммы | `coroutine.create/resume/yield`| Нет (кооператив) |
| р | Последовательный + параллельный | `parallel`,`future`| Нет (отдельные процессы) |
| Юлия | Задачи + темы | `@async`,`@threads`,`Distributed`| Да (потокобезопасные типы) |
| Дарт | Изоляты | `Isolate`,`async/await`| Нет (передача сообщений) |
| Перл | Нитки + вилка | `threads`,`fork`| Да (резьба) |
| МАТЛАБ | Параллельный бассейн | `parfor`,`spmd`,`gpuArray`| Нет (рабочие) |
| SQL | Н/Д | База данных поддерживает параллелизм (MVCC, блокировки) | Н/Д |
| Шелл | Фоновые процессы | `&`,`wait`,`xargs -P`| Нет (отдельные процессы) |
| Фортран | Coarrays + OpenMP |  `coarray`, `do concurrent`, OpenMP | Да (общая память) |
| Ада | Задачи + защищенные |  `task`, `protected object`, рандеву | Да (объекты охраны) |
| КОБОЛ | Н/Д | Пакетная обработка, без встроенного параллелизма | Н/Д |
| Пролог | Н/Д | Последовательный (в некоторых реализациях есть потоки) | Н/Д |
| Лисп/Кложур | СТМ + агенты |  `future`, `promise`, `core.async`, СТМ | Clojure: STM (ссылки, атомы) |
| Эрланг/Эликсир | Модель актера | `spawn`, передача сообщений,`receive`| Нет (передача сообщений) |
| OCaml | Домен + Эффект | `Domain.spawn`, обработчики эффектов (5.0+) | Нет (домены) |
| Ассамблея | Н/Д | Зависит от ОС (прерывания, системные вызовы) | Н/Д |
| Дельфи | Темы | `TThread`,`TTask`| Да (ручная синхронизация) |
| Царапина | Управляемый событиями | `when green flag clicked`, трансляция | Нет (изоляция спрайтов) |
| ВБ | асинхронный/ожидание | `Async/Await`,`Task`| Да |
## Создание темы
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

## Ключевые шаблоны параллелизма
### Производитель-потребитель
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

### Мьютекс/блокировка
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

## Сводная таблица
| Парадигма | Языки |
|----------|-----------|
| **Потоки ОС + Общая память** | C, C++, Java, C#, Фортран, Delphi, VB |
| **GIL/Lock + Threads** | Питон, Руби, Перл |
| **Горутины + каналы** | Перейти |
| **Актерская модель** | Эрланг, Эликсир, Скала (Акка), Рубин (Рактор) |
| **async/await + цикл событий** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (программная транзакционная память)** | Хаскелл, Clojure |
| **Сопрограммы (кооперативные)** | Луа, Котлин |
| **Изолирует (без общей памяти)** | Дарт, JavaScript, TypeScript |
| **Нет встроенного параллелизма** | КОБОЛ, Пролог, Скретч, SQL |