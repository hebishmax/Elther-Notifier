import requests
import json
from web3 import Web3
import argparse

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY"))

contract_address = Web3.to_checksum_address("0xYourContractAddress")
abi = json.load(open("contract/abi.json"))

contract = w3.eth.contract(address=contract_address, abi=abi)

def fetch_status_from_api():
    url = "https://api.github.com/events"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    return "available" if response.status_code == 200 else "busy"

def update_contract_status(status):
    account = w3.eth.account.from_key("YOUR_PRIVATE_KEY")
    txn = contract.functions.update_status(status).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 200000,
        "gasPrice": w3.to_wei("20", "gwei")
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash.hex()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check current network status")
    parser.add_argument("--update", action="store_true", help="Update network status onchain")
    args = parser.parse_args()

    if args.check:
        print(fetch_status_from_api())
    elif args.update:
        status = fetch_status_from_api()
        tx_hash = update_contract_status(status)
        print(f"Status updated onchain: {tx_hash}")

if __name__ == "__main__":
    main()
