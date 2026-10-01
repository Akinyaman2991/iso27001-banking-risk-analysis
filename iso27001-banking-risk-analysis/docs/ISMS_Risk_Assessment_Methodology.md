# 📐 ISO 27001:2022 & BDDK Uyumlu Bilgi Güvenliği Risk Metodolojisi

## 1. Amaç ve Kapsam
Bu doküman; Core Banking, Mobil/İnternet Bankacılığı, SWIFT ve IAM altyapılarındaki bilgi varlıklarının risk değerlendirme süreçlerini tanımlar.

## 2. Risk Hesaplama Formülü
Risk Değerlendirmesi; Varlık Değeri (AV), Tehdit Derecesi (T) ve Zafiyet Seviyesi (V) parametreleri çarpılarak hesaplanır:

$$Risk\ Skoru\ (R) = Varlık\ Değeri\ (AV) \times Tehdit\ (T) \times Zafiyet\ (V)$$

### Skala ve Derecelendirme (1-5 Likert Ölçeği)
- **1-15 (LOW):** Düşük Seviye Risk. Rutin izleme ve kabul edilebilir seviye.
- **16-45 (MEDIUM):** Orta Seviye Risk. Sonraki sprint/planlama döneminde kontrol ekleme.
- **46-80 (HIGH):** Yüksek Seviye Risk. 30 Gün içinde Ek-A ve BDDK kontrolü uygulama.
- **81-125 (CRITICAL):** Kritik Risk. Derhal aksiyon alma ve Yönetim Kurulu / CISO bilgilendirmesi.