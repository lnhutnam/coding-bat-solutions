# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""


def make_ends(nums):
    return (nums * 2, [nums[0], nums[len(nums) - 1]])[len(nums) > 1]


class TestMakeEnds(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_ends([1, 2, 3]), [1, 3])

    def test_case_01(self):
        self.assertEqual(make_ends([1, 2, 3, 4]), [1, 4])

    def test_case_02(self):
        self.assertEqual(make_ends([7, 4, 6, 2]), [7, 2])

    def test_case_03(self):
        self.assertEqual(make_ends([1, 2, 2, 2, 2, 2, 2, 3]), [1, 3])

    def test_case_04(self):
        self.assertEqual(make_ends([7, 4]), [7, 4])

    def test_case_05(self):
        self.assertEqual(make_ends([7]), [7, 7])

    def test_case_06(self):
        self.assertEqual(make_ends([5, 2, 9]), [5, 9])

    def test_case_07(self):
        self.assertEqual(make_ends([2, 3, 4, 1]), [2, 1])


if __name__ == "__main__":
    unittest.main()
