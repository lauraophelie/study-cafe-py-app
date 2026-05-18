from cryptography.fernet import Fernet 

from cryptography.hazmat.primitives.asymmetric import ec

from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

import base64

# host creates room
group_key = Fernet.generate_key()
group_cipher = Fernet(group_key)

print("Study room opened")

# host generates diffie-hellman keys
host_private_key = ec.generate_private_key(
    ec.SECP256R1()
)
host_public_key = host_private_key.public_key()

# invite token
invite_token = {
    "host_ip": "192.168.1.5",
    "port": 5000,
    "room_id": "ROOM-123"
}

# client joins
client_private_key = ec.generate_private_key(
    ec.SECP256R1()
)
client_public_key = client_private_key.public_key()

# public key exchange : host & client exchange public key

# both derive same shared secret
# host side 
host_shared_secret = host_private_key.exchange(
    ec.ECDH(),
    client_public_key
)

# client side
client_shared_secret = client_private_key.exchange(
    ec.ECDH(),
    host_public_key
)

host_shared_secret == client_shared_secret

# use HKDF to derive a real encryption key
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"study-session"
).derive(host_shared_secret)

fernet_key = base64.urlsafe_b64encode(derived_key)
secure_channel = Fernet(fernet_key)

# host sends group session key securely
encrypted_group_key = secure_channel.encrypt(group_key)


