<!-- 
此文件已从英语自动翻译成简体中文。
来源：coding_languages.md
注意：技术术语、代码示例和专有名词可能保留英文。
为提高准确性，请通过 pull request 贡献编辑。
-->

# 编程语言

## Python

Python 是一种高级、解释型、动态类型的通用编程语言。它强调可读性，并使用有意义的缩进作为块分隔符。

### 基本语法

```python
# 变量和类型
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 条件语句
if age >= 18:
    print("成人")
elif age >= 13:
    print("青少年")
else:
    print("儿童")

# 循环
for i in range(5):
    print(i)

while active:
    active = False
```

### 函数和类型注解

```python
def greet(name: str, times: int = 1) -> str:
    return (f"你好，{name}！" * times).strip()
```

### 列表推导式

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### 类和面向对象编程

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        return f"我叫{name}，今年{age}岁。"
```

## JavaScript

JavaScript 是一种解释型、面向对象、事件驱动的编程语言，主要用于客户端和服务器端 Web 开发。

### 基本语法

```javascript
// 变量和类型
let name = "Alice";
const age = 30;
let score = 9.5;
let active = true;

// 条件语句
if (age >= 18) {
    console.log("成人");
} else if (age >= 13) {
    console.log("青少年");
} else {
    console.log("儿童");
}

// 循环
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (active) {
    active = false;
}
```

### 函数

```javascript
function greet(name, times = 1) {
    return `你好，${name}！`.repeat(times).trim();
}

// 箭头函数
const greetArrow = (name, times = 1) => {
    return `你好，${name}！`.repeat(times).trim();
};
```

### 数组操作

```javascript
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## Java

Java 是一种编译型、面向对象、平台独立的编程语言，广泛用于企业应用程序和 Android 开发。

### 基本语法

```java
// 变量和类型
String name = "Alice";
int age = 30;
double score = 9.5;
boolean active = true;

// 条件语句
if (age >= 18) {
    System.out.println("成人");
} else if (age >= 13) {
    System.out.println("青少年");
} else {
    System.out.println("儿童");
}

// 循环
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (active) {
    active = false;
}
```

### 类和面向对象编程

```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String introduce() {
        return "我叫" + name + "，今年" + age + "岁。";
    }
}
```

## C++

C++ 是一种编译型、高性能、多用途的编程语言，用于系统、视频游戏和关键应用程序。

### 基本语法

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 变量和类型
    string name = "Alice";
    int age = 30;
    double score = 9.5;
    bool active = true;
    
    // 条件语句
    if (age >= 18) {
        cout << "成人" << endl;
    } else if (age >= 13) {
        cout << "青少年" << endl;
    } else {
        cout << "儿童" << endl;
    }
    
    // 循环
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (active) {
        active = false;
    }
    
    return 0;
}
```

## 编码基础（语言无关）

编程的基本概念对所有语言都是通用的：

- **变量**: 命名数据存储
- **数据类型**: 数据性质的定义（数字、文本、布尔值等）
- **控制结构**: 条件语句（if/else）和循环（for、while）
- **函数**: 可重用的代码块
- **数据结构**: 数组、列表、字典、集合
- **面向对象编程**: 类、对象、继承、多态
- **错误处理**: Try/catch、异常
- **输入/输出**: 数据读写

这些基本概念适用于任何选择的编程语言。掌握这些基础可以更容易地学习新语言。
