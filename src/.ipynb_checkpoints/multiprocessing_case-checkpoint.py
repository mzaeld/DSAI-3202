import time
import multiprocessing

def calculate_partial_sum(start, end, result, lock):
    partial_sum = sum(range(start, end + 1))
    with lock: 
        result.value += partial_sum

def run_multiprocessing(n):
    num_processes = 4  # Number of processes to use
    
    processes = []
    result = multiprocessing.Value('d', 0.0) 
    lock = multiprocessing.Lock()  
    chunk_size = n // num_processes
    
    start_time = time.time()
    
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else n
        process = multiprocessing.Process(target=calculate_partial_sum, args=(start, end, result, lock))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    total_sum_multiprocess = result.value
    end_time = time.time()
    
    execution_time_multiprocess = end_time - start_time
    print("multiprocess case: ")
    print(f"Sum: {int(total_sum_multiprocess)}")
    print(f"Execution Time: {execution_time_multiprocess:.10f} seconds")
    return total_sum_multiprocess
