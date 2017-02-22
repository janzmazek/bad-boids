"""
This module...
"""
import random

class Boids(object):
    """
    This class...
    """
    def __init__(self, config):
        self.config = config
        self.number_of_birds = self.config['number_of_birds']
        self.properties = self.initialise()

    def initialise(self):
        """
        This method...
        """
        x_coordinates_interval = self.config['x_coordinates_interval']
        y_coordinates_interval = self.config['y_coordinates_interval']
        x_velocities_interval = self.config['x_velocities_interval']
        y_velocities_interval = self.config['y_velocities_interval']
        # Starting  positions and velocities
        x_coordinate = self.randomise(x_coordinates_interval)
        y_coordinate = self.randomise(y_coordinates_interval)
        x_velocity = self.randomise(x_velocities_interval)
        y_velocity = self.randomise(y_velocities_interval)
        return {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
            "x_velocity": x_velocity,
            "y_velocity": y_velocity}

    def update(self):
        """
        This method...
        """
        alignment_constant = self.config['alignment_constant']/self.number_of_birds
        separation_limit = self.config['separation_limit']
        cohesion_limit = self.config['cohesion_limit']
        cohesion_constant = self.config['cohesion_constant']/self.number_of_birds
        birds = range(self.number_of_birds)

        # Fly towards the middle
        for bird_i in birds:
            for bird_j in birds:
                self.correct(bird_i, bird_j, alignment_constant)
        # Fly away from nearby boids
        for bird_i in birds:
            for bird_j in birds:
                if self.distance(bird_i, bird_j) < separation_limit:
                    self.correct(bird_i, bird_j)
        # Try to match speed with nearby boids
        for bird_i in birds:
            for bird_j in birds:
                if self.distance(bird_i, bird_j) < cohesion_limit:
                    self.correct(bird_i, bird_j, cohesion_constant)
        # Move according to velocities
        for bird in birds:
            x_velocity = self.properties["x_velocity"][bird]
            y_velocity = self.properties["y_velocity"][bird]
            self.properties["x_coordinate"][bird] += x_velocity
            self.properties["y_coordinate"][bird] += y_velocity

    def randomise(self, interval):
        """
        This method...
        """
        return [random.uniform(*interval) for i in range(self.number_of_birds)]

    def distance(self, bird_1, bird_2):
        """
        This method...
        """
        x_coordinate = self.properties["x_coordinate"]
        y_coordinate = self.properties["y_coordinate"]
        x_distance = (x_coordinate[bird_1]-x_coordinate[bird_2])**2
        y_distance = (y_coordinate[bird_1]-y_coordinate[bird_2])**2
        return x_distance + y_distance

    def correct(self, bird_1, bird_2, constant=1):
        """
        This method...
        """
        x_coordinate = self.properties["x_coordinate"]
        y_coordinate = self.properties["y_coordinate"]
        x_displacement = (x_coordinate[bird_2] - x_coordinate[bird_1])*constant
        y_displacement = (y_coordinate[bird_2] - y_coordinate[bird_1])*constant
        self.properties["x_velocity"][bird_1] += x_displacement
        self.properties["y_velocity"][bird_1] += y_displacement
