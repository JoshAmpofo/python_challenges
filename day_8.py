"""This challenge is about creating a function that takes one parameter
and a list of numbers as an argument. The function then returns the diff between the largest even number in the list
and the smallest odd number in the list"""


def odd_even(num):
    even = []  # create an empty list to hold both odd and even values
    odd = []
    for i in num:  # create an iteration loop
        if i % 2 == 0:
            even.append(i)  # if even, add to even list
        if i % 2 != 0:
            odd.append(i)  # if odd, add to odd list
    return max(even) - min(odd)  # calculate the difference between the largest even num and smallest odd number


print(odd_even([1, 2, 4, 6]))
