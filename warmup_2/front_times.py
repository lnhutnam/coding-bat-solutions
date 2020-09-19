# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. 
Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""


def front_times(str, n):
    return (str[:len(str)] * n, str[:3] * n)[len(str) > 3]


class TestFrontTimes(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(front_times('Chocolate', 2), 'ChoCho')

    def test_case_01(self):
        self.assertEqual(front_times('Chocolate', 3), 'ChoChoCho')

    def test_case_02(self):
        self.assertEqual(front_times('Abc', 3), 'AbcAbcAbc')

    def test_case_03(self):
        self.assertEqual(front_times('Ab', 4), 'AbAbAbAb')

    def test_case_04(self):
        self.assertEqual(front_times('A', 4), 'AAAA')

    def test_case_05(self):
        self.assertEqual(front_times('', 4), '')

    def test_case_06(self):
        self.assertEqual(front_times('Abc', 0), '')


if __name__ == "__main__":
    unittest.main()
