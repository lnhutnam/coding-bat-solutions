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
    pass


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(close_far(1, 2, 10), True)

    def test_case_00(self):
        self.assertEqual(close_far(1, 2, 10), True)

    def test_case_00(self):
        self.assertEqual(close_far(1, 2, 10), True)


if __name__ == "__main__":
    unittest.main()


