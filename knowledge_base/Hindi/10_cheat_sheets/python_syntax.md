# पाइथन सिंटैक्स चीट शीट

Python 3.x सिंटैक्स और सामान्य पैटर्न के लिए त्वरित संदर्भ।

---

## मूल सिंटैक्स

### वेरिएबल और डेटा टाइप
```python
# वेरिएबल असाइनमेंट (डिक्लेरेशन की आवश्यकता नहीं)
x = 5
name = "Alice"
is_active = True
price = 19.99

# टाइप जाँच
type(x)           # <class 'int'>
isinstance(x, int)  # True

# टाइप रूपांतरण
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### स्ट्रिंग्स
```python
s = "Hello, World!"

# स्लाइसिंग
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # स्ट्रिंग को उल्टा करें

# मेथड्स
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # खाली स्थान हटाएँ
f"Value: {x}"     # f-string का फ़ॉर्मैटिंग उपयोग
```

---

## कंट्रोल फ्लो

### शर्तें
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# टर्नरी ऑपरेटर
result = "yes" if condition else "no"
```

### लूप्स
```python
# for लूप
for i in range(5):      # 0 से 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# while लूप
while x < 10:
    x += 1

# लूप नियंत्रण
break       # लूप से बाहर निकलें
continue    # अगली पुनरावृत्ति पर जाएँ
else:       # यदि लूप break के बिना पूरा हो जाए तो चलाएँ
```

---

## डेटा स्ट्रक्चर्स

### लिस्ट्स
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # अंत में जोड़ें
lst.insert(0, 0)        # इंडेक्स पर जोड़ें
lst.remove(3)           # मान के आधार पर हटाएँ
lst.pop()               # अंतिम तत्व हटाएँ और लौटाएँ
lst.pop(0)              # पहला तत्व हटाएँ और लौटाएँ
lst.index(2)            # मान का इंडेक्स ढूँढें
lst.count(2)            # उपस्थितियों की गिनती करें
lst.sort()              # उसी लिस्ट में क्रमबद्ध करें
sorted(lst)             # क्रमबद्ध कॉपी लौटाएँ
lst.reverse()           # उसी लिस्ट को उल्टा करें
lst[1:4]                # स्लाइस
[i*2 for i in lst]      # लिस्ट कॉम्प्रिहेन्शन
```

### डिक्शनरीज़
```python
d = {"name": "Alice", "age": 30}

d["age"]                # मान एक्सेस करें
d.get("age", 0)         # डिफ़ॉल्ट के साथ सुरक्षित एक्सेस
d.keys()                # सभी कुंजियाँ प्राप्त करें
d.values()              # सभी मान प्राप्त करें
d.items()               # कुंजी-मान युग्म प्राप्त करें
d.update({"city": "NYC"})
del d["age"]            # कुंजी हटाएँ

{k: v*2 for k, v in d.items()}  # डिक्शनरी कॉम्प्रिहेन्शन
```

### सेट्स
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - डुप्लिकेट हटा दिए जाते हैं

s.add(5)
s.remove(3)
s.discard(10)           # यदि मौजूद हो तो हटाएँ (कोई त्रुटि नहीं)
s.union({4, 5, 6})      # सेट्स को मिलाएँ
s.intersection({2, 3})  # समान तत्व
s.difference({3, 4})    # वे तत्व जो s में हैं लेकिन दूसरे में नहीं
```

### ट्यूपल्स
```python
t = (1, 2, 3)
t[0]                    # एक्सेस (अपरिवर्तनीय)
x, y, z = t             # अनपैकिंग
```

---

## फंक्शन्स

### परिभाषा
```python
def greet(name, greeting="Hello"):
    """Docstring: Describe the function"""
    return f"{greeting}, {name}!"

# positional और keyword आर्ग्युमेंट्स के साथ कॉल करें
greet("Alice")
greet("Bob", greeting="Hi")

# परिवर्ती आर्ग्युमेंट्स
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### लैम्ब्डा फंक्शन्स
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## क्लासेस

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # इंस्टेंस वेरिएबल
        self.age = age
    
    def greet(self):          # इंस्टेंस मेथड
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# इनहेरिटेंस
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## फ़ाइल I/O

```python
# फ़ाइलें पढ़ना
with open("file.txt", "r") as f:
    content = f.read()        # पूरी फ़ाइल पढ़ें
    lines = f.readlines()     # पंक्तियों की सूची के रूप में पढ़ें

# फ़ाइलें लिखना
with open("file.txt", "w") as f:
    f.write("Hello\n")

# जोड़ने का मोड
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## त्रुटि प्रबंधन

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

# exception उत्पन्न करें
raise ValueError("Invalid value")
```

---

## मॉड्यूल्स और इम्पोर्ट्स

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# सामान्य स्टैंडर्ड लाइब्रेरी मॉड्यूल्स
os, sys, json, re, random, itertools, functools, pathlib
```

---

## सामान्य पैटर्न

### लिस्ट ऑपरेशन्स
```python
# फ़िल्टर
evens = [x for x in lst if x % 2 == 0]

# मैप
squares = [x**2 for x in lst]

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Enumerate
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### स्ट्रिंग ऑपरेशन्स
```python
# स्ट्रिंग्स की सूची को जोड़ें
", ".join(["a", "b", "c"])  # "a, b, c"

# स्ट्रिंग को विभाजित करें
"a,b,c".split(",")          # ['a', 'b', 'c']

# उपस्ट्रिंग जाँचें
"test" in "this is a test"  # True

# स्ट्रिंग्स को फ़ॉर्मैट करें
"{} {}".format("Hello", "World")
f"{value:.2f}"              # दशमलव के बाद 2 अंक
```

### डिक्शनरी ऑपरेशन्स
```python
# डिक्शनरीज़ को मर्ज करें
{**d1, **d2}
d1 | d2                     # Python 3.9+

# डिफ़ॉल्ट मान
d.get("key", default_value)

# पुनरावृत्ति करें
for k, v in d.items():
    pass
```

---

## बिल्ट-इन फंक्शन्स

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce functools से
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## त्वरित सुझाव

- एक-पंक्ति टिप्पणियों के लिए `#` का उपयोग करें
- `docstrings` और बहु-पंक्ति स्ट्रिंग्स के लिए `"""triple quotes"""` का उपयोग करें
- इंडेंटेशन महत्वपूर्ण है (आमतौर पर 4 spaces)
- नामकरण परंपराएँ: वेरिएबल्स/फंक्शन्स के लिए `snake_case`, क्लासेस के लिए `PascalCase`
- यह जाँचने के लिए `__name__ == "__main__"` कि स्क्रिप्ट सीधे चलाई गई है
- प्रोजेक्ट आइसोलेशन के लिए `virtualenv` या `venv` का उपयोग करें
- पैकेजेस को `pip install package_name` से इंस्टॉल करें

---

*अंतिम अपडेट: जून 2025 | Python 3.x*
