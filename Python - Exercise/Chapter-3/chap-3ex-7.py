# a program to sort the contents of lists in different orders

places = ['New York', 'Toronto', 'Doha', 'Islamabad', 'Zurich', 'London']
print(places)
print('\n')

print(sorted(places))  # alphabetical order list
print(places)  # checking the original list

print('\n')

print(sorted(places, reverse=True))  # reverse order list
print(places)  # checking the original list

print('\n')

places = list(reversed(places))  # reversing the order
print(places)  # prints reversed order

print('\n')

places = list(reversed(places))  # reversing again back to its original form
print(places)  # prints original order

print('\n')

places.sort()  # changes the original list to alphabetical order
print(places)  # prints the changes in the order of the list

places.sort(reverse=True)  # changes to reversed alphabetical order
print(places)  # prints the changes made
