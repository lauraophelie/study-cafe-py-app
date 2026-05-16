import socket

sock_clt = socket.socket()
port = 8124

sock_clt.connect(('127.0.0.1', port))
print(sock_clt.recv(1024).decode())
sock_clt.close()