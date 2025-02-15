from src.sequential_case import *
from src.threads_case import *
from src.multiprocessing_case import *
from src.performance_metrics import *

n = int(input("Enter a large number: "))
run_sequential(n)
run_threads(n)
run_multiprocessing(n)
calculate_performance_metrics(T_seq, T_thread, T_process, 4, 4)