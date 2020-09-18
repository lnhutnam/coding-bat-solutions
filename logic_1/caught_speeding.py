"""
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

For example test case:
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""

import unittest


def caught_speeding(speed, is_birthday):
    return (((0, 1)[61 <= speed <= 80], 2)[speed >= 81], ((0, 1)[66 <= speed <= 85], 2)[speed >= 86])[is_birthday]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(caught_speeding(60, False), 0)

    def test_case_01(self):
        self.assertEqual(caught_speeding(65, False), 1)

    def test_case_02(self):
        self.assertEqual(caught_speeding(65, True), 0)

    def test_case_03(self):
        self.assertEqual(caught_speeding(80, False), 1)

    def test_case_04(self):
        self.assertEqual(caught_speeding(85, False), 2)

    def test_case_05(self):
        self.assertEqual(caught_speeding(85, True), 1)

    def test_case_06(self):
        self.assertEqual(caught_speeding(70, False), 1)

    def test_case_07(self):
        self.assertEqual(caught_speeding(75, False), 1)

    def test_case_08(self):
        self.assertEqual(caught_speeding(75, True), 1)

    def test_case_09(self):
        self.assertEqual(caught_speeding(40, False), 0)

    def test_case_10(self):
        self.assertEqual(caught_speeding(40, True), 0)

    def test_case_11(self):
        self.assertEqual(caught_speeding(90, False), 2)


if __name__ == "__main__":
    unittest.main()
