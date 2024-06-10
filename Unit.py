import unittest
from even_checker import is_even


class TestEvenChecker(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

    def test_negative_even_number(self):
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-4))

    def test_negative_odd_number(self):
        self.assertFalse(is_even(-3))
        self.assertFalse(is_even(-5))


if __name__ == '__main__':
    unittest.main()
