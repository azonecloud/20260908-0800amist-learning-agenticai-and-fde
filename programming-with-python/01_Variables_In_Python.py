''' 
In Python, variables are used to store data or values in memory. 
Unlike some other programming languages, Python is dynamically typed, 
which means you don't need to specify the data type of a variable explicitly. 
The data type is inferred from the value assigned to the variable. 

Here's an overview of variables in Python:

1. Variable Naming Rules:
   - Variable names can consist of letters (a-z, A-Z), digits (0-9), and underscores (_).
   - They must start with a letter or an underscore (not with a digit).
   - Variable names are case-sensitive, meaning `myVar` and `myvar` are different variables.
   - Reserved keywords (e.g., `if`, `else`, `while`, `for`, etc.) cannot be used as variable names.

2. Variable Assignment:
   - You can assign a value to a variable using the `=` operator.
   - The variable will be created and automatically assigned the data type of the value.

3. Data Types of Variables:
   - Variables in Python can hold various data types, such as:
     - Numeric types: `int`, `float`, `complex`
     - Text type: `str`
     - Sequence types: `list`, `tuple`, `range`
     - Set types: `set`, `frozenset`
     - Mapping type: `dict`
     - Boolean type: `bool`
     - None type: `NoneType`

4. Variable Reassignment:
   - Variables can be reassigned with new values, and the data type can change accordingly.
   - Python's dynamic typing allows you to change the data type of a variable by reassigning it with a different value.

5. Printing Variables:
   - You can print the value of a variable using the `print()` function.

'''


# Integer variable
age = 30
print(age)  # Output: 30

# Float variable
pi = 3.14
print(pi)   # Output: 3.14

# String variable
name = "John"
print(name) # Output: John

# List variable
fruits = ["apple", "banana", "orange"]
print(fruits) # Output: ['apple', 'banana', 'orange']

# Boolean variables
is_student = True
is_teacher = False
print(is_student, is_teacher)  # Output: True False

# Variable reassignment
x = 10
print(x)  # Output: 10

x = "Hello, Python!"
print(x)  # Output: Hello, Python!

x,y = 5, 10
print(x,y)  # Output: 5 10