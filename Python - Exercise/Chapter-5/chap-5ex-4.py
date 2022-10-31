# a program to make a dictionary of 3 major rivers, print key-value seperately too

rivers = {
    'Nile': 'Egypt',
    'Indus': 'Pakistan',
    'Amazon': 'Brazil'
}

print('Printing Key-Value pairs:')

for key, value in rivers.items():
    print(f'\n Key: {key}')
    print(f'Value: {value}')

    print(f'The river {key} flows through {value}')
