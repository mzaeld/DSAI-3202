import time

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def run_sequential(n):
    
    start_time = time.time()
    total_sum_seq = calculate_sum(n)
    end_time = time.time()
    
    execution_time_seq = end_time - start_time

    print("sequential case: ")
    print(f"Sum: {total_sum_seq}")
    print(f"Execution Time: {execution_time_seq:.10f} seconds")
