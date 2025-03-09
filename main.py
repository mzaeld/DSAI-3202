from mpi4py import MPI
import numpy as np
from src.square import square
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size() #number of processes
results = None
print(f'Which process is this {rank}, and the size is {size}')

if rank == 0:
    numbers = np.arange(size,dtype = 'i')
else: 
    numbers = None
print(numbers)

number = np.zeros(1,dtype = 'i') #creates vectors of zeros with dimension of 1
comm.Scatter(numbers,number,root = 0) # distributing the numbers to all the processes
print(numbers)
print(number)

result = square(number[0])
print(result)
time.sleep(random.randint(1,10))
request = comm.isend(result,dest=0,tag = rank)


if rank == 0:
    results = np.zeros(size,dtype = 'i')
    for i in range(size):
        results[i] = comm.irecv(source = i,tag = i).wait()
    print(f'The results are: {results}')
    
request.wait()

        






