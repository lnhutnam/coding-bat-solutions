# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""


def string_splosion(str):
    pass


class TestStringSplosion(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_splosion('Code'), 'CCoCodCode')

    def test_case_01(self):
        self.assertEqual(string_splosion('abc'), 'aababc')

    def test_case_02(self):
        self.assertEqual(string_splosion('ab'), 'aab')


if __name__ == "__main__":
    unittest.main()
