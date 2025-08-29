Item_Name = {'bread':30,
             'milk' :22,
             'lassi':35,
             'ice cream':50,
             'biscuits' :20,
             'munchies' :50,
             }
# function one for showing all item in stock
def Show_all():
    print("\nAvailable items:")
    for key, value in Item_Name.items():
        print(f"{key}: {value}")


# function second for ordering items
def order_now(product_name,quantity):

    if product_name in Item_Name:
        price = Item_Name[product_name]
        total_price = price * quantity
        print("\norder summary:")
        print("Item:", product_name)
        print("Quantity:", quantity)
        print("total price:", total_price)
        return total_price
    else:
        print("Sorry, product not found.")
        return 0

# function for payment
def payment_option(total_price):
    while True:
        amount = int(input('Enter the amount for payment:'))
        if amount == total_price:
         print("payment successfully completed")
         break
        else:
         print("payment failed! please try again.")

# function  to add new items in dict
def add_item():
    while True:
        product_name = input('Enter the product name:')
        price = int(input('Enter the product price:'))
        Item_Name[product_name] = price
        print("Item Name:", product_name)

        choice = input('Do you want to add more products? (yes/no)')
        if choice != 'yes':
            break

Show_all()

product = input('\nEnter the product name to order: ')
quantity = int(input('Enter the product quantity: '))
total_price = order_now(product, quantity)
if total_price > 0:
    payment_option(total_price)

# Optionally allow adding items
add_more = input("\nDo you want to add new items to stock? (yes/no): ")
if add_more == "yes":
    add_item()
    Show_all()