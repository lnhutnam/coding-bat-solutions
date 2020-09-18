# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""

import unittest


def make_chocolate(small, big, goal):
    return ((-1, goal - big * 5)[(goal - big * 5) <= small], (-1, (goal - (goal // 5) * 5))[(goal - (goal // 5) * 5) <= small])[goal // 5 <= big]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_chocolate(4, 1, 9), 4)

    def test_case_01(self):
        self.assertEqual(make_chocolate(4, 1, 10), -1)

    def test_case_02(self):
        self.assertEqual(make_chocolate(4, 1, 7), 2)

    def test_case_03(self):
        self.assertEqual(make_chocolate(6, 2, 7), 2)

    def test_case_04(self):
        self.assertEqual(make_chocolate(4, 1, 5), 0)

    def test_case_05(self):
        self.assertEqual(make_chocolate(4, 1, 4), 4)

    def test_case_05(self):
        self.assertEqual(make_chocolate(5, 4, 9), 4)

    def test_case_06(self):
        self.assertEqual(make_chocolate(9, 3, 18), 3)

    def test_case_07(self):
        self.assertEqual(make_chocolate(3, 1, 9), -1)

    def test_case_08(self):
        self.assertEqual(make_chocolate(1, 2, 7), -1)

    def test_case_09(self):
        self.assertEqual(make_chocolate(1, 2, 6), 1)

    def test_case_10(self):
        self.assertEqual(make_chocolate(1, 2, 5), 0)

    def test_case_11(self):
        self.assertEqual(make_chocolate(6, 1, 10), 5)

    def test_case_12(self):
        self.assertEqual(make_chocolate(6, 1, 11), 6)

    def test_case_13(self):
        self.assertEqual(make_chocolate(6, 1, 12), -1)

    def test_case_14(self):
        self.assertEqual(make_chocolate(6, 1, 13), -1)

    def test_case_15(self):
        self.assertEqual(make_chocolate(6, 2, 10), 0)

    def test_case_16(self):
        self.assertEqual(make_chocolate(6, 2, 11), 1)

    def test_case_17(self):
        self.assertEqual(make_chocolate(6, 2, 12), 2)

    def test_case_18(self):
        self.assertEqual(make_chocolate(60, 100, 550), 50)

    def test_case_19(self):
        self.assertEqual(make_chocolate(1000, 1000000, 5000006), 6)

    def test_case_20(self):
        self.assertEqual(make_chocolate(7, 1, 12), 7)

    def test_case_21(self):
        self.assertEqual(make_chocolate(7, 1, 13), -1)

    def test_case_22(self):
        self.assertEqual(make_chocolate(7, 2, 13), 3)


if __name__ == "__main__":
    unittest.main()
