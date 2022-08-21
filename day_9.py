"""This challenge requires creating a function that takes a string of
numbers and returns the biggest odd number in the list"""


def biggest_odd(num):
    x = [i for i in num if int(i) % 2 != 0]
    return max(x)


print(biggest_odd('23569'))
