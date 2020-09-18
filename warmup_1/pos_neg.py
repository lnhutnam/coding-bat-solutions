# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
pos_neg(-4, -5, False) → False
pos_neg(-4, 5, False) → True
pos_neg(-4, 5, True) → False
pos_neg(1, 1, False) → False
pos_neg(-1, -1, False) → False
pos_neg(1, -1, True) → False
pos_neg(-1, 1, True) → False
pos_neg(1, 1, True) → False
pos_neg(-1, -1, True) → True
pos_neg(5, -5, False) → True
pos_neg(-6, 6, False) → True
pos_neg(-5, -6, False) → False
pos_neg(-2, -1, False) → False
pos_neg(1, 2, False) → False
pos_neg(-5, 6, True) → False
pos_neg(-5, -5, True) → True
"""

import unittest


def pos_neg(a, b, negative):
    return ((False, True)[a*b < 0], (False, True)[a < 0 and b < 0])[negative == True]


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(pos_neg(1, -1, False), True)

    def test_case_01(self):
        self.assertEqual(pos_neg(-1, 1, False), True)

    def test_case_02(self):
        self.assertEqual(pos_neg(-4, -5, True), True)

    def test_case_03(self):
        self.assertEqual(pos_neg(-4, -5, False), False)

    def test_case_04(self):
        self.assertEqual(pos_neg(-4, 5, False), True)

    def test_case_05(self):
        self.assertEqual(pos_neg(-4, 5, True), False)

    def test_case_06(self):
        self.assertEqual(pos_neg(1, 1, False), False)

    def test_case_07(self):
        self.assertEqual(pos_neg(-1, -1, False), False)

    def test_case_08(self):
        self.assertEqual(pos_neg(1, -1, True), False)

    def test_case_09(self):
        self.assertEqual(pos_neg(-1, 1, True), False)

    def test_case_10(self):
        self.assertEqual(pos_neg(1, 1, True), False)

    def test_case_11(self):
        self.assertEqual(pos_neg(-1, -1, True), True)

    def test_case_12(self):
        self.assertEqual(pos_neg(5, -5, False), True)

    def test_case_13(self):
        self.assertEqual(pos_neg(-6, 6, False), True)

    def test_case_14(self):
        self.assertEqual(pos_neg(-5, -6, False), False)

    def test_case_15(self):
        self.assertEqual(pos_neg(-2, -1, False), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(1, 2, False), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(-5, 6, True), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(-5, -5, True), True)


if __name__ == "__main__":
    unittest.main()


