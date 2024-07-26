# Sound_Recorder
This is a simple voice recorder application

# README

## Gambaran Umum

Skrip ini merekam audio dari mikrofon Anda dan menyimpannya sebagai file WAV. Skrip ini menggunakan pustaka `sounddevice` untuk merekam audio, `scipy` untuk menulis file WAV, dan `numpy` untuk menangani data audio.

## Fitur

- Merekam audio untuk durasi yang ditentukan.
- Menyimpan rekaman sebagai file WAV di folder yang ditentukan.
- Menangani pembuatan folder jika belum ada.

## Persyaratan

Sebelum menjalankan skrip, pastikan Anda telah menginstal pustaka Python berikut:

- `sounddevice`
- `scipy`
- `numpy`

Anda dapat menginstal pustaka-pustaka ini menggunakan pip:

```bash
pip install sounddevice scipy numpy
```

## Konfigurasi

Anda dapat memodifikasi parameter berikut dalam skrip sesuai kebutuhan Anda:

- `freq`: Frekuensi sampling (default adalah 44100 Hz).
- `duration`: Durasi rekaman dalam detik (default adalah 10 detik).
- `folder_name`: Nama folder tempat rekaman akan disimpan (default adalah `"hasil rekaman"`).

## Cara Menggunakan

1. Clone atau unduh repositori yang berisi skrip.
2. Jalankan skrip menggunakan Python:

   ```bash
   python <nama_skrip>.py
   ```

   Gantilah `<nama_skrip>` dengan nama file skrip yang sebenarnya.

3. Saat diminta, bicaralah ke mikrofon Anda. Skrip ini akan merekam suara Anda dan menyimpan rekaman sebagai file WAV.

## Penanganan Kesalahan

Jika terjadi kesalahan selama proses perekaman atau penyimpanan, skrip akan mencetak pesan kesalahan untuk membantu mendiagnosis masalah.

## Contoh

Berikut adalah contoh cara menjalankan skrip dan apa yang dapat diharapkan:

```bash
python record_audio.py
```

Output:
```
Silakan Bicara
Berhasil merekam dan menyimpan ke hasil rekaman/recording0.wav
```

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detailnya.

## Kontribusi

Silakan berkontribusi dengan mengajukan masalah atau permintaan tarik. Untuk perubahan besar, harap buka masalah terlebih dahulu untuk mendiskusikan apa yang ingin Anda ubah.
