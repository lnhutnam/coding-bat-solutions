"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

import unittest


def not_string(str):
    return ("not " + str, str)[str[:3] == "not"]

class Test(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()

