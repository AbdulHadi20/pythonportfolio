"""
Chapter 4, Exercise 1: Alien Colors #1

Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""

# in this section, the condition is true
alien_color = 'green'

if alien_color == 'green':
    print('Congratulations, you have earned 5 points.')


# in this section, the condtition is false, therefore there will be no output
alien_color = 'blue'

if alien_color == 'green':
    print('Congratulations, you have earned 5 points.')
