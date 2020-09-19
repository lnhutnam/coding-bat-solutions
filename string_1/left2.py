# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""


def left2(str):
    return str[2:] + str[:2]


class TestLeft2(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(left2('Hello'), 'lloHe')

    def test_case_01(self):
        self.assertEqual(left2('java'), 'vaja')

    def test_case_02(self):
        self.assertEqual(left2('Hi'), 'Hi')

    def test_case_03(self):
        self.assertEqual(left2('code'), 'deco')

    def test_case_04(self):
        self.assertEqual(left2('cat'), 'tca')

    def test_case_05(self):
        self.assertEqual(left2('12345'), '34512')

    def test_case_06(self):
        self.assertEqual(left2('Chocolate'), 'ocolateCh')

    def test_case_07(self):
        self.assertEqual(left2('bricks'), 'icksbr')


if __name__ == "__main__":
    unittest.main()
