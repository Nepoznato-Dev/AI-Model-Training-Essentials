#!/usr/bin/env python3
"""
Comprehensive script to fix translation issues across all languages.
Focuses on pattern-based automated fixes for mixed-language content.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class TranslationFixer:
    def __init__(self):
        self.stats = {'processed': 0, 'fixed': 0, 'errors': 0}
        
    # Arabic fixes - most critical
    ARABIC_FIXES = {
        # Headers
        '# Cloud العمارة': '# عمارة الحوسبة السحابية',
        '## Cloud الحوسبة الأساسيات': '## أساسيات الحوسبة السحابية',
        '### What is Cloud الحوسبة؟': '### ما هي الحوسبة السحابية؟',
        
        # Common mixed phrases
        'On-demand delivery من الحوسبة resources': 'تسليم حسب الطلب لموارد الحوسبة',
        'over ال internet مع pay-as-you-go pricing': 'عبر الإنترنت مع تسعير الدفع حسب الاستخدام',
        'Broad الشبكة Access': 'الوصول الواسع للشبكة',
        'متاح over الشبكة': 'متاح عبر الشبكة',
        'Multi-tenant model مع dynamic assignment': 'نموذج متعدد المستأجرين مع التعيين الديناميكي',
        'Scale outward و inward rapidly': 'التوسع والتقلص بسرعة',
        'Resource usage monitored و billed': 'مراقبة استخدام الموارد وإصدار الفواتير',
        'Combination من public و private clouds': 'مزيج من الحوسبة السحابية العامة والخاصة',
        'Shared by organizations مع common concerns': 'مشتركة بين منظمات ذات اهتمامات مشتركة',
        
        # Technical terms
        'operating الأنظمة': 'أنظمة التشغيل',
        'Lift-و-shift migrations': 'هجرات الرفع والنقل',
        'التطوير environments': 'بيئات التطوير',
        'Application التطوير': 'تطوير التطبيقات',
        'API النشر': 'نشر واجهات البرمجة',
        'Complete applications over internet': 'تطبيقات كاملة عبر الإنترنت',
        'business applications': 'تطبيقات الأعمال',
        
        # Fix Arabic characters appearing in Spanish (critical error)
        'vendor lock-في': 'vendor lock-in',
    }
    
    # French fixes
    FRENCH_FIXES = {
        '# Cloud Architecture': '# Architecture Cloud',
        '## Cloud Informatique Fondamentaux': '## Fondamentaux du Cloud Computing',
        'On-demand delivery de Informatique resources': 'Livraison à la demande de ressources informatiques',
        'over le/la internet avec pay-as-you-go pricing': 'via Internet avec une tarification à l\'usage',
        'Broad Réseau Access': 'Accès réseau large',
        'Disponible over Réseau': 'Disponible via le réseau',
        'Protect Données dans transit et at rest': 'Protéger les données en transit et au repos',
    }
    
    # German fixes  
    GERMAN_FIXES = {
        '## Cloud Datenverarbeitung Grundlagen': '## Grundlagen der Cloud-Datenverarbeitung',
        'On-demand delivery von Datenverarbeitung resources': 'Bedarfsgerechte Bereitstellung von Rechenressourcen',
        'over der/die/das internet': 'über das Internet',
        'Multi-tenant model mit dynamic assignment': 'Mandantenfähiges Modell mit dynamischer Zuweisung',
        'Vollständig applications': 'Vollständige Anwendungen',
        'Fortgeschritten technologies': 'Fortgeschrittene Technologien',
    }
    
    # Spanish fixes
    SPANISH_FIXES = {
        '# Cloud Arquitectura': '# Arquitectura en la Nube',
        '## Cloud Informática Fundamentos': '## Fundamentos de la Computación en la Nube',
        'On-demand delivery de Informática resources': 'Entrega bajo demanda de recursos informáticos',
        'over el/la internet con pay-as-you-go pricing': 'a través de Internet con precios de pago por uso',
        'Lift-y-shift migrations': 'Migraciones de traslado directo',
        'vendor lock-في': 'vendor lock-in',  # Critical: Arabic character fix
    }
    
    # Japanese fixes
    JAPANESE_FIXES = {
        '# Cloud アーキテクチャ': '# クラウドアーキテクチャ',
        '## Cloud コンピューティング 基礎': '## クラウドコンピューティングの基礎',
        'On-demand delivery の コンピューティング resources': 'オンデマンドでのコンピューティングリソースの提供',
        'over その internet と pay-as-you-go pricing': 'インターネット経由で従量課金制',
        'Lift-と-shift migrations': 'リフトアンドシフト移行',
    }
    
    # Korean fixes
    KOREAN_FIXES = {
        '# Cloud 아키텍처': '# 클라우드 아키텍처',
        '## Cloud 컴퓨팅 기초': '## 클라우드 컴퓨팅 기초',
        'On-demand delivery 의 컴퓨팅 resources': '온디맨드 컴퓨팅 리소스 제공',
        'over 그 internet 와 함께 pay-as-you-go pricing': '인터넷을 통한 종량제 가격 책정',
        'Lift-와-shift migrations': '리프트앤시프트 마이그레이션',
    }
    
    # Thai fixes
    THAI_FIXES = {
        'ให้: กรอกใบสมัครผ่านอินเทอร์เน็ต': 'ให้บริการ: ผ่านอินเทอร์เน็ต',
    }
    
    # Vietnamese fixes
    VIETNAMESE_FIXES = {
        'Hoàn thiện hồ sơ qua internet': 'Cung cấp: Qua internet',
    }
    
    # Persian fixes
    PERSIAN_FIXES = {
        'جابجایی های بالابر و جابجایی': 'مهاجرت لیفت اند شیفت',
    }

    def apply_fixes(self, content: str, fixes: Dict[str, str]) -> str:
        """Apply a dictionary of fixes to content."""
        result = content
        # Apply longer patterns first to avoid partial replacements
        for old, new in sorted(fixes.items(), key=lambda x: -len(x[0])):
            result = result.replace(old, new)
        return result
    
    def fix_language(self, lang_dir: Path, fixes: Dict[str, str], lang_name: str) -> None:
        """Process all markdown files in a language directory."""
        if not lang_dir.exists():
            print(f"Directory not found: {lang_dir}")
            return
            
        for md_file in lang_dir.rglob('*.md'):
            self.stats['processed'] += 1
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                fixed_content = self.apply_fixes(content, fixes)
                
                if content != fixed_content:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    self.stats['fixed'] += 1
                    print(f"✓ Fixed: {md_file.relative_to(lang_dir.parent)}")
                    
            except Exception as e:
                self.stats['errors'] += 1
                print(f"✗ Error processing {md_file}: {e}")
    
    def run_all_fixes(self, base_dir: Path = Path('/workspace/knowledge_base')) -> None:
        """Run fixes for all critical languages."""
        print("=" * 60)
        print("STARTING AUTOMATED TRANSLATION FIXES")
        print("=" * 60)
        
        # Critical languages
        critical_fixes = [
            (base_dir / 'Arabic', self.ARABIC_FIXES, 'Arabic'),
            (base_dir / 'French', self.FRENCH_FIXES, 'French'),
            (base_dir / 'German', self.GERMAN_FIXES, 'German'),
            (base_dir / 'Spanish', self.SPANISH_FIXES, 'Spanish'),
            (base_dir / 'Japanese', self.JAPANESE_FIXES, 'Japanese'),
            (base_dir / 'Korean', self.KOREAN_FIXES, 'Korean'),
            (base_dir / 'Thai', self.THAI_FIXES, 'Thai'),
            (base_dir / 'Vietnamese', self.VIETNAMESE_FIXES, 'Vietnamese'),
            (base_dir / 'Persian', self.PERSIAN_FIXES, 'Persian'),
        ]
        
        for lang_dir, fixes, lang_name in critical_fixes:
            print(f"\n{'='*60}")
            print(f"Processing {lang_name}...")
            print('='*60)
            self.fix_language(lang_dir, fixes, lang_name)
        
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Files processed: {self.stats['processed']}")
        print(f"Files fixed: {self.stats['fixed']}")
        print(f"Errors: {self.stats['errors']}")
        print("=" * 60)

if __name__ == '__main__':
    fixer = TranslationFixer()
    fixer.run_all_fixes()
