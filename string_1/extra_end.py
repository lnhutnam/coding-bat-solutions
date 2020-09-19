# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""


def extra_end(str):
    return str[len(str) - 2:] * 3


class TestExtraEnd(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(extra_end('Hello'), 'lololo')

    def test_case_01(self):
        self.assertEqual(extra_end('ab'), 'ababab')

    def test_case_02(self):
        self.assertEqual(extra_end('Hi'), 'HiHiHi')

    def test_case_03(self):
        self.assertEqual(extra_end('Candy'), 'dydydy')

    def test_case_04(self):
        self.assertEqual(extra_end('Code'), 'dedede')


if __name__ == "__main__":
    unittest.main()
