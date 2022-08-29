"""This challenge involves creating a function that compares the character and length of two strings returning true
if they are the same and false if not"""


def equal_strings(str1, str2):
    str_equal = sorted(str1) == sorted(str2)
    return str_equal


print(equal_strings('panda', 'penguin'))
