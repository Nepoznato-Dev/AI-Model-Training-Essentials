#!/usr/bin/env python3
"""
Script to rename knowledge base folders to their proper native language names.
"""

import os
from pathlib import Path

# Mapping of folder numbers to proper names in each language
FOLDER_NAMES = {
    "German": {
        "01": "01_technologie_und_computing",
        "02": "02_künstliche_intelligenz",
        "03": "03_datenwissenschaft",
        "04": "04_wissenschaft",
        "05": "05_geschäft_und_finanzen",
        "06": "06_geisteswissenschaften",
        "07": "07_referenz",
        "08": "08_zukunft",
        "10": "10_spickzettel",
    },
    "French": {
        "01": "01_technologie_et_informatique",
        "02": "02_intelligence_artificielle",
        "03": "03_science_des_données",
        "04": "04_sciences",
        "05": "05_business_et_finance",
        "06": "06_sciences_humaines",
        "07": "07_référence",
        "08": "08_futur",
        "10": "10_cheat_sheets",
    },
    "Spanish": {
        "01": "01_tecnología_y_computación",
        "02": "02_inteligencia_artificial",
        "03": "03_ciencia_de_datos",
        "04": "04_ciencias",
        "05": "05_negocios_y_finanzas",
        "06": "06_humanidades",
        "07": "07_referencia",
        "08": "08_futuro",
        "10": "10_chuletas",
    },
    "Italian": {
        "01": "01_technologia_e_informatica",
        "02": "02_intelligenza_artificiale",
        "03": "03_scienza_dei_dati",
        "04": "04_scienze",
        "05": "05_affari_e_finanza",
        "06": "06_scienze_umane",
        "07": "07_riferimento",
        "08": "08_futuro",
        "10": "10_cheat_sheets",
    },
    "Indonesian": {
        "01": "01_teknologi_dan_komputer",
        "02": "02_kecerdasan_buatan",
        "03": "03_ilmu_data",
        "04": "04_ilmu_pengetahuan",
        "05": "05_bisnis_dan_keuangan",
        "06": "06_humaniora",
        "07": "07_referensi",
        "08": "08_masa_depan",
        "10": "10_cheat_sheets",
    },
    "Vietnamese": {
        "01": "01_cong_nghe_va_may_tinh",
        "02": "02_tri_tue_nhan_tao",
        "03": "03_khoa_hoc_du_lieu",
        "04": "04_khoa_hoc",
        "05": "05_kinh_doanh_va_tai_chinh",
        "06": "06_nhan_van",
        "07": "07_tai_lieu_tham_khao",
        "08": "08_tuong_lai",
        "10": "10_cheat_sheets",
    },
    "Thai": {
        "01": "01_เทคโนโลยีและคอมพิวเตอร์",
        "02": "02_ปัญญาประดิษฐ์",
        "03": "03_วิทยาศาสตร์ข้อมูล",
        "04": "04_วิทยาศาสตร์",
        "05": "05_ธุรกิจและการเงิน",
        "06": "06_มนุษยศาสตร์",
        "07": "07_อ้างอิง",
        "08": "08_อนาคต",
        "10": "10_ชีทโกง",
    },
    "Persian": {
        "01": "01_فناوری_و_رایانش",
        "02": "02_هوش_مصنوعی",
        "03": "03_علم_داده",
        "04": "04_علوم",
        "05": "05_کسب_و_کار_و_امور_مالی",
        "06": "06_علوم_انسانی",
        "07": "07_منابع",
        "08": "08_آینده",
        "10": "10_تقلب_برگه",
    },
    "Polish": {
        "01": "01_technologia_i_komputery",
        "02": "02_sztuczna_inteligencja",
        "03": "03_nauka_o_danych",
        "04": "04_nauka",
        "05": "05_biznes_i_finanse",
        "06": "06_nauki_humanistyczne",
        "07": "07_referencje",
        "08": "08_przyszłość",
        "10": "10_ściągawki",
    },
    "Portuguese": {
        "01": "01_tecnologia_e_computação",
        "02": "02_inteligência_artificial",
        "03": "03_ciência_de_dados",
        "04": "04_ciências",
        "05": "05_negócios_e_finanças",
        "06": "06_humanidades",
        "07": "07_referência",
        "08": "08_futuro",
        "10": "10_cheat_sheets",
    },
    "Russian": {
        "01": "01_технологии_и_вычисления",
        "02": "02_искусственный_интеллект",
        "03": "03_наука_о_данных",
        "04": "04_наука",
        "05": "05_бизнес_и_финансы",
        "06": "06_гуманитарные_науки",
        "07": "07_справочник",
        "08": "08_будущее",
        "10": "10_шпаргалки",
    },
    "Turkish": {
        "01": "01_teknoloji_ve_bilişim",
        "02": "02_yapay_zeka",
        "03": "03_veri_bilimi",
        "04": "04_bilim",
        "05": "05_iş_ve_finans",
        "06": "06_beşeri_bilimler",
        "07": "07_kaynakça",
        "08": "08_gelecek",
        "10": "10_kopya_kağıtları",
    },
    "Japanese": {
        "01": "01_テクノロジーとコンピューティング",
        "02": "02_人工知能",
        "03": "03_データサイエンス",
        "04": "04_科学",
        "05": "05_ビジネスと金融",
        "06": "06_人文科学",
        "07": "07_リファレンス",
        "08": "08_未来",
        "10": "10_カンニングペーパー",
    },
    "Korean": {
        "01": "01_기술과_컴퓨팅",
        "02": "02_인공 지능",
        "03": "03_데이터_과학",
        "04": "04_과학",
        "05": "05_비즈니스와_금융",
        "06": "06_인문학",
        "07": "07_참고_자료",
        "08": "08_미래",
        "10": "10_치트시트",
    },
    "Mandarin (Simplified Chinese)": {
        "01": "01_技术与计算",
        "02": "02_人工智能",
        "03": "03_数据科学",
        "04": "04_科学",
        "05": "05_商业与金融",
        "06": "06_人文学科",
        "07": "07_参考",
        "08": "08_未来",
        "10": "10_速查表",
    },
    "Mandarin (Traditional Chinese)": {
        "01": "01_技術與計算",
        "02": "02_人工智慧",
        "03": "03_數據科學",
        "04": "04_科學",
        "05": "05_商業與金融",
        "06": "06_人文學科",
        "07": "07_參考",
        "08": "08_未來",
        "10": "10_速查表",
    },
    "Arabic": {
        "01": "01_التكنولوجيا_والحوسبة",
        "02": "02_الذكاء_الاصطناعي",
        "03": "03_علم_البيانات",
        "04": "04_العلوم",
        "05": "05_الأعمال_والمالية",
        "06": "06_العلوم_الإنسانية",
        "07": "07_المراجع",
        "08": "08_المستقبل",
        "10": "10_أوراق_الغش",
    },
}

def rename_folders():
    kb_path = Path("/workspace/knowledge_base")
    
    for lang_name, folder_mapping in FOLDER_NAMES.items():
        lang_path = kb_path / lang_name
        if not lang_path.exists():
            print(f"Skipping {lang_name}: directory does not exist")
            continue
        
        print(f"\n=== Processing {lang_name} ===")
        
        # Get current folders
        current_folders = {f.name: f for f in lang_path.iterdir() if f.is_dir() and f.name.startswith(tuple([f"{i:02d}" for i in range(1, 11)]))}
        
        print(f"Current folders: {list(current_folders.keys())}")
        
        # Process each expected folder number
        for num, expected_name in folder_mapping.items():
            # Find the folder with this number prefix
            matching_folder = None
            for folder_name, folder_path in current_folders.items():
                if folder_name.startswith(f"{num}_"):
                    matching_folder = (folder_name, folder_path)
                    break
            
            if matching_folder is None:
                print(f"  {num}: No folder found with this prefix")
                continue
            
            current_name, current_path = matching_folder
            
            if current_name == expected_name:
                print(f"  {num}: ✓ Already correctly named: {current_name}")
            else:
                new_path = lang_path / expected_name
                print(f"  {num}: Renaming '{current_name}' -> '{expected_name}'")
                
                # Check if target already exists
                if new_path.exists():
                    print(f"    Warning: Target path already exists, skipping")
                else:
                    try:
                        current_path.rename(new_path)
                        print(f"    Success!")
                    except Exception as e:
                        print(f"    Error: {e}")

if __name__ == "__main__":
    rename_folders()
