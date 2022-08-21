
"""This challenge involves creating a range out of a single value and returning the range as a string
separated by dots"""


def string_range(num):
    x = [str(n) for n in range(num)]  # use list comprehension to create range
    x = '.'.join(x)  # use join method to separate values with a dot
    return x


print(string_range(6))

