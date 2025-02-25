# 1 Debugging
# As you work through this problem set, whenever you encounter an error, please
# include a comment explaining what the error was and how you later resolved it.
# You can add these explanations at any relevant place in the file. Example:
# >>> print("Hello, World!")
# >>> """
# >>> I encountered the following eror: "SyntaxError: unterminated
# >>> string literal (detected at line 1) when I wrote
# >>> print("Hello, World!)". So I added the missing " at the end
# >>> and the code printed it successfully.
# >>> """

# 2 Practicing Sliding & Striding
# In this problem, you will practice slicing and striding lists!
# 2.1 Making a List Variable
# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually.

ListFirstTwentyNumbers = list(range(21))
print(ListFirstTwentyNumbers)


# 2.2 Working with List Elements
# Write a function that will take in your list from Part 2.1 and square each element
# in the list. Assign the result to a new variable.

ListFirstTwentyNumbers = list(range(21))
def squareList(ListFirstTwentyNumbers):
    return [x**2 for x in ListFirstTwentyNumbers]
SquaredList = squareList(list(range(21)))
print(SquaredList)

# 2.3 Slicing
# Write a function that takes in your new list from Part 2.2 and returns the first
# 15 elements of the list using slicing.


SquaredList = squareList(list(range(21)))
def first_fifteen_elements(SquaredList):
    return SquaredList[:15]
First_Fifteen = first_fifteen_elements(SquaredList)
print(First_Fifteen)

# 2.4 Striding
# Write a function that takes in your list from Part 2.2 and returns every 5th
# element from the list using striding.

SquaredList = squareList(list(range(21)))
def every_fifth_element(SquaredList):
    return SquaredList[4:21:5]
Every_Fifth_Element = every_fifth_element(SquaredList)
print(Every_Fifth_Element)

#I first entered the code return SquaredList[0:21:5] inside the function definition which 
# returned the list [0, 25, 100, 225, 400], which was incorrect and then I realized I didn't
# want it to start from the first value of 0 so then I changed it to return SquaredList[4:21:5]
# which resulted in the list [16, 81, 196, 361], which is what we wanted.

# 2.5 Slicing & Striding
# Write a function that takes your list from Part 2.2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.

SquaredList = squareList(list(range(21)))
def fancy_function(SquaredList):
    last_3_sliced = SquaredList[:-3]
    return last_3_sliced[::-3]
Last_3_Sliced = fancy_function(SquaredList)
print(Last_3_Sliced)
# [400, 289, 196, 121, 64, 25, 4]

# 3 2D lists
# 3.1 Creating a 5x5 2D List
# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.


def create_2d_list():
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append((i*5)+(j+1))
        matrix.append(row)
    return matrix
matrix = create_2d_list()
print(matrix)

# 3.2 Replacing 2D List with Multiples of 3
# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”.

matrix = create_2d_list()
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix [i][j] % 3 == 0:
                matrix [i][j] = "?"
    return matrix
Modified_matrix =  modified_2d_list(matrix)
print(Modified_matrix)

# 3.3 Summing None-’ ?’ Elements
# Assign the result of your function from Part 3.2 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.

matrix = create_2d_list()
new_matrix = modified_2d_list(matrix)
def sum_non_question_elements(new_matrix):
    valid_elements = []
    for row in new_matrix:
        for element in row:
            if element != "?":
                valid_elements.append(element)
    return sum(valid_elements)
Sum = sum_non_question_elements(new_matrix)
print(Sum)