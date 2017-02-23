"""
This module creates an animation of boids.
"""
from matplotlib import pyplot as plt
from matplotlib import animation
from boids.boids import Boids

class Animation(object):
    """
    This class creates an animation based on the inputs specified in the config
    file.
    Parameters
    ----------
    config: yaml file with specified:
        - x_axis
        - y_axis
        - frames
        - interval
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
        This method plots the graph of boids.
        """
        figure = plt.figure()
        axes = plt.axes(xlim=tuple(self.x_axis), ylim=tuple(self.y_axis))
        self.scatter = axes.scatter(
            self.boids.properties["x_coordinate"],
            self.boids.properties["y_coordinate"])
        anim = animation.FuncAnimation(
            figure,
            self.animate,
            frames=self.frames,
            interval=self.interval)
        plt.show()

    def animate(self, frame):
        """
        This method updates the graph with the new coordinates of boids.
        """
        self.boids.update()
        self.scatter.set_offsets(list(zip(
            self.boids.properties["x_coordinate"],
            self.boids.properties["y_coordinate"])))
