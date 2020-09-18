"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""

import unittest


def missing_char(str, n):
    return str[:n] + str[(n+1):]


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(missing_char('kitten', 1), 'ktten')

    def test_case_01(self):
        self.assertEqual(missing_char('kitten', 0), 'itten')

    def test_case_02(self):
        self.assertEqual(missing_char('kitten', 4), 'kittn')

    def test_case_04(self):
        self.assertEqual(missing_char('Hi', 0), 'i')

    def test_case_05(self):
        self.assertEqual(missing_char('Hi', 1), 'H')

    def test_case_06(self):
        self.assertEqual(missing_char('code', 0), 'ode')

    def test_case_07(self):
        self.assertEqual(missing_char('code', 1), 'cde')

    def test_case_08(self):
        self.assertEqual(missing_char('code', 2), 'coe')

    def test_case_09(self):
        self.assertEqual(missing_char('code', 3), 'cod')

    def test_case_10(self):
        self.assertEqual(missing_char('chocolate', 8), 'chocolat')


if __name__ == "__main__":
    unittest.main()
