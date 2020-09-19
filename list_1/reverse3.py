# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""


def reverse3(nums):
    nums.reverse()
    return nums


class TestReverse3(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(reverse3([1, 2, 3]), [3, 2, 1])

    def test_case_01(self):
        self.assertEqual(reverse3([5, 11, 9]), [9, 11, 5])

    def test_case_02(self):
        self.assertEqual(reverse3([7, 0, 0]), [0, 0, 7])

    def test_case_03(self):
        self.assertEqual(reverse3([2, 1, 2]), [2, 1, 2])

    def test_case_04(self):
        self.assertEqual(reverse3([1, 2, 1]), [1, 2, 1])

    def test_case_05(self):
        self.assertEqual(reverse3([2, 11, 3]), [3, 11, 2])

    def test_case_06(self):
        self.assertEqual(reverse3([0, 6, 5]), [5, 6, 0])

    def test_case_07(self):
        self.assertEqual(reverse3([7, 2, 3]), [3, 2, 7])


if __name__ == "__main__":
    unittest.main()
