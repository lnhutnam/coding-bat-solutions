# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


def sum67(nums):
    result = 0
    flag = False
    for num in nums:
        if num == 6:
            flag = True
        if (flag):
            if num == 7:
                flag = False
        else:
            result += num
    return result


class TestSum67(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum67([1, 2, 2]), 5)

    def test_case_01(self):
        self.assertEqual(sum67([1, 2, 2, 6, 99, 99, 7]), 5)

    def test_case_02(self):
        self.assertEqual(sum67([1, 1, 6, 7, 2]), 4)

    def test_case_03(self):
        self.assertEqual(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]), 2)

    def test_case_04(self):
        self.assertEqual(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]), 2)

    def test_case_05(self):
        self.assertEqual(sum67([2, 7, 6, 2, 6, 7, 2, 7]), 18)

    def test_case_06(self):
        self.assertEqual(sum67([2, 7, 6, 2, 6, 2, 7]), 9)

    def test_case_07(self):
        self.assertEqual(sum67([1, 6, 7, 7]), 8)

    def test_case_06(self):
        self.assertEqual(sum67([6, 7, 1, 6, 7, 7]), 8)

    def test_case_07(self):
        self.assertEqual(sum67([6, 8, 1, 6, 7]), 0)

    def test_case_08(self):
        self.assertEqual(sum67([]), 0)

    def test_case_09(self):
        self.assertEqual(sum67([6, 7, 11]), 11)

    def test_case_10(self):
        self.assertEqual(sum67([11, 6, 7, 11]), 22)

    def test_case_11(self):
        self.assertEqual(sum67([2, 2, 6, 7, 7]), 11)


if __name__ == "__main__":
    unittest.main()
