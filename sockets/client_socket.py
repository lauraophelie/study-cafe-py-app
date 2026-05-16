import socket

# sock_clt = socket.socket()
# port = 8124

# sock_clt.connect(('127.0.0.1', port))
# print(sock_clt.recv(1024).decode())
# sock_clt.close()

def create_client_socket():
    return socket.socket()

def connect_client_to_server(hostname, port):
    sock_clt = create_client_socket()
    sock_clt.connect((hostname, port))
    sock_clt.close