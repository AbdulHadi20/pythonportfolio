"""
Chapter 7, Exercise 4: Large Shirts

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different 
message.
"""

# defining a function and parameters having default values


def make_shirt(msg='I love Python', size='Large'):
    print('The size of the shirt is ' + size +
          ' and the msg on the shirt is ' + msg + '.')


# calling the functions
make_shirt()
make_shirt('m')
make_shirt(size='L', msg='You are a winner!!')
