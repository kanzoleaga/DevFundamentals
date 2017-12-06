import unittest
from shoting import *


class velocity_test (unittest.TestCase):
    def test_create_velocity_with_two_positions (self):
        start_position = Position()
        end_position = Position(3,4)
        velocity= Velocity (start_position, end_position)
        self.assertIsNotNone(velocity)

    def test_magnitude_is_zero_if_start_and_end_points_are_the_same (self):
        position = Position (1, 1)
        velocity = Velocity(position, position)
        self.assertEqual (0, velocity.magnitude())

    def test_magnitude_of_velocity_is_given_by_pythagoras_theorem (self):
        start_postion = Position ()
        end_postion = Position (4,5)
        velocity = Velocity (start_postion, end_postion)
        self. assertEqual (6.40, velocity.magnitude())

    def test_angle_of_velocity_is_45_if_x_and_y_of_end_postion_are_the_same (self):
        start_postion = Position ()
        end_position = Position (2,2)
        velocity = Velocity (start_postion, end_position)
        self.assertEqual (45, velocity.angle())

    def test_angle_of_velocity_is_given_by_arct_function (self):
        start_positon = Position ()
        end_position = Position (16,4)
        velocity = Velocity (start_positon, end_position)
        self.assertEqual (14.04, velocity.angle())

if __name__ == "__main__":
    unittest.main ()

