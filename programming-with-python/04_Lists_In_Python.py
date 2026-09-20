# In Python, a list is an ordered collection of items that can hold elements of different data types. 
# Lists are mutable, meaning you can modify, add, or remove elements after creation. 
# Lists are defined using square brackets `[]`.
# Lists are versatile data structures in Python and are widely used in various applications. 
# Their ability to store multiple elements of different data types and their mutability make them powerful tools for organizing and manipulating data.
# Here are some key characteristics and operations related to lists in Python:

#1. List Creation:You can create a list by enclosing elements in square brackets:
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", True, 3.14]
empty_list = []

print(type(my_list))
print(mixed_list)
print(empty_list)

# 2. Accessing Elements: Elements in a list are accessed using indexing, where indexing starts from 0:
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]    # 10
second_element = my_list[1]   # 20

print(type(my_list))
print("First Element in List",first_element)
print("First Element in List",second_element)

# 3. List Slicing: You can extract a portion of a list using slicing:
my_list = [10, 20, 30, 40, 50]
slice1 = my_list[1:4]   # [20, 30, 40]
slice2 = my_list[:3]    # [10, 20, 30]
slice3 = my_list[2:]    # [30, 40, 50]

print("List Elements From 1 to 4 indexes are ",slice1)
print("List Elements Till 3 indexes are ",slice2)
print("List Elements From 2 indexes are ",slice3)


# 4. List Concatenation: You can concatenate two lists using the `+` operator:
list1 = [1, 2, 3]
list2 = [4, 5, 6,7]
concatenated_list = list1 + list2   # [1, 2, 3, 4, 5, 6]

print("The Concatenated Tuple",concatenated_list)


# 5. Modifying Elements: Lists are mutable, so you can change the values of individual elements:
my_list = [1, 2, 3]

#Before Modification
print(my_list)

my_list[1] = 10   # [1, 10, 3]

#After Modification
print(my_list)


# 6. List Length: You can find the number of elements in a list using the `len()` function:
my_list = [10, 20, 30, 40, 50]
length = len(my_list)   # 5

print("Length of List",length)

#7. List Methods:Python provides various built-in list methods for common operations like appending, extending, removing elements, and more.
my_list = [1, 2, 3]
my_list.append(4)
print("Appended List",my_list)        # [1, 2, 3, 4]

my_list.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
print("Extended List",my_list)


my_list.remove(2)        # [1, 3, 4, 5, 6]
print("Removed Element from List",my_list)


#8. List Comprehension: List comprehension is a concise way to create lists based on existing lists or other iterables.
squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]
print("Squares from 1 to 6 ",squares)
