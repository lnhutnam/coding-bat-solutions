# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


import unittest


"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""


def xyz_there(str):
    i = 0
    while i < len(str) - 2:
        if str[i: i + 3] == 'xyz':
            if i == 0 or str[i - 1] != '.':
                return True
        i = i + 1
    return False


class TestXyzThere(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(xyz_there('abcxyz'), True)

    def test_case_01(self):
        self.assertEqual(xyz_there('abc.xyz'), False)

    def test_case_02(self):
        self.assertEqual(xyz_there('xyz.abc'), True)

    def test_case_03(self):
        self.assertEqual(xyz_there('abcxy'), False)

    def test_case_04(self):
        self.assertEqual(xyz_there('xyz'), True)

    def test_case_05(self):
        self.assertEqual(xyz_there('xy'), False)

    def test_case_06(self):
        self.assertEqual(xyz_there('x'), False)

    def test_case_07(self):
        self.assertEqual(xyz_there(''), False)

    def test_case_08(self):
        self.assertEqual(xyz_there('abc.xyzxyz'), True)

    def test_case_09(self):
        self.assertEqual(xyz_there('abc.xxyz'), True)

    def test_case_10(self):
        self.assertEqual(xyz_there('.xyz'), False)

    def test_case_11(self):
        self.assertEqual(xyz_there('12.xyz'), False)

    def test_case_12(self):
        self.assertEqual(xyz_there('12xyz'), True)

    def test_case_13(self):
        self.assertEqual(xyz_there('1.xyz.xyz2.xyz'), False)


if __name__ == "__main__":
    unittest.main()
