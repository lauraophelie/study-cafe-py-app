from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

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