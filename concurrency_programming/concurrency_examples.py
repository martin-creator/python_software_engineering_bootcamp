# Concurrency Programming
# 1. Concurrency Programming
## - Concurrency is the ability of different parts or units of a program, algorithm, or problem to be executed out-of-order or in partial order, without affecting the final outcome.
## - Concurrency is a property of systems in which several computations are executing simultaneously, and potentially interacting with each other.
## - Concurrency is a way to structure a program by breaking it into pieces that can be executed independently.

# 2. Concurrency vs Parallelism
## - Concurrency is about dealing with lots of things at once.
## - Parallelism is about doing lots of things at once.
## - Concurrency is when an application is making progress on more than one task at the same time.
## - Parallelism is when an application is running more than one task at the same time.
## - Concurrency is about structure, parallelism is about execution.
## - Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once.
## - A simple analogy is a chef in a kitchen. Concurrency is like having one chef in the kitchen who is working on multiple dishes at the same time. Parallelism is like having multiple chefs in the kitchen, each working on a different dish at the same time.

# 3. Synchronous vs Asynchronous
## - Synchronous: In a synchronous or blocking operation, the program waits for an I/O operation to complete before moving on to the next task.
## - Asynchronous: In an asynchronous or non-blocking operation, the program does not wait for the I/O operation to complete before moving on to the next task.

# 4. Threading
## - A thread is the smallest unit of processing that can be performed in an OS.
## - A thread is a lightweight process.
## - Threads are used to achieve parallelism.
## - Threads exist within a process.
## - A process can have multiple threads.
## - Threads share the same memory space.
## - Threads are used to achieve parallelism.
## - Threads are used to achieve concurrency.

# 5. Multiprocessing
## - Multiprocessing is a technique in which a computer or CPU has more than two processors.
## - Multiprocessing is the use of two or more central processing units (CPUs) within a single computer system.
## - Multiprocessing is the use of two or more processors (cores) in a single computer system.

# 6. Async IO
## - Async IO is a single-threaded, single-process design that uses non-blocking I/O calls to achieve concurrency.

# Examples of the above concepts are in the concurrency_programming directory using Python's threading, multiprocessing, and async IO libraries.


# Real world applications of the above concepts in the software development:

## Concurrent programming:
### - Web servers and web applications to handle multiple requests at the same time.
### - Databases to handle multiple queries at the same time.
### - Operating systems to handle multiple processes at the same time.

## Threading:
### - Web servers and web applications to handle multiple requests at the same time.
### - Databases to handle multiple queries at the same time.
### - Operating systems to handle multiple processes at the same time.

## Multiprocessing:
### - Web servers and web applications to handle multiple requests at the same time.
### - Databases to handle multiple queries at the same time.
### - Operating systems to handle multiple processes at the same time.

## Async IO:
### - Web servers and web applications to handle multiple requests at the same time.
### - Databases to handle multiple queries at the same time.
### - Operating systems to handle multiple processes at the same time.


# Example of a synchronous program
import time
import requests

urls = ['https://google.com',
        'https://wikipedia.org/wiki/Concurrency',
        'https://python.org',
        'https://pypi.org/project/requests/',
        'https://docs.python.org/3/library/asyncio-task.html',
        'https://www.apple.com/',
        'https://medium.com']

start = time.time()

sync_text_response = []

for url in urls:
    sync_text_response.append(requests.get(url).text)

end_time = time.time()

print('Requests time:', end_time - start)

# Example of an asynchronous program

import asyncio
import time
import requests
import aiohttp


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/requests/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://medium.com']

    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    end_time = time.time()
    print('Async requests time:', end_time - start)


# Example of a program using threading

import threading
import time

def print_numbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        time.sleep(1)
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start() # Start the first thread
t2.start() # Start the second thread

t1.join() # Wait for the first thread to finish
t2.join() # Wait for the second thread to finish

print('Done!')


# Example of a program using multiprocessing

import multiprocessing
import time

def print_numbers():
    for i in range(1, 11):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        time.sleep(1)
        print(letter)

p1 = multiprocessing.Process(target=print_numbers)
p2 = multiprocessing.Process(target=print_letters)

p1.start() # Start the first process
p2.start() # Start the second process

p1.join() # Wait for the first process to finish
p2.join() # Wait for the second process to finish

print('Done!')

# Example of a program using async IO

import asyncio
import time

async def print_numbers():
    for i in range(1, 11):
        await asyncio.sleep(1)
        print(i)

async def print_letters():
    for letter in 'abcdefghij':
        await asyncio.sleep(1)
        print(letter)

async def main():

    await asyncio.gather(print_numbers(), print_letters())
    
    print('Done!')

asyncio.run(main())

# Example of a program using async IO with aiohttp

import aiohttp
import asyncio
import time

async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/requests/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://medium.com']

    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    end_time = time.time()
    print('Async requests time:', end_time - start)


if __name__ == '__main__':
    asyncio.run(main())
    


