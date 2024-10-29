#!/usr/bin/python3
"""
main.py

This script provides a command-line interface for the basic calculator.
Users can perform addition, subtraction, multiplication, and division.
"""

from operations import add, subtract, multiply, divide

def main():
    """Main function to run the calculator."""
    print("Welcome to the Basic Calculator!")
    print("Select an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")

    while True:
        # Take input from the user
        choice = input("Enter your choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if choice is valid
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                except ValueError as e:
                    print(e)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
