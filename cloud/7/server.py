import socket
import json

PORT , BUFFER_SIZE = 8080, 1024

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

FUNCTIONS = {"add": add,"subtract": subtract}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(1)
print("Server listening on port", PORT)

conn, addr = server_socket.accept()
print("Connection from:", addr)

data = conn.recv(BUFFER_SIZE).decode()
request = json.loads(data)

func_name = request["function"]
args = request["args"]
result = FUNCTIONS[func_name](*args)

conn.sendall(str(result).encode())
conn.close()
server_socket.close()
print("Result sent to client.")
