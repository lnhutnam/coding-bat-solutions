"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

Test case for example:
alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""

import unittest


def alarm_clock(day, vacation):
    return (('7:00', '10:00')[day == 0 or day == 6], ('10:00', 'off')[day == 0 or day == 6])[vacation]


class MyTest(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(alarm_clock(1, False), '7:00')

    def test_case_01(self):
        self.assertEqual(alarm_clock(5, False), '7:00')

    def test_case_02(self):
        self.assertEqual(alarm_clock(0, False), '10:00')

    def test_case_03(self):
        self.assertEqual(alarm_clock(6, False), '10:00')

    def test_case_04(self):
        self.assertEqual(alarm_clock(0, True), 'off')

    def test_case_05(self):
        self.assertEqual(alarm_clock(6, True), 'off')

    def test_case_06(self):
        self.assertEqual(alarm_clock(1, True), '10:00')

    def test_case_07(self):
        self.assertEqual(alarm_clock(3, True), '10:00')

    def test_case_05(self):
        self.assertEqual(alarm_clock(5, True), '10:00')


if __name__ == "__main__":
    unittest.main()
