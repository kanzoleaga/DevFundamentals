import unittest
from  isPrime import is_prime

class PrimeTest (unittest.TestCase):
    def Setup (self):
        self.x = 5
    def test_5_is_prime (self):
        self.assertTrue(is_prime(5))
    def test_5_is_prime (self):
        self.assertTrue(is_prime(5))

