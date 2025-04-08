# 💹 capmint — Auto Mint Testnet cUSD with Web3.py

Script Python untuk otomatisasi proses mint token testnet cUSD dari faucet contract di jaringan MegaETH.

## 🚀 Fitur

- Mint token cUSD dalam jumlah besar (loop otomatis).
- Delay acak antar transaksi.
- Status transaksi (berhasil/gagal) ditampilkan real-time.
- GUI (opsional) bisa ditambahkan untuk tampilan saldo.

---

## 🧰 Requirement

- Python 3.10+
- Git
- Virtualenv (opsional tapi direkomendasikan)

---

## ⚖️ Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/deadlyraven13/capmint.git
cd capmint
```

### 2. Buat Virtual Environment (opsional tapi disarankan)

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Konfigurasi

### 1. Buat file `.env`

Di dalam direktori project, buat file `.env` dan isi seperti berikut:

```dotenv
PRIVATE_KEY=0x...           # Private key wallet kamu
WALLET_ADDRESS=0x...        # Public address wallet kamu
```

> ⚠️ **Jangan pernah share file `.env` ke publik.**

---

## ▶️ Menjalankan Script

```bash
python auto_mint_final.py
```

Script akan otomatis melakukan mint ke contract faucet sebanyak 1000x (bisa disesuaikan di kode).

---

## 📁 Struktur Folder

```
capmint/
├── auto_mint_final.py      # Script utama
├── .env                    # (kamu buat sendiri)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📟 Lisensi

MIT License. Gunakan dengan tanggung jawab.

---

## 💬 Kontak

Created by [@deadlyraven13](https://github.com/deadlyraven13)
