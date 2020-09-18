# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020

import unittest

from operations.sum import sum

class Test(unittest.TestCase):
    def test_add(self):
        res = sum(1, 2)
        self.assertEqual(res, 3)
       