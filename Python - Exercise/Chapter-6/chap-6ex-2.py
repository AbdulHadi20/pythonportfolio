"""
Chapter 6, Exercise 2: Movie tickets

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
 the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket 
 is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
"""

print('What is your age?')
print('Type quit to exit')

age = 0

while True:

    age = input()
    if age == 'quit':
        break

    else:

        age = int(age)
        if age < 3:
            print('The ticket is FREE of cost for you.')

        elif 3 <= age <= 12:
            print('The ticket cost is $10.')

        elif age > 12:
            print('The ticket cost is $15.')
