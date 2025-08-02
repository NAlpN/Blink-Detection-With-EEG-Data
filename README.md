# 👁️ EEG Blink Detection with MNE-Python

Bu proje, EEG sinyallerinden göz kırpma (blink) anlarını tespit etmek için geliştirilmiştir. Ham `.edf` formatındaki EEG verisi işlenerek, **band-pass filtreleme** ve **sinyal sivriliklerine (peaks) dayalı analiz** ile göz kırpmalar tespit edilir.

## 🚀 Özellikler

- `.edf` formatındaki EEG verilerini okuma (MNE kullanılarak)
- Belirli EEG kanalını izole edip görselleştirme (`Fp1`)
- 1–10 Hz aralığında band-pass filtreleme (Butterworth filtresi)
- `scipy.signal.find_peaks` ile blink tespiti
- Otomatik **blink rate** (Hz ve blink/dk) hesaplama
- EEG sinyali + tespit edilen blink'lerin görsel gösterimi

## 📁 Dosya Yapısı
  Blink-Detection-EEG/
  │
  ├── main.py # Tüm işlemleri gerçekleştiren ana betik
  ├── requirements.txt # Gerekli Python paketleri
  ├── README.md # Proje açıklaması (bu dosya)
  └── S001R01.edf # Örnek EEG verisi (PhysioNet'ten alınmıştır)


## 🛠️ Kullanılan Teknolojiler

- Python 3.9+
- [MNE-Python](https://mne.tools/)
- NumPy & Matplotlib
- SciPy

## Örnek Çıktı
  Tespit edilen blink sayısı: 8
  Blink Rate: 0.13 Hz
  Blink Rate: 7.87 blink/minute
  Durum: Uyanık ve dikkatli
