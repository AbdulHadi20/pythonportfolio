# making several dictionaries, storing them in a list, then printing using loops

pet_1 = {
    'animal': 'cat',
    'owner': 'AbdulHadi',
    'pet-color': 'ginger'}

pet_2 = {
    'animal': 'parrot',
    'owner': 'Asma',
    'pet-color': 'green'
}

pet_3 = {
    'animal': 'dog',
    'owner': 'Raphael',
    'pet-color': 'light brown'
}

pet_4 = {
    'animal': 'lion',
    'owner': 'Harris',
    'pet-color': 'white'
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(pet)

    print('\n')
