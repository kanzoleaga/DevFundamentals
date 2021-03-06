import unittest

from shooting import Projectile, Position, Velocity


class ProjectileTest(unittest.TestCase):

	def test_projectile_is_created_with_initial_position(self):
		projectile = Projectile(Position(5, 25))

		self.assertTrue(isinstance(projectile, Projectile))

	# def test_position_changes_when_projectile_is_shoot(self):
    #
	# 	initial_position = Position()
	# 	projectile = Projectile(initial_position)
	# 	velocity = Velocity(Position(), Position(3, 5))
    #
	# 	projectile.shoot(velocity)
    #
	# 	self.assertTrue(isinstance(projectile.position(), Position))
	# 	self.assertNotEqual(initial_position, projectile.position())
    #
	# def test_projectile_shot_to_the_floor_should_remain_there(self):
	# 	initial_position = Position(5, 10)
	# 	projectile = Projectile(initial_position)
	# 	velocity = Velocity(Position(), Position(0, -1))
    #
	# 	projectile.shoot(velocity)
    #
	# 	self.assertEqual(Position(5, 0), projectile.position())

	def test_projectile_shot_with_a_given_angle_follows_a_parabolic_path(self):
		pass

	def test_projectile_shot_with_a_given_angle_follows_a_parabolic_path(self):
		projectile = Projectile(Position (0, 3))
		velocity = Velocity(Position(0, 3), Position(4, 6))
		projectile.shoot(velocity)
		self.assertEquals(Position(3, 0), projectile.position())

if __name__ == "__main__":
	unittest.main()

