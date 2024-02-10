# Dependency Injection
# Dependency Injection is a technique in which an object receives other objects that it depends on. 
# These other objects are called dependencies. 
# Instead of creating the dependencies inside the object, they are passed to it from the outside.
# It is commonly used to make the code more modular and testable.
# Common parts of the code where dependency injection is used are:
# - Database connections
# - External services
# - Configuration settings
# - Logging
# - Caching
# - Authentication
# - Authorization
# - Email services
# - File storage
# - Error handling
# - Data validation
# - Data serialization
# - Data deserialization
# - Data transformation
# - Data migration

# Example 1: Dependency injection using constructor
class Logger:
    def __init__(self, file):
        self.file = file
        
    def log(self, message):
        self.file.write(message)

class File:
    def write(self, message):
        print(f"Writing to file: {message}")

file = File()
logger = Logger(file)
logger.log("This is a log message")
# Output: Writing to file: This is a log message
# The Logger class depends on the File class. Instead of creating the File object inside the Logger class, it is passed to it from the outside.

# Example 2: Dependency injection using method
class Logger:
    def log(self, message, file):
        file.write(message)

class File:
    def write(self, message):
        print(f"Writing to file: {message}")

file = File()
logger = Logger()
logger.log("This is a log message", file)
# Output: Writing to file: This is a log message
# The Logger class depends on the File class. Instead of creating the File object inside the Logger class, it is passed to it from the outside.


# Example 3: Dependency injection using property
class Logger:
    def log(self, message):
        self.file.write(message)
        
    @property
    def file(self):
        return self._file
    
    @file.setter
    def file(self, value):
        self._file = value

class File:
    def write(self, message):
        print(f"Writing to file: {message}")

file = File()
logger = Logger()
logger.file = file
logger.log("This is a log message")
# Output: Writing to file: This is a log message
# The Logger class depends on the File class. Instead of creating the File object inside the Logger class, it is passed to it from the outside.

# Example 4: Dependency injection using setter method
class Logger:
    def log(self, message):
        self.file.write(message)
        
    def set_file(self, file):
        self._file = file
        
    def get_file(self):
        return self._file

    file = property(get_file, set_file)

class File:
    def write(self, message):
        print(f"Writing to file: {message}")

file = File()
logger = Logger()
logger.file = file
logger.log("This is a log message")
# Output: Writing to file: This is a log message
# The Logger class depends on the File class. Instead of creating the File object inside the Logger class, it is passed to it from the outside.

# Example 5: Dependency injection using dependency injection framework
class Logger:
    def log(self, message):
        self.file.write(message)
        
    def __init__(self, file):
        self.file = file
    
class File:
    def write(self, message):
        print(f"Writing to file: {message}")

file = File()
logger = Logger(file)
logger.log("This is a log message")
# Output: Writing to file: This is a log message
# The Logger class depends on the File class. Instead of creating the File object inside the Logger class, it is passed to it from the outside.