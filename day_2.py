"""This function takes a list of strings as an argument and converts it
to integers and sums the list"""


def convert_add(list1):
    result = [int(item) for item in list1]  # list comprehension
    return sum(result)


print(convert_add(['1', '3', '5']))

"""This link provided help in solving this challenge!
https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int#:~:text=There%20are%20several
%20methods%20to%20convert%20string%20numbers,map%20%28int%2C%20results%29%20%3E%3E%3E%20results%20%
5B1%2C%202%2C%203%5D"""

# Alternative Approach - Expanded version

def convert_add(list1):
    new_list = []
    for item in list1:
        new_list.append(int(item))
    return sum(new_list)


print(convert_add(['1', '3', '5']))
