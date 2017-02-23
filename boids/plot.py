import yaml
from boids.animation import Animation

def plot():
    with open("boids/config.yaml", "r") as file:
        config = yaml.load(file)
    Animation(config)
