import unittest

from operations.sum import sum

class Test(unittest.TestCase):
    def test_add(self):
        res = sum(1, 2)
        self.assertEqual(res, 3)
        