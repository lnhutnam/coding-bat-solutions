# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
"""

import unittest


def make_bricks(small, big, goal):
    return ((False, True)[(goal - big * 5) <= small], (False, True)[(goal - (goal // 5) * 5) <= small])[goal // 5 <= big]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        # make_bricks(3, 1, 8) → True
        self.assertEqual(make_bricks(3, 1, 8), True)

    def test_case_01(self):
        # make_bricks(3, 1, 9) → False
        self.assertEqual(make_bricks(3, 1, 9), False)

    def test_case_02(self):
        # make_bricks(3, 2, 10) → True
        self.assertEqual(make_bricks(3, 2, 10), True)

    def test_case_03(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 10), True)

    def test_case_04(self):
        # make_bricks(3, 2, 9) → False
        self.assertEqual(make_bricks(3, 2, 9), False)

    def test_case_05(self):
        # make_bricks(6, 1, 11) → True
        self.assertEqual(make_bricks(6, 1, 11), True)

    def test_case_06(self):
        # make_bricks(6, 0, 11) → False
        self.assertEqual(make_bricks(6, 0, 11), False)

    def test_case_07(self):
        # make_bricks(1, 4, 11) → True
        self.assertEqual(make_bricks(1, 4, 11), True)

    def test_case_08(self):
        # make_bricks(0, 3, 10) → True
        self.assertEqual(make_bricks(0, 3, 10), True)

    def test_case_09(self):
        # make_bricks(1, 4, 12) → False
        self.assertEqual(make_bricks(1, 4, 12), False)

    def test_case_10(self):
        # make_bricks(3, 1, 7) → True
        self.assertEqual(make_bricks(3, 1, 7), True)

    def test_case_11(self):
        # make_bricks(1, 1, 7) → False
        self.assertEqual(make_bricks(1, 1, 7), False)

    def test_case_12(self):
        # make_bricks(2, 1, 7) → True
        self.assertEqual(make_bricks(2, 1, 7), True)

    def test_case_13(self):
        # make_bricks(7, 1, 11) → True
        self.assertEqual(make_bricks(7, 1, 11), True)

    def test_case_14(self):
        # make_bricks(7, 1, 8) → True
        self.assertEqual(make_bricks(7, 1, 8), True)

    def test_case_15(self):
        # make_bricks(7, 1, 13) → False
        self.assertEqual(make_bricks(7, 1, 13), False)

    def test_case_16(self):
        # make_bricks(43, 1, 46) → True
        self.assertEqual(make_bricks(43, 1, 46), True)

    def test_case_17(self):
        # make_bricks(40, 1, 46) → False
        self.assertEqual(make_bricks(40, 1, 46), False)

    def test_case_18(self):
        # make_bricks(40, 2, 47) → True
        self.assertEqual(make_bricks(40, 2, 47), True)

    def test_case_19(self):
        # make_bricks(40, 2, 50) → True
        self.assertEqual(make_bricks(40, 2, 50), True)

    def test_case_20(self):
        # make_bricks(40, 2, 52) → False
        self.assertEqual(make_bricks(40, 2, 52), False)

    def test_case_21(self):
        # make_bricks(22, 2, 33) → False
        self.assertEqual(make_bricks(22, 2, 33), False)

    def test_case_22(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 8), True)

    def test_case_23(self):
        # make_bricks(0, 2, 10) → True
        self.assertEqual(make_bricks(0, 2, 10), True)

    def test_case_24(self):
        # make_bricks(1000000, 1000, 1000100) → True
        self.assertEqual(make_bricks(1000000, 1000, 1000100), True)

    def test_case_25(self):
        # make_bricks(2, 1000000, 100003) → False
        self.assertEqual(make_bricks(2, 1000000, 100003), False)

    def test_case_26(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 8), True)

    def test_case_27(self):
        # make_bricks(20, 0, 19) → True
        self.assertEqual(make_bricks(20, 0, 19), True)

    def test_case_28(self):
        # make_bricks(20, 0, 21) → False
        self.assertEqual(make_bricks(20, 0, 21), False)

    def test_case_29(self):
        # make_bricks(20, 4, 51) → False
        self.assertEqual(make_bricks(20, 4, 51), False)

    def test_case_30(self):
        # make_bricks(20, 4, 39) → True
        self.assertEqual(make_bricks(20, 4, 39), True)


if __name__ == "__main__":
    unittest.main()
