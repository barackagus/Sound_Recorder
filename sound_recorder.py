import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Konfigurasi
freq = 44100  # Frekuensi sampling
duration = 10  # Durasi rekaman dalam detik
folder_name = "hasil rekaman"  # Nama folder untuk menyimpan file

try:
    # Membuat folder jika belum ada
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    print("Silakan Bicara")
    
    # Rekam suara
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2, dtype='int16')
    sd.wait()  # Tunggu hingga perekaman selesai
    
    # Normalisasi data suara untuk format int16
    recording = np.clip(recording, -32768, 32767)  # Batasi nilai agar dalam rentang int16
    
    # Simpan data rekaman ke file WAV di dalam folder
    file_path = os.path.join(folder_name, "recording0.wav")
    write(file_path, freq, recording)
    
    print("Successfully recorded and saved to", file_path)

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
