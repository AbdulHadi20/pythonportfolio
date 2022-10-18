# a program to display current date and time

import time  # importing time module
from datetime import date  # from the datetime library, importing date module
from datetime import datetime

date = date.today()
print("Today's date is ", date)

print("\n")

t = time.localtime()
current_time = time.strftime("%H : %M : %S", t)
print('The current time is ', current_time)

print("\n")
# printing both time and date together

date_time = datetime.now()
print("The date is", date_time)
