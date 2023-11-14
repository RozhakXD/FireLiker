# 🔥 FireLiker - TikTok Views Booster Bot

![FireLiker Logo](https://github.com/user-attachments/assets/6d5ade11-9163-4224-bc15-19cea7665a40)

**FireLiker** adalah bot otomatis berbasis Python yang menambah views video TikTok tanpa login, dengan meniru interaksi pengguna secara aman di situs Fireliker.com menggunakan Selenium.

## 🚀 Fitur Utama

- ✅ **Tanpa Login** – Tidak menyimpan atau meminta kredensial TikTok.
- ⚙️ **Otomatisasi Penuh** – Kirim views secara berkala dengan satu kali pengaturan.
- 🌐 **Berbasis Browser** – Menggunakan WebDriver untuk simulasi interaksi nyata.
- 🛡️ **Aman 99%** – Tidak melanggar kebijakan login atau keamanan TikTok.

## 🛠️ Instalasi

```bash
git clone https://github.com/RozhakLabs/FireLiker.git
cd FireLiker
pip install -r requirements.txt
python main.py
```

> **Note**: Pastikan Chrome dan `chromedriver` sudah terpasang, atau gunakan `webdriver-manager` (sudah disertakan).

## ▶️ Cara Menjalankan

1. Masukkan username Fireliker (bukan akun TikTok).
2. Ikuti instruksi di layar untuk verifikasi manual (captcha, dll).
3. Pilih video yang ingin ditambah views-nya.
4. Bot akan berjalan otomatis dan mengirim views.

## 📸 Screenshot

![Cuplikan layar 2025-05-01](https://github.com/user-attachments/assets/48eda380-4f80-42ab-80b4-cbca2ed3e81d)

## 📁 Struktur Proyek

```
FireLiker/
├── main.py          # Entry point utama bot
├── config.py        # Konfigurasi URL dan timeout
├── browser/         # Modul selenium dan aksi halaman
├── models/          # Representasi data video
└── utils/           # Logging & helper
```

## ⚠️ Disclaimer

FireLiker is intended solely for educational and technical learning purposes. All risks, including violations of TikTok policies or applicable laws, are the sole responsibility of the user. Use it wisely, on test accounts/environments, and avoid misuse.

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.