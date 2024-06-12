import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Cities:
    def __init__(self, cities: np.ndarray):
        self.cities = cities
        self.distance_matrix = None
        self.num_cities = len(cities)

    def show_cities_plot(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.cities[:, 0], self.cities[:, 1], c='blue', marker='o')
        for i, (x, y) in enumerate(self.cities):
            plt.text(x, y, str(i), fontsize=12, ha='right')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Cities')
        plt.grid(True)
        plt.show()

    def calculate_distance_matrix(self):
        self.distance_matrix = np.zeros((self.num_cities, self.num_cities))
        for x in range(self.num_cities):
            for y in range(self.num_cities):
                self.distance_matrix[x][y] = np.linalg.norm(self.cities[x] - self.cities[y])

    def show_distance_matrix_plot(self):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.distance_matrix, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=range(self.num_cities),
                    yticklabels=range(self.num_cities))
        plt.xlabel('City Index')
        plt.ylabel('City Index')
        plt.title('Distance Matrix Heatmap')
        plt.show()
