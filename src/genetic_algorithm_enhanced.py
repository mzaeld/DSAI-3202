from mpi4py import MPI
import time
import numpy as np
import pandas as pd
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population
"""
Parallel Genetic Algorithm for Solving the Traveling Salesman Problem (TSP) using MPI.

This program implements a genetic algorithm to find an optimal route for the TSP.
It distributes the computation across multiple processes using MPI for parallel execution.

Features:
- Uses genetic algorithm operators (selection, crossover, mutation) to evolve solutions.
- Parallelized with MPI for performance improvement.
- Handles population stagnation by regenerating new individuals.
- Collects and distributes fitness values across processes to maintain synchronization.

Parameters:
- population_size: Number of individuals in the population.
- num_generations: Number of generations to evolve the population.
- mutation_rate: Probability of mutation for offspring.
- stagnation_limit: Number of generations without improvement before regenerating population.

Inputs:
- city_distances_extended.csv: Distance matrix of cities for the TSP.

Outputs:
- Best solution found.
- Total distance of the best solution.
- Execution time of the algorithm.

"""

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start_time = time.time()

# Load the distance matrix
distance_matrix = pd.read_csv('city_distances_extended.csv').to_numpy()

# Parameters
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_tournaments = 4
mutation_rate = 0.1
num_generations = 200
infeasible_penalty = 1e6
stagnation_limit = 5

np.random.seed(42 + rank)  # Different seed for each process

# Split population among processes
local_population_size = population_size // size
population = generate_unique_population(local_population_size, num_nodes)

best_fitness = int(1e6)
stagnation_counter = 0

# Main GA loop
for generation in range(num_generations):
    # Each process evaluates fitness for its subset of the population
    fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
    
    # Gather fitness values from all processes
    all_fitness_values = np.empty(population_size, dtype=np.float64) if rank == 0 else None
    comm.Gather(fitness_values, all_fitness_values, root=0)
    
    if rank == 0:
        # Find global best fitness
        current_best_fitness = np.min(all_fitness_values)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1
        
        # Broadcast best fitness to all processes
        best_idx = np.argmin(all_fitness_values)
    else:
        current_best_fitness = None
        best_idx = None
    
    current_best_fitness = comm.bcast(current_best_fitness, root=0)
    best_idx = comm.bcast(best_idx, root=0)

    if stagnation_counter >= stagnation_limit:
        if rank == 0:
            print(f"Regenerating population at generation {generation} due to stagnation")
        population = generate_unique_population(local_population_size, num_nodes)
        stagnation_counter = 0
        continue
    
    # Selection, crossover, and mutation (done locally on each process)
    selected = select_in_tournament(population, fitness_values)
    offspring = []
    for i in range(0, len(selected), 2):
        parent1, parent2 = selected[i], selected[i + 1]
        route1 = order_crossover(parent1[1:], parent2[1:])
        offspring.append([0] + route1)
    
    mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

    # Replace the worst individuals with new offspring
    sorted_indices = np.argsort(fitness_values)[::-1][:len(mutated_offspring)]
    for i, idx in enumerate(sorted_indices):
        population[idx] = mutated_offspring[i]
    
    print(f"Rank {rank} - Generation {generation}: Best Fitness = {current_best_fitness}")

# Gather final population from all processes
final_population = comm.gather(population, root=0)
final_fitness_values = comm.gather(fitness_values, root=0)

if rank == 0:
    # Flatten lists
    final_population = [ind for sublist in final_population for ind in sublist]
    final_fitness_values = np.concatenate(final_fitness_values)
    
    best_idx = np.argmin(final_fitness_values)
    best_solution = final_population[best_idx]
    best_distance = final_fitness_values[best_idx]
    
    end_time = time.time()
    execution_time = end_time - start_time

    print("Best Solution:", best_solution)
    print("Total Distance:", best_distance)
    print(f"Execution Time: {execution_time:.4f} seconds")
