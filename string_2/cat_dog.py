# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""


def cat_dog(str):
    count = 0
    i = 0
    while i < len(str) - 2:
        if str[i] == 'c':
            if str[i:i + 3] == 'cat':
                count += 1
        elif str[i] == 'd':
            if str[i:i + 3] == 'dog':
                count -= 1
        i += 1
    return count == 0


class TestCatDog(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(cat_dog('catdog'), True)

    def test_case_01(self):
        self.assertEqual(cat_dog('catcat'), False)

    def test_case_02(self):
        self.assertEqual(cat_dog('1cat1cadodog'), True)

    def test_case_03(self):
        self.assertEqual(cat_dog('catxxdogxxxdog'), False)

    def test_case_04(self):
        self.assertEqual(cat_dog('catxdogxdogxcat'), True)

    def test_case_05(self):
        self.assertEqual(cat_dog('catxdogxdogxca'), False)

    def test_case_06(self):
        self.assertEqual(cat_dog('dogdogcat'), False)

    def test_case_07(self):
        self.assertEqual(cat_dog('dogogcat'), True)

    def test_case_08(self):
        self.assertEqual(cat_dog('dog'), False)

    def test_case_09(self):
        self.assertEqual(cat_dog('cat'), False)

    def test_case_10(self):
        self.assertEqual(cat_dog('ca'), True)

    def test_case_11(self):
        self.assertEqual(cat_dog('c'), True)

    def test_case_12(self):
        self.assertEqual(cat_dog(''), True)


if __name__ == "__main__":
    unittest.main()
