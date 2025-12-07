# Bitcoin Notes — Gokul Bansal

## Core Bitcoin Concepts

### Block Structure
- A block = header + transactions  
- Block header = 80 bytes containing:  
  - version  
  - previous block hash  
  - merkle root  
  - timestamp  
  - bits (difficulty target)  
  - nonce  

### UTXO Model
- Bitcoins are not "accounts" — they are **UTXOs** (unspent outputs).
- Transactions consume UTXOs and create new ones.

### Mining
- Miners find a nonce that produces a block header hash below the current target.
- Proof-of-Work keeps the network secure.

### Nodes
- Validate blocks and transactions.
- Maintain blockchain state.
- Relay information across network.

## Learning Logs
- ✓ Watched: "Bitcoin for Beginners — Andreas Antonopoulos"
- ✓ Read: Mastering Bitcoin (Ch 1–3)

More notes will be added as I progress.

