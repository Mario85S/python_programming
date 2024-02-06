#Validates the provided full name. The name must not be empty, have at least 4 characters, not exceed 25 characters, and consist of both a name and a surname.
def validate_full_name(full_name):

    
# Check for an empty input
    if not full_name:
        
        print("You haven't entered anything. Please enter your full name.")
        return False
 # Check for an input with less than 4 characters
    if len(full_name) < 4:
       
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
        return False

# Check for an input with more than 25 characters
    if len(full_name) > 25:
        
        print("You have entered more than 25 characters. Please make sure than you have only entered your full name.")
        return False
# Check for an input without both a name and a surname
    if len(full_name.split()) < 2:
        
        print("Please make sure you have entered your name and surname.")
        return False

    return True

while True:
    # Prompt the user to enter their full name
    user_full_name = input("Hello! Enter your full name, please\n")

    # Validate the provided full name
    if validate_full_name(user_full_name):
        
        # Valid name received
        print("Thank you for entering your name.")
        break
