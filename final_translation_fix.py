#!/usr/bin/env python3
"""Final comprehensive translation fixer."""

import os
from pathlib import Path
from typing import Dict, Tuple

class FinalFixer:
    def __init__(self):
        self.stats = {'processed': 0, 'fixed': 0}
        
    ARABIC_FIXES = {
        '# Cloud العمارة': '# عمارة الحوسبة السحابية',
        '## Cloud الحوسبة الأساسيات': '## أساسيات الحوسبة السحابية',
        '### What is Cloud الحوسبة؟': '### ما هي الحوسبة السحابية؟',
        'On-demand delivery من الحوسبة resources': 'تسليم حسب الطلب لموارد الحوسبة',
        'over ال internet مع pay-as-you-go pricing': 'عبر الإنترنت مع تسعير الدفع حسب الاستخدام',
        '(servers, storage, databases, networking, software)': '(الخوادم، التخزين، قواعد البيانات، الشبكات، البرمجيات)',
        'Broad الشبكة Access': 'الوصول الواسع للشبكة',
        'متاح over الشبكة': 'متاح عبر الشبكة',
        'via standard mechanisms': 'عبر الآليات القياسية',
        'Multi-tenant model مع dynamic assignment': 'نموذج متعدد المستأجرين مع التعيين الديناميكي',
        'Scale outward و inward rapidly': 'التوسع والتقلص بسرعة',
        'Resource usage monitored و billed': 'مراقبة استخدام الموارد وإصدار الفواتير',
        'Cloud Deployment Models': 'نماذج نشر الحوسبة السحابية',
        'Cloud النشر Models': 'نماذج نشر الحوسبة السحابية',
        'Public Cloud': 'الحوسبة السحابية العامة',
        'Private Cloud': 'الحوسبة السحابية الخاصة',
        'Hybrid Cloud': 'الحوسبة السحابية الهجينة',
        'Multi-Cloud': 'حوسبة سحابية متعددة',
        'Community Cloud': 'حوسبة سحابية مجتمعية',
        'Owned by providers, shared infrastructure': 'مملوكة من قبل المزودين، بنية تحتية مشتركة',
        'Dedicated to single organization': 'مخصصة لمنظمة واحدة',
        'on-premises or hosted': 'محلية أو مستضافة',
        'Combination من public و private clouds': 'مزيج من الحوسبة السحابية العامة والخاصة',
        'Using multiple public cloud providers': 'استخدام مزودي حوسبة سحابية عامة متعددين',
        'Shared by organizations مع common concerns': 'مشتركة بين منظمات ذات اهتمامات مشتركة',
        'Service Models': 'نماذج الخدمة',
        'Infrastructure as a Service': 'البنية التحتية كخدمة',
        'Platform as a Service': 'المنصة كخدمة',
        'Software as a Service': 'البرمجيات كخدمة',
        'Function as a Service': 'الدالة كخدمة',
        'Serverless': 'بدون خادم',
        'Provides': 'يوفر',
        'Virtual machines': 'آلات افتراضية',
        'operating الأنظمة': 'أنظمة التشغيل',
        'Examples': 'أمثلة',
        'Use Cases': 'حالات الاستخدام',
        'Lift-و-shift migrations': 'هجرات الرفع والنقل',
        'التطوير environments': 'بيئات التطوير',
        'high-control needs': 'احتياجات تحكم عالي',
        'Development platforms': 'منصات التطوير',
        'middleware': 'برمجيات وسيطة',
        'Application التطوير': 'تطوير التطبيقات',
        'API النشر': 'نشر واجهات البرمجة',
        'microservices': 'الخدمات المصغرة',
        'Complete applications over internet': 'تطبيقات كاملة عبر الإنترنت',
        'Email': 'البريد الإلكتروني',
        'CRM': 'إدارة علاقات العملاء',
        'collaboration': 'التعاون',
        'business applications': 'تطبيقات الأعمال',
        'Event-driven function execution': 'تنفيذ الدوال المدفوعة بالأحداث',
        'Event processing': 'معالجة الأحداث',
        'APIs': 'واجهات البرمجة',
        'scheduled tasks': 'مهام مجدولة',
        'real-time processing': 'معالجة في الوقت الفعلي',
    }

    def apply(self, content: str, fixes: Dict[str, str]) -> Tuple[str, int]:
        result = content
        changes = 0
        for old, new in sorted(fixes.items(), key=lambda x: -len(x[0])):
            if old in result:
                result = result.replace(old, new)
                changes += 1
        return result, changes
    
    def run(self):
        base = Path('/workspace/knowledge_base')
        for md_file in (base / 'Arabic').rglob('*.md'):
            self.stats['processed'] += 1
            try:
                content = md_file.read_text(encoding='utf-8')
                fixed, n = self.apply(content, self.ARABIC_FIXES)
                if n > 0:
                    md_file.write_text(fixed, encoding='utf-8')
                    self.stats['fixed'] += 1
                    print(f"✓ {md_file.name}")
            except Exception as e:
                print(f"✗ {md_file}: {e}")
        
        # Fix Spanish critical error
        for md_file in (base / 'Spanish').rglob('*.md'):
            self.stats['processed'] += 1
            try:
                content = md_file.read_text(encoding='utf-8')
                if 'vendor lock-في' in content:
                    md_file.write_text(content.replace('vendor lock-في', 'vendor lock-in'), encoding='utf-8')
                    self.stats['fixed'] += 1
                    print(f"✓ Spanish: {md_file.name}")
            except Exception as e:
                print(f"✗ {md_file}: {e}")
        
        print(f"\nDone! Processed: {self.stats['processed']}, Fixed: {self.stats['fixed']}")

if __name__ == '__main__':
    FinalFixer().run()
