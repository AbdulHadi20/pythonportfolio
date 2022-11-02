"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at 
least three times. Add code near the beginning of your program to print a message saying the deli has run out
of pastrami, and then use a while loop to remove alloccurrences of 'pastrami' from sandwich_orders. Make sure
no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['veggie', 'grilled cheese', 'chicken',
                   'beef', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print('The deli has run out of pastrami.')

for sandwich in sandwich_orders:
    if sandwich == 'pastrami':
        sandwich_orders.remove(sandwich)

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your ' + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\n')
print('Sandwich orders:')

for sandwich in finished_sandwiches:
    print(sandwich, 'Sandwich')

print(sandwich_orders)
