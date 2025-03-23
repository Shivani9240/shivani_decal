# This function adds two input numbers a and b
def add(a,b): 
    return a + b

# This function subtracts two input numbers, b from a
def subtract(a,b):
    return a - b

# This function multiplies two input numbers a and b
def multiply(a,b):
    return a*b
    
# This function divides two input numbers, a by b, as long as b is not zero
def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("cannot divide by zero")