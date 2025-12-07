#!/usr/bin/env python3

# Basic Bitcoin Block Header Parser (Starter Project)
# Usage: python3 block_parser.py block.hex

import sys

def parse_header(raw_hex):
    raw = bytes.fromhex(raw_hex)

    if len(raw) < 80:
        print("Error: block header must be at least 80 bytes")
        return

    version = int.from_bytes(raw[0:4], "little")
    prev_block = raw[4:36][::-1].hex()
    merkle_root = raw[36:68][::-1].hex()
    timestamp = int.from_bytes(raw[68:72], "little")
    bits = int.from_bytes(raw[72:76], "little")
    nonce = int.from_bytes(raw[76:80], "little")

    print("=== Block Header ===")
    print("Version:", version)
    print("Previous Block Hash:", prev_block)
    print("Merkle Root:", merkle_root)
    print("Timestamp:", timestamp)
    print("Bits:", bits)
    print("Nonce:", nonce)
    print("====================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 block_parser.py block.hex")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        hexdata = f.read().strip()

    parse_header(hexdata)

