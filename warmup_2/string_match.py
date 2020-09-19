# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""


def string_match(a, b):
    pass


class TestStringMatch(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_match('xxcaazz', 'xxbaaz'), 3)

    def test_case_01(self):
        self.assertEqual(string_match('abc', 'abc'), 2)

    def test_case_02(self):
        self.assertEqual(string_match('abc', 'axc'), 0)


if __name__ == "__main__":
    unittest.main()
