import random
import multiprocessing
from src.square import square
from src.timing import (
    time_sequential,
    time_multiprocessing,
    time_pool_map,
    time_pool_apply,
    time_concurrent_futures,
    time_pool_map_async,
    time_pool_apply_async
)
from src.connection_pool import ConnectionPool
from src.database_operations import access_database

def run_multiprocessing_tests_6():
    """Run performance tests for multiprocessing techniques."""
    numbers = [random.randint(1, 100) for _ in range(10**6)]
    
    print("Timing sequential:")
    _, time_seq = time_sequential(numbers)
    print(f"Sequential time: {time_seq:.4f} seconds\n")
    '''
    print("Timing multiprocessing (one process per number):")
    _, time_multi = time_multiprocessing(numbers)
    print(f"Multiprocessing time: {time_multi:.4f} seconds\n")'''
    
    print("Timing Pool.map:")
    _, time_map = time_pool_map(numbers)
    print(f"Pool.map() time: {time_map:.4f} seconds\n")

    print("Timing Pool.map_async:")
    _, time_map_async = time_pool_map_async(numbers)
    print(f"Pool.map_async() time: {time_map_async:.4f} seconds\n")

    print("Timing Pool.apply:")
    _, time_apply = time_pool_apply(numbers)
    print(f"Pool.apply() time: {time_apply:.4f} seconds\n")

    print("Timing Pool.apply_async:")
    _, time_apply_async = time_pool_apply_async(numbers)
    print(f"Pool.apply_async() time: {time_apply_async:.4f} seconds\n")
    
    print("Timing concurrent.futures:")
    _, time_futures = time_concurrent_futures(numbers)
    print(f"ProcessPoolExecutor time: {time_futures:.4f} seconds\n")

def run_multiprocessing_tests_7():
    """Run performance tests for multiprocessing techniques."""
    numbers = [random.randint(1, 100) for _ in range(10**7)]
    
    print("Timing sequential:")
    _, time_seq = time_sequential(numbers)
    print(f"Sequential time: {time_seq:.4f} seconds\n")
    '''
    print("Timing multiprocessing (one process per number):")
    _, time_multi = time_multiprocessing(numbers)
    print(f"Multiprocessing time: {time_multi:.4f} seconds\n")'''
    
    print("Timing Pool.map:")
    _, time_map = time_pool_map(numbers)
    print(f"Pool.map() time: {time_map:.4f} seconds\n")

    print("Timing Pool.map_async:")
    _, time_map_async = time_pool_map_async(numbers)
    print(f"Pool.map_async() time: {time_map_async:.4f} seconds\n")
    
    print("Timing Pool.apply:")
    _, time_apply = time_pool_apply(numbers)
    print(f"Pool.apply_async() time: {time_apply:.4f} seconds\n")
'''
    print("Timing Pool.apply_async:")
    _, time_apply_async = time_pool_apply_async(numbers)
    print(f"Pool.apply_async() time: {time_apply_async:.4f} seconds\n")
    
    print("Timing concurrent.futures:")
    _, time_futures = time_concurrent_futures(numbers)
    print(f"ProcessPoolExecutor time: {time_futures:.4f} seconds\n")'''


def run_semaphore_test():
    """Run the semaphore-based connection pool test."""
    num_processes = 5  # Total processes trying to access the database
    max_connections = 2  # Only 2 connections available

    pool = ConnectionPool(max_connections)

    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=access_database, args=(pool, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

"""Here are the funtions that can be uncommented if needed to run"""
#run_multiprocessing_tests_6() #power 6
run_multiprocessing_tests_7() #power 7
#run_semaphore_test()
