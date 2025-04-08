import os
import time
import random
from web3 import Web3
from dotenv import load_dotenv

# === LOAD ENV ===
load_dotenv()
RPC_URL = "https://carrot.megaeth.com/rpc"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = Web3.to_checksum_address(os.getenv("WALLET_ADDRESS"))
CONTRACT_ADDRESS = "0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f"
MINT_COUNT = 1000

# Delay antar transaksi (acak, dalam detik)
DELAY_MIN = 15
DELAY_MAX = 30

# === ABI ===
ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "receiver", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

# === SETUP WEB3 ===
w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

if not w3.is_connected():
    raise Exception("❌ Gagal konek ke RPC")

print(f"🔁 Memulai proses mint {MINT_COUNT}x testnet cUSD...\n")

# === FUNGSI CEK SALDO ===
def get_balance():
    try:
        balance_wei = contract.functions.balanceOf(WALLET_ADDRESS).call()
        return w3.from_wei(balance_wei, 'ether')
    except:
        return "N/A"

# === MINT LOOP ===
for i in range(MINT_COUNT):
    try:
        nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
        tx = contract.functions.mint(WALLET_ADDRESS, Web3.to_wei(1000, 'ether')).build_transaction({
            'from': WALLET_ADDRESS,
            'nonce': nonce,
            'gas': 250000,
            'gasPrice': w3.to_wei('0.01', 'gwei'),
        })

        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"🔃 Mint ke-{i+1}: TX terkirim → {w3.to_hex(tx_hash)}")

        receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        status = "✅ SUCCESS" if receipt.status == 1 else "❌ FAILED"
        print(f"   ↳ Status TX: {status}")

        # Tampilkan saldo setelah mint
        balance = get_balance()
        print(f"   💰 Saldo cUSD sekarang: {balance}\n")

    except Exception as e:
        print(f"🚨 Error saat mint ke-{i+1}: {e}\n")
        time.sleep(5)

    delay = random.randint(DELAY_MIN, DELAY_MAX)
    print(f"⏳ Delay {delay} detik...\n")
    time.sleep(delay)

print("🎉 Semua mint selesai!")
