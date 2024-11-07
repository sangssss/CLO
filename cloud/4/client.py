# chat_client.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    """Continuously receives and prints messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"\n{message.decode()}")
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def start_client():
    """Connects to the chat server and handles user input."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the chat server.")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())
        if message.strip().lower() == "exit":
            print("Disconnecting from the server...")
            client_socket.close()
            break

if __name__ == "__main__":
    start_client()
