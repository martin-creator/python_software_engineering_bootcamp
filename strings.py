
# String is a sequence of characters and can be accessed by index
# Strings are immutable
# Strings can be sliced
# Strings can be concatenated
# Strings can be repeated
# Strings can be formatted
# Strings can be compared
# Strings can be searched
# Strings can be replaced
# Strings can be split
# Strings can be joined
# Strings can be stripped
# Strings can be justified
# Strings can be centered
# Strings can be encoded
# Strings can be decoded
# Strings can be formatted

# Strings in programming are maninly used for:
# 1. Displaying information
# 2. Storing information
# 3. Manipulating information

# String can be created using single quotes, double quotes, triple quotes
# Single quotes and double quotes are used to create single line strings
# Triple quotes are used to create multi-line strings

# To display on commands on  string object
print(dir(str))

# Single quotes
str1 = 'Hello, World!'
print(str1)

# Double quotes
str2 = "Hello, World!"
print(str2)

# Triple quotes
str3 = '''Hello, 
World!'''
print(str3)


# Path: strings.py
# Compare this snippet from string.py:
# Example 1: Accessing characters in a string
 
str1 = 'Hello, World!'
print(str1[0])    # Output: H

# Example 2: Slicing a string
str1 = 'Hello, World!'
print(str1[7:12])    # Output: World

# Example 3: Concatenating strings
str1 = 'Hello, '
str2 = 'World!'
print(str1 + str2)    # Output: Hello, World!

# Example 4: Repeating strings
str1 = 'Hello, '
print(str1 * 3)    # Output: Hello, Hello, Hello,

# Example 5: Formatting strings
name = 'Alice'
age = 10
print('%s is %d years old.' % (name, age))    # Output: Alice is 10 years old.

# Example 6: Comparing strings
str1 = 'Hello, World!'
str2 = 'hello, world!'
print(str1 == str2)    # Output: False

# Example 7: Searching for a substring
str1 = 'Hello, World!'
print('lo' in str1)    # Output: True

# Example 8: Replacing a substring
str1 = 'Hello, World!'
print(str1.replace('Hello', 'Hi'))    # Output: Hi, World!

# Example 9: Splitting a string
str1 = 'Hello, World!'
print(str1.split(','))    # Output: ['Hello', ' World!']

# Example 10: Joining strings
str1 = ['Hello', 'World!']
print(','.join(str1))    # Output: Hello,World!

# Example 11: Stripping whitespaces
str1 = ' Hello, World! '
print(str1.strip())    # Output: Hello, World!

# Example 12: Justifying a string
str1 = 'Hello, World!'
print(str1.ljust(20, '*'))    # Output: Hello, World!*******

# Example 13: Centering a string
str1 = 'Hello, World!'
print(str1.center(20, '*'))    # Output: ***Hello, World!****

# Example 14: Encoding a string
str1 = 'Hello, World!'
print(str1.encode())    # Output: b'Hello, World!'

# Example 15: Decoding a string
str1 = b'Hello, World!'
print(str1.decode())    # Output: Hello, World!

# Example 16: Formatting a string
name = 'Alice'
age = 10
print('{} is {} years old.'.format(name, age))    # Output: Alice is 10 years old.

# Example 17: Creating a multi-line string
str1 = '''Hello,
World!'''
print(str1)    # Output: Hello,
              #          World!

# Example 18: Creating a multi-line string
str1 = 'Hello,\nWorld!'
print(str1)    # Output: Hello,
              #          World!

# Example 19: Finding the length of a string
str1 = 'Hello, World!'
print(len(str1))    # Output: 13

# Example 20: Finding the index of a substring
str1 = 'Hello, World!'
print(str1.index('World'))    # Output: 7

# Example 21: Counting the occurrences of a substring
str1 = 'Hello, World!'
print(str1.count('o'))    # Output: 2

# Example 22: Checking if a string is alphanumeric
str1 = 'Hello, World!'
print(str1.isalnum())    # Output: False

# Example 23: Checking if a string is alphabetic
str1 = 'Hello, World!'
print(str1.isalpha())    # Output: False

# Example 24: Checking if a string is decimal
str1 = 'Hello, World!'
print(str1.isdecimal())    # Output: False

# Example 25: Checking if a string is digit
str1 = 'Hello, World!'
print(str1.isdigit())    # Output: False

# Example 26: Checking if a string is identifier
str1 = 'Hello, World!'
print(str1.isidentifier())    # Output: False

# Example 27: Checking if a string is lowercase
str1 = 'Hello, World!'
print(str1.islower())    # Output: False

# Example 28: Checking if a string is numeric
str1 = 'Hello, World!'
print(str1.isnumeric())    # Output: False

# Example 29: Checking if a string is printable
str1 = 'Hello, World!'
print(str1.isprintable())    # Output: True

# Example 30: Checking if a string is space
str1 = 'Hello, World!'
print(str1.isspace())    # Output: False

# Example 31: Checking if a string is title
str1 = 'Hello, World!'
print(str1.istitle())    # Output: True

# Example 32: Checking if a string is uppercase
str1 = 'Hello, World!'
print(str1.isupper())    # Output: False

# Example 33: Converting a string to lowercase
str1 = 'Hello, World!'
print(str1.lower())    # Output: hello, world!

# Example 34: Converting a string to uppercase
str1 = 'Hello, World!'
print(str1.upper())    # Output: HELLO, WORLD!

# Example 35: Capitalizing a string
str1 = 'hello, world!'
print(str1.capitalize())    # Output: Hello, world!

# Example 36: Swapping the cases of a string
str1 = 'Hello, World!'
print(str1.swapcase())    # Output: hELLO, wORLD!

# Example 37: Finding the maximum character
str1 = 'Hello, World!'
print(max(str1))    # Output: r

# Example 38: Finding the minimum character
str1 = 'Hello, World!'
print(min(str1))    # Output: ' '

# Example 39: Reversing a string
str1 = 'Hello, World!'
print(str1[::-1])    # Output: !dlroW ,olleH



