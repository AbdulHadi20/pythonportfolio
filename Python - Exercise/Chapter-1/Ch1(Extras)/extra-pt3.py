"""
Chapter 1, Extra Pt. 3:

Write a program that performs the basic arithmetic opertaions
"""

# takes first number and stores in var. a
print('Enter a number = ')
a = int(input())

# takes second number and stores in var. b
print('Enter another number = ')
b = int(input())

add = a + b  # addition calculation
sub = a - b  # subtraction calculation
mul = a * b  # multiplication calculation
div = a / b  # division calculation
mod = a % b  # modulus calculation

print('The addition of the two numbers is ' + str(add))            # the outputs
print('The subtraction of the two numbers is ' + str(sub))
print('The multiplication of the two numbers is ' + str(mul))
print('The division of the two numbers is ' + str(div))
print('The modulus of the two numbers is ' + str(mod))
