from multiprocessing import Process, Value
import time

def writer(shared_value):
    shared_value.value = 42
    print("Writer process: wrote 42 into shared memory")

def reader(shared_value):
    time.sleep(1)
    print("Reader process: read from shared memory:", shared_value.value)

if __name__ == "__main__":
    shared_value = Value('i', 0)

    writer_process = Process(target=writer, args=(shared_value,))
    reader_process = Process(target=reader, args=(shared_value,))

    writer_process.start()
    reader_process.start()

    writer_process.join()
    reader_process.join()