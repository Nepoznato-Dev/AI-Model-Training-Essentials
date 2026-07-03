# Python 語法速查表

Python 3.x 語法和常見模式的快速參考。

---

## 基本語法

### 變數和資料型別
```python
# 變數賦值（無需宣告）
x = 5
name = "Alice"
is_active = True
price = 19.99

# 型別檢查
type(x)           # <class 'int'>
isinstance(x, int)  # True

# 型別轉換
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### 字串
```python
s = "Hello, World!"

# 切片
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # 反轉字串

# 方法
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # 移除空白
f"Value: {x}"     # f-string 格式化
```

---

## 控制流程

### 條件式
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# 三元運算子
result = "yes" if condition else "no"
```

### 迴圈
```python
# For 迴圈
for i in range(5):      # 0 到 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# While 迴圈
while x < 10:
    x += 1

# 迴圈控制
break       # 退出迴圈
continue    # 跳至下一次迭代
else:       # 如果迴圈完成而未中斷則執行
```

---

## 資料結構

### 串列
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # 加到結尾
lst.insert(0, 0)        # 在索引處插入
lst.remove(3)           # 依值移除
lst.pop()               # 移除並返回最後一個
lst.pop(0)              # 移除並返回第一個
lst.index(2)            # 尋找值的索引
lst.count(2)            # 計算出現次數
lst.sort()              # 就地排序
sorted(lst)             # 返回排序副本
lst.reverse()           # 就地反轉
lst[1:4]                # 切片
[i*2 for i in lst]      # 串列推導式
```

### 字典
```python
d = {"name": "Alice", "age": 30}

d["age"]                # 存取值
d.get("age", 0)         # 安全存取，帶預設值
d.keys()                # 取得所有鍵
d.values()              # 取得所有值
d.items()               # 取得鍵值對
d.update({"city": "NYC"})
del d["age"]            # 刪除鍵

{k: v*2 for k, v in d.items()}  # 字典推導式
```

### 集合
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - 重複項已移除

s.add(5)
s.remove(3)
s.discard(10)           # 如果存在則移除（無錯誤）
s.union({4, 5, 6})      # 組合集合
s.intersection({2, 3})  # 共同元素
s.difference({3, 4})    # s 中但不在其他集合中的元素
```

### 元組
```python
t = (1, 2, 3)
t[0]                    # 存取（不可變）
x, y, z = t             # 解包
```

---

## 函式

### 定義
```python
def greet(name, greeting="Hello"):
    """Docstring：描述函式"""
    return f"{greeting}, {name}!"

# 使用位置和關鍵字參數呼叫
greet("Alice")
greet("Bob", greeting="Hi")

# 可變參數
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### Lambda 函式
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## 類別

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 實例變數
        self.age = age
    
    def greet(self):          # 實例方法
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# 繼承
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## 檔案 I/O

```python
# 讀取檔案
with open("file.txt", "r") as f:
    content = f.read()        # 讀取整個檔案
    lines = f.readlines()     # 讀取為行的串列

# 寫入檔案
with open("file.txt", "w") as f:
    f.write("Hello\n")

# 附加模式
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## 錯誤處理

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
except Exception as e:
    print(f"General error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always executes")

# 拋出例外
raise ValueError("Invalid value")
```

---

## 模組和匯入

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# 常見的標準函式庫模組
os, sys, json, re, random, itertools, functools, pathlib
```

---

## 常見模式

### 串列操作
```python
# 過濾
evens = [x for x in lst if x % 2 == 0]

# 映射
squares = [x**2 for x in lst]

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Enumerate
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### 字串操作
```python
# 連接字串串列
", ".join(["a", "b", "c"])  # "a, b, c"

# 分割字串
"a,b,c".split(",")          # ['a', 'b', 'c']

# 檢查子字串
"test" in "this is a test"  # True

# 格式化字串
"{} {}".format("Hello", "World")
f"{value:.2f}"              # 2 位小數
```

### 字典操作
```python
# 合併字典
{**d1, **d2}
d1 | d2                     # Python 3.9+

# 預設值
d.get("key", default_value)

# 迭代
for k, v in d.items():
    pass
```

---

## 內建函式

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce 來自 functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## 快速提示

- 使用 `#` 進行單行註解
- 使用 `"""三引號"""`  進行文件字串和多行字串
- 縮排很重要（通常 4 個空格）
- 命名慣例：變數/函式使用 `snake_case`，類別使用 `PascalCase`
- `__name__ == "__main__"` 檢查腳本是否直接執行
- 使用 `virtualenv` 或 `venv` 進行專案隔離
- 使用 `pip install package_name` 安裝套件

---

*最後更新：2025年6月 | Python 3.x*
