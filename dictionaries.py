# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
#
# Examples of real world applications of dictionaries:
# 1. To store data in a way that is easy to search
# 2. To store data in a way that is easy to retrieve
# 3. To store data in a way that is easy to update
# 4. To store data in a way that is easy to delete
# 5. To store data in a way that is easy to insert
# 6. To store data in a way that is easy to sort
# 7. To store data in a way that is easy to filter
# 8. To store data in a way that is easy to transform
# 9. To store data in a way that is easy to manipulate
# 10. To store data in a way that is easy to aggregate
# 11. To store data in a way that is easy to compare
# 12. To store data in a way that is easy to validate
# 13. To store data in a way that is easy to serialize
# 14. To store data in a way that is easy to deserialize
# 15. To store data in a way that is easy to persist
# 
# Examples of application features that can be implemented using dictionaries:
# 1. User authentication
# 2. User authorization
# 3. User management
# 4. User roles
# 5. User permissions
# 6. User profiles
# 7. User preferences
# 8. User settings
# 9. User sessions
# 10. User activities
# 11. User history
# 12. User tracking
# 13. User engagement

# Example 1: Creating a dictionary
user = {
    "username": "john_doe",
    "email": "martin@example.com",
    "password": "password123"
}
print(user)    # Output: {'username': 'john_doe', 'email': '

# Example 2: Accessing elements in a dictionary
user = {
    "username": "john_doe",
    "email": "martin@gmailc.om",
    "password": "password123"
}
print(user["username"])    # Output: john_doe

# Example 3: Accessing elements in a dictionary
user = {
    "username": "john_doe",
    "email": "martin@gmail.com",
    "password": "password123"
}
print(user.get("email"))    # Output:

# Example 4: Accessing elements in a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}
print(book["year"])    # Output: 1988

# Example 5: Accessing elements in a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}
print(book.get("author"))    # Output: Paulo Coelho

# Example 6: Resetting the value of a key in a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

book["year"] = 1989
print(book)    # Output: {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'year': 1989}

# Example 7: Adding a new key-value pair to a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

book["publisher"] = "HarperCollins"
print(book)    # Output: {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'year': 1988, 'publisher': 'HarperCollins'}

# Example 8: Removing a key-value pair from a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

del book["year"]
print(book)    # Output: {'title': 'The Alchemist', 'author': 'Paulo Coelho'}

# Example 9: Iterating over a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

for key in book:
    print(key, book[key])
# Output:
# title The Alchemist
# author Paulo Coelho
# year 1988
    
# Example 10: Reverse iterating over a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

for key in reversed(book):
    print(key, book[key])
# Output:
# year 1988
    

# Example 11: Finding the length of a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

print(len(book))    # Output: 3

# Example 12: Filtering a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

filtered_book = {key: book[key] for key in book if key != "year"}
print(filtered_book)    # Output: {'title': 'The Alchemist', 'author': 'Paulo Coelho'}

# Example 13: Checking if a key is in a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

print("year" in book)    # Output: True

# Example 14: Checking if a value is in a dictionary
book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
}

print("Paulo Coelho" in book.values())    # Output: True


