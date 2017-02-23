# bad-boids
The second assignment for the Research Software Engineering with Python module at UCL. This Python package creates a boids model, which simulates the flocking behaviour of birds. The model's parameters can be modified in the configuration file "config.yaml" in the boids directory of the package.

## Installation
The package can be installed using pip:
```bash
pip install git+git://github.com/janzmazek/bad-boids.git
```
or if you want a local copy of the repository
```bash
git clone https://github.com/janzmazek/bad-boids.git
```
```bash
python setup.py install
```

## Usage
The package can be run using command line with command bad-boids.

Example:
```bash
greengraph --from “Ljubljana” --to “London” --steps 50 --out “plot.png”
