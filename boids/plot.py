import yaml
from boids.animation import Animation
import os

def plot():
    config = None
    # Check local package directory and global system directory for conf file
    for loc in os.curdir, os.path.join(os.curdir, 'bad-boids'), "/etc/bad-boids":
        try:
            with open(os.path.join(loc, 'config.yaml')) as source:
                config = yaml.load(source)
        except IOError:
            pass
    Animation(config)
