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

while True:

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

            break

        else:
            logging.info("invalid input")


