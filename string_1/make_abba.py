# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""

def make_abba(a, b):
  return a + b + b + a

class TestMakeAbba(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_abba('Hi', 'Bye'), 'HiByeByeHi')

    def test_case_01(self):
        self.assertEqual(make_abba('Yo', 'Alice'), 'YoAliceAliceYo')

    def test_case_02(self):
        self.assertEqual(make_abba('What', 'Up'), 'WhatUpUpWhat')

    def test_case_03(self):
        self.assertEqual(make_abba('aaa', 'bbb'), 'aaabbbbbbaaa')

    def test_case_04(self):
        self.assertEqual(make_abba('x', ''), 'xx')

    def test_case_05(self):
        self.assertEqual(make_abba('', 'y'), 'yy')

    def test_case_06(self):
        self.assertEqual(make_abba('Bo', 'Ya'), 'BoYaYaBo')

    def test_case_07(self):
        self.assertEqual(make_abba('Ya', 'Ya'), 'YaYaYaYa')

    def test_case_08(self):
        self.assertEqual(make_abba('x', 'y'), 'xyyx')


if __name__ == "__main__":
    unittest.main()