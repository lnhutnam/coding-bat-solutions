# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""
import unittest


def lone_sum(a, b, c):
    if a == b:
        if a == c:
            return 0
        else:
            return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def test_case_00(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def test_case_00(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)


if __name__ == "__main__":
    unittest.main()
