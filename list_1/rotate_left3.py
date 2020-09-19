# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""


def rotate_left3(nums):
    saved = nums[0]
    nums.remove(nums[0])
    nums.append(saved)
    return nums


class TestRotateLeft3(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(rotate_left3([1, 2, 3]), [2, 3, 1])

    def test_case_01(self):
        self.assertEqual(rotate_left3([5, 11, 9]), [11, 9, 5])

    def test_case_02(self):
        self.assertEqual(rotate_left3([7, 0, 0]), [0, 0, 7])

    def test_case_03(self):
        self.assertEqual(rotate_left3([1, 2, 1]), [2, 1, 1])

    def test_case_04(self):
        self.assertEqual(rotate_left3([0, 0, 1]), [0, 1, 0])


if __name__ == "__main__":
    unittest.main()
