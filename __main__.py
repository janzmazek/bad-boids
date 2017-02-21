from matplotlib import pyplot as plt
from matplotlib import animation
import yaml
from source.boids import Boids

with open("source/config.yaml", "r") as file:
    config = yaml.load(file)
x_axis = config['x_axis']
y_axis = config['y_axis']
frames = config['frames']
interval = config['interval']


def animate(frame):
   boids.update()
   scatter.set_offsets(list(zip(boids.boids[0],boids.boids[1])))

if __name__ == "__main__":
    boids = Boids()
    figure=plt.figure()
    axes=plt.axes(xlim=(x_axis[0], x_axis[1]), ylim=(y_axis[0], y_axis[1]))
    scatter=axes.scatter(boids.boids[0],boids.boids[1])
    anim = animation.FuncAnimation(figure, animate,
                                   frames=frames, interval=interval)
    plt.show()
