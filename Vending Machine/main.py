# Vending Machine (Utility App)

# a list of snacks and drinks
item_1 = {'Item Code': 0, 'Item Price': 1.50,
          'stock': 5, 'Item Name': 'Lays (salted)'}
item_2 = {'Item Code': 1, 'Item Price': 2.50,
          'stock': 5, 'Item Name': 'Doritos (BBQ)'}
item_3 = {'Item Code': 2, 'Item Price': 3.50,
          'stock': 5, 'Item Name': 'Cheetos (flaminhot)'}
item_4 = {'Item Code': 3, 'Item Price': 1.50,
          'stock': 5, 'Item Name': 'Chips-Oman'}
item_5 = {'Item Code': 4, 'Item Price': 2.00,
          'stock': 5, 'Item Name': 'Croissant'}
item_6 = {'Item Code': 5, 'Item Price': 3.00,
          'stock': 5, 'Item Name': 'Cupcakes'}
item_7 = {'Item Code': 6, 'Item Price': 2.00,
          'stock': 5, 'Item Name': 'kitkat'}
item_8 = {'Item Code': 7, 'Item Price': 2.50,
          'stock': 5, 'Item Name': 'Snickers'}
item_9 = {'Item Code': 8, 'Item Price': 2.50,
          'stock': 5, 'Item Name': 'Mars'}
item_10 = {'Item Code': 9, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Bounty'}
item_11 = {'Item Code': 10, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Galaxy'}
item_12 = {'Item Code': 11, 'Item Price': 2.00,
           'stock': 5, 'Item Name': 'MilkyWay'}
item_13 = {'Item Code': 12, 'Item Price': 1.50,
           'stock': 5, 'Item Name': 'Mango Juice'}
item_14 = {'Item Code': 13, 'Item Price': 1.50,
           'stock': 5, 'Item Name': 'Apple Juice'}
item_15 = {'Item Code': 14, 'Item Price': 1.50,
           'stock': 5, 'Item Name': 'Orange Juice'}
item_16 = {'Item Code': 15, 'Item Price': 2.00,
           'stock': 5, 'Item Name': 'Mix-Fruit Juice'}
item_17 = {'Item Code': 16, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Vanilla Milkshake'}
item_18 = {'Item Code': 17, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Chocolate Milkshake'}
item_19 = {'Item Code': 18, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Strawberry Milkshake'}
item_20 = {'Item Code': 19, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Mango Milkshake'}
item_21 = {'Item Code': 20, 'Item Price': 2.50,
           'stock': 5, 'Item Name': 'Banana Milkshake'}
item_22 = {'Item Code': 21, 'Item Price': 4.00,
           'stock': 5, 'Item Name': 'Pepsi'}
item_23 = {'Item Code': 22, 'Item Price': 4.00,
           'stock': 5, 'Item Name': 'Mountain Dew'}
item_24 = {'Item Code': 23, 'Item Price': 4.00,
           'stock': 5, 'Item Name': '7 UP'}
item_25 = {'Item Code': 24, 'Item Price': 4.00,
           'stock': 5, 'Item Name': 'Fanta'}
item_26 = {'Item Code': 25, 'Item Price': 1.50,
           'stock': 5, 'Item Name': 'Tea (karak)'}
item_27 = {'Item Code': 26, 'Item Price': 1.00,
           'stock': 5, 'Item Name': 'Water (small)'}
item_28 = {'Item Code': 27, 'Item Price': 2.00,
           'stock': 5, 'Item Name': 'Water(large)'}

items = [
    item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10,
    item_11, item_12, item_13, item_14, item_15, item_16, item_17, item_18, item_19,
    item_20, item_21, item_22, item_23, item_24, item_25, item_26, item_27, item_28
]

# global variables
cart = []
sum = 0
run = True
receipt = """Receipt"""

################################################################################################################

# function that greets and gives the initial command to the user


def greet_user():
    print('\n \t \t \t WELCOME TO THE VENDING MACHINE !!!')
    print('\n \t Please follow the instructions carefully to order your favorite snacks !!')

################################################################################################################

# categorizing of the types of snacks / drinks available
# function to display menu


def menu():
    # displaying snacks
    # used for loops to display the menu, categorized by specifying the items index positions
    print('\n \t \t ..........SNACKS.......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[0:6]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

    # displaying chocolates
    print('\n \t \t ..........CHOCOLATES.......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[6:12]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

    # displaying juices
    print('\n \t \t .........JUICES.......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[12:16]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

    # displaying milkshakes
    print('\n \t \t ..........MILKSHAKES.......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[16:21]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

    # displaying colddrinks
    print('\n \t \t ..........COLD-DRINKS.......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[21:25]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

    # displaying other beverages
    print('\n \t \t ..........DRINKS (OTHER).......... ')
    print('\n ITEM CODE \t \t ITEM PRICE \t \t STOCK \t \t ITEM NAME')
    for i in items[25:28]:
        print(
            f"      {i['Item Code']} \t \t   $ {i['Item Price']} \t \t {i['stock']} \t \t {i['Item Name']}")

################################################################################################################

# function that is responsible for the main operation of the machine


def vending_items():
    global run
    while run:                             # while loops runs while the conditions are true
        user_items = int(
            input('\n Please enter the code of the product you wish to buy = '))

        if user_items <= len(items):
            # adds item to the cart list according to the code entered by the user
            cart.append(items[user_items])

            print('\n Items in your cart are: ')   # prints the cart
            print('\n Item Price \t \t \t Item Name')
            for i in cart[0:]:
                print(f"  $ {i['Item Price']} \t \t \t {i['Item Name']}")

            # asks the user if they need more items
            more_items = str(input(
                '\n Do you wish to add more items ? \n Press enter or any key if yes and q to proceed to checkout = '))

            if more_items == 'q':    # if user selects q, the following condition will execute
                run = False

                print('\n Items in your cart are: ')  # prints cart

                print('\n Item Price \t \t \t Item Name')
                for i in cart[0:]:
                    print(f"  $ {i['Item Price']} \t \t \t {i['Item Name']}")

        else:
            # if user enters code not in list of dictionaries, this executes
            print('\n Invalid Code. Please try again!!!')
            vending_items()

################################################################################################################

# function to manage stocks


def stocks():
    for item in items:                 # using for loop to check if items are in stock
        if item.get('stock') == 0:      # if stock of an item is 0, lets the user know
            items.remove(item)
            print('\n Sorry the item is out of stock!!')
            menu()                          # displays the menu again

            # calling this function so user can add desired items in cart
            vending_items()

        elif item['stock'] > 0:    # if item is in stock, this statement executes
            if vending_items():
                # reduces a stock if user buys the item
                item['stock'] = item['stock'] - 1

################################################################################################################

# function that suggest random items to buy


def randomization():
    import random             # calling the random module
    print('\n')

    # saving a randomized dictionary in a variable
    random_items = random.choice(items)

    print(random_items)                   # printing the suggested item

    # asks the use if they want to buy the suggested item
    buy_random = str(
        input('\n Do you want to buy the suggested item ? (y/n) = '))

    if buy_random == 'y':
        # asks the user to enter the code of the suggested item to add it to cart
        addtocart = int(
            input('\n Please Enter the item code of the suggested item to add to cart  = '))

        # if code is correct, adds to cart
        if addtocart == random_items['Item Code']:

            # adds to cart according to the code entered
            cart.append(items[addtocart])

        else:
            # if code is invalid, this statement is executed
            print('\n Invalid Code!')

        print('\n Items in your cart are: ')
        print('\n Item Price \t \t \t Item Name')    # displays cart
        for i in cart[0:]:
            print(f"  $ {i['Item Price']} \t \t \t {i['Item Name']}")

    elif buy_random == 'n':
        # if user says no to suggested, this is executed
        print('\n Alright, you will be proceeded to checkout')

    else:
        print('\n Invalid Entry')  # if wrong code, another suggestion is given
        randomization()
################################################################################################################

# function that creats a receipt


def create_receipt(cart, receipt):
    for i in cart:                                    # usin for loop to create a receipt using items in cart
        receipt += f""" \t \n  $ {i['Item Price']} \t \t \t {i['Item Name']}"""  '\n'

    receipt += f""" \t Total = {total(cart)}"""
    return receipt                                 # displays the receipt to the user

################################################################################################################

# function that performs calculations


def total(cart):    # adds the price of all the items in cart using for loop
    sum = 0

    for i in cart:
        sum += i['Item Price']

    return sum    # displays the total amount

################################################################################################################

# function that performs the calculations


def moneypayment():

    print('\n You have to pay ', total(cart))
    print('\n PLEASE NOTE THAT ALL NOTES AND COINS ARE ACCEPTED!!!')

    # asks the user to pay amount
    money_paid = float(input('\n Please insert the money to pay = '))

    # if user does not enter required amount, payment fails
    if money_paid < total(cart):
        print('\n Payment Failed !!! \n Please try again..')
        moneypayment()

    # if successful, prints total, paid, and balance
    elif money_paid >= total(cart):
        balance = money_paid - total(cart)
        print('\n Total = ', total(cart))
        print('\n Paid = ', money_paid)
        print('\n Balance = ', balance)

    else:
        # if other than amount is entered, error shows
        print('\n Invalid Entry')
        moneypayment()

################################################################################################################

# calling all the functions according to the structure of the program


"""START OF THE PROGRAM (OUTPUT)"""

# calling the function that greets the user
greet_user()

# calling the function that displays the menu
menu()

# calling the function that performs the items selection
vending_items()

# calling the function that manages stocks
stocks()

# calling the function that is responsible to suggest items
randomization()

# displaying the final cart
print('\n Items in your cart are: ')
print('\n Item Price \t \t \t Item Name')
for i in cart[0:]:
    print(f"  $ {i['Item Price']} \t \t \t {i['Item Name']}")

# asking the user if they need a receipt or not
# asks the user if they want a receipt or not
receipt_print = int(
    input('\n Press the following: \n 1. For recipt \n 2. For No recipt \n'))
if receipt_print == 1:
    print(create_receipt(cart, receipt))

elif receipt_print == 2:
    print('\n Total Price = ', total(cart))

else:
    print('\n INVALID ENTRY!!')

# calling the function that perfroms the calculations
moneypayment()

# appreciation messages
print('\n Your Items have been dispensed. \n Please grab the products from the tray!!!')
print('\n THANKYOU!!!! HAVE A NICE DAY!!!')

""""END OF THE PROGRAM"""
