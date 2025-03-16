import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def square(n):
    """Computes the square of a number."""
    return n * n

def sequential_squares(numbers):
    """Computes squares sequentially using a for-loop."""
    return [square(n) for n in numbers]

def multiprocessing_squares(numbers):
    """Computes squares using a separate process for each number."""
    processes = []
    results = multiprocessing.Manager().list()  # Shared list for results

    def worker(n, results):
        results.append(square(n))  # Append result to shared list

    for n in numbers:
        p = multiprocessing.Process(target=worker, args=(n, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(results)

def pool_map_squares(numbers):
    """Synchronous: Uses multiprocessing.Pool with map()."""
    with multiprocessing.Pool() as pool:
        return pool.map(square, numbers)

def pool_apply_squares(numbers):
    """Synchronous: Uses multiprocessing.Pool with apply()."""
    with multiprocessing.Pool() as pool:
        return [pool.apply(square, args=(n,)) for n in numbers]

def pool_apply_async_squares(numbers):
    """Asynchronous: Uses multiprocessing.Pool with apply_async()."""
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(square, args=(n,)) for n in numbers]
        return [r.get() for r in results]  # Collect results after processing

def process_pool_executor_squares(numbers):
    """Uses concurrent.futures.ProcessPoolExecutor."""
    with ProcessPoolExecutor() as executor:
        return list(executor.map(square, numbers))

