import random
import matplotlib.pyplot as plt
import numpy as np
import objects.cities


class CitiesGenetic:
    def __init__(self, population_size, cities: objects.cities.Cities, tournament_size, mutation_rate, generations,
                 stagnation_limit, crossover_rate, show_progress = False):
        self.population_size = population_size
        self.cities = cities
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.stagnation_limit = stagnation_limit
        self.population = self.generate_population()
        self.population_fitness = None
        self.best_fitness_history = []
        self.best_route = None
        self.best_fitness = None
        self.show_progress = show_progress
        self.gen = 0

    def generate_individual(self):
        return np.random.permutation(self.cities.num_cities)

    def generate_population(self):
        return [self.generate_individual() for _ in range(self.population_size)]

    def fitness(self):
        self.population_fitness = []
        for individual in self.population:
            route_sum = sum(self.cities.distance_matrix[individual[i], individual[i + 1]] for i in range(self.cities.num_cities - 1))
            self.population_fitness.append(route_sum)

    def selection(self):
        selected = random.sample(list(zip(self.population, self.population_fitness)), self.tournament_size)
        selected.sort(key=lambda x: x[1])
        return selected[0][0]

    @staticmethod
    def crossover(parent1, parent2):
        size = len(parent1)
        child = [-1] * size
        start, end = sorted(random.sample(range(size), 2))
        child[start:end] = parent1[start:end]
        fill_pos = end
        for i in range(end, end + size):
            city = parent2[i % size]
            if city not in child:
                child[fill_pos % size] = city
                fill_pos += 1
        return child

    @staticmethod
    def mutate(individual):
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]
        return individual

    def evolve(self):
        best_fitness = float('inf')
        stagnation_counter = 0

        for gen in range(self.generations):
            self.fitness()

            new_population = []
            for _ in range(self.population_size):
                if random.random() < self.crossover_rate:
                    parent1 = self.selection()
                    parent2 = self.selection()
                    child = self.crossover(parent1, parent2)
                else:
                    child = self.selection()

                if random.random() < self.mutation_rate:
                    child = self.mutate(child)

                new_population.append(child)

            self.population = new_population
            current_best_fitness = min(self.population_fitness)
            self.best_fitness_history.append(best_fitness)
            worst_fitness = max(self.population_fitness)

            if gen % 5 == 0 and self.show_progress:
                print(f"Generation {gen}, Best Fitness: {current_best_fitness}, Worst Fitness: {worst_fitness}")

            if current_best_fitness < best_fitness:
                best_fitness = current_best_fitness
                stagnation_counter = 0
            else:
                stagnation_counter += 1

            if stagnation_counter >= self.stagnation_limit:
                if self.show_progress:
                    print(f"Terminating early at generation {gen} due to stagnation.")
                break
            self.gen += 1

        self.best_route = self.population[np.argmin(self.fitness())]
        self.best_fitness = self.population_fitness[np.argmin(self.fitness())]

    def show_best_route(self, offset= 0):
        print(f"Best Fitness: {self.best_fitness}")
        print(f"Best Route: {self.best_route}")
        plt.figure(figsize=(10, 6))
        for i in range(self.cities.num_cities):
            if i < self.cities.num_cities - 1:
                plt.plot([self.cities.cities[self.best_route[i + 1], 0], self.cities.cities[self.best_route[i], 0]],
                        [self.cities.cities[self.best_route[i + 1], 1], self.cities.cities[self.best_route[i], 1]],
                        'bo-')
            plt.text(self.cities.cities[self.best_route[i], 0] + offset, self.cities.cities[self.best_route[i], 1] + offset,
                     str(self.best_route[i]), fontsize=12, ha='center')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Best Route')
        plt.show()

    def show_fitness_history(self):
        plt.plot(self.best_fitness_history)
        plt.xlabel('Generations')
        plt.ylabel('Best Fitness')
        plt.title('Fitness Over Generations')
        plt.show()