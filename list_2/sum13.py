# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""


def sum13(nums):
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            result += nums[i]
            i += 1
    return result


class TestSum13(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum13([1, 2, 2, 1]), 6)

    def test_case_01(self):
        self.assertEqual(sum13([1, 1]), 2)

    def test_case_02(self):
        self.assertEqual(sum13([1, 2, 2, 1, 13]), 6)

    def test_case_03(self):
        self.assertEqual(sum13([1, 2, 13, 2, 1, 13]), 4)

    def test_case_04(self):
        self.assertEqual(sum13([13, 1, 2, 13, 2, 1, 13]), 3)

    def test_case_05(self):
        self.assertEqual(sum13([]), 0)

    def test_case_06(self):
        self.assertEqual(sum13([13]), 0)

    def test_case_07(self):
        self.assertEqual(sum13([13, 13]), 0)

    def test_case_08(self):
        self.assertEqual(sum13([13, 0, 13]), 0)

    def test_case_09(self):
        self.assertEqual(sum13([13, 1, 13]), 0)

    def test_case_10(self):
        self.assertEqual(sum13([5, 7, 2]), 14)

    def test_case_11(self):
        self.assertEqual(sum13([5, 13, 2]), 5)

    def test_case_12(self):
        self.assertEqual(sum13([0]), 0)

    def test_case_13(self):
        self.assertEqual(sum13([13, 0]), 0)


if __name__ == "__main__":
    unittest.main()
