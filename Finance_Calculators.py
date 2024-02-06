# Import math module
import math

# Define a function to validate users float input. 
def validate_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Define a function to validate users integer input. 
def validate_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ask user which calculation they would like to choose
print("Choose either 'INVESTMENT' or 'BOND' from the menu above to proceed:")
print("'INVESTMENT' - to calculate the amount of interest you will earn on your investment")
print("'BOND' - to calculate the amount you will have to pay on your home loan")

choice = input().lower()

if choice == "investment":
    deposit = validate_float_input("Enter deposit amount:\n")
    int_rate = validate_float_input("Enter interest rate:\n")
    years = validate_int_input("Enter number of years:\n")

    interest = input("Which type of interest you are interested: 'simple' or 'compound'?").lower()

    # Convert interest rate to decimal
    user_int_rate = int_rate / 100

    if interest == "simple":
        total_interest_amount = deposit * (1 + user_int_rate * years)
    elif interest == "compound":
        total_interest_amount = deposit * math.pow((1 + user_int_rate), years)
    else:
        print("Invalid input. Please enter either 'simple' or 'compound'.")
        exit()

    print("After {} years, your investment will be worth {:,.2f}£.".format(years, total_interest_amount))

elif choice == "bond":
    present_value = validate_float_input("Enter present house value:")
    interest_rate = validate_float_input("Enter interest rate:")
    total_months = validate_float_input("Enter the number of months you are planning to repay the bond:")

    # Calculate the total repayment for the bond
    monthly_rate = interest_rate / (12 * 100)
    repayment = (monthly_rate * present_value) / (1 - (1 + monthly_rate) ** (-total_months))

    print("Your monthly bond repayment will be {:,.2f}£.".format(repayment))

else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")
