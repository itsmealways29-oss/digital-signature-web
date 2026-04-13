from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from core.hashing import sha256_hash

def sign_data(private_key, data):
    hashed = sha256_hash(data)

    signature = private_key.sign(
        hashed,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    return signature, hashed


def verify_data(public_key, data, signature):
    hashed = sha256_hash(data)

    try:
        public_key.verify(
            signature,
            hashed,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True, hashed
    except:
        return False, hashed