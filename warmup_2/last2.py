# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""


def last2(str):
    pass


class TestLast2(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(last2('hixxhi'), 1)

    def test_case_01(self):
        self.assertEqual(last2('xaxxaxaxx'), 1)

    def test_case_02(self):
        self.assertEqual(last2('axxxaaxx'), 2)


if __name__ == "__main__":
    unittest.main()
