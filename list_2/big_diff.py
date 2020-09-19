# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""


def big_diff(nums):
    return max(nums) - min(nums)


class TestBigDiff(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(big_diff([10, 3, 5, 6]), 7)

    def test_case_01(self):
        self.assertEqual(big_diff([7, 2, 10, 9]), 8)

    def test_case_02(self):
        self.assertEqual(big_diff([2, 10, 7, 2]), 8)

    def test_case_03(self):
        self.assertEqual(big_diff([2, 10]), 8)

    def test_case_04(self):
        self.assertEqual(big_diff([10, 2]), 8)

    def test_case_05(self):
        self.assertEqual(big_diff([10, 0]), 10)

    def test_case_06(self):
        self.assertEqual(big_diff([2, 3]), 1)

    def test_case_07(self):
        self.assertEqual(big_diff([2, 2]), 0)

    def test_case_08(self):
        self.assertEqual(big_diff([2]), 0)

    def test_case_09(self):
        self.assertEqual(big_diff([5, 1, 6, 1, 9, 9]), 8)

    def test_case_10(self):
        self.assertEqual(big_diff([7, 6, 8, 5]), 3)

    def test_case_11(self):
        self.assertEqual(big_diff([7, 7, 6, 8, 5, 5, 6]), 3)


if __name__ == "__main__":
    unittest.main()
