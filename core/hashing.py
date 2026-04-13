import hashlib

def sha256_hash(data: bytes):
    return hashlib.sha256(data).digest()