"""
Chapter 7, Exercise 2: Favorite Book

Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title 
as an argument in the function call.
"""


def favorite_book(book):     # defining a function that has one parameter
    # msg to be printed
    print(f'One of my favorite books is {book.title()}.')


# calling the function and the data written in brackets gets stored in parameter (book)
favorite_book('Atomic Habits ')
