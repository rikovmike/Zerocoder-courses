import unittest

from AT01.main import safe_mod


class TestSafeMod(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(safe_mod(10, 3), 1)
        self.assertEqual(safe_mod(15, 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(safe_mod(-10, 3), 2)  # -10 % 3 = 2 (т.к. -10 = 3*(-4) + 2)
        self.assertEqual(safe_mod(10, -3), -2)  # 10 % -3 = -2 (т.к. 10 = -3*(-4) + (-2))
        self.assertEqual(safe_mod(-7, -3), -1) # -7 % -3 = -1 (т.к. -7 = -3*2 + (-1))

    def test_float_numbers(self):
        self.assertAlmostEqual(safe_mod(10.5, 3), 1.5)
        self.assertAlmostEqual(safe_mod(-10.5, 3), 1.5)

    def test_zero_dividend(self):
        self.assertEqual(safe_mod(0, 5), 0)

    def test_zero_divisor(self):
        self.assertIsNone(safe_mod(5, 0))
        self.assertIsNone(safe_mod(0, 0))

if __name__ == '__main__':
    unittest.main()