# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

import unittest


def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


class TestNearHundred(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(near_hundred(93), True)

    def test_case_01(self):
        self.assertEqual(near_hundred(90), True)

    def test_case_02(self):
        self.assertEqual(near_hundred(89), False)

    def test_case_03(self):
        self.assertEqual(near_hundred(110), True)

    def test_case_04(self):
        self.assertEqual(near_hundred(111), False)

    def test_case_05(self):
        self.assertEqual(near_hundred(121), False)

    def test_case_06(self):
        self.assertEqual(near_hundred(-101), False)

    def test_case_07(self):
        self.assertEqual(near_hundred(-209), False)

    def test_case_08(self):
        self.assertEqual(near_hundred(190), True)

    def test_case_09(self):
        self.assertEqual(near_hundred(209), True)      

    def test_case_10(self):
        self.assertEqual(near_hundred(0), False)     

    def test_case_11(self):
        self.assertEqual(near_hundred(5), False)

    def test_case_12(self):
        self.assertEqual(near_hundred(-50), False)

    def test_case_13(self):
        self.assertEqual(near_hundred(191), True)

    def test_case_14(self):
        self.assertEqual(near_hundred(189), False)

    def test_case_15(self):
        self.assertEqual(near_hundred(200), True)

    def test_case_16(self):
        self.assertEqual(near_hundred(210), True)

    def test_case_17(self):
        self.assertEqual(near_hundred(211), False)

    def test_case_18(self):
        self.assertEqual(near_hundred(290), False)

if __name__ == "__main__":
    unittest.main()

