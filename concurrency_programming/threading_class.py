# Creating a thread using the threading class
## The threading class is a class that represents a thread. You can create a thread by creating an instance of the threading class and passing the target function as an argument to the constructor. The target function is the function that the thread will execute. You can also pass arguments to the target function by passing them as arguments to the constructor. The threading class has a start method that starts the thread, and a join method that waits for the thread to finish. Here's an example of how to create a thread using the threading class:
#
## Advantages of using the threading class
## The threading class has several advantages over the threading module. First, it is more object-oriented, which makes it easier to work with. Second, it has a more flexible API, which allows you to create more complex threading scenarios. Finally, it is more powerful, which allows you to create more efficient and scalable threading solutions.
#
## Disadvantages of using the threading class
## The threading class has a few disadvantages. First, it is more complex, which makes it harder to learn and use. Second, it is more error-prone, which makes it more difficult to debug. Finally, it is less portable, which makes it harder to run on different platforms.

import threading
import time

class PrintNumbers(threading.Thread):
    def run(self):
        for i in range(1, 11):
            time.sleep(1)
            print(i)

class PrintLetters(threading.Thread):
    def run(self):
        for letter in 'abcdefghij':
            time.sleep(1)
            print(letter)

t1 = PrintNumbers()
t2 = PrintLetters()

# Start the first thread
t1.start()

# Start the second thread
t2.start()

# Wait for the first thread to finish
t1.join()

# Wait for the second thread to finish
t2.join()

print('Done!')

# Example Advanced Threading Class with arguments and return values

import threading
import time

class PrintNumbers(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self) # Call the constructor of the parent class
        self.name = name
        self.delay = delay

    def run(self): # This method is called when the thread is started
        for i in range(1, 11):
            time.sleep(self.delay)
            print(i)

class PrintLetters(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        for letter in 'abcdefghij':
            time.sleep(self.delay)
            print(letter)


t1 = PrintNumbers('PrintNumbers', 1)
t2 = PrintLetters('PrintLetters', 1)

t1.start()
t2.start()

t1.join()
t2.join()

print('Done!')

