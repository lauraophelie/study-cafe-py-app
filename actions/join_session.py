from cryptography.fernet import Fernet

from actions.ecdh_key import convert_public_key_to_bytes, derive_secure_channel, deserialize_public_key_bytes, exchange_keys, generate_ecdh_key_pair

import socket

def join_study_session(username, study_link):
    private_key, public_key = generate_ecdh_key_pair()
    dec_study_link = study_link.decode()

    client_socket = socket.socket()
    client_socket.connect((dec_study_link.server_host, dec_study_link.server_port_number))

    host_public_key_bytes = client_socket.recv(4096)
    host_public_key = deserialize_public_key_bytes(host_public_key_bytes)

    public_key_bytes = convert_public_key_to_bytes(public_key)
    client_socket.send(public_key_bytes)

    shared_secret = exchange_keys(private_key, host_public_key)
    secure_channel = derive_secure_channel(shared_secret)
    enc_group_key = client_socket.recv(4096)

    group_key = secure_channel.decrypt(enc_group_key)
    group_cipher = Fernet(group_key)

    message = input("---")

    while message.lower().strip() != 'bye':
        enc_message = group_cipher.encrypt(message.encode())
        client_socket.send(enc_message)

        enc_response = client_socket.recv(4096)
        response = group_cipher.decrypt(enc_response).decode()

        print(f"Received from server: {response}")

        message = input("---")

    client_socket.close()

