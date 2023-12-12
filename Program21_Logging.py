"""
The below program explains about logging module in Python
Log files help us in debugging if something bad happens
Log files also provides statistics of our application
To implement logging Python contains one in-built module called logging

Different logging levels in Python.

    1. CRITICAL => 50
    2. ERROR => 40
    3. WARNING => 30
    4. INFO => 20
    5. DEBUG => 10
    6. NOTSET => 0

If we don't set any log level by default we will get WARNING and above levels added to our program
To implement logging we need to have the file which stores the log info and the level it needs to store
We can implement logging by using basicConfig() function of logging module
logging.basicConfig(filename='log.txt',level=logging.INFO)

After creating log file we can use the below methods to write messages to the log file created
logging.debug(message)
logging.info(message)
logging.warning(message)
logging.error(message)
logging.critical(message)

The process of identifying and fixing the bug is called debugging.
The most common way of debugging is using print statement but after fixing the problem we need to make sure
we remove the statements which were added as part of debugging.

Instead of using print statement for debugging we can use assert statement as we can turn off and turn on assert
statements whenever we want.
There are two types of assert statements in Python.

    1. Simple version
    2. Augmented version
"""

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)  # It will by default create log.txt file
# If the file is already available it will append the data to the file

print('Python logging demo')

logging.debug("This is debug message")  # this methods will write data to the log file we specify
logging.info("This is info message")
logging.critical("This is critical message")
logging.error("This is error message")
logging.warning("This is warning message")

print('A new request came to use our application')
logging.info('A new request came to use our application')
try:
    x = int(input('Enter the first number:'))
    y = int(input('Enter the second number:'))
    print(x/y)
except ZeroDivisionError as msg:
    print('cannot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('Please pass only int values')
    logging.exception(msg)
logging.info('Request processing completed')

# Simple version of assert statement

x = 10
assert x == 10  # since the condition failed we will get assertion error
print('The value of x is:',x)

# Augmented version of assert statement which will display some msg along with AssertionError 

x = 10
assert x > 10, 'Here x value should be greater than 10 but it is not'
print('The value of x is:', x)

# We can turn off assert statements by passing -O option while calling our program
# /Users/dharani-kumar/coding/PythonCodingPractice/venv/bin/python
#   -O /Users/dharani-kumar/coding/PythonCodingPractice/Program21_Logging.py

