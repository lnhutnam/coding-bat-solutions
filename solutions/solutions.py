
# list 1


# list 2

# logic 1
# =======================================================================================================================================
"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

Test case for example:
alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""


def alarm_clock(day, vacation):
    return (('7:00', '10:00')[day == 0 or day == 6], ('10:00', 'off')[day == 0 or day == 6])[vacation]


# =======================================================================================================================================
"""
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

For example test case:
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""


def caught_speeding(speed, is_birthday):
    return (((0, 1)[61 <= speed <= 80], 2)[speed >= 81], ((0, 1)[66 <= speed <= 85], 2)[speed >= 86])[is_birthday]


# =======================================================================================================================================
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


def cigar_party(cigars, is_weekend):
    return ((False, True)[is_weekend and cigars >= 40], True)[40 <= cigars <= 60]


# =======================================================================================================================================
"""
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. 
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
Otherwise the result is 1 (maybe).

For example test case:
date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""


def date_fashion(you, date):
    return ((1, 2)[you >= 8 or date >= 8], 0)[you <= 2 or date <= 2]


# =======================================================================================================================================
"""
Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""


def in1to10(n, outside_mode):
    return ((False, True)[(outside_mode == True and (n <= 1 or n >= 10))], True)[n in range(1, 11) and outside_mode == False]


# =======================================================================================================================================
"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

Test case for example:
love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""


def love6(a, b):
    return (False, True)[a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6]


# =======================================================================================================================================
"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""


def near_ten(num):
    return (False, True)[num % 10 <= 2 or num % 10 >= 8]


# =======================================================================================================================================
"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""


def sorta_sum(a, b):
    return (a + b, 20)[a + b in range(10, 20)]


# =======================================================================================================================================
"""
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

For example test case:
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

"""


def squirrel_play(temp, is_summer):
    return (60 <= temp <= 90, 60 <= temp <= 100)[is_summer]

# logic 2

# string 1

# string 2


# warmup 1
# =======================================================================================================================================
"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

For example test case:
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""


def diff21(n):
    return (2*abs(n - 21), abs(n - 21))[n < 21]


# =======================================================================================================================================
"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(str):
    if (len(str) <= 1):
        return str
    else:
        return str[len(str) - 1] + str[1: len(str) - 1] + str[0]


# =======================================================================================================================================
"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""


def front3(str):
    return (str[:3] + str[:3] + str[:3], str[:len(str)] + str[:len(str)] + str[:len(str)])[len(str) < 3]


# =======================================================================================================================================
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""


def makes10(a, b):
    return (False, True)[(a == 10) or (b == 10) or (a + b == 10)]


# =======================================================================================================================================
"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""


def missing_char(str, n):
    return str[:n] + str[(n+1):]


# =======================================================================================================================================
"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""


def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))


# =======================================================================================================================================
"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""


def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


# =======================================================================================================================================
"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""


def not_string(str):
    return ("not " + str, str)[str[:3] == "not"]


# =======================================================================================================================================
"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""


def parrot_trouble(talking, hour):
    return (False, (hour < 7 or hour > 20))[talking]


# =======================================================================================================================================
"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
pos_neg(-4, -5, False) → False
pos_neg(-4, 5, False) → True
pos_neg(-4, 5, True) → False
pos_neg(1, 1, False) → False
pos_neg(-1, -1, False) → False
pos_neg(1, -1, True) → False
pos_neg(-1, 1, True) → False
pos_neg(1, 1, True) → False
pos_neg(-1, -1, True) → True
pos_neg(5, -5, False) → True
pos_neg(-6, 6, False) → True
pos_neg(-5, -6, False) → False
pos_neg(-2, -1, False) → False
pos_neg(1, 2, False) → False
pos_neg(-5, 6, True) → False
pos_neg(-5, -5, True) → True
"""


def pos_neg(a, b, negative):
    return ((False, True)[a*b < 0], (False, True)[a < 0 and b < 0])[negative == True]


# =======================================================================================================================================
"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
    return (not weekday or vacation)


# =======================================================================================================================================
"""
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.

For example test case:
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""


def sum_double(a, b):
    return ((a+b), 2*(a+b))[a == b]
# =======================================================================================================================================


# warmup 2
# =======================================================================================================================================
