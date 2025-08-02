# 1. Aşama: Veri Setini Okuma ve Görselleştirme

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

raw = mne.io.read_raw_edf("S001R01.edf", preload=True)

# raw.plot(n_channels=10, scalings='auto')

print(raw.ch_names)

raw.pick_channels(['Fp1.'])

data, times = raw[:1]

# plt.figure(figsize=(12, 4))
# plt.plot(times, data[0], color='blue')
# plt.title("Ham EEG Sinyali (Fp1)")
# plt.xlabel("Zaman (saniye)")
# plt.ylabel("Mikrovolt")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# 2. Aşama: Bandpass Filtre + Blink Tespiti (Peak Detection)

from scipy.signal import butter, filtfilt, find_peaks

def b_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_b_filter(data, lowcut, highcut, fs, order=4):
    b, a = b_bandpass(lowcut, highcut, fs, order)
    return filtfilt(b, a, data)

filtered = apply_b_filter(data[0], 1.0, 10.0, raw.info['sfreq'])
peaks, _ = find_peaks(filtered, height=0.0002, distance=200)

# plt.figure(figsize=(12, 4))
# plt.plot(times, filtered, label='Filtreden Geçmiş EEG (Fp1)', color='green')
# plt.plot(times[peaks], filtered[peaks], 'rx', label='Tespit Edilen Blink')
# plt.title("Blink Tespiti – Fp1 Kanalı")
# plt.xlabel("Zaman (s)")
# plt.ylabel("Mikrovolt")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

print(f"Tespit edilen blink sayısı: {len(peaks)}")

duration_sec = times[-1]  # Son zaman değeri
blink_rate_hz = len(peaks) / duration_sec
blink_rate_min = blink_rate_hz * 60

print(f"Blink Rate: {blink_rate_hz:.2f} Hz")
print(f"Blink Rate: {blink_rate_min:.2f} blink/minute")

if blink_rate_min < 10:
    print("Durum: Uyanık ve dikkatli")
elif 10 <= blink_rate_min < 25:
    print("Durum: Orta düzey yorgunluk")
else:
    print("Durum: Yorgunluk belirtileri var")