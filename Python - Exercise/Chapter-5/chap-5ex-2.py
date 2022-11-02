"""
Chapter 5, Exercise 2: Glossary

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between
each word-meaning pair in your output.    
"""

glossary = {'loop':
            'a loop is an operation in programming that repeats a certain statement until a certain condition is met',
            'concatenation':
            'it refers to the joining of multiple strings to make a single long string.',
            'bin()':
            'it is the function, used to find the binary value of a certain character.',
            'IDE':
            'IDE stands for integrated development environment. It is a space built for coders to run, save, debug, etc. their code in a single environment. ',
            'GitHub': 'It is a platform where we can store our code projects in a cloud based repositories, collaborate with other developers and control the versions.'}

print('Loop:')
print(glossary['loop'])
print('\n')

print('Concatenation:')
print(glossary['concatenation'])
print('\n')

print('bin():')
print(glossary['bin()'])
print('\n')

print('IDE:')
print(glossary['IDE'])
print('\n')

print('GitHub:')
print(glossary['GitHub'])
