"""
This module...
"""
import random

class Initialisation(object):
    """
    This class...
    """
    def __init__(self, config):
        self.x_coordinates_interval = config['x_coordinates_interval']
        self.y_coordinates_interval = config['y_coordinates_interval']
        self.x_velocities_interval = config['x_velocities_interval']
        self.y_velocities_interval = config['y_velocities_interval']
        self.number_of_birds = config["number_of_birds"]

    def get_properties(self):
        """
        This method...
        """
        # Starting  positions and velocities
        x_coordinate = self.randomise(self.x_coordinates_interval)
        y_coordinate = self.randomise(self.y_coordinates_interval)
        x_velocity = self.randomise(self.x_velocities_interval)
        y_velocity = self.randomise(self.y_velocities_interval)
        return {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
            "x_velocity": x_velocity,
            "y_velocity": y_velocity}

    def randomise(self, interval):
        """
        This method...
        """
        return [random.uniform(*interval) for i in range(self.number_of_birds)]
