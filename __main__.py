import yaml
from source.animation import Animation

if __name__ == "__main__":
    with open("source/config.yaml", "r") as file:
        config = yaml.load(file)
    Animation(config)
