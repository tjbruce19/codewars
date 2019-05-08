"""
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below),
a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.
"""
def _check_sequential(number):
    number_list = list(str(number))
    if int(number_list[-1]) == 0:
        if int(number_list[-2]) != 9 and int(number_list[-2]) != 1:
            return False
        else:
            number_list = number_list[:-1]
    minus_v = int(number_list[1]) - int(number_list[0])
    if abs(minus_v) == 1:
        for i in range(1, len(number_list)):
            if int(number_list[i]) - int(number_list[i - 1]) != minus_v:
                return False
    else:
        return False
    return True

def _check_palindrome(number):
    number_list = list(str(number))
    while len(number_list) > 1:
        if number_list.pop(0) != number_list.pop(-1):
            return False
    return True

def _check_interesting_number(number, awesome_phrases):
    if number < 100:
        return False
    return True if number in awesome_phrases or number % 100 == 0 or _check_sequential(number) or _check_palindrome(
        number) else False


def is_interesting(number, awesome_phrases):
    if _check_interesting_number(number, awesome_phrases):
        return 2
    elif _check_interesting_number(number+1, awesome_phrases) or _check_interesting_number(number+2, awesome_phrases):
        return 1
    return 0

print(is_interesting(67888,[]))
# print(_check_palindrome(11211))
# print(_check_sequential(3210))
