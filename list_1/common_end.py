# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""


def common_end(a, b):
    return (False, True)[a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]]


class TestCommonEnd(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(common_end([1, 2, 3], [7, 3]), True)

    def test_case_01(self):
        self.assertEqual(common_end([1, 2, 3], [7, 3, 2]), False)

    def test_case_02(self):
        self.assertEqual(common_end([1, 2, 3], [1, 3]), True)

    def test_case_03(self):
        self.assertEqual(common_end([1, 2, 3], [1]), True)

    def test_case_04(self):
        self.assertEqual(common_end([1, 2, 3], [2]), False)


if __name__ == "__main__":
    unittest.main()
