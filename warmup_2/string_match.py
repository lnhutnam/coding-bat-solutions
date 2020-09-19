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
    length = (len(b), len(a))[len(a) <= len(b)]
    length -= 1
    count = 0
    i = 0
    while i < length:
        if a[i:i+2] == b[i:i+2]:
            count += 1
        i += 1
    return count


class TestStringMatch(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_match('xxcaazz', 'xxbaaz'), 3)

    def test_case_01(self):
        self.assertEqual(string_match('abc', 'abc'), 2)

    def test_case_02(self):
        self.assertEqual(string_match('abc', 'axc'), 0)

    def test_case_03(self):
        self.assertEqual(string_match('hello', 'he'), 1)

    def test_case_04(self):
        self.assertEqual(string_match('he', 'hello'), 1)

    def test_case_05(self):
        self.assertEqual(string_match('h', 'hello'), 0)

    def test_case_06(self):
        self.assertEqual(string_match('', 'hello'), 0)

    def test_case_07(self):
        self.assertEqual(string_match('aabbccdd', 'abbbxxd'), 1)

    def test_case_08(self):
        self.assertEqual(string_match('aaxxaaxx', 'iaxxai'), 3)

    def test_case_09(self):
        self.assertEqual(string_match('iaxxai', 'aaxxaaxx'), 3)


if __name__ == "__main__":
    unittest.main()
