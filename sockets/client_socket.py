import socket

def connect_to_host_server(port_number):
    client_socket = socket.socket()
    client_socket.connect((socket.gethostname(), port_number))

    message = input("---")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(f"Received from server : {data}")
        message = input("---")

    client_socket.close()

# if __name__ == '__main__':
#     connect_to_host_server(3118)