---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# مقایسه خدمات ابری
مقایسه کنار هم از سه ارائه‌دهنده اصلی ابر - AWS، Azure و Google Cloud - در محاسبات، ذخیره‌سازی، پایگاه‌های داده، AI/ML، شبکه، نظارت و زیرساخت به عنوان کد. برای معمارانی مفید است که تصمیم می گیرند از کدام پلتفرم استفاده کنند، یا خدمات نقشه برداری از یک ابر به ابر دیگر.
---

## بررسی اجمالی ارائه دهنده
| | AWS | لاجوردی | Google Cloud (GCP) |
|---|-----|-------|--------------------|
| **سهم بازار** | ~31% (بزرگترین) | ~25% (دوم) | ~11% (سومین، سریعترین رشد) |
| **نقاط قوت** | وسعت خدمات؛ بلوغ؛ اکوسیستم | ادغام سازمانی؛ ابر هیبریدی؛ پشته مایکروسافت | داده / AI; Kubernetes; شبکه جهانی |
| **بهترین برای** | استارت آپ به شرکت ها؛ گسترده ترین کاتالوگ خدمات | شرکت های دارای Microsoft/Active Directory؛ هیبرید | حجم کاری فشرده داده؛ Kubernetes-بومی; AI/ML |
| **مناطق** | 33 منطقه، 105 AZ | بیش از 60 منطقه | 40+ منطقه، 100+ منطقه |
| **سطح آزاد** | 12 ماه ردیف رایگان + همیشه رایگان | 12 ماه رایگان + 200 دلار اعتبار | اعتبار 300 دلاری برای 90 روز + همیشه رایگان |
---

## محاسبه کنید
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **ماشین های مجازی** | EC2 (ابر محاسباتی الاستیک) | ماشین های مجازی | موتور محاسباتی |
| **مقیاس بندی خودکار** | گروه های مقیاس خودکار | مجموعه مقیاس ماشین مجازی | گروه های نمونه |
| **توابع بدون سرور** | لامبدا | توابع لاجوردی | توابع ابری |
| **رجیستری کانتینر** | ECR (Elastic Container Registry) | رجیستری کانتینر لاجورد | رجیستری مصنوعات |
| **ارکستراسیون کانتینری** | ECS / EKS | ACS / AKS | GKE / Cloud Run |
| **ظروف بدون سرور ** | Fargate | برنامه های کانتینر | Cloud Run |
| **پلتفرم برنامه (PaaS)** | Elastic Beanstalk، App Runner | سرویس اپلیکیشن | موتور برنامه |
| ** پردازش دسته ای ** | دسته AWS | دسته لاجوردی | دسته ابری |
| **GPU / محاسبات هوش مصنوعی** | EC2 (نمونه های P4d، P5) | ماشین های مجازی سری NC/ND | ماشین های مجازی A2/A3; TPU |
### مدل های قیمت گذاری VM
| مدل | AWS | لاجوردی | GCP |
|-------|-----|-------|-----|
| **در صورت تقاضا** | موارد درخواستی | پرداخت به موقع | بر حسب تقاضا |
| **محفوظ / متعهد** | موارد رزرو شده (1-3 سال) | ماشین های مجازی رزرو شده (1 تا 3 سال) | تخفیف استفاده متعهد (1 تا 3 سال) |
| **نقطه/قابل وقفه** | موارد نقطه ای | ماشین های مجازی نقطه ای | VMهای قابل پیش‌گیری / Spot VM |
| **طرح های پس انداز** | طرح های پس انداز | طرح های پس انداز | تخفیف استفاده متعهد |
---

## ذخیره سازی
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **ذخیره سازی اشیا** | S3 | Blob Storage | فضای ذخیره سازی ابری |
| **بلاک ذخیره سازی** | EBS | دیسک های مدیریت شده | دیسک ماندگار |
| **ذخیره سازی فایل** | EFS، FSx | فایل های لاجوردی | فروشگاه فایل |
| **بایگانی / سرد** | S3 Glacier, Deep Archive | Blob Cool/Archive layers | Cloud Storage Coldline/Archive |
| **انتقال داده** | گلوله برفی، DataSync | جعبه داده | دستگاه انتقال |
### مقایسه کلاس های ذخیره سازی
| مورد استفاده | AWS S3 | لکه لاجوردی | GCP Cloud Storage |
|----------|--------|-----------|------------------|
| **دسترسی مکرر** | S3 استاندارد | داغ | استاندارد |
| **دسترسی نادر ** | S3 Standard-IA | باحال | نزدیک |
| **دسترسی نادر** | S3 One Zone-IA | — | Coldline |
| **بایگانی** | S3 Glacier / Deep Archive | آرشیو | آرشیو |
---

## پایگاه های داده
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **رابطه ای (مدیریت شده)** | RDS (MySQL، PostgreSQL، Oracle، SQL Server) | پایگاه داده Azure (MySQL، PostgreSQL)؛ Azure SQL | Cloud SQL (MySQL، PostgreSQL) |
| **رابطه ای (ابر-بومی)** | Aurora (سازگار MySQL/PostgreSQL) | پایگاه داده Azure SQL (استخرهای الاستیک) | آچار ابری (توزیع شده در سطح جهانی) |
| **NoSQL (سند)** | DynamoDB | Cosmos DB (MongoDB API، SQL API) | فایر استور; فروشگاه داده |
| **NoSQL (ستون عریض)** | DynamoDB (همچنین) | Cosmos DB (Cassandra API) | Bigtable |
| **NoSQL (کلید-مقدار)** | DynamoDB، ElastiCache | Azure Cache برای Redis | Memorystore (Redis) |
| **نمودار** | نپتون | Cosmos DB (Gremlin API) | — |
| **سریال زمانی** | جریان زمانی | Azure Data Explorer | — |
| **لجر** | QLDB | Azure Confidential Ledger | — |
| **کش در حافظه** | ElastiCache (Redis، Memcached) | Azure Cache برای Redis | Memorystor |
| **جستجو** | سرویس OpenSearch | جستجوی هوش مصنوعی Azure | جستجوی ابری؛ Vertex AI Search |
| **انبار داده** | Redshift | تجزیه و تحلیل سیناپس | BigQuery |
---

## هوش مصنوعی و یادگیری ماشین
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **پلتفرم ML** | SageMaker | یادگیری ماشین لاجورد | Vertex AI |
| **APIهای از پیش آموزش دیده** | شناخت (دید)، پولی (TTS)، درک (NLP)، رونویسی | خدمات شناختی (بینایی، گفتار، زبان، تصمیم گیری) | Vision AI، گفتار به متن، API زبان طبیعی |
| **LLM / هوش مصنوعی مولد ** | بستر (کلود، لاما، تیتان) | سرویس Azure OpenAI (GPT-4، DALL-E) | Vertex AI (Gemini)؛ مدل باغ |
| **وکتور / جاسازی ها** | OpenSearch (k-NN)، پایگاه های دانش بستر | جستجوی هوش مصنوعی Azure (وکتور) | Vertex AI Vector Search, AlloyDB |
| **MLOps** | SageMaker Pipelines, Model Registry | Azure ML Pipelines, Model Registry | Pipelines Vertex AI, Model Registry |
| **برچسب گذاری داده** | SageMaker Ground Truth | Azure ML Data Labeling | برچسب‌گذاری داده‌های هوش مصنوعی Vertex |
| **هوش مصنوعی مکالمه** | لکس | سرویس ربات لاجورد | Dialogflow CX / ES |
| **ترجمه** | ترجمه | مترجم | API ترجمه |
---

## شبکه
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **شبکه مجازی** | VPC | شبکه مجازی (VNet) | VPC |
| **تعادل بار** | ELB/ALB/NLB/CLB | Load Balancer (برنامه، شبکه، دروازه) | توازن بار ابری |
| **DNS** | مسیر 53 | Azure DNS | Cloud DNS |
| **CDN** | CloudFront | درب ورودی لاجوردی | Cloud CDN |
| **درگاه API** | دروازه API | مدیریت API | دروازه API |
| **VPN** | VPN سایت به سایت، VPN مشتری | درگاه VPN | Cloud VPN |
| **Direct Connect / ExpressRoute** | اتصال مستقیم | ExpressRoute | اتصال ابری |
| **لینک خصوصی** | PrivateLink، VPC Endpoints | لینک خصوصی، نقاط پایانی خصوصی | Private Service Connect |
| **فایروال** | WAF، فایروال شبکه | فایروال لاجورد، WAF | زره ابری، فایروال |
| **محافظت DDoS** | سپر استاندارد / پیشرفته | حفاظت DDoS | زره ابری |
---

## نظارت و ثبت نام
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **متریک / نظارت** | CloudWatch | مانیتور لاجوردی | Cloud Monitoring (Stackdriver) |
| ** ثبت نام ** | گزارش های CloudWatch | Log Analytics (Log Monitor Azure) | ثبت ابر |
| **ردیابی** | اشعه ایکس | Application Insights | ردیابی ابری |
| **هشدار** | هشدارهای CloudWatch | هشدارهای مانیتور Azure | هشدارهای مانیتورینگ ابری |
| **داشبورد** | داشبوردهای CloudWatch | کتاب کار / داشبورد لاجورد | داشبوردهای مانیتورینگ ابری |
| **ردیابی خطا** | CloudWatch Synthetics | Application Insights | گزارش خطای ابری |
| **شخص ثالث** | Datadog، New Relic، PagerDuty | Datadog، New Relic، PagerDuty | Datadog، New Relic، PagerDuty |
---

## زیرساخت به عنوان کد و DevOps
| دسته خدمات | AWS | لاجوردی | GCP |
|-----------------|-----|-------|-----|
| **IaC (بومی)** | CloudFormation | الگوهای ARM / Bicep | مدیر استقرار / پولومی |
| **IaC (cross-cloud)** | Terraform، Pulumi، CDK | Terraform، Pulumi، Bicep | Terraform، Pulumi |
| **CI/CD** | CodePipeline، CodeBuild | Azure DevOps، GitHub Actions | ساخت ابر؛ استقرار ابری |
| **رجیستری کانتینر** | ECR | رجیستری کانتینر لاجورد | رجیستری مصنوعات |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD در AKS | Config Sync (Anthos) |
| **مدیریت اسرار** | مدیر اسرار فروشگاه پارامتر SSM | طاق کلید | مدیر مخفی |
---

## ملاحظات قیمت گذاری
| فاکتور | AWS | لاجوردی | GCP |
|--------|-----|-------|-----|
| **جزئیات صورتحساب** | در هر ثانیه (بعد از ساعت اول برای برخی) | در هر ثانیه | در هر ثانیه |
| **تخفیفات استفاده پایدار** | موارد رزرو شده / طرح های پس انداز | VM های رزرو شده | تخفیف استفاده متعهد |
| **نمونه های نقطه ای** | تا 90 درصد تخفیف | تا 90 درصد تخفیف | تا 91% تخفیف |
| **خروج داده** | شارژ شده (گران) | شارژ شده | قیمت یکسان بدون توجه به مقصد (اغلب ارزان تر) |
| **سطح آزاد** | 12 ماه + همیشه رایگان | 12 ماه + 200 دلار اعتبار | 300 دلار برای 90 روز + همیشه رایگان |
| **تخفیفات سازمانی** | برنامه تخفیف سازمانی (EDP) | MACC (قرارداد تعهد پولی) | استفاده متعهد + CUD |
---

## چه زمانی از کدام استفاده کنیم
| سناریو | توصیه شده | چرا |
|----------|------------|-----|
| ** گسترده ترین انتخاب خدمات؛ اکوسیستم بالغ ** | AWS | بزرگترین کاتالوگ; اکثر ادغام های شخص ثالث |
| **شرکت مایکروسافت؛ اکتیو دایرکتوری؛ هیبرید ** | لاجوردی | ادغام بومی AD. ابزار هیبریدی قوی |
| **ذخیره سازی داده ها BigQuery; analytics-heavy** | GCP | BigQuery بهترین در کلاس است. یکپارچه سازی داده های بدون درز |
| ** توسعه بومی Kubernetes** | GCP | GKE صیقلی ترین Kubernetes مدیریت شده است |
| **برنامه های مولد AI / LLM** | Azure یا GCP | Azure OpenAI برای مدل های GPT؛ Vertex AI for Gemini |
| **برنامه های کاربردی در مقیاس جهانی با تاخیر کم** | GCP | شبکه جهانی گوگل یک مزیت واقعی است |
| **حکومت / حجم کاری سنگین** | AWS یا Azure | اکثر گواهینامه های انطباق؛ مناطق GovCloud |
| **استارت آپ های حساس به هزینه** | GCP یا AWS | سطح رایگان GCP سخاوتمندانه است. AWS دارای اعتبار راه اندازی است |
| **پشته مایکروسافت / دات نت موجود ** | لاجوردی | ادغام دقیق با ویژوال استودیو، دات نت، آفیس 365 |
| **استراتژی چند ابری** | Terraform + هر سه | از Terraform برای مدیریت منابع در ابرها استفاده کنید |
---

## خلاصه
هر سه ابر توانمند، قابل اعتماد و دائما در حال گسترش هستند. انتخاب معمولاً به این نتیجه می رسد: اینکه تیم شما از قبل چه می داند، قراردادهای موجود شما چگونه به نظر می رسد و کدام خدمات خاص برای حجم کاری شما مهم است. چند ابری به طور فزاینده ای رایج است - از Terraform یا Pulumi برای جلوگیری از قفل شدن فروشنده در لایه زیرساخت استفاده کنید و هر ابری را برای بهترین عملکرد انتخاب کنید.