# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

import unittest


def front3(str):
    return (str[:3] + str[:3] + str[:3], str[:len(str)] + str[:len(str)] + str[:len(str)])[len(str) < 3]


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(front3('Java'), 'JavJavJav')

    def test_case_01(self):
        self.assertEqual(front3('Chocolate'), 'ChoChoCho')

    def test_case_02(self):
        self.assertEqual(front3('abc'), 'abcabcabc')

    def test_case_03(self):
        self.assertEqual(front3('abcXYZ'), 'abcabcabc')

    def test_case_04(self):
        self.assertEqual(front3('ab'), 'ababab')

    def test_case_05(self):
        self.assertEqual(front3('a'), 'aaa')

    def test_case_06(self):
        self.assertEqual(front3(''), '')


if __name__ == "__main__":
    unittest.main()
