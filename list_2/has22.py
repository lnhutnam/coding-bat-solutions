# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


class TestHas22(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(has22([1, 2, 2]), True)

    def test_case_01(self):
        self.assertEqual(has22([1, 2, 1, 2]), False)

    def test_case_02(self):
        self.assertEqual(has22([2, 1, 2]), False)

    def test_case_03(self):
        self.assertEqual(has22([1, 2, 2]), True)

    def test_case_04(self):
        self.assertEqual(has22([2, 2, 1, 2]), True)

    def test_case_05(self):
        self.assertEqual(has22([1, 3, 2]), False)

    def test_case_06(self):
        self.assertEqual(has22([1, 3, 2, 2]), True)

    def test_case_07(self):
        self.assertEqual(has22([2, 3, 2, 2]), True)

    def test_case_08(self):
        self.assertEqual(has22([4, 2, 4, 2, 2, 5]), True)

    def test_case_09(self):
        self.assertEqual(has22([1, 2]), False)

    def test_case_10(self):
        self.assertEqual(has22([2, 2]), True)

    def test_case_11(self):
        self.assertEqual(has22([2]), False)

    def test_case_12(self):
        self.assertEqual(has22([]), False)

    def test_case_13(self):
        self.assertEqual(has22([3, 3, 2, 2]), True)

    def test_case_14(self):
        self.assertEqual(has22([5, 2, 5, 2]), False)


if __name__ == "__main__":
    unittest.main()
