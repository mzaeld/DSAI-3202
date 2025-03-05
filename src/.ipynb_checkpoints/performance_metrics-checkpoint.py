import time
from src.sequential_case import run_sequential
from src.threads_case import run_threads
from src.multiprocessing_case import run_multiprocessing

def compute_metrics(n):
    """
    Computes performance metrics for sequential, threading, and multiprocessing cases.

    Arguments:
    n (int): The upper limit of the range for which the sum is calculated.

    Prints:
    - Estimated parallelizable fraction (f) for threading and multiprocessing.
    - Speedup, efficiency, and speedup estimates using Amdahl's and Gustafson's laws for both cases.
    """
    # Sequential case
    start_seq = time.time()
    run_sequential(n)
    end_seq = time.time()
    T1 = end_seq - start_seq
    
    # Threading case
    start_thread = time.time()
    run_threads(n)
    end_thread = time.time()
    Tp_thread = end_thread - start_thread
    
    # Multiprocessing case
    start_process = time.time()
    run_multiprocessing(n)
    end_process = time.time()
    Tp_process = end_process - start_process
    
    p = 4  # Number of parallel units

    # Estimate f (parallelizable fraction)
    f_thread = (1 - (1 / (T1 / Tp_thread))) * p / (p - 1)
    f_process = (1 - (1 / (T1 / Tp_process))) * p / (p - 1)
    
    # Threading metrics
    speedup_thread = T1 / Tp_thread
    efficiency_thread = speedup_thread / p
    amdahl_speedup_thread = 1 / ((1 - f_thread) + (f_thread / p))
    gustafson_speedup_thread = p - (p - 1) * (1 - f_thread)
    
    # Multiprocessing metrics
    speedup_process = T1 / Tp_process
    efficiency_process = speedup_process / p
    amdahl_speedup_process = 1 / ((1 - f_process) + (f_process / p))
    gustafson_speedup_process = p - (p - 1) * (1 - f_process)
    
    # Display results
    print("Performance Metrics:")
    print(f"Estimated Parallelizable Fraction (Threads): {f_thread:.4f}")
    print(f"Speedup (Threads): {speedup_thread:.4f}")
    print(f"Efficiency (Threads): {efficiency_thread:.4f}")
    print(f"Amdahl's Law Speedup (Threads): {amdahl_speedup_thread:.4f}")
    print(f"Gustafson's Law Speedup (Threads): {gustafson_speedup_thread:.4f}")
    
    print(f"Estimated Parallelizable Fraction (Multiprocessing): {f_process:.4f}")
    print(f"Speedup (Multiprocessing): {speedup_process:.4f}")
    print(f"Efficiency (Multiprocessing): {efficiency_process:.4f}")
    print(f"Amdahl's Law Speedup (Multiprocessing): {amdahl_speedup_process:.4f}")
    print(f"Gustafson's Law Speedup (Multiprocessing): {gustafson_speedup_process:.4f}")




    
