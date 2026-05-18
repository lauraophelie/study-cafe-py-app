import socket
import random

def connect_to_server():
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port_number = random.randint(1000, 5000)
    print(port_number)

    host_socket.bind((host_name, port_number))
    host_socket.listen(5)

    conn, address = host_socket.accept()
    print(f"Connection from : {address}")

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        print(f"Data from connected user : {data}")
        data = input("---")
        conn.send(data.encode())
    
    conn.close()

# if __name__ == '__main__':
#     connect_to_server()