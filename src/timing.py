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

'''def time_multiprocessing(numbers):
    """Multiprocessing with a separate process for each number."""
    start = time.time()
    with multiprocessing.Pool(processes=len(numbers)) as pool:
        results = pool.map(square, numbers)
    end = time.time()
    return results, end - start'''
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

def time_pool_apply(numbers):
    """Multiprocessing using Pool.apply() for each number."""
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = [pool.apply(square, (n,)) for n in numbers]
    end = time.time()
    return results, end - start

'''def time_concurrent_futures(numbers):
    """Multiprocessing using concurrent.futures.ProcessPoolExecutor."""
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))
    end = time.time()
    return results, end - start

def time_concurrent_futures(numbers):
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))

    end_time = time.time()
    return results, end_time - start_time'''

def time_concurrent_futures(numbers):
    start_time = time.time()
    num_workers = min(8, multiprocessing.cpu_count())  # Set to 8 or available CPUs

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(square, numbers))

    end_time = time.time()
    return results, end_time - start_time
