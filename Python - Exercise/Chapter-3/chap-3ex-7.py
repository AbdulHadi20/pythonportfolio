"""
Chapter 3, Exercise 7: Seeing the world

Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

places = ['New York', 'Toronto', 'Doha', 'Islamabad', 'Zurich', 'London']      # list of places 
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
