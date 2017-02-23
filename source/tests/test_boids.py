import unittest
from source.boids import Boids

class TestBoids(unittest.TestCase):
    config = {
        "x_coordinates_interval": (-100, 100),
        "y_coordinates_interval": (-200, 200),
        "x_velocities_interval": (-300, 300),
        "y_velocities_interval": (-400, 400),
        "number_of_birds": 10,
        "cohesion_limit": 10000,
        "cohesion_constant": 0.125,
        "alignment_constant": 0.01,
        "separation_limit": 100}

    def test_properties(self):
        boids = Boids(TestBoids.config)
        self.assertTrue(type(boids.properties) is dict)
        self.assertEqual(len(boids.properties), 4)
        self.assertEqual(len(boids.properties["x_coordinate"]),
                         TestBoids.config["number_of_birds"])

    def test_update(self):
        boids = Boids(TestBoids.config)
        boids.update()
        self.assertTrue(type(boids.properties) == dict)

    def test_distance(self):
        boids = Boids(TestBoids.config)
        self.assertTrue(boids.distance(0, 1) > 0)
        self.assertTrue(boids.distance(0, 0) == 0)
        self.assertTrue(type(boids.distance(0, 1)) is float)

    def test_correct_velocities(self):
        boids = Boids(TestBoids.config)
        old_x_coordinates = boids.properties["x_coordinate"][:]
        old_y_coordinates = boids.properties["y_coordinate"][:]
        old_x_velocities = boids.properties["x_velocity"][:]
        old_y_velocities = boids.properties["y_velocity"][:]
        boids.correct_velocities(0, 1)
        new_x_coordinates = boids.properties["x_coordinate"][:]
        new_y_coordinates = boids.properties["y_coordinate"][:]
        new_x_velocities = boids.properties["x_velocity"][:]
        new_y_velocities = boids.properties["y_velocity"][:]
        self.assertListEqual(old_x_coordinates, new_x_coordinates)
        self.assertListEqual(old_y_coordinates, new_y_coordinates)
        self.assertListEqual(old_x_velocities[1:], new_x_velocities[1:])
        self.assertListEqual(old_y_velocities[1:], new_y_velocities[1:])
        self.assertFalse(old_x_velocities[0] == new_x_velocities[0])
        self.assertFalse(old_y_velocities[0] == new_y_velocities[0])

    def test_correct_coordinates(self):
        boids = Boids(TestBoids.config)
        old_x_coordinates = boids.properties["x_coordinate"][:]
        old_y_coordinates = boids.properties["y_coordinate"][:]
        old_x_velocities = boids.properties["x_velocity"][:]
        old_y_velocities = boids.properties["y_velocity"][:]
        boids.correct_coordinates(0)
        new_x_coordinates = boids.properties["x_coordinate"][:]
        new_y_coordinates = boids.properties["y_coordinate"][:]
        new_x_velocities = boids.properties["x_velocity"][:]
        new_y_velocities = boids.properties["y_velocity"][:]
        self.assertListEqual(old_x_velocities, new_x_velocities)
        self.assertListEqual(old_y_velocities, new_y_velocities)
        self.assertListEqual(old_x_coordinates[1:], new_x_coordinates[1:])
        self.assertListEqual(old_y_coordinates[1:], new_y_coordinates[1:])
        self.assertFalse(old_x_coordinates[0] == new_x_coordinates[0])
        self.assertFalse(old_y_coordinates[0] == new_y_coordinates[0])
