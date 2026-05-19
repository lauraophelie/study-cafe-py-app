import socket
import random
import threading

from cryptography.fernet import Fernet
from actions.study_invite_link import StudyInviteLink

def start_study_session(student_name, duration=60):
    host_socket, port_number = create_host_socket()
    print(port_number)

    study_invite = create_study_invite(student_name, host_socket)

    while True:
        conn, address = host_socket.accept()

        thread = threading.Thread(target=handle_incoming_user, args=(conn, address))
        thread.start()

        print(f"Active connections : {threading.activeCount() - 1}")

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

def handle_incoming_user(conn, address):
    print(f"New connection from {address}")
    while True:
        try:
            message = conn.recv(1024).decode()

            if message:
                print(f"Message from {address}: {message}")
                conn.send(message.encode())
        except Exception as e:
            print(f"Error with connection from {address}: {e}")
            break
    conn.close()

def open_study_session():
    group_key = Fernet.generate_key()
    group_cipher = Fernet(group_key)

    return group_key, group_cipher