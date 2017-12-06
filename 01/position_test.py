import unittest 
from shoting import Position 

class PositionTest (unittest.TestCase):
    def test_position_can_be_created_with_no_params (self):
        position = Position ()
        self.assertTrue(position != None)
    def test_position_with_no_params_corresponds_to_origin (self):
        position= Position()
        self.assertEqual (0, position.x())
        self.assertEqual(0, position.y())
    def test_position_can_be_created_with_x_and_y_params (self):
        position = Position(2,3)
        self.assertEqual(2, position.x())
        self.assertEqual(3, position.y())
    def test_distance_to_same_position_is_cero (self):
        position = Position(1,3)
        self.assertEqual(0, position.distance_to(position))
    def test_position_with_same_coordinates_are_equal (self):
        first_pos = Positon (1,2)
        second_pos = Positon(1, 2)
        self.assertTrue(first_pos == second_pos)
        

if __name__ == "__main__":
   unittest.main()

