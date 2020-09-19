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
    result = ''

    i = 0
    while i < len(str):
        result += str[:i+1]
        i += 1

    return result


class TestStringSplosion(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_splosion('Code'), 'CCoCodCode')

    def test_case_01(self):
        self.assertEqual(string_splosion('abc'), 'aababc')

    def test_case_02(self):
        self.assertEqual(string_splosion('ab'), 'aab')

    def test_case_03(self):
        self.assertEqual(string_splosion('x'), 'x')

    def test_case_04(self):
        self.assertEqual(string_splosion('fade'), 'ffafadfade')

    def test_case_05(self):
        self.assertEqual(string_splosion('There'), 'TThTheTherThere')

    def test_case_06(self):
        self.assertEqual(string_splosion('Kitten'), 'KKiKitKittKitteKitten')

    def test_case_07(self):
        self.assertEqual(string_splosion('Bye'), 'BByBye')

    def test_case_08(self):
        self.assertEqual(string_splosion('Good'), 'GGoGooGood')

    def test_case_09(self):
        self.assertEqual(string_splosion('Bad'), 'BBaBad')


if __name__ == "__main__":
    unittest.main()
