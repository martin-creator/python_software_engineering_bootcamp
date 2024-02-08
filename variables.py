# A variable is a container for a value, which can be of various types
# Variables are used to store data, and data can be of various types
# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it
# Variables do not need to be declared with any particular type and can even change type after they have been set
# String variables can be declared either by using single or double quotes

# Example

x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even change type after they have been set
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting
# Example
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# Get the type
# You can get the data type of a variable with the type() function
# Example
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes
# Example
x = "John"
# is the same as
x = 'John'
y = "Martin"
# is the same as 
y = 'Martin'

# Case-Sensitive
# Variable names are case-sensitive
# Example
a = 4
A = "Sally"
# A will not overwrite a

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume)
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Example
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read
# There are several techniques you can use to make them more readable:
# Camel Case
# Each word, except the first, starts with a capital letter
# Example: myVariableName
# Pascal Case
# Each word starts with a capital letter
# Example: MyVariableName
# Snake Case
# Each word is separated by an underscore
# Example: my_variable_name

# Example
# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line
# Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line
# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking
# Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print statement is often used to output variables
# To combine both text and a variable, Python uses the + character
# Example
x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable    
# Example
x = "Python is "
y = "awesome"
z = x + y
print(z)

# For numbers, the + character works as a mathematical operator
# Example
x = 5
y = 10
print(x + y)

# If you try to combine a string and a number, Python will give you an error
# Example
# x = 5
# y = "John"
# print(x + y)

# Global Variables

