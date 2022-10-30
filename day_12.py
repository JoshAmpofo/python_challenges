# Write a function that takes a string separated by dots and counts the dots

def count_dots(letters):
    count = 0  # set counter to hold value of each dot
    dots = list()  # create array to store individual element of function argument
    for i in letters:
        dots.append(letters)  # iterate through function argument and append each element to array
        if i == ".":  # check if item is equal to dot
            count += 1  # if equal, count and store count, each time increasing value
    return count  # return value of count


print("The number of dots is", count_dots("h.e.l.p."))  # function call
