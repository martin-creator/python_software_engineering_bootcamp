# Typing in python is a way to specify the type of a variable, function, or class.
# It helps to catch errors early and makes the code easier to understand.
# The typing module provides a way to specify types in python.

# Examples of typing in python and their usage

# 1. Type hints
# Type hints are used to specify the type of a variable, function, or class.
# They are used to catch errors early and make the code easier to understand.
# The typing module provides a way to specify types in python.

# Example:
from typing import List

def greet(name: str) -> str:
    return f"Hello, {name}"

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# 2. Type aliases
# Type aliases are used to create a new name for an existing type.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import List, Tuple

Vector = List[float]
Point = Tuple[float, float]

def scale_vector(vector: Vector, factor: float) -> Vector:
    return [x * factor for x in vector]

def distance(p1: Point, p2: Point) -> float:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# 3. Generics
# Generics are used to create reusable code that works with different types.
# They are used to make the code more flexible and reusable.

# Example:
from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

# 4. Union types
# Union types are used to specify that a variable can have one of several types.
# They are used to make the code more flexible and easier to understand.

# Example:
from typing import Union

def square_root(x: Union[int, float]) -> float:
    return x**0.5

# 5. Optional types
# Optional types are used to specify that a variable can be None in addition to a specific type.
# They are used to make the code more flexible and easier to understand.

# Example:
from typing import Optional

def get_name(prefix: str, suffix: Optional[str] = None) -> str:
    if suffix is not None:
        return f"{prefix} {suffix}"
    else:
        return prefix
    
# 6. Any type
# The Any type is used to specify that a variable can have any type.
# It is used to make the code more flexible and easier to understand.

# Example:
from typing import Any

def print_value(value: Any) -> None:
    print(value)

# 7. Type checking
# Type checking is the process of verifying that the types specified in the code are correct.
# It is used to catch errors early and make the code more reliable.
    
# Example:
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Type checking can be done using the `mypy` tool, which checks the types in the code and reports any errors.

# 8. Type hints for classes
# Type hints can also be used to specify the types of class attributes and methods.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import List

class ShoppingCart:
    items: List[str]
    
    def __init__(self) -> None:
        self.items = []
        
    def add_item(self, item: str) -> None:
        self.items.append(item)
        
    def get_items(self) -> List[str]:
        return self.items
    
# 9. Type hints for functions
# Type hints can be used to specify the types of function arguments and return values.
# They are used to make the code more readable and easier to understand.
    
# Example:
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# 10. Type hints for modules
# Type hints can be used to specify the types of module-level variables and functions.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import List

items: List[str] = []

def add_item(item: str) -> None:
    items.append(item)

def get_items() -> List[str]:
    return items

# 11. Type hints for built-in types
# Type hints can be used to specify the types of built-in types such as int, float, str, etc.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# 12. Type hints for dictionaries
# Type hints can be used to specify the types of dictionary keys and values.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Dict

def get_value(data: Dict[str, int], key: str) -> int:
    return data[key]

# 13. Type hints for tuples
# Type hints can be used to specify the types of tuple elements.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Tuple

def get_coordinates(point: Tuple[float, float]) -> Tuple[float, float]:
    return point

# 14. Type hints for sets
# Type hints can be used to specify the types of set elements.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Set

def unique_values(data: Set[int]) -> Set[int]:
    return data

# 15. Type hints for iterators
# Type hints can be used to specify the types of iterator elements.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Iterator

def get_first_item(data: Iterator[int]) -> int:
    return next(data)

# 16. Type hints for context managers
# Type hints can be used to specify the types of context manager elements.
# They are used to make the code more readable and easier to understand 
# Simple example of context manager is `open` function in python.

# Example:
from typing import ContextManager

def open_file(filename: str) -> ContextManager:
    return open(filename)


# 17. Type hints for decorators
# Type hints can be used to specify the types of decorator arguments and return values.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Callable

def my_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# 18. Type hints for async functions
# Type hints can be used to specify the types of async function arguments and return values.
# They are used to make the code more readable and easier to understand.

# Example:
from typing import Coroutine

async def my_async_function() -> Coroutine:
    return "Hello, world"



