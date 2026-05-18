from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

import base64

def get_encrypted_group_key(secure_channel, group_key):
    return secure_channel.encrypt(group_key)

def get_derived_key(host_shared_secret):
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"study-session"
    ).derive(host_shared_secret)

    fernet_key = base64.urlsafe_b64encode(derived_key)
    secure_channel = Fernet(fernet_key)

    return secure_channel

def save_public_key(private_key, public_key_name):
    pem_public_key = private_key.public_key().public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_file = open(f"public-{public_key_name}-key.pub", "w")
    public_key_file.write(pem_public_key.decode())
    public_key_file.close()

def generate_ecdh_key_pair():
    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )
    public_key = private_key.public_key()

    print(f"Private key : {private_key}")
    print(f"Public key : {public_key}")

    return private_key, public_key