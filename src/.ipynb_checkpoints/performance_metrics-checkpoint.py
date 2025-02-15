from src.sequential_case import *
from src.threads_case import *
from src.multiprocessing_case import *

def calculate_dynamic_f(T_seq, T_thread):
    return 1 - (T_seq - T_thread) / T_seq if T_seq > 0 else 0

def calculate_performance_metrics(T_seq, T_thread, T_process, num_threads, num_processes):
    f = calculate_dynamic_f(T_seq, T_thread)
    S_thread = T_seq / T_thread
    S_process = T_seq / T_process
    E_thread = S_thread / num_threads
    E_process = S_process / num_processes
    S_Amdahl_thread = 1 / ((1 - f) + (f / num_threads))
    S_Amdahl_process = 1 / ((1 - f) + (f / num_processes))
    S_Gustafson_thread = num_threads - (num_threads - 1) * (1 - f)
    S_Gustafson_process = num_processes - (num_processes - 1) * (1 - f)
    
    return {
        "Parallel Fraction (f)": f,
        "Speedup (Threading)": S_thread,
        "Speedup (Multiprocessing)": S_process,
        "Efficiency (Threading)": E_thread,
        "Efficiency (Multiprocessing)": E_process,
        "Amdahl's Speedup (Threading)": S_Amdahl_thread,
        "Amdahl's Speedup (Multiprocessing)": S_Amdahl_process,
        "Gustafson's Speedup (Threading)": S_Gustafson_thread,
        "Gustafson's Speedup (Multiprocessing)": S_Gustafson_process
    }
