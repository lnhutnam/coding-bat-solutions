# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""
import unittest


def sleep_in(weekday, vacation):
    return (not weekday or vacation)


class Test(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sleep_in(False, False), True)

    def test_case_01(self):
        self.assertEqual(sleep_in(True, False), False)

    def test_case_02(self):
        self.assertEqual(sleep_in(False, True), True)


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))

print("Start testing")
if __name__ == "__main__":
    unittest.main()

