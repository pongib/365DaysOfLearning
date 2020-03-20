# Define the `char_range` generator here
def char_range(start, end, step=1):
    start_digit = ord(start)
    end_digit = ord(end)
    if start_digit <= end_digit:
        while start_digit <= end_digit:
            yield chr(start_digit)
            start_digit += step
    else:
        while start_digit >= end_digit:
            yield chr(start_digit)
            start_digit -= step


# solution
# def char_range(start, stop, step=1):
#     stop_modifier = 1
#     start_code = ord(start)
#     stop_code = ord(stop)

#     if start_code > stop_code:
#         step *= -1
#         stop_modifier *= -1

#     for value in range(start_code, stop_code + stop_modifier, step):
#         yield chr(value)

# Tests to verify the implementation of char_range
# *Do not modify
##################################################

# Ensure that `char_range` is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"1.Expected char_range to be a generator function but was not."

# Ensure that the result *does* includes the stop character
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"2.Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"

# Iterate backwards if the start code point is higher than the stop code point

assert list(char_range("e", "a")) == [
    "e",
    "d",
    "c",
    "b",
    "a",
], f"3.Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"

# Properly step if a step value is provided

assert list(char_range("a", "e", 2)) == [
    "a",
    "c",
    "e",
], f"4.Expected ['a', 'c', 'e'] but got {repr(list(char_range('a', 'e', 2)))}"

# Step properly if the start code point is higher than the stop code point

assert list(char_range("e", "a", 2)) == [
    "e",
    "c",
    "a",
], f"5.Expected ['e', 'c', 'a'] but got {repr(list(char_range('e', 'a', 2)))}"

