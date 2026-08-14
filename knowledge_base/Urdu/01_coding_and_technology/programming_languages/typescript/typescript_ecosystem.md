<!--
---
# Metadata
title: "TypeScript — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the TypeScript ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [typescript, ecosystem, tooling, npm, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# TypeScript — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ TypeScript ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔ TypeScript اپنے ایکو سسٹم کا زیادہ تر حصہ JavaScript کے ساتھ شیئر کرتا ہے لیکن اس کے اپنے مخصوص ٹولز ہیں۔
---

## کمپائلر اور ٹائپ چیکنگ
| ٹول | مقصد |
|------|---------|
| **tsc** | آفیشل ٹائپ اسکرپٹ کمپائلر |
| **ts-node** | TS کو براہ راست چلائیں (dev) |
| **tsx** | تیز رفتار TS عملدرآمد (esbuild) |
| **SWC** | زنگ پر مبنی کمپائلر |
| **بناؤ** | TS سپورٹ کے ساتھ الٹرا فاسٹ بنڈلر |
| **TypeScript SDK** | IDE انضمام |
```bash
tsc --init                      # create tsconfig.json
tsc --noEmit                    # type-check only
tsc --watch                     # watch mode
tsx src/index.ts                # run TypeScript directly
```

---

## پیکیج مینجمنٹ
JavaScript کی طرح: **npm**، **pnpm**، **سوت**، **بن**۔ TypeScript npm رجسٹری کا استعمال کرتا ہے ( قسم کی تعریفوں کے لیے`@types/*`پیکجز)۔
```bash
npm install -D @types/node @types/express  # type definitions
npx typesync                               # auto-install missing types
```

---

## قسم کی تعریف کے ذرائع
| ماخذ | مقصد |
|---------|---------|
| **یقینی طور پر ٹائپ شدہ** | کمیونٹی کے زیر انتظام`@types/*`پیکیجز |
| **بنڈل شدہ اقسام** | لائبریریاں اپنے`.d.ts`|
| **قسم کے چیلنجز** | TypeScript کی اقسام کی مشق کریں |
| **ٹائپ فیسٹ** | افادیت کی اقسام کا مجموعہ |
---

## ٹولز بنائیں
| ٹول | قسم | کے لیے بہترین |
|------|------|---------|
| **وائٹ** | بنڈلر | فاسٹ دیو، HMR |
| **ٹسپ** | TS بنڈلر | لائبریری کی عمارت (esbuild-based) |
| **رول اپ + پلگ ان** | بنڈلر | لائبریریاں |
| **ویب پیک + ٹی ایس لوڈر** | بنڈلر | پیچیدہ ایپس |
| **tsc** | مرتب کرنے والا | سادہ منصوبے |
| **pkgroll** | پیکیج بنڈلر | npm پیکجز |
---

## فریم ورک (TypeScript-First)
### فرنٹ اینڈ
| فریم ورک | TS سپورٹ |
|------------|------------|
| **Next.js** | بلٹ ان، فرسٹ کلاس |
| **نکسٹ 3** | بلٹ ان |
| **SvelteKit** | بلٹ ان |
| **کونیی** | TypeScript درکار ہے |
| **ریمکس** | بلٹ ان |
| **آسٹرو** | بلٹ ان |
### بیک اینڈ
| فریم ورک | TS سپورٹ |
|------------|------------|
| **tRPC** | اینڈ ٹو اینڈ ٹائپ سیفٹی |
| **NestJS** | TypeScript-first |
| **ہونو** | TypeScript-first |
| **تیز بنائیں** | اچھی قسم کی حمایت |
| **ایکسپریس** | @types/express کے ذریعے |
---

## ٹیسٹنگ
| فریم ورک | TS سپورٹ |
|------------|------------|
| **ویسٹ** | مقامی ٹائپ اسکرپٹ |
| **مذاق + مذاق** | ٹرانسفارمر کے ذریعے |
| ** ڈرامہ نگار** | مقامی ٹائپ اسکرپٹ |
| **صنوبر** | مقامی ٹائپ اسکرپٹ |
---

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ESLint + typescript-eslint** | قسم سے آگاہ قواعد کے ساتھ لنٹنگ |
| **خوبصورت** | فارمیٹنگ |
| **بائیوم** | فاسٹ لنٹ + فارمیٹ |
| **ts-prune** | غیر استعمال شدہ برآمدات تلاش کریں |
| **ڈیپ چیک** | غیر استعمال شدہ انحصار تلاش کریں |
| **ماج** | انحصار کا تصور |
```json
// tsconfig.json (strict)
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "moduleResolution": "bundler",
    "target": "ES2022",
    "module": "ES2022"
  }
}
```

---

## IDEs اور ایڈیٹرز
| IDE | TS سپورٹ |
|------|------------|
| ** VS کوڈ** | TS ٹیم کی طرف سے بنایا گیا، بہترین تعاون |
| **ویب طوفان** | بہترین ری فیکٹرنگ |
| **کرسر** | AI سے چلنے والا |
---

## مکمل اسٹیک قسم کی حفاظت
| ٹول | مقصد |
|------|---------|
| **tRPC** | کوڈجن کے بغیر اختتام سے آخر تک کی اقسام |
| **زوڈ** | رن ٹائم توثیق + قسم کا اندازہ |
| **پرزم** | ٹائپ سیف ORM |
| **بوندا باندی** | ٹائپ سیف ایس کیو ایل |
| **OpenAPI + codegen** | API قسم کی نسل |
```typescript
// Zod: runtime validation with type inference
import { z } from "zod";

const UserSchema = z.object({
  name: z.string().min(2),
  email: z.string().email(),
  age: z.number().int().positive(),
});

type User = z.infer<typeof UserSchema>;
// { name: string; email: string; age: number; }

const user = UserSchema.parse(data); // throws if invalid
```

---

## تعیناتی۔
JavaScript کی طرح: **Vercel**، **Netlify**، **Cloudflare Workers**، **Docker**، **AWS Lambda**، وغیرہ۔ TypeScript جاوا اسکرپٹ پر مرتب ہوتا ہے، لہذا JS تعیناتی کے تمام اختیارات کام کرتے ہیں۔
---

## خلاصہ
ٹائپ سیفٹی کو شامل کرتے ہوئے TypeScript کا ماحولیاتی نظام JavaScript کی وسیع لائبریری کا فائدہ اٹھاتا ہے۔ جدید اسٹیک یہ ہے: **Vite** عمارت کے لیے، **Vitest** ٹیسٹنگ کے لیے، **typescript-eslint** linting کے لیے، **Zod** رن ٹائم توثیق کے لیے، **tRPC** اینڈ ٹو اینڈ ٹائپ سیفٹی کے لیے، **Prisma** یا **Drizzle** ٹائپ سیف ڈیٹا بیس تک رسائی کے لیے، اور **Next** یا مکمل فریم کے لیے TypeScript کی سپر پاور جاوا اسکرپٹ کے ماحولیاتی نظام کی وسعت کو برقرار رکھتے ہوئے کمپائل کے وقت کیڑے پکڑ رہی ہے۔