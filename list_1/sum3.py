# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints length 3, return the sum of all the elements.


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""


def sum3(nums):
    return sum(nums)


class TestSum3(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum3([1, 2, 3]), 6)

    def test_case_01(self):
        self.assertEqual(sum3([5, 11, 2]), 18)

    def test_case_02(self):
        self.assertEqual(sum3([7, 0, 0]), 7)

    def test_case_03(self):
        self.assertEqual(sum3([1, 2, 1]), 4)

    def test_case_04(self):
        self.assertEqual(sum3([1, 1, 1]), 3)

    def test_case_05(self):
        self.assertEqual(sum3([2, 7, 2]), 11)


if __name__ == "__main__":
    unittest.main()
