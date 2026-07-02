#!/usr/bin/env python3
"""
Translation script for knowledge base files from English to multiple languages.
Uses a simple dictionary-based approach for common terms and structural translation.
"""

import re
from pathlib import Path

# Repository-local paths
BASE_DIR = Path(__file__).resolve().parent
ENGLISH_BASE = BASE_DIR / "knowledge_base" / "English"
KB_BASE = BASE_DIR / "knowledge_base"

# Target languages with their directory names
TARGET_LANGUAGES = {
    'Arabic': 'ar',
    'French': 'fr',
    'German': 'de',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Mandarin (Simplified Chinese)': 'zh-CN',
    'Mandarin (Traditional Chinese)': 'zh-TW',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Spanish': 'es',
    'Turkish': 'tr'
}

# Common technical terms that should remain in English or have standard translations
TECH_TERMS = {
    'API': {'fr': 'API', 'de': 'API', 'es': 'API', 'pt': 'API', 'ru': 'API', 'ja': 'API', 'ko': 'API', 'zh-CN': 'API', 'zh-TW': 'API', 'ar': 'API', 'tr': 'API'},
    'ML': {'fr': 'ML', 'de': 'ML', 'es': 'ML', 'pt': 'ML', 'ru': 'ML', 'ja': 'ML', 'ko': 'ML', 'zh-CN': '机器学习', 'zh-TW': '機器學習', 'ar': 'ML', 'tr': 'ML'},
    'AI': {'fr': 'IA', 'de': 'KI', 'es': 'IA', 'pt': 'IA', 'ru': 'ИИ', 'ja': 'AI', 'ko': 'AI', 'zh-CN': '人工智能', 'zh-TW': '人工智慧', 'ar': 'AI', 'tr': 'YZ'},
    'HTTP': {'fr': 'HTTP', 'de': 'HTTP', 'es': 'HTTP', 'pt': 'HTTP', 'ru': 'HTTP', 'ja': 'HTTP', 'ko': 'HTTP', 'zh-CN': 'HTTP', 'zh-TW': 'HTTP', 'ar': 'HTTP', 'tr': 'HTTP'},
    'SQL': {'fr': 'SQL', 'de': 'SQL', 'es': 'SQL', 'pt': 'SQL', 'ru': 'SQL', 'ja': 'SQL', 'ko': 'SQL', 'zh-CN': 'SQL', 'zh-TW': 'SQL', 'ar': 'SQL', 'tr': 'SQL'},
    'Git': {'fr': 'Git', 'de': 'Git', 'es': 'Git', 'pt': 'Git', 'ru': 'Git', 'ja': 'Git', 'ko': 'Git', 'zh-CN': 'Git', 'zh-TW': 'Git', 'ar': 'Git', 'tr': 'Git'},
    'Linux': {'fr': 'Linux', 'de': 'Linux', 'es': 'Linux', 'pt': 'Linux', 'ru': 'Linux', 'ja': 'Linux', 'ko': 'Linux', 'zh-CN': 'Linux', 'zh-TW': 'Linux', 'ar': 'Linux', 'tr': 'Linux'},
    'Python': {'fr': 'Python', 'de': 'Python', 'es': 'Python', 'pt': 'Python', 'ru': 'Python', 'ja': 'Python', 'ko': 'Python', 'zh-CN': 'Python', 'zh-TW': 'Python', 'ar': 'Python', 'tr': 'Python'},
    'JavaScript': {'fr': 'JavaScript', 'de': 'JavaScript', 'es': 'JavaScript', 'pt': 'JavaScript', 'ru': 'JavaScript', 'ja': 'JavaScript', 'ko': 'JavaScript', 'zh-CN': 'JavaScript', 'zh-TW': 'JavaScript', 'ar': 'JavaScript', 'tr': 'JavaScript'},
    'Cloud': {'fr': 'Cloud', 'de': 'Cloud', 'es': 'Nube', 'pt': 'Nuvem', 'ru': 'Облако', 'ja': 'クラウド', 'ko': '클라우드', 'zh-CN': '云', 'zh-TW': '雲', 'ar': 'سحابة', 'tr': 'Bulut'},
}

def get_language_name(lang_code):
    """Get full language name from code."""
    for name, code in TARGET_LANGUAGES.items():
        if code == lang_code:
            return name
    return lang_code

def translate_title(title, target_lang):
    """Translate markdown title preserving structure."""
    match = re.match(r'^(#{1,6})\s*(.*)$', title)
    if match:
        prefix, content = match.groups()
        translated_content = simple_translate(content, target_lang)
        return f"{prefix} {translated_content}".rstrip()
    return simple_translate(title, target_lang)

def simple_translate(text, target_lang):
    """
    Simple translation function using common patterns.
    For production use, integrate with proper translation APIs.
    """
    # This is a placeholder - in practice you'd use Google Translate API, DeepL, etc.
    # For now, we'll create translated versions with language markers
    
    lang_name = get_language_name(target_lang)
    
    # Common word translations (expanded dictionary)
    translations = {
        'the': {'fr': 'le/la', 'de': 'der/die/das', 'es': 'el/la', 'pt': 'o/a', 'ru': 'the', 'ja': 'その', 'ko': '그', 'zh-CN': '这', 'zh-TW': '這', 'ar': 'ال', 'tr': 'bu'},
        'and': {'fr': 'et', 'de': 'und', 'es': 'y', 'pt': 'e', 'ru': 'и', 'ja': 'と', 'ko': '와', 'zh-CN': '和', 'zh-TW': '和', 'ar': 'و', 'tr': 've'},
        'of': {'fr': 'de', 'de': 'von', 'es': 'de', 'pt': 'de', 'ru': 'из', 'ja': 'の', 'ko': '의', 'zh-CN': '的', 'zh-TW': '的', 'ar': 'من', 'tr': 'in'},
        'in': {'fr': 'dans', 'de': 'in', 'es': 'en', 'pt': 'em', 'ru': 'в', 'ja': 'で', 'ko': '에서', 'zh-CN': '在', 'zh-TW': '在', 'ar': 'في', 'tr': 'içinde'},
        'for': {'fr': 'pour', 'de': 'für', 'es': 'para', 'pt': 'para', 'ru': 'для', 'ja': 'のために', 'ko': '위한', 'zh-CN': '为', 'zh-TW': '為', 'ar': 'لأجل', 'tr': 'için'},
        'with': {'fr': 'avec', 'de': 'mit', 'es': 'con', 'pt': 'com', 'ru': 'с', 'ja': 'と', 'ko': '와 함께', 'zh-CN': '与', 'zh-TW': '與', 'ar': 'مع', 'tr': 'ile'},
        'Introduction': {'fr': 'Introduction', 'de': 'Einführung', 'es': 'Introducción', 'pt': 'Introdução', 'ru': 'Введение', 'ja': 'はじめに', 'ko': '소개', 'zh-CN': '介绍', 'zh-TW': '介紹', 'ar': 'مقدمة', 'tr': 'Giriş'},
        'Overview': {'fr': 'Aperçu', 'de': 'Übersicht', 'es': 'Descripción general', 'pt': 'Visão geral', 'ru': 'Обзор', 'ja': '概要', 'ko': '개요', 'zh-CN': '概述', 'zh-TW': '概述', 'ar': 'نظرة عامة', 'tr': 'Genel Bakış'},
        'Fundamentals': {'fr': 'Fondamentaux', 'de': 'Grundlagen', 'es': 'Fundamentos', 'pt': 'Fundamentos', 'ru': 'Основы', 'ja': '基礎', 'ko': '기초', 'zh-CN': '基础', 'zh-TW': '基礎', 'ar': 'الأساسيات', 'tr': 'Temeller'},
        'Advanced': {'fr': 'Avancé', 'de': 'Fortgeschritten', 'es': 'Avanzado', 'pt': 'Avançado', 'ru': 'Продвинутый', 'ja': '上級', 'ko': '고급', 'zh-CN': '高级', 'zh-TW': '高級', 'ar': 'متقدم', 'tr': 'İleri Düzey'},
        'Basics': {'fr': 'Bases', 'de': 'Grundlagen', 'es': 'Conceptos básicos', 'pt': 'Básico', 'ru': 'Основы', 'ja': '基本', 'ko': '기본', 'zh-CN': '基础', 'zh-TW': '基礎', 'ar': 'الأساسيات', 'tr': 'Temeller'},
        'Guide': {'fr': 'Guide', 'de': 'Leitfaden', 'es': 'Guía', 'pt': 'Guia', 'ru': 'Руководство', 'ja': 'ガイド', 'ko': '가이드', 'zh-CN': '指南', 'zh-TW': '指南', 'ar': 'دليل', 'tr': 'Rehber'},
        'Reference': {'fr': 'Référence', 'de': 'Referenz', 'es': 'Referencia', 'pt': 'Referência', 'ru': 'Справочник', 'ja': 'リファレンス', 'ko': '참조', 'zh-CN': '参考', 'zh-TW': '參考', 'ar': 'مرجع', 'tr': 'Referans'},
        'Examples': {'fr': 'Exemples', 'de': 'Beispiele', 'es': 'Ejemplos', 'pt': 'Exemplos', 'ru': 'Примеры', 'ja': '例', 'ko': '예시', 'zh-CN': '示例', 'zh-TW': '範例', 'ar': 'أمثلة', 'tr': 'Örnekler'},
        'Best Practices': {'fr': 'Meilleures pratiques', 'de': 'Best Practices', 'es': 'Mejores prácticas', 'pt': 'Melhores práticas', 'ru': 'Лучшие практики', 'ja': 'ベストプラクティス', 'ko': '모범 사례', 'zh-CN': '最佳实践', 'zh-TW': '最佳實踐', 'ar': 'أفضل الممارسات', 'tr': 'En İyi Uygulamalar'},
        'Security': {'fr': 'Sécurité', 'de': 'Sicherheit', 'es': 'Seguridad', 'pt': 'Segurança', 'ru': 'Безопасность', 'ja': 'セキュリティ', 'ko': '보안', 'zh-CN': '安全', 'zh-TW': '安全', 'ar': 'الأمان', 'tr': 'Güvenlik'},
        'Performance': {'fr': 'Performance', 'de': 'Leistung', 'es': 'Rendimiento', 'pt': 'Desempenho', 'ru': 'Производительность', 'ja': 'パフォーマンス', 'ko': '성능', 'zh-CN': '性能', 'zh-TW': '效能', 'ar': 'الأداء', 'tr': 'Performans'},
        'Architecture': {'fr': 'Architecture', 'de': 'Architektur', 'es': 'Arquitectura', 'pt': 'Arquitetura', 'ru': 'Архитектура', 'ja': 'アーキテクチャ', 'ko': '아키텍처', 'zh-CN': '架构', 'zh-TW': '架構', 'ar': 'العمارة', 'tr': 'Mimari'},
        'Development': {'fr': 'Développement', 'de': 'Entwicklung', 'es': 'Desarrollo', 'pt': 'Desenvolvimento', 'ru': 'Разработка', 'ja': '開発', 'ko': '개발', 'zh-CN': '开发', 'zh-TW': '開發', 'ar': 'التطوير', 'tr': 'Geliştirme'},
        'Testing': {'fr': 'Test', 'de': 'Testen', 'es': 'Pruebas', 'pt': 'Teste', 'ru': 'Тестирование', 'ja': 'テスト', 'ko': '테스트', 'zh-CN': '测试', 'zh-TW': '測試', 'ar': 'الاختبار', 'tr': 'Test Etme'},
        'Deployment': {'fr': 'Déploiement', 'de': 'Bereitstellung', 'es': 'Implementación', 'pt': 'Implantação', 'ru': 'Развертывание', 'ja': 'デプロイ', 'ko': '배포', 'zh-CN': '部署', 'zh-TW': '部署', 'ar': 'النشر', 'tr': 'Dağıtım'},
        'Management': {'fr': 'Gestion', 'de': 'Verwaltung', 'es': 'Gestión', 'pt': 'Gerenciamento', 'ru': 'Управление', 'ja': '管理', 'ko': '관리', 'zh-CN': '管理', 'zh-TW': '管理', 'ar': 'الإدارة', 'tr': 'Yönetim'},
        'Systems': {'fr': 'Systèmes', 'de': 'Systeme', 'es': 'Sistemas', 'pt': 'Sistemas', 'ru': 'Системы', 'ja': 'システム', 'ko': '시스템', 'zh-CN': '系统', 'zh-TW': '系統', 'ar': 'الأنظمة', 'tr': 'Sistemler'},
        'Technology': {'fr': 'Technologie', 'de': 'Technologie', 'es': 'Tecnología', 'pt': 'Tecnologia', 'ru': 'Технология', 'ja': 'テクノロジー', 'ko': '기술', 'zh-CN': '技术', 'zh-TW': '技術', 'ar': 'التكنولوجيا', 'tr': 'Teknoloji'},
        'Computing': {'fr': 'Informatique', 'de': 'Datenverarbeitung', 'es': 'Informática', 'pt': 'Computação', 'ru': 'Вычисления', 'ja': 'コンピューティング', 'ko': '컴퓨팅', 'zh-CN': '计算', 'zh-TW': '計算', 'ar': 'الحوسبة', 'tr': 'Bilişim'},
        'Data': {'fr': 'Données', 'de': 'Daten', 'es': 'Datos', 'pt': 'Dados', 'ru': 'Данные', 'ja': 'データ', 'ko': '데이터', 'zh-CN': '数据', 'zh-TW': '資料', 'ar': 'البيانات', 'tr': 'Veri'},
        'Science': {'fr': 'Science', 'de': 'Wissenschaft', 'es': 'Ciencia', 'pt': 'Ciência', 'ru': 'Наука', 'ja': '科学', 'ko': '과학', 'zh-CN': '科学', 'zh-TW': '科學', 'ar': 'العلوم', 'tr': 'Bilim'},
        'Business': {'fr': 'Entreprise', 'de': 'Geschäft', 'es': 'Negocios', 'pt': 'Negócios', 'ru': 'Бизнес', 'ja': 'ビジネス', 'ko': '비즈니스', 'zh-CN': '商业', 'zh-TW': '商業', 'ar': 'الأعمال', 'tr': 'İş'},
        'Finance': {'fr': 'Finance', 'de': 'Finanzen', 'es': 'Finanzas', 'pt': 'Finanças', 'ru': 'Финансы', 'ja': '金融', 'ko': '금융', 'zh-CN': '金融', 'zh-TW': '金融', 'ar': 'المالية', 'tr': 'Finans'},
        'Investing': {'fr': 'Investissement', 'de': 'Investieren', 'es': 'Inversión', 'pt': 'Investimento', 'ru': 'Инвестирование', 'ja': '投資', 'ko': '투자', 'zh-CN': '投资', 'zh-TW': '投資', 'ar': 'الاستثمار', 'tr': 'Yatırım'},
        'Law': {'fr': 'Droit', 'de': 'Recht', 'es': 'Derecho', 'pt': 'Direito', 'ru': 'Закон', 'ja': '法律', 'ko': '법률', 'zh-CN': '法律', 'zh-TW': '法律', 'ar': 'القانون', 'tr': 'Hukuk'},
        'Legal': {'fr': 'Juridique', 'de': 'Rechtlich', 'es': 'Legal', 'pt': 'Jurídico', 'ru': 'Юридический', 'ja': '法的', 'ko': '법적', 'zh-CN': '法律', 'zh-TW': '法律', 'ar': 'قانوني', 'tr': 'Yasal'},
        'History': {'fr': 'Histoire', 'de': 'Geschichte', 'es': 'Historia', 'pt': 'História', 'ru': 'История', 'ja': '歴史', 'ko': '역사', 'zh-CN': '历史', 'zh-TW': '歷史', 'ar': 'التاريخ', 'tr': 'Tarih'},
        'Culture': {'fr': 'Culture', 'de': 'Kultur', 'es': 'Cultura', 'pt': 'Cultura', 'ru': 'Культура', 'ja': '文化', 'ko': '문화', 'zh-CN': '文化', 'zh-TW': '文化', 'ar': 'الثقافة', 'tr': 'Kültür'},
        'Geography': {'fr': 'Géographie', 'de': 'Geographie', 'es': 'Geografía', 'pt': 'Geografia', 'ru': 'География', 'ja': '地理', 'ko': '지리', 'zh-CN': '地理', 'zh-TW': '地理', 'ar': 'الجغرافيا', 'tr': 'Coğrafya'},
        'Arts': {'fr': 'Arts', 'de': 'Künste', 'es': 'Artes', 'pt': 'Artes', 'ru': 'Искусства', 'ja': '芸術', 'ko': '예술', 'zh-CN': '艺术', 'zh-TW': '藝術', 'ar': 'الفنون', 'tr': 'Sanat'},
        'Literature': {'fr': 'Littérature', 'de': 'Literatur', 'es': 'Literatura', 'pt': 'Literatura', 'ru': 'Литература', 'ja': '文学', 'ko': '문학', 'zh-CN': '文学', 'zh-TW': '文學', 'ar': 'الأدب', 'tr': 'Edebiyat'},
        'Psychology': {'fr': 'Psychologie', 'de': 'Psychologie', 'es': 'Psicología', 'pt': 'Psicologia', 'ru': 'Психология', 'ja': '心理学', 'ko': '심리학', 'zh-CN': '心理学', 'zh-TW': '心理學', 'ar': 'علم النفس', 'tr': 'Psikoloji'},
        'Language': {'fr': 'Langue', 'de': 'Sprache', 'es': 'Idioma', 'pt': 'Idioma', 'ru': 'Язык', 'ja': '言語', 'ko': '언어', 'zh-CN': '语言', 'zh-TW': '語言', 'ar': 'اللغة', 'tr': 'Dil'},
        'English': {'fr': 'Anglais', 'de': 'Englisch', 'es': 'Inglés', 'pt': 'Inglês', 'ru': 'Английский', 'ja': '英語', 'ko': '영어', 'zh-CN': '英语', 'zh-TW': '英語', 'ar': 'الإنجليزية', 'tr': 'İngilizce'},
        'Dictionary': {'fr': 'Dictionnaire', 'de': 'Wörterbuch', 'es': 'Diccionario', 'pt': 'Dicionário', 'ru': 'Словарь', 'ja': '辞書', 'ko': '사전', 'zh-CN': '词典', 'zh-TW': '詞典', 'ar': 'القاموس', 'tr': 'Sözlük'},
        'General Knowledge': {'fr': 'Connaissances générales', 'de': 'Allgemeinwissen', 'es': 'Conocimientos generales', 'pt': 'Conhecimento geral', 'ru': 'Общие знания', 'ja': '一般知識', 'ko': '일반 상식', 'zh-CN': '常识', 'zh-TW': '常識', 'ar': 'المعرفة العامة', 'tr': 'Genel Kültür'},
        'Communication': {'fr': 'Communication', 'de': 'Kommunikation', 'es': 'Comunicación', 'pt': 'Comunicação', 'ru': 'Коммуникация', 'ja': 'コミュニケーション', 'ko': '의사소통', 'zh-CN': '沟通', 'zh-TW': '溝通', 'ar': 'التواصل', 'tr': 'İletişim'},
        'Safe': {'fr': 'Sûr', 'de': 'Sicher', 'es': 'Seguro', 'pt': 'Seguro', 'ru': 'Безопасный', 'ja': '安全な', 'ko': '안전한', 'zh-CN': '安全', 'zh-TW': '安全', 'ar': 'آمن', 'tr': 'Güvenli'},
        'Future': {'fr': 'Futur', 'de': 'Zukunft', 'es': 'Futuro', 'pt': 'Futuro', 'ru': 'Будущее', 'ja': '未来', 'ko': '미래', 'zh-CN': '未来', 'zh-TW': '未來', 'ar': 'المستقبل', 'tr': 'Gelecek'},
        'Events': {'fr': 'Événements', 'de': 'Ereignisse', 'es': 'Eventos', 'pt': 'Eventos', 'ru': 'События', 'ja': 'イベント', 'ko': '이벤트', 'zh-CN': '事件', 'zh-TW': '事件', 'ar': 'الأحداث', 'tr': 'Olaylar'},
        'Cheat Sheets': {'fr': 'Aide-mémoire', 'de': 'Spickzettel', 'es': 'Chuletas', 'pt': 'Colas', 'ru': 'Шпаргалки', 'ja': 'チートシート', 'ko': '치트 시트', 'zh-CN': '速查表', 'zh-TW': '速查表', 'ar': 'أوراق الغش', 'tr': 'Kopya Kağıtları'},
        'Commands': {'fr': 'Commandes', 'de': 'Befehle', 'es': 'Comandos', 'pt': 'Comandos', 'ru': 'Команды', 'ja': 'コマンド', 'ko': '명령', 'zh-CN': '命令', 'zh-TW': '命令', 'ar': 'الأوامر', 'tr': 'Komutlar'},
        'Syntax': {'fr': 'Syntaxe', 'de': 'Syntax', 'es': 'Sintaxis', 'pt': 'Sintaxe', 'ru': 'Синтаксис', 'ja': '構文', 'ko': '구문', 'zh-CN': '语法', 'zh-TW': '語法', 'ar': 'بناء الجملة', 'tr': 'Sözdizimi'},
        'Quick Reference': {'fr': 'Référence rapide', 'de': 'Schnellreferenz', 'es': 'Referencia rápida', 'pt': 'Referência rápida', 'ru': 'Быстрый справочник', 'ja': 'クイックリファレンス', 'ko': '빠른 참조', 'zh-CN': '快速参考', 'zh-TW': '快速參考', 'ar': 'مرجع سريع', 'tr': 'Hızlı Referans'},
        'Machine Learning': {'fr': 'Apprentissage automatique', 'de': 'Maschinelles Lernen', 'es': 'Aprendizaje automático', 'pt': 'Aprendizado de máquina', 'ru': 'Машинное обучение', 'ja': '機械学習', 'ko': '기계 학습', 'zh-CN': '机器学习', 'zh-TW': '機器學習', 'ar': 'التعلم الآلي', 'tr': 'Makine Öğrenimi'},
        'Deep Learning': {'fr': 'Apprentissage profond', 'de': 'Tiefes Lernen', 'es': 'Aprendizaje profundo', 'pt': 'Aprendizado profundo', 'ru': 'Глубокое обучение', 'ja': '深層学習', 'ko': '딥 러닝', 'zh-CN': '深度学习', 'zh-TW': '深度學習', 'ar': 'التعلم العميق', 'tr': 'Derin Öğrenme'},
        'Neural Networks': {'fr': 'Réseaux de neurones', 'de': 'Neuronale Netze', 'es': 'Redes neuronales', 'pt': 'Redes neurais', 'ru': 'Нейронные сети', 'ja': 'ニューラルネットワーク', 'ko': '신경망', 'zh-CN': '神经网络', 'zh-TW': '神經網絡', 'ar': 'الشبكات العصبية', 'tr': 'Sinir Ağları'},
        'Database': {'fr': 'Base de données', 'de': 'Datenbank', 'es': 'Base de datos', 'pt': 'Banco de dados', 'ru': 'База данных', 'ja': 'データベース', 'ko': '데이터베이스', 'zh-CN': '数据库', 'zh-TW': '資料庫', 'ar': 'قاعدة البيانات', 'tr': 'Veritabanı'},
        'Web': {'fr': 'Web', 'de': 'Web', 'es': 'Web', 'pt': 'Web', 'ru': 'Веб', 'ja': 'ウェブ', 'ko': '웹', 'zh-CN': '网络', 'zh-TW': '網路', 'ar': 'الويب', 'tr': 'Web'},
        'Network': {'fr': 'Réseau', 'de': 'Netzwerk', 'es': 'Red', 'pt': 'Rede', 'ru': 'Сеть', 'ja': 'ネットワーク', 'ko': '네트워크', 'zh-CN': '网络', 'zh-TW': '網路', 'ar': 'الشبكة', 'tr': 'Ağ'},
        'Environmental': {'fr': 'Environnemental', 'de': 'Umwelt', 'es': 'Ambiental', 'pt': 'Ambiental', 'ru': 'Экологический', 'ja': '環境', 'ko': '환경', 'zh-CN': '环境', 'zh-TW': '環境', 'ar': 'بيئي', 'tr': 'Çevresel'},
        'Sustainability': {'fr': 'Durabilité', 'de': 'Nachhaltigkeit', 'es': 'Sostenibilidad', 'pt': 'Sustentabilidade', 'ru': 'Устойчивость', 'ja': '持続可能性', 'ko': '지속 가능성', 'zh-CN': '可持续性', 'zh-TW': '永續性', 'ar': 'الاستدامة', 'tr': 'Sürdürülebilirlik'},
        'Food': {'fr': 'Alimentation', 'de': 'Essen', 'es': 'Comida', 'pt': 'Comida', 'ru': 'Еда', 'ja': '食べ物', 'ko': '음식', 'zh-CN': '食物', 'zh-TW': '食物', 'ar': 'طعام', 'tr': 'Yiyecek'},
        'Agriculture': {'fr': 'Agriculture', 'de': 'Landwirtschaft', 'es': 'Agricultura', 'pt': 'Agricultura', 'ru': 'Сельское хозяйство', 'ja': '農業', 'ko': '농업', 'zh-CN': '农业', 'zh-TW': '農業', 'ar': 'الزراعة', 'tr': 'Tarım'},
        'Nutrition': {'fr': 'Nutrition', 'de': 'Ernährung', 'es': 'Nutrición', 'pt': 'Nutrição', 'ru': 'Питание', 'ja': '栄養', 'ko': '영양', 'zh-CN': '营养', 'zh-TW': '營養', 'ar': 'التغذية', 'tr': 'Beslenme'},
        'Medicine': {'fr': 'Médecine', 'de': 'Medizin', 'es': 'Medicina', 'pt': 'Medicina', 'ru': 'Медицина', 'ja': '医学', 'ko': '의학', 'zh-CN': '医学', 'zh-TW': '醫學', 'ar': 'الطب', 'tr': 'Tıp'},
        'Healthcare': {'fr': 'Soins de santé', 'de': 'Gesundheitswesen', 'es': 'Atención médica', 'pt': 'Saúde', 'ru': 'Здравоохранение', 'ja': '医療', 'ko': '의료', 'zh-CN': '医疗', 'zh-TW': '醫療', 'ar': 'الرعاية الصحية', 'tr': 'Sağlık Hizmetleri'},
        'Nature': {'fr': 'Nature', 'de': 'Natur', 'es': 'Naturaleza', 'pt': 'Natureza', 'ru': 'Природа', 'ja': '自然', 'ko': '자연', 'zh-CN': '自然', 'zh-TW': '自然', 'ar': 'الطبيعة', 'tr': 'Doğa'},
        'Economics': {'fr': 'Économie', 'de': 'Wirtschaft', 'es': 'Economía', 'pt': 'Economia', 'ru': 'Экономика', 'ja': '経済', 'ko': '경제', 'zh-CN': '经济', 'zh-TW': '經濟', 'ar': 'الاقتصاد', 'tr': 'Ekonomi'},
        'Geopolitics': {'fr': 'Géopolitique', 'de': 'Geopolitik', 'es': 'Geopolítica', 'pt': 'Geopolítica', 'ru': 'Геополитика', 'ja': '地政学', 'ko': '지정학', 'zh-CN': '地缘政治', 'zh-TW': '地緣政治', 'ar': 'الجيوسياسية', 'tr': 'Jeopolitik'},
        'Human Behavior': {'fr': 'Comportement humain', 'de': 'Menschliches Verhalten', 'es': 'Comportamiento humano', 'pt': 'Comportamento humano', 'ru': 'Человеческое поведение', 'ja': '人間の行動', 'ko': '인간 행동', 'zh-CN': '人类行为', 'zh-TW': '人類行為', 'ar': 'السلوك البشري', 'tr': 'İnsan Davranışı'},
        'Knowledge Base': {'fr': 'Base de connaissances', 'de': 'Wissensdatenbank', 'es': 'Base de conocimientos', 'pt': 'Base de conhecimento', 'ru': 'База знаний', 'ja': 'ナレッジベース', 'ko': '지식 기반', 'zh-CN': '知识库', 'zh-TW': '知識庫', 'ar': 'قاعدة المعرفة', 'tr': 'Bilgi Tabanı'},
        'Critique': {'fr': 'Critique', 'de': 'Kritik', 'es': 'Crítica', 'pt': 'Crítica', 'ru': 'Критика', 'ja': '批判', 'ko': '비판', 'zh-CN': '批评', 'zh-TW': '批評', 'ar': 'نقد', 'tr': 'Eleştiri'},
        'Improvements': {'fr': 'Améliorations', 'de': 'Verbesserungen', 'es': 'Mejoras', 'pt': 'Melhorias', 'ru': 'Улучшения', 'ja': '改善', 'ko': '개선', 'zh-CN': '改进', 'zh-TW': '改進', 'ar': 'تحسينات', 'tr': 'İyileştirmeler'},
        'Table of Contents': {'fr': 'Table des matières', 'de': 'Inhaltsverzeichnis', 'es': 'Tabla de contenidos', 'pt': 'Tabela de conteúdos', 'ru': 'Содержание', 'ja': '目次', 'ko': '목차', 'zh-CN': '目录', 'zh-TW': '目錄', 'ar': 'جدول المحتويات', 'tr': 'İçindekiler'},
        'Learning Paths': {'fr': 'Parcours d\'apprentissage', 'de': 'Lernpfade', 'es': 'Rutas de aprendizaje', 'pt': 'Caminhos de aprendizado', 'ru': 'Пути обучения', 'ja': '学習パス', 'ko': '학습 경로', 'zh-CN': '学习路径', 'zh-TW': '學習路徑', 'ar': 'مسارات التعلم', 'tr': 'Öğrenme Yolları'},
        'Statistics': {'fr': 'Statistiques', 'de': 'Statistiken', 'es': 'Estadísticas', 'pt': 'Estatísticas', 'ru': 'Статистика', 'ja': '統計', 'ko': '통계', 'zh-CN': '统计', 'zh-TW': '統計', 'ar': 'إحصائيات', 'tr': 'İstatistikler'},
        'Disclaimers': {'fr': 'Avertissements', 'de': 'Haftungsausschlüsse', 'es': 'Descargos de responsabilidad', 'pt': 'Avisos legais', 'ru': 'Отказ от ответственности', 'ja': '免責事項', 'ko': '면책 조항', 'zh-CN': '免责声明', 'zh-TW': '免責聲明', 'ar': 'إخلاء المسؤولية', 'tr': 'Sorumluluk Reddi'},
        'Contributing': {'fr': 'Contribuer', 'de': 'Beitragen', 'es': 'Contribuir', 'pt': 'Contribuir', 'ru': 'Вклад', 'ja': '貢献', 'ko': '기여', 'zh-CN': '贡献', 'zh-TW': '貢獻', 'ar': 'المساهمة', 'tr': 'Katkıda Bulunma'},
    }
    
    result = text
    
    # Apply translations for known words/phrases using whole-word matching
    # to avoid corrupting unrelated words (for example, "in" inside
    # "computing").
    for english, translations_dict in sorted(translations.items(), key=lambda item: len(item[0]), reverse=True):
        translated = translations_dict.get(target_lang)
        if not translated:
            continue
        pattern = re.compile(rf"(?<!\w){re.escape(english)}(?!\w)", re.IGNORECASE)
        result = pattern.sub(translated, result)
    
    return result

def translate_content(content, target_lang, filename):
    """Translate markdown content while preserving structure."""
    lines = content.split('\n')
    translated_lines = []
    
    in_code_block = False
    code_block_fence = None
    
    for line in lines:
        # Check for code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_fence = line.strip()
            else:
                in_code_block = False
                code_block_fence = None
            translated_lines.append(line)
            continue
        
        # Skip code blocks and YAML frontmatter
        if in_code_block or line.strip().startswith('---'):
            translated_lines.append(line)
            continue
        
        # Skip lines that are mostly code or URLs
        if line.strip().startswith('http') or line.strip().startswith('mailto'):
            translated_lines.append(line)
            continue
        
        # Translate titles
        if line.strip().startswith('#'):
            translated_lines.append(translate_title(line, target_lang))
            continue
        
        # Translate list items (but preserve formatting)
        if line.strip().startswith('-') or line.strip().startswith('*') or line.strip().startswith('1.'):
            # Extract the content after the list marker
            stripped = line.lstrip()
            marker_end = 0
            if stripped.startswith('-') or stripped.startswith('*'):
                marker_end = 1
            elif stripped[0].isdigit():
                # Find the dot and space
                for i, char in enumerate(stripped):
                    if char == '.':
                        marker_end = i + 2  # Include the space after the number
                        break
            
            if marker_end > 0:
                prefix = line[:len(line) - len(stripped) + marker_end]
                content_part = stripped[marker_end:]
                translated_content = simple_translate(content_part, target_lang)
                translated_lines.append(f"{prefix}{translated_content}")
            else:
                translated_lines.append(simple_translate(line, target_lang))
            continue
        
        # Regular text translation
        translated_lines.append(simple_translate(line, target_lang))
    
    return '\n'.join(translated_lines)

def add_translation_header(content, target_lang, source_file):
    """Add a header indicating this is a translation."""
    lang_name = get_language_name(target_lang)
    header = f"""<!-- 
This file was automatically translated from English to {lang_name}.
Source: {source_file}
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

"""
    return header + content

def copy_directory_structure(source_dir, target_dir):
    """Copy the directory structure from source to target."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Create subdirectories
    for subdir in source_path.iterdir():
        if subdir.is_dir():
            dest = target_path / subdir.name
            dest.mkdir(parents=True, exist_ok=True)
            print(f"  Created directory: {dest}")

ENGLISH_CATEGORY_DIRS = {
    "01_technology_and_computing",
    "02_artificial_intelligence",
    "03_data_science",
    "04_science",
    "05_business_and_finance",
    "06_humanities",
    "07_reference",
    "08_future",
    "10_cheat_sheets",
}

def target_markdown_files(root_dir):
    """Return the markdown files for a language, preferring localized folders."""
    files = []
    root_dir = Path(root_dir)

    readme = root_dir / "README.md"
    if readme.exists():
        files.append(readme)

    subdirs = [path for path in root_dir.iterdir() if path.is_dir()]
    localized_subdirs = [path for path in subdirs if path.name not in ENGLISH_CATEGORY_DIRS]
    selected_subdirs = localized_subdirs if localized_subdirs else [path for path in subdirs if path.name in ENGLISH_CATEGORY_DIRS]

    for subdir in sorted(selected_subdirs, key=lambda path: path.name):
        files.extend(sorted(subdir.rglob("*.md"), key=lambda path: path.relative_to(root_dir).as_posix()))

    return sorted(files, key=lambda path: path.relative_to(root_dir).as_posix())

def translate_file(source_file, target_file, target_lang):
    """Translate a single file and save to target directory."""
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    target_file.parent.mkdir(parents=True, exist_ok=True)
    translated_content = translate_content(content, target_lang, source_file.name)
    translated_content = add_translation_header(translated_content, target_lang, source_file.name)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(translated_content)

    return target_file

def main():
    """Main translation function."""
    # Get all markdown files
    md_files = sorted(ENGLISH_BASE.rglob("*.md"), key=lambda path: path.relative_to(ENGLISH_BASE).as_posix())
    print(f"Found {len(md_files)} markdown files to translate")
    print(f"Target languages: {', '.join(TARGET_LANGUAGES.keys())}")
    print(f"Total translations needed: {len(md_files) * len(TARGET_LANGUAGES)}\n")
    
    total_translations = 0
    successful = 0
    failed = 0
    
    for lang_name, lang_code in TARGET_LANGUAGES.items():
        target_dir = KB_BASE / lang_name
        print(f"\n{'='*60}")
        print(f"Translating to {lang_name} ({lang_code})")
        print(f"{'='*60}")

        target_dir.mkdir(exist_ok=True)

        target_files = target_markdown_files(target_dir)
        if len(target_files) != len(md_files):
            print(f"  Skipping {lang_name}: expected {len(md_files)} files, found {len(target_files)} tracked markdown files")
            failed += len(md_files)
            continue

        lang_successful = 0
        for source_file, target_file in zip(md_files, target_files):
            try:
                target_path = translate_file(source_file, target_file, lang_code)
                print(f"  ✓ {source_file.relative_to(ENGLISH_BASE)} -> {target_path.relative_to(KB_BASE)}")
                lang_successful += 1
                successful += 1
            except Exception as e:
                print(f"  ✗ Error translating {source_file}: {e}")
                failed += 1
        
        total_translations += len(md_files)
        print(f"\n{lang_name}: {lang_successful}/{len(md_files)} files translated successfully")
    
    print(f"\n{'='*60}")
    print(f"Translation Summary")
    print(f"{'='*60}")
    print(f"Total files processed: {total_translations}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(successful/total_translations*100):.1f}%")

if __name__ == '__main__':
    main()
