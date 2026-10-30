"""Check that the designated NSM addresses are verifiably unspendable: Zcash
P2SH addresses whose script hash is HASH160 of the script OP_RETURN (the
single byte 0x6a), which fails evaluation whatever a spender supplies.

    python3 verify_nsm_donation_address.py
"""

import hashlib

ADDRESSES = {  # address: (network, P2SH version prefix)
    "t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ": ("Mainnet", bytes.fromhex("1cbd")),
    "t2CYfLDri6rrH4WSuXtHiu1WMWus6kFY2Ea": ("Testnet", bytes.fromhex("1cba")),
}
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
OP_RETURN = bytes([0x6A])
HASH160 = hashlib.new("ripemd160", hashlib.sha256(OP_RETURN).digest()).digest()

for address, (network, prefix) in ADDRESSES.items():
    n = 0
    for c in address:
        n = n * 58 + ALPHABET.index(c)
    raw = n.to_bytes(26, "big")
    payload, checksum = raw[:-4], raw[-4:]
    assert hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4] == checksum, f"{address}: bad Base58Check checksum"
    assert payload[:2] == prefix, f"{address}: not a {network} P2SH address"
    assert payload[2:] == HASH160, f"{address}: the script hash is not HASH160(OP_RETURN)"
    print(f"{address}: {network} P2SH, script hash {HASH160.hex()} = HASH160(OP_RETURN): unspendable")
