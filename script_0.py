
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Retrieve values from .env
RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")

# Connect to the blockchain node
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if w3.is_connected():
    print(" Connected to Legion Crypto")
else:
    print(" Connection failed")

# Check balance
balance = w3.eth.get_balance(SENDER_ADDRESS)
print(f'Balance: {w3.from_wei(balance, "ether")} ETH') # Исправлено: {...}

# Function to send a transaction
def send_transaction(recipient, amount_eth):
    nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f' Transaction sent: {tx_hash.hex()}') # Исправлено: {...}

# Simple Python script - Commit 0 - 2025-02-25 04:14:24
print(f"Performing blockchain info check: w3.eth.get_gas_price()")
print(f"Web3 is connected: {w3.is_connected}") # Исправлено: {...}
print(f"Commit Number: 0")
print(f"Random number: 100")
# Example: Send 0.01 ETH
recipient_address = '0xRecipientAddressHere'
send_transaction(recipient_address, 0.01)
print(f"Simulating NFT interaction with contract: MyTokenContract")
print(f"Performing NFT action: mint_nft()")
