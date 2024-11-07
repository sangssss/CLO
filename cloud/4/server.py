# chat_server.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
clients = []

def broadcast(message, sender_client):
    """Broadcasts a message to all clients except the sender."""
    for client in clients:
        if client != sender_client:
            try:
                client.sendall(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    """Handles communication with a connected client."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message or message.decode().strip().lower() == "exit":
                print("Client disconnected.")
                clients.remove(client_socket)
                client_socket.close()
                break
            print(f"Received message: {message.decode()}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    """Starts the chat server and listens for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
