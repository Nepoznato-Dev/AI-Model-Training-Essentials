---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teknoloji Sözlüğü
Yapay zeka modellerini, donanımı, karşılaştırmaları ve temel kavramları kapsayan bir referans sözlüğü
modern yapay zeka ve bilgi işlem ortamında.
---

## Yapay Zeka Dil Modelleri ve Yardımcıları
### SohbetGPT
ChatGPT, OpenAI tarafından geliştirilen ve ilk olarak Kasım 2022'de piyasaya sürülen bir yapay zeka sohbet robotudur.
GPT serisi büyük dil modelleri (LLM'ler) tarafından desteklenmektedir. ChatGPT bunlardan biridir
100 milyona ulaşan, tarihteki en hızlı büyüyen tüketici yapay zeka ürünlerinden biri
kullanıcılar lansmandan sonraki iki ay içinde. Metin tabanlı konuşmayı, kodu destekler
oluşturma, özetleme ve yaratıcı yazma. Ücretli katmanlar şunlara erişim sağlar:
GPT-4 ve GPT-4o gibi daha güçlü modeller.
### GPT (Üretken Önceden Eğitimli Transformatör)
GPT, OpenAI tarafından oluşturulan büyük dil modelleri ailesidir. Mimarlık
sonraki belirteç tahmin hedefiyle eğitilmiş, yalnızca kod çözücüye yönelik bir Transformer kullanır
büyük metin topluluğu. Anahtar sürümler arasında GPT-2 (2019, 1,5B parametreler, dikkate değer) bulunur
"yayınlanması çok tehlikeli" tanıtım için), GPT-3 (2020, 175B parametreleri, yaygın olarak
API aracılığıyla kullanılır), GPT-3.5 (orijinal ChatGPT'nin omurgası) ve GPT-4
(2023, çok modlu, birçok kıyaslamada insan uzman düzeyine yakın performans).
### Claude
Claude, Anthropic tarafından geliştirilen bir yapay zeka asistanıdır. Adını Claude'dan alıyor
Bilgi teorisinin kurucusu Shannon. Antropik eski tarafından kuruldu
OpenAI araştırmacıları ve "anayasal yapay zeka"ya odaklanıyor;
modelleri bir dizi ilkeyi takip edecek şekilde eğiterek daha güvenli hale getirin. Claude modelleri
(Claude 1, 2, 3 Haiku / Sonnet / Opus) uzun bağlam pencereleriyle tanınır (yukarı
200.000 jetona kadar), incelikli akıl yürütme ve zararlı çıktının azaltılması
temel LLM'ler.
### İkizler
Gemini, Google DeepMind'ın çok modlu yapay zeka modelleri ailesidir.
Aralık 2023. Gemini doğası gereği çok modludur; sıfırdan eğitilmiştir
Daha önceki modellerin aksine, aynı anda metin, resim, ses ve video
ince ayar yoluyla eklenen yöntemler. Sürümler Gemini Nano'yu (cihazda) içerir.
Gemini Flash (hızlı, uygun maliyetli) ve Gemini Ultra (en yüksek yetenek).
Gemini, Google'ın yapay zeka sohbet robotu Bard'a (Gemini olarak yeniden adlandırıldı) ve Google Arama Yapay Zekasına güç veriyor
Genel bakış.
### Phi-3-mini
Phi-3-mini, Microsoft tarafından 3.8B ile geliştirilen küçük bir dil modelidir (SLM).
parametreler. Nisan 2024'da piyasaya sürüldü. Çoğu büyük modelin aksine Phi-3-mini
dikkatle seçilmiş "ders kitabı kalitesinde" bir veri seti üzerinde eğitildi - bir teknik
Microsoft Research'ün öncülük ettiği, ham hacim yerine veri kalitesine öncelik veren bir teknoloji.
GPT-4 veya Claude 3 Opus'tan çok daha küçük olmasına rağmen, Phi-3-mini maçlar veya
MMLU gibi muhakeme kriterlerinde birkaç kat daha büyük modellerden daha iyi performans gösterir ve
İnsan Değerlendirmesi. Temel varyantında 4k token bağlam penceresini ve 128k token bağlam penceresini destekler
uzun bağlam varyantındaki pencere. Phi-3-mini tek bir tüketici GPU'sunda çalışabilir
hatta yeterli RAM'e sahip modern bir akıllı telefondaki cihazda bile.
### Lama (Meta AI)
Llama (Büyük Dil Modeli Meta AI), açık ağırlıklı bir model ailesidir
Meta tarafından yayınlandı. Llama 2 (2023) araştırma ve ticari kullanım için piyasaya sürüldü
7B ila 70B parametreleri arasında değişen boyutlarda. Lama 3 (2024) iyileştirildi
8B'den 70B'ye (ve daha sonra 400B+) kadar değişen modellerle performansı önemli ölçüde artırdı.
Ağırlıklar herkese açık olarak indirilebildiğinden, Lama modelleri temeldir
ince ayarlı değişkenlerden oluşan geniş bir ekosistem için (Mistral, Alpaca, Vicuna, vb.)
ve yerel/özel AI dağıtımları için yaygın olarak kullanılır.
### Mistral
Mistral AI, açık ve tescilli LLM'ler geliştiren bir Fransız yapay zeka şirketidir.
Mistral 7B (2023), 7B parametreli bir modelin aşağıdakilerle eşleşebileceğini gösterdi
kaydırma gibi etkili teknikler kullanılarak çok daha büyük modellerin performansı
pencere dikkati ve gruplandırılmış sorgu dikkati. Mixtral 8x7B (2023) bir karışımdır.
uzman modeli - her jetonu 8 uzman ağdan oluşan bir alt kümeye yönlendirir,
hesaplama açısından daha ucuzken GPT-3.5 düzeyinde performans elde etmek.
Mistral'ın modelleri tamamen açık ağırlıklıdır ve yerel olarak çalıştırılabilir.
---

## GPU Donanımı ve Grafik Kartları
### GPU (Grafik İşleme Birimi)
GPU, büyük ölçüde paralel hesaplama için tasarlanmış bir işlemcidir. Başlangıçta
3D grafiklerin işlenmesi için tasarlanan GPU'lar, AI/ML eğitimi için vazgeçilmez hale geldi
ve çıkarım çünkü binlerce kayan nokta işlemi gerçekleştirebilirler
binlerce küçük çekirdeği aynı anda kullanıyor. İki ana GPU üreticisi
AI için NVIDIA ve AMD'dir.
### NVIDIA GeForce RTX Serisi
RTX (Ray Tracing Texel eXtreme) serisi, NVIDIA'nın tüketici GPU serisidir. RTX
30xx (Ampere, 2020) ve RTX 40xx (Ada Lovelace, 2022) nesilleri şunları içerir:
Yapay zeka operasyonlarını hızlandırmak için özel Tensör Çekirdekleri. VRAM (video RAM)
AI modellerini yerel olarak çalıştırmak için kritik öneme sahiptir; 8 GB'lik bir GPU, 7B parametresini işleyebilir
4 bitlik nicemlemeli modeller; 24 GB'lık bir GPU, 4 bitlik 70B modellerini işleyebilir.
### NVIDIA A-Serisi ve H-Serisi (Veri Merkezi)
A100 (Ampere, 2020) ve H100 (Hopper, 2022), NVIDIA'nın profesyonel yapay zekasıdır
hızlandırıcılar. H100, 80 GB'a kadar HBM3 belleğe sahiptir ve standarttır
Günümüzdeki çoğu büyük ölçekli LLM eğitiminin arkasında donanım bulunmaktadır. Bu GPU'ların maliyeti 25.000 dolardır.
Her biri 40.000 ABD doları ancak tüketici RTX kartlarının 10-30 katı AI verimi sunuyor.
### AMD Radeon RX Serisi
AMD'nin tüketici GPU serisi. RX 7900 XTX (2022) 24 GB VRAM'e sahiptir ve çalışabilir
ROCm (AMD'nin GPU hesaplama yığını) aracılığıyla yerel LLM'ler. AMD GPU'lar genellikle daha azdır
AI çerçeveleri için NVIDIA'dan daha iyi destekleniyor, ancak destek gelişiyor.
### Intel Arc
Intel Arc, Intel'in 2022'den itibaren piyasaya sürülen ayrık GPU ürün serisidir. Arc
GPU'lar XeSS'yi (Intel'in süper örneklemesi) destekler ve sınırlı ancak büyüyen bir desteğe sahiptir
OpenVINO ve IPEX-LLM çerçeveleri aracılığıyla yapay zeka çıkarım görevleri için.
### ARK Intel (ark.intel.com)
ARK, Intel'in ark.intel.com adresindeki resmi ürün özellikleri veritabanıdır. o
her Intel CPU, GPU, FPGA ve
Çekirdek sayıları, saat hızları, TDP, desteklenen bellek türleri dahil NUC ürünü,
ve talimat seti özellikleri. "Teknik özellikler için ARK'yı kontrol edin" ifadesini duyduğunuzda bunun anlamı
Yetkili donanım bilgileri için bu veritabanını ziyaret etmek.
---

## Yapay Zeka Performans Karşılaştırmaları
### MMLU (Devasa Çok Görevli Dil Anlayışı)
MMLU, aşağıdakiler de dahil olmak üzere 57 akademik konu genelinde LLM bilgisini test eden bir kıyaslamadır:
matematik, tarih, hukuk, tıp ve bilgisayar bilimi. Şunlardan oluşur:
Gerçek üniversite düzeyindeki sınavlardan alınan çoktan seçmeli sorular. Bir puan
%70'i kabaca insan lisans düzeyidir; GPT-4 ve Claude 3'ün puanı %86'nın üzerindedir.
Phi-3-mini, küçük boyutuna rağmen %70 civarında puan alıyor.
### İnsan Değerlendirmesi
HumanEval, OpenAI'nin kod üretimi için referans noktasıdır. 164 Python'dan oluşur
Otomatik test durumlarıyla ilgili programlama sorunları. Modeller ölçülür
pass@k — oluşturulan k çözümden en az birinin tümünü geçme olasılığı
testler. GPT-4 puanları ~%87 (geçti@1); iyi ayarlanmış bir 7B modeli ~%50–60'a ulaşabilir.
### HellaSwag
HellaSwag sağduyulu bir akıl yürütme ölçütüdür. Modellere bir cümle verilir
sıradan bir aktiviteyi tanımlıyor ve en olası devamı seçmelidir
dört seçenek. Yanlış seçenekler özellikle makul olacak şekilde tasarlanmıştır ancak
incelikle yanlış. Bir modelin temel bir fiziksel anlayışa sahip olup olmadığını test eder.
ve sosyal durumlar.
### ARC (AI2 Muhakeme Mücadelesi)
ARC, Allen Yapay Zeka Enstitüsü'nün bir ölçütüdür. İlkokuldan oluşur
"Kolay" ve "Zorlu" setlere bölünmüş fen soruları. Mücadele seti
erişime dayalı yöntemleri ve basit istatistiksel modelleri içeren sorular içerir
çok adımlı akıl yürütmeyi gerektiren bir mücadele.
---

## Temel Yapay Zeka/Makine Öğrenimi Kavramları
### RAG (Geri Alma-Artırılmış Nesil)
RAG, bir geri alma sistemini (tipik olarak bir vektör) birleştiren bir tekniktir.
veritabanı) bir dil modeliyle. Yalnızca modele güvenmek yerine
Parametrik bilgi, RAG öncelikle ilgili belgeleri harici bir kaynaktan alır.
bilgi tabanını oluşturur ve ardından bunları modelin bağlamına dahil eder. Bu şunları sağlar:
güncel veya alana özgü bilgilerle ilgili soruları yanıtlayan model
yeniden eğitim olmadan. Potato.ai bir RAG biçimi kullanır; KB'sinden alır
ve bir yanıt oluşturmadan önce sonuçları bağlama dahil eder.
### İnce ayar
İnce ayar, önceden eğitilmiş bir modeli eğitmeye devam etme sürecidir.
daha küçük, alana özgü veri kümesi. Bu, modelin ağırlıklarını
belirli bir görev veya etki alanı. Örneğin, bir temel LLM'ye ince ayar yapılabilir.
Tıbbi bir Soru-Cevap asistanı oluşturmak için tıbbi kayıtlar. İnce ayar
hesaplama açısından pahalıdır ancak sıfırdan eğitimden çok daha ucuzdur.
### Kuantizasyon
Niceleme, model ağırlıklarının sayısal kesinliğini azaltır (örneğin 32 bitten
4 bitlik tamsayıya kadar kayar). Bu, bellek ayak izini önemli ölçüde azaltır — 7B modeli
16 bit hassasiyette ~14 GB VRAM gerekir; 4 bitlik aynı model (GGUF formatı)
~4GB gerektirir. Niceleme tipik olarak küçük ama kabul edilebilir bir doğruluğa neden olur
bozulma ve büyük modellerin tüketici üzerinde çalışmasını sağlayan ana tekniktir
donanım ve hatta mobil cihazlar.
### Bağlam Penceresi
Bağlam penceresi, bir modelin aynı anda işleyebileceği maksimum jeton sayısıdır.
hem istemi hem de oluşturulan yanıtı içerir. GPT-3.5'in 4.096 jetonu vardı
pencere; GPT-4 Turbo ve Claude 3 128.000 jetonu destekliyor; İkizler 1.5 Pro
1.000.000 jetonu destekler. Daha büyük bir bağlam penceresi modelin "görmesini" sağlar
aynı anda daha fazla konuşma veya belgenin kullanılması, uzun süre tutarlılığın arttırılması
borsalar.
### RLHF (İnsan Geri Bildiriminden Takviyeli Öğrenme)
RLHF, temel dil modelini dönüştüren eğitim tekniğidir (ki bu
sadece bir sonraki jetonu tahmin eden) talimatları takip eden bir asistana dönüşür ve
yardımsever davranır. İnsan değerlendiriciler model çıktılarını puanlar, bir ödül modeli eğitilir
tercihlerine göre belirlenir ve daha sonra dil modeli buna göre optimize edilir
Takviyeli öğrenmeyi kullanan ödül modeli. ChatGPT, Claude ve Gemini'nin hepsi kullanıyor
RLHF çeşitleri veya benzer hizalama teknikleri (örn. Anayasal AI,
Doğrudan Tercih Optimizasyonu).
### Trafo Mimarisi
Transformer, tüm modern Yüksek Lisans'ların temelini oluşturan sinir ağı mimarisidir.
Vaswani ve arkadaşlarının 2017 tarihli "İhtiyacınız Olan Tek Şey Dikkat" başlıklı makalesinde tanıtılan
tüm jetonları paralel olarak işlemek için kişisel dikkat mekanizmalarını kullanır.
sırayla. Yalnızca Kodlayıcı Transformatörleri (BERT), görevleri anlamak için kullanılır;
Yalnızca kod çözücüye yönelik Transformatörler (GPT, Llama, Mistral) üretim görevleri için kullanılır;
Kodlayıcı-kod çözücü Transformatörleri (T5, BART) çeviri ve özetleme için kullanılır.
### Yerleştirmeler ve Vektör Veritabanları
Gömmeler, metinlerin (veya görsellerin) yoğun sayısal temsilleridir.
bir sinir ağı. Semantik olarak benzer metinler birbirine yakın yerleştirmelere sahiptir.
vektör uzayı. Vektör veritabanları (ChromaDB, Pinecone, Weaviate, Qdrant) deposu
Bu yerleştirmeler hızlı, yaklaşık en yakın komşu aramasını destekler. Onlar
Potato.ai'nin soğuk bellek katmanı da dahil olmak üzere RAG sistemlerinin depolama omurgasıdır.