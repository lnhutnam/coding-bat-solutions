# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""

import unittest


def lucky_sum(a, b, c):
    #    if a == 13:
    #         return 0
    #     if b == 13:
    #         return a
    #     if c == 13:
    #         return a + b
    #     return a + b + c
    return (((a + b + c, a + b)[c == 13], a)[b == 13], 0)[a == 13]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)

    def test_case_01(self):
        self.assertEqual(lucky_sum(1, 2, 13), 3)

    def test_case_02(self):
        self.assertEqual(lucky_sum(1, 13, 3), 1)

    def test_case_03(self):
        self.assertEqual(lucky_sum(1, 13, 13), 1)

    def test_case_04(self):
        self.assertEqual(lucky_sum(6, 5, 2), 13)

    def test_case_05(self):
        self.assertEqual(lucky_sum(13, 2, 3), 0)

    def test_case_06(self):
        self.assertEqual(lucky_sum(13, 2, 13), 0)

    def test_case_07(self):
        self.assertEqual(lucky_sum(13, 13, 2), 0)

    def test_case_08(self):
        self.assertEqual(lucky_sum(9, 4, 13), 13)

    def test_case_09(self):
        self.assertEqual(lucky_sum(8, 13, 2), 8)

    def test_case_10(self):
        self.assertEqual(lucky_sum(7, 2, 1), 10)

    def test_case_11(self):
        self.assertEqual(lucky_sum(3, 3, 13), 6)


if __name__ == "__main__":
    unittest.main()
