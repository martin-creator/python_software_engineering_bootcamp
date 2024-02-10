# Generators in python are used to create iterators. 
# A generator is a special type of function that returns an iterator.
# It looks like a normal function but contains a yield statement. 
# The yield statement returns the value and saves the state of the function. 
# The next time the function is called, it continues from where it left off.
# This is different from a normal function, which starts from the beginning every time it is called.
# 
# Common use cases for generators are:
# 1. Generating an infinite sequence
# 2. Generating a large sequence of values
# 3. Generating a sequence of values that are expensive to compute
# 4. Generating a sequence of values that are expensive to store
# 5. Generating a sequence of values that are expensive to retrieve
# 6. Generating a sequence of values that are expensive to transmit
# 7. Generating a sequence of values that are expensive to process
# 8. Generating a sequence of values that are expensive to filter
# 9. Generating a sequence of values that are expensive to transform
# 10. Generating a sequence of values that are expensive to sort

# Example 1: A simple generator
# The following example shows how to create a simple generator that returns an iterator. The generator function contains a yield statement, which returns the value and saves the state of the function. The next time the function is called, it continues from where it left off.

# Define a generator function
def my_generator():
    yield 1
    yield 2
    yield 3

# Create an iterator from the generator
iterator = my_generator()

# Iterate over the iterator
for value in iterator:
    print(value)

# Output:
# 1
# 2
# 3
    
# Example 2: A generator with arguments
# The following example shows how to create a generator that takes arguments. The generator function contains a yield statement, which returns the value and saves the state of the function. The next time the function is called, it continues from where it left off.

# Define a generator function with arguments
def my_generator(start, end):
    while start <= end:
        yield start
        start += 1

# Create an iterator from the generator
iterator = my_generator(1, 3)

# Iterate over the iterator
for value in iterator:
    print(value)

# Output:
# 1
# 2
# 3
    