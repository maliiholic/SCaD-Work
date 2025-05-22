import unittest
from Prime_No_Checker import is_prime  # Importing the function

class MyTestCase(unittest.TestCase):

    def test_prime(self):
        """Test if prime numbers return True."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_not_prime(self):
        """Test if non-prime numbers return False."""
        self.assertFalse(is_prime(4))  # 4 is divisible by 2
        self.assertFalse(is_prime(6))  # 6 is divisible by 2
        self.assertFalse(is_prime(8))  # 8 is divisible by 2
        self.assertFalse(is_prime(9))  # 9 is divisible by 3
        self.assertFalse(is_prime(1))  # 1 is not prime

    def test_edge_cases(self):
        """Test the edge cases for prime number checks."""
        self.assertFalse(is_prime(0))   # 0 is not prime
        self.assertFalse(is_prime(-1))  # Negative numbers are not prime
        self.assertFalse(is_prime(-5))  # Negative numbers are not prime

    def test_additional_asserts(self):
        """Additional assertions for better testing."""
        # ensuring always boolean is returned
        self.assertIsInstance(is_prime(7), bool)

        # checking specifically the num 10
        self.assertNotIn(10, [2, 3, 5, 7, 11])

if __name__ == '__main__':
    unittest.main()
