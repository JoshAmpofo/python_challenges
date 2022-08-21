"""This challenge is to create a function that takes no argument but asks user to input a price
and discount of the product. The function then returns the new price after applying discount"""


def my_discount():
    user_price = int(input('Enter price of product: '))
    user_discount = int(input('Enter discount: '))
    discount_price = (user_discount/100)*user_price
    new_price = user_price - discount_price
    return f'The new price after applying discount is {new_price}'


print(my_discount())
