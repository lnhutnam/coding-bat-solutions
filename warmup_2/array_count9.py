# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""


def array_count9(nums):
    count = 0
    for num in nums:
        count += 1 if num == 9 else 0
    return count


class TestArrayCount9(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(array_count9([1, 2, 9]), 1)

    def test_case_01(self):
        self.assertEqual(array_count9([1, 9, 9]), 2)

    def test_case_02(self):
        self.assertEqual(array_count9([1, 9, 9, 3, 9]), 3)

    def test_case_03(self):
        self.assertEqual(array_count9([4, 2, 4, 3, 1]), 0)

    def test_case_04(self):
        self.assertEqual(array_count9([1, 2, 3]), 0)

    def test_case_05(self):
        self.assertEqual(array_count9([]), 0)

    def test_case_06(self):
        self.assertEqual(array_count9([9, 2, 4, 3, 1]), 1)


if __name__ == "__main__":
    unittest.main()
