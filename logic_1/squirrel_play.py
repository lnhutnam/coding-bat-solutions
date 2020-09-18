"""
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

For example test case:
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

"""

import unittest


def squirrel_play(temp, is_summer):
    return (60 <= temp <= 90, 60 <= temp <= 100)[is_summer]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(squirrel_play(70, False), True)

    def test_case_01(self):
        self.assertEqual(squirrel_play(95, False), False)

    def test_case_02(self):
        self.assertEqual(squirrel_play(95, True), True)

    def test_case_03(self):
        self.assertEqual(squirrel_play(90, False), True)

    def test_case_04(self):
        self.assertEqual(squirrel_play(90, True), True)

    def test_case_05(self):
        self.assertEqual(squirrel_play(50, False), False)

    def test_case_06(self):
        self.assertEqual(squirrel_play(50, True), False)

    def test_case_07(self):
        self.assertEqual(squirrel_play(100, False), False)

    def test_case_08(self):
        self.assertEqual(squirrel_play(100, True), True)

    def test_case_09(self):
        self.assertEqual(squirrel_play(105, True), False)

    def test_case_10(self):
        self.assertEqual(squirrel_play(59, False), False)

    def test_case_11(self):
        self.assertEqual(squirrel_play(59, True), False)

    def test_case_12(self):
        self.assertEqual(squirrel_play(60, False), True)


if __name__ == "__main__":
    unittest.main()
