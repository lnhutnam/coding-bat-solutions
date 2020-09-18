"""
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.

For example test case:

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""

import unittest


def cigar_party(cigars, is_weekend):
    return ((False, True)[is_weekend and cigars >= 40], True)[40 <= cigars <= 60]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(cigar_party(30, False), False)

    def test_case_01(self):
        self.assertEqual(cigar_party(50, False), True)

    def test_case_02(self):
        self.assertEqual(cigar_party(70, True), True)

    def test_case_03(self):
        self.assertEqual(cigar_party(30, True), False)

    def test_case_04(self):
        self.assertEqual(cigar_party(50, True), True)

    def test_case_05(self):
        self.assertEqual(cigar_party(60, False), True)

    def test_case_06(self):
        self.assertEqual(cigar_party(61, False), False)

    def test_case_07(self):
        self.assertEqual(cigar_party(40, False), True)

    def test_case_08(self):
        self.assertEqual(cigar_party(39, False), False)

    def test_case_09(self):
        self.assertEqual(cigar_party(40, True), True)

    def test_case_10(self):
        self.assertEqual(cigar_party(39, True), False)


if __name__ == "__main__":
    unittest.main()

# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020