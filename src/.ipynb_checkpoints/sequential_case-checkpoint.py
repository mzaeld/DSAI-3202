import random
import time

def generate_chars():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=1000))

def generate_numbers():
    return sum(random.randint(0, 100) for _ in range(1000))

def run_sequential():
    start_time = time.time()
    chars = generate_chars()
    numbers = generate_numbers()
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time:.5f} seconds")
    return end_time - start_time