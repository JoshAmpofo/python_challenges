"""This function checks to see if a number is divisible by 5.
If divisible, the function returns the square root of the number. If not, returns the remainder of the division"""

import math


def divide_or_square(number):
    if number % 5 == 0:
        return f'The square root of the number is {math.sqrt(number)}'
    elif number % 5 != 0:
        return f'The remainder of the division is {math.remainder(number, 5)}'


print(divide_or_square(13))


# Alternative Approach

def divide_or_square(user_input):
    if user_input % 5 == 0:
        sqrt = user_input ** 0.5
        return f'Square root of the number is {sqrt}'
    else:
        remainder = user_input % 5
        return f'Remainder of division is {remainder}'


print(divide_or_square(13))

