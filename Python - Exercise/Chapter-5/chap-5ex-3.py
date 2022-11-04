"""
Chapter 5, Exercise 3: 

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing 
your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure 
that your loop works, add five more Python terms to your glossary.When you run your program again, these new 
words and meanings should automatically be included in the output.
"""
# creating a gloassary
glossary = {'loop':
            'a loop is an operation in programming that repeats a certain statement until a certain condition is met',
            'concatenation':
            'it refers to the joining of multiple strings to make a single long string.',
            'bin()':
            'it is the function, used to find the binary value of a certain character.',
            'IDE':
            'IDE stands for integrated development environment. It is a space built for coders to run, save, debug, etc. their code in a single environment. ',
            'GitHub': 'It is a platform where we can store our code projects in a cloud based repositories, collaborate with other developers and control the versions.',
            'Python': 'It is a high-level programming language developed by  Guido van Rossum ',
            'Interpreter': 'It is a tool in an IDE that finds potential errors and points them out to be fixed.',
            'Functions': 'They are the building blocks of the code.',
            'library': 'A library is a collection of related modules. They are pre-written codes.'}

# using for loops to print all the definitions
for word, definition in glossary.items():
    print(f'{word.title()}: {definition.title()}.')
