# None type is a data type of its own (NoneType) and only has one value: None.
# It is used to indicate that a variable does not have a value.
# None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
# It is used to indicate that a variable does not have a value.
# 
# Commonly used in the following scenarios:
# When a function does not return any value, it returns None.

# Examples of using the None type

# Example 1: Using the None type
x = None
print(x)    # Output: None

# Example 2: Using the None type in a conditional statement
x = None
if x:
    print('x is True')
else:
    print('x is False')    # Output: x is False

# Example 3: Using the None type in a conditional statement
x = None
if not x:
    print('x is False')    # Output: x is False
else:
    print('x is True')

# Example 4: Using the None type in a conditional statement
x = None
if x is None:
    print('x is None')    # Output: x is None

