"""

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""
import unittest

def monkey_trouble(a_smile, b_smile):
  return ((a_smile and b_smile) or (not a_smile and not b_smile))

class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(monkey_trouble(True, True), True)
    def test_case_01(self):
        self.assertEqual(monkey_trouble(False, False), True)
    def test_case_02(self):
        self.assertEqual(monkey_trouble(True, False), False)
    def test_case_03(self):
        self.assertEqual(monkey_trouble(False, True), False)

if __name__ == "__main__":
    unittest.main()