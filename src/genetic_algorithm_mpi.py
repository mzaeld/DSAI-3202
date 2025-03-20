from mpi4py import MPI
import time
import numpy as np
import pandas as pd
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start_time = time.time()

# Rank 0 loads the distance matrix and distributes it
distance_matrix = None
if rank == 0:
    distance_matrix = pd.read_csv('city_distances.csv').to_numpy()

distance_matrix = comm.bcast(distance_matrix, root=0)  # Broadcast to all ranks

# Parameters
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_generations = 200
mutation_rate = 0.1
stagnation_limit = 5
infeasible_penalty = 1e6
num_tournaments = 4

# Rank 0 generates the initial population and distributes it
population = None
if rank == 0:
    population = generate_unique_population(population_size, num_nodes)

# Split population among processes
split_population = np.array_split(population, size) if rank == 0 else None
local_population = comm.scatter(split_population, root=0)

best_calculate_fitness = int(1e6)
stagnation_counter = 0

# Main GA loop
for generation in range(num_generations):
    # Evaluate fitness locally
    local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])

    # Gather fitness values at Rank 0
    all_fitness_values = comm.gather(local_fitness_values, root=0)
    if rank == 0:
        all_fitness_values = np.concatenate(all_fitness_values)
        current_best_calculate_fitness = np.min(all_fitness_values)
        if current_best_calculate_fitness < best_calculate_fitness:
            best_calculate_fitness = current_best_calculate_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # Regenerate population if stagnation occurs
        if stagnation_counter >= stagnation_limit:
            print(f"Regenerating at generation {generation}")
            best_individual = population[np.argmin(all_fitness_values)]
            population = generate_unique_population(population_size - 1, num_nodes)
            population.append(best_individual)
            stagnation_counter = 0
            split_population = np.array_split(population, size)
    
    # Broadcast stagnation status
    stagnation_counter = comm.bcast(stagnation_counter, root=0)

    # Each process selects parents and performs crossover
    local_selected = select_in_tournament(local_population, local_fitness_values)
    local_offspring = []
    for i in range(0, len(local_selected), 2):
        parent1, parent2 = local_selected[i], local_selected[i + 1]
        child = [0] + order_crossover(parent1[1:], parent2[1:])
        local_offspring.append(child)
    
    # Apply mutation
    local_mutated_offspring = [mutate(route, mutation_rate) for route in local_offspring]

    # Gather offspring at Rank 0
    all_offspring = comm.gather(local_mutated_offspring, root=0)

    if rank == 0:
        all_offspring = [item for sublist in all_offspring for item in sublist]  # Flatten list
        # Replace worst individuals
        worst_indices = np.argsort(all_fitness_values)[-len(all_offspring):]
        for i, idx in enumerate(worst_indices):
            population[idx] = all_offspring[i]

        # Split population again
        split_population = np.array_split(population, size)

    # Scatter updated population to all processes
    local_population = comm.scatter(split_population, root=0)

    if rank == 0:
        print(f"Generation {generation}: Best calculate_fitness = {current_best_calculate_fitness}")

# Final gather to determine best solution
local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])
all_fitness_values = comm.gather(local_fitness_values, root=0)
all_population = comm.gather(local_population, root=0)

if rank == 0:
    all_fitness_values = np.concatenate(all_fitness_values)
    all_population = [item for sublist in all_population for item in sublist]
    best_idx = np.argmin(all_fitness_values)
    best_solution = all_population[best_idx]
    best_distance = all_fitness_values[best_idx]

    end_time = time.time()
    execution_time = end_time - start_time

    print("Best Solution:", best_solution)
    print("Total Distance:", best_distance)
    print(f"Execution Time: {execution_time:.4f} seconds")
