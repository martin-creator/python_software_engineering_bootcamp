# Tuples are immutable, meaning they cannot be changed. They are used to store multiple items in a single variable.
# Tuples items are ordered, unchangeable, and allow duplicate values.
# Tuples are written with round brackets.
# Tuples are commonly used in real world applications under the following scenarios:
# 1. To store multiple values in a single variable
# 2. To store values in a specific order
# 3. To store values that cannot be changed
# 4. To store values that can be duplicated
# 5. To store values that can be of different data types
# 6. To store values that can be of the same data type

# Examples of common operations on tuples:
# 1. Accessing elements in a tuple
# 2. Slicing a tuple
# 3. Joining tuples
# 4. Checking if an element is in a tuple

# Common tuple operations

# Example 1: Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)    # Output: ('apple', 'banana', 'cherry')

# Example 2: Accessing elements in a tuple
fruits = ("apple", "banana", "cherry")
print(fruits[1])    # Output: banana

# Example 3: Slicing a tuple
fruits = ("apple", "banana", "cherry", "date")
print(fruits[1:3])    # Output: ('banana', 'cherry')

# Example 4: Joining tuples
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "onion", "potato")
print(fruits + vegetables)    # Output: ('apple', 'banana', 'cherry', 'carrot', 'onion', 'potato')

# Example 5: Checking if an element is in a tuple
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)    # Output: True

# Example 6: Checking if an element is in a tuple
fruits = ("apple", "banana", "cherry")
print("date" not in fruits)    # Output: True

# Example 7: Finding the length of a tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))    # Output: 3

# Example 8: Finding the length of a tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))    # Output: 3

# Example 9: Finding the length of a tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))    # Output: 3

# Example 10: Finding  index of an element in a tuple
fruits = ("apple", "banana", "cherry")
print(fruits.index("banana"))    # Output: 1

# Example 11: Finding the count of an element in a tuple
fruits = ("apple", "banana", "cherry", "banana")
print(fruits.count("banana"))    # Output: 2

# Example 12: repeating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits * 2)    # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Example 13: Converting a list to a tuple
fruits = ["apple", "banana", "cherry"]
print(tuple(fruits))    # Output: ('apple', 'banana', 'cherry')

# Example 14: Converting a string to a tuple
fruits = "apple"
print(tuple(fruits))    # Output: ('a', 'p', 'p', 'l', 'e')

# Example 15: Converting a range to a tuple
fruits = range(3)
print(tuple(fruits))    # Output: (0, 1, 2)

# Example 16: Converting a dictionary to a tuple
fruits = {"apple", "banana", "cherry"}
print(tuple(fruits))    # Output: ('banana', 'cherry', 'apple')

# Example 17: Converting a set to a tuple
fruits = {"apple", "banana", "cherry"}
print(tuple(fruits))    # Output: ('banana', 'cherry', 'apple')

# Example 18: Converting a frozen set to a tuple
fruits = frozenset({"apple", "banana", "cherry"})
print(tuple(fruits))    # Output: ('banana', 'cherry', 'apple')
# A frozen set is a set that is immutable, meaning it cannot be changed. It is used to store multiple items in a single variable.

# Example 19: reversing a tuple
fruits = ("apple", "banana", "cherry")
print(fruits[::-1])    # Output: ('cherry', 'banana', 'apple')

# Example 20: Sorting a tuple
fruits = ("apple", "banana", "cherry")
print(sorted(fruits))    # Output: ['apple', 'banana', 'cherry']
# The sorted() function returns a sorted list of the specified iterable object.

# Example 21: Sorting a tuple
fruits = ("apple", "banana", "cherry")
print(sorted(fruits, reverse=True))    # Output: ['cherry', 'banana', 'apple']

#
