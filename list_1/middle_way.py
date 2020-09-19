# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


import unittest

"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""


def middle_way(a, b):
    return [a[1], b[1]]


class TestMiddleWay(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])

    def test_case_01(self):
        self.assertEqual(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])

    def test_case_02(self):
        self.assertEqual(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])

    def test_case_03(self):
        self.assertEqual(middle_way([1, 9, 7], [4, 8, 8]), [9, 8])

    def test_case_04(self):
        self.assertEqual(middle_way([1, 2, 3], [3, 1, 4]), [2, 1])

    def test_case_05(self):
        self.assertEqual(middle_way([1, 2, 3], [4, 1, 1]), [2, 1])


if __name__ == "__main__":
    unittest.main()
