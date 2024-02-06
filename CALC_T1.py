# Import the os module for file handling
import os

# Create a Function to perform calculation
def calculate(num_1, num_2, operator):
    result = None
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    elif operator == '/':
        result = num_1 / num_2
    return result

# Function to write equation and result to a file
def write_equation_to_file(num_1, num_2, operator, result):
    with open('equations.txt', 'a') as f:
        f.write(f"{num_1} {operator} {num_2} = {result}\n")

# Create a Function to read equations and results from a .text file (Check if the file exists first)
def read_from_file(file_name):
    if not os.path.exists(file_name): 
        return None
    with open(file_name, 'r') as f:
        equations = f.readlines()
    return equations

# Create Main function to run calculator. Give user an option to enter two numbers and an operator or read equations from a file.
def run_calculator():
    while True:
        try:
            choice = input("Enter 1 to make a calculation or 2 to read equations from a file: ")
            if choice == '1': 
                num_1 = float(input("Enter the first number: "))
                num_2 = float(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, /): ")
                result = calculate(num_1, num_2, operator)
                if result is not None:
                    print(f"{num_1} {operator} {num_2} = {result}")
                    write_equation_to_file(num_1, num_2, operator, result)
            elif choice == '2': 
                file_name = input("Enter the name of the text file: ")
                equations = read_from_file(file_name)
                if equations is None:
                    print("The file does not exist.")
                    continue
                for equation in equations:
                    num_1, operator, num_2, equals, result = equation.split()
                    result = float(result)
                    print(f"{num_1} {operator} {num_2} = {result}")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception:
            print("An error occurred. Please try again.")

if __name__ == '__main__':
    run_calculator()




