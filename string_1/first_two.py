# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""


def first_two(str):
    return ((str[:2], str)[len(str) <= 2], '')[len(str) == 0]


class TestFirstTwo(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(first_two('Hello'), 'He')

    def test_case_01(self):
        self.assertEqual(first_two('abcdefg'), 'ab')

    def test_case_02(self):
        self.assertEqual(first_two('ab'), 'ab')

    def test_case_03(self):
        self.assertEqual(first_two('a'), 'a')

    def test_case_04(self):
        self.assertEqual(first_two(''), '')

    def test_case_05(self):
        self.assertEqual(first_two('Kitten'), 'Ki')

    def test_case_06(self):
        self.assertEqual(first_two('hi'), 'hi')

    def test_case_07(self):
        self.assertEqual(first_two('hiya'), 'hi')


if __name__ == "__main__":
    unittest.main()
