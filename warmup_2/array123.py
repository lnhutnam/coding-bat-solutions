# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""


def array123(nums):
    return str([1, 2, 3])[1:-1] in str(nums)


class TestArray123(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(array123([1, 1, 2, 3, 1]), True)

    def test_case_01(self):
        self.assertEqual(array123([1, 1, 2, 4, 1]), False)

    def test_case_02(self):
        self.assertEqual(array123([1, 1, 2, 1, 2, 3]), True)

    def test_case_03(self):
        self.assertEqual(array123([1, 1, 2, 1, 2, 1]), False)

    def test_case_04(self):
        self.assertEqual(array123([1, 2, 3, 1, 2, 3]), True)

    def test_case_05(self):
        self.assertEqual(array123([1, 2, 3]), True)

    def test_case_06(self):
        self.assertEqual(array123([1, 1, 1]), False)

    def test_case_07(self):
        self.assertEqual(array123([1, 2]), False)

    def test_case_08(self):
        self.assertEqual(array123([1]), False)

    def test_case_09(self):
        self.assertEqual(array123([]), False)


if __name__ == "__main__":
    unittest.main()
