# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""


def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


class TestMakeTags(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(make_tags('i', 'Yay'), '<i>Yay</i>')

    def test_case_01(self):
        self.assertEqual(make_tags('i', 'Hello'), '<i>Hello</i>')

    def test_case_02(self):
        self.assertEqual(make_tags('cite', 'Yay'), '<cite>Yay</cite>')

    def test_case_03(self):
        self.assertEqual(make_tags('address', 'here'),
                         '<address>here</address>')

    def test_case_04(self):
        self.assertEqual(make_tags('body', 'Heart'), '<body>Heart</body>')

    def test_case_05(self):
        self.assertEqual(make_tags('i', 'i'), 	'<i>i</i>')

    def test_case_06(self):
        self.assertEqual(make_tags('i', ''), '<i></i>')


if __name__ == "__main__":
    unittest.main()
