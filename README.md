# Cap app — Auto Mint Testnet

Script Python untuk otomatisasi proses mint token testnet cUSD dari faucet contract di jaringan MegaETH.

🔗 Source Faucet Resmi: [https://cap.app/testnet](https://cap.app/testnet)

##  Fitur

- Mint token cUSD dalam jumlah besar (loop otomatis).
- Delay acak antar transaksi.
- Status transaksi (berhasil/gagal) ditampilkan real-time.

---

##  Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/deadlyraven13/CapAutoMint_BOT.git
cd CapAutoMint_BOT
```

### 2. Buat Virtual Environment (opsional tapi disarankan)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Buat file `.env`

Di dalam direktori project, buat file `nano .env` dan isi seperti berikut:

```dotenv
PRIVATE_KEY=0x...           # Private key wallet kamu
WALLET_ADDRESS=0x...        # Public address wallet kamu
```
PRIVATE KEY MENGUNAKAN 0x

## 5. Menjalankan Script

```bash
python bot.py
```

Script akan otomatis melakukan mint ke contract faucet sebanyak 1000x (bisa disesuaikan di kode).

---

##  Struktur Folder

```
CapAutoMint_BOT/
├── bot.py      
├── .env                    
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

