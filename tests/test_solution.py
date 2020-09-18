# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


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
from solutions.solutions import make_bricks
from solutions.solutions import lone_sum
from solutions.solutions import lucky_sum
from solutions.solutions import no_teen_sum
from solutions.solutions import round_sum

# string 1

# string 2

# warmup 1
from solutions.solutions import diff21
from solutions.solutions import front_back
from solutions.solutions import front3
from solutions.solutions import makes10
from solutions.solutions import missing_char
from solutions.solutions import monkey_trouble
from solutions.solutions import near_hundred
from solutions.solutions import not_string
from solutions.solutions import parrot_trouble
from solutions.solutions import pos_neg
from solutions.solutions import sleep_in
from solutions.solutions import sum_double
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
class TestMakeBricks(unittest.TestCase):
    def test_case_00(self):
        # make_bricks(3, 1, 8) → True
        self.assertEqual(make_bricks(3, 1, 8), True)

    def test_case_01(self):
        # make_bricks(3, 1, 9) → False
        self.assertEqual(make_bricks(3, 1, 9), False)

    def test_case_02(self):
        # make_bricks(3, 2, 10) → True
        self.assertEqual(make_bricks(3, 2, 10), True)

    def test_case_03(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 10), True)

    def test_case_04(self):
        # make_bricks(3, 2, 9) → False
        self.assertEqual(make_bricks(3, 2, 9), False)

    def test_case_05(self):
        # make_bricks(6, 1, 11) → True
        self.assertEqual(make_bricks(6, 1, 11), True)

    def test_case_06(self):
        # make_bricks(6, 0, 11) → False
        self.assertEqual(make_bricks(6, 0, 11), False)

    def test_case_07(self):
        # make_bricks(1, 4, 11) → True
        self.assertEqual(make_bricks(1, 4, 11), True)

    def test_case_08(self):
        # make_bricks(0, 3, 10) → True
        self.assertEqual(make_bricks(0, 3, 10), True)

    def test_case_09(self):
        # make_bricks(1, 4, 12) → False
        self.assertEqual(make_bricks(1, 4, 12), False)

    def test_case_10(self):
        # make_bricks(3, 1, 7) → True
        self.assertEqual(make_bricks(3, 1, 7), True)

    def test_case_11(self):
        # make_bricks(1, 1, 7) → False
        self.assertEqual(make_bricks(1, 1, 7), False)

    def test_case_12(self):
        # make_bricks(2, 1, 7) → True
        self.assertEqual(make_bricks(2, 1, 7), True)

    def test_case_13(self):
        # make_bricks(7, 1, 11) → True
        self.assertEqual(make_bricks(7, 1, 11), True)

    def test_case_14(self):
        # make_bricks(7, 1, 8) → True
        self.assertEqual(make_bricks(7, 1, 8), True)

    def test_case_15(self):
        # make_bricks(7, 1, 13) → False
        self.assertEqual(make_bricks(7, 1, 13), False)

    def test_case_16(self):
        # make_bricks(43, 1, 46) → True
        self.assertEqual(make_bricks(43, 1, 46), True)

    def test_case_17(self):
        # make_bricks(40, 1, 46) → False
        self.assertEqual(make_bricks(40, 1, 46), False)

    def test_case_18(self):
        # make_bricks(40, 2, 47) → True
        self.assertEqual(make_bricks(40, 2, 47), True)

    def test_case_19(self):
        # make_bricks(40, 2, 50) → True
        self.assertEqual(make_bricks(40, 2, 50), True)

    def test_case_20(self):
        # make_bricks(40, 2, 52) → False
        self.assertEqual(make_bricks(40, 2, 52), False)

    def test_case_21(self):
        # make_bricks(22, 2, 33) → False
        self.assertEqual(make_bricks(22, 2, 33), False)

    def test_case_22(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 8), True)

    def test_case_23(self):
        # make_bricks(0, 2, 10) → True
        self.assertEqual(make_bricks(0, 2, 10), True)

    def test_case_24(self):
        # make_bricks(1000000, 1000, 1000100) → True
        self.assertEqual(make_bricks(1000000, 1000, 1000100), True)

    def test_case_25(self):
        # make_bricks(2, 1000000, 100003) → False
        self.assertEqual(make_bricks(2, 1000000, 100003), False)

    def test_case_26(self):
        # make_bricks(3, 2, 8) → True
        self.assertEqual(make_bricks(3, 2, 8), True)

    def test_case_27(self):
        # make_bricks(20, 0, 19) → True
        self.assertEqual(make_bricks(20, 0, 19), True)

    def test_case_28(self):
        # make_bricks(20, 0, 21) → False
        self.assertEqual(make_bricks(20, 0, 21), False)

    def test_case_29(self):
        # make_bricks(20, 4, 51) → False
        self.assertEqual(make_bricks(20, 4, 51), False)

    def test_case_30(self):
        # make_bricks(20, 4, 39) → True
        self.assertEqual(make_bricks(20, 4, 39), True)


class TestLoneSum(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def test_case_01(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def test_case_02(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)

    def test_case_03(self):
        self.assertEqual(lone_sum(9, 2, 2), 9)

    def test_case_04(self):
        self.assertEqual(lone_sum(2, 2, 9), 9)

    def test_case_05(self):
        self.assertEqual(lone_sum(2, 9, 2), 9)

    def test_case_05(self):
        self.assertEqual(lone_sum(2, 9, 3), 14)

    def test_case_06(self):
        self.assertEqual(lone_sum(4, 2, 3), 9)

    def test_case_02(self):
        self.assertEqual(lone_sum(1, 3, 1), 3)


class TestLuckyNum(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)

    def test_case_01(self):
        self.assertEqual(lucky_sum(1, 2, 13), 3)

    def test_case_02(self):
        self.assertEqual(lucky_sum(1, 13, 3), 1)

    def test_case_03(self):
        self.assertEqual(lucky_sum(1, 13, 13), 1)

    def test_case_04(self):
        self.assertEqual(lucky_sum(6, 5, 2), 13)

    def test_case_05(self):
        self.assertEqual(lucky_sum(13, 2, 3), 0)

    def test_case_06(self):
        self.assertEqual(lucky_sum(13, 2, 13), 0)

    def test_case_07(self):
        self.assertEqual(lucky_sum(13, 13, 2), 0)

    def test_case_08(self):
        self.assertEqual(lucky_sum(9, 4, 13), 13)

    def test_case_09(self):
        self.assertEqual(lucky_sum(8, 13, 2), 8)

    def test_case_10(self):
        self.assertEqual(lucky_sum(7, 2, 1), 10)

    def test_case_11(self):
        self.assertEqual(lucky_sum(3, 3, 13), 6)


class TestNoTeenSum(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(no_teen_sum(1, 2, 3), 6)

    def test_case_01(self):
        self.assertEqual(no_teen_sum(2, 13, 1), 3)

    def test_case_02(self):
        self.assertEqual(no_teen_sum(2, 1, 14), 3)

    def test_case_03(self):
        self.assertEqual(no_teen_sum(2, 1, 15), 18)

    def test_case_04(self):
        self.assertEqual(no_teen_sum(2, 1, 16), 19)

    def test_case_05(self):
        self.assertEqual(no_teen_sum(2, 1, 17), 3)

    def test_case_06(self):
        self.assertEqual(no_teen_sum(17, 1, 2), 3)

    def test_case_07(self):
        self.assertEqual(no_teen_sum(2, 15, 2), 19)

    def test_case_08(self):
        self.assertEqual(no_teen_sum(16, 17, 18), 16)

    def test_case_09(self):
        self.assertEqual(no_teen_sum(17, 18, 19), 0)

    def test_case_10(self):
        self.assertEqual(no_teen_sum(15, 16, 1), 32)

    def test_case_11(self):
        self.assertEqual(no_teen_sum(15, 15, 19), 30)

    def test_case_12(self):
        self.assertEqual(no_teen_sum(15, 19, 16), 31)

    def test_case_13(self):
        self.assertEqual(no_teen_sum(5, 17, 18), 5)

    def test_case_14(self):
        self.assertEqual(no_teen_sum(17, 18, 16), 16)

    def test_case_15(self):
        self.assertEqual(no_teen_sum(17, 19, 18), 0)


class TestRoundSum(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_case_01(self):
        self.assertEqual(round_sum(12, 13, 14), 30)

    def test_case_02(self):
        self.assertEqual(round_sum(6, 4, 4), 10)

    def test_case_03(self):
        self.assertEqual(round_sum(4, 6, 5), 20)

    def test_case_04(self):
        self.assertEqual(round_sum(4, 4, 6), 10)

    def test_case_05(self):
        self.assertEqual(round_sum(9, 4, 4), 10)

    def test_case_06(self):
        self.assertEqual(round_sum(0, 0, 1), 0)

    def test_case_07(self):
        self.assertEqual(round_sum(0, 9, 0), 10)

    def test_case_08(self):
        self.assertEqual(round_sum(10, 10, 19), 40)

    def test_case_09(self):
        self.assertEqual(round_sum(20, 30, 40), 90)

    def test_case_10(self):
        self.assertEqual(round_sum(45, 21, 30), 100)

    def test_case_11(self):
        self.assertEqual(round_sum(23, 11, 26), 60)

    def test_case_12(self):
        self.assertEqual(round_sum(23, 24, 25), 70)

    def test_case_13(self):
        self.assertEqual(round_sum(25, 24, 25), 80)

    def test_case_14(self):
        self.assertEqual(round_sum(23, 24, 29), 70)

    def test_case_15(self):
        self.assertEqual(round_sum(11, 24, 36), 70)

    def test_case_16(self):
        self.assertEqual(round_sum(24, 36, 32), 90)

    def test_case_17(self):
        self.assertEqual(round_sum(14, 12, 26), 50)

    def test_case_18(self):
        self.assertEqual(round_sum(12, 10, 24), 40)



# string 1 tesing
# =======================================================================================================================================


# string 2 tesing
# =======================================================================================================================================


# warmup 1 tesing
# =======================================================================================================================================
class TestDiff21(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(diff21(19), 2)

    def test_case_01(self):
        self.assertEqual(diff21(10), 11)

    def test_case_02(self):
        self.assertEqual(diff21(21), 0)

    def test_case_03(self):
        self.assertEqual(diff21(22), 2)

    def test_case_04(self):
        self.assertEqual(diff21(25), 8)

    def test_case_05(self):
        self.assertEqual(diff21(30), 18)

    def test_case_06(self):
        self.assertEqual(diff21(0), 21)

    def test_case_07(self):
        self.assertEqual(diff21(1), 20)

    def test_case_08(self):
        self.assertEqual(diff21(-1), 22)

    def test_case_09(self):
        self.assertEqual(diff21(-2), 23)

    def test_case_10(self):
        self.assertEqual(diff21(2), 19)

    def test_case_11(self):
        self.assertEqual(diff21(50), 58)


class TestFrontBack(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(front_back('code'), 'eodc')

    def test_case_01(self):
        self.assertEqual(front_back('a'), 'a')

    def test_case_02(self):
        self.assertEqual(front_back('ab'), 'ba')

    def test_case_03(self):
        self.assertEqual(front_back('abc'), 'cba')

    def test_case_04(self):
        self.assertEqual(front_back(''), '')

    def test_case_05(self):
        self.assertEqual(front_back('Chocolate'), 'ehocolatC')

    def test_case_06(self):
        self.assertEqual(front_back('aavJ'), 'Java')

    def test_case_07(self):
        self.assertEqual(front_back('hello'), 'oellh')


class TestFront3(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(front3('Java'), 'JavJavJav')

    def test_case_01(self):
        self.assertEqual(front3('Chocolate'), 'ChoChoCho')

    def test_case_02(self):
        self.assertEqual(front3('abc'), 'abcabcabc')

    def test_case_03(self):
        self.assertEqual(front3('abcXYZ'), 'abcabcabc')

    def test_case_04(self):
        self.assertEqual(front3('ab'), 'ababab')

    def test_case_05(self):
        self.assertEqual(front3('a'), 'aaa')

    def test_case_06(self):
        self.assertEqual(front3(''), '')


class TestMake10(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(makes10(9, 10), True)

    def test_case_01(self):
        self.assertEqual(makes10(9, 9), False)

    def test_case_02(self):
        self.assertEqual(makes10(1, 9), True)

    def test_case_03(self):
        self.assertEqual(makes10(10, 1), True)

    def test_case_04(self):
        self.assertEqual(makes10(10, 10), True)

    def test_case_05(self):
        self.assertEqual(makes10(8, 2), True)

    def test_case_06(self):
        self.assertEqual(makes10(8, 3), False)

    def test_case_07(self):
        self.assertEqual(makes10(10, 42), True)

    def test_case_00(self):
        self.assertEqual(makes10(12, -2), True)


class TestMissingChar(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(missing_char('kitten', 1), 'ktten')

    def test_case_01(self):
        self.assertEqual(missing_char('kitten', 0), 'itten')

    def test_case_02(self):
        self.assertEqual(missing_char('kitten', 4), 'kittn')

    def test_case_04(self):
        self.assertEqual(missing_char('Hi', 0), 'i')

    def test_case_05(self):
        self.assertEqual(missing_char('Hi', 1), 'H')

    def test_case_06(self):
        self.assertEqual(missing_char('code', 0), 'ode')

    def test_case_07(self):
        self.assertEqual(missing_char('code', 1), 'cde')

    def test_case_08(self):
        self.assertEqual(missing_char('code', 2), 'coe')

    def test_case_09(self):
        self.assertEqual(missing_char('code', 3), 'cod')

    def test_case_10(self):
        self.assertEqual(missing_char('chocolate', 8), 'chocolat')


class TestMonkeyTrouble(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(monkey_trouble(True, True), True)

    def test_case_01(self):
        self.assertEqual(monkey_trouble(False, False), True)

    def test_case_02(self):
        self.assertEqual(monkey_trouble(True, False), False)

    def test_case_03(self):
        self.assertEqual(monkey_trouble(False, True), False)


class TestNearHundred(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(near_hundred(93), True)

    def test_case_01(self):
        self.assertEqual(near_hundred(90), True)

    def test_case_02(self):
        self.assertEqual(near_hundred(89), False)

    def test_case_03(self):
        self.assertEqual(near_hundred(110), True)

    def test_case_04(self):
        self.assertEqual(near_hundred(111), False)

    def test_case_05(self):
        self.assertEqual(near_hundred(121), False)

    def test_case_06(self):
        self.assertEqual(near_hundred(-101), False)

    def test_case_07(self):
        self.assertEqual(near_hundred(-209), False)

    def test_case_08(self):
        self.assertEqual(near_hundred(190), True)

    def test_case_09(self):
        self.assertEqual(near_hundred(209), True)

    def test_case_10(self):
        self.assertEqual(near_hundred(0), False)

    def test_case_11(self):
        self.assertEqual(near_hundred(5), False)

    def test_case_12(self):
        self.assertEqual(near_hundred(-50), False)

    def test_case_13(self):
        self.assertEqual(near_hundred(191), True)

    def test_case_14(self):
        self.assertEqual(near_hundred(189), False)

    def test_case_15(self):
        self.assertEqual(near_hundred(200), True)

    def test_case_16(self):
        self.assertEqual(near_hundred(210), True)

    def test_case_17(self):
        self.assertEqual(near_hundred(211), False)

    def test_case_18(self):
        self.assertEqual(near_hundred(290), False)


class TestNotString(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(not_string('candy'), 'not candy')

    def test_case_01(self):
        self.assertEqual(not_string('x'), 'not x')

    def test_case_02(self):
        self.assertEqual(not_string('not bat'), 'not bat')

    def test_case_03(self):
        self.assertEqual(not_string('bat'), "not bat")

    def test_case_04(self):
        self.assertEqual(not_string('not'), "not")

    def test_case_05(self):
        self.assertEqual(not_string('is not'), "not is not")

    def test_case_06(self):
        self.assertEqual(not_string('no'), "not no")


class TestParrotTrouble(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(parrot_trouble(True, 6), True)

    def test_case_01(self):
        self.assertEqual(parrot_trouble(True, 7), False)

    def test_case_03(self):
        self.assertEqual(parrot_trouble(False, 6), False)

    def test_case_04(self):
        self.assertEqual(parrot_trouble(False, 21), False)

    def test_case_05(self):
        self.assertEqual(parrot_trouble(False, 20), False)

    def test_case_06(self):
        self.assertEqual(parrot_trouble(True, 23), True)

    def test_case_07(self):
        self.assertEqual(parrot_trouble(False, 23), False)

    def test_case_08(self):
        self.assertEqual(parrot_trouble(True, 20), False)

    def test_case_09(self):
        self.assertEqual(parrot_trouble(False, 12), False)


class TestPosNeg(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(pos_neg(1, -1, False), True)

    def test_case_01(self):
        self.assertEqual(pos_neg(-1, 1, False), True)

    def test_case_02(self):
        self.assertEqual(pos_neg(-4, -5, True), True)

    def test_case_03(self):
        self.assertEqual(pos_neg(-4, -5, False), False)

    def test_case_04(self):
        self.assertEqual(pos_neg(-4, 5, False), True)

    def test_case_05(self):
        self.assertEqual(pos_neg(-4, 5, True), False)

    def test_case_06(self):
        self.assertEqual(pos_neg(1, 1, False), False)

    def test_case_07(self):
        self.assertEqual(pos_neg(-1, -1, False), False)

    def test_case_08(self):
        self.assertEqual(pos_neg(1, -1, True), False)

    def test_case_09(self):
        self.assertEqual(pos_neg(-1, 1, True), False)

    def test_case_10(self):
        self.assertEqual(pos_neg(1, 1, True), False)

    def test_case_11(self):
        self.assertEqual(pos_neg(-1, -1, True), True)

    def test_case_12(self):
        self.assertEqual(pos_neg(5, -5, False), True)

    def test_case_13(self):
        self.assertEqual(pos_neg(-6, 6, False), True)

    def test_case_14(self):
        self.assertEqual(pos_neg(-5, -6, False), False)

    def test_case_15(self):
        self.assertEqual(pos_neg(-2, -1, False), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(1, 2, False), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(-5, 6, True), False)

    def test_case_16(self):
        self.assertEqual(pos_neg(-5, -5, True), True)


class TestSleepIn(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sleep_in(False, False), True)

    def test_case_01(self):
        self.assertEqual(sleep_in(True, False), False)

    def test_case_02(self):
        self.assertEqual(sleep_in(False, True), True)


class TestSumDboule(unittest.TestCase):
    def test_case_00(self):
        self.assertEqual(sum_double(1, 2), 3)

    def test_case_01(self):
        self.assertEqual(sum_double(3, 2), 5)

    def test_case_02(self):
        self.assertEqual(sum_double(2, 2), 8)

    def test_case_03(self):
        self.assertEqual(sum_double(-1, 0), -1)

    def test_case_04(self):
        self.assertEqual(sum_double(3, 3), 12)

    def test_case_05(self):
        self.assertEqual(sum_double(0, 0), 0)

    def test_case_06(self):
        self.assertEqual(sum_double(0, 1), 1)

    def test_case_07(self):
        self.assertEqual(sum_double(3, 4), 7)

# warmup 2 tesing
# =======================================================================================================================================
