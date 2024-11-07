import socket

SERVER_IP = '127.0.0.1'
PORT = 8080
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

with open("send_file.txt", "rb") as file:
    while True:
        data = file.read(BUFFER_SIZE)
        if not data:
            break
        client_socket.sendall(data)

client_socket.close()
print("File sent to server.")
