# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""


def first_half(str):
    return str[:(len(str) // 2)]


class TestFirstHalf(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(first_half('WooHoo'), 'Woo')

    def test_case_01(self):
        self.assertEqual(first_half('HelloThere'), 'Hello')

    def test_case_02(self):
        self.assertEqual(first_half('abcdef'), 'abc')

    def test_case_03(self):
        self.assertEqual(first_half('ab'), 'a')

    def test_case_04(self):
        self.assertEqual(first_half(''), '')

    def test_case_05(self):
        self.assertEqual(first_half('0123456789'), '01234')

    def test_case_06(self):
        self.assertEqual(first_half('kitten'), 'kit')


if __name__ == "__main__":
    unittest.main()
