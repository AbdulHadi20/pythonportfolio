"""
Chapter 3, Exercise 6: Shrinking guest list

You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the 
end of your program.    
"""
guest_list = ['Messi', 'Neymar', 'Ronaldo', 'Lewandowski']   # list of guests

print('Bad news guys, I only can invite two people for dinner....')  # msg 

print('Sorry my dear friend ' +
      guest_list[3] + ', You are not invited for dinner.')                  
guest_list.pop(3)                                                      # removing guest 
print(guest_list)

print('Sorry my dear friend ' +
      guest_list[1] + ', You are not invited for dinner.')
guest_list.pop(1)                                                      # removing second guest
print(guest_list)

print('Dear ' + guest_list[0] + ', you are still invited for dinner.')    # sending invitations to remaining guests
print('Dear ' + guest_list[1] + ', you are still invited for dinner.')

del guest_list[:]                                                     # deleting the complete list
print('Guest List: ', guest_list)                                     # printing the empty list
