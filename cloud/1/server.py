import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

message = conn.recv(1024).decode()
print(f"Received from client: {message}")
conn.send(message.encode())

conn.close()
server_socket.close()