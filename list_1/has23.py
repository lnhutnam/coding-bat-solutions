# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""


def has23(nums):
    return (False, True)[2 in nums or 3 in nums]


class TestHas23(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(has23([2, 5]), True)

    def test_case_01(self):
        self.assertEqual(has23([4, 3]), True)

    def test_case_02(self):
        self.assertEqual(has23([4, 5]), False)

    def test_case_03(self):
        self.assertEqual(has23([2, 2]), True)

    def test_case_04(self):
        self.assertEqual(has23([3, 2]), True)

    def test_case_05(self):
        self.assertEqual(has23([3, 3]), True)

    def test_case_06(self):
        self.assertEqual(has23([7, 7]), False)

    def test_case_07(self):
        self.assertEqual(has23([3, 9]), True)

    def test_case_08(self):
        self.assertEqual(has23([9, 5]), False)


if __name__ == "__main__":
    unittest.main()
