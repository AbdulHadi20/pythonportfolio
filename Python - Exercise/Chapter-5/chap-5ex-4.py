"""
Chapter 5, Exercise 4: Rivers

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
"""

rivers = {                                                         # dictionary/glossary
    'Nile': 'Egypt',
    'Indus': 'Pakistan',
    'Amazon': 'Brazil'
}

print('Printing Key-Value pairs:')

for key, value in rivers.items():                                      # for loop to display key-value pairs
    print(f'\n Key: {key}')
    print(f'Value: {value}')

    print(f'The river {key} flows through {value}')

print('The following are included the set: ')

for river in rivers.keys():
    print(
    print(f"-{river.title()}")

print('\nThe following countries are included in theset: ')
for country in rivers.values():
  print(f"-{country.title()}") 
