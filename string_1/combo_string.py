# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""


def combo_string(a, b):
    return (a + b + a, b + a + b)[len(a) > len(b)]


class TestComboString(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(combo_string('Hello', 'hi'), 'hiHellohi')

    def test_case_01(self):
        self.assertEqual(combo_string('hi', 'Hello'), 'hiHellohi')

    def test_case_02(self):
        self.assertEqual(combo_string('aaa', 'b'), 'baaab')

    def test_case_03(self):
        self.assertEqual(combo_string('b', 'aaa'), 'baaab')

    def test_case_04(self):
        self.assertEqual(combo_string('aaa', ''), 'aaa')

    def test_case_05(self):
        self.assertEqual(combo_string('', 'bb'), 'bb')

    def test_case_06(self):
        self.assertEqual(combo_string('aaa', '1234'), 'aaa1234aaa')

    def test_case_07(self):
        self.assertEqual(combo_string('aaa', 'bb'), 'bbaaabb')

    def test_case_08(self):
        self.assertEqual(combo_string('a', 'bb'), 'abba')

    def test_case_09(self):
        self.assertEqual(combo_string('bb', 'a'), 'abba')

    def test_case_10(self):
        self.assertEqual(combo_string('xyz', 'ab'), 'abxyzab')


if __name__ == "__main__":
    unittest.main()
