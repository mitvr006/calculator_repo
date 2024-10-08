import math
import logging
logging.basicConfig(level=logging.INFO)

current_value = 0
num1 =0
num2 =0

logging.info("""\nWelcome to current_value in calculator
    Choose an operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Clear
    6. percentage (%)
    7. square (x²)                          
    8. Exit""")

while True:
    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            current_value = num1 + num2
            logging.info(current_value)

        elif choice == '2':
            current_value = num1 - num2
            logging.info(current_value)

        elif choice == '3':
            current_value = num1 * num2
            logging.info(current_value)

        elif choice == '4':
            if num2 != 0:
                current_value = num1 / num2
                logging.info(current_value)
            else:
                logging.error("Error: Division by zero.")

    elif choice == '5': #clear all data
        current_value = 0
        entry =""
        logging.info("Calculator cleared.")

    elif choice == '6':  
        entry = input("Enter the percentage (e.g., 50 for 50%): ")
        if entry.replace('.', '', 1).isdigit(): 
            percentage = float(entry)
            number = float(input("Enter the number to calculate the percentage of: "))
            result = (percentage / 100) * number
            logging.info(f"{percentage}% of {number} ={result}")
        else:
            logging.warning("Invalid input. Please enter a valid percentage.") 

    elif choice == '7':  # Calculate Square
        entry = input("Enter a number to square: ")
        if entry.lstrip('-').replace('.', '', 1).isdigit():  
            number = float(entry)
            result = number ** 2  
            logging.info(f"{number}² = {result}")
        else:
            logging.warning("Invalid input. Please enter a valid number.")                  

    elif choice == '8':
        logging.info("Exiting...")
        break

    else:
        logging.info("Invalid choice, please try again.")
