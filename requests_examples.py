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
    

# Asynchronous Requests Vs Synchronous Requests
# 1. Synchronous Requests
#    - In synchronous requests, the client sends a request to the server and waits for the response.
#    - The client cannot perform any other tasks while waiting for the response.
#    - Synchronous requests are blocking, meaning that the client is blocked until the server responds.
# 2. Asynchronous Requests
#    - In asynchronous requests, the client sends a request to the server and continues to perform other tasks while waiting for the response.
#    - The client does not wait for the response and can continue to perform other tasks.
#    - Asynchronous requests are non-blocking, meaning that the client is not blocked while waiting for the server to respond.
#    - Asynchronous requests are useful for improving the performance of web applications by allowing the client to perform other tasks while waiting for the server to respond.
#    - Asynchronous requests are commonly used in web development to improve the responsiveness of web applications and to handle a large number of concurrent requests.
#    - Asynchronous requests can be implemented using various techniques, such as callbacks, promises, and async/await in JavaScript, and coroutines, threads, and event loops in Python.
#    - Asynchronous requests are also used in other programming languages and frameworks to improve the performance of web applications and to handle a large number of concurrent requests.
    
# Example 8: Asynchronous Requests
# The following example shows how to make asynchronous requests using the requests library in Python.
# To make asynchronous requests, you can use the aiohttp library, which provides an asynchronous HTTP client for making requests in Python.
# You can install the aiohttp library using pip:
# pip install aiohttp
    
# requests_examples.py
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def test_asynchronous_requests():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://jsonplaceholder.typicode.com/posts")
        print(html)

# Run the test using the following command:
# pytest requests_examples.py
        
# Conclusion
# The requests library is the de facto standard for making HTTP requests in Python.
# It provides a simple and easy-to-use API for sending requests and handling responses.
# You can use the requests library to interact with web services and consume data in your application.
        
# Example 9: Request with timeout
# The following example shows a request with timeout using the requests library.
# You can specify a timeout for the request using the timeout parameter in the requests library.
# The timeout parameter specifies the maximum time to wait for the server to respond to the request.
# If the server does not respond within the specified timeout, the request will be aborted and an exception will be raised.
# You can specify the timeout in seconds as a float or an integer value.
# The following example shows how to specify a timeout for the request using the timeout parameter in the requests library.
        
# requests_examples.py
def test_request_with_timeout():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=1)
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 10: Request with proxies
# The following example shows a request with proxies using the requests library.
# You can specify a proxy for the request using the proxies parameter in the requests library.
# The proxies parameter specifies the proxy server to use for the request.
    
# requests_examples.py
def test_request_with_proxies():
    proxies = {
        "http": "http://jsonplaceholder.typicode.com",
        "https": "https://jsonplaceholder.typicode.com"
    }

    response = requests.get("https://jsonplaceholder.typicode.com/posts", proxies=proxies)
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 11: Request with SSL verification
# The following example shows a request with SSL verification using the requests library.
# You can specify SSL verification for the request using the verify parameter in the requests library.
# The verify parameter specifies whether to verify the SSL certificate of the server.
# By default, the verify parameter is set to True, which means that the SSL certificate will be verified.
    
# requests_examples.py
def test_request_with_ssl_verification():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", verify=True)
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
# Example 12: Synchrnous Request
# The following example shows a synchronous request using the requests library.
# You can make synchronous requests using the requests library in Python.
# The following example shows how to make a synchronous request using the requests library.
    
# requests_examples.py
def test_synchronous_request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    print(response.json())

# Run the test using the following command:
# pytest requests_examples.py
    
    