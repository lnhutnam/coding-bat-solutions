"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""

import unittest


def makes10(a, b):
    return (False, True)[(a == 10) or (b == 10) or (a + b == 10)]


class Testing(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(makes10(9, 10), True)

    def test_case_01(self):
        self.assertEqual(makes10(9, 9), False)

    def test_case_02(self):
        self.assertEqual(makes10(1, 9), True)

    def test_case_03(self):
        self.assertEqual(makes10(10, 1), True)

    def test_case_04(self):
        self.assertEqual(makes10(10, 10), True)

    def test_case_05(self):
        self.assertEqual(makes10(8, 2), True)

    def test_case_06(self):
        self.assertEqual(makes10(8, 3), False)

    def test_case_07(self):
        self.assertEqual(makes10(10, 42), True)

    def test_case_00(self):
        self.assertEqual(makes10(12, -2), True)


if __name__ == "__main__":
    unittest.main()
