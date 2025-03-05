import random
import time
import multiprocessing

def generate_chars():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1000))

def generate_numbers():
    return sum(random.randint(0, 100) for _ in range(1000))

def run_multiprocessing():
    start_time = time.time()
    p1 = multiprocessing.Process(target=generate_chars)
    p2 = multiprocessing.Process(target=generate_numbers)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print(f"Multiprocessing Execution Time: {end_time - start_time:.5f} seconds")
    return end_time - start_time
