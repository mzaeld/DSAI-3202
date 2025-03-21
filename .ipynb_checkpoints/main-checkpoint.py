from mpi4py import MPI
import numpy as np
from src.square import square
import time
import random
from src.virus_simulation import initialize_population, spread_virus

def part1():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()  # Number of processes
    
    # Define the range of numbers (up to 1e8)
    N = int(1e8)  
    chunk_size = N // size  
    start = rank * chunk_size
    end = (rank + 1) * chunk_size if rank != size - 1 else N 
    

    local_numbers = np.arange(start + 1, end + 1, dtype=np.int64)  
    local_squares = np.array([square(x) for x in local_numbers], dtype=np.int64)
    
    if rank == 0:
        results = np.zeros(N, dtype=np.int64)  # Create space for full results
    
    comm.Gather(local_squares, results if rank == 0 else None, root=0)
    
  
    if rank == 0:
        print(f"Size of final array: {len(results)}")
        print(f"Last square value: {results[-1]}")


"""seond part of the lab"""
def part2():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    population_size = 1000
    spread_chance = 0.3  
    vaccination_rate = np.random.uniform(0.1, 0.5)  
   
    population = initialize_population(population_size, rank)
    
   
    num_steps = 10
    for step in range(num_steps):
        population = spread_virus(population, spread_chance, vaccination_rate)
    

        if rank != 0:
            comm.send(population, dest=0)
        else:
           
            for i in range(1, size):
                received_data = comm.recv(source=i)
                population += received_data
    
    total_infected = np.sum(population)
    infection_rate = total_infected / population_size
    print(f"Process {rank} Infection Rate: {infection_rate}")

print("#####PART 1#####")
part1()
print("#####PART 2#####")
part2()
