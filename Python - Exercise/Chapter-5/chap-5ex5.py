"""
Chapter 5, Exercise 5: Pets


Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about
each pet.
   
"""
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
