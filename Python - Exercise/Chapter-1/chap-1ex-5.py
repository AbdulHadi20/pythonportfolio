"""
Chapter 1, Exercise 5: Compute area of circle

Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

print('Enter the radius of the circle = ')  # takes value from the user
radius = float(input())

pi = 3.14                                                                 
area = pi * radius * radius  # calcultaion

#output statement
print('The area of the circle with radius ' +
      str(radius) + 'units is ' + str(area) + 'sq.units')
