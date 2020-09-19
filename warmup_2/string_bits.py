# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""


def string_bits(str):
    result = ""
    i = 0
    while i < len(str):
        result += str[i]
        i += 2
    return result


class TestStringBits(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(string_bits('Hello'), 'Hlo')

    def test_case_01(self):
        self.assertEqual(string_bits('Hi'), 'H')

    def test_case_02(self):
        self.assertEqual(string_bits('Heeololeo'), 'Hello')

    def test_case_03(self):
        self.assertEqual(string_bits('HiHiHi'), 'HHH')

    def test_case_04(self):
        self.assertEqual(string_bits(''), '')

    def test_case_05(self):
        self.assertEqual(string_bits('Greetings'), 'Getns')

    def test_case_06(self):
        self.assertEqual(string_bits('Chocoate'), 'Coot')

    def test_case_07(self):
        self.assertEqual(string_bits('pi'), 'p')

    def test_case_08(self):
        self.assertEqual(string_bits('Hello Kitten'), 'HloKte')

    def test_case_09(self):
        self.assertEqual(string_bits('hxaxpxpxy'), 'happy')


if __name__ == "__main__":
    unittest.main()
