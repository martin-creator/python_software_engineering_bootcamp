# Logging in python
# Python has a built-in module called logging to log the output of a program.
# The logging module can be used to log messages to a file, console, or other output streams.
# Logging is particularly useful for debugging and troubleshooting.

# Example 1: Logging to a file
# The basicConfig method is used to configure the logging module.
# It takes several optional arguments to customize the log output.
# The filename argument is used to specify the name of the log file.
# The level argument is used to specify the logging level.
# The format argument is used to specify the format of the log messages.

import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')

logging.info('This is an info message')

logging.warning('This is a warning message')

logging.error('This is an error message')

logging.critical('This is a critical message')

# Example 2: Logging to the console
# By default, the log messages are written to the console.
# The basicConfig method can be used to customize the log output.
# The stream argument is used to specify the output stream.

import logging

logging.basicConfig(stream=open('example.log', 'w'), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')

logging.info('This is an info message')

logging.warning('This is a warning message')

logging.error('This is an error message')

logging.critical('This is a critical message')

# Example 3: Logging to a file and console
# The basicConfig method can be used to log messages to a file and console at the same time.
# The filename argument is used to specify the name of the log file.
# The stream argument is used to specify the output stream.

import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()

console.setLevel(logging.INFO)

console.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.getLogger('').addHandler(console)

logging.debug('This is a debug message')

logging.info('This is an info message')

logging.warning('This is a warning message')

logging.error('This is an error message')

logging.critical('This is a critical message')

# Example 4: Logging to a file and console with different log levels
# The basicConfig method can be used to log messages to a file and console at the same time.
# The filename argument is used to specify the name of the log file.
# The stream argument is used to specify the output stream.

import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()

console.setLevel(logging.INFO)

console.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.getLogger('').addHandler(console)

logging.debug('This is a debug message')

logging.info('This is an info message')

logging.warning('This is a warning message')

logging.error('This is an error message')

logging.critical('This is a critical message')
