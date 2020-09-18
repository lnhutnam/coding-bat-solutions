# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
"""

import unittest


def round10(num):
    return (num - num % 10, num + (10 - num % 10))[num % 10 >= 5]


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_case_01(self):
        self.assertEqual(round_sum(12, 13, 14), 30)

    def test_case_02(self):
        self.assertEqual(round_sum(6, 4, 4), 10)

    def test_case_03(self):
        self.assertEqual(round_sum(4, 6, 5), 20)

    def test_case_04(self):
        self.assertEqual(round_sum(4, 4, 6), 10)

    def test_case_05(self):
        self.assertEqual(round_sum(9, 4, 4), 10)

    def test_case_06(self):
        self.assertEqual(round_sum(0, 0, 1), 0)

    def test_case_07(self):
        self.assertEqual(round_sum(0, 9, 0), 10)

    def test_case_08(self):
        self.assertEqual(round_sum(10, 10, 19), 40)

    def test_case_09(self):
        self.assertEqual(round_sum(20, 30, 40), 90)

    def test_case_10(self):
        self.assertEqual(round_sum(45, 21, 30), 100)

    def test_case_11(self):
        self.assertEqual(round_sum(23, 11, 26), 60)

    def test_case_12(self):
        self.assertEqual(round_sum(23, 24, 25), 70)

    def test_case_13(self):
        self.assertEqual(round_sum(25, 24, 25), 80)

    def test_case_14(self):
        self.assertEqual(round_sum(23, 24, 29), 70)

    def test_case_15(self):
        self.assertEqual(round_sum(11, 24, 36), 70)

    def test_case_16(self):
        self.assertEqual(round_sum(24, 36, 32), 90)

    def test_case_17(self):
        self.assertEqual(round_sum(14, 12, 26), 50)

    def test_case_18(self):
        self.assertEqual(round_sum(12, 10, 24), 40)


if __name__ == "__main__":
    unittest.main()
