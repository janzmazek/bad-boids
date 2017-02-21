from matplotlib import pyplot as plt
from matplotlib import animation
import yaml
import random

with open("source/config.yaml", "r") as file:
    config = yaml.load(file)
bird_number = config['bird_number']
x_interval = config['x_interval']
y_interval = config['y_interval']
x_velocity_interval = config['x_velocity_interval']
y_velocity_interval = config['y_velocity_interval']
attraction_coefficient = config['attraction_coefficient']
reflection_limit = config['reflection_limit']
speeding_limit = config['speeding_limit']
speeding_coefficient = config['speeding_coefficient']
x_axis = config['x_axis']
y_axis = config['y_axis']
frames = config['frames']
interval = config['interval']

# Starting  positions and velocities
boids_x=[random.uniform(x_interval[0], x_interval[1]) for x in range(bird_number)]
boids_y=[random.uniform(y_interval[0], y_interval[1]) for x in range(bird_number)]
boid_x_velocities=[random.uniform(x_velocity_interval[0], x_velocity_interval[1]) for x in range(bird_number)]
boid_y_velocities=[random.uniform(y_velocity_interval[0],y_velocity_interval[1]) for x in range(bird_number)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(bird_number):
        for j in range(bird_number):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*attraction_coefficient/bird_number
    for i in range(bird_number):
        for j in range(bird_number):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*attraction_coefficient/bird_number
    # Fly away from nearby boids
    for i in range(bird_number):
        for j in range(bird_number):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < reflection_limit:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(bird_number):
        for j in range(bird_number):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < speeding_limit:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speeding_coefficient/bird_number
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speeding_coefficient/bird_number
    # Move according to velocities
    for i in range(bird_number):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(x_axis[0], x_axis[1]), ylim=(y_axis[0], y_axis[1]))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
