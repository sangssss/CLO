import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
message = "Hello, Server!"
client_socket.send(message.encode())
echoed_message = client_socket.recv(1024).decode()
print(f"Received from server: {echoed_message}")
client_socket.close()