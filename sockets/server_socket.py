import socket

sock = socket.socket()
port = 8124

sock.bind(('', port))
print("Socket attached to port %s" %(port))

sock.listen(5)

while True:
    conn, addr = sock.accept()
    print("Connection from ", addr)

    conn.send("Thank you for connecting".encode())
    conn.close()
    break
