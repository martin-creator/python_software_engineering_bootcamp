# Global variables are  variables that are defined outside of functions.

# Global variables can be used by everyone, both inside of functions and outside.

# Example 1: Using a global variable outside a function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Example 2: Using a global variable inside a function
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
# Output: Python is awesome
# The function will print the local x, and then the code will print the global x.

# Example 3: Changing a global variable inside a function
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
# The global keyword makes the variable global.
# Output: fantastic