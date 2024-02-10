# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”.
# These are commonly used for operator overloading.
#
# Examples of most commonly used dunder method, usecases and implementation

# Example 1: __init__ method
# The __init__ method is used to initialize an object.
# It is called when an object of a class is created.
# It is also known as a constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
            
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 25)
person.display()

# Example 2: __str__ method
# The __str__ method is used to return a string representation of an object.
# This method is called when print() or str() function is invoked on an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
            
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person = Person("John", 25)
print(person)
# Output: Name: John, Age: 25

# Example 3: __add__ method
# The __add__ method is used to overload the + operator.
# It is called when the + operator is used on the objects of a class.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def display(self):
        print(f"X: {self.x}, Y: {self.y}")

point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = point1 + point2
point3.display()
# Output: X: 4, Y: 6

# Example 4: __len__ method
# The __len__ method is used to return the length of an object.
# It is called when the built-in len() function is invoked on the object.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
            
    def __len__(self):
        return len(self.numbers)
    
numbers = Numbers([1, 2, 3, 4, 5])
print(len(numbers))
# Output: 5

# Example 5: __getitem__ method
# The __getitem__ method is used to access the item at a given index.
# It is called when the object is indexed using the square bracket.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
            
    def __getitem__(self, index):
        return self.numbers[index]
    
numbers = Numbers([1, 2, 3, 4, 5])
print(numbers[2])
# Output: 3

# Example 6: __setitem__ method
# The __setitem__ method is used to set the value at a given index.
# It is called when the object is indexed using the square bracket.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
            
    def __setitem__(self, index, value):
        self.numbers[index] = value

    def display(self):
        print(self.numbers)

numbers = Numbers([1, 2, 3, 4, 5])
numbers[2] = 6
numbers.display()
# Output: [1, 2, 6, 4, 5]

# Example 7: __delitem__ method
# The __delitem__ method is used to delete the item at a given index.
# It is called when the object is indexed using the square bracket.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
            
    def __delitem__(self, index):
        del self.numbers[index]

    def display(self):
        print(self.numbers)

numbers = Numbers([1, 2, 3, 4, 5])
del numbers[2]
numbers.display()
# Output: [1, 2, 4, 5]

# Example 8: __iter__ method
# The __iter__ method is used to return an iterator object.
# It is called when an iterator is created from the object.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
            
    def __iter__(self):
        return iter(self.numbers)
    
numbers = Numbers([1, 2, 3, 4, 5])
for number in numbers:
    print(number)
# Output: 1
#         2
#         3
#         4
#         5
    
# Example 9: __next__ method
# The __next__ method is used to return the next item from an iterator.
# It is called when the next() function is invoked on an iterator.
    
class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
            
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration
        
numbers = Numbers([1, 2, 3, 4, 5])
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Example 10: __call__ method
# The __call__ method is used to make an object callable.
# It is called when the object is called as a function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
            
    def __call__(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("John", 25)
person()
# Output: Name: John, Age: 25

# Example 11: __eq__ method
# The __eq__ method is used to compare the equality of two objects.
# It is called when the == operator is used on the objects.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)
# Output: True

# Example 12: __lt__ method
# The __lt__ method is used to compare the less than relation of two objects.
# It is called when the < operator is used on the objects.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
point1 = Point(1, 2)
point2 = Point(3, 4)

print(point1 < point2)
# Output: True

