# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""


def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


class TestCountEvems(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(count_evens([2, 1, 2, 3, 4]), 3)

    def test_case_01(self):
        self.assertEqual(count_evens([2, 2, 0]), 3)

    def test_case_02(self):
        self.assertEqual(count_evens([1, 3, 5]), 0)

    def test_case_03(self):
        self.assertEqual(count_evens([]), 0)

    def test_case_04(self):
        self.assertEqual(count_evens([11, 9, 0, 1]), 1)

    def test_case_05(self):
        self.assertEqual(count_evens([2, 11, 9, 0]), 2)

    def test_case_06(self):
        self.assertEqual(count_evens([2]), 1)

    def test_case_07(self):
        self.assertEqual(count_evens([2, 5, 12]), 2)


if __name__ == "__main__":
    unittest.main()
