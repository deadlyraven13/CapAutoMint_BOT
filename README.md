# capmint 🪙

Script otomatis untuk melakukan mint token testnet cUSD dari CAP Faucet di jaringan MegaETH. Berguna untuk testing skenario transaksi atau automation di jaringan MegaETH tanpa menguras dana asli.

🔗 **Source Faucet Resmi:** [https://cap.app/testnet](https://cap.app/testnet)

---

## 🚀 Fitur

- Mint otomatis hingga 1000x transaksi.
- Delay acak antar transaksi agar tidak dicurigai bot.
- Status transaksi ditampilkan langsung di terminal.
- Ditulis dengan Python 3 + Web3.py.
- Konfigurasi aman via `.env`.

---

## 💪 Cara Instalasi

1. **Clone repository ini**

```bash
git clone https://github.com/deadlyraven13/capmint.git
cd capmint
```

2. **Buat dan aktifkan virtual environment**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# atau
source venv/bin/activate     # Linux/macOS
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Buat file `.env` dan isi sebagai berikut:**

```
PRIVATE_KEY=isi_dengan_private_key_anda
WALLET_ADDRESS=isi_dengan_alamat_wallet_anda
```

> ✅ *Jangan pernah membagikan file `.env` ke publik!*

---

## ▶️ Cara Menjalankan

```bash
python auto_mint_final.py
```

Transaksi akan berjalan otomatis sebanyak 1000 kali (atau bisa kamu ubah di dalam kode), dengan jeda acak antara 15 sampai 30 detik tiap transaksi.

---

## 📜 Lisensi

MIT © 2025 deadlyraven13

