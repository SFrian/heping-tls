
# 🛡️ Pentest Attack Dashboard

Dashboard visual interaktif untuk menampilkan hasil serangan pentest seperti Apache Benchmark (ab) dan Hping3 menggunakan Flask dan Chart.js.

## 🚀 Fitur
- Jalankan pengujian `ab` untuk melihat request per detik
- Jalankan `hping3` untuk melihat jumlah paket yang dikirim
- Hasil ditampilkan dalam grafik interaktif
- Docker-ready

## 🧰 Prasyarat
- Python 3.x
- `ab` (Apache Benchmark)
- `hping3`
- Docker (opsional jika menjalankan via container)

## 🔧 Instalasi Lokal

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/namarepo.git
   cd namarepo
   ```

2. **Install dependensi:**
   ```bash
   pip install flask
   ```

3. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```

4. **Buka browser ke:**
   ```
   http://localhost:5000
   ```

## 🐳 Jalankan dengan Docker

1. **Build Docker image:**
   ```bash
   docker build -t pentest-dashboard .
   ```

2. **Jalankan container:**
   ```bash
   docker run -it --rm --net=host pentest-dashboard
   ```

> 🛑 **Catatan:** `--net=host` dibutuhkan agar `ab` dan `hping3` bisa mengakses jaringan dengan benar.

## 📂 Struktur Folder

```
├── app.py              # Backend Flask
├── index.html          # Frontend (Dashboard)
├── Dockerfile          # Docker konfigurasi
└── README.md           # Dokumentasi
```

## ⚠️ Peringatan
- `hping3` menggunakan `--flood`, yang bisa menyebabkan DoS (Denial of Service). Gunakan hanya di lab atau jaringan legal yang kamu miliki izin.
- Proyek ini hanya untuk tujuan edukasi!

## 📄 Lisensi
MIT License
