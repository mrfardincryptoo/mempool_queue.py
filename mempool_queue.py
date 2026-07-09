# Simulate a basic Mempool queue for incoming transactions
mempool = []

def add_to_mempool(tx_hash, sender):
    mempool.append({"tx": tx_hash, "from": sender})
    print(f"Tx {tx_hash[:8]}... added to mempool.")

def process_next_tx():
    if mempool:
        next_tx = mempool.pop(0)
        print(f"Processing Tx: {next_tx['tx']} from {next_tx['from']}")
    else:
        print("Mempool is empty.")

add_to_mempool("0xabc1239999999999999999999999", "UserA")
process_next_tx()
