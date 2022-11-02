"""
Chapter 3, Exercise 5: Change guest list

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in your list.
"""

guest_list = ['Joe', 'Kristian', 'Ryan', 'Rafael']        # list of guests

print('Just heard that ' + guest_list[2] + " wouldn't be able to make it....")   # msg that a guest won't make it 

guest_list[2] = 'Patrick'  # replacing a guest
print(guest_list)

print('Hi again ' + guest_list[0] +                                              # sending msgs to all the guests in the modified list
      ', You are invited for dinner at my house. ')
print('Hi again ' + guest_list[1] +
      ', You are invited for dinner at my house. ')
print('Hi  ' + guest_list[2] + ', You are invited for dinner at my house. ')
print('Hi again ' + guest_list[3] +
      ', You are invited for dinner at my house. ')
