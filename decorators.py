# Decorators in python are used to modify the behavior of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
# A decorator works in the following simple steps:
# 1. A function is taken as the input.
# 2. A new function is defined that takes the place of the input function.
# 3. The new function contains the input function and modifies its behavior.
# 4. The new function returns the input function.
# 5. The decorator function is used to add the new functionality to the input function.
# 6. The input function is then called and the new functionality is added to it.
# 
# Common uses of decorators are:
# 1. Logging
# 2. Timing
# 3. Authorization
# 4. Synchronization
# 5. Rate-limiting
# 6. Caching
# 7. Retrying
# 8. Parameter validation
# 9. Debugging
# 10. Deprecation warnings
# 11. Mocking
# 12. Error handling
# 13. Monitoring
# 14. Profiling
# 15. Tracing
# 16. Testing
# 17. Validation
# 18. Wrapping

# Examples of decorator implementation and usage

# Example 1: A simple decorator
# The following example shows how to create a simple decorator that adds functionality to a function. The decorator function takes the input function as an argument and returns a new function that adds the new functionality to the input function.

# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Define a function to be decorated
def say_hello():
    print("Hello!")

# Decorate the function
say_hello = my_decorator(say_hello)

# Another way to decorate the function
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Example 2: A decorator with arguments
# The following example shows how to create a decorator that takes arguments. The decorator function takes the input function as an argument and returns a new function that adds the new functionality to the input function.

# Define a decorator function that takes arguments
def my_decorator_with_args(prefix, suffix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Something is happening before the function is called.")
            func(*args, **kwargs)
            print(f"{suffix}: Something is happening after the function is called.")
        return wrapper
    return decorator

# Define a function to be decorated
@my_decorator_with_args("START", "END")
def say_hello(name):
    print(f"Hello, {name}!")

# Another way to decorate the function
def say_hello(name):
    print(f"Hello, {name}!")
say_hello = my_decorator_with_args("START", "END")(say_hello) # this is IIFE meaning Immediately Invoked Function Expression

# Call the decorated function
say_hello("John")

# Output:
# START: Something is happening before the function is called.
# Hello, John!
# END: Something is happening after the function is called.
