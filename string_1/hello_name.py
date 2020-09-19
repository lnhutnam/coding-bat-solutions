# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

For example test case:
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""

import unittest


def hello_name(name):
    return "Hello " + name + "!"


class TestHelloName(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(hello_name('Bob'), 'Hello Bob!')

    def test_case_01(self):
        self.assertEqual(hello_name('Alice'), 'Hello Alice!')

    def test_case_02(self):
        self.assertEqual(hello_name('X'), 'Hello X!')

    def test_case_03(self):
        self.assertEqual(hello_name('Dolly'), 'Hello Dolly!')

    def test_case_04(self):
        self.assertEqual(hello_name('Alpha'), 'Hello Alpha!')

    def test_case_05(self):
        self.assertEqual(hello_name('Omega'), 'Hello Omega!')

    def test_case_06(self):
        self.assertEqual(hello_name('Goodbye'), 'Hello Goodbye!')

    def test_case_07(self):
        self.assertEqual(hello_name('ho ho ho'), 'Hello ho ho ho!')

    def test_case_08(self):
        self.assertEqual(hello_name('xyz!'), 'Hello xyz!!')

    def test_case_09(self):
        self.assertEqual(hello_name('Hello'), 'Hello Hello!')


if __name__ == "__main__":
    unittest.main()
