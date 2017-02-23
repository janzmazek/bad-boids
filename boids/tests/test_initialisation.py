import unittest
from boids.initialisation import Initialisation

class TestInitialisation(unittest.TestCase):
    config = {
        "x_coordinates_interval": (-100, 100),
        "y_coordinates_interval": (-200, 200),
        "x_velocities_interval": (-300, 300),
        "y_velocities_interval": (-400, 400),
        "number_of_birds": 10}

    def test_get_properties(self):
        properties = Initialisation(TestInitialisation.config).get_properties()
        self.assertTrue(type(properties) is dict)
        self.assertEqual(len(properties), 4)
        self.assertTrue("x_coordinate" in properties and
                        "y_coordinate" in properties and
                        "x_velocity" in properties and
                        "y_velocity" in properties)
        self.assertEqual(len(properties["x_coordinate"]),
                         TestInitialisation.config["number_of_birds"])

    def test_randomise(self):
        init = Initialisation(TestInitialisation.config)
        self.assertTrue(type(init.randomise((0, 1))) is list)
        self.assertEqual(len(init.randomise((0, 1))),
                         TestInitialisation.config["number_of_birds"])
        self.assertTrue(max(init.randomise((-100, 100))) <= 100)
        self.assertTrue(min(init.randomise((-100, 100))) >= -100)
