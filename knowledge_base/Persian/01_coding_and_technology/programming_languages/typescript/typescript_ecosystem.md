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
# TypeScript - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم TypeScript را پوشش می‌دهد. TypeScript بیشتر اکوسیستم خود را با جاوا اسکریپت به اشتراک می گذارد اما ابزارهای تخصصی خود را دارد.
---

## کامپایلر و بررسی نوع
| ابزار | هدف |
|------|---------|
| **tsc** | کامپایلر رسمی TypeScript |
| **ts-node** | TS را مستقیماً (dev) اجرا کنید |
| **tsx** | اجرای سریع TS (esbuild) |
| **SWC** | کامپایلر مبتنی بر زنگ |
| **esbuild** | باندلر فوق سریع با پشتیبانی TS |
| **TypeScript SDK** | یکپارچه سازی IDE |
```bash
tsc --init                      # create tsconfig.json
tsc --noEmit                    # type-check only
tsc --watch                     # watch mode
tsx src/index.ts                # run TypeScript directly
```

---

## مدیریت بسته
مانند جاوا اسکریپت: **npm**، **pnpm**، ** نخ**، **bun**. TypeScript از رجیستری npm (بسته های`@types/*`برای تعاریف نوع) استفاده می کند.
```bash
npm install -D @types/node @types/express  # type definitions
npx typesync                               # auto-install missing types
```

---

## منابع تعریف را تایپ کنید
| منبع | هدف |
|--------|---------|
| **حتما تایپ شده** | بسته های`@types/*`نگهداری شده توسط جامعه |
| **انواع همراه** | کتابخانه ها`.d.ts`خود را ارسال می کنند
| **چالش های نوع ** | تمرین انواع TypeScript |
| **type-fest** | مجموعه انواع ابزار |
---

## ابزارهای ساخت
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **Vite** | باندلر | توسعه سریع، HMR |
| **تساپ** | باندلر TS | ساختمان کتابخانه (مبتنی بر esbuild) |
| **تجمیع + افزونه** | باندلر | کتابخانه ها |
| **پک وب + ts-loader** | باندلر | برنامه های پیچیده |
| **tsc** | کامپایلر | پروژه های ساده |
| **pkgroll** | بسته بند | بسته های npm |
---

## چارچوب (TypeScript-First)
### Frontend
| چارچوب | پشتیبانی TS |
|-----------|-----------|
| **Next.js** | توکار درجه یک |
| **Nuxt 3** | داخلی |
| **SvelteKit** | داخلی |
| **زاویه** | TypeScript مورد نیاز |
| **ریمیکس** | داخلی |
| **آسترو** | داخلی |
### Backend
| چارچوب | پشتیبانی TS |
|-----------|-----------|
| **tRPC** | ایمنی از نوع انتها به انتها |
| **NestJS** | TypeScript-first |
| **هنو** | TypeScript-first |
| **تعطیف** | پشتیبانی از نوع خوب |
| **اکسپرس** | از طریق @types/express |
---

## تست
| چارچوب | پشتیبانی TS |
|-----------|-----------|
| **Vitest** | Native TypeScript |
| **Jest + ts-jest** | از طریق ترانسفورماتور |
| **نمایشنامه نویس** | Native TypeScript |
| **سرو** | Native TypeScript |
---

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **ESLint + typescript-eslint** | پرده زدن با قوانین نوع آگاه |
| **زیباتر** | قالب بندی |
| **بیوم** | پرز سریع + فرمت |
| **ts-prune** | یافتن صادرات بلااستفاده |
| **داپچک** | پیدا کردن وابستگی های استفاده نشده |
| **madge** | تجسم وابستگی |
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

## IDE ها و ویرایشگرها
| IDE | پشتیبانی TS |
|-----|-----------|
| ** کد VS ** | ساخته شده توسط تیم TS، بهترین پشتیبانی |
| **وب طوفان** | بازسازی عالی |
| **مکان نما** | مجهز به هوش مصنوعی |
---

## ایمنی نوع تمام پشته
| ابزار | هدف |
|------|---------|
| **tRPC** | انواع انتها به انتها بدون کدژن |
| **زود** | اعتبار سنجی زمان اجرا + استنتاج نوع |
| **پریسما** | نوع ایمن ORM |
| **نم نم نم باران** | نوع ایمن SQL |
| **OpenAPI + codegen** | تولید نوع API |
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

## استقرار
مانند جاوا اسکریپت: **Vercel**، **Netlify**، **Cloudflare Workers**، **Docker**، **AWS Lambda**، و غیره. TypeScript به جاوا اسکریپت کامپایل می‌شود، بنابراین همه گزینه‌های استقرار JS کار می‌کنند.
---

## خلاصه
اکوسیستم TypeScript از کتابخانه وسیع جاوا اسکریپت استفاده می کند و در عین حال ایمنی نوع را اضافه می کند. پشته مدرن عبارتند از: **Vite** برای ساختن، **Vitest** برای آزمایش، **typescript-eslint** برای linting، **Zod** برای اعتبارسنجی زمان اجرا، **tRPC** برای ایمنی نوع سرتاسر، **Prisma** یا **Drizzle** برای دسترسی نوع ایمن به پایگاه داده، و **Next.jsckt** یا Full Framework **Next.jsckt** یا کامل است. ابرقدرت تایپ اسکریپت در زمان کامپایل باگ هایی را پیدا می کند و در عین حال وسعت اکوسیستم جاوا اسکریپت را حفظ می کند.