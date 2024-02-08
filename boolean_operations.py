# A boolean is a data type that is either True or False.
# They are commonly used in computer programs to make decisions.
# Commonly used in conditional statements, and loops.
# Also used in functions and methods that return a boolean value.
# Also used in comparison operators.
# The is and is not operators are used to compare the identity of two objects.
# The is operator returns True if the two objects are the same object
# The is not operator returns True if the two objects are not the same object
# The in and not in operators are used to check if a value is present in a sequence.
# The in operator returns True if the value is present in the sequence
# The not in operator returns True if the value is not present in the sequence
# The comparison operators are used to compare two values.
# The == operator returns True if the two values are equal

# Examples of Boolean Operations

# Example 1: Using the and operator
x = 5
print(x > 3 and x < 10)    # Output: True

# Example 2: Using the or operator
x = 5
print(x > 3 or x < 4)    # Output: True

# Example 3: Using the not operator
x = 5
print(not(x > 3 and x < 10))    # Output: False

# Example 4: Using the in operator
str1 = 'Hello, World!'
print('lo' in str1)    # Output: True

# Example 5: Using the not in operator
str1 = 'Hello, World!'
print('lo' not in str1)    # Output: False

# Example 6: Using the is operator
x = 5
print(x is 5)    # Output: True

# Example 7: Using the is not operator
x = 5
print(x is not 5)    # Output: False

# Example 8: Using the comparison operators
x = 5
print(x == 5)    # Output: True
print(x != 5)    # Output: False
print(x > 5)    # Output: False
print(x < 5)    # Output: False
print(x >= 5)    # Output: True

# Example 9: Using the comparison operators
x = 5
y = 10
print(x == 5 and y == 10)    # Output: True
print(x == 5 or y == 5)    # Output: True
print(not(x == 5 and y == 10))    # Output: False
print(x is 5)    # Output: True
print(x is not 5)    # Output: False
print(x == 5)    # Output: True
print(x != 5)    # Output: False
print(x > 5)    # Output: False

# Example 10: Using the comparison operators in a conditional statement
x = 5
if x == 5:
    print('x is 5')    # Output: x is 5
else:
    print('x is not 5')

