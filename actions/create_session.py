import socket
import random
import threading

from cryptography.fernet import Fernet

from actions.ecdh_key import convert_public_key_to_bytes, derive_secure_channel, deserialize_public_key_bytes, exchange_keys, generate_ecdh_key_pair, get_encrypted_group_key
from actions.study_invite_link import StudyInviteLink

def start_study_session(student_name, duration=60):
    host_socket, port_number = create_host_socket()
    print(port_number)

    print(student_name)
    print(duration)

    # study_invite = create_study_invite(student_name, host_socket)
    group_key, group_cipher = open_study_session()
    private_key, public_key = generate_ecdh_key_pair()

    # study_invite.generate_invite_link(group_cipher)
    while True:
        conn, address = host_socket.accept()

        thread = threading.Thread(target=handle_incoming_user, args=(conn, address, public_key, private_key, group_key, group_cipher))
        thread.start()

        print(f"Active connections : {threading.activeCount() - 1}")

def share_study_session():
    pass

def create_study_invite(student_name, socket):
    return StudyInviteLink(
        socket=socket,
        student_name=student_name
    )

def create_host_socket():
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port_number = random.randint(1000, 5000)

    host_socket.bind((host_name, port_number))
    host_socket.listen(5)

    return host_socket, port_number

def handle_incoming_user(conn, address, public_key, private_key, group_key, group_cipher):
    print(f"New connection from {address}")
    
    public_key_bytes = convert_public_key_to_bytes(public_key)
    conn.send(public_key_bytes)

    client_public_key_bytes = conn.recv(4096)
    client_public_key = deserialize_public_key_bytes(client_public_key_bytes)

    shared_secret = exchange_keys(private_key, client_public_key)
    secure_channel = derive_secure_channel(shared_secret)

    enc_group_key = get_encrypted_group_key(secure_channel, group_key)
    conn.send(enc_group_key)

    while True:
        try:
            enc_message = conn.recv(4096)

            if not enc_message:
                break

            message = group_cipher.decrypt(enc_message).decode()
            print(f"[{address}] : {message}")

            enc_response = group_cipher.encrypt(f"Server received : {message}".encode())
            conn.send(enc_response)
        except Exception as e:
            print(f"Error with connection from {address}: {e}")
            break
    conn.close()

def open_study_session():
    group_key = Fernet.generate_key()
    group_cipher = Fernet(group_key)

    return group_key, group_cipher