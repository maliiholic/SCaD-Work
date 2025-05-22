import unittest
from calculator import add,subtract,multiply,divide

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,8),11)
        self.assertEqual(add(-1,1),0)
        self.assertIsInstance((add(3,8)),int,float)

    def test_subtract(self):
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(0,3),-3)

    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(multiply(0,3),0)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)
        self.assertAlmostEqual(divide(10,3),3.3333, places=4)

        with self.assertRaises(ValueError):
            divide(10,0)
if __name__ == '__main__':
    unittest.main()
