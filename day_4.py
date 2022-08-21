"""This challenge takes two parameters and checks to see if they are floats.
If one value is a float, the fxn return 1, else if both are floats,
the fxn returns 2"""

# comparison tables come in handy in this function.


def only_floats(a, b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0


print(only_floats(12.1, 23))

# Had a little help from 50 days of python challenges book
