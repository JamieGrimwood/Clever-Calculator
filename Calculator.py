# Import our modules
import time
from datetime import date
import os

today = date.today()

answer = 0
firstnum = 0
secondnum = 0
operation = ""
operationselect = ""

def clear_console():
    os.system('clear')

def logans():
    day = today.strftime("%d/%m/%Y")
    log = "(" + day + ") Worked out " + str(firstnum) + str(operation) + str(secondnum) + " which equalled " + str(answer) + "."
    with open('calculator.log', 'a') as f:
        f.writelines("\n" + log)
        # Log to the calculator.log file.
    input("\nPress ENTER to go back to the begining.")
    clear_console()
    start()

def calculate():
    global answer
    if operation == "+":
        # Work out the answer
        answer = firstnum+secondnum
        print("The answer is " + str(answer))
        print("\n\n")
        # Log the answer
        logans()
    elif operation == "-":
        # Work out the answer
        answer = firstnum-secondnum
        print("The answer is " + str(answer))
        print("\n\n")
        # Log the answer
        logans()
    elif operation == "*":
        # Work out the answer
        answer = firstnum*secondnum
        print("The answer is " + str(answer))
        print("\n\n")
        # Log the answer
        logans()
    elif operation == "/":
        # Work out the answer
        answer = firstnum/secondnum
        print("The answer is " + str(answer))
        print("\n\n")
        # Log the answer
        logans()
    else:
        print("big error " + firstnum + operation + secondnum)

def check_number(firstnumber):
    try:
        # Convert it into integer to check if it is a number
        val = int(firstnumber)
        return val
    except ValueError:
        try:
            # Convert it into float to check if it is a number
            val = float(firstnumber)
            return val
        except ValueError:
            return "false"

def enter_second_number():
    print("Please input the second number")
    secondnumber = input()
    # Check if it is a number
    isanum2 = check_number(secondnumber)
    if isanum2 == "false":
        print("That is not a number! Please enter an actual number.")
    else:
        # Make the second number accessable in the entire file
        global secondnum
        secondnum = isanum2
        calculate()

def enter_first_number():
    print("Please input the first number")
    firstnumber = input()
    # Check if it is a program
    isanum1 = check_number(firstnumber)
    if isanum1 == "false":
        print("That is not a number! Please enter an actual number.")
    else:
        # Make the first number accessable in the entire file
        global firstnum
        firstnum = isanum1
        enter_second_number()

def checkoperation(operationselect):
    if operationselect == "+":
        return
    if operationselect == "-":
        return
    if operationselect == "*":
        return
    if operationselect == "/":
        return
    else:
        print("That isn't one of the options.")
        start()

def start():
    print("Welcome to the clever calculator")
    time.sleep(3)
    print("Please select what operation you would like to do:\n\n")
    print("Add (+), Subtract (-), Times (*), Divide (/)")
    global operationselect
    operationselect = input()
    checkoperation(operationselect)
    # Make the operation accessable in the entire file
    global operation
    operation = operationselect
    enter_first_number()

# Start the program
start()
