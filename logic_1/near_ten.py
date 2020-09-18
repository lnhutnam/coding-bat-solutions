"""

Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""

import unittest


def near_ten(num):
    return (False, True)[num % 10 <= 2 or num % 10 >= 8]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(near_ten(12), True)

    def test_case_01(self):
        self.assertEqual(near_ten(17), False)

    def test_case_02(self):
        self.assertEqual(near_ten(19), True)

    def test_case_03(self):
        self.assertEqual(near_ten(31), True)

    def test_case_04(self):
        self.assertEqual(near_ten(6), False)

    def test_case_05(self):
        self.assertEqual(near_ten(10), True)

    def test_case_06(self):
        self.assertEqual(near_ten(11), True)

    def test_case_07(self):
        self.assertEqual(near_ten(21), True)

    def test_case_08(self):
        self.assertEqual(near_ten(22), True)

    def test_case_09(self):
        self.assertEqual(near_ten(23), False)

    def test_case_10(self):
        self.assertEqual(near_ten(54), False)

    def test_case_11(self):
        self.assertEqual(near_ten(155), False)

    def test_case_12(self):
        self.assertEqual(near_ten(158), True)

    def test_case_13(self):
        self.assertEqual(near_ten(1), True)


if __name__ == "__main__":
    unittest.main()
