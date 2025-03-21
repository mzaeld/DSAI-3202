import numpy as np

def initialize_population(population_size, rank):
    population = np.zeros(population_size)
    if rank == 0:
        infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
        population[infected_indices] = 1
    return population

def spread_virus(population, spread_chance, vaccination_rate):
    new_population = population.copy()
    for i in range(len(population)):
        if population[i] == 1:  # If the person is infected
            for j in range(len(population)):
                if population[j] == 0 and np.random.rand() < spread_chance:
                    # A person gets infected if they are unvaccinated and the infection chance is met
                    if np.random.rand() > vaccination_rate:
                        new_population[j] = 1
    return new_population
