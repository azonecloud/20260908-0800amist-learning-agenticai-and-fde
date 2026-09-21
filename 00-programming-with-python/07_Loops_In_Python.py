# In Python, IF statements and WHILE loops are fundamental control flow structures. 
# They help in decision-making and repeating tasks based on conditions.
# IF statements execute code only when a condition is True.
# WHILE loops repeatedly execute code as long as a condition remains True.
# Proper indentation is very important in Python because it defines the block of code.
# Here's a brief overview of how IF statements and WHILE loops work in Python:

# =========================================================
# 1. IF Statement
# =========================================================
# The IF statement is used to check a condition.
# If the condition is True, the code inside the IF block executes.

age = 18

if age >= 18:
    print("You are eligible to vote.")

# =========================================================
# 2. IF-ELSE Statement
# =========================================================
# The ELSE block executes when the IF condition is False.

number = 5

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# =========================================================
# 3. IF-ELIF-ELSE Statement
# =========================================================
# ELIF stands for "else if".
# It allows checking multiple conditions.

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# =========================================================
# 4. Nested IF Statement
# =========================================================
# You can place one IF statement inside another IF statement.

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")

# =========================================================
# 5. WHILE Loop
# =========================================================
# A WHILE loop repeatedly executes as long as the condition is True.

count = 1

while count <= 5:
    print("Count value:", count)
    count += 1

# =========================================================
# 6. Infinite WHILE Loop
# =========================================================
# If the condition always remains True, the loop becomes infinite.
# Be careful while using infinite loops.

# Example (commented to avoid infinite execution)

# while True:
#     print("This loop will run forever")

# =========================================================
# 7. Using BREAK in WHILE Loop
# =========================================================
# The BREAK statement stops the loop immediately.

num = 1

while num <= 10:
    print(num)

    if num == 5:
        print("Breaking the loop")
        break

    num += 1

# =========================================================
# 8. Using CONTINUE in WHILE Loop
# =========================================================
# The CONTINUE statement skips the current iteration.

value = 0

while value < 5:
    value += 1

    if value == 3:
        continue

    print(value)

# =========================================================
# 9. WHILE Loop with ELSE
# =========================================================
# The ELSE block executes when the loop finishes normally.

x = 1

while x <= 3:
    print("Value:", x)
    x += 1
else:
    print("Loop completed successfully")

# =========================================================
# 10. Practical Example
# =========================================================
# Example: Finding the sum of numbers from 1 to 5

total = 0
n = 1

while n <= 5:
    total += n
    n += 1

print("Sum of numbers from 1 to 5 is:", total)

# =========================================================
# 11. Combining IF and WHILE
# =========================================================
# IF conditions are commonly used inside WHILE loops.

number = 1

while number <= 10:

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

    number += 1

# =========================================================
# Important Notes:
# =========================================================
# - IF statements are used for decision-making.
# - WHILE loops are used for repeated execution.
# - Indentation is mandatory in Python.
# - Use BREAK to stop a loop early.
# - Use CONTINUE to skip an iteration.
# - Be careful with infinite loops.
# - Conditions in IF and WHILE statements evaluate to either True or False.

