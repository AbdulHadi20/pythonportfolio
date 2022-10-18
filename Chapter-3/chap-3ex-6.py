# a program to shrink guest list

guest_list = ['Messi', 'Neymar', 'Ronaldo', 'Lewandowski']

print('Bad news guys, I only can invite two people for dinner....')

print('Sorry my dear friend ' +
      guest_list[3] + ', You are not invited for dinner.')
guest_list.pop(3)
print(guest_list)

print('Sorry my dear friend ' +
      guest_list[1] + ', You are not invited for dinner.')
guest_list.pop(1)
print(guest_list)

print('Dear ' + guest_list[0] + ', you are still invited for dinner.')
print('Dear ' + guest_list[1] + ', you are still invited for dinner.')

del guest_list[:]
print('Guest List: ', guest_list)
