from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

import base64

'''
steps to follow : 
- host creates room : 
    * open_study_session() = group_key, group_cipher

- host generates dh keys (private, public)
    * generate_ecdh_key_pair() = host_private_key, host_public_key
    * save host_public_key_file

- generate invite token
    * StudyInviteLink.generate_invite_link(group_cipher)

- client joins -> generate dh keys (private, public)
    * generate_ecdh_key_pair() = client_private_key, client_public_key
    * save client_public_key_file
- host & client exchange public keys

- derive from the same shared key : get the shared_key
    * exchange_keys(host_private_key, client_public_key) = host_shared_key

- get derived key from the shared secret 
    * get_derived_key(host_shared_key) = secure_channel

- host sends group session key securely 
    * get_encrypted_group_key(secure_channel, group_key)
'''

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

def exchange_keys(host_private_key, exchanged_public_key):
    return host_private_key.exchange(
        ec.ECDH(),
        exchanged_public_key
    )

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