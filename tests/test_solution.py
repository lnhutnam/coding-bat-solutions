import unittest

# ====================================================== IMPORT SECTION =================================================================
# list 1
# list 2
# logic 1
from solutions.solutions import alarm_clock
from solutions.solutions import caught_speeding
from solutions.solutions import cigar_party
from solutions.solutions import date_fashion
from solutions.solutions import in1to10
from solutions.solutions import love6
from solutions.solutions import near_ten
from solutions.solutions import sorta_sum
from solutions.solutions import squirrel_play
# logic 2

# string 1

# string 2

# warmup 1

# warmup 2

# =======================================================================================================================================

# list 1 testing
# =======================================================================================================================================


# list 2 testing
# =======================================================================================================================================

# logic 1 testing
# =======================================================================================================================================
class TestAlarmClock(unittest.TestCase):
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

    def test_case_08(self):
        self.assertEqual(alarm_clock(5, True), '10:00')


class TestCaughtSpeeding(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(caught_speeding(60, False), 0)

    def test_case_01(self):
        self.assertEqual(caught_speeding(65, False), 1)

    def test_case_02(self):
        self.assertEqual(caught_speeding(65, True), 0)

    def test_case_03(self):
        self.assertEqual(caught_speeding(80, False), 1)

    def test_case_04(self):
        self.assertEqual(caught_speeding(85, False), 2)

    def test_case_05(self):
        self.assertEqual(caught_speeding(85, True), 1)

    def test_case_06(self):
        self.assertEqual(caught_speeding(70, False), 1)

    def test_case_07(self):
        self.assertEqual(caught_speeding(75, False), 1)

    def test_case_08(self):
        self.assertEqual(caught_speeding(75, True), 1)

    def test_case_09(self):
        self.assertEqual(caught_speeding(40, False), 0)

    def test_case_10(self):
        self.assertEqual(caught_speeding(40, True), 0)

    def test_case_11(self):
        self.assertEqual(caught_speeding(90, False), 2)


class TestCigarParty(unittest.TestCase):
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


class TestDateFashion(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(date_fashion(5, 10), 2)

    def test_case_01(self):
        self.assertEqual(date_fashion(5, 2), 0)

    def test_case_02(self):
        self.assertEqual(date_fashion(5, 5), 1)

    def test_case_03(self):
        self.assertEqual(date_fashion(3, 3), 1)

    def test_case_04(self):
        self.assertEqual(date_fashion(10, 2), 0)

    def test_case_05(self):
        self.assertEqual(date_fashion(2, 9), 0)

    def test_case_06(self):
        self.assertEqual(date_fashion(9, 9), 2)

    def test_case_07(self):
        self.assertEqual(date_fashion(10, 5), 2)

    def test_case_08(self):
        self.assertEqual(date_fashion(2, 2), 0)

    def test_case_09(self):
        self.assertEqual(date_fashion(3, 7), 1)

    def test_case_10(self):
        self.assertEqual(date_fashion(2, 7), 0)

    def test_case_11(self):
        self.assertEqual(date_fashion(6, 2), 0)


class TestInOneToTen(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(in1to10(5, False), True)

    def test_case_01(self):
        self.assertEqual(in1to10(11, False), False)

    def test_case_02(self):
        self.assertEqual(in1to10(11, True), True)

    def test_case_03(self):
        self.assertEqual(in1to10(10, False), True)

    def test_case_04(self):
        self.assertEqual(in1to10(10, True), True)

    def test_case_05(self):
        self.assertEqual(in1to10(9, False), True)

    def test_case_06(self):
        self.assertEqual(in1to10(9, True), False)

    def test_case_07(self):
        self.assertEqual(in1to10(1, False), True)

    def test_case_08(self):
        self.assertEqual(in1to10(1, True), True)

    def test_case_09(self):
        self.assertEqual(in1to10(0, False), False)

    def test_case_10(self):
        self.assertEqual(in1to10(0, True), True)

    def test_case_11(self):
        self.assertEqual(in1to10(-1, False), False)

    def test_case_12(self):
        self.assertEqual(in1to10(-1, True), True)

    def test_case_13(self):
        self.assertEqual(in1to10(99, False), False)

    def test_case_14(self):
        self.assertEqual(in1to10(-99, True), True)


class TestLoveSix(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(love6(6, 4), True)

    def test_case_01(self):
        self.assertEqual(love6(4, 5), False)

    def test_case_02(self):
        self.assertEqual(love6(1, 5), True)

    def test_case_03(self):
        self.assertEqual(love6(1, 6), True)

    def test_case_04(self):
        self.assertEqual(love6(1, 8), False)

    def test_case_05(self):
        self.assertEqual(love6(1, 7), True)

    def test_case_06(self):
        self.assertEqual(love6(7, 5), False)

    def test_case_07(self):
        self.assertEqual(love6(8, 2), True)

    def test_case_08(self):
        self.assertEqual(love6(6, 6), True)

    def test_case_09(self):
        self.assertEqual(love6(-6, 2), False)

    def test_case_10(self):
        self.assertEqual(love6(-4, 10), True)

    def test_case_11(self):
        self.assertEqual(love6(-7, 1), False)

    def test_case_12(self):
        self.assertEqual(love6(-6, 12), True)

    def test_case_13(self):
        self.assertEqual(love6(-2, -4), False)

    def test_case_14(self):
        self.assertEqual(love6(7, 1), True)

    def test_case_15(self):
        self.assertEqual(love6(0, 9), False)

    def test_case_16(self):
        self.assertEqual(love6(8, 3), False)

    def test_case_17(self):
        self.assertEqual(love6(3, 3), True)

    def test_case_18(self):
        self.assertEqual(love6(3, 4), False)


class TestNearTen(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(near_ten(12), True)

    def test_case_01(self):
        self.assertEqual(near_ten(17), False)

    def test_case_02(self):
        self.assertEqual(near_ten(19), True)

    def test_case_03(self):
        self.assertEqual(near_ten(31), True)

    def test_case_04(self):
        self.assertEqual(near_ten(6), False)

    def test_case_05(self):
        self.assertEqual(near_ten(10), True)

    def test_case_06(self):
        self.assertEqual(near_ten(11), True)

    def test_case_07(self):
        self.assertEqual(near_ten(21), True)

    def test_case_08(self):
        self.assertEqual(near_ten(22), True)

    def test_case_09(self):
        self.assertEqual(near_ten(23), False)

    def test_case_10(self):
        self.assertEqual(near_ten(54), False)

    def test_case_11(self):
        self.assertEqual(near_ten(155), False)

    def test_case_12(self):
        self.assertEqual(near_ten(158), True)

    def test_case_13(self):
        self.assertEqual(near_ten(1), True)

class TestSortaSum(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sorta_sum(3, 4), 7)

    def test_case_01(self):
        self.assertEqual(sorta_sum(9, 4), 20)

    def test_case_02(self):
        self.assertEqual(sorta_sum(10, 11), 21)

    def test_case_03(self):
        self.assertEqual(sorta_sum(12, -3), 9)

    def test_case_04(self):
        self.assertEqual(sorta_sum(-3, 12), 9)

    def test_case_05(self):
        self.assertEqual(sorta_sum(4, 5), 9)

    def test_case_06(self):
        self.assertEqual(sorta_sum(4, 6), 20)

    def test_case_07(self):
        self.assertEqual(sorta_sum(14, 7), 21)

    def test_case_08(self):
        self.assertEqual(sorta_sum(14, 6), 20)

class TestSquirrelPlay(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(squirrel_play(70, False), True)

    def test_case_01(self):
        self.assertEqual(squirrel_play(95, False), False)

    def test_case_02(self):
        self.assertEqual(squirrel_play(95, True), True)

    def test_case_03(self):
        self.assertEqual(squirrel_play(90, False), True)

    def test_case_04(self):
        self.assertEqual(squirrel_play(90, True), True)

    def test_case_05(self):
        self.assertEqual(squirrel_play(50, False), False)

    def test_case_06(self):
        self.assertEqual(squirrel_play(50, True), False)

    def test_case_07(self):
        self.assertEqual(squirrel_play(100, False), False)

    def test_case_08(self):
        self.assertEqual(squirrel_play(100, True), True)

    def test_case_09(self):
        self.assertEqual(squirrel_play(105, True), False)

    def test_case_10(self):
        self.assertEqual(squirrel_play(59, False), False)

    def test_case_11(self):
        self.assertEqual(squirrel_play(59, True), False)

    def test_case_12(self):
        self.assertEqual(squirrel_play(60, False), True)



# logic 2 tesing
# =======================================================================================================================================



# string 1 tesing
# =======================================================================================================================================



# string 2 tesing
# =======================================================================================================================================



# warmup 1 tesing
# =======================================================================================================================================



# warmup 2 tesing
# =======================================================================================================================================