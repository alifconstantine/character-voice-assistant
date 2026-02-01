# Character Voice Assistant (Qwen3-TTS)

Proyek ini adalah asisten suara interaktif yang menggabungkan kecerdasan LLM (OpenRouter) dengan teknologi *voice cloning* dari Qwen3-TTS untuk meniru suara Yae Miko dari Genshin Impact atau Karakter Lainnya.

## Prasyarat (Requirements)
- **GPU NVIDIA** sangat direkomendasikan (RTX 30-series atau lebih baru untuk performa terbaik).
- **Python 3.10+**.
- **SoX (Sound eXchange)** terinstall di sistem dan masuk ke PATH.

## Cara Penggunaan

### 1. Clone Repository
```bash
git clone https://github.com/alifconstantine/character-voice-assistant.git
cd Clone-Voice
```

### 2. Setup Virtual Environment (Rekomendasi)
Sangat disarankan untuk menggunakan venv agar library tidak berantakan di sistem utama.

```bash
python -m venv venv
# Aktifkan venv (Windows)
.\venv\Scripts\activate
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment
```bash
OPENROUTER_API_KEY=your_api_key_here
```

### 5. Siapkan Audio Referensi
Pastikan kamu memiliki file audio untuk di-clone:

Masukkan file suara ke folder proyek (Contoh: `yae-wav_train.WAV`).

Update variabel `ref_audio` dan `ref_text` di dalam `main.py` sesuai dengan file audio dan isi ucapannya.

## Pemilihan Model (0.6B vs 1.7B)
Di dalam `main.py`, kamu bisa memilih varian model berdasarkan spesifikasi PC kamu:

| Fitur | Qwen3-TTS-0.6B (Recommended) | Qwen3-TTS-1.7B |
| :-------- | :------- | :------------------------- |
| **VRAM** | ~4 GB (Hemat memori) | ~8 GB (Lebih berat) |
| **Kecepatan** | Sangat Cepat (RTF ~0.86) | Standar (RTF ~1.26) |
| **Kualitas** | Bagus & Jelas | Sangat Realistis & Detail |
| **Cocok Untuk** | RTX 3050 / 4050 / Laptop | RTX 3060 / 4060 ke atas |

## Menjalankan Program
Setelah semua siap, jalankan program dengan:

```bash
python main.py
```
