import socket
import random
import threading

def handle_incoming_client(conn, address):
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

def connect_to_server():
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port_number = random.randint(1000, 5000)

    print(port_number)

    host_socket.bind((host_name, port_number))
    host_socket.listen(5)

    while True:
        conn, address = host_socket.accept()

        thread = threading.Thread(target=handle_incoming_client, args=(conn, address))
        thread.start()

        print(f"Active connections : {threading.activeCount() - 1}")

    # conn, address = host_socket.accept()
    # print(f"Connection from : {address}")

    # while True:
    #     data = conn.recv(1024).decode()

    #     if not data:
    #         break

    #     print(f"Data from connected user : {data}")
    #     data = input("---")
    #     conn.send(data.encode())
    
    # conn.close()

if __name__ == '__main__':
    connect_to_server()