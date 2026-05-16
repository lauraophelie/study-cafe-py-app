import socket
import random

def connect_to_server():
    sock = socket.socket()
    port_number = random.randint(1000, 8124)

    sock.bind(('', port_number))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print("Connection from ", addr)

        conn.send("Thank you for joining the study session :)".encode())
        conn.close()

        break

# sock = socket.socket()
# port = 8124

# sock.bind(('', port))
# print("Socket attached to port %s" %(port))

# sock.listen(5)

# while True:
#     conn, addr = sock.accept()
#     print("Connection from ", addr)

#     conn.send("Thank you for connecting".encode())
#     conn.close()
#     break
