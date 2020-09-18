"""
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.

For example test case:
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
import unittest


def sum_double(a, b):
    return ((a+b), 2*(a+b))[a == b]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum_double(1, 2), 3)

    def test_case_01(self):
        self.assertEqual(sum_double(3, 2), 5)

    def test_case_02(self):
        self.assertEqual(sum_double(2, 2), 8)

    def test_case_03(self):
        self.assertEqual(sum_double(-1, 0), -1)

    def test_case_04(self):
        self.assertEqual(sum_double(3, 3), 12)

    def test_case_05(self):
        self.assertEqual(sum_double(0, 0), 0)

    def test_case_06(self):
        self.assertEqual(sum_double(0, 1), 1)

    def test_case_07(self):
        self.assertEqual(sum_double(3, 4), 7)


if __name__ == '__main__':
    unittest.main()
