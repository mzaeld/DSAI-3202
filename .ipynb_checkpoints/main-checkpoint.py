from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}  # Fixed quotes
    comm.send(data, dest=1, tag=11)
    print('On process 0, data sending:', data)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print('On process 1, data received:', data)  # Fixed print statement

