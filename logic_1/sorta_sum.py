"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""

import unittest


def sorta_sum(a, b):
    return (a + b, 20)[a + b in range(10, 20)]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sorta_sum(3, 4), 7)

    def test_case_01(self):
        self.assertEqual(sorta_sum(9, 4), 20)

    def test_case_02(self):
        self.assertEqual(sorta_sum(10, 11), 21)

    def test_case_03(self):
        self.assertEqual(sorta_sum(12, -3), 9)

    def test_case_04(self):
        self.assertEqual(sorta_sum(-3, 12), 9)

    def test_case_05(self):
        self.assertEqual(sorta_sum(4, 5), 9)

    def test_case_06(self):
        self.assertEqual(sorta_sum(4, 6), 20)

    def test_case_07(self):
        self.assertEqual(sorta_sum(14, 7), 21)

    def test_case_08(self):
        self.assertEqual(sorta_sum(14, 6), 20)


if __name__ == "__main__":
    unittest.main()


# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020