import socket

PORT = 8080
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(1)

print("Server listening on port", PORT)
conn, addr = server_socket.accept()
print("Connection from:", addr)

with open("received_file.txt", "wb") as file:
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        file.write(data)

conn.close()
server_socket.close()
print("File received and saved as 'received_file.txt'")
