import multiprocessing

def sender(queue):
    while True:
        message = input("Enter a message to send (or type 'exit' to stop): ")
        if message.lower() == 'exit':
            queue.put(None)  
            break
        queue.put(message)

def receiver(queue):
    while True:
        message = queue.get()
        if message is None:  # Check for stop signal
            break
        print(f"Received message: {message}")

if __name__ == '__main__':
    
    queue = multiprocessing.Queue()

    sender_process = multiprocessing.Process(target=sender, args=(queue,))
    receiver_process = multiprocessing.Process(target=receiver, args=(queue,))

    sender_process.start()
    receiver_process.start()
    
    sender_process.join()
    receiver_process.join()
