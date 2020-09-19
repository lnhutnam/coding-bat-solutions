# =======================================================================================================================================
# VNU-HCM, University of Science
# Department Computer Science, Faculty of Information Technology
# Authors: Nhut-Nam Le (Tich Phan Suy Rong)
# © 2020


# list 1
# =======================================================================================================================================
"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""


import unittest


def first_last6(nums):
    return (False, True)[nums[0] == 6 or nums[len(nums) - 1] == 6]


# =======================================================================================================================================
"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""


def same_first_last(nums):
    if (len(nums) == 0):
        return False
    return (((False, True)[nums[0] == nums[len(nums) - 1]], True)[len(nums) == 1], False)[len(nums) == 0]


# =======================================================================================================================================
"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]
"""


def make_pi():
    return [3, 1, 4]


# =======================================================================================================================================
"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""


def common_end(a, b):
    return (False, True)[a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]]


# =======================================================================================================================================
"""
Given an array of ints length 3, return the sum of all the elements.


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""


def sum3(nums):
    return sum(nums)


# =======================================================================================================================================
"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""


def rotate_left3(nums):
    saved = nums[0]
    nums.remove(nums[0])
    nums.append(saved)
    return nums


# =======================================================================================================================================
"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""


def reverse3(nums):
    nums.reverse()
    return nums


# =======================================================================================================================================
"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""


def max_end3(nums):
    max_value = max(nums[0], nums[len(nums) - 1])
    return [max_value] * 3


# =======================================================================================================================================
"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""


def sum2(nums):
    return (sum(nums[:2]), sum(nums))[len(nums) <= 2]


# =======================================================================================================================================
"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""


def middle_way(a, b):
    return [a[1], b[1]]


# =======================================================================================================================================
"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""


def make_ends(nums):
    return (nums * 2, [nums[0], nums[len(nums) - 1]])[len(nums) > 1]


# =======================================================================================================================================
"""
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""


def has23(nums):
    return (False, True)[2 in nums or 3 in nums]


# list 2
# =======================================================================================================================================
"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""


def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


# =======================================================================================================================================
"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""


def big_diff(nums):
    return max(nums) - min(nums)


# =======================================================================================================================================
"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)


# =======================================================================================================================================
"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""


def sum13(nums):
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            result += nums[i]
            i += 1
    return result


# =======================================================================================================================================
"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


def sum67(nums):
    result = 0
    flag = False
    for num in nums:
        if num == 6:
            flag = True
        if (flag):
            if num == 7:
                flag = False
        else:
            result += num
    return result


# =======================================================================================================================================

"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

# =======================================================================================================================================


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
# =======================================================================================================================================
"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
"""


def make_bricks(small, big, goal):
    return ((False, True)[(goal - big * 5) <= small], (False, True)[(goal - (goal // 5) * 5) <= small])[goal // 5 <= big]


# =======================================================================================================================================
"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""


def lone_sum(a, b, c):
    #    if a == b:
    #        if a == c:
    #            return 0
    #        else:
    #            return c
    #    if a == c:
    #        return b
    #    if b == c:
    #        return a
    #    return a + b + c
    return (((a + b + c, a)[b == c], b)[a == c], (c, 0)[a == c])[a == b]


# =======================================================================================================================================
"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""


def lucky_sum(a, b, c):
    #    if a == 13:
    #         return 0
    #     if b == 13:
    #         return a
    #     if c == 13:
    #         return a + b
    #     return a + b + c
    return (((a + b + c, a + b)[c == 13], a)[b == 13], 0)[a == 13]


# =======================================================================================================================================
"""
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""


def fix_teen(n):
    return (0, n)[n < 13 or n > 19 or n == 15 or n == 16]


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


# =======================================================================================================================================
"""
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
"""


def round10(num):
    return (num - num % 10, num + (10 - num % 10))[num % 10 >= 5]


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# =======================================================================================================================================
"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""


def close_far(a, b, c):
    return (abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2 or abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2)


# =======================================================================================================================================
"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""


def make_chocolate(small, big, goal):
    return ((-1, goal - big * 5)[(goal - big * 5) <= small], (-1, (goal - (goal // 5) * 5))[(goal - (goal // 5) * 5) <= small])[goal // 5 <= big]


# =======================================================================================================================================
# string 1
"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

For example test case:
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""


def hello_name(name):
    return "Hello " + name + "!"


# =======================================================================================================================================


# =======================================================================================================================================

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
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""


def string_times(str, n):
    return str * n


# =======================================================================================================================================
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. 
Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""


def front_times(str, n):
    return (str[:len(str)] * n, str[:3] * n)[len(str) > 3]


# =======================================================================================================================================
"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""


def string_bits(str):
    result = ""
    i = 0
    while i < len(str):
        result += str[i]
        i += 2
    return result
