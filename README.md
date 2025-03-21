#description
This repository is for parallel and distributed computing for DSAI3202

This is Assignment 1

Part I:
Results(10^6):
- Sequential time: 0.0577 seconds
- Pool.map() time: 0.3486 seconds
- Pool.map_async() time: 0.3656 seconds
- Pool.apply_async() time: 35.5076 seconds
- Pool.apply() time: 145.0094 seconds
- ProcessPoolExecutor time: 135.0321 seconds


• What are your conclusions?
- The multiprocessing for loop has an error, and that is due to too many processes for the OS to handle.
- Pool.map is still the fastest compared to the the other types even faster than the async and that is because of the scheduling and overhead differences.
- In the meantime, the pool.apply_async is much faster than the pool.apply
  
• Redo the test with 10^7 numbers.
Results(10^7):
Sequential time: 0.5513 seconds
Pool.map() time: 1.6743 seconds
Pool.map_async() time: 1.6024 seconds

• Test both synchronous and asynchronous versions in the pool.
• What are your conclusions?
- When tested with 10^7 numbers, the code for apply, apply_async and concurrent.futures got killed and that is because due too big
of a workload that causes the OS to forcely kill them. 



Semaphores:
What happens if more processes try to access the pool than there are available
connections?
- If there are more processes than the available connections they will have to wait until a connection is released. In my case, I put max_connections as 2 whilst the number of processes are 5 so that means when the 2 processes uses the the connections then the other 3 will wait until the connection is released.

How does the semaphore prevent race conditions and ensure safe access to the
connections?
- The semaphore it organizes and prevents conflicts by acting as a controller, it uses the acquire() and release() to prevent race conditions.
- They use acquire as a requesting access, if connections available then it will gets access and if they are not available the processes will have to wait.
- They use the release() to free the connections when the processes is done with the connections.






Part II:
• Explain the program outlined in the script genetic_algorithm_trial.py
- This script solves the Traveling Salesman Problem (TSP) using a Genetic Algorithm (GA) to find the shortest path between cities. It starts by reading a distance file (city_distances.csv) and creating a bunch of random routes. Each route is checked to see how good it is (based on total distance), and the best ones are picked to create new routes using Tournament Selection. Order Crossover mixes routes from two parents, while Mutation makes small random changes to keep things interesting. Bad routes are replaced with better ones to keep improving. If progress stops for too long, the algorithm resets most of the population but keeps the best route. After repeating this process for many generations, it prints the shortest route found, how far it is, and how long it took to run.

• Define the parts to be distributed and parallelized, explain your choices 
- Distance Matrix Distribution : Rank 0 loads & broadcasts the matrix to all processes.
- Population Distribution : Rank 0 generates & scatters population among processes.
- Fitness Evaluation : Each process independently computes fitness for its subset.
- Fitness Gathering : Gathered at Rank 0 to track progress & detect stagnation.
- Selection, Crossover & Mutation : Done locally within each process.
- Offspring Gathering & Replacement : Rank 0 gathers offspring, replaces weakest, and redistributes.

• What improvements do you propose? Add them to your code.
- Independent Local Processing : Each process generates its own population instead of waiting for Rank 0.
- No Frequent Synchronization : Less data gathering/scattering, reducing communication overhead.
- Local Selection, Crossover & Mutation : Each process fully handles its genetic operations independently.
- Less Rank 0 Dependency : No centralized control except for final results gathering.
- Stagnation Handling Improved : Instead of redistributing, each process regenerates its own population when needed.
• After adding your improvements, recompute the performance metrics and compare with before the enhancements.

•How would you add more cars to the problem?
- Change route representation: Each car should have its own route rather than one long route
- Crossover: Swap subroutes between cars instead of swapping city within the route
- Mutation: Reassigning the cities between vehiclesv instead of changing order within the route
- One city per vehicle

Results(using the extended csv):
mpi: Execution Time: 65.0891 seconds
mpi_improved - Execution Time: 13.2652 seconds


