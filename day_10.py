"""This challenge involves writing a function that takes a password input
from a user and hides the password, returning the length of the input to the user"""


def hide_password():
    user = input('enter your name: ')
    return f"Your password is {len(user) * '*'} and it's {len(user)} characters long"


print(hide_password())
