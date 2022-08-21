"""This challenge requires creating a function that takes a user email and returns their username"""


def user_name():
    user_mail = input('enter your email: ')
    extract_user_name = user_mail.split('@')[0]
    return f'Your username is: {extract_user_name}'


print(user_name())

"""I had wanted to use regular expressions but it wasn't working because I couldn't figure out my regex syntax 
so had to resort to the slicing method"""
