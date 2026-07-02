# ورقة مرجعية سريعة لصياغة بايثون

مرجع سريع لصياغة Python 3.x والأنماط الشائعة.

---

## الصياغة الأساسية

### المتغيرات وأنواع البيانات
```python
# إسناد المتغيرات (لا حاجة للتصريح المسبق)
x = 5
name = "Alice"
is_active = True
price = 19.99

# التحقق من النوع
type(x)           # <class 'int'>
isinstance(x, int)  # True

# تحويل النوع
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### السلاسل النصية (Strings)
```python
s = "Hello, World!"

# التقطيع (Slicing)
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # عكس السلسلة

# الدوال (Methods)
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # إزالة المسافات البيضاء
f"Value: {x}"     # تنسيق f-string
```

---

## التحكم في تدفق البرنامج

### الجمل الشرطية
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# عامل الشرط الثلاثي (Ternary operator)
result = "yes" if condition else "no"
```

### الحلقات التكرارية
```python
# حلقة for
for i in range(5):      # من 0 إلى 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# حلقة while
while x < 10:
    x += 1

# التحكم في الحلقة
break       # الخروج من الحلقة
continue    # الانتقال إلى التكرار التالي
else:       # تُنفَّذ إذا اكتملت الحلقة دون break
```

---

## هياكل البيانات

### القوائم (Lists)
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # الإضافة في النهاية
lst.insert(0, 0)        # الإدراج عند فهرس معين
lst.remove(3)           # الحذف بالقيمة
lst.pop()               # حذف وإرجاع العنصر الأخير
lst.pop(0)              # حذف وإرجاع العنصر الأول
lst.index(2)            # إيجاد فهرس القيمة
lst.count(2)            # عد التكرارات
lst.sort()              # الترتيب في المكان
sorted(lst)             # إرجاع نسخة مرتبة
lst.reverse()           # العكس في المكان
lst[1:4]                # تقطيع (Slice)
[i*2 for i in lst]      # قائمة مُشتقة (List comprehension)
```

### القواميس (Dictionaries)
```python
d = {"name": "Alice", "age": 30}

d["age"]                # الوصول إلى القيمة
d.get("age", 0)         # وصول آمن مع قيمة افتراضية
d.keys()                # الحصول على جميع المفاتيح
d.values()              # الحصول على جميع القيم
d.items()               # الحصول على أزواج المفتاح والقيمة
d.update({"city": "NYC"})
del d["age"]            # حذف مفتاح

{k: v*2 for k, v in d.items()}  # قاموس مُشتق (Dict comprehension)
```

### المجموعات (Sets)
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - تُزال التكرارات

s.add(5)
s.remove(3)
s.discard(10)           # الحذف إن وُجد (بدون خطأ)
s.union({4, 5, 6})      # دمج المجموعات
s.intersection({2, 3})  # العناصر المشتركة
s.difference({3, 4})    # العناصر الموجودة في s وغير موجودة في الأخرى
```

### الصفوف (Tuples)
```python
t = (1, 2, 3)
t[0]                    # الوصول (غير قابل للتغيير)
x, y, z = t             # فك التغليف (Unpacking)
```

---

## الدوال

### التعريف
```python
def greet(name, greeting="Hello"):
    """توثيق الدالة (Docstring): وصف الدالة"""
    return f"{greeting}, {name}!"

# الاستدعاء بوسائط موضعية ووسائط بالاسم
greet("Alice")
greet("Bob", greeting="Hi")

# وسائط متغيرة العدد
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### دوال لامدا (Lambda)
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## الأصناف (Classes)

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # متغير النسخة (Instance variable)
        self.age = age
    
    def greet(self):          # دالة النسخة (Instance method)
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# الوراثة (Inheritance)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## عمليات إدخال/إخراج الملفات

```python
# قراءة الملفات
with open("file.txt", "r") as f:
    content = f.read()        # قراءة الملف بالكامل
    lines = f.readlines()     # القراءة كقائمة من الأسطر

# كتابة الملفات
with open("file.txt", "w") as f:
    f.write("Hello\n")

# وضع الإلحاق (Append)
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## معالجة الأخطاء

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

# إثارة استثناء
raise ValueError("Invalid value")
```

---

## الوحدات والاستيراد

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# وحدات المكتبة القياسية الشائعة
os, sys, json, re, random, itertools, functools, pathlib
```

---

## أنماط شائعة

### عمليات القوائم
```python
# التصفية (Filter)
evens = [x for x in lst if x % 2 == 0]

# التحويل (Map)
squares = [x**2 for x in lst]

# الدمج (Zip)
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# الترقيم (Enumerate)
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### عمليات السلاسل النصية
```python
# دمج قائمة من السلاسل النصية
", ".join(["a", "b", "c"])  # "a, b, c"

# تقسيم سلسلة نصية
"a,b,c".split(",")          # ['a', 'b', 'c']

# التحقق من سلسلة فرعية
"test" in "this is a test"  # True

# تنسيق السلاسل النصية
"{} {}".format("Hello", "World")
f"{value:.2f}"              # منزلتان عشريتان
```

### عمليات القواميس
```python
# دمج القواميس
{**d1, **d2}
d1 | d2                     # Python 3.9+

# قيمة افتراضية
d.get("key", default_value)

# التكرار
for k, v in d.items():
    pass
```

---

## الدوال المضمّنة

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce من functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## نصائح سريعة

- استخدم `#` للتعليقات ذات السطر الواحد
- استخدم `"""علامات اقتباس ثلاثية"""` لتوثيق الدوال (docstrings) والسلاسل النصية متعددة الأسطر
- المسافة البادئة (Indentation) مهمة (عادة 4 مسافات)
- اتفاقيات التسمية: `snake_case` للمتغيرات/الدوال، و`PascalCase` للأصناف
- `__name__ == "__main__"` للتحقق مما إذا كان السكربت يُشغَّل مباشرة
- استخدم `virtualenv` أو `venv` لعزل المشروع
- ثبّت الحزم باستخدام `pip install package_name`

---

*آخر تحديث: يونيو 2025 | Python 3.x*
