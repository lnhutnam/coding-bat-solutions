"""
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. 
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
Otherwise the result is 1 (maybe).

For example test case:
date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""

import unittest


def date_fashion(you, date):
    return ((1, 2)[you >= 8 or date >= 8], 0)[you <= 2 or date <= 2]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(date_fashion(5, 10), 2)

    def test_case_01(self):
        self.assertEqual(date_fashion(5, 2), 0)

    def test_case_02(self):
        self.assertEqual(date_fashion(5, 5), 1)

    def test_case_03(self):
        self.assertEqual(date_fashion(3, 3), 1)

    def test_case_04(self):
        self.assertEqual(date_fashion(10, 2), 0)

    def test_case_05(self):
        self.assertEqual(date_fashion(2, 9), 0)

    def test_case_06(self):
        self.assertEqual(date_fashion(9, 9), 2)

    def test_case_07(self):
        self.assertEqual(date_fashion(10, 5), 2)

    def test_case_08(self):
        self.assertEqual(date_fashion(2, 2), 0)

    def test_case_09(self):
        self.assertEqual(date_fashion(3, 7), 1)

    def test_case_10(self):
        self.assertEqual(date_fashion(2, 7), 0)

    def test_case_11(self):
        self.assertEqual(date_fashion(6, 2), 0)


if __name__ == "__main__":
    unittest.main()
