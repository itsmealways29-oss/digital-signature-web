from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key
)

def load_private_key(file_bytes):
    return load_pem_private_key(file_bytes, password=None)

def load_public_key(file_bytes):
    return load_pem_public_key(file_bytes)