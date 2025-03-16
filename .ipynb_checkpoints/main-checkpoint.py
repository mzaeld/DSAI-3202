import time
import random
from src.square_functions import (
    sequential_squares, multiprocessing_squares,
    pool_map_squares, pool_apply_squares,
    pool_apply_async_squares, process_pool_executor_squares
)

def run_benchmark(numbers, label):
    """Runs all methods and prints execution times."""
    print(f"\n=== Benchmarking {label} ===")

    start = time.time()
    sequential_squares(numbers)
    print(f"Sequential: {time.time() - start:.4f} sec")

    start = time.time()
    multiprocessing_squares(numbers)
    print(f"Multiprocessing (one process per number): {time.time() - start:.4f} sec")

    start = time.time()
    pool_map_squares(numbers)
    print(f"Multiprocessing Pool (map, synchronous): {time.time() - start:.4f} sec")

    start = time.time()
    pool_apply_squares(numbers)
    print(f"Multiprocessing Pool (apply, synchronous): {time.time() - start:.4f} sec")

    start = time.time()
    pool_apply_async_squares(numbers)
    print(f"Multiprocessing Pool (apply_async, asynchronous): {time.time() - start:.4f} sec")

    start = time.time()
    process_pool_executor_squares(numbers)
    print(f"ProcessPoolExecutor (synchronous): {time.time() - start:.4f} sec")

if __name__ == "__main__":
    NUMBERS_1M = [random.randint(1, 100) for _ in range(10**6)]
    NUMBERS_10M = [random.randint(1, 100) for _ in range(10**7)]

    run_benchmark(NUMBERS_1M, "1,000,000 numbers")
    run_benchmark(NUMBERS_10M, "10,000,000 numbers")



        






