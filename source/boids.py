import yaml
import random

class Boids(object):
    def __init__(self, config_file_name="source/config.yaml"):
        with open(config_file_name, "r") as file:
            config = yaml.load(file)
        self.bird_number = config['bird_number']
        x_interval = config['x_interval']
        y_interval = config['y_interval']
        x_velocity_interval = config['x_velocity_interval']
        y_velocity_interval = config['y_velocity_interval']
        self.attraction_coefficient = config['attraction_coefficient']
        self.reflection_limit = config['reflection_limit']
        self.speeding_limit = config['speeding_limit']
        self.speeding_coefficient = config['speeding_coefficient']

        # Starting  positions and velocities
        boids_x=[random.uniform(x_interval[0], x_interval[1]) for x in range(self.bird_number)]
        boids_y=[random.uniform(y_interval[0], y_interval[1]) for x in range(self.bird_number)]
        boid_x_velocities=[random.uniform(x_velocity_interval[0], x_velocity_interval[1]) for x in range(self.bird_number)]
        boid_y_velocities=[random.uniform(y_velocity_interval[0],y_velocity_interval[1]) for x in range(self.bird_number)]
        self.boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

    def update(self):
        xs,ys,xvs,yvs=self.boids
        # Fly towards the middle
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                xvs[i]=xvs[i]+(xs[j]-xs[i])*self.attraction_coefficient/self.bird_number
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                yvs[i]=yvs[i]+(ys[j]-ys[i])*self.attraction_coefficient/self.bird_number
        # Fly away from nearby boids
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < self.reflection_limit:
                    xvs[i]=xvs[i]+(xs[i]-xs[j])
                    yvs[i]=yvs[i]+(ys[i]-ys[j])
        # Try to match speed with nearby boids
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < self.speeding_limit:
                    xvs[i]=xvs[i]+(xvs[j]-xvs[i])*self.speeding_coefficient/self.bird_number
                    yvs[i]=yvs[i]+(yvs[j]-yvs[i])*self.speeding_coefficient/self.bird_number
        # Move according to velocities
        for i in range(self.bird_number):
            xs[i]=xs[i]+xvs[i]
            ys[i]=ys[i]+yvs[i]
