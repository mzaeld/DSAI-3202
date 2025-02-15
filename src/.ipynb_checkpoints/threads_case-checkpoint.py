import threading
import time
import random
import string
# Function to join a thousand random letters
def join_random_letters(start = 0, end = 1000):
    letters = [random.choice(string.ascii_letters) for _ in range(start,end)]
    joined_letters = ''.join(letters)
    print("Joined Letters Task Done")
# Function to add a thousand random numbers
def add_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(1000)]
    total_sum = sum(numbers)
    print("Add Numbers Task Done")
# Measure the total time for both operations
def run_threads():
    total_start_time = time.time()
    # Create threads for both functions
    starts
    thread_letters_1 = threading.Thread(target=join_random_letters)
    thread_letters_2 = threading.Thread(target=join_random_letters)
    #thread_numbers_1 = threading.Thread(target=add_random_numbers)
    #thread_numbers_2 = threading.Thread(target=add_random_numbers)
    # Start the threads
    thread_letters_1.start()
    thread_letters_2.start()
    #thread_numbers_1.start()
    #thread_numbers_2.start()
    # Wait for all threads to complete
    thread_letters_1.join()
    thread_letters_2.join()
    total_end_time = time.time()
    print(f"Total time taken for threads: {total_end_time - total_start_time} seconds")



     