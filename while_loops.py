# While loops are used to execute a block of code repeatedly as long as a condition is true.
# The while loop has the following syntax:
# while condition:
#     code block
#
# Real world applocations of while loops:
# 1. To execute a block of code repeatedly
# 2. To execute a block of code until a condition is met
# 3. To execute a block of code until a condition is false
# 4. To execute a block of code until a condition is true
# 5. To execute a block of code until a condition is satisfied
# 6. To execute a block of code until a condition is not satisfied
# 7. To execute a block of code until a condition is met
# 8. To execute a block of code until a condition is not met
# 

# Example 1: Using a while loop to execute a block of code repeatedly
i = 0
while i < 5:
    print(i)
    i += 1
# Output: 0
# Output: 1
# Output: 2
# Output: 3
# Output: 4
    
# Example 2: Using a while loop to execute a block of code until a condition is met
x = 10
y = 20
while x < y:
    print("x is less than y")
    x += 1
# Output: x is less than y
# Output: x is less than y
# Output: x is less than y
# Output: x is less than y
# Output: x is less than y
# Output: x is less than y
    
# Example 3: Using a while loop to execute a block of code until a condition is false
x = 10
y = 20
while x > y:
    print("x is greater than y")
    x += 1
else:
    print("x is less than y")
# Output: x is less than y


# Example 4: Using a while loop to execute a block of code until a condition is true
x = 10
y = 20
while x < y:
    print("x is less than y")
    x += 1
else:
    print("x is equal to y")


# Output: x is less than y