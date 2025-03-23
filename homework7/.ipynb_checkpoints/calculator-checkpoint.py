import math_tools

First_input = input("Enter your first number")
Second_input = input("Enter your second number")
Operation = input("Enter what operation you want")

if Operation == "Add" or Operation == "add":
    print(math_tools.add(int(First_input), int(Second_input)))
elif Operation == "Subtract" or Operation == "subtract":
    print(math_tools.subtract(int(First_input), int(Second_input)))
elif Operation == "Multiply" or Operation == "multiply":
    print(math_tools.multiply(int(First_input), int(Second_input)))
elif Operation == "Divide" or Operation == "divide":
    print(math_tools.divide(int(First_input), int(Second_input)))