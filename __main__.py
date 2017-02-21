from matplotlib import pyplot as plt
from matplotlib import animation

import random

bird_number = 50
x_interval = [-450.0, 50.0]
y_interval = [300.0, 600.0]
x_velocity_interval = [0.0, 10.0]
y_velocity_interval = [-20.0, 20.0]
attraction_coefficient = 0.01
reflection_limit = 100
speeding_limit = 10000
speeding_coeficient = 0.125
x_axis = (-500, 1500)
y_axis = (-500, 1500)
frames = 200
interval = 50

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
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speeding_coeficient/bird_number
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speeding_coeficient/bird_number
    # Move according to velocities
    for i in range(bird_number):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=x_axis, ylim=y_axis)
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
