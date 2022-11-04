"""
Chapter 1, Exercise 3: Print date and time

Write a Python program to display the current date and time.
 
"""
# a program to display current date and time

import time  # importing time module
from datetime import date  # from the datetime library, importing date module
from datetime import datetime # from datetime library, importing datetime module

# printing date only
date = date.today()
print("Today's date is ", date)

print("\n")

# printing time only
t = time.localtime()
current_time = time.strftime("%H : %M : %S", t)  # date format has been defined between the brackets
print('The current time is ', current_time)

print("\n")
# printing both time and date together

date_time = datetime.now()
print("The date is", date_time)
