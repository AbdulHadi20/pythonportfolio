"""
Chapter 6, Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

print('Enter the toppings you want to have for your pizza ')
print('Type quit to exit')

while True:
    topping = str(input())
    print(topping + 'will be added to your pizza.')

    if topping == 'quit':
        break

    else:
        print('You have selected the following toppings: \n ' + str(topping).title())
