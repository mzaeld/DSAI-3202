import time
import threading

def calculate_partial_sum(start, end, result, index):
    total = sum(range(start, end + 1))
    result[index] = total

def run_threads(n):
    num_threads = 4  # Number of threads to use
    
    threads = []
    result = [0] * num_threads  # Shared list to store results
    chunk_size = n // num_threads
    
    start_time = time.time()
    
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=calculate_partial_sum, args=(start, end, result, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    total_sum_thread = sum(result)
    end_time = time.time()
    
    execution_time_thread = end_time - start_time

    print("threads case: ")
    print(f"Sum: {total_sum_thread}")
    print(f"Execution Time: {execution_time_thread:.10f} seconds")
    return execution_time_thread






     