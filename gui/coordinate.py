import matplotlib.pyplot as plt
from numpy import array


class Coordinate:

    def __init__(self, title: str, max_x, max_y):
        self.title = title
        self.max_x = max_x
        self.max_y = max_y
        self.coordinates = []

    def show(self):
        # Create a figure and set up the event listener
        fig, ax = plt.subplots()
        ax.set_title(self.title)
        fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.xlim(0, self.max_x)  # Adjust the limits according to your requirements
        plt.ylim(0, self.max_y)
        plt.grid(True)
        plt.show()

        # Convert the list of cities to a numpy array
        self.coordinates = array(self.coordinates)

    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            self.coordinates.append([event.xdata, event.ydata])
            plt.scatter(event.xdata, event.ydata, c='blue', marker='o')
            plt.text(event.xdata, event.ydata, str(len(self.coordinates) - 1), fontsize=12, ha='right')
            plt.draw()
