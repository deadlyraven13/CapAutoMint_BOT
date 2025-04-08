# 💹 capmint – Auto Mint Testnet cUSD on MegaETH

Script otomatis untuk mint testnet cUSD ke wallet kamu di jaringan MegaETH menggunakan Python dan Web3.py.

## 🚀 Fitur

- Mint hingga 1000x cUSD langsung ke wallet
- Delay acak antara setiap transaksi untuk menghindari spam detection
- Menampilkan status transaksi (sukses/gagal)
- Kode bersih dan mudah dimodifikasi
- GUI (opsional) versi Tkinter/Streamlit coming soon

## 🛆 Requirements

- Python 3.8+
- Web3.py
- dotenv

Install dependensi:
```bash
pip install -r requirements.txt
```

## ⚙️ Konfigurasi

Buat file `.env` di direktori yang sama:

```env
PRIVATE_KEY=0xYOUR_PRIVATE_KEY
WALLET_ADDRESS=0xYOUR_WALLET_ADDRESS
```

> ⚠️ **Jangan share file `.env` kamu ke publik!**

## 🧪 Cara Jalankan

```bash
python auto_mint_final.py
```

## 💡 Catatan

- RPC default menggunakan: `https://carrot.megaeth.com/rpc`
- Kontrak mint cUSD: `0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f`
- Token ini adalah token ERC-20

## 📜 Lisensi

MIT License
