menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

print("Menu:")
print("1-Pizza: $2.99")
print("2-Burger: $3.99")
print("3-Hot dog: $1.99")
print("4-Cheese: $0.59")
print("5-Ice cream: $1.49")
print("6-Churro: $0.79")
print("7-Soda: $0.89")

print("Please write two items from the menu.")

item1 = input("Item 1: ")
if item1 in menu:
    p_item1 = menu[item1]
else:
    print("Item 1 is not on the menu.")
    exit()

item2 = input("Item 2: ")
if item2 in menu:
    p_item2 = menu[item2]
else:
    print("Item 2 is not on the menu.")
    exit()

def total_price(p_item1, p_item2): 
    total = p_item1 + p_item2
    return total

print(f"The total price of {item1} and {item2} is $", total_price(p_item1, p_item2))

print("Price difference between two items:")
i1 = input("Enter one item from the menu: ")
if i1 not in menu:
        print("Item 1 is not on the menu.")
        exit()
i2 = input("Enter another item from the menu: ")
if i2 not in menu:
        print("Item 2 is not on the menu.")
        exit()
        
def price_difference(i1, i2):
    if i1 in menu and i2 in menu:
        diff = abs(menu[i1] - menu[i2])
        if diff < 0:
            diff = abs(menu[i2] - menu[i1])
        return diff
    else:
        return "One or both items are not on the menu."
    
print(f"The price difference between {i1} and {i2} is $", price_difference(i1, i2))

print("Inflation calculator")
item = input("Enter the item in the menu: ")
porc_infla = input("Enter the inflation rate (as a percentage): %")

def inflation (item, porc_infla) :
    if item in menu:
        price = menu[item]
        inflation_amount = price * (float(porc_infla) / 100)
        new_price = price + inflation_amount
        return new_price
    else:
        return "Item not found in the menu."

menu[item] = inflation(item, porc_infla)

print("Updated menu after inflation:")
print(menu)

print("Deflation calculator")
itemd = input("Enter the item in the menu: ")
porc_defla = input("Enter the inflation rate (as a percentage): %")

def deflation(itemd, porc_defla):
    if itemd in menu:
        price = menu[itemd]
        deflation_amount = price * (float(porc_defla) / 100)
        new_price = price - deflation_amount
        return new_price
    else:
        return "Item not found in the menu."

menu[item] = deflation(item, porc_infla)

print("Updated menu after deflation:")
print(menu)

# Discount funtion
print("Discount calculator, look the money you saved!")
item_discount = input("Enter the item in the menu: ")
discount_rate = input("Enter the discount rate (as a percentage): %")

def discount(item_discount, discount_rate):
    if item_discount in menu:
        price = menu[item_discount]
        discount_amount = price * (float(discount_rate) / 100)
       
        return discount_amount
    else:   
        return "Item not found in the menu."

print("The money you saved is $", discount(item_discount, discount_rate))