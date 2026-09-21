#In Python, a tuple is an ordered, immutable collection of elements. 
#Tuples are similar to lists, but unlike lists, their elements cannot be modified, added, or removed after creation. 
# Tuples are defined using parentheses `()` or the `tuple()` constructor.

# 1. Tuple Creation:You can create a tuple using parentheses or the `tuple()` constructor: 
my_tuple = (1, 2, 3)
another_tuple = tuple([4, 5, 6])

print(type(my_tuple))
print(my_tuple)

# 2. Accessing Elements:Elements in a tuple are accessed using indexing, similar to lists:
my_tuple = (10, 20, 30, 40, 50)
first_element = my_tuple[0]    # 10
second_element = my_tuple[1]   # 20

print("The First Element in the Tuple is",first_element)
print("The Second Element in the Tuple is",second_element)

# 3. Tuple Slicing: You can extract a portion of a tuple using slicing:
my_tuple = (10, 20, 30, 40, 50)
slice1 = my_tuple[1:4]   # (20, 30, 40)
slice2 = my_tuple[:3]    # (10, 20, 30)
slice3 = my_tuple[2:]    # (30, 40, 50)

print("Tuple Elements From 1 to 4 indexes are ",slice1)
print("Tuple Elements Till 3 indexes are ",slice2)
print("Tuple Elements From 2 indexes are ",slice3)


# 4. Tuple Concatenation:You can concatenate two tuples using the `+` operator:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2   # (1, 2, 3, 4, 5, 6)

print("The Concatenated Tuple",concatenated_tuple)

# 5. Tuple Length:You can find the number of elements in a tuple using the `len()` function:
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)   # 5

print("Length of Tuple is",length)

# 6. Unpacking Tuples: Tuples can be unpacked into individual variables:
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a,b,c)
# a = 10, b = 20, c = 30

# 7. Immutable Nature: As mentioned earlier, tuples are immutable. Once created, their elements cannot be changed:
my_tuple = (1, 2, 3)
my_tuple[0] = 100   # Raises TypeError: 'tuple' object does not support item assignment

