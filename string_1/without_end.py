# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""


def without_end(str):
    return str[1:len(str) - 1]


class TestWithoutEnd(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(without_end('Hello'), 'ell')

    def test_case_01(self):
        self.assertEqual(without_end('java'), 'av')

    def test_case_02(self):
        self.assertEqual(without_end('coding'), 'odin')

    def test_case_03(self):
        self.assertEqual(without_end('code'), 'od')

    def test_case_04(self):
        self.assertEqual(without_end('ab'), '')

    def test_case_05(self):
        self.assertEqual(without_end('Chocolate!'), 'hocolate')

    def test_case_06(self):
        self.assertEqual(without_end('kitten'), 'itte')

    def test_case_07(self):
        self.assertEqual(without_end('woohoo'), 'ooho')


if __name__ == "__main__":
    unittest.main()
