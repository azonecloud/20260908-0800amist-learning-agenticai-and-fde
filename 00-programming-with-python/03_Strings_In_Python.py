#1. String Creation:You can create a string using single, double, or triple quotes:

single_quoted = 'This is a single-quoted string.'
double_quoted = "This is a double-quoted string."
triple_quoted = '''This is a triple-quoted string.'''

print("Single Quotes Text",single_quoted)
print("Double Quotes Text",double_quoted)
print("Triple Quotes Text",triple_quoted)

# 2. Escaping Characters:To include special characters within a string, you can use escape sequences, indicated by a backslash (\):
escaped_string = "This is a string with a newline character: \\n"

# 3. Accessing Characters: You can access individual characters in a string using indexing. In Python, indexing starts from 0:
my_string = "Hello, World!"
first_char = my_string[0]   # 'H'
second_char = my_string[1]  # 'e'

print(my_string)
print("First Character from my_string",first_char)
print("Second Character from my_string",second_char)

#4. Slicing Strings:You can extract a portion of a string using slicing:
my_string = "Hello, World!"
slice1 = my_string[0:5]    # 'Hello'
slice2 = my_string[7:]     # 'World!'
print(slice1)
print(slice2)

#5. String Concatenation:You can concatenate strings using the `+` operator:
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2   # 'Hello, World'

print("Concatenated String",result)

# 6. String Length:You can find the length of a string using the `len()` function:
my_string = "Hello"
length = len(my_string)   # 5
print("The lenghth of the string",length)

# 7. String Methods:Python provides various string methods for common operations like uppercasing, lowercasing, splitting, replacing, etc.
my_string = "Hello, World!"
upper_case = my_string.upper() # 'HELLO, WORLD!'
print(upper_case)
lower_case = my_string.lower()   # 'hello, world!'
print(lower_case)

split_string = my_string.split(', ')  # ['Hello', 'World!']
print(split_string)


# 8. String Formatting:Python supports different ways of formatting strings, including old-style formatting with `%`, and new-style formatting with `.format()` or f-strings (formatted string literals):
name = "Alice"
age = 30
formatted_str = "My name is %s and I am %d years old." % (name, age)
# 'My name is Alice and I am 30 years old.'
print(formatted_str)

formatted_str = "My name is {} and I am {} years old.".format(name, age)
# 'My name is Alice and I am 30 years old.'
print(formatted_str)

# RECOMMENDED
formatted_str = f"My name is {name} and I am {age} years old."
# 'My name is Alice and I am 30 years old.'
print(formatted_str)
