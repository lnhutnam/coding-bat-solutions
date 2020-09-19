# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""


def double_char(str):
    result = ''
    for c in str:
        result += c * 2
    return result


class TestDoubleChar(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(double_char('The'), 'TThhee')

    def test_case_00(self):
        self.assertEqual(double_char('AAbb'), 'AAAAbbbb')

    def test_case_00(self):
        self.assertEqual(double_char('Hi-There'), 'HHii--TThheerree')

    def test_case_00(self):
        self.assertEqual(double_char('Word!'), 'WWoorrdd!!')

    def test_case_00(self):
        self.assertEqual(double_char('!!'), '!!!!')

    def test_case_00(self):
        self.assertEqual(double_char(''), '')

    def test_case_00(self):
        self.assertEqual(double_char('a'), 'aa')

    def test_case_00(self):
        self.assertEqual(double_char('.'), '..')

    def test_case_00(self):
        self.assertEqual(double_char('aa'), 'aaaa')


if __name__ == "__main__":
    unittest.main()
