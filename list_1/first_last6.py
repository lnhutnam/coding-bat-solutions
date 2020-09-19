# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""


def first_last6(nums):
    return (False, True)[nums[0] == 6 or nums[len(nums) - 1] == 6]


class TestFirstLast6(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(first_last6([1, 2, 6]), True)

    def test_case_01(self):
        self.assertEqual(first_last6([6, 1, 2, 3]), True)

    def test_case_02(self):
        self.assertEqual(first_last6([13, 6, 1, 2, 3]), False)

    def test_case_03(self):
        self.assertEqual(first_last6([3, 2, 1]), False)

    def test_case_04(self):
        self.assertEqual(first_last6([3, 6, 1]), False)

    def test_case_05(self):
        self.assertEqual(first_last6([3, 6]), True)

    def test_case_06(self):
        self.assertEqual(first_last6([6]), True)

    def test_case_07(self):
        self.assertEqual(first_last6([3]), False)

    def test_case_08(self):
        self.assertEqual(first_last6([5, 6]), True)

    def test_case_09(self):
        self.assertEqual(first_last6([5, 5]), False)

    def test_case_10(self):
        self.assertEqual(first_last6([1, 2, 3, 4, 6]), True)

    def test_case_11(self):
        self.assertEqual(first_last6([1, 2, 3, 4]), False)


if __name__ == "__main__":
    unittest.main()
