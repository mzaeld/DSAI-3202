import time
import random
import string
# Function to join a thousand random letters
def join_random_letters():
    letters = [random.choice(string.ascii_letters) for _ in range(1000)]
    joined_letters = ''.join(letters)
    return joined_letters
# Function to add a thousand random numbers
def add_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(1000)]
    total_sum = sum(numbers)
    return total_sum
def run_sequential(start = 0, end_letters = 100000, num_numbers = 100000):
    # Measure the total time for both operations
    total_start_time = time.time()
    join_random_letters(start_letters, end_letters)
    add_random_numbers()
    total_end_time = time.time()
    print(f"Total time taken for sequential: {total_end_time - total_start_time} seconds")
