"""
Chapter 4, Exercise 3: Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

# in this section, the first condition is true
alien_color = 'blue'

if alien_color == 'blue':
    print('You have earned 5 points.')

elif alien_color == 'white':
    print('You have earned 10 points.')

else:
    print('You have earned 15 points.')

# in this section, the second condition is true
alien_color = 'white'

if alien_color == 'blue':
    print('You have earned 5 points.')

elif alien_color == 'white':
    print('You have earned 10 points.')

else:
    print('You have earned 15 points.')

# in this section, the last condition is true
alien_color = 'brown'

if alien_color == 'blue':
    print('You have earned 5 points.')

elif alien_color == 'white':
    print('You have earned 10 points.')

else:
    print('You have earned 15 points.')
