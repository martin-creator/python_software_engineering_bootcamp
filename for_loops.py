# For loops in Python
# A for loop is used to iterate over a sequence (list, tuple, string, or dictionary). The for loop is used to execute a block of code multiple times. The for loop has the following syntax:
# The for loop has the following syntax:
# for variable in sequence:
#     code block
#
# Real world applocations of for loops:
# 1. To iterate over a list of items
# 2. To iterate over a tuple of items
# 3. To iterate over a string of characters
# 4. To iterate over a dictionary of key-value pairs
# 5. To iterate over a set of items
# 6. To iterate over a range of numbers
# 7. To iterate over a frozen set of items
# 8. To iterate over a file
# 9. To iterate over a generator
# 10. To iterate over a zip object
# 11. To iterate over a enumerate object
# 12. To iterate over a map object
# 13. To iterate over a filter object
# 14. To iterate over a reversed object
# 15. To iterate over a sorted object
# 16. To iterate over a copy of a list
# 17. To iterate over a copy of a tuple

# Example 1: Using a for loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple
# Output: banana
# Output: cherry

# Example 2: Using a for loop to iterate over a tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
# Output: apple
# Output: banana
# Output: cherry
    
# Example 3: Using a for loop to iterate over a string
for char in "apple":
    print(char)
# Output: a
# Output: p
# Output: p
# Output: l
# Output: e
    
# Example 4: Using a for loop to iterate over a dictionary
shop = {
    "name": "John's Grocery",
    "address": "123 Main Street",
    "phone": "555-1234"
}
for key in shop:
    print(key, shop[key])
# Output: name John's Grocery
# Output: address 123 Main Street
# Output: phone 555-1234
    