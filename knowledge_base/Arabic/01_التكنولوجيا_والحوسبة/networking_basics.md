<!-- 
This file was automatically translated from English to Arabic.
Source: networking_basics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# أساسيات الشبكات

## نموذج OSI (7 طبقات)
- الطبقة الفيزيائية
- طبقة ربط البيانات
- طبقة الشبكة
- طبقة النقل
- طبقة الجلسة
- طبقة العرض
- طبقة التطبيق

## عنونة IP
### IPv4
- عنوان من 32 بت
- مثال: `192.168.1.10`

### IPv6
- عنوان من 128 بت
- مساحة أكبر بكثير

### النطاقات الخاصة
- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

### CIDR
- طريقة مختصرة لوصف الشبكات
- مثال: `192.168.1.0/24`

## DNS
### أنواع السجلات
- `A`
- `AAAA`
- `CNAME`
- `MX`
- `TXT`

### أدوات شائعة
- `nslookup`
- `dig`
- `ping`
- `traceroute`

## TCP و UDP
- TCP موثوق ومرتّب.
- UDP أسرع وأقل كلفة لكنه لا يضمن التسليم.

## التوجيه والتبديل
- المبدلات تعمل داخل الشبكة المحلية.
- الموجهات تربط الشبكات المختلفة.

## الشبكات اللاسلكية
- Wi‑Fi
- Bluetooth
- LTE / 5G
