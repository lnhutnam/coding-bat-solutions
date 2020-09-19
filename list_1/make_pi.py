# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]
"""


def make_pi():
    return [3, 1, 4]


class TestMakePi(unittest.TestCase):
    def test_case(self):
        self.assertEqual(make_pi(), [3, 1, 4])


if __name__ == "__main__":
    unittest.main()
