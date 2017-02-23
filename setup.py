from setuptools import setup, find_packages

setup(
      name = "Bad-boids",
      version = "1.0.0",
      description = "Boids simulation",
      author = "Jan Zmazek",
      url = "https://github.com/janzmazek/bad-boids",
      license = "MIT License",
      packages = find_packages(exclude=['*test']),
      scripts = ['scripts/bad-boids'],
      data_files = [('/etc/bad-boids' ,['config.yaml'])],
      install_requires = ['argparse', 'matplotlib']
)
