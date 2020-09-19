# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""


def last2(str):
    if len(str) < 2:
        return 0
    i = 0
    count = 0
    while i < len(str) - 2:
        sub = str[i: i + 2]
        if sub == str[len(str)-2:]:
            count += 1
        i += 1
    return count


class TestLast2(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(last2('hixxhi'), 1)

    def test_case_01(self):
        self.assertEqual(last2('xaxxaxaxx'), 1)

    def test_case_02(self):
        self.assertEqual(last2('axxxaaxx'), 2)

    def test_case_03(self):
        self.assertEqual(last2('xxaxxaxxaxx'), 3)

    def test_case_04(self):
        self.assertEqual(last2('xaxaxaxx'), 0)

    def test_case_05(self):
        self.assertEqual(last2('xxxx'), 2)

    def test_case_06(self):
        self.assertEqual(last2('13121312'), 1)

    def test_case_07(self):
        self.assertEqual(last2('11212'), 1)

    def test_case_08(self):
        self.assertEqual(last2('13121311'), 0)

    def test_case_09(self):
        self.assertEqual(last2('1717171'), 2)

    def test_case_10(self):
        self.assertEqual(last2('hi'), 0)

    def test_case_11(self):
        self.assertEqual(last2('h'), 0)

    def test_case_12(self):
        self.assertEqual(last2(''), 0)


if __name__ == "__main__":
    unittest.main()
