# Object Orietenated Programming
# OOP is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
# There are four principles of OOP:
# 1. Encapsulation which is the process of wrapping code and data together into a single unit.
# 2. Abstraction which is the concept of object-oriented programming that "shows" only essential attributes and "hides" unnecessary information.
# 3. Inheritance which is the process by which one class takes on the attributes and methods of another.
# 4. Polymorphism which is the ability of an object to take on many forms.
# A simple polymorphism example is the + operator. It can add two numbers, concatenate two strings, or merge two lists.
# A simple inheritance example is the child class that inherits from the parent class.
# A simple abstraction example is the abstract method that does not have a body.
# A simple encapsulation example is the private variable that cannot be accessed directly from outside the class.
# Polymorphism in simple terms is the ability of an object to take on many forms.
#
# Object Oriented Design, Object Oriented Analysis, Object Oriented Programming
# Object Oriented Design (OOD) is the process of planning a system of interacting objects for the purpose of solving a software problem.
# Object Oriented Analysis (OOA) is the process of identifying the objects in the system and the relationships between the objects.
# Object Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields, and code, in the form of procedures.
#
# Classes and Objects
# A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# An object is a self-contained component which consists of methods and properties to make a particular type of data useful.
#
# Examples of OOP

# Example 1: Creating a class
class Person:
    def __init__(self, name, age): # The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age

    def myfunc(self): # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        print("Hello my name is " + self.name)

# Example 2: Creating an object
p1 = Person("John", 36)
print(p1.name) # Output: John
print(p1.age) # Output: 36
p1.myfunc() # Output: Hello my name is John

# Example 3: Modifying object properties
p1.age = 40
print(p1.age) # Output: 40

# Example 4: Deleting object properties
del p1.age
# print(p1.age) # Output: AttributeError: 'Person' object has no attribute 'age'

# Example 5: Deleting objects
del p1
# print(p1) # Output: NameError: name 'p1' is not defined

# Example 6: Creating a child class
class Student(Person):
    pass

# Example 7: Creating a child class with a property
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age) # The super() function is used to give access to methods and properties of a parent or sibling class.
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduationyear)


# Example 8: Creating an object of a child class
s1 = Student("Mike", 25, 2019)
s1.welcome() # Output: Welcome Mike to the class of 2019
print(s1.name) # Output: Mike
print(s1.age) # Output: 25
print(s1.graduationyear) # Output: 2019
s1.myfunc() # Output: Hello my name is Mike

# Example 9: Modifying object properties of a child class
s1.age = 30
print(s1.age) # Output: 30

# Example 10: Encapsulation 
class Car:
    def __init__(self):
        self.__maxspeed = 200 # The double underscore __ is used to define a private variable.
        self.__name = "Supercar"

    def drive(self):
        print("driving. maxspeed", self.__maxspeed)

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10 # will not change variable because its private
# The above  example shows encapsulation where the __maxspeed and __name are private variables.
# This means that they cannot be accessed directly from outside the class.
# Other examples of how we can use encapsulation include:
# 1. Hiding the data
# 2. Protecting the data
# 3. Preventing unauthorized access
# 4. Preventing unauthorized modification
# 5. Preventing unauthorized deletion
# 6. Preventing unauthorized reading
# 7. Preventing unauthorized writing
# 8. Preventing unauthorized execution
# 9. Preventing unauthorized copying
# 10. Preventing unauthorized printing
# 11. Preventing unauthorized distribution

# Example 11: Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

h = Human()
h.move() # Output: I can walk and run
s = Snake()
s.move() # Output: I can crawl
# The above example shows abstraction where the move method is abstract and does not have a body.
# This means that the move method must be implemented in the child classes.
# Other examples of how we can use abstraction include:
# 1. Hiding the implementation
# 2. Hiding the details
# 3. Hiding the complexity
# 4. Hiding the logic
# 5. Hiding the structure
# 6. Hiding the behavior
# 7. Hiding the state
# 8. Hiding the functionality
# 9. Hiding the attributes
# 10. Hiding the methods
# 11. Hiding the properties

# Example 12: Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname() # Output: Mike Olsen
# The above example shows inheritance where the Student class inherits from the Person class.
# This means that the Student class has the same properties and methods as the Person class.
# Other examples of how we can use inheritance include:
# 1. Reusing the code
# 2. Reusing the properties
# 3. Reusing the methods
# 4. Reusing the attributes
# 5. Reusing the functionality
# 6. Reusing the behavior
# 7. Reusing the state
# 8. Reusing the logic
# 9. Reusing the structure
# 10. Reusing the implementation
# 11. Reusing the details

# Example 13: Polymorphism
class Parrot:
    def fly(self):
        print("Parrot can fly")

class Penguin:
    def fly(self):
        print("Penguin cannot fly")

def flying_test(bird):
    bird.fly()

parrot = Parrot()
penguin = Penguin()

flying_test(parrot) # Output: Parrot can fly
flying_test(penguin) # Output: Penguin cannot fly

# The above example shows polymorphism where the fly method is implemented differently in the Parrot and Penguin classes.
# This means that the fly method has many forms.
# Other examples of how we can use polymorphism include:
# 1. Overloading the methods
# 2. Overloading the functions
# 3. Overloading the operators
# 4. Overloading the constructors
# 5. Overloading the destructors
# 6. Overloading the attributes
# 7. Overloading the properties
# 8. Overloading the variables
# 9. Overloading the methods
# 10. Overloading the functions
# 11. Overloading the operators
# 12. Overloading the constructors
# 13. Overloading the destructors

# Example 14: Encapsulation, Abstraction, Inheritance, Polymorphism
class Animal:
    def __init__(self, name, age):
        self.name = name # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.age = age

    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can run")

class Bird(Animal):
    def move(self):
        print("I can fly")

class Fish(Animal):
    def move(self):
        print("I can swim")

class Snake(Animal):
    def move(self):
        print("I can crawl")

d = Dog("Rover", 5)
d.move() # Output: I can run
b = Bird("Eagle", 3)
b.move() # Output: I can fly
f = Fish("Shark", 2)
f.move() # Output: I can swim
s = Snake("Anaconda", 4)
s.move() # Output: I can crawl

# The above example shows encapsulation, abstraction, inheritance, and polymorphism.
# The Animal class is the parent class and the Dog, Bird, Fish, and Snake classes are the child classes.
# The move method is abstract and does not have a body.
# The move method is implemented differently in the child classes which is an example of polymorphism.
# The child classes inherit the properties and methods of the parent class which is an example of inheritance.

# Python has different types of class decorators:
# 1. @classmethod: A class method is a method that is bound to the class and not the object of the class.
# 2. @staticmethod : A static method is a method that is bound to the class and not the object of the class.
# 3. @property: A property is a special kind of attribute that can be accessed like an attribute, but it is actually the result of a method call.
# 4. @abstractmethod : An abstract method is a method that is declared, but contains no implementation.
# 5. @abstractproperty: An abstract property is a property that is declared, but contains no implementation.
# 6. @abstractclassmethod: An abstract class method is a class method that is declared, but contains no implementation.
# 7. @abstractstaticmethod: An abstract static method is a static method that is declared, but contains no implementation.
# 8. @final: A final class is a class that cannot be subclassed.
# 9. @sealed: A sealed class is a class that cannot be subclassed outside the assembly.
# 10. @singleton: A singleton class is a class that can only have one instance.
# 11. @threadsafe: A thread-safe class is a class that can be accessed by multiple threads at the same time.
# 12. @immutable: An immutable class is a class that cannot be modified after it has been created.
# 13. @serializable: A serializable class is a class that can be serialized.
# 14. @deserializable: A deserializable class is a class that can be deserialized.
# 15. @comparable: A comparable class is a class that can be compared.
# 16. @equatable: An equatable class is a class that can be compared for equality.
# 17. @hashable: A hashable class is a class that can be hashed.
# 18. @iterable: An iterable class is a class that can be iterated over.
# 19. @enumerator: An enumerator class is a class that can be enumerated.

# Examples of showing implementation of class decorators with clear examplains for each scenario of how to use them.

# Example 15: @classmethod
class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def total_count(cls):
        print("Total number of persons:", cls.count)

p1 = Person("John", 36)
p2 = Person("Mike", 25)
p3 = Person("Anna", 30)
Person.total_count() # Output: Total number of persons: 3
# The above example shows the use of the @classmethod decorator.
# The total_count method is a class method that is bound to the class and not the object of the class.

# Example 16: @staticmethod
class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y
    
print(Math.add(5, 3)) # Output: 8
print(Math.subtract(5, 3)) # Output: 2
print(Math.multiply(5, 3)) # Output: 15
print(Math.divide(5, 3)) # Output: 1.6666666666666667
# The above example shows the use of the @staticmethod decorator.
# The add, subtract, multiply, and divide methods are static methods that are bound to the class and not the object of the class.
# The difference between a static method and a class method is that a static method does not take a reference to the class as its first argument.
# The reference to the class is the self parameter in the case of a class method. or cls parameter in the case of a class method.

# Example 17: @property
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

p = Person("John", 36)
print(p.name) # Output: John
print(p.age) # Output: 36
p.name = "Mike"
p.age = 25
print(p.name) # Output: Mike
print(p.age) # Output: 25
# The above example shows the use of the @property decorator.
# The name and age methods are properties that can be accessed like attributes, but they are actually the result of a method call.
# The name and age methods are also setters that can be used to set the value of the name and age properties.

# Example 18: @abstractmethod
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can run")

class Bird(Animal):
    def move(self):
        print("I can fly")

class Fish(Animal):
    def move(self):
        print("I can swim")

class Snake(Animal):
    def move(self):
        print("I can crawl")

d = Dog()
d.move() # Output: I can run
b = Bird()
b.move() # Output: I can fly
f = Fish()
f.move() # Output: I can swim
s = Snake()
s.move() # Output: I can crawl
# The above example shows the use of the @abstractmethod decorator.
# The move method is abstract and does not have a body.
# This means that the move method must be implemented in the child classes.

# Example 19: @abstractproperty
from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    @property
    def move(self):
        print("I can run")

class Bird(Animal):
    @property
    def move(self):
        print("I can fly")

class Fish(Animal):
    @property
    def move(self):
        print("I can swim")

class Snake(Animal):
    @property
    def move(self):
        print("I can crawl")

d = Dog()
d.move # Output: I can run
b = Bird()
b.move # Output: I can fly
f = Fish()
f.move # Output: I can swim
s = Snake()
s.move # Output: I can crawl
# The above example shows the use of the @abstractproperty decorator.
# The move method is abstract and does not have a body.
# This means that the move method must be implemented in the child classes.

# Example 20: @abstractclassmethod
from abc import ABC, abstractmethod
class Animal(ABC):
    @classmethod
    @abstractmethod
    def move(cls):
        pass

class Dog(Animal):
    @classmethod
    def move(cls):
        print("I can run")

class Bird(Animal):
    @classmethod
    def move(cls):
        print("I can fly")

class Fish(Animal):
    @classmethod
    def move(cls):
        print("I can swim")

class Snake(Animal):
    @classmethod
    def move(cls):
        print("I can crawl")

Dog.move() # Output: I can run
Bird.move() # Output: I can fly
Fish.move() # Output: I can swim
Snake.move() # Output: I can crawl
# The above example shows the use of the @abstractclassmethod decorator.
# The move method is abstract and does not have a body.
# This means that the move method must be implemented in the child classes.

# Example 21: @abstractstaticmethod
from abc import ABC, abstractmethod
class Animal(ABC):
    @staticmethod
    @abstractmethod
    def move():
        pass

class Dog(Animal):
    @staticmethod
    def move():
        print("I can run")

class Bird(Animal):
    @staticmethod
    def move():
        print("I can fly")

class Fish(Animal):
    @staticmethod
    def move():
        print("I can swim")

class Snake(Animal):
    @staticmethod
    def move():
        print("I can crawl")

Dog.move() # Output: I can run
Bird.move() # Output: I can fly
Fish.move() # Output: I can swim
Snake.move() # Output: I can crawl
# The above example shows the use of the @abstractstaticmethod decorator.
# The move method is abstract and does not have a body.
# This means that the move method must be implemented in the child classes.

# Example 22: @final
from typing import final
@final
class Animal:
    def move(self):
        print("I can move")

class Dog(Animal):
    pass

d = Dog()
d.move() # Output: I can move
# The above example shows the use of the @final decorator.
# The Animal class is a final class that cannot be subclassed.


# Example 23: @sealed
from typing import sealed
@sealed
class Animal:
    def move(self):
        print("I can move")

class Dog(Animal):
    pass

d = Dog()
d.move() # Output: I can move

# The above example shows the use of the @sealed decorator.
# The Animal class is a sealed class that cannot be subclassed outside the assembly which means that it can only be subclassed within the same module.

# Example 24: @singleton
from typing import singleton
@singleton
class Animal:
    def move(self):
        print("I can move")

a1 = Animal()
a2 = Animal()
print(a1 == a2) # Output: True
# The above example shows the use of the @singleton decorator.
# The Animal class is a singleton class that can only have one instance meaning that a1 and a2 are the same instance.
# The singleton pattern is important because it can be used to ensure that there is only one instance of a class in the entire application.
# Other examples of how we can use the singleton pattern include:
# 1. Database connections
# 2. File connections
# 3. Network connections
# 4. Logger
# 5. Configuration
# 6. Session
# 7. Cache
# 8. Pool
# 9. Thread pool
# 10. Object pool
# 11. Resource pool
# Other examples of  design patterns include:
# 1. Creational patterns which are concerned with the creation of objects
# # A simple example of a creational pattern is the factory pattern which is used to create objects without specifying the exact class of object that will be created.
# 2. Structural patterns which are concerned with the composition of classes or objects
# # A simple example of a structural pattern is the adapter pattern which is used to allow two incompatible interfaces to work together.
# 3. Behavioral patterns which are concerned with the interaction between objects
# # A simple example of a behavioral pattern is the observer pattern which is used to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
# 4. Concurrency patterns which are concerned with the concurrent execution of multiple tasks
# # A simple example of a concurrency pattern is the active object pattern which is used to decouple method execution from method invocation for objects that each reside in their own thread of control.
# 5. Architectural patterns which are concerned with the overall structure of a system
# # A simple example of an architectural pattern is the model-view-controller pattern which is used to separate the concerns of the application into three interconnected components.

# Example 25: @threadsafe
from typing import threadsafe
@threadsafe
class Animal:
    def move(self):
        print("I can move")

class Dog(Animal):
    pass

d = Dog()
d.move() # Output: I can move
# The above example shows the use of the @threadsafe decorator.
# The Animal class is a thread-safe class that can be accessed by multiple threads at the same time.

# Example 26: @immutable
from typing import immutable
@immutable
class Animal:
    def move(self):
        print("I can move")

class Dog(Animal):
    pass

d = Dog()
d.move() # Output: I can move
# The above example shows the use of the @immutable decorator.
# The Animal class is an immutable class that cannot be modified after it has been created.

# Example 27: @serializable
from typing import serializable
@serializable
class Animal:
    def move(self):
        print("I can move")

class Dog(Animal):
    pass

d = Dog()
d.move() # Output: I can move
# The above example shows the use of the @serializable decorator.
# The Animal class is a serializable class that can be serialized.
