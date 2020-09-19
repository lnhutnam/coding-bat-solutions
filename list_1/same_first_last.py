# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""


def same_first_last(nums):
    if (len(nums) == 0):
        return False
    return (((False, True)[nums[0] == nums[len(nums) - 1]], True)[len(nums) == 1], False)[len(nums) == 0]


class TestSameFirstLast(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(same_first_last([1, 2, 3]), False)

    def test_case_01(self):
        self.assertEqual(same_first_last([1, 2, 3, 1]), True)

    def test_case_02(self):
        self.assertEqual(same_first_last([1, 2, 1]), True)

    def test_case_03(self):
        self.assertEqual(same_first_last([7]), True)

    def test_case_04(self):
        self.assertEqual(same_first_last([]), False)

    def test_case_05(self):
        self.assertEqual(same_first_last([1, 2, 3, 4, 5, 1]), True)

    def test_case_06(self):
        self.assertEqual(same_first_last([1, 2, 3, 4, 5, 13]), False)

    def test_case_07(self):
        self.assertEqual(same_first_last([13, 2, 3, 4, 5, 13]), True)

    def test_case_08(self):
        self.assertEqual(same_first_last([7, 7]), True)


if __name__ == "__main__":
    unittest.main()
