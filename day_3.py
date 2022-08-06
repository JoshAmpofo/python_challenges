"""This challenge is to create a function that checks how many students are in school
and returns the number of students present"""

# Initializing dictionary
register = {'Micheal': 'yes', 'John': 'no', 'Peter': 'yes',
            'Mary': 'yes'}

# Creating dictionary function


def register_check(register):
    count = 0  # initializing count
    for key in register:  # setting for loop
        if register[key] == 'yes':  # selecting key values in dictionary
            count = count + 1
    return f'The total number of students present is {count}'


print(register_check(register))
