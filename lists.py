# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# List are commonly used in programming and are very versatile. They can be used to store different types of data such as integers, strings, characters, and objects.
# Lists are mutable, meaning their elements can be changed unlike string or tuple.
# Examples of common operations on lists:
# 1. Accessing elements in a list
# 2. Slicing a list
# 3. Changing elements in a list
# 4. Adding elements to a list
# 5. Removing elements from a list
# 6. Looping through a list
# 7. List comprehension
# 8. Joining lists
# 9. Checking if an element is in a list
# 10. Finding the length of a list
#
# Common uses of lists in real world applications:
# 1. To-do lists
# 2. Shopping lists
# 3. Lists of students in a class
# 4. Lists of employees in a company
# 5. Lists of customers in a store
# 6. Lists of products in a store
# 7. Lists of items in a warehouse
#
# When do we use a list datatype?
# 1. When you want to store multiple values in a single variable
# 2. When you want to store values in a specific order
# 3. When you want to store values that can be changed
# 4. When you want to store values that can be duplicated
# 5. When you want to store values that can be of different data types
# 6. When you want to store values that can be of the same data type
# 
# The Logtime complexity of list operations:
# 1. Accessing elements in a list: O(1)
# 2. Slicing a list: O(k)
# 3. Changing elements in a list: O(1)
# 4. Adding elements to a list: O(1)
# 5. Removing elements from a list: O(n)
# 6. Looping through a list: O(n)
# 7. List comprehension: O(n)
# 8. Joining lists: O(n)
# 9. Checking if an element is in a list: O(n)
# 10. Finding the length of a list: O(1)

# Common operations on lists

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)    # Output: ['apple', 'banana', 'cherry']

# Example 2: Accessing elements in a list
fruits = ["apple", "banana", "cherry"]
print(fruits[1])    # Output: banana

# Example 3: Slicing a list
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[1:3])    # Output: ['banana', 'cherry']

# Example 4: Changing elements in a list
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)    # Output: ['apple', 'blackcurrant', 'cherry']

# Example 5: Adding elements to a list
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)    # Output: ['apple', 'banana', 'cherry', 'date']

# Example 6: Removing elements from a list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)    # Output: ['apple', 'cherry']

# Example 7: Looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    # Output: apple, banana, cherry

# Example 8: List comprehension
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)    # Output: ['apple', 'banana']

# Example 9: Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)    # Output: ['a', 'b', 'c', 1, 2, 3]

# Example 10: Checking if an element is in a list
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")    # Output: Yes, 'apple' is in the fruits list

# Example 11: Finding the length of a list
fruits = ["apple", "banana", "cherry"]
print(len(fruits))    # Output: 3

# Example 12: Clearing a list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)    # Output: []

# Example 13: Copying a list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)    # Output: ['apple', 'banana', 'cherry']

# Example 14: Counting elements in a list
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)    # Output: 1

# Example 15: Extending a list
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]
fruits.extend(cars)
print(fruits)    # Output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Example 16: Finding the index of an element in a list
fruits = ["apple", "banana", "cherry"]
x = fruits.index("cherry")
print(x)    # Output: 2

# Example 17: Inserting an element into a list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "date")
print(fruits)    # Output: ['apple', 'date', 'banana', 'cherry']

# Example 18: Popping an element from a list
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)    # Output: ['apple', 'banana']

# Example 19: Reversing a list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)    # Output: ['cherry', 'banana', 'apple']

# Example 20: Sorting a list
fruits = ["apple", "banana", "cherry"]
fruits.sort()
print(fruits)    # Output: ['apple', 'banana', 'cherry']

# Example 21: Sorting a list in descending order
fruits = ["apple", "banana", "cherry"]
fruits.sort(reverse=True)
print(fruits)    # Output: ['cherry', 'banana', 'apple']

# Example 22: Creating a list using the list constructor
fruits = list(("apple", "banana", "cherry"))    # note the double round-brackets
print(fruits)    # Output: ['apple', 'banana', 'cherry']

# Example 23: Creating a list using the list constructor
fruits = list("apple")
print(fruits)    # Output: ['a', 'p', 'p', 'l', 'e']

# Example 24: Creating a list using the list constructor
fruits = list(range(5))
print(fruits)    # Output: [0, 1, 2, 3, 4]

# Example 25: Creating a list using the list constructor
fruits = list(range(2, 5))
print(fruits)    # Output: [2, 3, 4]

# Example 26: Slicing a list in place
fruits = ["apple", "banana", "cherry", "date"]
fruits[1:3] = ["blackcurrant", "blueberry"]

# Example 27: Slicing a list in place
fruits = ["apple", "banana", "cherry", "date"]
fruits[1:3] = ["blackcurrant"]
print(fruits)    # Output: ['apple', 'blackcurrant', 'date']

# Example 28: Printing all methods of a list
fruits = ["apple", "banana", "cherry"]
print(dir(fruits))

# Example 29:  Destructuring a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)    # Output: apple
print(y)    # Output: banana
print(z)    # Output: cherry

# Example 30:  Destructuring a list
fruits = ["apple", "banana", "cherry"]
x, y, *z = fruits
print(x)    # Output: apple
print(y)    # Output: banana
print(z)    # Output: ['cherry']

# Example 31:  Destructuring a list
fruits = ["apple", "banana", "cherry"]
*x, y, z = fruits
print(x)    # Output: ['apple']
print(y)    # Output: banana
print(z)    # Output: cherry

# Example 32:  Destructuring a list
fruits = ["apple", "banana", "cherry"]
x, *y, z = fruits
print(x)    # Output: apple
print(y)    # Output: ['banana']
print(z)    # Output: cherry


