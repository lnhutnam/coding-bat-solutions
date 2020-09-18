"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

Test case for example:
love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""

import unittest


def love6(a, b):
    return (False, True)[a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(love6(6, 4), True)

    def test_case_01(self):
        self.assertEqual(love6(4, 5), False)

    def test_case_02(self):
        self.assertEqual(love6(1, 5), True)

    def test_case_03(self):
        self.assertEqual(love6(1, 6), True)

    def test_case_04(self):
        self.assertEqual(love6(1, 8), False)

    def test_case_05(self):
        self.assertEqual(love6(1, 7), True)

    def test_case_06(self):
        self.assertEqual(love6(7, 5), False)

    def test_case_07(self):
        self.assertEqual(love6(8, 2), True)

    def test_case_08(self):
        self.assertEqual(love6(6, 6), True)

    def test_case_09(self):
        self.assertEqual(love6(-6, 2), False)

    def test_case_10(self):
        self.assertEqual(love6(-4, 10), True)

    def test_case_11(self):
        self.assertEqual(love6(-7, 1), False)

    def test_case_12(self):
        self.assertEqual(love6(-6, 12), True)

    def test_case_13(self):
        self.assertEqual(love6(-2, -4), False)

    def test_case_14(self):
        self.assertEqual(love6(7, 1), True)

    def test_case_15(self):
        self.assertEqual(love6(0, 9), False)

    def test_case_16(self):
        self.assertEqual(love6(8, 3), False)

    def test_case_17(self):
        self.assertEqual(love6(3, 3), True)

    def test_case_18(self):
        self.assertEqual(love6(3, 4), False)


if __name__ == "__main__":
    unittest.main()


# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020