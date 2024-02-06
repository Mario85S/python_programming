# Create cafe menu, stock and price dictionaries
menu = ['sandwich', 'snack', 'salad', 'tea', 'coffee', 'cake']

# menu stock dictionary
stock = {
    'sandwich': 25,
    'snack': 15,
    'salad': 20,
    'tea': 30,
    'coffee': 50,
    'cake': 25
}

# price for each menu item dictionary
price = {
    'sandwich': 4.5,
    'snack': 1.5,
    'salad': 2,
    'tea': 2.5,
    'coffee': 3,
    'cake': 2.5
}

# calculate total stock worth in the cafe
total_stock_worth = 0
for items in menu:
    item_value = stock[items] * price[items]
    total_stock_worth += item_value

# print total stock worth
print(f"Total stock worth: £{total_stock_worth:.2f}")
