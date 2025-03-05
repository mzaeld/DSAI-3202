import random
import time
import threading

def generate_chars():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1000))

def generate_numbers():
    return sum(random.randint(0, 100) for _ in range(1000))

def run_threads():
    start_time = time.time()
    t1 = threading.Thread(target=generate_chars)
    t2 = threading.Thread(target=generate_numbers)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print(f"Threaded Execution Time: {end_time - start_time:.5f} seconds")
    return end_time - start_time



     