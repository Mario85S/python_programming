# Create function to validate users input. Only numbers aloud.
def validate_time_input(prompt):
    while True:
        try:
            time_input = int(input(prompt))
            if time_input >= 0:
                return time_input
            else:
                print("Invalid input. Please enter a number for time in minutes.")
        except ValueError:
            print("Invalid input. Please enter a number for time in minutes.")

# Get user input for swimming time
swimming_time = validate_time_input("Please enter swimming time in minutes:\n")

# Get user input for cycling time
cycling_time = validate_time_input("Please enter cycling time in minutes:\n")

# Get user input for running time
running_time = validate_time_input("Please enter running time in minutes:\n")

# Calculate total triathlon time
total_triathlon_time = swimming_time + cycling_time + running_time

# Display total triathlon time
print("Total triathlon time:", total_triathlon_time)

# Display appropriate award message based on total triathlon time
if total_triathlon_time <= 100:
    print("Within qualifying time. Provincial colors.")
elif total_triathlon_time <= 105:
    print("Within 5 minutes of qualifying time. Provincial half colors.")
elif total_triathlon_time <= 110:
    print("Within 10 minutes of qualifying time. Provincial scroll.")
else:
    print("More than 10 minutes of qualifying time. No award.")
