# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)


class TestCenterdAverage(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(centered_average([1, 2, 3, 4, 100]), 3)

    def test_case_01(self):
        self.assertEqual(centered_average([1, 1, 5, 5, 10, 8, 7]), 5)

    def test_case_02(self):
        self.assertEqual(centered_average([-10, -4, -2, -4, -2, 0]), -3)

    def test_case_03(self):
        self.assertEqual(centered_average([5, 3, 4, 6, 2]), 4)

    def test_case_04(self):
        self.assertEqual(centered_average([5, 3, 4, 0, 100]), 4)

    def test_case_05(self):
        self.assertEqual(centered_average([100, 0, 5, 3, 4]), 4)

    def test_case_06(self):
        self.assertEqual(centered_average([4, 0, 100]), 4)

    def test_case_07(self):
        self.assertEqual(centered_average([0, 2, 3, 4, 100]), 3)

    def test_case_08(self):
        self.assertEqual(centered_average([1, 1, 100]), 1)

    def test_case_09(self):
        self.assertEqual(centered_average([7, 7, 7]), 7)

    def test_case_10(self):
        self.assertEqual(centered_average([1, 7, 8]), 7)

    def test_case_11(self):
        self.assertEqual(centered_average([1, 1, 99, 99]), 50)

    def test_case_12(self):
        self.assertEqual(centered_average([1000, 0, 1, 99]), 50)

    def test_case_13(self):
        self.assertEqual(centered_average([4, 4, 4, 4, 5]), 4)

    def test_case_14(self):
        self.assertEqual(centered_average([4, 4, 4, 1, 5]), 4)

    def test_case_15(self):
        self.assertEqual(centered_average([6, 4, 8, 12, 3]), 6)


if __name__ == "__main__":
    unittest.main()
