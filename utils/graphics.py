import matplotlib.pyplot as plt


def show_routes(gas, offset=0):
    fig, axs = plt.subplots(2, 5, figsize=(20, 10))
    #axs.flatten()
    x = 0
    y = 0
    for i, ga in enumerate(gas):
        axs[x, y].set_title(f"Route {i}: {ga.best_fitness}")
        for j in range(ga.cities.num_cities):
            if j < ga.cities.num_cities - 1:
                axs[x, y].plot([ga.cities.cities[ga.best_route[j + 1], 0], ga.cities.cities[ga.best_route[j], 0]],
                         [ga.cities.cities[ga.best_route[j + 1], 1], ga.cities.cities[ga.best_route[j], 1]],
                         'bo-')
            axs[x, y].text(ga.cities.cities[ga.best_route[j], 0] + offset, ga.cities.cities[ga.best_route[j], 1] + offset,
                     str(ga.best_route[j]), fontsize=12, ha='center')
        axs[x, y].set_xlabel('X Coordinate')
        axs[x, y].set_ylabel('Y Coordinate')
        axs[x, y].grid(True)

        if i >= 4:
            y = i - 4
            x = 1
        else:
            y += 1

    plt.tight_layout()
    plt.show()
