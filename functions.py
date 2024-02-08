# Functions are  blocks of code that carry out a specific task and can be used repeatedly in a program.
# Functions are used to organize code into manageable pieces.
# Functions are used to make code reusable.
# Functions are used to make code more readable.
# Functions are used to make code more maintainable.
# Functions are used to make code more testable.
# Functions are used to make code more scalable.
# Functions are used to make code more modular.
# Functions are used to make code more efficient.
# Functions are used to make code more reliable.
# Functions are used to make code more predictable.
# Functions are used to make code more flexible.
# Functions are used to make code more secure.

# Example 1: Creating a function
def greet():
    print("Hello, World!")

greet()
# Output: Hello, World!

# Example 2: Creating a function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output: Hello, Alice!

# Example 3: Creating a function with a return statement
def add(x, y):
    return x + y

result = add(10, 20)
print(result)
# Output: 30

# Example 4: Creating a function with a default parameter
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
# Output: Hello, World!

# Example 5: Creating a function with a variable number of arguments
def add(*args):
    return sum(args)

result = add(10, 20, 30)
print(result)
# Output: 60

# Example 6: Creating a function with a variable number of keyword arguments
def greet(**kwargs):
    print(f"Hello, {kwargs['name']}!")

greet(name="Alice")
# Output: Hello, Alice!

# Example 7: Creating a function with many keyword arguments
def greet(**kwargs):
    print(f"Hello, {kwargs['name']}! You are {kwargs['age']} years old.")

greet(name="Alice", age=10)
# Output: Hello, Alice! You are 10 years old.

# Example 8: Creating a function with a docstring
def greet(name):
    """
    This function greets the user.
    """
    print(f"Hello, {name}!")

greet("Alice")
# Output: Hello, Alice!

