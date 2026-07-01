<!-- 
Bu dosya İngilizceden Türkçeye otomatik olarak çevrilmiştir.
Kaynak: coding_languages.md
Not: Teknik terimler, kod örnekleri ve özel isimler İngilizce kalabilir.
Doğruluk iyileştirmeleri için lütfen pull request yoluyla düzenlemeler katkısında bulunun.
-->

# Programlama Dilleri

## Python

Python, yüksek seviyeli, yorumlanan, dinamik tipli ve genel amaçlı bir programlama dilidir. Okunabilirliği vurgular ve blok sınırlayıcıları olarak anlamlı girinti kullanır.

### Temel Sözdizimi

```python
# Değişkenler ve tipler
ad: str = "Alice"
yas: int = 30
puan: float = 9.5
aktif: bool = True

# Koşullar
if yas >= 18:
    print("yetişkin")
elif yas >= 13:
    print("ergen")
else:
    print("çocuk")

# Döngüler
for i in range(5):
    print(i)

while aktif:
    aktif = False
```

### Fonksiyonlar ve Tip Açıklamaları

```python
def selamla(ad: str, kez: int = 1) -> str:
    return (f"Merhaba, {ad}! " * kez).strip()
```

### Liste Anlamaları

```python
kareler = [x**2 for x in range(10)]
ciftler = [x for x in range(20) if x % 2 == 0]
```

### Sınıflar ve OOP

```python
class Kisi:
    def __init__(self, ad: str, yas: int):
        self.ad = ad
        self.yas = yas
    
    def tanit(self) -> str:
        return f"Benim adım {self.ad} ve {self.yas} yaşındayım."
```

## JavaScript

JavaScript, yorumlanan, nesne yönelimli ve olay güdümlü bir programlama dilidir, öncelikle istemci ve sunucu tarafı web geliştirme için kullanılır.

### Temel Sözdizimi

```javascript
// Değişkenler ve tipler
let ad = "Alice";
const yas = 30;
let puan = 9.5;
let aktif = true;

// Koşullar
if (yas >= 18) {
    console.log("yetişkin");
} else if (yas >= 13) {
    console.log("ergen");
} else {
    console.log("çocuk");
}

// Döngüler
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (aktif) {
    aktif = false;
}
```

### Fonksiyonlar

```javascript
function selamla(ad, kez = 1) {
    return `Merhaba, ${ad}! `.repeat(kez).trim();
}

// Ok fonksiyonu
const selamlaOk = (ad, kez = 1) => {
    return `Merhaba, ${ad}! `.repeat(kez).trim();
};
```

### Dizi Manipülasyonu

```javascript
const sayilar = [1, 2, 3, 4, 5];
const kareler = sayilar.map(x => x ** 2);
const ciftler = sayilar.filter(x => x % 2 === 0);
const toplam = sayilar.reduce((acc, x) => acc + x, 0);
```

## Java

Java, derlenen, nesne yönelimli ve platformdan bağımsız bir programlama dilidir, kurumsal uygulamalarda ve Android geliştirmede yaygın olarak kullanılır.

### Temel Sözdizimi

```java
// Değişkenler ve tipler
String ad = "Alice";
int yas = 30;
double puan = 9.5;
boolean aktif = true;

// Koşullar
if (yas >= 18) {
    System.out.println("yetişkin");
} else if (yas >= 13) {
    System.out.println("ergen");
} else {
    System.out.println("çocuk");
}

// Döngüler
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (aktif) {
    aktif = false;
}
```

### Sınıflar ve OOP

```java
public class Kisi {
    private String ad;
    private int yas;
    
    public Kisi(String ad, int yas) {
        this.ad = ad;
        this.yas = yas;
    }
    
    public String tanit() {
        return "Benim adım " + ad + " ve " + yas + " yaşındayım.";
    }
}
```

## C++

C++, derlenen, yüksek performanslı ve çok yönlü bir programlama dilidir, sistemler, video oyunları ve kritik uygulamalar için kullanılır.

### Temel Sözdizimi

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Değişkenler ve tipler
    string ad = "Alice";
    int yas = 30;
    double puan = 9.5;
    bool aktif = true;
    
    // Koşullar
    if (yas >= 18) {
        cout << "yetişkin" << endl;
    } else if (yas >= 13) {
        cout << "ergen" << endl;
    } else {
        cout << "çocuk" << endl;
    }
    
    // Döngüler
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (aktif) {
        aktif = false;
    }
    
    return 0;
}
```

## Kodlamanın Temelleri (Dil Bağımsız)

Temel programlama kavramları tüm dillerde ortaktır:

- **Değişkenler**: İsimlendirilmiş veri depolama
- **Veri tipleri**: Verinin doğasının tanımlanması (sayılar, metin, booleanlar vb.)
- **Kontrol yapıları**: Koşullar (if/else) ve döngüler (for, while)
- **Fonksiyonlar**: Yeniden kullanılabilir kod blokları
- **Veri yapıları**: Diziler, listeler, sözlükler, kümeler
- **Nesne yönelimli programlama**: Sınıflar, nesneler, kalıtım, çok biçimlilik
- **Hata yönetimi**: Try/catch, istisnalar
- **Giriş/Çıkış**: Veri okuma ve yazma

Bu temel kavramlar, seçilen programlama dilinden bağımsız olarak geçerlidir. Bu temellerin hakimiyeti, yeni dilleri daha kolay öğrenmeyi sağlar.
