#!/usr/bin/env python3
"""
Script to fix Arabic translations in knowledge_base/Arabic/
This replaces mixed English-Arabic text with proper Arabic translations.
"""

import os
import re
from pathlib import Path

# Translation dictionary for common technical terms
TERM_TRANSLATIONS = {
    # Cloud Architecture terms
    r'\bCloud\b': 'سحابة',
    r'\bCloud Computing\b': 'الحوسبة السحابية',
    r'\bArchitecture\b': 'العمارة',
    r'Cloud العمارة': 'عمارة الحوسبة السحابية',
    r'Cloud الحوسبة الأساسيات': 'أساسيات الحوسبة السحابية',
    r'What is Cloud الحوسبة': 'ما هي الحوسبة السحابية',
    
    # General computing terms
    r'\bcomputing\b': 'حوسبة',
    r'\bresources\b': 'موارد',
    r'\binternet\b': 'الإنترنت',
    r'\bnetwork\b': 'شبكة',
    r'\bNetwork\b': 'شبكة',
    r'\bserver\b': 'خادم',
    r'\bservers\b': 'خوادم',
    r'\bstorage\b': 'تخزين',
    r'\bdatabase\b': 'قاعدة بيانات',
    r'\bdatabases\b': 'قواعد بيانات',
    r'\bnetworking\b': 'شبكات',
    r'\bsoftware\b': 'برمجيات',
    r'\bpricing\b': 'تسعير',
    
    # NIST characteristics
    r'On-Demand Self-Service': 'خدمة ذاتية حسب الطلب',
    r'Broad الشبكة Access': 'وصول واسع للشبكة',
    r'Resource Pooling': 'تجميع الموارد',
    r'Rapid Elasticity': 'مرونة سريعة',
    r'Measured Service': 'خدمة مقاسة',
    r'Available over network': 'متاح عبر الشبكة',
    r'Multi-tenant model': 'نموذج متعدد المستأجرين',
    r'dynamic assignment': 'تعيين ديناميكي',
    r'Scale outward and inward': 'توسع وتقلص بسرعة',
    r'Resource usage monitored': 'مراقبة استخدام الموارد',
    r'billed': 'الفواتير',
    
    # Deployment models
    r'Cloud Deployment Models': 'نماذج نشر الحوسبة السحابية',
    r'Public Cloud': 'الحوسبة السحابية العامة',
    r'Private Cloud': 'الحوسبة السحابية الخاصة',
    r'Hybrid Cloud': 'الحوسبة السحابية الهجينة',
    r'Multi-Cloud': 'حوسبة سحابية متعددة',
    r'Community Cloud': 'حوسبة سحابية مجتمعية',
    r'Owned by providers': 'مملوكة من قبل المزودين',
    r'shared infrastructure': 'بنية تحتية مشتركة',
    r'Dedicated to single organization': 'مخصصة لمنظمة واحدة',
    r'on-premises or hosted': 'محلية أو مستضافة',
    r'Combination من public و private clouds': 'مزيج من الحوسبة السحابية العامة والخاصة',
    r'Using multiple public cloud providers': 'استخدام مزودي حوسبة سحابية عامة متعددين',
    r'Shared by organizations مع common concerns': 'مشتركة بين منظمات ذات اهتمامات مشتركة',
    
    # Service models
    r'Service Models': 'نماذج الخدمة',
    r'Infrastructure as a Service': 'البنية التحتية كخدمة',
    r'Platform as a Service': 'المنصة كخدمة',
    r'Software as a Service': 'البرمجيات كخدمة',
    r'Function as a Service': 'الدالة كخدمة',
    r'Serverless': 'بدون خادم',
    r'Provides': 'يوفر',
    r'Virtual machines': 'آلات افتراضية',
    r'operating الأنظمة': 'أنظمة التشغيل',
    r'Examples': 'أمثلة',
    r'Use Cases': 'حالات الاستخدام',
    r'Lift-و-shift migrations': 'هجرات الرفع والنقل',
    r'tطوير environments': 'بيئات التطوير',
    r'high-control needs': 'احتياجات تحكم عالي',
    r'Development platforms': 'منصات التطوير',
    r'middleware': 'برمجيات وسيطة',
    r'Application التطوير': 'تطوير التطبيقات',
    r'API النشر': 'نشر واجهات البرمجة',
    r'microservices': 'خدمات مصغرة',
    r'Complete applications over internet': 'تطبيقات كاملة عبر الإنترنت',
    r'Email': 'البريد الإلكتروني',
    r'CRM': 'إدارة علاقات العملاء',
    r'collaboration': 'التعاون',
    r'business applications': 'تطبيقات الأعمال',
    r'Event-driven function execution': 'تنفيذ الدوال المدفوعة بالأحداث',
    r'Event processing': 'معالجة الأحداث',
    r'APIs': 'واجهات البرمجة',
    r'scheduled tasks': 'مهام مجدولة',
    r'real-time processing': 'معالجة في الوقت الفعلي',
}

def fix_arabic_text(content):
    """Apply translations to fix mixed Arabic-English text."""
    result = content
    
    # Apply translations in order (longer patterns first to avoid partial replacements)
    for pattern, replacement in sorted(TERM_TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        result = re.sub(pattern, replacement, result)
    
    # Fix specific known issues
    fixes = {
        'On-demand delivery من الحوسبة resources': 'تسليم حسب الطلب لموارد الحوسبة',
        'over ال internet مع pay-as-you-go pricing': 'عبر الإنترنت مع تسعير الدفع حسب الاستخدام',
        'متاح over الشبكة': 'متاح عبر الشبكة',
        'Scale outward و inward rapidly': 'توسع وتقلص بسرعة',
        'Resource usage monitored و billed': 'مراقبة استخدام الموارد وإصدار الفواتير',
        'Combination من public و private clouds': 'مزيج من الحوسبة السحابية العامة والخاصة',
        'Shared by organizations مع common concerns': 'مشتركة بين منظمات ذات اهتمامات مشتركة',
    }
    
    for old, new in fixes.items():
        result = result.replace(old, new)
    
    return result

def process_file(file_path):
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fixed_content = fix_arabic_text(content)
        
        if content != fixed_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    arabic_dir = Path('/workspace/knowledge_base/Arabic')
    processed = 0
    fixed = 0
    
    for md_file in arabic_dir.rglob('*.md'):
        processed += 1
        if process_file(md_file):
            fixed += 1
            print(f"Fixed: {md_file}")
    
    print(f"\nProcessed {processed} files, fixed {fixed} files")

if __name__ == '__main__':
    main()
