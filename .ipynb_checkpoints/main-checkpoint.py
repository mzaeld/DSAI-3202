from src.sequential_case import *
from src.threads_case import *
from src.multiprocessing_case import *

se_time =run_sequential()
te_time = run_threads()
mpe_time = run_multiprocessing()

parallel_fraction = 0.9  # Fraction of code that is parallelizable

t_speedup = se_time / te_time
mp_speedup = se_time / mpe_time
t_efficiency = t_speedup / 2
mp_efficiency = t_speedup / 2
t_parallel_fraction = 1 - ((se_time - te_time) / se_time)
mp_parallel_fraction = 1 - ((se_time - mpe_time) / se_time)
t_amdahl = 1 / ((1 - t_parallel_fraction) + (t_parallel_fraction / 2))
mp_amdahl = 1 / ((1 - mp_parallel_fraction) + (mp_parallel_fraction / 2))
t_gustafson = 2 - (1 - t_parallel_fraction) * (2 - 1)
mp_gustafson = 2 - (1 - mp_parallel_fraction) * (2 - 1)

print("THREADING:")
print(f"Speedup: {t_speedup:.5f}")
print(f"Efficiency: {t_efficiency:.5f}")
print(f"Amdahl's Speedup: {t_amdahl:.5f}")
print(f"Gustafson's Speedup: {t_gustafson:.5f}")

print("MULTIPROCESSING:")
print(f"Speedup: {mp_speedup:.5f}")
print(f"Efficiency: {mp_efficiency:.5f}")
print(f"Amdahl's Speedup: {mp_amdahl:.5f}")
print(f"Gustafson's Speedup: {mp_gustafson:.5f}")
