from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import *

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

with open("private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        Encoding.PEM,
        PrivateFormat.PKCS8,
        NoEncryption()
    ))

with open("public.pem", "wb") as f:
    f.write(private_key.public_key().public_bytes(
        Encoding.PEM,
        PublicFormat.SubjectPublicKeyInfo
    ))

print("Keys generated!")
