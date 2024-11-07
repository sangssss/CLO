from multiprocessing import Process, Pipe

def child_process(conn):
    message_from_parent = conn.recv()
    print(f"Child received: {message_from_parent}")
    response = "Hello from child"
    conn.send(response)
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    message_to_child = input("Enter a message to send to the child: ")
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    parent_conn.send(message_to_child)
    response_from_child = parent_conn.recv()
    print(f"Parent received: {response_from_child}")
    parent_conn.close()
    p.join()
