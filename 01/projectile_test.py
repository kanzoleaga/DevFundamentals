import  unittest
from shoting import Projectile, Position, Velocity

class ProjectileTest (unittest.TestCase):
    def test_projectile_is_created_with_initial_position (self):
        projectile = Projectile(Position(5,25))
        self.assertTrue(isinstance(projectile, Projectile))
    def test_position_changes_when_projectile_is_shoot (self):
        inital_position = Position()
        projectile = Projectile(inital_position)

        velocity = Velocity(Position(), Position(3,5))
        projectile.shoot(velocity)
        self.assertTrue(isinstance(projectile.position(), Position))
        self.assertNotEqual(Position(), projectile.position())

if __name__ == "__main__":
    unittest.main ()
