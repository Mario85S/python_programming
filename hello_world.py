# Import re module to make sure user has entered only letters as his name.
import re

# Ask user for his name from input.  
user_name_regex = r"^[a-zA-Z\s]+$"

while True:
    user_name = input("Please enter your name:\n").strip().title()
    if re.match(user_name_regex, user_name):
        break
    else:
        print("Invalid input. Please enter your name using only letters and spaces.")
 
# Ask for user's age from input. Using try, except to make sure user input  is integer with no string or float entered. 
while True:
    try:
        user_age = int(input("Please enter your age:\n"))
        break
    except ValueError:
        print("Invalid input. Please enter your age as a whole number.")

# print user name, user age and "Hello World!"
print(f"{user_name} is {user_age}!\n" "Hello World!")

