"""
Chapter 2, Exercise 3: Stripping names

Tidy up the code to make it easier to understand
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

# use of lstrip()

word_1 = '                 Python'
new_word_1 = word_1.lstrip()
print(word_1)
print(new_word_1)

# use of rstrip()

word_2 = 'Python                     is cool'
new_word_2 = word_2.rstrip()
print(word_2)
print(new_word_2)

# use of strip()

word_3 = '               Nice work             '
new_word_3 = word_3.strip()
print(word_3)
print(new_word_3)

# use of \n

print('Friends I made during the first month of the semester: \n Asma \n Joe \n Obaid \n Faiza')

# use of \t

print('The tallest building in the world is \t Burj Khalifa')
