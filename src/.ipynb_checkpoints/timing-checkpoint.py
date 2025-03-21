import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from src.square import square

def time_sequential(numbers):
    """Sequential computation using a for loop."""
    start = time.time()
    results = [square(n) for n in numbers]
    end = time.time()
    return results, end - start

def time_multiprocessing(numbers):
    start_time = time.time()
    processes = []
    results = []

    for n in numbers:
        p = multiprocessing.Process(target=lambda q, num: q.append(square(num)), args=(results, n))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    return results, end_time - start_time

def time_pool_map(numbers):
    """Multiprocessing using Pool.map() to distribute tasks."""
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    end = time.time()
    return results, end - start

#async
def time_pool_map_async(numbers):
    """Multiprocessing using Pool.map_async() for non-blocking execution."""
    start = time.time()
    with multiprocessing.Pool() as pool:
        result_obj = pool.map_async(square, numbers)
        results = result_obj.get()  # Waits for results
    end = time.time()
    return results, end - start
    
#sync

def time_pool_apply(numbers):
    """Multiprocessing using Pool.apply() for each number."""
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = [pool.apply(square, (n,)) for n in numbers]
    end = time.time()
    return results, end - start

#async
def time_pool_apply_async(numbers):
    """Multiprocessing using Pool.apply_async() for non-blocking execution."""
    start = time.time()
    with multiprocessing.Pool() as pool:
        result_objs = [pool.apply_async(square, (n,)) for n in numbers]
        results = [obj.get() for obj in result_objs]  # Collect results
    end = time.time()
    return results, end - start

def time_concurrent_futures(numbers):
    start_time = time.time()
    num_workers = min(8, multiprocessing.cpu_count())  # Set to 8 or available CPUs

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(square, numbers))

    end_time = time.time()
    return results, end_time - start_time
