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
    pass


class TestArrayFront9(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)

    def test_case_01(self):
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)

    def test_case_02(self):
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)


if __name__ == "__main__":
    unittest.main()
