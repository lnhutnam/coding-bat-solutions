"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

import unittest


def not_string(str):
    return ("not " + str, str)[str[:3] == "not"]


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(not_string('candy'), 'not candy')

    def test_case_01(self):
        self.assertEqual(not_string('x'), 'not x')

    def test_case_02(self):
        self.assertEqual(not_string('not bat'), 'not bat')

    def test_case_03(self):
        self.assertEqual(not_string('bat'), "not bat")

    def test_case_04(self):
        self.assertEqual(not_string('not'), "not")

    def test_case_05(self):
        self.assertEqual(not_string('is not'), "not is not")

    def test_case_06(self):
        self.assertEqual(not_string('no'), "not no")


if __name__ == "__main__":
    unittest.main()
