# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""

import unittest


def make_chocolate(small, big, goal):
    pass


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_chocolate(4, 1, 9), 4)

    def test_case_00(self):
        self.assertEqual(make_chocolate(4, 1, 10), -1)

    def test_case_00(self):
        self.assertEqual(make_chocolate(4, 1, 7), 2)


if __name__ == "__main__":
    unittest.main()


