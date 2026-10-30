"""Check that the NSM donation address is verifiably unspendable: a Zcash
Mainnet P2SH address whose script hash is HASH160 of the script OP_RETURN
(the single byte 0x6a), which fails evaluation whatever a spender supplies.

    python3 verify_nsm_donation_address.py
"""

import hashlib

ADDRESS = "t3QZUHYkaEQEuWosAc9HgMPKiQRdvuBPCQZ"
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
MAINNET_P2SH = bytes.fromhex("1cbd")
OP_RETURN = bytes([0x6A])

n = 0
for c in ADDRESS:
    n = n * 58 + ALPHABET.index(c)
raw = n.to_bytes(26, "big")
payload, checksum = raw[:-4], raw[-4:]
assert hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4] == checksum, "bad Base58Check checksum"
assert payload[:2] == MAINNET_P2SH, "not a Mainnet P2SH (t3) address"
script_hash = payload[2:]
hash160 = hashlib.new("ripemd160", hashlib.sha256(OP_RETURN).digest()).digest()
assert script_hash == hash160, "the script hash is not HASH160(OP_RETURN)"
print(f"{ADDRESS}: Mainnet P2SH, script hash {script_hash.hex()} = HASH160(OP_RETURN): unspendable")
