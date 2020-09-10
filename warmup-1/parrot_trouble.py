"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""

import unittest


def parrot_trouble(talking, hour):
    return (False, (hour < 7 or hour > 20))[talking]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(parrot_trouble(True, 6), True)

    def test_case_01(self):
        self.assertEqual(parrot_trouble(True, 7), False)

    def test_case_03(self):
        self.assertEqual(parrot_trouble(False, 6), False)

    def test_case_04(self):
        self.assertEqual(parrot_trouble(False, 21), False)

    def test_case_05(self):
        self.assertEqual(parrot_trouble(False, 20), False)

    def test_case_06(self):
        self.assertEqual(parrot_trouble(True, 23), True)

    def test_case_07(self):
        self.assertEqual(parrot_trouble(False, 23), False)

    def test_case_08(self):
        self.assertEqual(parrot_trouble(True, 20), False)

    def test_case_09(self):
        self.assertEqual(parrot_trouble(False, 12), False)


if __name__ == "__main__":
    unittest.main()
