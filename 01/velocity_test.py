import unittest
from ./shoting import *

class Velocity (unittest.TestCase):
    def test_create_velocity_with_two_positions (self):
        start_position = Position()
        end_position = Position(3,4)
        velocity= Velocity (start_position, end_position)
        self.assertIsNotNone(velocity)
    def test_magnitude_is_zero_if_start_and_end_points_are_the_same (self):
        position = Position (1, 1)
        velocity = Velocity(position,position)
        self.assertEquals (0, velocity.magnitude())

    def test_magnitude_of_velocity_is_given_by_pythagoras_theorem (self):
        start_postion = Position ()
        end_postion = Positon (4,5)
        velocity = Velocity (start_postion, end_postion)
        self. assertEquals (5, velocity.magnitude())
    def test_angle_of_velocity_is_45_if_x_and_y_of_end_postion_are_the_same (self)
        start_postion = Position ()
        end_position = Position (2,2)
        velocity = Velocity (start_postion, end_position)
        self.assertEquals (45, velocity.angle())
    def test_angle_of_velocity_is 

if __name__ == "__main__":
    unittest.main ()

