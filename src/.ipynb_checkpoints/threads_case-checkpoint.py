import time
import threading

def calculate_partial_sum(start, end, result, index):
    """
    Calculates the sum of integers from start to end and stores the result in a shared list.

    Arguments:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    result (list): A shared list to store partial sums.
    index (int): The index in the result list where the partial sum will be stored.
    """
    total = sum(range(start, end + 1))
    result[index] = total

def run_threads(n):
    """
    Executes the sum calculation using multiple threads.

    Arguments:
    n (int): The upper limit of the range for which the sum is calculated.

    Returns:
    float: The execution time taken to compute the sum using threading.
    """
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







     