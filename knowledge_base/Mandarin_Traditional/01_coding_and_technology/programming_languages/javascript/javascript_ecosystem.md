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
# JavaScript — 生態系統與工具指南
本指南涵蓋了 JavaScript 生態系統中的基本工具、架構和基礎架構。
---

## 運行時
|運行時 |環境 |最適合 |
|---------|-------------|----------|
| **Node.js** |伺服器/CLI |後端、API、工具 |
| **德諾** |伺服器/CLI |預設安全，TypeScript 原生 |
| **髮髻** |伺服器/CLI |快速的內建捆綁器/測試運行器 |
| **瀏覽器** |客戶端|網頁應用程式|
---

## 套件管理
|工具|登記處 |特點|
|------|----------|----------|
| **npm** | npmjs.com |預設使用 Node.js |
| **紗線** | npmjs.com |工作區，PnP 模式 |
| **pnpm** | npmjs.com |快速、磁碟效率高、嚴格 |
| **小圓麵包** | npmjs.com |超快，內建 |
```bash
npm init -y                   # initialize project
npm install express           # add dependency
npm install -D typescript     # add dev dependency
npm run build                 # run script from package.json
```

---

## 建置工具和捆綁器
|工具|類型 |最適合 |
|------|------|----------|
| **投票** |捆綁器 |現代快速開發伺服器 |
| **esbuild** |捆綁器 |超快，基於 Go |
| **網路套件** |捆綁器 |成熟、高度可設定|
| **匯總** |捆綁器 |圖書館，tree-shaking |
| **包裹** |捆綁器 |零配置|
| **渦輪機組** |捆綁器 | Next.js，基於 Rust |
| **SWC** |編譯器|快速 TypeScript/JSX |
| **通天塔** |編譯器|翻譯、插件 |
---

## 框架
＃＃＃ 前端
|框架|類型 |最適合 |
|------------|------|----------|
| **反應** |使用者介面庫 |基於元件的 UI、生態系統 |
| **Vue** |進取|平易近人，偉大的DX |
| **苗條** |編譯器|運行時間最短，速度快 |
| **角度** |完整框架|企業，TypeScript 優先 |
| **固體** |反應式|細粒度反應性 |
| **天文** |靜態/SSR |內容網站、島嶼 |
### 後端
|框架|類型 |最適合 |
|------------|------|----------|
| **快遞** |微|簡單的 API、中介軟體 |
| **快點** |效能|高通量 API |
| **NestJS** |企業 |結構化、DI、TypeScript |
| **榮譽** |邊緣 |輕量級、多運行時 |
| **相思木** |現代|快遞繼任者|
---

## 測試
|框架|類型 |
|------------|------|
| **存取** |快速、Vite 原生 |
| **開玩笑** |成熟的快照測試 |
| **劇作家** | E2E，多重瀏覽器 |
| **柏樹** | E2E，開發者體驗|
| **測試庫** |元件測試|
| **摩卡** |靈活、基於插件 |
```bash
vitest                        # run tests
vitest --coverage             # with coverage
playwright test               # E2E tests
```

---

## 程式碼品質
|工具|目的|
|------|---------|
| **ESLint** | Linter（可設定規則）|
| **更漂亮** |程式碼格式化程式|
| **生物群落** |快速 linter + 格式化程式 (Rust) |
| **打字稿** |靜態類型檢查 |
| **ts 模式** | TS 的模式匹配 |
```json
// eslint.config.js (flat config)
export default [
  { rules: { "no-unused-vars": "warn" } }
];
```

---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 程式碼** |占主導地位，優秀的 JS/TS 支援 |
| **網路風暴** |功能齊全的 JetBrains IDE |
| **遊標** | AI 驅動的 VS Code 分叉 |
| **Neovim** |基於終端的LSP |
---

## 部署
|平台|類型 |
|----------|------|
| **維塞爾** |前端/無伺服器 (Next.js) |
| **網路化** |前端/Jamstack |
| **Cloudflare 工作人員** |邊緣運算|
| **鐵路** |全端PaaS |
| **Fly.io** |全球應用程式託管 |
| **AWS Lambda** |無伺服器|
| **碼頭工人** |貨櫃式|
---

＃＃ 概括
JavaScript 的生態系統是程式設計領域最大的。現代堆疊是：**Vite** 用於構建，**pnpm** 用於包，**Vitest** 用於測試，**ESLint + Prettier** 用於代碼質量，**React/Next.js** 或 **Vue/Nuxt** 用於前端，以及 **Vercel** 或 **Cloudflare** 用於部署。 TypeScript 現在對於任何嚴肅的專案都是必不可少的。生態系統發展迅速－保持最新狀態但避免框架流失。