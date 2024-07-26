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

print("""select operation
        1.Add
        2.sub
        3.multi
        4.div""")

while True:

    #take input from the user 
    choice = input ("Enter choice (1/2/3/4):")

    # check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1 = float (input("Enter first number:"))
            num2 = float (input("Enter second number:"))
        except ValueError:
            print("invalid input. Please enter a number.")

            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2)) 

        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '4':
            
            print(num1, "/", num2, "=",div(num1, num2) )

            break

        else:
            print("invalid input")


