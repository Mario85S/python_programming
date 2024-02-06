def while_average_num():
    # Initialize variables to store the sum and count of numbers
    total_num = 0
    count_result = 0

    # Continuously prompt the user for a number until they enter -1
    while True:
        # Try to convert the user input to an integer
        try:
            user_num = int(input("Please enter a number:\n"))
        except ValueError:
            # If the input is not an integer, display an error message and continue
            print("Invalid input. Please enter an integer.\n")
            continue

        # Check if the entered number is -1, indicating the end of input
        if user_num == -1:
            break

        # Add the valid integer to the total sum and increment the count
        total_num += user_num
        count_result += 1

    # Calculate the average if at least one valid number was entered
    if count_result > 0:
        average_count = total_num / count_result
        print("The average of the entered numbers is:", average_count)

while_average_num
