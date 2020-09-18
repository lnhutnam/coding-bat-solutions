"""
Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""

import unittest


def in1to10(n, outside_mode):
    return ((False, True)[(outside_mode == True and (n <= 1 or n >= 10))], True)[n in range(1, 11) and outside_mode == False]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(in1to10(5, False), True)

    def test_case_01(self):
        self.assertEqual(in1to10(11, False), False)

    def test_case_02(self):
        self.assertEqual(in1to10(11, True), True)

    def test_case_03(self):
        self.assertEqual(in1to10(10, False), True)

    def test_case_04(self):
        self.assertEqual(in1to10(10, True), True)

    def test_case_05(self):
        self.assertEqual(in1to10(9, False), True)

    def test_case_06(self):
        self.assertEqual(in1to10(9, True), False)

    def test_case_07(self):
        self.assertEqual(in1to10(1, False), True)

    def test_case_08(self):
        self.assertEqual(in1to10(1, True), True)

    def test_case_09(self):
        self.assertEqual(in1to10(0, False), False)

    def test_case_10(self):
        self.assertEqual(in1to10(0, True), True)

    def test_case_11(self):
        self.assertEqual(in1to10(-1, False), False)

    def test_case_12(self):
        self.assertEqual(in1to10(-1, True), True)

    def test_case_13(self):
        self.assertEqual(in1to10(99, False), False)

    def test_case_14(self):
        self.assertEqual(in1to10(-99, True), True)


if __name__ == "__main__":
    unittest.main()


# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020