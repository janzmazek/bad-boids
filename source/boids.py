import random

class Boids(object):
    def __init__(self, config):
        self.config = config
        self.bird_number = self.config['bird_number']
        self.initialise()

    def initialise(self):
        x_interval = self.config['x_interval']
        y_interval = self.config['y_interval']
        x_velocity_interval = self.config['x_velocity_interval']
        y_velocity_interval = self.config['y_velocity_interval']
        # Starting  positions and velocities
        boids_x=[random.uniform(x_interval[0], x_interval[1]) for x in range(self.bird_number)]
        boids_y=[random.uniform(y_interval[0], y_interval[1]) for x in range(self.bird_number)]
        boid_x_velocities=[random.uniform(x_velocity_interval[0], x_velocity_interval[1]) for x in range(self.bird_number)]
        boid_y_velocities=[random.uniform(y_velocity_interval[0],y_velocity_interval[1]) for x in range(self.bird_number)]
        self.boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

    def update(self):
        attraction_coefficient = self.config['attraction_coefficient']
        reflection_limit = self.config['reflection_limit']
        speeding_limit = self.config['speeding_limit']
        speeding_coefficient = self.config['speeding_coefficient']

        xs,ys,xvs,yvs=self.boids
        # Fly towards the middle
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                xvs[i]=xvs[i]+(xs[j]-xs[i])*attraction_coefficient/self.bird_number
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                yvs[i]=yvs[i]+(ys[j]-ys[i])*attraction_coefficient/self.bird_number
        # Fly away from nearby boids
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < reflection_limit:
                    xvs[i]=xvs[i]+(xs[i]-xs[j])
                    yvs[i]=yvs[i]+(ys[i]-ys[j])
        # Try to match speed with nearby boids
        for i in range(self.bird_number):
            for j in range(self.bird_number):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < speeding_limit:
                    xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speeding_coefficient/self.bird_number
                    yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speeding_coefficient/self.bird_number
        # Move according to velocities
        for i in range(self.bird_number):
            xs[i]=xs[i]+xvs[i]
            ys[i]=ys[i]+yvs[i]
