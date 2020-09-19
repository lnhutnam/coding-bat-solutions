# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

import unittest


def string_times(str, n):
    return str * n


class TestStringTimes(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_times('Hi', 2), 'HiHi')

    def test_case_01(self):
        self.assertEqual(string_times('Hi', 3), 'HiHiHi')

    def test_case_02(self):
        self.assertEqual(string_times('Hi', 1), 'Hi')

    def test_case_03(self):
        self.assertEqual(string_times('Hi', 0), '')

    def test_case_04(self):
        self.assertEqual(string_times('Hi', 5), 'HiHiHiHiHi')

    def test_case_05(self):
        self.assertEqual(string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')

    def test_case_06(self):
        self.assertEqual(string_times('x', 4), 'xxxx')

    def test_case_07(self):
        self.assertEqual(string_times('', 4), '')

    def test_case_08(self):
        self.assertEqual(string_times('code', 2), 'codecode')

    def test_case_09(self):
        self.assertEqual(string_times('code', 3), 'codecodecode')

if __name__ == "__main__":
    unittest.main()
    