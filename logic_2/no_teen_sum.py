# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""

import unittest


def fix_teen(n):
    return (0, n)[n < 13 or n > 19 or n == 15 or n == 16]


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(no_teen_sum(1, 2, 3), 6)

    def test_case_01(self):
        self.assertEqual(no_teen_sum(2, 13, 1), 3)

    def test_case_02(self):
        self.assertEqual(no_teen_sum(2, 1, 14), 3)

    def test_case_03(self):
        self.assertEqual(no_teen_sum(2, 1, 15), 18)

    def test_case_04(self):
        self.assertEqual(no_teen_sum(2, 1, 16), 19)

    def test_case_05(self):
        self.assertEqual(no_teen_sum(2, 1, 17), 3)

    def test_case_06(self):
        self.assertEqual(no_teen_sum(17, 1, 2), 3)

    def test_case_07(self):
        self.assertEqual(no_teen_sum(2, 15, 2), 19)

    def test_case_08(self):
        self.assertEqual(no_teen_sum(16, 17, 18), 16)

    def test_case_09(self):
        self.assertEqual(no_teen_sum(17, 18, 19), 0)

    def test_case_10(self):
        self.assertEqual(no_teen_sum(15, 16, 1), 32)

    def test_case_11(self):
        self.assertEqual(no_teen_sum(15, 15, 19), 30)

    def test_case_12(self):
        self.assertEqual(no_teen_sum(15, 19, 16), 31)

    def test_case_13(self):
        self.assertEqual(no_teen_sum(5, 17, 18), 5)

    def test_case_14(self):
        self.assertEqual(no_teen_sum(17, 18, 16), 16)

    def test_case_15(self):
        self.assertEqual(no_teen_sum(17, 19, 18), 0)


if __name__ == "__main__":
    unittest.main()
