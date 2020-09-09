"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

For example test case:
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""
import unittest

def diff21(n):
    return (2*abs(n - 21), abs(n - 21))[n < 21]

class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(diff21(19), 2)
    def test_case_01(self):
        self.assertEqual(diff21(10), 11)
    def test_case_02(self):
        self.assertEqual(diff21(21), 0)
    def test_case_03(self):
        self.assertEqual(diff21(22), 2)
    def test_case_04(self):
        self.assertEqual(diff21(25), 8)
    def test_case_05(self):
        self.assertEqual(diff21(30), 18)
    def test_case_06(self):
        self.assertEqual(diff21(0), 21)
    def test_case_07(self):
        self.assertEqual(diff21(1), 20)
    def test_case_08(self):
        self.assertEqual(diff21(-1), 22)
    def test_case_09(self):
        self.assertEqual(diff21(-2), 23)
    def test_case_10(self):
        self.assertEqual(diff21(2), 19)
    def test_case_11(self):
        self.assertEqual(diff21(50), 58)

if __name__ == "__main__":
    unittest.main()