<!--
---
# Metadata
title: "Cross-Language Comparison — I/O & File Operations"
description: "Side-by-side comparison of I/O and file operations across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [io, file-operations, cross-language, comparison, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# مقایسه بین زبانی - عملیات ورودی/خروجی و فایل
## خروجی کنسول
| زبان | چاپ به stdout |
|----------|----------------|
| پایتون | `print("Hello")`|
| جاوا اسکریپت | `console.log("Hello")`|
| زنگ زدگی | `println!("Hello")`|
| برو | `fmt.Println("Hello")`|
| جاوا | `System.out.println("Hello")`|
| ج | `printf("Hello\n")`|
| C++ | `std::cout << "Hello" << std::endl`|
| سی شارپ | `Console.WriteLine("Hello")`|
| یاقوت | `puts "Hello"`|
| سویفت | `print("Hello")`|
| کاتلین | `println("Hello")`|
| پی اچ پی | `echo "Hello\n"`|
| TypeScript | `console.log("Hello")`|
| هاسکل | `putStrLn "Hello"`|
| اسکالا | `println("Hello")`|
| R | `cat("Hello\n")`|
| جولیا | `println("Hello")`|
| پرل | `say "Hello"`|
| لوا | `print("Hello")`|
| متلب | `disp('Hello')`|
| دارت | `print('Hello')`|
| پرولوگ | `write('Hello'), nl.`|
| لیسپ | `(format t "Hello~%")`|
| اکسیر | `IO.puts("Hello")`|
| ارلنگ | `io:format("Hello~n")`|
| OCaml | `print_endline "Hello"`|
| آدا | `Put_Line("Hello")`|
| COBOL | `DISPLAY 'Hello'`|
| فرترن | `print *, 'Hello'`|
| مونتاژ | `syscall`(نوشتن در fd 1) |
| دلفی | `WriteLn('Hello')`|
| خراش | `say [Hello]`|
| VB | `Console.WriteLine("Hello")`|
| پوسته | `echo "Hello"`|
| SQL | N/A (مجموعه نتایج را برمی‌گرداند) |
## خواندن یک فایل
```python
# Python
with open("file.txt", "r") as f:
    content = f.read()
# Or line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

```javascript
// JavaScript (Node.js)
const fs = require('fs');
const content = fs.readFileSync('file.txt', 'utf-8');
// Or async
const content = await fs.promises.readFile('file.txt', 'utf-8');
```

```rust
// Rust
use std::fs;
let content = fs::read_to_string("file.txt").expect("read error");
// Or line by line
use std::io::{BufRead, BufReader};
use std::fs::File;
let file = File::open("file.txt").unwrap();
for line in BufReader::new(file).lines() {
    println!("{}", line.unwrap());
}
```

```go
// Go
content, err := os.ReadFile("file.txt")
if err != nil {
    log.Fatal(err)
}
// Or line by line
file, _ := os.Open("file.txt")
defer file.Close()
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

```java
// Java
String content = Files.readString(Path.of("file.txt"));
// Or line by line
try (var lines = Files.lines(Path.of("file.txt"))) {
    lines.forEach(System.out::println);
}
```

```c
// C
FILE *f = fopen("file.txt", "r");
char buf[1024];
while (fgets(buf, sizeof(buf), f)) {
    printf("%s", buf);
}
fclose(f);
```

```csharp
// C#
string content = File.ReadAllText("file.txt");
// Or line by line
foreach (string line in File.ReadLines("file.txt")) {
    Console.WriteLine(line);
}
```

```ruby
# Ruby
content = File.read("file.txt")
# Or line by line
File.foreach("file.txt") do |line|
    puts line
end
```

```swift
// Swift
let content = try String(contentsOfFile: "file.txt")
```

```kotlin
// Kotlin
val content = File("file.txt").readText()
// Or line by line
File("file.txt").forEachLine { println(it) }
```

```haskell
-- Haskell
content <- readFile "file.txt"
-- Or line by line
interact id  -- copy stdin to stdout
```

```php
<?php
$content = file_get_contents("file.txt");
// Or line by line
$handle = fopen("file.txt", "r");
while (($line = fgets($handle)) !== false) {
    echo $line;
}
fclose($handle);
```

```bash
# Bash
content=$(cat file.txt)
# Or line by line
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

```lua
-- Lua
local file = io.open("file.txt", "r")
local content = file:read("*a")
file:close()
-- Or line by line
for line in io.lines("file.txt") do
    print(line)
end
```

```r
# R
content <- readLines("file.txt")
# Or entire file
content <- paste(readLines("file.txt"), collapse = "\n")
```

```perl
# Perl
open my $fh, '<', 'file.txt' or die $!;
my $content = do { local $/; <$fh> };
close $fh;
# Or line by line
while (<$fh>) { print; }
```

```matlab
% MATLAB
content = fileread('file.txt');
% Or line by line
fid = fopen('file.txt');
while ~feof(fid)
    line = fgetl(fid);
    disp(line);
end
fclose(fid);
```

```erlang
% Erlang
{ok, Content} = file:read_file("file.txt").
```

```elixir
# Elixir
content = File.read!("file.txt")
# Or stream
"file.txt" |> File.stream!() |> Enum.each(&IO.puts/1)
```

```ocaml
(* OCaml *)
let content = In_channel.with_open_bin "file.txt" @@ fun ic ->
  In_channel.input_all ic
```

```fortran
! Fortran
open(unit=10, file='file.txt', status='old')
do
    read(10, '(A)', iostat=ios) line
    if (ios /= 0) exit
    print *, trim(line)
end do
close(10)
```

```ada
-- Ada
with Ada.Text_IO; use Ada.Text_IO;
F : File_Type;
Open(F, In_File, "file.txt");
while not End_Of_File(F) loop
    Put_Line(Get_Line(F));
end loop;
Close(F);
```

```prolog
% Prolog
open('file.txt', read, Stream),
read_line_to_codes(Stream, Line),
% ... process line
close(Stream).
```

## نوشتن یک فایل
```python
# Python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
```

```rust
// Rust
use std::fs;
fs::write("output.txt", "Hello, World!\n").expect("write error");
```

```go
// Go
os.WriteFile("output.txt", []byte("Hello, World!\n"), 0644)
```

```java
// Java
Files.writeString(Path.of("output.txt"), "Hello, World!\n");
```

```javascript
// JavaScript (Node.js)
fs.writeFileSync('output.txt', 'Hello, World!\n');
```

```c
// C
FILE *f = fopen("output.txt", "w");
fprintf(f, "Hello, World!\n");
fclose(f);
```

## درخواست های HTTP
```python
# Python
import requests
resp = requests.get("https://api.example.com/data")
data = resp.json()
```

```javascript
// JavaScript (browser)
const resp = await fetch("https://api.example.com/data");
const data = await resp.json();
```

```rust
// Rust (reqwest)
let resp = reqwest::get("https://api.example.com/data").await?;
let data: Value = resp.json().await?;
```

```go
// Go
resp, err := http.Get("https://api.example.com/data")
defer resp.Body.Close()
body, _ := io.ReadAll(resp.Body)
```

```java
// Java (HttpClient, Java 11+)
HttpClient client = HttpClient.newHttpClient();
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/data"))
    .build();
HttpResponse<String> resp = client.send(req, BodyHandlers.ofString());
```

```bash
# Bash (curl)
curl -s https://api.example.com/data | jq .
```

```ruby
# Ruby (net/http)
require 'net/http'
uri = URI("https://api.example.com/data")
response = Net::HTTP.get(uri)
```

```elixir
# Elixir (HTTPoison or Req)
{:ok, resp} = Req.get("https://api.example.com/data")
data = resp.body
```
