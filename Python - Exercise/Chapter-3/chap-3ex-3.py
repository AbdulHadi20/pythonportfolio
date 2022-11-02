"""
Chapter 3, Exercise 3: Your Own List

Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""

transport_modes = ['car', 'bus', 'metro', 'boat'] # list of transportations

print('Travelling by ' + transport_modes[0].title() + ' is really easy.')  # printing each means of transport with a specific msg
print('I travel to the university by ' +
      transport_modes[1].title() + ' everyday.')
print('My favorite means of transportation is travelling by ' +
      transport_modes[2].title())
print('Travelling by ' + transport_modes[3].title() + ' is really long.')
