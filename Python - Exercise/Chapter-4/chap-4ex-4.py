# a program that asks for age and tells the stage of life

print('Enter your age = ')
age = int(input())

if age < 2:
    print('You are an infant')

elif age == 2 or age < 4:
    print('You are a toddler')

elif age == 4 or age < 13:
    print('You are a kid')

elif age == 13 or age < 20:
    print('You are a teenager')

elif age == 20 or age < 65:
    print('You are an adult')

else:
    print('You are an elder')
