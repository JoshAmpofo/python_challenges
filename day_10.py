"""This challenge involves writing a function that takes a password input
from a user and hides the password, returning the length of the input to the user"""


# def hide_password():
#     user = input('enter your name: ')
#     return f"Your password is {len(user) * '*'} and it's {len(user)} characters long"
#
#
# print(hide_password())

#####################################################################
def convert_numbers(num):
    new_list = []
    for num in num:
        new_list.append('{:,}'.format(num))
    return new_list


print(convert_numbers([1000000, 2356989, 2354672, 9878098]))

