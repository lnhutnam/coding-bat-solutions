# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""


def count_hi(str):
    count = 0
    i = 0
    while i < len(str) - 1:
        if str[i:i + 2] == 'hi':
            count += 1
            i += 1
        i += 1
    return count


class TestCountHi(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(count_hi('abc hi ho'), 1)

    def test_case_01(self):
        self.assertEqual(count_hi('ABChi hi'), 2)

    def test_case_02(self):
        self.assertEqual(count_hi('hihi'), 2)

    def test_case_03(self):
        self.assertEqual(count_hi('hiHIhi'), 2)

    def test_case_04(self):
        self.assertEqual(count_hi(''), 0)

    def test_case_05(self):
        self.assertEqual(count_hi('h'), 0)

    def test_case_06(self):
        self.assertEqual(count_hi('hi'), 1)

    def test_case_07(self):
        self.assertEqual(count_hi('Hi is no HI on ahI'), 0)

    def test_case_08(self):
        self.assertEqual(count_hi('hiho not HOHIhi'), 2)


if __name__ == "__main__":
    unittest.main()
