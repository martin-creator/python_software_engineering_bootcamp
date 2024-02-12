# Requests in Python
#  To send an HTTP request, you can use the requests library.
#  The requests library is the de facto standard for making HTTP requests in Python.
#  It abstracts the complexities of making requests behind a simple API so that you can focus on interacting with services and consuming data in your application.
#  The requests library is not part of the Python standard library, so you need to install it first.
#  You can install the requests library using pip:
#  pip install requests
# examples of free apis we can call for the requests
# 1. https://jsonplaceholder.typicode.com/
# 2. https://api.github.com/
# 3. https://jsonplaceholder.typicode.com/posts
# 4. https://jsonplaceholder.typicode.com/posts/1

# Example 1: Simple Request
# The following example shows a simple request using the requests library.

# requests_examples.py
import requests

def test_simple_request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 2: Request with parameters
# The following example shows a request with parameters using the requests library.
    
# requests_examples.py
def test_request_with_parameters():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 3: Request with headers
# The following example shows a request with headers using the requests library.
    
# requests_examples.py
def test_request_with_headers():
    headers = {
        "Content-Type": "application",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 4: Request with data
# The following example shows a request with data using the requests library.
    
# requests_examples.py
def test_request_with_data():
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
    assert response.status_code == 201
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    

# Example 5: Request with JSON
# The following example shows a request with JSON using the requests library.
    
# requests_examples.py
def test_request_with_json():
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    assert response.status_code == 201
    print(response.json())


# Run the test using the following command:
# pytest requests_examples.py
    
# Example 6: Request with authentication
# The following example shows a request with authentication using the requests library.
    
# requests_examples.py
def test_request_with_authentication():
    response = requests.get("https://api.github.com/user", auth=("username", "password"))
    assert response.status_code != 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 7: Request with cookies
# The following example shows a request with cookies using the requests library.
    
# requests_examples.py
def test_request_with_cookies():
    cookies = {
        "session_id": "12345"
    }
    response = requests.get("https://jsonplaceholder.typicode.com/posts", cookies=cookies)
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    