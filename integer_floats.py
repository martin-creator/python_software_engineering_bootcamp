# An integer is a number that can be written without a fractional component. For example, 21, 4, and 0 are integers, while 9.5, 5 1/2, and √2 are not. An integer float is a float that is also an integer. For example, 21.0, 4.0, and 0.0 are integer floats, while 9.5, 5.5, and 2.5 are not. Write a program that reads a float from the user. Your program should display a message indicating whether the entered number is an integer float or not.
# A float is a number that contains a decimal point. For example, 21.0, 4.0, and 0.0 are floats, while 21, 4, and 0 are not. An integer float is a float that is also an integer. For example, 21.0, 4.0, and 0.0 are integer floats, while 9.5, 5.5, and 2.5 are not. Write a program that reads a float from the user. Your program should display a message indicating whether the entered number is an integer float or not.

# Integers are commonly used for:
# 1. Counting
# 2. Storing information
# 3. Manipulating information
#
# Integers can be created using:
# 1. Decimal
# 2. Binary
# 3. Octal
# 4. Hexadecimal
#
# To display all commands on integer object
# print(dir(int))
#
# # Decimal
# num1 = 21
# print(num1)
#
# # Binary
# num2 = 0b10101
#
# Floats are commonly used for:
# 1. Storing information
# 2. Manipulating information
#
# Floats can be created using:
# 1. Decimal
# 2. Scientific notation
#
# To display all commands on float object
# print(dir(float))
#
# # Decimal
# num1 = 21.0
# print(num1)
#
# # Scientific notation
# num2 = 2.1e1
# print(num2)

# Type casting
#
# Is the process of converting one data type to another data type.
# Example 1: Converting an integer to a float
num1 = 21
print(float(num1))    # Output: 21.0

# Example 2: Converting a float to an integer
num2 = 4.0
print(int(num2))    # Output: 4

# Common operations on integers and floats

# 1. Addition
# Example 1: Adding two integers
num1 = 21
num2 = 4
print(num1 + num2)    # Output: 25

# Example 2: Adding an integer and a float
num1 = 21
num2 = 4.0
print(num1 + num2)    # Output: 25.0

# 2. Subtraction
# Example 1: Subtracting two integers
num1 = 21
num2 = 4
print(num1 - num2)    # Output: 17

# Example 2: Subtracting an integer from a float
num1 = 21
num2 = 4.0
print(num1 - num2)    # Output: 17.0

# 3. Multiplication
# Example 1: Multiplying two integers
num1 = 21
num2 = 4
print(num1 * num2)    # Output: 84

# Example 2: Multiplying an integer and a float
num1 = 21
num2 = 4.0
print(num1 * num2)    # Output: 84.0

# 4. Division
# Example 1: Dividing two integers
num1 = 21
num2 = 4
print(num1 / num2)    # Output: 5.25

# Example 2: Dividing an integer by a float
num1 = 21
num2 = 4.0
print(num1 / num2)    # Output: 5.25

# 5. Modulus
# Example 1: Finding the remainder of two integers
num1 = 21
num2 = 4
print(num1 % num2)    # Output: 1

# Example 2: Finding the remainder of an integer and a float
num1 = 21
num2 = 4.0
print(num1 % num2)    # Output: 1.0

# 6. Exponentiation
# Example 1: Raising an integer to the power of another integer
num1 = 2
num2 = 3
print(num1 ** num2)    # Output: 8

# Example 2: Raising an integer to the power of a float
num1 = 2
num2 = 3.0
print(num1 ** num2)    # Output: 8.0

# 7. Floor division
# Example 1: Performing floor division on two integers
num1 = 21
num2 = 4
print(num1 // num2)    # Output: 5

# Example 2: Performing floor division on an integer and a float
num1 = 21
num2 = 4.0
print(num1 // num2)    # Output: 5.0

# 8. Comparison
# Example 1: Comparing two integers
num1 = 21
num2 = 4
print(num1 == num2)    # Output: False

# Example 2: Comparing an integer and a float
num1 = 21
num2 = 4.0
print(num1 == num2)    # Output: False

# 9. Conversion
# Example 1: Converting an integer to a float
num1 = 21
print(float(num1))    # Output: 21.0

# Example 2: Converting a float to an integer
num2 = 4.0
print(int(num2))    # Output: 4

# 10. Absolute value
# Example 1: Finding the absolute value of an integer
num1 = -21
print(abs(num1))    # Output: 21

# Example 2: Finding the absolute value of a float
num2 = -4.0
print(abs(num2))    # Output: 4.0

# 11. Rounding
# Example 1: Rounding an integer
num1 = 21
print(round(num1))    # Output: 21

# Example 2: Rounding a float
num2 = 4.0
print(round(num2))    # Output: 4.0

# 12. Minimum
# Example 1: Finding the minimum of two integers
num1 = 21
num2 = 4
print(min(num1, num2))    # Output: 4

# Example 2: Finding the minimum of an integer and a float
num1 = 21
num2 = 4.0
print(min(num1, num2))    # Output: 4.0

# 13. Maximum
# Example 1: Finding the maximum of two integers
num1 = 21
num2 = 4
print(max(num1, num2))    # Output: 21

# Example 2: Finding the maximum of an integer and a float
num1 = 21
num2 = 4.0
print(max(num1, num2))    # Output: 21.0

# 14. Sum
# Example 1: Finding the sum of two integers
num1 = 21
num2 = 4
print(sum([num1, num2]))    # Output: 25

# Example 2: Finding the sum of an integer and a float
num1 = 21
num2 = 4.0
print(sum([num1, num2]))    # Output: 25.0

# 15. Conjugate
# Example 1: Finding the conjugate of an integer
num1 = 21
print(num1.conjugate())    # Output: 21

# Example 2: Finding the conjugate of a float   
num2 = 4.0
print(num2.conjugate())    # Output: 4.0

# 16. Real
# Example 1: Finding the real part of an integer
num1 = 21
print(num1.real)    # Output: 21

# Example 2: Finding the real part of a float
num2 = 4.0
print(num2.real)    # Output: 4.0

# 17. Imaginary
# Example 1: Finding the imaginary part of an integer
num1 = 21
print(num1.imag)    # Output: 0

# Example 2: Finding the imaginary part of a float
num2 = 4.0
print(num2.imag)    # Output: 0.0

# 18. Hexadecimal
# Example 1: Converting an integer to a hexadecimal string
num1 = 21
print(hex(num1))    # Output: 0x15

# Example 2: Converting a float to a hexadecimal string
num2 = 4.0
print(hex(int(num2)))    # Output: 0x4

# 19. Octal
# Example 1: Converting an integer to an octal string
num1 = 21
print(oct(num1))    # Output: 0o25

# Example 2: Converting a float to an octal string
num2 = 4.0
print(oct(int(num2)))    # Output: 0o4

# 20. Binary
# Example 1: Converting an integer to a binary string
num1 = 21
print(bin(num1))    # Output: 0b10101

# Example 2: Converting a float to a binary string
num2 = 4.0
print(bin(int(num2)))    # Output: 0b100

# 21. Bitwise AND
# Example 1: Performing bitwise AND on two integers
num1 = 21
num2 = 4
print(num1 & num2)    # Output: 4

# Example 2: Performing bitwise AND on an integer and a float
num1 = 21
num2 = 4.0
print(int(num1) & int(num2))    # Output: 4

# 22. Bitwise OR
# Example 1: Performing bitwise OR on two integers
num1 = 21
num2 = 4
print(num1 | num2)    # Output: 21

# Example 2: Performing bitwise OR on an integer and a float
num1 = 21
num2 = 4.0
print(int(num1) | int(num2))    # Output: 21

# 23. Bitwise XOR
# Example 1: Performing bitwise XOR on two integers
num1 = 21
num2 = 4
print(num1 ^ num2)    # Output: 17

# Example 2: Performing bitwise XOR on an integer and a float
num1 = 21
num2 = 4.0
print(int(num1) ^ int(num2))    # Output: 17

# 24. Bitwise NOT
# Example 1: Performing bitwise NOT on an integer
num1 = 21
print(~num1)    # Output: -22

# Example 2: Performing bitwise NOT on a float
num2 = 4.0
print(int(~num2))    # Output: -5

# 25. Left shift
# Example 1: Performing left shift on an integer
num1 = 21
print(num1 << 2)    # Output: 84

# Example 2: Performing left shift on a float
num2 = 4.0
print(int(num2) << 2)    # Output: 16

# 26. Right shift
# Example 1: Performing right shift on an integer
num1 = 21
print(num1 >> 2)    # Output: 5

# Example 2: Performing right shift on a float
num2 = 4.0
print(int(num2) >> 2)    # Output: 1

# 27. Identity
# Example 1: Checking if two integers are the same object
num1 = 21
num2 = 21
print(num1 is num2)    # Output: True

# Example 2: Checking if an integer and a float are the same object
num1 = 21
num2 = 21.0
print(num1 is num2)    # Output: False

# 28. Membership
# Example 1: Checking if an integer is in a list
num1 = 21
print(num1 in [21, 4])    # Output: True

# Example 2: Checking if an integer is not in a list
num1 = 21
print(num1 not in [21, 4])    # Output: False

# 29. Assignment
# Example 1: Assigning an integer to a variable
num1 = 21
print(num1)    # Output: 21

# Example 2: Assigning a float to a variable
num2 = 4.0
print(num2)    # Output: 4.0

# 30. Augmented assignment
# Example 1: Adding an integer to a variable
num1 = 21
num1 += 4
print(num1)    # Output: 25

# Example 2: Adding a float to a variable
num2 = 4.0
num2 += 21

# Example 3: Subtracting an integer from a variable
num1 = 21
num1 -= 4
print(num1)    # Output: 17

# Example 4: Subtracting a float from a variable
num2 = 4.0
num2 -= 21
print(num2)    # Output: -17.0

# Example 5: Multiplying a variable by an integer
num1 = 21
num1 *= 4
print(num1)    # Output: 84

# Example 6: Multiplying a variable by a float
num2 = 4.0
num2 *= 21
print(num2)    # Output: 84.0

# Example 7: Dividing a variable by an integer
num1 = 21
num1 /= 4
print(num1)    # Output: 5.25

# Example 8: Dividing a variable by a float
num2 = 4.0
num2 /= 21
print(num2)    # Output: 0.19047619047619047

# Example 9: Finding the remainder of a variable and an integer
num1 = 21
num1 %= 4
print(num1)    # Output: 1

# Example 10: Finding the remainder of a variable and a float
num2 = 4.0
num2 %= 21
print(num2)    # Output: 4.0

# Example 11: Raising a variable to the power of an integer
num1 = 2
num1 **= 3
print(num1)    # Output: 8

# Example 12: Raising a variable to the power of a float
num2 = 2
num2 **= 3.0
print(num2)    # Output: 8.0

# Example 13: Performing floor division on a variable and an integer
num1 = 21
num1 //= 4
print(num1)    # Output: 5

# Example 14: Performing floor division on a variable and a float
num2 = 21
num2 //= 4.0
print(num2)    # Output: 5.0

# 31. Deletion
# Example 1: Deleting an integer
num1 = 21
del num1

# Example 2: Deleting a float
num2 = 4.0
del num2

# 32. Printing
# Example 1: Printing an integer
num1 = 21
print(num1)    # Output: 21

# Example 2: Printing a float
num2 = 4.0
print(num2)    # Output: 4.0

# 33. Length
# Example 1: Finding the length of an integer
num1 = 21
print(len(str(num1)))    # Output: 2

# Example 2: Finding the length of a float
num2 = 4.0
print(len(str(num2)))    # Output: 3 because of the decimal point

# 34. Iteration
# Example 1: Iterating over an integer
num1 = 21
for i in range(num1):
    print(i)

# Example 2: Iterating over a float
num2 = 4.0
for i in range(int(num2)):
    print(i)

# 35. Indexing
# Example 1: Accessing the first digit of an integer
num1 = 21
print(str(num1)[0])    # Output: 2

# Example 2: Accessing the first digit of a float
num2 = 4.0
print(str(num2)[0])    # Output: 4

# 36. Slicing
# Example 1: Slicing an integer
num1 = 21
print(str(num1)[0:2])    # Output: 21

# Example 2: Slicing a float
num2 = 4.0
print(str(num2)[0:1])    # Output: 4

# 37. Concatenation
# Example 1: Concatenating two integers
num1 = 21
num2 = 4
print(str(num1) + str(num2))    # Output: 214

# Example 2: Concatenating an integer and a float
num1 = 21
num2 = 4.0
print(str(num1) + str(num2))    # Output: 21.04.0

# 38. Repetition
# Example 1: Repeating an integer
num1 = 21
print(str(num1) * 3)    # Output: 212121

# Example 2: Repeating a float
num2 = 4.0
print(str(num2) * 3)    # Output:

# 39. Formatting
# Example 1: Formatting an integer
num1 = 21
print('%d' % num1)    # Output: 21

# Example 2: Formatting a float
num2 = 4.0
print('%f' % num2)    # Output: 4.000000

# 40. Comparison
# Example 1: Comparing two integers
num1 = 21
num2 = 4
print(num1 == num2)    # Output: False

# Example 2: Comparing an integer and a float
num1 = 21
num2 = 4.0
print(num1 == num2)    # Output: False

# 41. Searching
# Example 1: Searching for a substring in an integer
num1 = 21
print('1' in str(num1))    # Output: True

# Example 2: Searching for a substring in a float
num2 = 4.0
print('4' in str(num2))    # Output: True

# 42. Replacement
# Example 1: Replacing a substring in an integer
num1 = 21
print(str(num1).replace('1', '2'))    # Output: 22

# Example 2: Replacing a substring in a float
num2 = 4.0
print(str(num2).replace('4', '5'))    # Output: 5.0

# 43. Splitting
# Example 1: Splitting an integer
num1 = 21
print(str(num1).split('1'))    # Output: ['2', '']

# Example 2: Splitting a float
num2 = 4.0
print(str(num2).split('4'))    # Output: ['', '.0']

# 44. Joining
# Example 1: Joining two integers
num1 = 21
num2 = 4
print(''.join([str(num1), str(num2)]))    # Output: 214

# Example 2: Joining an integer and a float
num1 = 21
num2 = 4.0
print(''.join([str(num1), str(num2)]))    # Output: 21.04.0

# 45. Stripping
# Example 1: Stripping an integer
num1 = 21
print(str(num1).strip('2'))    # Output: 1

# Example 2: Stripping a float
num2 = 4.0
print(str(num2).strip('4'))    # Output: .0

# 46. Justification
# Example 1: Justifying an integer
num1 = 21
print(str(num1).ljust(10, '0'))    # Output: 2100000000

# Example 2: Justifying a float
num2 = 4.0
print(str(num2).ljust(10, '0'))    # Output: 4.00000000

# 47. Centering
# Example 1: Centering an integer
num1 = 21
print(str(num1).center(10, '0'))    # Output: 0002100000
