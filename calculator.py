<<<<<<< HEAD
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
=======
import logging
logging.basicConfig(level=logging.INFO)

   # this function adds two number 
def add(x,y):
    return x + y

   # this function sub two number
def sub(x,y):
    return x - y

   # this function multi two number
def multi(x,y):
    return x * y

   # this function div two number
def div(x,y):
    result=x/y
    return result

logging.info("""welcome to calculator\nselect operation:
        1.Add
        2.Sub
        3.Multi
        4.Div""")
>>>>>>> 575f4d0cbaa21990b5ff2623f8a3887d5f19c29a

while True:
    choice = input("Enter your choice (1-6): ")

<<<<<<< HEAD
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
=======
    #take input from the user 
    choice = input ("Enter choice :")

    # check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1 = float (input("Enter first number:"))
            num2 = float (input("Enter second number:"))
        except ValueError:
            logging.error("invalid input. Please enter a number.")
            continue

        if choice == '1':
            logging.info(add(num1, num2))

        elif choice == '2':
            logging.info(sub(num1, num2)) 

        elif choice == '3':
            logging.info(multi(num1, num2))

        elif choice == '4':
            logging.info(div(num1, num2) )
>>>>>>> 575f4d0cbaa21990b5ff2623f8a3887d5f19c29a

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
<<<<<<< HEAD
            logging.warning("Invalid input. Please enter a valid percentage.") 
=======
            logging.info("invalid input")
>>>>>>> 575f4d0cbaa21990b5ff2623f8a3887d5f19c29a

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
