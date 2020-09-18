# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

import unittest

##########################
def front_back(str):
  if (len(str) <= 1):
    return str
  else:
    return str[len(str) - 1] + str[1: len(str) - 1] + str[0]


############# TESTING CLASS #############
class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(front_back('code'), 'eodc')

    def test_case_01(self):
        self.assertEqual(front_back('a'), 'a')

    def test_case_02(self):
        self.assertEqual(front_back('ab'), 'ba')

    def test_case_03(self):
        self.assertEqual(front_back('abc'), 'cba')

    def test_case_04(self):
        self.assertEqual(front_back(''), '')

    def test_case_05(self):
        self.assertEqual(front_back('Chocolate'), 'ehocolatC')

    def test_case_06(self):
        self.assertEqual(front_back('aavJ'), 'Java')

    def test_case_07(self):
        self.assertEqual(front_back('hello'), 'oellh')


if __name__ == "__main__":
    unittest.main()


