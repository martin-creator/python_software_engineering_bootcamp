# Exception handling in Python
# It is used to catch errors early and make the code more reliable.
# It helps to handle errors and exceptions in a more controlled way.
# It is used to make the code more robust and reliable.
# The commonn areas where exception handling is used are:
# - File I/O
# - Network I/O
# - Database I/O
# - User input
# - External libraries
# - System calls
#
# Common exceptions in Python
# - ValueError: Raised when a function receives an argument of the correct type but an inappropriate value.
# - TypeError: Raised when an operation or function is applied to an object of an inappropriate type.
# - NameError: Raised when a local or global name is not found.
# - ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
# - FileNotFoundError: Raised when a file or directory is requested but cannot be found.
# - ImportError: Raised when an import statement fails to find the module definition.
# - IndexError: Raised when a sequence subscript is out of range.
# - KeyError: Raised when a dictionary key is not found.
# - AttributeError: Raised when an attribute reference or assignment fails.
# - MemoryError: Raised when an operation runs out of memory.
# - SyntaxError: Raised when the parser encounters a syntax error.
# - IndentationError: Raised when the parser encounters an indentation error.
# - TabError: Raised when the parser encounters a tab character in an indentation-sensitive context.
# - IOError: Raised when an I/O operation fails.
# - PermissionError: Raised when trying to run an operation without the adequate access rights.
# - TimeoutError: Raised when a system function times out.
# - ConnectionError: Raised when a connection to a remote machine is refused.
# - ArithmeticError: Raised when numeric calculations fail.
# - AssertionError: Raised when an assert statement fails.
# - SystemError: Raised when the interpreter finds an internal error.
# - SystemExit: Raised when the interpreter is asked to exit.
# - KeyboardInterrupt: Raised when the user hits the interrupt key (normally Control-C or Delete).
# - Exception: Base class for all exceptions.

# Example 1: Handling ZeroDivisionError
num = 10
try:
    result = num / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")

# Example 2: Handling ValueError
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")

# Example 3: Handling FileNotFoundError
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File not found")

# Example 4: Handling IndexError
try:
    list = [1, 2, 3]
    print(list[3])
except IndexError:
    print("Index out of range")

# Example 5: More complex example of exception handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print(e)

# Example 6: Using else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
else:
    print(result)
finally:
    print("Execution completed")

# The else block is executed if the code in the try block does not raise any exception.
# The finally block is always executed whether an exception is raised or not.
# The above  format is normally used to release resources like file, network, database, etc.
    
# Example 7: Raising exceptions
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number not allowed")
    else:
        print(num)
except ValueError as e:
    print(e)

# Example 8: Custom exception
class MyException(Exception):
    pass

try:
    raise MyException
except MyException:
    print("MyException raised")

# Example 9: Custom exception with message
class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyException("This is a custom exception")
except MyException as e:
    print(e.message)

# Example 10: Using assert statement
num = 10
assert num >= 0, "Number is negative"

# The assert statement is used to check if a condition is True, and if not, it raises an AssertionError with the specified message.

# Example 11: Using assert statement with custom exception
class ValueTooSmallError(Exception):
    pass

num = 10
try:
    assert num >= 0, "Number is negative"
except AssertionError:
    raise ValueTooSmallError("Number is too small")

# The assert statement can be used to raise a custom exception if the condition is not met.

# Example 12: Using assert statement with custom exception and message
class ValueTooSmallError(Exception):
    def __init__(self, message):
        self.message = message

num = 10
try:
    assert num >= 0, "Number is negative"
except AssertionError:
    raise ValueTooSmallError("Number is too small")

# The assert statement can be used to raise a custom exception with a message if the condition is not met.

