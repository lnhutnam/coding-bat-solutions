# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""


def non_start(a, b):
    return a[1:] + b[1:]


class TestNonstart(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(non_start('Hello', 'There'), 'ellohere')

    def test_case_01(self):
        self.assertEqual(non_start('java', 'code'), 'avaode')

    def test_case_02(self):
        self.assertEqual(non_start('shotl', 'java'), 'hotlava')

    def test_case_03(self):
        self.assertEqual(non_start('ab', 'xy'), 'by')

    def test_case_04(self):
        self.assertEqual(non_start('x', 'ac'), 'c')

    def test_case_05(self):
        self.assertEqual(non_start('a', 'x'), '')

    def test_case_06(self):
        self.assertEqual(non_start('kit', 'kat'), 'itat')

    def test_case_07(self):
        self.assertEqual(non_start('mart', 'dart'), 'artart')

    def test_case_08(self):
        self.assertEqual(non_start('ab', 'x'), 'b')


if __name__ == "__main__":
    unittest.main()
