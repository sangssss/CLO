import socket
import json

SERVER_IP = '127.0.0.1'
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

request = {"function": "add","args": [10, 5]
}
client_socket.sendall(json.dumps(request).encode())

result = client_socket.recv(1024).decode()
print("Result from server:", result)

client_socket.close()
