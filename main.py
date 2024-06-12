import objects.cities
import objects.cities_genetic as ga
from gui.coordinate import Coordinate
import utils.graphics as graph
import numpy as np


if __name__ == '__main__':
    #cities_coordinate = np.array([[0, 0], [1, 5], [2, 3], [4, 7], [6, 2], [8, 6], [7, 1], [3, 8], [5, 5], [9, 0]])
    cities_coordinate = Coordinate("Select cities coordinates", 20, 20)
    cities_coordinate.show()
    cities = objects.cities.Cities(cities_coordinate.coordinates)
    #cities = objects.cities.Cities(cities_coordinate)
    #cities.show_cities_plot()
    cities.calculate_distance_matrix()
    #cities.show_distance_matrix_plot()

    population_size = 15 * cities.num_cities
    tournament_size = 3
    mutation_rate = 0.15
    generations = 1000
    stagnation_limit = 30
    crossover_rate = 0.9
    ga_retry = 10

    best_fitness = float('inf')
    best_index = None
    cities_ga_list = []
    for i in range(0, ga_retry):
        cities_ga = ga.CitiesGenetic(population_size, cities, tournament_size, mutation_rate, generations,
                                     stagnation_limit, crossover_rate, False)
        cities_ga.evolve()
        cities_ga_list.append(cities_ga)
        print(f"{i}: {cities_ga.best_fitness} ({cities_ga.gen} generation)")
        if cities_ga.best_fitness < best_fitness:
            best_fitness = cities_ga.best_fitness
            best_index = i

    graph.show_routes(cities_ga_list, 0.18)
    #cities_ga_list[best_index].show_best_route(0.18)
    #cities_ga_list[best_index].show_fitness_history()