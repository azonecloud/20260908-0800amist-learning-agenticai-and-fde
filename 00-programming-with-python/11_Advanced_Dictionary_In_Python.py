# In Python, a dictionary is a powerful and versatile data structure used to store key-value pairs. 
# It is also known as an associative array or hash map in other programming languages. 
# Dictionaries are mutable, unordered, and allow fast access to elements through their keys. 
# They are defined using curly braces `{}` and colons `:` to separate keys and values.
# Remember that dictionaries are unordered, so the order of elements during iteration may not be the same as the order of insertion.
# If you need an ordered dictionary, you can use `collections.OrderedDict` from the `collections` module.
# Here's a brief overview of how dictionaries work in Python:

# 1. **Creating a Dictionary:**
# To create a dictionary, enclose key-value pairs inside curly braces `{}`. 
# Each key-value pair is separated by a colon `:` and different pairs are separated by commas.


# Real-World Example of Python Dictionary
# Example: Student Information System

# Empty dictionary
student_database = {}

# Dictionary with student details
student1 = {
    'student_id': 101,
    'name': 'Rahul Kumar',
    'age': 20,
    'course': 'Computer Science',
    'college': 'ABC Engineering College'
}

student2 = {
    'student_id': 102,
    'name': 'Priya Sharma',
    'age': 21,
    'course': 'Electronics',
    'college': 'XYZ Engineering College'
}

# Accessing dictionary values
print("Course of student2:", student2["course"])

# Accessing values using keys
sname = student1['name']
sage = student1['age']
scourse = student1['course']

print(sname)
print(sage)
print(scourse)

# Modifying a value
student1['age'] = 22

# Adding a new key-value pair
student1['city'] = 'Hyderabad'

print("Updated student dictionary:", student1)

# Checking if key exists
if 'name' in student1:
    print("Student name exists in the dictionary.")

# Dictionary methods
keys_list = list(student1.keys())
values_list = list(student1.values())
items_list = list(student1.items())

print("\nKeys:", keys_list)
print("Values:", values_list)
print("Items:", items_list)

# Iterating through keys
print("\nIterating through keys:")
for key in student1:
    print(key, ":", student1[key])

# Iterating through values
print("\nIterating through values:")
for value in student1.values():
    print(value)

# Iterating through both keys and values
print("\nIterating through key-value pairs:")
for key, value in student1.items():
    print(key, "=", value)