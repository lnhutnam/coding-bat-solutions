# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


import unittest

"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""


def count_code(str):
    count = 0
    i = 0
    while i < len(str) - 3:
        if str[i: i + 4][0] == 'c' and str[i: i + 4][1] == 'o' and str[i: i + 4][3] == 'e':
            count += 1
            i += 4
        else:
            i += 1
    return count


class TestCountCode(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(count_code('aaacodebbb'), 1)

    def test_case_01(self):
        self.assertEqual(count_code('codexxcode'), 2)

    def test_case_02(self):
        self.assertEqual(count_code('cozexxcope'), 2)

    def test_case_03(self):
        self.assertEqual(count_code('cozfxxcope'), 1)

    def test_case_04(self):
        self.assertEqual(count_code('xxcozeyycop'), 1)

    def test_case_05(self):
        self.assertEqual(count_code('cozcop'), 0)

    def test_case_06(self):
        self.assertEqual(count_code('abcxyz'), 0)

    def test_case_07(self):
        self.assertEqual(count_code('code'), 1)

    def test_case_08(self):
        self.assertEqual(count_code('ode'), 0)

    def test_case_09(self):
        self.assertEqual(count_code('c'), 0)

    def test_case_10(self):
        self.assertEqual(count_code(''), 0)

    def test_case_11(self):
        self.assertEqual(count_code('AAcodeBBcoleCCccoreDD'), 3)

    def test_case_12(self):
        self.assertEqual(count_code('AAcodeBBcoleCCccorfDD'), 2)

    def test_case_13(self):
        self.assertEqual(count_code('coAcodeBcoleccoreDD'), 3)


if __name__ == "__main__":
    unittest.main()
