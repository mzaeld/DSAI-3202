from src.square import square
from src.timing import (
    time_sequential,
    time_multiprocessing,
    time_pool_map,
    time_pool_apply,
    time_concurrent_futures
)
import random

def main():
    numbers = [random.randint(1, 100) for _ in range(10**6)]
    
    print("Timing sequential:")
    _, time_seq = time_sequential(numbers)
    print(f"Sequential time: {time_seq:.4f} seconds\n")
    
    '''print("Timing multiprocessing (one process per number):")
    _, time_multi = time_multiprocessing(numbers)  # Limited for performance
    print(f"Multiprocessing time: {time_multi:.4f} seconds\n")'''
    
    print("Timing Pool.map:")
    _, time_map = time_pool_map(numbers)
    print(f"Pool.map() time: {time_map:.4f} seconds\n")
    
    '''print("Timing Pool.apply:")
    _, time_apply = time_pool_apply(numbers)  # Limited for performance
    print(f"Pool.apply() time: {time_apply:.4f} seconds\n")'''
    
    print("Timing concurrent.futures:")
    _, time_futures = time_concurrent_futures(numbers)
    print(f"ProcessPoolExecutor time: {time_futures:.4f} seconds\n")
    
if __name__ == "__main__":
    main()
