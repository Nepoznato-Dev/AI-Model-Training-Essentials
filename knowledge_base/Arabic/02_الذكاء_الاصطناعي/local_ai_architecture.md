<!-- 
This file was automatically translated from English to Arabic.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# بنية الذكاء الاصطناعي المحلي

## لماذا نشغّل الذكاء الاصطناعي محليًا؟
- الخصوصية
- التحكم الكامل بالبيانات
- زمن استجابة أقل
- العمل دون اتصال
- خفض التكاليف المتكررة

## متطلبات العتاد
### ذاكرة GPU (VRAM)
كلما زادت VRAM أمكن تشغيل نماذج أكبر أو بدقة أعلى.

### RAM
تساعد في التحميل والمعالجة والـ offloading.

### التخزين
- ملفات النموذج
- ذاكرة التخزين المؤقت
- السجلات

### CPU
مهم في المعالجة المسبقة والتحميل والاستدلال عند غياب GPU قوي.

## التكميم
- يقلل الحجم والمتطلبات.
- صيغ شائعة: `GGUF` و `Q4` و `Q5` و `Q8`.

## محركات الاستدلال
- `llama.cpp`
- `Ollama`
- `vLLM`
- `LM Studio`

## اختيار النموذج
- اختر النموذج حسب الذاكرة والجودة وسرعة الاستجابة.
- اختبر عدة صيغ قبل الاعتماد.

## النشر المحلي
- تنزيل النموذج
- تشغيل الخادم
- ضبط المنفذ والموارد
- مراقبة الاستهلاك
