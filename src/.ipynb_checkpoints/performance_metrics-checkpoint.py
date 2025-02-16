import time
from src.sequential_case import run_sequential
from src.threads_case import run_threads
from src.multiprocessing_case import run_multiprocessing

def compute_metrics(n):
    # Run sequential case
    start_seq = time.time()
    run_sequential(n)
    end_seq = time.time()
    T1 = end_seq - start_seq
    
    # Run threading case
    start_thread = time.time()
    run_threads(n)
    end_thread = time.time()
    Tp_thread = end_thread - start_thread
    
    # Run multiprocessing case
    start_process = time.time()
    run_multiprocessing(n)
    end_process = time.time()
    Tp_process = end_process - start_process
    
    p = 4  # Number of threads/processes
    f = 0.9  # Assumed parallelizable fraction
    
    # Compute metrics
    speedup_thread = T1 / Tp_thread
    efficiency_thread = speedup_thread / p
    amdahl_speedup = 1 / ((1 - f) + (f / p))
    gustafson_speedup = p - (p - 1) * (1 - f)
    
    speedup_process = T1 / Tp_process
    efficiency_process = speedup_process / p
    
    print("Performance Metrics:")
    print(f"Speedup (Threads): {speedup_thread:.4f}")
    print(f"Efficiency (Threads): {efficiency_thread:.4f}")
    print(f"Amdahl's Law Speedup: {amdahl_speedup:.4f}")
    print(f"Gustafson's Law Speedup: {gustafson_speedup:.4f}")
    print(f"Speedup (Multiprocessing): {speedup_process:.4f}")
    print(f"Efficiency (Multiprocessing): {efficiency_process:.4f}")
    }
