# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""


def array_front9(nums):
    return ((False, True)[9 in nums], (False, True)[9 in nums[:4]])[len(nums) > 4]


class TestArrayFront9(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)

    def test_case_01(self):
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)

    def test_case_02(self):
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)

    def test_case_03(self):
        self.assertEqual(array_front9([9, 2, 3]), True)

    def test_case_04(self):
        self.assertEqual(array_front9([1, 9, 9]), True)

    def test_case_05(self):
        self.assertEqual(array_front9([1, 2, 3]), False)

    def test_case_06(self):
        self.assertEqual(array_front9([1, 9]), True)

    def test_case_07(self):
        self.assertEqual(array_front9([5, 5]), False)

    def test_case_07(self):
        self.assertEqual(array_front9([2]), False)

    def test_case_08(self):
        self.assertEqual(array_front9([9]), True)

    def test_case_09(self):
        self.assertEqual(array_front9([]), False)

    def test_case_10(self):
        self.assertEqual(array_front9([3, 9, 2, 3, 3]), True)


if __name__ == "__main__":
    unittest.main()
