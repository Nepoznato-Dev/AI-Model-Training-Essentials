<!--
---
# Metadata
title: "JavaScript — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the JavaScript ecosystem including package managers, build tools, testing frameworks, linters, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [javascript, ecosystem, tooling, npm, node, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# جاوا اسکریپت - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم جاوا اسکریپت را پوشش می‌دهد.
---

## زمان اجرا
| زمان اجرا | محیط زیست | بهترین برای |
|---------|-------------|----------|
| **Node.js** | سرور/CLI | Backend، API ها، ابزارسازی |
| **دنو** | سرور/CLI | به طور پیش فرض ایمن، TypeScript native |
| **نان** | سرور/CLI | باندلر/آزمایشی سریع و داخلی |
| **مرورگر** | سمت مشتری | برنامه های کاربردی وب |
---

## مدیریت بسته
| ابزار | رجیستری | ویژگی ها |
|------|----------|----------|
| **npm** | npmjs.com | پیش فرض با Node.js |
| **نخ** | npmjs.com | فضاهای کاری، حالت PnP |
| **pnpm** | npmjs.com | سریع، کارآمد، سختگیر |
| **نان** | npmjs.com | فوق سریع، داخلی |
```bash
npm init -y                   # initialize project
npm install express           # add dependency
npm install -D typescript     # add dev dependency
npm run build                 # run script from package.json
```

---

## ابزار و بسته‌کننده‌های ساخت
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **Vite** | باندلر | سرور توسعه سریع، مدرن |
| **esbuild** | باندلر | فوق سریع، مبتنی بر Go |
| **وبک** | باندلر | بالغ، بسیار قابل تنظیم |
| **مجموعه** | باندلر | کتابخانه ها، درخت تکانی |
| **بسته** | باندلر | پیکربندی صفر |
| **توربوپک** | باندلر | Next.js، مبتنی بر Rust |
| **SWC** | کامپایلر | Fast TypeScript/JSX |
| **بابل** | کامپایلر | ترجمه، پلاگین |
---

## چارچوب
### Frontend
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **واکنش** | کتابخانه UI | رابط کاربری مبتنی بر مؤلفه، اکوسیستم |
| **Vue** | پیشرو | قابل دسترس، DX عالی |
| **Svelte** | کامپایلر | حداقل زمان اجرا، سریع |
| **زاویه** | فریمورک کامل | Enterprise، TypeScript-first |
| **جامد** | واکنشی | واکنش ریز دانه |
| **آسترو** | Static/SSR | سایت های محتوا، جزایر |
### Backend
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **اکسپرس** | میکرو | API های ساده، میان افزار |
| **تعطیف** | عملکرد | APIهای پرتوان |
| **NestJS** | شرکت | Structured، DI، TypeScript |
| **هنو** | لبه | سبک وزن، چند بار اجرا |
| **کوآ** | مدرن | جانشین اکسپرس |
---

## تست
| چارچوب | نوع |
|-----------|------|
| **Vitest** | سریع، بومی |
| **شوخی** | بالغ، تست فوری |
| **نمایشنامه نویس** | E2E، چند مرورگر |
| **سرو** | E2E، تجربه توسعه دهنده |
| **کتابخانه تست** | تست کامپوننت |
| **موکا** | انعطاف پذیر، مبتنی بر پلاگین |
```bash
vitest                        # run tests
vitest --coverage             # with coverage
playwright test               # E2E tests
```

---

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **ESLint** | لینتر (قوانین قابل تنظیم) |
| **زیباتر** | فرمت کننده کد |
| **بیوم** | لینتر سریع + فرمت کننده (Rust) |
| **TypeScript** | بررسی نوع استاتیک |
| **ts-pattern** | تطبیق الگو برای TS |
```json
// eslint.config.js (flat config)
export default [
  { rules: { "no-unused-vars": "warn" } }
];
```

---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| ** کد VS ** | پشتیبانی غالب و عالی JS/TS |
| **وب طوفان** | JetBrains IDE با امکانات کامل |
| **مکان نما** | فورک VS Code مجهز به هوش مصنوعی |
| **Neovim** | مبتنی بر ترمینال با LSP |
---

## استقرار
| پلت فرم | نوع |
|----------|------|
| **ورسل** | Frontend/Serverless (Next.js) |
| **Netlify** | Frontend/Jamstack |
| **Cloudflare Workers** | محاسبات لبه |
| **راه آهن** | تمام پشته PaaS |
| **Fly.io** | میزبانی برنامه، جهانی |
| **AWS Lambda** | بدون سرور |
| **داکر** | کانتینری |
---

## خلاصه
اکوسیستم جاوا اسکریپت بزرگترین در برنامه نویسی است. پشته مدرن عبارتند از: **Vite** برای ساختن، **pnpm** برای بسته‌ها، **Vitest** برای آزمایش، **ESLint + Prettier** برای کیفیت کد، **React/Next.js** یا **Vue/Nuxt** برای frontend، و **Vercel** یا **Cloudflare** برای استقرار. TypeScript اکنون برای هر پروژه جدی ضروری است. اکوسیستم به سرعت حرکت می کند - در حال حاضر بمانید اما از چرخش چارچوب اجتناب کنید.