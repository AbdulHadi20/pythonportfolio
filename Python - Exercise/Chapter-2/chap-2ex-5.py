# a program to find how many  $6 USB sticks can be bought for a specific amount

print('Enter the amount available = ')
amount = float(input())

amount_of_USB = 6
print('A single USB stick costs ' + str(amount_of_USB) + ' dollars.')

USBs_bought = amount // amount_of_USB
balance = amount % amount_of_USB

print('You have ' + str(amount) + ' dollars and you can buy ' +
      str(USBs_bought) + ' sticks')
print('Balance = ' + str(balance))
