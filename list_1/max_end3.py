# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""


def max_end3(nums):
    max_value = max(nums[0], nums[len(nums) - 1])
    return [max_value] * 3


class TestMaxEnd3(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(max_end3([1, 2, 3]), [3, 3, 3])

    def test_case_01(self):
        self.assertEqual(max_end3([11, 5, 9]), [11, 11, 11])

    def test_case_02(self):
        self.assertEqual(max_end3([2, 11, 3]), [3, 3, 3])

    def test_case_03(self):
        self.assertEqual(max_end3([11, 3, 3]), [11, 11, 11])

    def test_case_04(self):
        self.assertEqual(max_end3([3, 11, 11]), [11, 11, 11])

    def test_case_05(self):
        self.assertEqual(max_end3([2, 2, 2]), [2, 2, 2])

    def test_case_06(self):
        self.assertEqual(max_end3([2, 11, 2]), [2, 2, 2])

    def test_case_07(self):
        self.assertEqual(max_end3([0, 0, 1]), [1, 1, 1])


if __name__ == "__main__":
    unittest.main()
