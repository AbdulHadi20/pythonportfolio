"""
Chapter 1, Extra Pt. 1:
A program to ask the values from the user, then printing the area and the perimeter of a square
"""

# taking the value from the user
print('Enter the length of the side of the square = ')
s = int(input())

area = s * s    # mathematical calculation for area of square

print('The area of the square with sides of ' + str(s) +
      ' units is ' + str(area) + 'sq. units')  # prints the area

perimeter = 4 * s  # calculation for the perimeter of the square

# prints the perimeter
print('The perimeter of the square with sides of ' +
      str(s) + ' units is ' + str(perimeter))
