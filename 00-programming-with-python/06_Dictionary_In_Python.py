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


# Empty dictionary
empty_dict = {}

# Dictionary with some key-value pairs
person = {
'name': 'John Doe',
'age': 30,
'occupation': 'Software Engineer'
}

print("Name of the person",person["name"])

# 2. **Accessing Values:** You can access the value associated with a specific key using square brackets `[]`.

# Accessing values using keys
vname,vage,voccupation = person['name'], person['age'], person['occupation']

print(vname)  # Output: John Doe
print(vage)   # Output: 30
print(voccupation)  # Output: Software Engineer


# 3. **Modifying and Adding Elements:**Dictionaries are mutable, so you can modify the values associated with existing keys or add new key-value pairs.
# Modifying a value
person['age'] = 31

# Adding a new key-value pair
person['city'] = 'New York'

print("Updated person dictionary:", person)  # Output: {'name': 'John Doe', 'age': 31, 'occupation': 'Software Engineer', 'city': 'New York'}
# 4. **Checking Key Existence:** You can check if a key exists in a dictionary using the `in` keyword.

if 'name' in person:
 print("Name exists in the dictionary.")


# 5. **Dictionary Methods:** Dictionaries in Python come with various useful methods. Some of the commonly used methods include:
 # - `keys()`: Returns a list of all the keys in the dictionary.
 # - `values()`: Returns a list of all the values in the dictionary.
 # - `items()`: Returns a list of tuples containing key-value pairs.
 # - `get(key, default)`: Returns the value for a given key if it exists; otherwise, it returns the default value.
 # - `pop(key)`: Removes and returns the value associated with the specified key.
 # - `clear()`: Removes all key-value pairs from the dictionary.


# Example usage of dictionary methods
keys_list = list(person.keys())
values_list = list(person.values())
items_list = list(person.items())

print(keys_list)
print(values_list)
print(items_list)


# 6. **Iterating Through a Dictionary:** You can iterate through the keys or values or both using loops.

# Iterating through keys
for key in person:
   print(key, person[key])

# Iterating through values
for value in person.values():
   print(value)

# Iterating through both keys and values
for key, value in person.items():
   print(key, value)


