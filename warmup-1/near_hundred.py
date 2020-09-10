"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

import unittest


def near_hundred(n):
    return (abs(100 - n) < 10) or (abs(200 - n) < 10)


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(near_hundred(93), True)

    def test_case_01(self):
        self.assertEqual(near_hundred(90), True)

    def test_case_02(self):
        self.assertEqual(near_hundred(89), False)

if __name__ == "__main__":
    unittest.main()
