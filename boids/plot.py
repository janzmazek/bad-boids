import yaml
from boids.animation import Animation
import os

def plot():
    with open("boids/config.yaml", "r") as file:
        config = yaml.load(file)
    Animation(config)
