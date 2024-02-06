# import re module to validate user inputs
import re

# Validate item name 
def validate_item(item_name):
    item_regex = r"^[a-zA-Z\s]+$"
    if re.match(item_regex, item_name):
        return True
    else:
        return False

# Get valid item input from user
def get_item_input(prompt):
    while True:
        item_name = input(prompt)
        if validate_item(item_name):
            return item_name
        else:
            print("Invalid input. Please enter your item name using only letters and spaces.")

# Create a greeting line to greet customers.
greeting_line = "Hello, May I have your order please?"
print(greeting_line)

# Ask customer to choose their favorite three items
Item1 = get_item_input("Enter your first item, please:\n")
Item2 = get_item_input("Enter your second item, please:\n")
Item3 = get_item_input("Enter your third item, please:\n")

# Print order confirmation
print("ORDER CONFIRMATION\nTHANK YOU!")
print(Item1)
print(Item2)
print(Item3)
