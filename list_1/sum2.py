# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


import unittest

"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""


def sum2(nums):
    return (sum(nums[:2]), sum(nums))[len(nums) <= 2]


class TestSum2(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum2([1, 2, 3]), 3)

    def test_case_01(self):
        self.assertEqual(sum2([1, 1]), 2)

    def test_case_02(self):
        self.assertEqual(sum2([1, 1, 1, 1]), 2)

    def test_case_03(self):
        self.assertEqual(sum2([1, 2]), 3)

    def test_case_04(self):
        self.assertEqual(sum2([1]), 1)

    def test_case_05(self):
        self.assertEqual(sum2([]), 0)

    def test_case_06(self):
        self.assertEqual(sum2([4, 5, 6]), 9)

    def test_case_07(self):
        self.assertEqual(sum2([4]), 4)


if __name__ == "__main__":
    unittest.main()
