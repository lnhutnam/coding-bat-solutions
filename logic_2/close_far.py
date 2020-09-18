# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""

import unittest


def close_far(a, b, c):
    return (abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2 or abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2)


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(close_far(1, 2, 10), True)

    def test_case_01(self):
        self.assertEqual(close_far(1, 2, 3), False)

    def test_case_02(self):
        self.assertEqual(close_far(4, 1, 3), True)

    def test_case_03(self):
        self.assertEqual(close_far(4, 5, 3), False)

    def test_case_04(self):
        self.assertEqual(close_far(4, 3, 5), False)

    def test_case_05(self):
        self.assertEqual(close_far(-1, 10, 0), True)

    def test_case_06(self):
        self.assertEqual(close_far(0, -1, 10), True)

    def test_case_07(self):
        self.assertEqual(close_far(10, 10, 8), True)

    def test_case_08(self):
        self.assertEqual(close_far(10, 8, 9), False)

    def test_case_09(self):
        self.assertEqual(close_far(8, 9, 10), False)

    def test_case_10(self):
        self.assertEqual(close_far(8, 9, 7), False)

    def test_case_11(self):
        self.assertEqual(close_far(8, 6, 9), True)


if __name__ == "__main__":
    unittest.main()
