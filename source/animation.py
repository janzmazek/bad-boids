"""
This module...
"""
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from source.boids import Boids

class Animation(object):
    """
    This class...
    """
    def __init__(self, config):
        self.x_axis = config['x_axis']
        self.y_axis = config['y_axis']
        self.frames = config['frames']
        self.interval = config['interval']
        self.boids = Boids(config)

        self.plot()

    def plot(self):
        """
        This method...
        """
        figure = plt.figure()
        axes = plt.axes(xlim=tuple(self.x_axis), ylim=tuple(self.y_axis))
        self.scatter = axes.scatter(
            self.boids.properties["x_coordinate"],
            self.boids.properties["y_coordinate"])
        FuncAnimation(figure, self.animate, frames=self.frames,
                      interval=self.interval)
        plt.show()

    def animate(self, frame):
        """
        This method...
        """
        self.boids.update()
        self.scatter.set_offsets(list(zip(
            self.boids.properties["x_coordinate"],
            self.boids.properties["y_coordinate"])))
