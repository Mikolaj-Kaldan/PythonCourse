import unittest
import math
from Python import Vector

class TestVector(unittest.TestCase):  

    def setUp(self):
        self.v = Vector(1, 2, 3)
        self.w = Vector(2, -3, 2)

    def test_ne(self):
        self.assertNotEqual(self.v, self.w)

    def test_add(self):
        self.assertEqual(self.v + self.w, Vector(3, -1, 5))

    def test_diff(self):
        self.assertEqual(self.v - self.w, Vector(-1, 5, 1))

    def test_dot(self):
        self.assertEqual(self.v * self.w, 2)

    def test_cross(self):
        self.assertEqual(self.v.cross(self.w), Vector(13, 4, -7))

    def test_length(self):
        self.assertEqual(self.v.length(),  math.sqrt(14))

    def tearDown(self):
        print("cleaning")

if __name__ == "__main__":
    unittest.main()
