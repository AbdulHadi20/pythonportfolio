"""
Chapter 1, Extra Pt. 2:

Write a program that takes the values from the user and prints the area and the perimeter of a rectangle
"""

# for the area of the rectangle

# takes the length from the user
print('Enter the length of the sides of the rectangle = ')
l = int(input())

print('Enter the width of the rectangle = ')  # takes the width from the user
w = int(input())

area = l * w                   # calculation for finding area
perimeter = 2*l*w              # calculation for finding perimeter

print('The area of the rectangle is = ' + str(area))  # prints the area
print('The perimeter of thr rectangle is = ' +
      str(perimeter))  # prints the perimeter
