# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""


def make_out_word(out, word):
    return out[:2] + word + out[len(out) - 2:]


class TestMakeOutWord(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_out_word('<<>>', 'Yay'), '<<Yay>>')

    def test_case_01(self):
        self.assertEqual(make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')

    def test_case_02(self):
        self.assertEqual(make_out_word('[[]]', 'word'), '[[word]]')

    def test_case_03(self):
        self.assertEqual(make_out_word('HHoo', 'Hello'), 'HHHellooo')

    def test_case_04(self):
        self.assertEqual(make_out_word('abyz', 'YAY'), 'abYAYyz')


if __name__ == "__main__":
    unittest.main()
